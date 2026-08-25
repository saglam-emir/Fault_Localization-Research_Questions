"""
step3_matrices.py
===================
STEP 3 - Two observation matrices, one shared Ochiai formula.

3a. Trace matrix (traditional SBFL baseline): per-test line coverage via
    `defects4j coverage -t <test>` (Cobertura). Defects4J's `-i` coverage
    scope defaults to only the bug's modified class(es); to score
    suspiciousness across the whole project we instead pass our own
    instrument-classes file enumerating every class under dir.src.classes.
    Every `defects4j coverage` call is timed via /usr/bin/time -v - their
    sum is RQ3's SBFL_Time (this is exactly the per-test instrumentation +
    execution cost a traditional trace-based SBFL tool pays).
3b. Slice matrix (hybrid): rows = Step 2's virtual columns, columns = the
    union of every statement appearing in any virtual column's dynamic
    slice, cell = slice membership. This is the Extended (assertion-level)
    SBFL matrix the hybrid approach scores suspiciousness from.
3c. Ochiai: both matrices share one row=observation/column=statement
    orientation (plus a trailing PASS/FAIL "result" column), so one scoring
    function serves both - any ranking difference comes purely from how the
    two matrices were built, not from two scoring implementations.

Both matrix builders drop:
  - statements outside dir.src.classes (test code can never become a row -
    layer 1 for the trace matrix, layer 3 re-validation for the slice
    matrix, since Step 2 already filtered it once);
  - bracket-only lines (a lone '{'/'}' etc.) - real bytecode-bearing lines,
    but not "statements" in the SBFL sense.
"""

import math
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import common
from context import DEFECTS4J_CMD, TEST_TIMEOUT_SEC

COVERAGE_XML_NAME = "coverage.xml"


# ---------------------------------------------------------------------------
# 3a. Trace matrix (traditional SBFL)
# ---------------------------------------------------------------------------
def _build_instrument_classes_file(ctx):
    src_root = ctx.checkout_dir / common.export_d4j_prop(
        ctx.checkout_dir, "dir.src.classes", ctx.step3_dir, "_dir_src_classes.tmp.txt", ctx.logger)
    fqcns = sorted(".".join(f.relative_to(src_root).with_suffix("").parts) for f in src_root.rglob("*.java"))
    if not fqcns:
        common.fail_fast(ctx.logger, f"No .java files found under {src_root}.")
    out_file = ctx.step3_dir / "instrument_classes_all.txt"
    out_file.write_text("\n".join(fqcns) + "\n", encoding="utf-8")
    return out_file


def _parse_coverage_xml(path: Path):
    executed = {}
    if not path.exists():
        return executed
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return executed
    for cls in root.iter("class"):
        filename = cls.get("filename", cls.get("name", "unknown"))
        for lines_el in cls.findall("lines"):
            for line_el in lines_el.findall("line"):
                try:
                    executed[(Path(filename).name, int(line_el.get("number")))] = int(line_el.get("hits", "0"))
                except (TypeError, ValueError):
                    continue
    return executed


def _run_coverage_for_test(ctx, test_case: str, instrument_file: Path):
    rc, stdout, stderr, elapsed, peak_kb = common.run_cmd_timed(
        [DEFECTS4J_CMD, "coverage", "-t", test_case, "-i", str(instrument_file)],
        cwd=ctx.checkout_dir, timeout=TEST_TIMEOUT_SEC, logger=ctx.logger,
    )
    ctx.metrics.sbfl_time_sec += elapsed
    ctx.metrics.note_memory(peak_kb)
    coverage_xml = ctx.checkout_dir / COVERAGE_XML_NAME
    if rc != 0 or not coverage_xml.exists():
        ctx.logger.warning(f"`defects4j coverage -t {test_case}` produced no {COVERAGE_XML_NAME} (rc={rc})")
        return {}
    return _parse_coverage_xml(coverage_xml)


def _is_main_source(ctx, cache, file_name):
    if file_name not in cache:
        cache[file_name] = common.find_main_source_file(
            ctx.checkout_dir, file_name, ctx.step3_dir, "_dir_src_classes.tmp.txt", ctx.logger) is not None
    return cache[file_name]


