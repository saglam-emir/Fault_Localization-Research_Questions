"""
step4_ranking.py
==================
STEP 4 - Ranking (RQ5: SBFL vs. Hybrid fault-localization performance).

Ranking uses standard competition ranking ("1-2-2-4"): statements tied on
ochiai_score all receive the same rank - the `rank` (== r_best, the
best/top position of that tied group). Each row also carries `tie_size`, so
the group's `r_worst = rank + tie_size - 1` (the task's tie-breaking
formula) is always derivable.

Average Precision is deliberately NOT computed in this module (removed by
request - AP is now computed externally, off rq5.csv's per-fault-line
rank_best_*/tie_size_* columns, which together give every r_worst an
external AP formula needs; see rq_writers._write_rq5's docstring). This
module's job ends at producing the ranked lists (trace_ranked/slice_ranked)
- rq_writers.py reads rank/tie_size straight off them, no re-derivation.
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

    # Diagnostic only (no AP/rank math - see module docstring): which
    # ground-truth statements this matrix's ranking doesn't contain at all
    # (never covered/sliced by anything). rq5.csv carries the authoritative,
    # per-fault-line version of this (RQ5_MISSING cells).
    relevant = sorted({(f["file"], f["line"]) for f in gt})
    for label, ranked in (("trace (SBFL)", trace_ranked), ("slice (hybrid)", slice_ranked)):
        by_pos = {(r["file"], r["line"]) for r in ranked}
        missing = [k for k in relevant if k not in by_pos]
        if missing:
            logger.info(f"{label}: {len(missing)}/{len(relevant)} ground-truth statement(s) not present "
                        f"in this ranking (never covered/sliced): {missing}")

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
                     "line-level SBFL or slicing technique can find this by construction. The rank_best "
                     "values in rq5.csv for this bug are not a meaningful measure of either technique's "
                     "capability and should be excluded from primary cross-bug scoring "
                     "(see rq0_answerability.csv).", ""]
    summary += [f"- SBFL   ranked {len(trace_ranked)} statement(s)",
               f"- Hybrid ranked {len(slice_ranked)} statement(s)", ""]
    if ochiai_result.get("slice_universe_empty"):
        summary += ["> **WARNING**: the hybrid slice matrix's statement universe was empty for this "
                     "target (every virtual column's dynamic slice was empty or test-code-only). Any "
                     "rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing "
                     "failure, not a genuine result - see step2_slicing's log and "
                     "step3_matrices/slice_matrix_status.csv.", ""]
    if ochiai_result.get("slice_fail_side_empty"):
        summary += ["> **WARNING**: every Virtual_Fail column covers zero statements in the slice "
                     "universe (only passing-test slices contributed). Every statement therefore "
                     "scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this "
                     "bug is a degenerate tie-break artifact, not genuine localization - see "
                     "step3_matrices/slice_matrix_status.csv.", ""]
    for title, ranked in (("Trace-Based SBFL", trace_ranked), ("Slice-Based Hybrid", slice_ranked)):
        summary += [f"## Top 10 - {title}", "", "| Rank | Tie Size | File:Line | Ochiai | Code |",
                    "|------|----------|-----------|--------|------|"]
        for row in ranked[:10]:
            summary.append(f"| {row['rank']} | {row['tie_size']} | {row['file']}:{row['line']} | "
                            f"{row['ochiai_score']} | `{row['code']}` |")
        summary.append("")
    (ctx.step4_dir / "ranking_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    logger.info(f"Step4: SBFL ranked {len(trace_ranked)} statement(s) | "
                f"Hybrid ranked {len(slice_ranked)} statement(s) (AP no longer computed here - see rq5.csv)")

    return {
        "trace_ranked": trace_ranked, "slice_ranked": slice_ranked,
        "bug_fully_unanswerable": bug_fully_unanswerable,
    }
