#!/usr/bin/env python3
"""
run_pipeline.py
================
Main entry point. For each of the 4 target buggy versions in targets.py,
runs the full assertion-level hybrid SBFL pipeline EXACTLY ONCE and, from
that single pass, derives the data for all 5 RQs:

    Step 1  Test execution (untraced baseline + per-test) + Target Variable
            Pool construction (RQ1 raw data)
    Step 2  Dynamic slicing: failing-test criteria + selective passing-test
            criteria -> virtual test columns (RQ2/RQ3/RQ4 raw data)
    Step 3  Trace matrix (traditional SBFL baseline) + slice matrix
            (hybrid) + Ochiai scoring for both
    Step 4  Ranking with tie-break (r_worst) + Average Precision (RQ5)
    RQ     Append one row per target to rq1.csv..rq5.csv under resQ_outputs/

Each target is isolated: a fatal error in one target's pipeline (raised as
common.StepFailure) is caught and logged, and the remaining targets still
run - one bad checkout should not blank out the other 3 targets' results.

Usage
-----
    python3 run_pipeline.py                  # all 4 targets
    python3 run_pipeline.py Csv_3b            # just one target (by name)
"""

import sys
import time
from pathlib import Path

import common
import ground_truth
import rq_writers
import step1_tests
import step2_slicing
import step3_matrices
import step4_ranking
from context import RunContext
from targets import TARGETS

RESQ_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = RESQ_ROOT / "resQ_outputs"
LOG_DIR = OUTPUTS_DIR / "logs"
WORK_DIR = OUTPUTS_DIR / "work"

top_logger = common.setup_logger("run_pipeline", LOG_DIR)


def run_one_target(target: dict) -> bool:
    name = target["name"]
    logger = common.setup_logger(f"target.{name}", LOG_DIR)
    ctx = RunContext(
        name=name, project_id=target["project_id"], bug_id=target["bug_id"], variant=target["variant"],
        checkout_dir=Path(target["checkout_dir"]), work_dir=WORK_DIR / name, logger=logger,
    )

    if not ctx.checkout_dir.exists():
        logger.error(f"Checkout directory missing for {name}: {ctx.checkout_dir}. Skipping.")
        return False

    logger.info("=" * 70)
    logger.info(f"TARGET {name}  (project={ctx.project_id}, vid={ctx.vid})  checkout={ctx.checkout_dir}")
    logger.info("=" * 70)

    start = time.time()
    try:
        step1_out = step1_tests.run(ctx)
        step2_out = step2_slicing.run(ctx, step1_out["test_results"], step1_out["target_pool"])
        step3_out = step3_matrices.run(ctx, step1_out["test_results"], step2_out["virtual_columns"])
        gt_faults = ground_truth.load_ground_truth_faults(ctx.project_id, ctx.bug_id, logger)
        step4_out = step4_ranking.run(ctx, step3_out, gt_faults)

        rq_writers.write_all(
            ctx, OUTPUTS_DIR,
            test_results=step1_out["test_results"],
            target_pool=step1_out["target_pool"],
            passed_variable_matches=step2_out["passed_variable_matches"],
            virtual_columns=step2_out["virtual_columns"],
            ochiai_result=step3_out,
            ranking_result=step4_out,
            ground_truth_faults=gt_faults,
        )
    except common.StepFailure as e:
        logger.error(f"TARGET {name} stopped safely after a fatal step error: {e}")
        return False
    except Exception:
        logger.exception(f"TARGET {name} crashed with an unexpected error.")
        return False

    logger.info(f"TARGET {name} COMPLETE in {time.time() - start:.1f}s")
    return True


def main():
    names = set(sys.argv[1:])
    targets = [t for t in TARGETS if not names or t["name"] in names]
    if not targets:
        top_logger.error(f"No matching targets for {sorted(names)}; available: {[t['name'] for t in TARGETS]}")
        sys.exit(1)

    top_logger.info(f"Running pipeline for {len(targets)} target(s): {[t['name'] for t in targets]}")
    results = {t["name"]: run_one_target(t) for t in targets}

    top_logger.info("=" * 70)
    for name, ok in results.items():
        top_logger.info(f"  {'OK  ' if ok else 'FAIL'}  {name}")
    top_logger.info(f"RQ csv files written to: {OUTPUTS_DIR}")
    top_logger.info("=" * 70)

    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
