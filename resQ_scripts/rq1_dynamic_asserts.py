"""
rq1_dynamic_asserts.py
========================
RQ1's Pass_Assert/Fail_Assert as TRUE dynamic assertion-EXECUTION counts -
not a static source-level call-site count, and deliberately NOT Step 1/2's
Target Variable Pool (target_pool/passed_variable_matches), which answers a
different question by design: "which assertions do we need as Slicer4J
backward-slicing criteria" (a selective set, scoped to what Steps 2-5 need -
see step1_tests.py/step2_slicing.py's own docstrings). This module answers
"of every assertX(...) call any test in the suite actually executed at
runtime, how many held true and how many threw?" - loop iterations counted
once per iteration actually executed, and anything after a short-circuiting
failure correctly excluded because it never ran at all.

Mechanism
---------
Slicer4J's own instrumentation already produces, as a byproduct of every
backward slice it runs, a full bytecode-level dynamic execution trace
(`trace.log_icdg.log` - one row per instruction actually executed, in real
execution order, with a fresh row per occurrence, so a loop iterating N
times produces N rows for the same source line). This module never reads
the *slice* those calls produced (raw-slice.log/slice.log) - only the trace
underneath it - so it is entirely independent of, and never modifies,
Step 2's Target-Pool/virtual-column slicing methodology that RQ2/RQ4/RQ5
depend on.

For a test Step 2 already sliced at least once (every failing test - it
always contributes >=1 Target Pool row; any passing test whose assertion
matched the Target Pool), that trace already exists on disk at zero extra
cost - read back from Step 2's own failing_slice_metadata.csv/
passed_slice_metadata.csv. For a passing test Step 2 never sliced (the
large majority - its assertions never matched the Target Pool), one new
Slicer4J run is issued purely to obtain its trace, seeded on any one of that
test's own assertions (which one doesn't matter: Slicer4J's `run()` phase
executes the WHOLE instrumented test regardless of the backward criterion -
the criterion only controls what its OWN `-m s` slice step would extract,
which this module ignores). `_trace_only_attempt` deliberately bypasses
slicer_runner._slicer4j_attempt for these throwaway runs so they are NOT
folded into ctx.metrics: RQ3 measures the hybrid approach's own slicing
overhead, and trace-only runs are extra work only RQ1's assertion count
needs, not part of that methodology. Their output lives under
ctx.step2_dir/_assert_trace_only/, never read by anything RQ2/4/5 touches.

Classification, read straight off the trace in real execution order:
  - Passing test: every dynamic hit on one of the test's own assertion
    source lines is a Pass - the test finished clean, so nothing it
    executed could have thrown.
  - Failing test: every hit is a Pass EXCEPT the chronologically LAST one,
    which is the Fail - the trace itself physically stops there, because
    that is the exact bytecode instruction whose AssertionError propagated
    and ended the method. Assertions written after it in source never
    executed under a short-circuiting failure and, by construction, never
    produce a trace row - no separate "ignore assertions after the failure
    line" rule is needed; the trace already reflects what actually ran.
"""

import re
from pathlib import Path

import common
import java_ast
import slicer_runner
from context import SLICER4J_SCRIPT, SLICER4J_TIMEOUT_SEC, SLICER4J_MAX_ATTEMPTS

_ICDG_LOC_RE = re.compile(r":LINENO:(\d+):FILE:([^:]+):")


