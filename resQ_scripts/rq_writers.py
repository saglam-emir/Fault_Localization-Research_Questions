"""
rq_writers.py
==============
Turns one target's already-computed pipeline artifacts (Steps 1-4 outputs,
ground truth) into one row per RQ csv. Nothing here re-runs any tool - every
number is read back out of data Steps 1-4 already produced during the
target's single pipeline pass, per the "run exactly once per buggy version"
requirement.

Each RQ csv lives directly under resQ_outputs/ (the task's required output
location) and is upserted (keyed on Project+BugID, see common.upsert_csv_row)
as each target finishes - one row per target no matter how many times or in
what target subset run_pipeline.py is invoked - so a long multi-target run
leaves usable partial results on disk even if a later target fails, without
reruns silently accumulating duplicate rows.
"""

from pathlib import Path

import common

RQ_KEY_FIELDS = ["Project", "BugID"]  # one row per target; reruns upsert on this key, never duplicate

RQ1_FIELDS = ["Project", "BugID", "Pass_TC", "Fail_TC", "Pass_Assert", "Fail_Assert"]
RQ2_FIELDS = ["Project", "BugID", "Full_Execution_Size", "Union_Passing_Slices",
              "Union_Failing_Slices", "Union_All_Slices", "Reduction_Ratio",
              # Same three underlying quantities as Full_Execution_Size/Union_Passing_Slices/
              # Union_Failing_Slices above, appended under the exact column names requested
              # for the paper/doc-facing schema. Kept alongside (not replacing) the original
              # names so nothing already reading those breaks - see _write_rq2's docstring.
              "Statements executed", "Union statements in slices of passing assertions",
              "Union statements in slices of failing assertions"]
# Suffixed with the actual unit each value is computed/rounded in - all four
# time fields are wall-clock seconds (context.Metrics.*_time_sec, timed via
# time.time() in common.run_cmd_timed), Peak_Memory is kilobytes (parsed
# straight from `/usr/bin/time -v`'s "Maximum resident set size (kbytes)" -
# see common.py's _MAX_RSS_RE), never converted to MB/bytes anywhere in the
# pipeline.
RQ3_FIELDS = ["Project", "BugID", "Baseline_Time_(s)", "SBFL_Time_(s)", "Hybrid_Time_(s)",
              "Avg_Slice_Time_(s)", "Peak_Memory_(KB)"]
RQ4_FIELDS = ["Project", "BugID", "Total_Faults", "Included_In_Slice", "Fault_Inclusion_Rate"]
RQ5_FIELDS = ["Project", "BugID", "SBFL_Top_Rank", "Hybrid_Top_Rank", "SBFL_AP", "Hybrid_AP"]
# Kept deliberately separate from rq1-rq5's existing schemas (no columns
# added to those) so nothing already reading them breaks. This is the join
# key any cross-bug aggregate analysis should filter on (WHERE NOT
# Bug_Fully_Unanswerable) before computing "did SBFL/Hybrid find the bug"
# summary stats - see ground_truth.classify_answerability's docstring for
# why a bug can be provably unscoreable by any line-level technique.
RQ0_FIELDS = ["Project", "BugID", "Total_Fault_Lines", "Unanswerable_Fault_Lines", "Bug_Fully_Unanswerable"]


