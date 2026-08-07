"""
common.py
=========
Shared helpers used by every pipeline step: logging, subprocess execution
(plain and memory/time-measured), CSV I/O, and small text/path utilities.

Kept target-agnostic (no reference to a specific RunContext) except where a
helper caches a value onto a target's work_dir - those take the relevant
paths as plain arguments instead of importing a global config, since
run_pipeline.py runs all 4 targets in one process.
"""

import csv
import hashlib
import logging
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from context import ENCODING, DEFECTS4J_CMD, JAVA8_HOME, TEST_TIMEOUT_SEC


class StepFailure(Exception):
    """Raised by fail_fast(). Caught by run_pipeline.py at the per-target
    level so one target's fatal error does not abort the other 3 targets.
    """


def setup_logger(name: str, log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%Y-%m-%d %H:%M:%S")

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    logger.addHandler(console)

    file_handler = logging.FileHandler(log_dir / f"{name}.log", encoding=ENCODING)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
    return logger


def fail_fast(logger, message: str):
    logger.error(f"FATAL: {message}")
    raise StepFailure(message)


def _full_env(env=None):
    full_env = os.environ.copy()
    if JAVA8_HOME:
        full_env["JAVA_HOME"] = JAVA8_HOME
        full_env["PATH"] = str(Path(JAVA8_HOME) / "bin") + os.pathsep + full_env.get("PATH", "")
    if env:
        full_env.update(env)
    return full_env


def run_cmd(cmd, cwd=None, timeout=None, logger=None, env=None):
    """Run a command (list form), capture stdout/stderr. Never raises on a
    non-zero exit code; converts a hard timeout / missing executable into a
    (-1, "", <message>) tuple so callers can keep processing remaining work
    instead of crashing.
    """
    printable = " ".join(str(c) for c in cmd)
    if logger:
        logger.info(f"RUN: {printable}" + (f"  (cwd={cwd})" if cwd else ""))
    try:
        proc = subprocess.run(
            cmd, cwd=str(cwd) if cwd else None, env=_full_env(env),
            capture_output=True, text=True, timeout=timeout,
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired:
        msg = f"TIMEOUT after {timeout}s: {printable}"
        if logger:
            logger.error(msg)
        return -1, "", msg
    except FileNotFoundError as e:
        msg = f"COMMAND NOT FOUND: {printable} ({e})"
        if logger:
            logger.error(msg)
        return -1, "", msg


_MAX_RSS_RE = re.compile(r"Maximum resident set size \(kbytes\):\s*(\d+)")


def run_cmd_timed(cmd, cwd=None, timeout=None, logger=None, env=None):
    """Like run_cmd, but wraps `cmd` in `/usr/bin/time -v` and additionally
    returns (elapsed_sec, peak_rss_kb). Used for every subprocess call whose
    duration/memory feeds RQ3 (Baseline_Time, SBFL_Time, Hybrid_Time,
    Avg_Slice_Time, Peak_Memory).

    `/usr/bin/time -v` reports "Maximum resident set size" for the wrapped
    process *and its reaped children* (RUSAGE_CHILDREN) - which correctly
    covers e.g. Slicer4J's python wrapper spawning a java subprocess.
    peak_rss_kb is None if `/usr/bin/time -v` itself is unavailable or its
    output could not be parsed (elapsed_sec is still always measured
    directly via time.time(), independent of that).
    """
    wrapped = ["/usr/bin/time", "-v"] + [str(c) for c in cmd]
    start = time.time()
    rc, stdout, stderr = run_cmd(wrapped, cwd=cwd, timeout=timeout, logger=logger, env=env)
    elapsed = time.time() - start

    peak_kb = None
    m = _MAX_RSS_RE.search(stderr)
    if m:
        peak_kb = float(m.group(1))
    else:
        # /usr/bin/time missing, or the command itself failed to exec -
        # fall back to a plain (untimed-memory) run so the step still gets
        # a usable stdout/stderr/rc.
        if logger:
            logger.warning("`/usr/bin/time -v` produced no 'Maximum resident set size' line; "
                            "peak memory unavailable for this call.")
        rc, stdout, stderr = run_cmd(cmd, cwd=cwd, timeout=timeout, logger=logger, env=env)
        elapsed = time.time() - start

    return rc, stdout, stderr, elapsed, peak_kb


def export_d4j_prop(project_dir: Path, prop_name: str, cache_dir: Path, tmp_name: str, logger) -> str:
    """`defects4j export -p <prop_name>`, cached to disk since the value
    never changes for a given checkout.
    """
    out_file = Path(cache_dir) / tmp_name
    if out_file.exists():
        return out_file.read_text(encoding=ENCODING).strip()
    rc, stdout, stderr = run_cmd(
        [DEFECTS4J_CMD, "export", "-p", prop_name, "-o", str(out_file)],
        cwd=project_dir, timeout=TEST_TIMEOUT_SEC, logger=logger,
    )
    if rc != 0 or not out_file.exists():
        fail_fast(logger, f"`defects4j export -p {prop_name}` failed: {stderr}")
    return out_file.read_text(encoding=ENCODING).strip()


def find_main_source_file(project_dir: Path, file_name: str, cache_dir: Path, tmp_name: str, logger):
    """Resolve `file_name` (e.g. 'Lexer.java') strictly under dir.src.classes
    (src/main/java) - deliberately never falls back to dir.src.tests, so
    test code can never enter a statement universe (matrix rows/slice
    lines). Returns None if not found there.
    """
    base_dir = Path(project_dir) / export_d4j_prop(project_dir, "dir.src.classes", cache_dir, tmp_name, logger)
    matches = list(base_dir.rglob(file_name))
    return matches[0] if matches else None


_UNSAFE_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
_MAX_SAFE_FILENAME_LEN = 150


def safe_filename(raw: str, max_len: int = _MAX_SAFE_FILENAME_LEN) -> str:
    """Turn an arbitrary string (e.g. a slicing variable name) into a name
    safe to use as a file/directory name on Linux.
    """
    cleaned = _UNSAFE_FILENAME_CHARS.sub("_", raw)
    cleaned = re.sub(r"\s+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    if not cleaned:
        cleaned = "unnamed"
    if len(cleaned) > max_len:
        digest = hashlib.sha1(raw.encode("utf-8", errors="replace")).hexdigest()[:10]
        cleaned = f"{cleaned[: max_len - 11]}_{digest}"
    return cleaned


_BRACKET_ONLY_RE = re.compile(r'^[{}()\[\];,\s]*$')


def is_bracket_only_code(code: str) -> bool:
    """True for a source line that is nothing but bracket/punctuation (e.g.
    a lone '{', '}', '});'). Such lines carry a real bytecode instruction
    (so slicers/coverage tools legitimately report them) but are not
    "statements" in the SBFL sense and are dropped from every statement
    universe before statement_ids are assigned.
    """
    stripped = code.strip()
    if not stripped:
        return False
    return bool(_BRACKET_ONLY_RE.match(stripped)) and any(c in "{}()[]" for c in stripped)


def write_csv(path, fieldnames, rows) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding=ENCODING) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def read_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    with open(path, newline="", encoding=ENCODING) as f:
        return list(csv.DictReader(f))


def append_csv_row(path, fieldnames, row) -> None:
    """Append one row to a shared cross-target RQ csv, writing the header
    only if the file does not exist yet. Used by rq_writers.py so each
    target's row is durably persisted the moment that target finishes,
    instead of buffering all 4 targets' rows in memory until the very end.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not path.exists()
    with open(path, "a", newline="", encoding=ENCODING) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if is_new:
            writer.writeheader()
        writer.writerow({k: row.get(k, "") for k in fieldnames})
