"""
rq_writers.py
==============
Turns one target's already-computed pipeline artifacts (Steps 1-4 outputs,
ground truth) into one row per RQ csv. Nothing here re-runs any tool - every
number is read back out of data Steps 1-4 already produced during the
target's single pipeline pass, per the "run exactly once per buggy version"
requirement.

Each RQ csv lives directly under resQ_outputs/ (the task's required output
location) and is appended to as each target finishes, so a long multi-target
run leaves usable partial results on disk even if a later target fails.
"""

from pathlib import Path

import common

RQ1_FIELDS = ["Project", "BugID", "Pass_TC", "Fail_TC", "Pass_Assert", "Fail_Assert"]
RQ2_FIELDS = ["Project", "BugID", "Full_Execution_Size", "Union_Passing_Slices",
              "Union_Failing_Slices", "Union_All_Slices", "Reduction_Ratio"]
RQ3_FIELDS = ["Project", "BugID", "Baseline_Time", "SBFL_Time", "Hybrid_Time", "Avg_Slice_Time", "Peak_Memory"]
RQ4_FIELDS = ["Project", "BugID", "Total_Faults", "Included_In_Slice", "Fault_Inclusion_Rate"]
RQ5_FIELDS = ["Project", "BugID", "SBFL_Top_Rank", "Hybrid_Top_Rank", "SBFL_AP", "Hybrid_AP"]


def _write_rq1(ctx, outputs_dir, test_results, target_pool, passed_variable_matches):
    pass_tc = sum(1 for r in test_results if r["result"] == "PASS")
    fail_tc = sum(1 for r in test_results if r["result"] == "FAIL")
    # Pass_Assert = "Correct" assertions from failing tests (evaluated
    # before the failure) + the selectively-filtered assertions from
    # passing tests that matched the Target Variable Pool.
    pass_assert = sum(1 for r in target_pool if r["status"] == "Correct") + len(passed_variable_matches)
    fail_assert = sum(1 for r in target_pool if r["status"] == "Incorrect")

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Pass_TC": pass_tc, "Fail_TC": fail_tc,
           "Pass_Assert": pass_assert, "Fail_Assert": fail_assert}
    common.append_csv_row(outputs_dir / "rq1.csv", RQ1_FIELDS, row)
    return row


def _write_rq2(ctx, outputs_dir, virtual_columns, ochiai_result):
    full_execution_size = len(ochiai_result["trace_universe"])
    per_column = ochiai_result["per_column_statements"]
    # per_column_statements is captured before step3's bracket-only-line
    # filtering; intersect with the slice matrix's own (already-filtered)
    # statement universe so Union_All_Slices always matches what the slice
    # matrix/ranking actually scored, and Reduction_Ratio is apples-to-apples
    # against Full_Execution_Size (also bracket-only-filtered).
    slice_universe = set(ochiai_result["slice_universe"])

    union_pass, union_fail = set(), set()
    for row in virtual_columns:
        stmts = per_column.get(row["virtual_test_id"], set()) & slice_universe
        if row["virtual_status"] == "Virtual_Pass":
            union_pass |= stmts
        else:
            union_fail |= stmts
    union_all = union_pass | union_fail

    reduction_ratio = (1 - (len(union_all) / full_execution_size)) if full_execution_size else 0.0

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Full_Execution_Size": full_execution_size,
           "Union_Passing_Slices": len(union_pass), "Union_Failing_Slices": len(union_fail),
           "Union_All_Slices": len(union_all), "Reduction_Ratio": round(reduction_ratio, 6)}
    common.append_csv_row(outputs_dir / "rq2.csv", RQ2_FIELDS, row)
    return row


def _write_rq3(ctx, outputs_dir):
    m = ctx.metrics
    row = {"Project": ctx.project_id, "BugID": ctx.vid,
           "Baseline_Time": round(m.baseline_time_sec, 3),
           "SBFL_Time": round(m.sbfl_time_sec, 3),
           "Hybrid_Time": round(m.hybrid_time_sec, 3),
           "Avg_Slice_Time": round(m.avg_slice_time_sec, 3),
           "Peak_Memory": round(m.peak_memory_kb, 1)}
    common.append_csv_row(outputs_dir / "rq3.csv", RQ3_FIELDS, row)
    return row


def _write_rq4(ctx, outputs_dir, ground_truth_faults, virtual_columns, ochiai_result):
    per_column = ochiai_result["per_column_statements"]
    union_fail = set()
    for row in virtual_columns:
        if row["virtual_status"] == "Virtual_Fail":
            union_fail |= per_column.get(row["virtual_test_id"], set())

    faults = sorted({(Path(f["file"]).name, f["line"]) for f in ground_truth_faults})
    total = len(faults)
    included = sum(1 for f in faults if f in union_fail)
    rate = (included / total) if total else 0.0

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Total_Faults": total,
           "Included_In_Slice": included, "Fault_Inclusion_Rate": round(rate, 6)}
    common.append_csv_row(outputs_dir / "rq4.csv", RQ4_FIELDS, row)
    return row


def _write_rq5(ctx, outputs_dir, ranking_result):
    row = {"Project": ctx.project_id, "BugID": ctx.vid,
           "SBFL_Top_Rank": ranking_result["sbfl_top_rank"],
           "Hybrid_Top_Rank": ranking_result["hybrid_top_rank"],
           "SBFL_AP": round(ranking_result["sbfl_ap"], 6),
           "Hybrid_AP": round(ranking_result["hybrid_ap"], 6)}
    common.append_csv_row(outputs_dir / "rq5.csv", RQ5_FIELDS, row)
    return row


def write_all(ctx, outputs_dir, *, test_results, target_pool, passed_variable_matches,
              virtual_columns, ochiai_result, ranking_result, ground_truth_faults):
    rq1 = _write_rq1(ctx, outputs_dir, test_results, target_pool, passed_variable_matches)
    rq2 = _write_rq2(ctx, outputs_dir, virtual_columns, ochiai_result)
    rq3 = _write_rq3(ctx, outputs_dir)
    rq4 = _write_rq4(ctx, outputs_dir, ground_truth_faults, virtual_columns, ochiai_result)
    rq5 = _write_rq5(ctx, outputs_dir, ranking_result)
    ctx.logger.info(f"RQ rows written for {ctx.name}: rq1={rq1} rq2={rq2} rq3={rq3} rq4={rq4} rq5={rq5}")
