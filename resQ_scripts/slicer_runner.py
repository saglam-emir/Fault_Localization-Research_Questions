"""
slicer_runner.py
==================
Shared Slicer4J invocation logic used by both the failing-test slicing step
and the selective passing-test slicing step, so both share one exact recipe.

Two non-obvious details, load-bearing for correct results:

1. Slicer4J's `-b` backward-criterion class token must be the fully
   qualified class name (e.g. "org.apache.commons.csv.CSVParserTest"), not a
   bare source file name - Slicer4J matches it against the ":FILE:" field in
   its own instrumentation trace, which is always fully qualified.

2. `-dep <dir>` is globbed as `<dir>/*` onto the runtime classpath.
   `defects4j export -p cp.test` returns every jar in defects4j's local
   repo cache, INCLUDING multiple incompatible versions of the same
   artifact. Symlinking all of them into one flat directory loses cp.test's
   resolution order and can silently change runtime behavior (a genuinely
   failing test flipping to PASS under the wrong jar version).
   `build_dependency_dir` deduplicates by artifact identity, keeping
   cp.test's first-seen (= actually resolved) version of each jar.

Soot's multi-threaded instrumentation pass can also intermittently throw a
ConcurrentModificationException. `run_slicer4j_criterion` retries the whole
slicer4j.py invocation a few times to work around that flakiness rather than
failing the whole target on a transient Soot crash.
"""

import os
import re
import shutil
from pathlib import Path

import common
from context import ENCODING, SLICER4J_SCRIPT, SLICER4J_TIMEOUT_SEC, SLICER4J_MAX_ATTEMPTS, TEST_TIMEOUT_SEC

_DEP_VERSION_SUFFIX_RE = re.compile(r"-[0-9][^/]*\.jar$")


def get_test_source_dir(project_dir: Path, cache_dir: Path, logger) -> Path:
    return project_dir / common.export_d4j_prop(project_dir, "dir.src.tests", cache_dir, "_dir_src_tests.tmp.txt", logger)


def build_instrumentable_jar(ctx) -> Path:
    """Package the already-compiled classes (main + test) into one jar for
    Slicer4J's `-j` argument. Assumes `defects4j test`/`compile` has already
    produced up-to-date .class files with debug info. Always rebuilt fresh
    (cheap) so a stale jar from an earlier run can never mask a recompile.
    """
    project_dir, out_dir, logger = ctx.checkout_dir, ctx.step2_dir, ctx.logger
    jar_path = out_dir / "instrumentable.jar"

    bin_classes = project_dir / common.export_d4j_prop(project_dir, "dir.bin.classes", out_dir, "_dir_bin_classes.tmp.txt", logger)
    bin_tests = project_dir / common.export_d4j_prop(project_dir, "dir.bin.tests", out_dir, "_dir_bin_tests.tmp.txt", logger)

    if not bin_classes.exists():
        common.fail_fast(logger, f"Compiled classes directory not found: {bin_classes}. Run `defects4j compile` first.")

    staging = out_dir / "_jar_staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    shutil.copytree(bin_classes, staging, dirs_exist_ok=True)
    if bin_tests.exists():
        shutil.copytree(bin_tests, staging, dirs_exist_ok=True)

    if jar_path.exists():
        jar_path.unlink()
    rc, stdout, stderr = common.run_cmd(["jar", "cf", str(jar_path), "-C", str(staging), "."],
                                         cwd=project_dir, timeout=TEST_TIMEOUT_SEC, logger=logger)
    if rc != 0 or not jar_path.exists():
        common.fail_fast(logger, f"Failed to build instrumentable jar: {stderr}")
    logger.info(f"Built instrumentable jar at {jar_path}")
    return jar_path


def _dedup_key(jar_path_str: str) -> str:
    base = Path(jar_path_str).name
    key = _DEP_VERSION_SUFFIX_RE.sub("", base)
    if key == base and base.endswith(".jar"):
        key = base[:-4]
    return key


