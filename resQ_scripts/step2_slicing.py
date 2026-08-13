"""
step2_slicing.py
==================
STEP 2 - Dynamic slicing (assertion-level, Target Pool strategy).

2a. Failing tests: for every (test_case, variable, line, status) row in
    Step 1's Target Variable Pool, run one targeted Slicer4J backward slice
    with that exact variable as the seed. `status=Correct` -> Virtual_Pass,
    `status=Incorrect` -> Virtual_Fail.
2b. Passing tests (selective scan): statically scan every PASSING test's
    *full* assertion set (it all executed and held) and keep only the
    assertions whose variable name matches one already in the Target
    Variable Pool - this is the "only evaluate assertions whose output
    variables are in Target_Pool" requirement. Dynamic slicing is expensive,
    so passing tests are never sliced wholesale.
2c. Run Slicer4J on exactly those matched passing-test assertions -> always
    Virtual_Pass (the test passed).
2d. Collect: every slice.log (format "FullyQualifiedClass:Line" per
    statement) becomes one "virtual test" column - merges 2a+2c's metadata,
    resolves each entry to its (source_file, line), and writes both a
    line-numbers-only file and a human-readable listing per column.

    TEST-CODE FILTERING: Slicer4J's criterion is anchored inside the test
    method, so slice.log legitimately contains test-class statements as
    dependency-chain noise. Those must never become matrix rows - every
    entry is resolved strictly under dir.src.classes (src/main/java, never
    dir.src.tests) before being kept; anything that doesn't resolve there is
    dropped.
"""

import time
from pathlib import Path

import common
import java_ast
import slicer_runner
from context import ALIAS_SCAN_MAX_CANDIDATES, ALIAS_SCAN_MAX_LINES_BACK

VIRTUAL_COLUMNS_FIELDS = [
    "virtual_test_id", "test_case", "test_class", "test_method",
    "variable", "line", "virtual_status", "slice_size", "slice_path", "extra_slice_paths",
]


def _run_aliasing_extras(ctx, jar_path, dep_dir, test_source_dir, row, tag, out_root):
    """Correction roadmap Step 4: seed extra Slicer4J criteria on any local
    the test's own source shows `row['variable']` being handed to before the
    criterion line (see java_ast.find_aliasing_seed_candidates), so a
    "receiver mutated the seed via a wrapping object" pattern (verified on
    Csv-13's `writer`/`printer`) gets a chance to contribute statements the
    primary criterion's same-line-only retry can never reach. Returns a list
    of extra slice_log Paths (possibly empty - a candidate that also comes
    back trivial contributes nothing, which is an expected, honest outcome
    for a genuinely void mutating call; see java_ast's docstring on what
    this can and cannot fix).
    """
    test_class, test_method = row["test_class"], row["test_method"]
    variable, line = row["variable"], int(row["line"])
    src_file = test_source_dir / (test_class.replace(".", "/") + ".java")
    candidates = java_ast.find_aliasing_seed_candidates(
        src_file, test_method, variable, line,
        max_lookback_lines=ALIAS_SCAN_MAX_LINES_BACK, max_candidates=ALIAS_SCAN_MAX_CANDIDATES,
    )
    extra_logs = []
    for cand in candidates:
        cand_tag = common.safe_filename(f"{tag}_alias_{cand['variable']}")
        cand_out_dir = out_root / cand_tag
        ctx.logger.info(f"[{tag}] Aliasing candidate: '{cand['variable']}' (seed '{variable}' was handed "
                         f"to it) @ line {cand['line']} - running an extra Slicer4J criterion.")
        cand_log = slicer_runner.run_slicer4j_criterion(
            ctx, jar_path, dep_dir, test_class, cand["line"], cand["variable"],
            test_class, test_method, cand_out_dir, tag=cand_tag,
        )
        if cand_log:
            extra_logs.append(cand_log)
    return extra_logs