def _trace_only_attempt(ctx, jar_path, dep_dir, class_name, line_no, variable,
                         test_class, test_method, out_dir: Path, tag: str):
    """One Slicer4J invocation whose only purpose is to obtain
    trace.log_icdg.log for a test Step 2 never sliced. Unlike
    slicer_runner.run_slicer4j_criterion, this does not retry on a
    "trivial slice" outcome (irrelevant here - we never read the slice) and
    does not touch ctx.metrics (see module docstring). Returns the Path to
    a populated trace.log_icdg.log, or None if every attempt failed to even
    produce a trace (retried for the same transient Soot flakiness
    slicer_runner.py documents).
    """
    logger = ctx.logger
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "python3", SLICER4J_SCRIPT,
        "-j", str(jar_path), "-o", str(out_dir),
        "-b", f"{class_name}:{line_no}", "-v", variable,
        "-tc", test_class, "-tm", test_method, "-dep", str(dep_dir),
    ]
    trace_log = out_dir / "trace.log"
    icdg_log = out_dir / "trace.log_icdg.log"
    last_stderr = ""

    for attempt in range(1, SLICER4J_MAX_ATTEMPTS + 1):
        trace_log.unlink(missing_ok=True)
        icdg_log.unlink(missing_ok=True)

        rc, stdout, stderr = common.run_cmd(cmd, cwd=ctx.checkout_dir, timeout=SLICER4J_TIMEOUT_SEC, logger=logger)
        last_stderr = stderr
        (out_dir / "slicer4j_stdout.log").write_text(stdout, encoding="utf-8")
        (out_dir / "slicer4j_stderr.log").write_text(stderr, encoding="utf-8")

        if trace_log.exists() and trace_log.stat().st_size > 0 and icdg_log.exists():
            logger.info(f"[{tag}] trace-only Slicer4J OK on attempt {attempt}/{SLICER4J_MAX_ATTEMPTS} "
                        f"for {test_class}::{test_method}")
            return icdg_log

        logger.warning(f"[{tag}] trace-only Slicer4J attempt {attempt}/{SLICER4J_MAX_ATTEMPTS} produced no "
                        f"usable trace for {test_class}::{test_method} (rc={rc})")

    logger.warning(f"[{tag}] trace-only Slicer4J gave up after {SLICER4J_MAX_ATTEMPTS} attempts for "
                    f"{test_class}::{test_method}; this test contributes 0 to Pass_Assert/Fail_Assert. "
                    f"stderr tail: {last_stderr[-300:]}")
    return None


def _dynamic_assertion_hits(icdg_path: Path, test_class: str, assertion_lines: set) -> list:
    """Every dynamic hit on one of `assertion_lines` inside `test_class`,
    in real execution order (the leading id Slicer4J's own trace rows are
    numbered with - see slicer4j.py's dynamic_slice(), which reads this
    exact same field the same way: `line.split(", ")[0]`). A line inside a
    loop that iterates N times produces N separate entries here, one per
    iteration actually executed.
    """
    if not icdg_path.exists():
        return []
    hits = []
    for line in icdg_path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = _ICDG_LOC_RE.search(line)
        if not m:
            continue
        lineno, file_cls = int(m.group(1)), m.group(2)
        if file_cls != test_class or lineno not in assertion_lines:
            continue
        try:
            event_id = int(line.split(", ", 1)[0])
        except ValueError:
            continue
        hits.append((event_id, lineno))
    hits.sort(key=lambda h: h[0])
    return [lineno for _, lineno in hits]


def _count_for_test(icdg_path: Path, test_class: str, assertion_lines: set, passed: bool):
    hits = _dynamic_assertion_hits(icdg_path, test_class, assertion_lines)
    if not hits:
        return 0, 0
    if passed:
        return len(hits), 0
    return len(hits) - 1, 1  # every hit passed except the last, which is the one that threw