def _get_code(ctx, cache, file_name, line_no):
    if file_name not in cache:
        src_path = common.find_main_source_file(ctx.checkout_dir, file_name, ctx.step3_dir, "_dir_src_classes.tmp.txt", ctx.logger)
        cache[file_name] = src_path.read_text(encoding="utf-8", errors="replace").splitlines() if src_path and src_path.exists() else None
    lines = cache[file_name]
    return lines[line_no - 1].strip() if lines is not None and 0 < line_no <= len(lines) else ""


def build_trace_matrix(ctx, test_results):
    logger = ctx.logger
    instrument_file = _build_instrument_classes_file(ctx)

    per_test_coverage, universe = {}, set()
    for row in test_results:
        covered = {k for k, hits in _run_coverage_for_test(ctx, row["test_case"], instrument_file).items() if hits > 0}
        per_test_coverage[row["test_case"]] = covered
        universe.update(covered)

    if not universe:
        common.fail_fast(logger, "No coverage data collected from any test.")

    main_cache = {}
    dropped = {f for f, _ in universe if not _is_main_source(ctx, main_cache, f)}
    if dropped:
        universe = {s for s in universe if s[0] not in dropped}
        for tc in per_test_coverage:
            per_test_coverage[tc] = {s for s in per_test_coverage[tc] if s[0] not in dropped}

    code_cache = {}
    bracket_only = {s for s in universe if common.is_bracket_only_code(_get_code(ctx, code_cache, *s))}
    universe -= bracket_only
    if not universe:
        common.fail_fast(logger, "Trace matrix statement universe is empty after filtering.")

    ordered = sorted(universe)
    sids = {stmt: f"S{i+1}" for i, stmt in enumerate(ordered)}
    mapping_rows = [{"statement_id": sids[s], "file": s[0], "line": s[1], "code": _get_code(ctx, code_cache, *s)} for s in ordered]
    common.write_csv(ctx.step3_dir / "trace_statement_mapping.csv", ["statement_id", "file", "line", "code"], mapping_rows)

    matrix_rows = []
    for row in test_results:
        covered = per_test_coverage.get(row["test_case"], set())
        mrow = {"test_case": row["test_case"]}
        for stmt in ordered:
            mrow[sids[stmt]] = 1 if stmt in covered else 0
        mrow["result"] = row["result"]
        matrix_rows.append(mrow)
    fieldnames = ["test_case"] + [sids[s] for s in ordered] + ["result"]
    common.write_csv(ctx.step3_dir / "trace_observation_matrix.csv", fieldnames, matrix_rows)

    logger.info(f"Step3a: trace matrix {len(test_results)} tests x {len(ordered)} statements.")
    return {"matrix_rows": matrix_rows, "mapping_rows": mapping_rows, "statement_universe": ordered}


# ---------------------------------------------------------------------------
# 3b. Slice matrix (hybrid)
# ---------------------------------------------------------------------------
def _load_slice_statements(ctx, virtual_test_id):
    code_path = ctx.slice_code_dir / f"{virtual_test_id}_slice.txt"
    stmts = set()
    if not code_path.exists():
        return stmts
    for line in code_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or ":" not in line:
            continue
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        try:
            line_no = int(parts[1])
        except ValueError:
            continue
        if line_no != -1:
            stmts.add((parts[0], line_no))
    return stmts