def _slice_criteria(ctx, jar_path, dep_dir, rows, out_root: Path, tag_suffix: str):
    """Shared driver for both 2a (failing) and 2c (passed) slicing: one
    primary Slicer4J run per row, plus (correction roadmap Step 4) any
    aliasing-candidate extra runs, unioned into the same virtual column.
    Returns virtual-column metadata rows.
    """
    test_source_dir = slicer_runner.get_test_source_dir(ctx.checkout_dir, ctx.step2_dir, ctx.logger)
    metadata = []
    for i, row in enumerate(rows, start=1):
        test_class, test_method = row["test_class"], row["test_method"]
        variable, line = row["variable"], int(row["line"])
        virtual_status = row["virtual_status"]
        tag = common.safe_filename(f"{test_method}_{variable}_L{line}_{tag_suffix}_{i}")
        out_dir = out_root / tag

        print(f"[INFO] ({i}/{len(rows)}) Slicing [{virtual_status}]: {test_class}::{test_method} "
              f"var={variable} @ line {line}")

        slice_log = slicer_runner.run_slicer4j_criterion(
            ctx, jar_path, dep_dir, test_class, line, variable, test_class, test_method, out_dir, tag=tag,
        )
        extra_logs = _run_aliasing_extras(ctx, jar_path, dep_dir, test_source_dir, row, tag, out_root)

        slice_size = 0
        for sp in ([slice_log] if slice_log else []) + extra_logs:
            slice_size += len([l for l in sp.read_text(encoding="utf-8").splitlines() if l.strip()])

        metadata.append({
            "virtual_test_id": tag, "test_case": row["test_case"], "test_class": test_class,
            "test_method": test_method, "variable": variable, "line": line,
            "virtual_status": virtual_status, "slice_size": slice_size,
            "slice_path": str(slice_log) if slice_log else "",
            "extra_slice_paths": ";".join(str(p) for p in extra_logs),
        })
    return metadata


def _scan_passed_assertions(ctx, target_variables, passed_tests):
    test_source_dir = slicer_runner.get_test_source_dir(ctx.checkout_dir, ctx.step2_dir, ctx.logger)
    matches = []
    for row in passed_tests:
        src_file = test_source_dir / (row["test_class"].replace(".", "/") + ".java")
        for a in java_ast.parse_assertions_in_method(src_file, row["test_method"]):
            if a["variable"] and a["variable"] in target_variables:
                matches.append({"test_case": row["test_case"], "test_class": row["test_class"],
                                 "test_method": row["test_method"], "variable": a["variable"],
                                 "line": a["line"], "virtual_status": "Virtual_Pass"})
    return matches


def fq_class_to_source_file(fq_class: str) -> str:
    simple = fq_class.rsplit(".", 1)[-1].split("$", 1)[0]
    return f"{simple}.java"


def _collect(ctx, virtual_columns):
    logger = ctx.logger
    main_source_cache, source_text_cache, dropped = {}, {}, set()
    updated = []

    def is_main_source(file_name):
        if file_name not in main_source_cache:
            main_source_cache[file_name] = common.find_main_source_file(
                ctx.checkout_dir, file_name, ctx.step2_dir, "_dir_src_classes.tmp.txt", logger) is not None
        return main_source_cache[file_name]

    for row in virtual_columns:
        vtid = row["virtual_test_id"]
        # Primary criterion's slice_path plus (correction roadmap Step 4)
        # any aliasing-candidate extra_slice_paths, unioned into one
        # virtual column - see _run_aliasing_extras. A row with only a
        # primary path behaves exactly as before this change.
        slice_paths = [p for p in (
            [row.get("slice_path", "")] + row.get("extra_slice_paths", "").split(";")
        ) if p and Path(p).exists()]
        lines_out = ctx.slice_lines_dir / f"{vtid}.txt"
        code_out = ctx.slice_code_dir / f"{vtid}_slice.txt"

        if not slice_paths:
            lines_out.write_text("", encoding="utf-8")
            code_out.write_text(f"# No slice produced for {row['test_case']} (variable={row['variable']})\n", encoding="utf-8")
            row["slice_size"] = 0
            updated.append(row)
            continue

        entries = []
        for slice_path in slice_paths:
            for line in Path(slice_path).read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or ":" not in line:
                    continue
                fq_class, _, line_no_str = line.rpartition(":")
                try:
                    line_no = int(line_no_str)
                except ValueError:
                    continue
                entries.append((fq_class_to_source_file(fq_class), line_no))
        entries = list(dict.fromkeys(entries))  # dedup across primary+extra paths, preserve order

        filtered = []
        for file_name, line_no in entries:
            if line_no == -1 or is_main_source(file_name):
                filtered.append((file_name, line_no))
            else:
                dropped.add(file_name)
        entries = filtered

        lines_out.write_text("\n".join(str(ln) for _, ln in entries) + ("\n" if entries else ""), encoding="utf-8")

        n_extra = len(slice_paths) - 1
        extra_note = f", +{n_extra} aliasing-candidate criterion/criteria unioned in" if n_extra else ""
        code_lines = [f"# Dynamic slice for {row['test_case']} (variable: {row['variable']}, "
                      f"virtual_test_id: {vtid}{extra_note})", ""]
        for file_name, line_no in entries:
            if line_no == -1:
                code_lines.append(f"{file_name}:-1: <synthetic statement, no source line>")
                continue
            if file_name not in source_text_cache:
                src_path = common.find_main_source_file(ctx.checkout_dir, file_name, ctx.step2_dir, "_dir_src_classes.tmp.txt", logger)
                source_text_cache[file_name] = (
                    src_path.read_text(encoding="utf-8", errors="replace").splitlines() if src_path and src_path.exists() else None
                )
            src_lines = source_text_cache[file_name]
            code_text = (src_lines[line_no - 1].strip() if src_lines is not None and 0 < line_no <= len(src_lines)
                         else "<source unavailable>")
            code_lines.append(f"{file_name}:{line_no}: {code_text}")
        code_out.write_text("\n".join(code_lines) + "\n", encoding="utf-8")

        row["slice_size"] = len(entries)
        updated.append(row)

    if dropped:
        logger.info(f"Test-code filter: excluded statements from {len(dropped)} non-main-source file(s): {sorted(dropped)}")
    return updated


