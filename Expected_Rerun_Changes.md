# Expected Rerun Changes (temporary tracking file)

Status as of 2026-08-13: code changes below are committed to the pipeline
scripts, but `run_pipeline.py` has **not** been re-executed for any target.
Everything in this file is a prediction of what the next full rerun
(`python3 run_pipeline.py` with no target arg, covering all 4 targets:
`Csv_3b`, `Csv_13b`, `JacksonXml_1b`, `JacksonXml_6b`) will change in
`resQ_outputs/rq1.csv`, `resQ_outputs/rq2.csv`, and `resQ_outputs/rq3.csv` —
not a record of an actual run. Delete this file once the rerun has happened
and the three CSVs have been checked against it.

## rq1.csv — dynamic assertion counting (`rq1_dynamic_asserts.py`, commit `c133ac1`)

Current `Pass_Assert`/`Fail_Assert` values on disk were written by the
**old** logic (`_write_rq1`, pre-`c133ac1`):

```
pass_assert = count(Target Pool rows with status == "Correct") + count(passed_variable_matches)
fail_assert = count(Target Pool rows with status == "Incorrect")
```

i.e. a *selective* count scoped to Step 1/2's slicing-criterion pool, not
every assertion the suite actually executed.

The new logic (`rq1_dynamic_asserts.compute`, already wired into
`_write_rq1`) instead reads Slicer4J's own bytecode-level execution trace
and counts **every** dynamic hit on an `assertX(...)` line, per iteration
actually run, with a failing test's assertions-after-the-throw correctly
excluded because they never produced a trace row. Because it is no longer
scoped to the Target Pool, this is expected to be a strictly wider
(⇒ generally larger) count than the current values, especially for:
- passing tests whose assertions never matched the Target Pool (previously
  contributed 0 to `Pass_Assert`, will now contribute their real dynamic
  hit count via a throwaway trace-only Slicer4J run);
- any assertion inside a loop that iterates more than once (previously
  counted once per Target Pool row; now counted once per iteration).

Current (pre-rerun) values, for reference:

| Project | BugID | Pass_TC | Fail_TC | Pass_Assert (old) | Fail_Assert (old) |
|---|---|---|---|---|---|
| Csv | 3b | 73 | 4 | 49 | 2 |
| Csv | 13b | 208 | 4 | 11 | 2 |
| JacksonXml | 1b | 131 | 6 | 92 | 3 |
| JacksonXml | 6b | 174 | 11 | 49 | 5 |

**Expected after rerun:** `Pass_TC`/`Fail_TC` unchanged (test outcomes
aren't touched by this change). `Pass_Assert`/`Fail_Assert` recomputed from
the trace and expected to move (most likely upward, per above) to the true
dynamic-execution counts; exact numbers are unknown until the rerun
actually happens — no number in this section should be treated as the
predicted new value, only the direction/mechanism of the change.

## rq2.csv — three doc-facing column names added (this session)

**Important finding from Step 1's analysis, before making any change:**
the three union columns first requested in this session's original prompt
(`Union_Passing_Slices`, `Union_Failing_Slices`, `Union_All_Slices`) were
**not missing** — they've existed in `RQ2_FIELDS`/`_write_rq2` since the
very first pipeline commit (`b1457e1`) and `rq2.csv` already holds real
computed data for all 4 targets. Neither that logic nor any of its
upstream inputs (`step1_tests.py`, `step2_slicing.py`, `step3_matrices.py`,
`ground_truth.py`) were touched by the RQ1 dynamic-assertion work in
`c133ac1`, so those 5 existing columns are **not expected to change** on
rerun (barring ordinary Slicer4J run-to-run flakiness in the underlying
slices themselves).

What *was* actually missing, per the corrected request, were three
columns under specific doc-facing names. `_write_rq2` now also emits these
as aliases of the existing values (same sets, same numbers - no new
computation, see code comment in `rq_writers.py`):

| New column | Alias of | Meaning |
|---|---|---|
| `Statements executed` | `Full_Execution_Size` | size of the full dynamic trace-coverage universe (`defects4j coverage`, all tests) |
| `Union statements in slices of passing assertions` | `Union_Passing_Slices` | union of dynamic-slice statements across all `Virtual_Pass` columns, intersected with the filtered slice universe |
| `Union statements in slices of failing assertions` | `Union_Failing_Slices` | same, for `Virtual_Fail` columns |

`RQ2_FIELDS` is now 10 columns (was 7); `common.upsert_csv_row` fills the 3
new cells as `""` for any row it doesn't rewrite, so the very next
`upsert_csv_row("rq2.csv", ...)` call for *any single target* will already
widen the on-disk header to 10 columns, leaving the other, not-yet-rerun
targets' rows blank in the 3 new columns until they are rerun too.

Current (pre-rerun) values for the 5 pre-existing columns, for reference —
after a full rerun, the 3 new columns should simply equal
`Full_Execution_Size`, `Union_Passing_Slices`, `Union_Failing_Slices`
respectively, row for row:

| Project | BugID | Full_Execution_Size | Union_Passing_Slices | Union_Failing_Slices | Union_All_Slices | Reduction_Ratio |
|---|---|---|---|---|---|---|
| Csv | 3b | 443 | 208 | 57 | 208 | 0.530474 |
| Csv | 13b | 609 | 1 | 59 | 59 | 0.90312 |
| JacksonXml | 1b | 1198 | 124 | 107 | 124 | 0.896494 |
| JacksonXml | 6b | 1334 | 65 | 4 | 65 | 0.951274 |

**Expected after rerun:**
- `Full_Execution_Size`, `Union_Passing_Slices`, `Union_Failing_Slices`,
  `Union_All_Slices`, `Reduction_Ratio` — unchanged (same code path, same
  upstream data as before this session).
- `Statements executed`, `Union statements in slices of passing
  assertions`, `Union statements in slices of failing assertions` — newly
  populated, and should exactly match the current values of
  `Full_Execution_Size`, `Union_Passing_Slices`, `Union_Failing_Slices`
  respectively for the same row.
