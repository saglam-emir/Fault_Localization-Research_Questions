"""
step1_tests.py
================
STEP 1 - Test execution + Target Variable Pool construction (assertion-level
Target Pool strategy, see the pipeline's top-level docstring in
run_pipeline.py).

1a. Run the full relevant test suite ONCE with no coverage/tracing
    instrumentation (`defects4j test`) - this is RQ3's Baseline_Time, and
    its `failing_tests` output is Defects4J's own ground truth for which
    tests fail (task requirement: fetch failing tests via defects4j).
1b. Re-run every relevant test individually (`defects4j test -t`) to get a
    clean per-test PASS/FAIL spectrum row (needed for the trace matrix in
    step3, and to know which tests are eligible for step2's passing-test
    scan). This per-test time is charged to the hybrid approach in RQ3,
    since a plain SBFL tool typically needs it too for `defects4j coverage`,
    but the hybrid approach needs it as a prerequisite for slicing.
1c. Target_Pool construction: for every FAILING test, walk its assertions
    top-to-bottom (via java_ast) up to the exact line its own stack-trace
    frame reports as the failure site. Everything before that line is
    `Correct` (JUnit halts at the first failing assertion, so anything
    reached before it held true); the assertion at that line is
    `Incorrect`; anything after never executed and is ignored outright.
"""

import re
import time
from pathlib import Path

import common
import java_ast
import slicer_runner
from context import DEFECTS4J_CMD, TEST_TIMEOUT_SEC

TEST_ANNOTATION_RE = re.compile(r"@Test\b")
METHOD_RE = re.compile(r"(?:public|protected)\s+void\s+(test\w*|[A-Za-z_][A-Za-z0-9_]*)\s*\(")
BLOCK_HEADER_RE = re.compile(r"^--- (\S+)::(\S+)\s*$")


def _relevant_test_classes(ctx):
    out_file = ctx.step1_dir / "_relevant_test_classes.tmp.txt"
    rc, stdout, stderr = common.run_cmd(
        [DEFECTS4J_CMD, "export", "-p", "tests.relevant", "-o", str(out_file)],
        cwd=ctx.checkout_dir, timeout=TEST_TIMEOUT_SEC, logger=ctx.logger,
    )
    if rc != 0 or not out_file.exists():
        common.fail_fast(ctx.logger, f"`defects4j export -p tests.relevant` failed (rc={rc}). stderr={stderr}")
    return [l.strip() for l in out_file.read_text(encoding="utf-8").splitlines() if l.strip()]


def _find_test_methods(test_source_dir: Path, class_name: str, logger):
    src_file = test_source_dir / (class_name.replace(".", "/") + ".java")
    if not src_file.exists():
        logger.warning(f"Test source file not found for {class_name}: {src_file}")
        return []
    text = src_file.read_text(encoding="utf-8", errors="replace")
    methods, pending_test = [], False
    for line in text.splitlines():
        if TEST_ANNOTATION_RE.search(line):
            pending_test = True
            continue
        m = METHOD_RE.search(line)
        if m:
            if pending_test:
                methods.append(m.group(1))
                pending_test = False
            elif m.group(1).startswith("test"):
                methods.append(m.group(1))
    seen, unique = set(), []
    for m in methods:
        if m not in seen:
            seen.add(m)
            unique.append(m)
    return unique