def build_slice_matrix(ctx, virtual_columns):
    logger = ctx.logger
    main_cache, dropped = {}, set()

    per_column, universe = {}, set()
    for row in virtual_columns:
        stmts = _load_slice_statements(ctx, row["virtual_test_id"])
        kept = set()
        for f, ln in stmts:
            if _is_main_source(ctx, main_cache, f):
                kept.add((f, ln))
            else:
                dropped.add(f)
        per_column[row["virtual_test_id"]] = kept
        universe.update(kept)

    if dropped:
        logger.warning(f"Step3b: dropped statements from {len(dropped)} non-main-source file(s): {sorted(dropped)}")
    # An empty universe here (every virtual column's dynamic slice came back
    # empty or entirely test-code) is a legitimate - if disappointing -
    # outcome of the variable-based slicing criterion (e.g. Slicer4J finding
    # no backward dependencies for a given (variable, line) pair), not a
    # pipeline defect. Degrade gracefully to a 0-statement matrix rather
    # than aborting the whole target: RQ1-RQ4 don't depend on it, and RQ5's
    # hybrid side just reports "nothing ranked" (see step4_ranking.py).
    code_cache = {}
    if universe:
        bracket_only = {s for s in universe if common.is_bracket_only_code(_get_code(ctx, code_cache, *s))}
        universe -= bracket_only
    universe_empty = not universe
    if universe_empty:
        logger.warning("Step3b: slice matrix statement universe is empty (every virtual column's dynamic "
                        "slice was empty or test-code-only) - hybrid Ochiai/ranking will be trivially empty.")

    # A second, more insidious degenerate case than an empty universe: the
    # universe is non-empty (passing-side slices produced real statements),
    # but EVERY Virtual_Fail column individually covers zero of those
    # statements (e.g. all failing-criteria slices came back empty while
    # passing-criteria slices did not). ochiai_score's failed_covered term
    # is then 0 for every single statement, so every statement scores 0.0
    # and ties for rank 1 (see build_ranking's tie logic in
    # step4_ranking.py) - any rq5.csv rank_best_slice=1 in that state is a
    # tie-break artifact of zero failing-side data, not a genuine top-1
    # localization, and is otherwise indistinguishable from a real hit by
    # anyone just reading rq5.csv.
    fail_ids = [r["virtual_test_id"] for r in virtual_columns if r["virtual_status"] == "Virtual_Fail"]
    fail_side_empty = bool(fail_ids) and not universe_empty and all(
        not (per_column.get(vtid, set()) & universe) for vtid in fail_ids
    )
    if fail_side_empty:
        logger.warning(
            f"Step3b: all {len(fail_ids)} Virtual_Fail column(s) cover ZERO statements in the slice "
            f"universe (only Virtual_Pass columns contributed statements). Every Ochiai score will be "
            f"0.0 and the entire universe will tie for rank 1 - any rq5.csv rank_best_slice=1 this "
            f"produces is a degenerate tie-break artifact, not a real top-1 localization."
        )

    # Written unconditionally, with a fixed schema regardless of outcome -
    # unlike slice_statement_mapping.csv / slice_observation_matrix.csv
    # (whose column count legitimately varies with the size of the
    # statement universe, 0 included), this file lets any downstream tool
    # that loops over targets check "did this target's hybrid slicing
    # actually produce usable data?" without needing to parse a
    # variable-width CSV or infer it from a suspiciously-perfect rank.
    common.write_csv(
        ctx.step3_dir / "slice_matrix_status.csv",
        ["statement_universe_size", "is_empty", "fail_side_empty"],
        [{"statement_universe_size": len(universe), "is_empty": universe_empty,
          "fail_side_empty": fail_side_empty}],
    )

    ordered = sorted(universe)
    sids = {stmt: f"S{i+1}" for i, stmt in enumerate(ordered)}
    mapping_rows = [{"statement_id": sids[s], "file": s[0], "line": s[1], "code": _get_code(ctx, code_cache, *s)} for s in ordered]
    common.write_csv(ctx.step3_dir / "slice_statement_mapping.csv", ["statement_id", "file", "line", "code"], mapping_rows)

    status_rows = [{"virtual_test_id": r["virtual_test_id"], "virtual_status": r["virtual_status"],
                    "source_test_case": r["test_case"], "test_class": r["test_class"], "test_method": r["test_method"],
                    "variable": r["variable"], "line": r["line"]} for r in virtual_columns]
    common.write_csv(ctx.step3_dir / "virtual_test_status.csv",
                      ["virtual_test_id", "virtual_status", "source_test_case", "test_class", "test_method", "variable", "line"],
                      status_rows)

    matrix_rows = []
    for row in virtual_columns:
        covered = per_column[row["virtual_test_id"]]
        mrow = {"virtual_test_id": row["virtual_test_id"]}
        for stmt in ordered:
            mrow[sids[stmt]] = 1 if stmt in covered else 0
        mrow["result"] = "PASS" if row["virtual_status"] == "Virtual_Pass" else "FAIL"
        matrix_rows.append(mrow)
    fieldnames = ["virtual_test_id"] + [sids[s] for s in ordered] + ["result"]
    common.write_csv(ctx.step3_dir / "slice_observation_matrix.csv", fieldnames, matrix_rows)

    logger.info(f"Step3b: slice matrix {len(virtual_columns)} virtual columns x {len(ordered)} statements.")
    return {
        "matrix_rows": matrix_rows, "mapping_rows": mapping_rows, "statement_universe": ordered,
        "per_column_statements": per_column, "universe_empty": universe_empty,
        "fail_side_empty": fail_side_empty,
    }


