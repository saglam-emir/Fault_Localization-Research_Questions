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
import slicer_runner

VIRTUAL_COLUMNS_FIELDS = [
    "virtual_test_id", "test_case", "test_class", "test_method",
    "variable", "line", "virtual_status", "slice_size", "slice_path",
]


def _slice_criteria(ctx, jar_path, dep_dir, rows, out_root: Path, tag_suffix: str):
    """Shared driver for both 2a (failing) and 2c (passed) slicing: one
    Slicer4J run per row, returns virtual-column metadata rows.
    """
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
        slice_size = 0
        if slice_log:
            slice_size = len([l for l in slice_log.read_text(encoding="utf-8").splitlines() if l.strip()])

        metadata.append({
            "virtual_test_id": tag, "test_case": row["test_case"], "test_class": test_class,
            "test_method": test_method, "variable": variable, "line": line,
            "virtual_status": virtual_status, "slice_size": slice_size,
            "slice_path": str(slice_log) if slice_log else "",
        })
    return metadata


def _scan_passed_assertions(ctx, target_variables, passed_tests):
    import java_ast
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
        vtid, slice_path = row["virtual_test_id"], row.get("slice_path", "")
        lines_out = ctx.slice_lines_dir / f"{vtid}.txt"
        code_out = ctx.slice_code_dir / f"{vtid}_slice.txt"

        if not slice_path or not Path(slice_path).exists():
            lines_out.write_text("", encoding="utf-8")
            code_out.write_text(f"# No slice produced for {row['test_case']} (variable={row['variable']})\n", encoding="utf-8")
            row["slice_size"] = 0
            updated.append(row)
            continue

        entries = []
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

        filtered = []
        for file_name, line_no in entries:
            if line_no == -1 or is_main_source(file_name):
                filtered.append((file_name, line_no))
            else:
                dropped.add(file_name)
        entries = filtered

        lines_out.write_text("\n".join(str(ln) for _, ln in entries) + ("\n" if entries else ""), encoding="utf-8")

        code_lines = [f"# Dynamic slice for {row['test_case']} (variable: {row['variable']}, virtual_test_id: {vtid})", ""]
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

    return {"virtual_columns": virtual_columns, "passed_variable_matches": matches}
