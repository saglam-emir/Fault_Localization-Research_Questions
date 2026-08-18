#!/usr/bin/env python3
"""
rerun_ranking.py
==================
Ranking-only re-entry point. Steps 2 (answerability) and 3 (line
normalization) of the correction roadmap only change how ground-truth
lines are interpreted/matched - they never change what got executed,
sliced, or scored into Step 3's matrices. Re-running the full
Steps 1-3 pipeline (defects4j + Slicer4J, tens of minutes per target) just
to pick up a ground-truth-matching change would be slow AND methodologically
noisier than necessary (it reintroduces test/JVM run-to-run variance into a
change that has nothing to do with test execution).

This script instead reloads each target's already-persisted Step 3 CSVs
from disk and re-runs only Step 4 (ranking) + the ground-truth-dependent RQ
rows (rq0/rq4/rq5 - rq1/rq2/rq3 do not depend on ground truth at all and are
left untouched). No defects4j or Slicer4J call is made.

Usage
-----
    python3 rerun_ranking.py                  # all 4 targets
    python3 rerun_ranking.py Csv_3b            # just one target (by name)

Requires that target's resQ_outputs/work/<name>/step2_slicing and
step3_matrices already exist on disk (i.e. Steps 1-3 have run at least once
under some version of the pipeline).
"""

import sys
from pathlib import Path

import common
import ground_truth
import rq_writers
import step3_matrices
import step4_ranking
from context import RunContext
from targets import TARGETS

RESQ_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = RESQ_ROOT / "resQ_outputs"
LOG_DIR = OUTPUTS_DIR / "logs"
WORK_DIR = OUTPUTS_DIR / "work"


def _bool(raw, default=False):
    if raw is None or raw == "":
        return default
    return str(raw).strip().lower() == "true"


def rerun_one_target(target: dict) -> bool:
    name = target["name"]
    logger = common.setup_logger(f"rerank.{name}", LOG_DIR)
    ctx = RunContext(
        name=name, project_id=target["project_id"], bug_id=target["bug_id"], variant=target["variant"],
        checkout_dir=Path(target["checkout_dir"]), work_dir=WORK_DIR / name, logger=logger,
    )

    trace_mapping = common.read_csv(ctx.step3_dir / "trace_statement_mapping.csv")
    trace_scores = common.read_csv(ctx.step3_dir / "trace_ochiai_scores.csv")
    slice_mapping = common.read_csv(ctx.step3_dir / "slice_statement_mapping.csv")
    slice_scores = common.read_csv(ctx.step3_dir / "slice_ochiai_scores.csv")
    virtual_columns = common.read_csv(ctx.step2_dir / "virtual_columns.csv")

    if not trace_mapping or not trace_scores:
        logger.error(f"{name}: no persisted Step 3 trace matrix found under {ctx.step3_dir} - "
                     f"run the full pipeline (run_pipeline.py {name}) at least once first. Skipping.")
        return False

    trace_universe = [(r["file"], int(r["line"])) for r in trace_mapping]
    slice_universe = [(r["file"], int(r["line"])) for r in slice_mapping]

    per_column_statements = {
        vtid: step3_matrices._load_slice_statements(ctx, vtid)
        for vtid in sorted({r["virtual_test_id"] for r in virtual_columns})
    }

    status_rows = common.read_csv(ctx.step3_dir / "slice_matrix_status.csv")
    if status_rows:
        slice_universe_empty = _bool(status_rows[0].get("is_empty"), default=not slice_universe)
        slice_fail_side_empty = _bool(status_rows[0].get("fail_side_empty"))
    else:
        # Pre-fix runs never wrote this file (see step3_matrices.py history) -
        # fall back to recomputing the same "empty universe" check directly;
        # fail_side_empty can't be reconstructed without re-running Step 3
        # (it needs Virtual_Fail ids, which virtual_columns.csv does have -
        # recompute it exactly the same way build_slice_matrix does).
        slice_universe_empty = not slice_universe
        universe_set = set(slice_universe)
        fail_ids = [r["virtual_test_id"] for r in virtual_columns if r["virtual_status"] == "Virtual_Fail"]
        slice_fail_side_empty = bool(fail_ids) and not slice_universe_empty and all(
            not (per_column_statements.get(vtid, set()) & universe_set) for vtid in fail_ids
        )
        logger.info(f"{name}: no slice_matrix_status.csv on disk (pre-fix run); recomputed "
                    f"is_empty/fail_side_empty directly instead of trusting a stale/missing file.")

    ochiai_result = {
        "trace_mapping": trace_mapping, "trace_scores": trace_scores, "trace_universe": trace_universe,
        "slice_mapping": slice_mapping, "slice_scores": slice_scores, "slice_universe": slice_universe,
        "per_column_statements": per_column_statements,
        "slice_universe_empty": slice_universe_empty,
        "slice_fail_side_empty": slice_fail_side_empty,
    }

    gt_faults = ground_truth.load_ground_truth_faults(ctx.project_id, ctx.bug_id, logger, ctx.checkout_dir)
    answerability = ground_truth.classify_answerability(gt_faults, trace_universe, logger)
    ranking_result = step4_ranking.run(ctx, ochiai_result, gt_faults, answerability)

    # Only the ground-truth-dependent RQ rows are recomputed here - rq1
    # (test/assertion counts) and rq3 (timing) never touch ground truth at
    # all, and rq2 (slice reduction stats) doesn't either; re-deriving them
    # from disk would be redundant work that also risks silently drifting
    # from what the full pipeline run actually measured (e.g. RQ3's timing
    # is a live measurement, not something to fabricate from a re-run).
    rq0 = rq_writers._write_rq0(ctx, OUTPUTS_DIR, answerability)
    rq4 = rq_writers._write_rq4(ctx, OUTPUTS_DIR, gt_faults, virtual_columns, ochiai_result)
    rq5 = rq_writers._write_rq5(ctx, OUTPUTS_DIR, gt_faults, ranking_result)
    logger.info(f"{name}: ranking-only re-run complete. rq0={rq0} rq4={rq4} rq5={rq5}")
    return True


def main():
    names = set(sys.argv[1:])
    targets = [t for t in TARGETS if not names or t["name"] in names]
    if not targets:
        print(f"No matching targets for {sorted(names)}; available: {[t['name'] for t in TARGETS]}")
        sys.exit(1)

    results = {t["name"]: rerun_one_target(t) for t in targets}
    print("=" * 70)
    for name, ok in results.items():
        print(f"  {'OK  ' if ok else 'FAIL'}  {name}")
    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
