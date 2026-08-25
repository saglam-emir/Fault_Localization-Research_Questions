"""
rq1_dynamic_asserts.py
========================
RQ1's Pass_Assert/Fail_Assert - see run_pipeline.py's top docstring and
run_pipeline.py's top-level RQ1 summary.

Methodology (matches the RQ1 task description exactly)
--------------------------------------------------------
Test-level SBFL treats a test case as one PASS/FAIL spectrum row.
Assertion-level treats every assertX(...) call as its own PASS/FAIL
observation (and, in Step 2, its own Slicer4J slice). RQ1 quantifies how
much that switch grows the amount of diagnostic information:

  - FAILING tests: JUnit halts at the first failing assertion, so only the
    assertions actually reached before the throw are real observations -
    everything up to and including the failure line, nothing after (it
    never ran). This is exactly Step 1's Target Variable Pool
    (target_pool, `status="Correct"` for the ones that held, `"Incorrect"`
    for the one that threw) - reused here as-is rather than recomputed,
    since it is already scoped precisely this way (see step1_tests.py's
    docstring, section 1c).
  - PASSING tests: the whole method ran and every assertion in it held, so
    EVERY assertX(...) call in a passing test's body is a genuine Pass
    observation - not just the ones Step 2 happened to select as slicing
    criteria (step2_slicing.py's 2b/2c only picks passing-test assertions
    whose variable name matches something already in the Target Pool, a
    selective subset scoped to what Steps 2-5 need, not a full count - see
    that module's own docstring). This module re-parses every passing
    test's full assertion set independently for that reason.

Both sides count STATIC assertX(...) call sites (one assertion = one
potential slice, per the task description), never dynamic executions - an
assertion inside a loop that iterates N times is still exactly one
observation, not N. This intentionally does NOT read Slicer4J's dynamic
bytecode trace (a strictly different, execution-count question) - no
Slicer4J run is issued by this module at all, so it costs nothing beyond
the AST parses Step 1 already pays for in step1_tests.py.

Only assertions java_ast can resolve to a checked root variable are
counted (`if not a["variable"]`), matching Step 1's own Target Pool filter
exactly (step1_tests.py:214) - an assertion whose checked expression is a
bare literal can never seed a Slicer4J criterion/slice either, so it is
not a countable "assertion-level observation" under this task's own
"each assertion gets its own slice" framing.

  Pass_Assert = (static, variable-resolvable assertX(...) call sites across
                 every PASSING test's own method body)
              + (Target Pool rows with status=="Correct", the assertions
                 that held inside a FAILING test before its throw)
  Fail_Assert = Target Pool rows with status=="Incorrect" (the one
                assertion, if any, that actually ended each failing test -
                a failing test that crashed via an uncaught exception
                before reaching any assertX(...) call contributes 0 here,
                which is correct: no assertion actually failed).
"""

import common
import java_ast
import slicer_runner


def compute(ctx, test_results, target_pool):
    """Returns {"pass_assert": int, "fail_assert": int, "rows": [...]}.
    `target_pool` is Step 1's already-computed target_pool list (one dict
    per Correct/Incorrect assertion row) - reused here, not recomputed, so
    Fail_Assert can never disagree with what Step 2 actually sliced on.
    """
    logger = ctx.logger
    test_source_dir = slicer_runner.get_test_source_dir(ctx.checkout_dir, ctx.step2_dir, logger)

    rows = []
    pass_static_total = 0
    for r in test_results:
        if r["result"] != "PASS":
            continue
        src_file = test_source_dir / (r["test_class"].replace(".", "/") + ".java")
        assertions = java_ast.parse_assertions_in_method(src_file, r["test_method"])
        counted = [a for a in assertions if a["variable"]]
        pass_static_total += len(counted)
        rows.append({
            "test_case": r["test_case"], "result": "PASS",
            "assertx_calls_found": len(assertions),
            "assertx_calls_counted": len(counted),
        })

    # criterion_kind=="assertion" only - excludes step1_tests.py's synthetic
    # "exception_site" fallback rows (a failing test that crashed via an
    # uncaught exception before ever reaching an assertX(...) call). Those
    # exist so Step 2 still has something to slice on, but they are not
    # real assertions, so they must not inflate Fail_Assert/Pass_Assert -
    # a test in that bucket correctly contributes 0 to both.
    real_assertion_rows = [p for p in target_pool if p["criterion_kind"] == "assertion"]
    pool_correct = sum(1 for p in real_assertion_rows if p["status"] == "Correct")
    pool_incorrect = sum(1 for p in real_assertion_rows if p["status"] == "Incorrect")

    pass_assert = pass_static_total + pool_correct
    fail_assert = pool_incorrect

    common.write_csv(
        ctx.step2_dir / "assertion_counts.csv",
        ["test_case", "result", "assertx_calls_found", "assertx_calls_counted"],
        rows,
    )
    logger.info(
        f"RQ1 assertion counts: Pass_Assert={pass_assert} "
        f"(PASS-test static call sites={pass_static_total} + Target Pool Correct={pool_correct}), "
        f"Fail_Assert={fail_assert} (Target Pool Incorrect) across {len(test_results)} test(s) "
        f"({len(rows)} PASS)."
    )
    return {"pass_assert": pass_assert, "fail_assert": fail_assert, "rows": rows}