def _write_rq1(ctx, outputs_dir, test_results, assert_counts):
    pass_tc = sum(1 for r in test_results if r["result"] == "PASS")
    fail_tc = sum(1 for r in test_results if r["result"] == "FAIL")
    # Pass_Assert/Fail_Assert are TRUE dynamic assertion-execution counts
    # (loop iterations counted per iteration actually run, short-circuited
    # assertions after a failure correctly excluded because they never ran)
    # - see rq1_dynamic_asserts.compute's docstring. Deliberately NOT Step
    # 1/2's Target Variable Pool, which is a selective slicing-criterion set
    # scoped to RQ2/RQ4/RQ5's needs, not a full assertion-execution count.
    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Pass_TC": pass_tc, "Fail_TC": fail_tc,
           "Pass_Assert": assert_counts["pass_assert"], "Fail_Assert": assert_counts["fail_assert"]}
    common.upsert_csv_row(outputs_dir / "rq1.csv", RQ1_FIELDS, row, key_fields=RQ_KEY_FIELDS)
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
           "Union_All_Slices": len(union_all), "Reduction_Ratio": round(reduction_ratio, 6),
           # Aliases of the three fields above under the doc-facing column names (same
           # values, same sets - see RQ2_FIELDS's comment).
           "Statements executed": full_execution_size,
           "Union statements in slices of passing assertions": len(union_pass),
           "Union statements in slices of failing assertions": len(union_fail)}
    common.upsert_csv_row(outputs_dir / "rq2.csv", RQ2_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def _write_rq3(ctx, outputs_dir):
    m = ctx.metrics
    row = {"Project": ctx.project_id, "BugID": ctx.vid,
           "Baseline_Time_(s)": round(m.baseline_time_sec, 3),
           "SBFL_Time_(s)": round(m.sbfl_time_sec, 3),
           "Hybrid_Time_(s)": round(m.hybrid_time_sec, 3),
           "Avg_Slice_Time_(s)": round(m.avg_slice_time_sec, 3),
           "Peak_Memory_(KB)": round(m.peak_memory_kb, 1)}
    common.upsert_csv_row(outputs_dir / "rq3.csv", RQ3_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def _write_rq4(ctx, outputs_dir, ground_truth_faults, virtual_columns, ochiai_result):
    per_column = ochiai_result["per_column_statements"]
    union_fail = set()
    for row in virtual_columns:
        if row["virtual_status"] == "Virtual_Fail":
            union_fail |= per_column.get(row["virtual_test_id"], set())

    # Match on statement_line (normalized), same convention as
    # step4_ranking.py's AP/rank matching - a multi-line statement's
    # coverage/slice hit lands on its first physical line, not necessarily
    # the diff's edit line (see ground_truth.normalize_statement_line).
    faults = sorted({(Path(f["file"]).name, f.get("statement_line", f["line"])) for f in ground_truth_faults})
    total = len(faults)
    included = sum(1 for f in faults if f in union_fail)
    rate = (included / total) if total else 0.0

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Total_Faults": total,
           "Included_In_Slice": included, "Fault_Inclusion_Rate": round(rate, 6)}
    common.upsert_csv_row(outputs_dir / "rq4.csv", RQ4_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def _write_rq0(ctx, outputs_dir, answerability):
    total = len(answerability) if answerability else 0
    unanswerable = sum(1 for f in answerability if not f["answerable"]) if answerability else 0
    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Total_Fault_Lines": total,
           "Unanswerable_Fault_Lines": unanswerable,
           "Bug_Fully_Unanswerable": bool(total) and unanswerable == total}
    common.upsert_csv_row(outputs_dir / "rq0_answerability.csv", RQ0_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def _write_rq5(ctx, outputs_dir, ranking_result):
    row = {"Project": ctx.project_id, "BugID": ctx.vid,
           "SBFL_Top_Rank": ranking_result["sbfl_top_rank"],
           "Hybrid_Top_Rank": ranking_result["hybrid_top_rank"],
           "SBFL_AP": round(ranking_result["sbfl_ap"], 6),
           "Hybrid_AP": round(ranking_result["hybrid_ap"], 6)}
    common.upsert_csv_row(outputs_dir / "rq5.csv", RQ5_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def write_all(ctx, outputs_dir, *, test_results, assert_counts,
              virtual_columns, ochiai_result, ranking_result, ground_truth_faults, answerability=None):
    rq0 = _write_rq0(ctx, outputs_dir, answerability)
    rq1 = _write_rq1(ctx, outputs_dir, test_results, assert_counts)
    rq2 = _write_rq2(ctx, outputs_dir, virtual_columns, ochiai_result)
    rq3 = _write_rq3(ctx, outputs_dir)
    rq4 = _write_rq4(ctx, outputs_dir, ground_truth_faults, virtual_columns, ochiai_result)
    rq5 = _write_rq5(ctx, outputs_dir, ranking_result)
    ctx.logger.info(f"RQ rows written for {ctx.name}: rq0={rq0} rq1={rq1} rq2={rq2} rq3={rq3} rq4={rq4} rq5={rq5}")
