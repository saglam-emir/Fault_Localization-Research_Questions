"""
step4_ranking.py
==================
STEP 4 - Ranking (RQ5: SBFL vs. Hybrid fault-localization performance).

Ranking uses standard competition ranking ("1-2-2-4"): statements tied on
ochiai_score all receive the same rank - the `rank` (== r_best, the
best/top position of that tied group). Each row also carries `tie_size`, so
the group's `r_worst = rank + tie_size - 1` (the task's tie-breaking
formula) is always derivable.

Average Precision (RQ5), per the task's formula
`AP = sum(P@rank(d_i)) / |Relevant|`:
  - `Relevant` = the ground-truth faulty statements (from ground_truth.py),
    deduplicated by (file, line).
  - `rank(d_i)` uses r_worst (the pessimistic/worst-case position within a
    tied group) - the only tie-break rule the task specifies, so it is used
    consistently everywhere a single rank number is needed for a tied
    ground-truth statement.
  - `P@k = (# Relevant statements ranked within the first k positions) / k`.
    Because tied statements share one `rank` value equal to their group's
    r_best, and a later group's rank is always > any earlier group's
    r_worst, "rows with rank <= k" is exactly the first k ranked positions
    whenever k itself is some group's r_worst - which is always true here
    since k is always taken as some d_i's own r_worst.
  - A ground-truth statement absent from the ranking entirely (never
    covered/sliced by any test) contributes P=0 to the sum.

`*_Top_Rank` (SBFL_Top_Rank / Hybrid_Top_Rank) reports the best (minimum)
r_best among the ground-truth statements that do appear in the ranking -
the earliest position a real fault is first encountered while reading down
the list. If no ground-truth statement appears in the ranking at all, it is
reported as one past the last ranked statement (worse than everything).
"""

from pathlib import Path

import common


def build_ranking(scores, mapping_rows, logger, label):
    mapping_by_id = {r["statement_id"]: r for r in mapping_rows}
    enriched, dropped = [], []
    for row in scores:
        mapping = mapping_by_id.get(row["statement_id"])
        if mapping is None:
            dropped.append(row["statement_id"])
            continue
        enriched.append({
            "statement_id": row["statement_id"], "file": mapping["file"],
            "line": int(mapping["line"]), "code": mapping["code"],
            "ochiai_score": float(row["ochiai_score"]),
        })
    if dropped:
        logger.warning(f"{label}: dropped {len(dropped)} statement_id(s) absent from mapping: {sorted(dropped)}")

    enriched.sort(key=lambda r: (-r["ochiai_score"], r["file"], r["line"]))

    ranked, i, n = [], 0, len(enriched)
    while i < n:
        j = i
        while j < n and enriched[j]["ochiai_score"] == enriched[i]["ochiai_score"]:
            j += 1
        rbest, tie_size = i + 1, j - i
        for row in enriched[i:j]:
            ranked.append({**row, "rank": rbest, "tie_size": tie_size, "r_worst": rbest + tie_size - 1})
        i = j
    return ranked


def average_precision_and_top_rank(ranked, ground_truth_faults, logger, label):
    """ground_truth_faults: [{"file": <basename>, "line": int}, ...]."""
    relevant = sorted({(f["file"], f["line"]) for f in ground_truth_faults})
    if not relevant:
        return 0.0, ""

    by_pos = {(r["file"], r["line"]): r for r in ranked}
    relevant_ranks = sorted(by_pos[k]["rank"] for k in relevant if k in by_pos)
    missing = [k for k in relevant if k not in by_pos]
    if missing:
        logger.info(f"{label}: {len(missing)}/{len(relevant)} ground-truth statement(s) not present "
                    f"in this ranking (never covered/sliced): {missing}")

    ap_terms = []
    for key in relevant:
        row = by_pos.get(key)
        if row is None:
            ap_terms.append(0.0)
            continue
        k = row["r_worst"]
        hits_within_k = sum(1 for rk in relevant_ranks if rk <= k)
        ap_terms.append(hits_within_k / k)
    ap = sum(ap_terms) / len(relevant)

    if relevant_ranks:
        top_rank = min(relevant_ranks)
    elif ranked:
        # The ranking exists but contains none of the ground-truth
        # statements - "worse than every ranked statement" is a meaningful,
        # comparable sentinel.
        top_rank = len(ranked) + 1
    else:
        # Nothing was ranked at all (e.g. every dynamic slice came back
        # empty) - there is no rank to report, not even a worst-case one.
        top_rank = ""
    return ap, top_rank


def _write_ranking_csv(path, ranked):
    common.write_csv(path, ["rank", "statement_id", "file", "line", "code", "ochiai_score", "tie_size", "r_worst"], ranked)


def _write_answerability_csv(path, answerability):
    common.write_csv(path, ["file", "line", "approx", "answerable"], answerability)


