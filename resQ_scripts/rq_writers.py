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
              # Pass_TC_Slices/Fail_TC_Slices are a GENUINELY DIFFERENT grouping from
              # Union_Passing_Slices/Union_Failing_Slices above, not aliases of them - see
              # _write_rq2's docstring for the exact distinction (source-test-case-outcome
              # grouping vs assertion-outcome grouping) and why they can diverge.
              "Pass_TC_Slices", "Fail_TC_Slices"]
# Suffixed with the actual unit each value is computed/rounded in - all four
# time fields are wall-clock seconds (context.Metrics.*_time_sec, timed via
# time.time() in common.run_cmd_timed), Peak_Memory is kilobytes (parsed
# straight from `/usr/bin/time -v`'s "Maximum resident set size (kbytes)" -
# see common.py's _MAX_RSS_RE), never converted to MB/bytes anywhere in the
# pipeline.
RQ3_FIELDS = ["Project", "BugID", "Baseline_Time_(s)", "SBFL_Time_(s)", "Hybrid_Time_(s)",
              "Avg_Slice_Time_(s)", "Peak_Memory_(KB)"]
RQ4_FIELDS = ["Project", "BugID", "Total_Faults", "Included_In_Slice", "Fault_Inclusion_Rate",
              # Fail_Assert_Count/Not_All_Faulty_Stmts_In_Slice/No_Faulty_Stmts_In_Slice are
              # computed ENTIRELY from virtual_columns/Target Pool data (see _write_rq4) -
              # deliberately independent of rq1.csv's Fail_Assert (rq1_dynamic_asserts.py's
              # static assertion-count mechanism), which answers a different question. Never
              # import or reference that module/value here.
              "Fail_Assert_Count", "Not_All_Faulty_Stmts_In_Slice", "No_Faulty_Stmts_In_Slice"]
# One row per (bug, ground-truth fault LINE), not per bug - a bug with N fault
# lines produces N consecutive rows. Column names are lowercase/underscored by
# deliberate one-off request, unlike every other RQ csv's PascalCase/Title_Case
# schema - not a typo. RQ5_KEY_FIELDS (not the shared RQ_KEY_FIELDS) is required
# because "Project"+"BugID" alone is no longer a unique row key - see
# _write_rq5's docstring.
RQ5_FIELDS = ["project", "bug_id", "file_name", "line_no",
              "rank_best_trace", "tie_size_trace", "rank_best_slice", "tie_size_slice"]
RQ5_KEY_FIELDS = ["project", "bug_id", "file_name", "line_no"]
# Written into rank_best_*/tie_size_* when a fault line is absent from that
# matrix's ranking entirely (never covered/sliced) - a literal, unambiguous
# marker distinct from both a real numeric rank and an empty/blank cell (see
# _write_rq5's docstring for why 0 is wrong here too).
RQ5_MISSING = "None"
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
    # Pass_Assert/Fail_Assert are STATIC assertX(...) call-site counts (one
    # assertion = one potential slice, never a per-loop-iteration execution
    # count) - see rq1_dynamic_asserts.compute's docstring. Fail_Assert
    # reuses Step 1's Target Pool Incorrect rows as-is (so it can never
    # disagree with what Step 2 actually sliced on); Pass_Assert adds every
    # PASSING test's own full assertion set on top of the Target Pool's
    # Correct rows, deliberately wider than Step 2's 2b/2c selective
    # passing-test scan (which only keeps assertions whose variable matches
    # something already in the Target Pool - a slicing-criterion subset,
    # not a full per-test assertion count).
    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Pass_TC": pass_tc, "Fail_TC": fail_tc,
           "Pass_Assert": assert_counts["pass_assert"], "Fail_Assert": assert_counts["fail_assert"]}
    common.upsert_csv_row(outputs_dir / "rq1.csv", RQ1_FIELDS, row, key_fields=RQ_KEY_FIELDS)
    return row