def build_dependency_dir(ctx) -> Path:
    """Build a `-dep` directory containing exactly one jar per runtime
    dependency, keeping cp.test's first-seen (= actually resolved) version
    of each. Always rebuilt fresh, same staleness reasoning as the jar.
    """
    project_dir, logger = ctx.checkout_dir, ctx.logger
    cp_test = common.export_d4j_prop(project_dir, "cp.test", ctx.step2_dir, "_cp_test.tmp.txt", logger)

    if ctx.dep_dir.exists():
        shutil.rmtree(ctx.dep_dir)
    ctx.dep_dir.mkdir(parents=True)

    seen, linked = set(), 0
    for entry in cp_test.split(os.pathsep):
        if not entry.endswith(".jar") or not Path(entry).is_file():
            continue
        key = _dedup_key(entry)
        if key in seen:
            continue
        seen.add(key)
        dest = ctx.dep_dir / Path(entry).name
        try:
            dest.symlink_to(entry)
        except OSError:
            shutil.copy(entry, dest)
        linked += 1

    logger.info(f"Built deduplicated dependency dir with {linked} jar(s) at {ctx.dep_dir}")
    return ctx.dep_dir


def run_slicer4j_criterion(ctx, jar_path, dep_dir, class_name, line_no, variable,
                            test_class, test_method, out_dir: Path, tag: str = ""):
    """Run one Slicer4J backward-slicing criterion, retrying on transient
    Soot failures. Returns the Path to a populated slice.log on success, or
    None if every attempt failed (recorded as an empty slice, not a fatal
    pipeline error). Every attempt's wall time and peak memory are folded
    into ctx.metrics regardless of outcome, so RQ3's Avg_Slice_Time /
    Peak_Memory reflect real work done, not just successful attempts.
    """
    logger = ctx.logger
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "python3", SLICER4J_SCRIPT,
        "-j", str(jar_path), "-o", str(out_dir),
        "-b", f"{class_name}:{line_no}", "-v", variable,
        "-tc", test_class, "-tm", test_method, "-dep", str(dep_dir),
    ]

    slice_log = out_dir / "slice.log"
    trace_log = out_dir / "trace.log"
    last_stderr = ""

    for attempt in range(1, SLICER4J_MAX_ATTEMPTS + 1):
        for stale in (slice_log, trace_log, out_dir / "trace.log_icdg.log"):
            stale.unlink(missing_ok=True)

        rc, stdout, stderr, elapsed, peak_kb = common.run_cmd_timed(
            cmd, cwd=ctx.checkout_dir, timeout=SLICER4J_TIMEOUT_SEC, logger=logger
        )
        ctx.metrics.slice_call_count += 1
        ctx.metrics.slice_time_total_sec += elapsed
        ctx.metrics.note_memory(peak_kb)

        (out_dir / "slicer4j_stdout.log").write_text(stdout, encoding=ENCODING)
        (out_dir / "slicer4j_stderr.log").write_text(stderr, encoding=ENCODING)
        last_stderr = stderr

        if trace_log.exists() and trace_log.stat().st_size > 0 and slice_log.exists():
            logger.info(f"[{tag}] Slicer4J OK on attempt {attempt}/{SLICER4J_MAX_ATTEMPTS} "
                        f"for {test_class}::{test_method} @ {class_name}:{line_no} var={variable}")
            return slice_log

        logger.warning(f"[{tag}] Slicer4J attempt {attempt}/{SLICER4J_MAX_ATTEMPTS} produced no usable "
                        f"slice for {test_class}::{test_method} @ {class_name}:{line_no} var={variable} (rc={rc})")

    logger.warning(f"[{tag}] Slicer4J gave up after {SLICER4J_MAX_ATTEMPTS} attempts for "
                    f"{test_class}::{test_method} @ {class_name}:{line_no} var={variable}. "
                    f"stderr tail: {last_stderr[-300:]}")
    return None