def run(ctx, ochiai_result, ground_truth_faults, answerability=None):
    """`answerability`: ground_truth.classify_answerability's output, same
    order as `ground_truth_faults` (None if the caller didn't compute it -
    kept optional so this function still works standalone/pre-Step-2).
    """
    logger = ctx.logger
    # Matching uses `statement_line` (the enclosing statement's first line,
    # per ground_truth.normalize_statement_line) - coverage/slice tools
    # report a multi-line statement's hit on that same first line, so
    # matching on the raw diff line would mismatch a genuine hit by however
    # many lines the statement spans (verified concretely on Csv-13's
    # CSVFormat.java: diff line 319, statement/coverage line 318). `line`
    # (the original, un-normalized diff line) is kept only for the summary
    # header's human-readable display, never for matching.
    gt = [{"file": Path(f["file"]).name, "line": f.get("statement_line", f["line"])} for f in ground_truth_faults]
    gt_display = [(Path(f["file"]).name, f["line"]) for f in ground_truth_faults]
    line_shifts = {(Path(f["file"]).name, f["line"]): f.get("statement_line", f["line"])
                   for f in ground_truth_faults if f.get("statement_line", f["line"]) != f["line"]}

    trace_ranked = build_ranking(ochiai_result["trace_scores"], ochiai_result["trace_mapping"], logger, "trace (SBFL)")
    slice_ranked = build_ranking(ochiai_result["slice_scores"], ochiai_result["slice_mapping"], logger, "slice (hybrid)")

    _write_ranking_csv(ctx.step4_dir / "trace_ranking.csv", trace_ranked)
    _write_ranking_csv(ctx.step4_dir / "slice_ranking.csv", slice_ranked)

    trace_ap, trace_top = average_precision_and_top_rank(trace_ranked, gt, logger, "trace (SBFL)")
    slice_ap, slice_top = average_precision_and_top_rank(slice_ranked, gt, logger, "slice (hybrid)")

    bug_fully_unanswerable = bool(answerability) and all(not f["answerable"] for f in answerability)
    if answerability is not None:
        _write_answerability_csv(ctx.step4_dir / "ground_truth_answerability.csv", answerability)

    summary = ["# Ranking Comparison Summary", "",
               f"Ground truth faulty statement(s) (diff line): {gt_display}", ""]
    if line_shifts:
        summary += [f"Statement-line-normalized for matching (multi-line statement, first-line "
                    f"attribution - see ground_truth.normalize_statement_line): "
                    f"{[(f, diff_ln, '->', stmt_ln) for (f, diff_ln), stmt_ln in line_shifts.items()]}", ""]
    if answerability is not None:
        unanswerable = [(f["file"], f["line"]) for f in answerability if not f["answerable"]]
        summary += [f"Ground_Truth_Answerable: {not bug_fully_unanswerable}"]
        if unanswerable:
            summary += [f"Unanswerable fault line(s) (dead code in the buggy build - see "
                        f"ground_truth_answerability.csv): {unanswerable}"]
        summary += [""]
    if bug_fully_unanswerable:
        summary += ["> **WARNING**: every ground-truth fault line for this bug is an approximate "
                     "pure-deletion anchor that never executed in any test (dead code in the buggy "
                     "build, not a wrong-but-live statement - typically an entire deleted method). No "
                     "line-level SBFL or slicing technique can find this by construction. The top "
                     "rank/AP numbers below are not a meaningful measure of either technique's "
                     "capability for this bug and should be excluded from primary cross-bug scoring "
                     "(see rq0_answerability.csv).", ""]
    summary += [f"- SBFL   top rank: {trace_top}, AP: {trace_ap:.4f}",
               f"- Hybrid top rank: {slice_top}, AP: {slice_ap:.4f}", ""]
    if ochiai_result.get("slice_universe_empty"):
        summary += ["> **WARNING**: the hybrid slice matrix's statement universe was empty for this "
                     "target (every virtual column's dynamic slice was empty or test-code-only). The "
                     "Hybrid numbers above reflect a slicing failure, not a genuine 0%/rank-1 result - "
                     "see step2_slicing's log and step3_matrices/slice_matrix_status.csv.", ""]
    if ochiai_result.get("slice_fail_side_empty"):
        summary += ["> **WARNING**: every Virtual_Fail column covers zero statements in the slice "
                     "universe (only passing-test slices contributed). Every statement therefore "
                     "scores Ochiai=0.0 and ties for rank 1 - Hybrid top rank/AP above are a "
                     "degenerate tie-break artifact, not genuine localization - see "
                     "step3_matrices/slice_matrix_status.csv.", ""]
    for title, ranked in (("Trace-Based SBFL", trace_ranked), ("Slice-Based Hybrid", slice_ranked)):
        summary += [f"## Top 10 - {title}", "", "| Rank | Tie Size | File:Line | Ochiai | Code |",
                    "|------|----------|-----------|--------|------|"]
        for row in ranked[:10]:
            summary.append(f"| {row['rank']} | {row['tie_size']} | {row['file']}:{row['line']} | "
                            f"{row['ochiai_score']} | `{row['code']}` |")
        summary.append("")
    (ctx.step4_dir / "ranking_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    logger.info(f"Step4: SBFL top_rank={trace_top} AP={trace_ap:.4f} | Hybrid top_rank={slice_top} AP={slice_ap:.4f}")

    return {
        "trace_ranked": trace_ranked, "slice_ranked": slice_ranked,
        "sbfl_top_rank": trace_top, "hybrid_top_rank": slice_top,
        "sbfl_ap": trace_ap, "hybrid_ap": slice_ap,
        "bug_fully_unanswerable": bug_fully_unanswerable,
    }