def _write_rq2(ctx, outputs_dir, test_results, virtual_columns, ochiai_result):
    full_execution_size = len(ochiai_result["trace_universe"])
    per_column = ochiai_result["per_column_statements"]
    # per_column_statements is captured before step3's bracket-only-line
    # filtering; intersect with the slice matrix's own (already-filtered)
    # statement universe so Union_All_Slices always matches what the slice
    # matrix/ranking actually scored, and Reduction_Ratio is apples-to-apples
    # against Full_Execution_Size (also bracket-only-filtered).
    slice_universe = set(ochiai_result["slice_universe"])

    # Union_Passing_Slices/Union_Failing_Slices: grouped by whether the
    # virtual column's SOURCE TEST CASE - taken as a whole, per Step 1's
    # test_results - passed or failed. This reuses only Step 1's plain
    # per-test PASS/FAIL, already computed and passed in for RQ1 anyway;
    # deliberately independent of RQ1's own static assertion-count
    # mechanism (rq1_dynamic_asserts.py) - see that module's docstring on
    # why it stays decoupled from Step 2's virtual-column methodology.
    tc_result = {r["test_case"]: r["result"] for r in test_results}
    tc_pass, tc_fail = set(), set()
    for row in virtual_columns:
        stmts = per_column.get(row["virtual_test_id"], set()) & slice_universe
        outcome = tc_result.get(row["test_case"])
        if outcome == "PASS":
            tc_pass |= stmts
        elif outcome == "FAIL":
            tc_fail |= stmts
        else:
            ctx.logger.warning(f"RQ2: virtual column {row['virtual_test_id']!r}'s source test case "
                                f"{row['test_case']!r} has no Step 1 test_results entry; excluded from "
                                f"Union_Passing_Slices/Union_Failing_Slices (should not happen - every "
                                f"virtual column is built from either a failing or a passing Step 1 test).")
    union_all = tc_pass | tc_fail

    reduction_ratio = (1 - (len(union_all) / full_execution_size)) if full_execution_size else 0.0

    # Pass_TC_Slices/Fail_TC_Slices: a DIFFERENT grouping of the same
    # per-column statement sets, by the OUTCOME OF THE ASSERTION ITSELF
    # (virtual_status), not by its source test case's outcome above.
    # Virtual_Pass means this exact criterion evaluated true at runtime;
    # Virtual_Fail means it is the one assertion whose failure ended the
    # test. A single FAILING test contributes BOTH: every assertion JUnit
    # reached before the failure line is individually "Correct"/
    # Virtual_Pass (see step1_tests.py's Target Variable Pool construction,
    # status="Correct"/"Incorrect"), and only the one at the failure line
    # is Virtual_Fail. Every virtual column Step 2 built from a passing
    # test's assertion scan (2b/2c) is trivially Virtual_Pass AND from a
    # passing test case, so it agrees with Union_Passing_Slices either way.
    # The two groupings can only diverge on virtual columns Step 2 built
    # from a FAILING test's Target Pool rows (2a): a "Correct"/Virtual_Pass
    # assertion drawn from an otherwise-FAILING test counts toward
    # Pass_TC_Slices here (its own outcome is Virtual_Pass), but toward
    # Union_Failing_Slices above, since its source test still failed.
    assertion_pass, assertion_fail = set(), set()
    for row in virtual_columns:
        stmts = per_column.get(row["virtual_test_id"], set()) & slice_universe
        if row["virtual_status"] == "Virtual_Pass":
            assertion_pass |= stmts
        else:
            assertion_fail |= stmts

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Full_Execution_Size": full_execution_size,
           "Union_Passing_Slices": len(tc_pass), "Union_Failing_Slices": len(tc_fail),
           "Union_All_Slices": len(union_all), "Reduction_Ratio": round(reduction_ratio, 6),
           "Pass_TC_Slices": len(assertion_pass), "Fail_TC_Slices": len(assertion_fail)}
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
    # slice_universe intersection added for consistency with the actual
    # (slice) observation matrix / RQ2's Union_Failing_Slices: per_column
    # (ochiai_result["per_column_statements"]) is captured BEFORE Step 3b's
    # bracket-only-line filtering, so without this intersection union_fail
    # could contain statements that never appear as a column in
    # slice_observation_matrix.csv (i.e. were never actually scored/ranked).
    # slice_observation_matrix.csv's own cell values are defined as exactly
    # "statement in per_column[virtual_test_id], for statement in
    # sorted(slice_universe)" (see step3_matrices.build_slice_matrix), so
    # this intersection reproduces the matrix's own membership test exactly
    # - not a re-read of the CSV file (redundant I/O for identical data
    # already in memory), but the same underlying definition.
    slice_universe = set(ochiai_result["slice_universe"])
    union_fail = set()
    for row in virtual_columns:
        if row["virtual_status"] == "Virtual_Fail":
            union_fail |= per_column.get(row["virtual_test_id"], set()) & slice_universe

    # Match on statement_line (normalized), same convention as
    # step4_ranking.py's rank matching - a multi-line statement's
    # coverage/slice hit lands on its first physical line, not necessarily
    # the diff's edit line (see ground_truth.normalize_statement_line).
    faults = sorted({(Path(f["file"]).name, f.get("statement_line", f["line"])) for f in ground_truth_faults})
    total = len(faults)
    included = sum(1 for f in faults if f in union_fail)
    rate = (included / total) if total else 0.0

    # Fail_Assert_Count: count of Virtual_Fail virtual columns (Step 2's
    # failing-assertion slicing criteria) that fed union_fail above -
    # computed ENTIRELY from virtual_columns/Target Pool data, deliberately
    # NOT rq1.csv's Fail_Assert (rq1_dynamic_asserts.py's independent
    # static assertion-count mechanism - see RQ4_FIELDS's comment). Provides the
    # "how many failing-assertion criteria contributed" context for
    # Included_In_Slice/Fault_Inclusion_Rate above.
    fail_assert_count = sum(1 for row in virtual_columns if row["virtual_status"] == "Virtual_Fail")

    # Not_All_Faulty_Stmts_In_Slice: ground truth ⊄ slice (at least one
    # fault statement missing from union_fail). No_Faulty_Stmts_In_Slice:
    # ground truth ∩ slice = ∅ (none of them are). Both are deterministic
    # functions of included/total above (not independent data), kept as
    # explicit columns for readability/filtering. With an empty ground
    # truth (total==0) both are forced False rather than the vacuously-true
    # set-theory answer for "none in slice" (∅∩X=∅) - there is nothing to
    # check, so asserting "none of the faults are covered" would be
    # misleading, not merely technically true.
    not_all_faulty_stmts_in_slice = (included < total) if total else False
    no_faulty_stmts_in_slice = (included == 0) if total else False

    row = {"Project": ctx.project_id, "BugID": ctx.vid, "Total_Faults": total,
           "Included_In_Slice": included, "Fault_Inclusion_Rate": round(rate, 6),
           "Fail_Assert_Count": fail_assert_count,
           "Not_All_Faulty_Stmts_In_Slice": not_all_faulty_stmts_in_slice,
           "No_Faulty_Stmts_In_Slice": no_faulty_stmts_in_slice}
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