def run(ctx, test_results, target_pool):
    # RQ3: everything in Step 2 (jar/dep-dir build + both slicing halves) is
    # extra work only the hybrid approach pays for, on top of the per-test
    # execution time it shares with SBFL (charged in step1_tests.py). Timed
    # as one lump sum rather than per-sub-step, since jar/dep-dir building
    # is a fixed cost that has to happen before either slicing half can run.
    step2_start = time.time()
    logger = ctx.logger
    jar_path = slicer_runner.build_instrumentable_jar(ctx)
    dep_dir = slicer_runner.build_dependency_dir(ctx)

    # 2a. Failing-test slicing, one criterion per Target Variable Pool row.
    failing_rows = [
        {"test_case": r["test_case"], "test_class": r["test_class"], "test_method": r["test_method"],
         "variable": r["variable"], "line": r["line"],
         "virtual_status": "Virtual_Pass" if r["status"] == "Correct" else "Virtual_Fail"}
        for r in target_pool
    ]
    failing_metadata = _slice_criteria(ctx, jar_path, dep_dir, failing_rows, ctx.slicer_failing_dir, "F")
    common.write_csv(ctx.step2_dir / "failing_slice_metadata.csv", VIRTUAL_COLUMNS_FIELDS, failing_metadata)

    # 2b. Selective static scan of passing tests' assertions against the pool.
    target_variables = {r["variable"] for r in target_pool}
    passed_tests = [r for r in test_results if r["result"] == "PASS"]
    matches = _scan_passed_assertions(ctx, target_variables, passed_tests)
    common.write_csv(
        ctx.step2_dir / "passed_variable_matches.csv",
        ["test_case", "test_class", "test_method", "variable", "line", "virtual_status"], matches,
    )
    logger.info(f"Step2: {len(matches)} passing-test assertion(s) matched the Target Variable Pool "
                f"(out of {len(passed_tests)} passing tests scanned).")

    # 2c. Dynamic slicing on exactly those matches.
    passed_metadata = _slice_criteria(ctx, jar_path, dep_dir, matches, ctx.slicer_passed_dir, "P")
    ctx.metrics.hybrid_extra_time_sec += time.time() - step2_start
    common.write_csv(ctx.step2_dir / "passed_slice_metadata.csv", VIRTUAL_COLUMNS_FIELDS, passed_metadata)

    # 2d. Collect into unified virtual columns + per-column slice files.
    virtual_columns = _collect(ctx, failing_metadata + passed_metadata)
    common.write_csv(ctx.step2_dir / "virtual_columns.csv", VIRTUAL_COLUMNS_FIELDS, virtual_columns)

    n_fail = len([r for r in virtual_columns if r["virtual_status"] == "Virtual_Fail"])
    n_pass = len(virtual_columns) - n_fail
    logger.info(f"Step2: {len(virtual_columns)} virtual column(s) collected ({n_fail} Virtual_Fail, {n_pass} Virtual_Pass).")

    # Catch a total slicing failure here, not three steps later as a 0-column
    # slice_observation_matrix.csv someone has to notice by diffing against
    # another target's file. If every single virtual column's slice came
    # back empty, Slicer4J most likely only ever returned the seed criterion
    # line itself (which the main-source filter then correctly drops, since
    # the seed sits in test code) - a real slicing failure, distinct from
    # the "empty Target Variable Pool" case (nothing was even attempted).
    if virtual_columns and all(r["slice_size"] == 0 for r in virtual_columns):
        logger.warning(
            f"Step2: ALL {len(virtual_columns)} virtual column(s) produced an EMPTY slice after "
            f"main-source filtering. Slicer4J likely only traced each criterion's own seed line "
            f"(see _slicer4j_failing/*/slice.log and _slicer4j_passed/*/slice.log). Step3's slice "
            f"matrix, Step4's hybrid ranking, and RQ2/RQ4/RQ5's hybrid columns will all be "
            f"degenerate/empty for this target - this is a slicing failure, not a real 0% result."
        )

    return {"virtual_columns": virtual_columns, "passed_variable_matches": matches}