def compute(ctx, test_results):
    """Returns {"pass_assert": int, "fail_assert": int, "rows": [...]}.
    Requires Step 2 (step2_slicing.run) to have already completed for this
    target - reads failing_slice_metadata.csv/passed_slice_metadata.csv it
    already wrote, and (re)builds the same instrumentable jar/dep dir Step 2
    used (both documented as cheap/safe to rebuild fresh - see
    slicer_runner.build_instrumentable_jar/build_dependency_dir).
    """
    logger = ctx.logger
    jar_path = slicer_runner.build_instrumentable_jar(ctx)
    dep_dir = slicer_runner.build_dependency_dir(ctx)
    test_source_dir = slicer_runner.get_test_source_dir(ctx.checkout_dir, ctx.step2_dir, logger)

    failing_metadata = common.read_csv(ctx.step2_dir / "failing_slice_metadata.csv")
    passed_metadata = common.read_csv(ctx.step2_dir / "passed_slice_metadata.csv")

    # test_case -> every assertion source line in that test's own method body
    # (unrestricted - a superset for a failing test, since it also includes
    # assertions after the failure line; those simply never appear as a
    # dynamic hit below, so including them here is harmless).
    assertion_lines_by_test = {}
    for r in test_results:
        src_file = test_source_dir / (r["test_class"].replace(".", "/") + ".java")
        assertion_lines_by_test[r["test_case"]] = {
            a["line"] for a in java_ast.parse_assertions_in_method(src_file, r["test_method"])
        }

    # test_case -> out_dir(s) Step 2 already ran Slicer4J in (zero extra cost).
    existing_out_dirs = {}
    for row in failing_metadata + passed_metadata:
        for p in [row.get("slice_path", "")] + row.get("extra_slice_paths", "").split(";"):
            if p:
                existing_out_dirs.setdefault(row["test_case"], []).append(Path(p).parent)

    trace_only_root = ctx.step2_dir / "_assert_trace_only"
    rows = []
    for r in test_results:
        test_case, test_class, test_method = r["test_case"], r["test_class"], r["test_method"]
        passed = r["result"] == "PASS"
        assertion_lines = assertion_lines_by_test.get(test_case, set())

        icdg_path = None
        for out_dir in existing_out_dirs.get(test_case, []):
            cand = out_dir / "trace.log_icdg.log"
            if cand.exists():
                icdg_path = cand
                break

        if icdg_path is None and assertion_lines:
            src_file = test_source_dir / (test_class.replace(".", "/") + ".java")
            assertions = java_ast.parse_assertions_in_method(src_file, test_method)
            seed = next((a for a in reversed(assertions) if a["variable"]), None)
            if seed is None:
                logger.warning(f"{test_case}: every assertion's checked expression is a literal (no "
                                f"seedable variable); cannot obtain a trace-only run for this test.")
            else:
                tag = common.safe_filename(f"{test_method}_{seed['variable']}_L{seed['line']}_traceonly")
                icdg_path = _trace_only_attempt(
                    ctx, jar_path, dep_dir, test_class, seed["line"], seed["variable"],
                    test_class, test_method, trace_only_root / tag, tag,
                )

        pass_n = fail_n = 0
        if icdg_path is not None:
            pass_n, fail_n = _count_for_test(icdg_path, test_class, assertion_lines, passed)
        elif assertion_lines:
            logger.warning(f"{test_case}: no dynamic trace obtained; contributes 0 to Pass_Assert/Fail_Assert "
                            f"despite having {len(assertion_lines)} statically-detected assertion(s).")

        rows.append({
            "test_case": test_case, "result": r["result"], "assertion_source_lines": len(assertion_lines),
            "dynamic_pass_asserts": pass_n, "dynamic_fail_asserts": fail_n,
            "trace_source": str(icdg_path) if icdg_path else "",
        })

    common.write_csv(
        ctx.step2_dir / "assertion_execution_counts.csv",
        ["test_case", "result", "assertion_source_lines", "dynamic_pass_asserts", "dynamic_fail_asserts",
         "trace_source"],
        rows,
    )

    pass_assert = sum(r["dynamic_pass_asserts"] for r in rows)
    fail_assert = sum(r["dynamic_fail_asserts"] for r in rows)
    untraced = sum(1 for r in rows if not r["trace_source"])
    logger.info(f"RQ1 dynamic assertion counts: Pass_Assert={pass_assert} Fail_Assert={fail_assert} "
                f"across {len(rows)} test(s) ({untraced} untraced).")
    return {"pass_assert": pass_assert, "fail_assert": fail_assert, "rows": rows}