def _persist_and_restore_failure_snapshot(ctx, restore_only=False):
    failing_file = ctx.checkout_dir / "failing_tests"
    snapshot_file = ctx.step1_dir / "full_suite_failing_tests.txt"
    if restore_only:
        if snapshot_file.exists():
            failing_file.write_text(snapshot_file.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
        return ""
    if not failing_file.exists():
        return ""
    content = failing_file.read_text(encoding="utf-8", errors="replace")
    snapshot_file.write_text(content, encoding="utf-8")
    return content


def _run_full_suite(ctx):
    """RQ3 Baseline_Time: one untraced `defects4j test` run. Also the
    ground-truth failing-test snapshot the Target Variable Pool is built
    from.
    """
    logger = ctx.logger
    logger.info("Running full test suite via `defects4j test` (baseline, untraced)...")
    rc, stdout, stderr, elapsed, peak_kb = common.run_cmd_timed(
        [DEFECTS4J_CMD, "test"], cwd=ctx.checkout_dir, timeout=TEST_TIMEOUT_SEC * 4, logger=logger,
    )
    ctx.metrics.baseline_time_sec = elapsed
    ctx.metrics.note_memory(peak_kb)
    if rc != 0:
        logger.warning(f"`defects4j test` returned rc={rc} (expected if tests fail). stderr tail: {stderr[-500:]}")

    content = _persist_and_restore_failure_snapshot(ctx)
    _persist_and_restore_failure_snapshot(ctx, restore_only=True)
    failing = {line.replace("---", "").strip() for line in content.splitlines() if line.startswith("---")}
    logger.info(f"Baseline run: {elapsed:.1f}s, ground-truth failing tests ({len(failing)}): {sorted(failing)}")
    return failing


def _run_single_test(ctx, test_id: str):
    rc, stdout, stderr = common.run_cmd([DEFECTS4J_CMD, "test", "-t", test_id], cwd=ctx.checkout_dir,
                                         timeout=TEST_TIMEOUT_SEC, logger=ctx.logger)
    failing_file = ctx.checkout_dir / "failing_tests"
    result = "PASS"
    if failing_file.exists() and failing_file.read_text(encoding="utf-8", errors="replace").strip():
        result = "FAIL"
    if rc != 0 and result == "PASS":
        ctx.logger.warning(f"{test_id}: rc={rc} without a failing_tests entry; stderr tail: {stderr[-300:]}")
        result = "FAIL"
    _persist_and_restore_failure_snapshot(ctx, restore_only=True)
    return result


def _find_failure_line(block_text: str, test_class: str, test_method: str):
    frame_re = re.compile(re.escape(f"at {test_class}.{test_method}(") + r"([^:)]+):(\d+)\)")
    m = frame_re.search(block_text)
    return (m.group(1), int(m.group(2))) if m else (None, None)


def run(ctx):
    """Returns {"test_results": [...], "target_pool": [...], "passed_variable_matches_precursor": target_variables}."""
    logger = ctx.logger

    ground_truth_failing = _run_full_suite(ctx)

    test_classes = _relevant_test_classes(ctx)
    test_source_dir = slicer_runner.get_test_source_dir(ctx.checkout_dir, ctx.step1_dir, logger)

    per_test_start = time.time()
    rows = []
    for class_name in test_classes:
        methods = _find_test_methods(test_source_dir, class_name, logger)
        for method in methods:
            test_case = f"{class_name}::{method}"
            result = _run_single_test(ctx, test_case)
            in_ground_truth = test_case in ground_truth_failing
            if (result == "FAIL") != in_ground_truth:
                logger.warning(f"Discrepancy for {test_case}: isolated={result}, full-suite-failing={in_ground_truth}")
            rows.append({"test_id": len(rows) + 1, "test_class": class_name, "test_method": method,
                         "test_case": test_case, "result": result})
    ctx.metrics.hybrid_extra_time_sec += time.time() - per_test_start

    if not rows:
        common.fail_fast(logger, "No tests were discovered/executed.")

    common.write_csv(ctx.step1_dir / "test_results.csv",
                      ["test_id", "test_class", "test_method", "test_case", "result"], rows)
    failing_rows = [r for r in rows if r["result"] == "FAIL"]
    common.write_csv(ctx.step1_dir / "failing_tests.csv",
                      ["test_id", "test_class", "test_method", "test_case", "result"], failing_rows)
    logger.info(f"Step1: {len(rows)} test(s) executed ({len(failing_rows)} FAIL, {len(rows) - len(failing_rows)} PASS).")

    # --- Target Variable Pool -------------------------------------------
    snapshot_file = ctx.step1_dir / "full_suite_failing_tests.txt"
    content = snapshot_file.read_text(encoding="utf-8", errors="replace") if snapshot_file.exists() else ""
    blocks, current_key, current_lines = {}, None, []
    for line in content.splitlines():
        m = BLOCK_HEADER_RE.match(line)
        if m:
            if current_key is not None:
                blocks[current_key] = "\n".join(current_lines)
            current_key, current_lines = (m.group(1), m.group(2)), []
        elif current_key is not None:
            current_lines.append(line)
    if current_key is not None:
        blocks[current_key] = "\n".join(current_lines)

    pool_rows, pool_id = [], 0
    for (test_class, test_method), block_text in blocks.items():
        test_case = f"{test_class}::{test_method}"
        source_file_name, fail_line = _find_failure_line(block_text, test_class, test_method)
        if fail_line is None:
            logger.warning(f"{test_case}: no stack-trace frame for the test method itself; skipping.")
            continue
        src_file = test_source_dir / (test_class.replace(".", "/") + ".java")
        assertions = java_ast.parse_assertions_in_method(src_file, test_method, max_line=fail_line)
        if not assertions:
            logger.warning(f"{test_case}: no assertX(...) calls found up to line {fail_line}.")
            continue
        for a in assertions:
            status = "Incorrect" if a["line"] == fail_line else "Correct"
            if not a["variable"]:
                continue
            pool_id += 1
            pool_rows.append({"pool_id": pool_id, "test_case": test_case, "test_class": test_class,
                               "test_method": test_method, "source_file": source_file_name, "line": a["line"],
                               "assert_type": a["assert_type"], "raw_expression": a["raw_expression"],
                               "variable": a["variable"], "status": status})

    common.write_csv(
        ctx.step1_dir / "target_variable_pool.csv",
        ["pool_id", "test_case", "test_class", "test_method", "source_file", "line",
         "assert_type", "raw_expression", "variable", "status"],
        pool_rows,
    )
    if not pool_rows:
        # Legitimate outcome, not a pipeline defect: it means every failing
        # test's own failure line was never an assertX(...) call (e.g. the
        # bug throws an exception from application code before any
        # assertion is reached). There is nothing to build slicing criteria
        # from, but RQ1 (test-level counts) is still perfectly answerable,
        # so downstream steps run on an empty pool instead of aborting the
        # whole target - they degrade to empty slices/rankings gracefully.
        logger.warning(
            "Target Variable Pool is empty (no failing test's own failure line coincided with an "
            "assertX(...) call - likely a non-assertion exception). Continuing with an empty pool; "
            "RQ2-RQ5 will reflect that no slicing criteria exist for this bug."
        )
    logger.info(f"Step1: Target Variable Pool has {len(pool_rows)} row(s) "
                f"({len([r for r in pool_rows if r['status'] == 'Correct'])} Correct, "
                f"{len([r for r in pool_rows if r['status'] == 'Incorrect'])} Incorrect).")

    return {"test_results": rows, "target_pool": pool_rows}