# ---------------------------------------------------------------------------
# 3c. Ochiai (shared formula for both matrices)
# ---------------------------------------------------------------------------
def ochiai_score(failed_covered, failed_not_covered, passed_covered):
    total_failed = failed_covered + failed_not_covered
    total_covering = failed_covered + passed_covered
    denom = math.sqrt(total_failed * total_covering) if (total_failed and total_covering) else 0.0
    return (failed_covered / denom) if denom > 0 else 0.0


def compute_ochiai(matrix_rows, id_column: str):
    if not matrix_rows:
        # No virtual columns at all (e.g. an empty Target Variable Pool
        # produced zero slicing criteria) - nothing to score, not an error.
        return [], 0, 0
    statement_ids = [k for k in matrix_rows[0].keys() if k not in (id_column, "result")]
    counts = {sid: [0, 0, 0, 0] for sid in statement_ids}  # ef, nf, ep, np
    n_fail = n_pass = 0
    for row in matrix_rows:
        status = row.get("result")
        n_fail += status == "FAIL"
        n_pass += status == "PASS"
        for sid in statement_ids:
            covered = row.get(sid) == 1 or row.get(sid) == "1"
            c = counts[sid]
            if status == "FAIL":
                c[0 if covered else 1] += 1
            elif status == "PASS":
                c[2 if covered else 3] += 1

    scores = []
    for sid in statement_ids:
        ef, nf, ep, np_ = counts[sid]
        scores.append({"statement_id": sid, "failed_covered": ef, "failed_not_covered": nf,
                        "passed_covered": ep, "passed_not_covered": np_,
                        "ochiai_score": round(ochiai_score(ef, nf, ep), 6)})
    return scores, n_fail, n_pass


OCHIAI_FIELDS = ["statement_id", "failed_covered", "failed_not_covered", "passed_covered", "passed_not_covered", "ochiai_score"]


def run(ctx, test_results, virtual_columns):
    trace = build_trace_matrix(ctx, test_results)
    slice_ = build_slice_matrix(ctx, virtual_columns)

    trace_scores, trace_nf, trace_np = compute_ochiai(trace["matrix_rows"], "test_case")
    common.write_csv(ctx.step3_dir / "trace_ochiai_scores.csv", OCHIAI_FIELDS, trace_scores)

    slice_scores, slice_nf, slice_np = compute_ochiai(slice_["matrix_rows"], "virtual_test_id")
    common.write_csv(ctx.step3_dir / "slice_ochiai_scores.csv", OCHIAI_FIELDS, slice_scores)

    ctx.logger.info(f"Step3c: trace Ochiai ({trace_nf} FAIL/{trace_np} PASS rows), "
                     f"slice Ochiai ({slice_nf} FAIL/{slice_np} PASS rows).")

    return {
        "trace_mapping": trace["mapping_rows"], "trace_scores": trace_scores,
        "trace_universe": trace["statement_universe"],
        # Per-test-case coverage rows (test_case, one 1/0 column per trace
        # statement, plus "result") - RQ2's passing_TC_size/failing_TC_size
        # need this to split the RAW (unsliced) execution spectrum by
        # source-test-case outcome; nothing else currently reads it back out
        # of the ochiai_result dict.
        "trace_matrix_rows": trace["matrix_rows"],
        "slice_mapping": slice_["mapping_rows"], "slice_scores": slice_scores,
        "slice_universe": slice_["statement_universe"],
        "per_column_statements": slice_["per_column_statements"],
        "slice_universe_empty": slice_["universe_empty"],
        "slice_fail_side_empty": slice_["fail_side_empty"],
    }
