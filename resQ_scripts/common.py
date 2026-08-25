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

    NOTE: kept for callers that genuinely want raw append. For the RQ result
    csvs, which must hold exactly one row per (Project, BugID) no matter how
    many times run_pipeline.py is invoked - for all targets or a single one
    - use upsert_csv_row instead.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not path.exists()
    with open(path, "a", newline="", encoding=ENCODING) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if is_new:
            writer.writeheader()
        writer.writerow({k: row.get(k, "") for k in fieldnames})


def upsert_csv_row(path, fieldnames, row, key_fields) -> None:
    """Write one row to a shared cross-target RQ csv, replacing any existing
    row(s) whose `key_fields` match instead of duplicating them.

    Re-running run_pipeline.py - for all 4 targets or just one - is a
    supported, ordinary workflow (see its own module docstring: "python3
    run_pipeline.py Csv_3b # just one target"). Plain append (see
    append_csv_row) makes every rerun accumulate duplicate rows for
    whichever targets it touched; a blind truncate-at-start would instead
    destroy the other targets' already-recorded rows on a single-target
    rerun. Upserting on `key_fields` keeps exactly one row per target no
    matter how many times or in what combination the pipeline is invoked,
    while still writing the row to disk the moment its target finishes (a
    crash on a later target does not lose earlier targets' rows).

    Key comparison is done on str(...) of every key field, not the raw
    values: `row` (freshly built in-process, e.g. rq_writers._write_rq5's
    `line_no`) can carry a real int, while every row read back via
    read_csv/csv.DictReader is str-only by construction - comparing the two
    directly (int 90 != str "90") silently never matches an on-disk row from
    a PRIOR run, so old rows never get replaced, only ever added to. This
    bit only rq5.csv in practice (its line_no key field is the sole non-string
    key across all RQ csvs; Project/BugID elsewhere are already strings), but
    would silently corrupt any future int-keyed RQ file too.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    key = tuple(str(row.get(k)) for k in key_fields)
    kept = [r for r in read_csv(path) if tuple(str(r.get(k)) for k in key_fields) != key]
    kept.append(row)
    write_csv(path, fieldnames, kept)