def _write_rq5(ctx, outputs_dir, ground_truth_faults, ranking_result):
    """One row per ground-truth fault LINE (not one row per bug - see
    RQ5_FIELDS's comment). rank_best_*/tie_size_* are read directly off
    step4_ranking.build_ranking()'s already-computed trace_ranked/
    slice_ranked lists (ranking_result) - no ranking math happens here, and
    nothing is re-derived from the raw matrices, per the approved plan.
    AP is deliberately NOT computed here anymore (approved for deletion -
    see step4_ranking.py); this file carries exactly the rank_best/tie_size
    data an external AP computation needs (rank_best + tie_size together
    give r_worst = rank_best + tie_size - 1, the task's tie-break rule).

    Matches ground-truth faults against the ranked lists on the NORMALIZED
    statement_line (see ground_truth.normalize_statement_line), the same
    convention step4_ranking.run() and RQ4 already use - trace_ranked/
    slice_ranked's own "line" field is the coverage/slice tools' bytecode
    line-number-table convention, so matching on the raw diff line would
    silently miss any multi-line-statement fault the technique actually did
    find (verified concretely on Csv-13: diff line 319, statement line
    318). file_name/line_no below are therefore this normalized statement
    line, not the raw patch line.

    A fault line absent from a given ranking (never covered/sliced by
    anything in that matrix) gets RQ5_MISSING ("None") in that ranking's
    two cells - not 0 (0 would misrepresent it as "found at the very best
    rank") and not blank (ambiguous with a genuinely empty/unset cell).
    """
    trace_by_pos = {(r["file"], r["line"]): r for r in ranking_result["trace_ranked"]}
    slice_by_pos = {(r["file"], r["line"]): r for r in ranking_result["slice_ranked"]}

    faults = sorted({(Path(f["file"]).name, f.get("statement_line", f["line"])) for f in ground_truth_faults})

    rows = []
    for file_name, line_no in faults:
        t = trace_by_pos.get((file_name, line_no))
        s = slice_by_pos.get((file_name, line_no))
        row = {
            "project": ctx.project_id, "bug_id": ctx.vid, "file_name": file_name, "line_no": line_no,
            "rank_best_trace": t["rank"] if t else RQ5_MISSING,
            "tie_size_trace": t["tie_size"] if t else RQ5_MISSING,
            "rank_best_slice": s["rank"] if s else RQ5_MISSING,
            "tie_size_slice": s["tie_size"] if s else RQ5_MISSING,
        }
        common.upsert_csv_row(outputs_dir / "rq5.csv", RQ5_FIELDS, row, key_fields=RQ5_KEY_FIELDS)
        rows.append(row)
    return rows


def write_all(ctx, outputs_dir, *, test_results, assert_counts,
              virtual_columns, ochiai_result, ranking_result, ground_truth_faults, answerability=None):
    rq0 = _write_rq0(ctx, outputs_dir, answerability)
    rq1 = _write_rq1(ctx, outputs_dir, test_results, assert_counts)
    rq2 = _write_rq2(ctx, outputs_dir, test_results, virtual_columns, ochiai_result)
    rq3 = _write_rq3(ctx, outputs_dir)
    rq4 = _write_rq4(ctx, outputs_dir, ground_truth_faults, virtual_columns, ochiai_result)
    rq5 = _write_rq5(ctx, outputs_dir, ground_truth_faults, ranking_result)
    ctx.logger.info(f"RQ rows written for {ctx.name}: rq0={rq0} rq1={rq1} rq2={rq2} rq3={rq3} rq4={rq4} rq5={rq5}")
