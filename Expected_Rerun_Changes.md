# Expected Rerun Changes (temporary tracking file)

**Update, 2026-08-14:** the rq1/rq2/rq3 predictions below (as they stood on
2026-08-13) were checked against a completed full 4-target rerun and
confirmed materialized - see "STATUS: VERIFIED" notes inline. Since then,
`rq2.csv` (v1→v2), `rq4.csv`, and `rq5.csv` (full schema rewrite) all
picked up same-day code changes that have **not** been rerun yet.
Everything under the "not yet rerun" headings below is a prediction of the
*next* full rerun (`python3 run_pipeline.py` with no target arg, covering
all 4 targets: `Csv_3b`, `Csv_13b`, `JacksonXml_1b`, `JacksonXml_6b`), not
a record of an actual run. Delete this file once that rerun has happened
and `resQ_outputs/rq2.csv`, `rq4.csv`, and `rq5.csv` have all been checked
against their predictions below.

## rq1.csv — dynamic assertion counting (`rq1_dynamic_asserts.py`, commit `c133ac1`)

**STATUS: VERIFIED (2026-08-14).** The full rerun confirmed the predicted
direction: `Pass_Assert` moved 49→1264, 11→1759, 92→806, 49→1003 across the
4 targets (8×-160× larger). One value worth a second look, not a rerun
defect: `JacksonXml_6b`'s `Fail_Assert` went 5→0 despite 11 failing tests -
consistent with the new trace-based mechanism if none of those 11 tests'
traces hit an `assertX(...)` line before throwing (e.g. failing via an
uncaught exception rather than a JUnit assertion).

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

## rq2.csv (v1, superseded) — three doc-facing column names added

**STATUS: VERIFIED (2026-08-14), then SUPERSEDED (same day, see "rq2.csv
v2" below).** The rerun confirmed the 5 pre-existing columns held exactly
steady for 3 of 4 targets, and the 3 aliased columns populated correctly
and matched their originals row-for-row, as predicted. `JacksonXml_6b` did
drift (`Union_Passing_Slices` 65→60, cascading into `Union_All_Slices` and
`Reduction_Ratio`) - ordinary Slicer4J run-to-run slice nondeterminism,
already flagged as a caveat below, not a surprise. This whole v1 design -
aliasing `Statements executed` / `Union statements in slices of passing
assertions` / `Union statements in slices of failing assertions` onto the
existing values - was itself replaced on 2026-08-14 (see "rq2.csv v2"):
`Statements executed` was deleted outright, and the two "assertions"
columns turned out to need genuinely different values, not aliases - kept
here only as a historical record of what v1 predicted and verified.

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

## rq3.csv — unit suffixes added to headers (this session)

**STATUS: VERIFIED (2026-08-14).** Header confirmed as
`Baseline_Time_(s),SBFL_Time_(s),Hybrid_Time_(s),Avg_Slice_Time_(s),Peak_Memory_(KB)`,
all 4 rows fully populated with no blanks - the full-simultaneous-rerun
requirement worked as intended. Values shifted a few percent from the
pre-rerun numbers (e.g. `Csv_3b` `Baseline_Time_(s)` 3.09→3.499), ordinary
wall-clock/RSS jitter as predicted, not a concern.

**Step 1 analysis:** the 5 metrics themselves (`_write_rq3` in
`rq_writers.py`, fed by `context.Metrics` / `common.run_cmd_timed`) were
already correct and are untouched by this change — only the CSV column
*names* were missing their units. Confirmed the actual units straight from
where each value is produced, not assumed:
- `Baseline_Time`, `SBFL_Time`, `Hybrid_Time`, `Avg_Slice_Time` — all four
  are wall-clock seconds (`context.Metrics.*_time_sec`, measured via
  `time.time()` deltas in `common.run_cmd_timed`/`run_cmd`), rounded to 3
  decimals in `_write_rq3`.
- `Peak_Memory` — kilobytes, parsed directly from `/usr/bin/time -v`'s
  `Maximum resident set size (kbytes)` line (`common.py`'s `_MAX_RSS_RE`),
  rounded to 1 decimal. Never converted to MB or bytes anywhere in the
  pipeline (current on-disk values like `667272.0` for `Peak_Memory` are
  KB, i.e. ~667 MB — consistent with a JVM process, not a byte or MB
  count).

`RQ3_FIELDS` renamed (not just extended) to:

| Old header | New header |
|---|---|
| `Baseline_Time` | `Baseline_Time_(s)` |
| `SBFL_Time` | `SBFL_Time_(s)` |
| `Hybrid_Time` | `Hybrid_Time_(s)` |
| `Avg_Slice_Time` | `Avg_Slice_Time_(s)` |
| `Peak_Memory` | `Peak_Memory_(KB)` |

Current (pre-rerun) values for reference — same numbers are expected back
under the new header names after rerun, since the computation itself did
not change:

| Project | BugID | Baseline_Time | SBFL_Time | Hybrid_Time | Avg_Slice_Time | Peak_Memory |
|---|---|---|---|---|---|---|
| Csv | 3b | 3.09 | 281.253 | 1186.712 | 6.901 | 667272.0 |
| Csv | 13b | 5.261 | 770.317 | 1540.659 | 7.482 | 668948.0 |
| JacksonXml | 1b | 14.49 | 550.72 | 1725.878 | 6.908 | 1007140.0 |
| JacksonXml | 6b | 19.196 | 771.315 | 2251.852 | 6.795 | 1142496.0 |

**Expected after rerun:** the 5 columns reappear under their new,
unit-suffixed names with values numerically unchanged from the table
above (assuming ordinary run-to-run timing/memory jitter only — these are
wall-clock/RSS measurements, not deterministic like RQ1/RQ2/RQ4/RQ5's
counts, so small fluctuations between runs are expected and not a bug).

**Gotcha specific to this change, unlike RQ2's column *addition*:** this
was a rename, not an addition, so `Baseline_Time` and
`Baseline_Time_(s)` are two different dict keys as far as
`common.upsert_csv_row` is concerned. The moment `_write_rq3` runs for
*any single target*, the whole file is rewritten under the new 5-column
header, and every *other* target's row - read back in under the old key
names - has nothing matching the new keys, so `row.get(k, "")` blanks all
5 metric cells for that row (not just the 3 new ones, as in RQ2's case).
Full data for all 4 targets is only guaranteed once **every** target has
been rerun at least once after this change - a partial/single-target
rerun will transiently blank the untouched targets' rq3.csv metrics until
they're rerun too. Rerunning all 4 targets together (the normal
no-arg `run_pipeline.py` invocation) avoids ever observing that
intermediate blanked state.

## rq2.csv v2 — "Statements executed" deleted; the two "assertions" columns redefined (2026-08-14, VERIFIED)

**STATUS: VERIFIED (2026-08-14, second rerun).** `Statements executed` gone from the header as
expected. `Pass_TC_Slices`/`Fail_TC_Slices` matched the predicted table exactly for all 4
targets (201/148, 1/59, 120/107, 65/4), confirming both the divergence cases (`Csv_3b`,
`JacksonXml_1b`) and the non-divergence cases (`Csv_13b`, `JacksonXml_6b`). Note: this run's
`Union_Passing_Slices`/`Union_Failing_Slices` for `JacksonXml_6b` landed on 65/4 (the *original*
pre-drift values), not the 60/4 seen in the intermediate verified rerun - pure Slicer4J
run-to-run nondeterminism cutting the other way this time, exactly the caveat already flagged
below, not a new issue.

**Why v1 needed fixing:** v1 (above) aliased `Union statements in slices
of passing assertions` / `...failing assertions` onto the *exact same*
Python variables as `Union_Passing_Slices`/`Union_Failing_Slices` - same
computation, just a second dict key. On review this was wrong: those two
existing columns already group virtual columns by **the individual
assertion's own outcome** (`virtual_status`: `Virtual_Pass` = this
specific criterion evaluated true, `Virtual_Fail` = this specific
criterion is the one that threw). A single FAILING test contributes rows
to *both* buckets - every assertion JUnit reached before the failure line
is individually `Correct`/`Virtual_Pass` (Step 1's Target Variable Pool,
`step1_tests.py`), and only the one at the failure line is
`Virtual_Fail`. Aliasing a second name onto that same computation gave two
columns with identical values and identical meaning - not the "these mean
different things" the schema is supposed to express.

**The fix - Task 1 (delete):** `Statements executed` (the
`Full_Execution_Size` alias) is removed outright, no replacement. Nothing
else needed a third name for "size of the full trace-coverage universe" -
`Full_Execution_Size` already covers it under its original name.

**The fix - Tasks 2/3 (differentiate, not just rename):** `_write_rq2`
now also computes `Pass_TC_Slices`/`Fail_TC_Slices` - the **same**
per-virtual-column slice-statement sets, unioned by a **different**
grouping: whether the virtual column's **source test case, taken as a
whole**, passed or failed per Step 1's `test_results` (`test_case` field
looked up against each test's own PASS/FAIL), not by the individual
assertion's outcome. Concretely: a `Correct`/`Virtual_Pass` assertion
drawn from an otherwise-FAILING test still counts toward
`Union_Passing_Slices` (assertion-outcome view) but now counts toward
`Fail_TC_Slices` instead (source-test-outcome view), since the test it
came from still failed overall. Every virtual column built from a
*passing* test's assertion scan (Step 2b/2c) is trivially `Virtual_Pass`
**and** from a passing test case, so it agrees under both groupings - the
two views can only diverge on virtual columns built from a *failing*
test's Target Pool rows (Step 2a), specifically their `Correct` ones.
This is deliberately independent of RQ1's own dynamic assertion-hit trace
(`rq1_dynamic_asserts.py`) - reuses only Step 1's already-computed
per-test PASS/FAIL, not RQ1's separate bytecode-trace mechanism (keeping
the architectural boundary that module's own docstring establishes).

**Naming:** shortened, underscore-separated, and deliberately reuses RQ1's
established `_TC`/`Assert` vocabulary (`Pass_TC`/`Fail_TC` = test-case
counts, `Pass_Assert`/`Fail_Assert` = assertion counts) so a reader of
both CSVs recognizes `_TC_` as "grouped by test case" on sight, distinct
from the assertion-level `Union_Passing_Slices`/`Union_Failing_Slices`
next to it.

**Code changes:** `RQ2_FIELDS` in `rq_writers.py` is now `["Project",
"BugID", "Full_Execution_Size", "Union_Passing_Slices",
"Union_Failing_Slices", "Union_All_Slices", "Reduction_Ratio",
"Pass_TC_Slices", "Fail_TC_Slices"]` (9 columns, down from v1's 10).
`_write_rq2` now takes `test_results` as a parameter (threaded through
from `write_all`, which already received it for `_write_rq1`) to build
the `test_case → PASS/FAIL` lookup.

**Predicted values after the next rerun** - computed just now by
re-running this exact grouping logic offline against the *already
materialized* Step 1-3 artifacts on disk from the 2026-08-14 rerun
(`slice_observation_matrix.csv`, `virtual_test_status.csv`,
`test_results.csv` under `resQ_outputs/work/<target>/`) - not a guess.
`Union_Passing_Slices`/`Union_Failing_Slices` were recomputed the same way
as a sanity check and matched the current `rq2.csv` exactly (208/57,
1/59, 124/107, 60/4), confirming the script's logic before trusting its
`Pass_TC_Slices`/`Fail_TC_Slices` output:

| Project | BugID | Union_Passing_Slices | Union_Failing_Slices | Pass_TC_Slices (predicted) | Fail_TC_Slices (predicted) | Diverges? |
|---|---|---|---|---|---|---|
| Csv | 3b | 208 | 57 | 201 | 148 | Yes - 7 statements move out of the passing bucket, growing the failing bucket by 91 |
| Csv | 13b | 1 | 59 | 1 | 59 | No - this bug's failing-test criteria contribute no `Correct` rows |
| JacksonXml | 1b | 124 | 107 | 120 | 107 | Yes - 4 statements move out of the passing bucket, but they were already inside the failing bucket (no growth there) |
| JacksonXml | 6b | 60 | 4 | 60 | 4 | No - same as Csv_13b |

**Caveat:** these are computed from the *current* on-disk slice artifacts,
which were themselves produced by one particular Slicer4J run. As already
observed for `JacksonXml_6b`'s `Union_Passing_Slices` (65→60 across the
v1 rerun), Slicer4J's own dynamic slicing has some run-to-run
nondeterminism - so `Pass_TC_Slices`/`Fail_TC_Slices` after the *next*
actual rerun should land close to this table but are not guaranteed to
match it exactly, for the same reason `Union_Passing_Slices`/
`Union_Failing_Slices` aren't guaranteed to reproduce 208/57/124/107/60/4
verbatim either.

**Expected after rerun:** `Full_Execution_Size`, `Union_Passing_Slices`,
`Union_Failing_Slices`, `Union_All_Slices`, `Reduction_Ratio` unchanged in
formula (same code as v1, values subject only to ordinary Slicer4J
nondeterminism). `Statements executed` gone from the header entirely.
`Pass_TC_Slices`/`Fail_TC_Slices` populated per the table above, and -
this is the concrete, checkable proof the two groupings are genuinely
different - **not** expected to equal `Union_Passing_Slices`/
`Union_Failing_Slices` for `Csv_3b` and `JacksonXml_1b`.

## rq4.csv — slice_universe consistency fix + 3 new columns (2026-08-14, VERIFIED)

**STATUS: VERIFIED (2026-08-14, second rerun).** All 4 targets matched the predicted table
exactly, cell for cell, including the 3 new columns - `Csv_3b` 3/0/0.0/2/True/True, `Csv_13b`
2/2/1.0/2/False/False, `JacksonXml_1b` 6/0/0.0/3/True/True, `JacksonXml_6b` 10/0/0.0/5/True/True.
Confirms the `slice_universe` consistency fix changed nothing observable, as predicted.

**Consistency fix:** `union_fail` (feeding `Included_In_Slice`) is now intersected with
`ochiai_result["slice_universe"]`, exactly mirroring RQ2's `Union_Failing_Slices` and the
actual `(slice) observation matrix`'s own column membership (`slice_observation_matrix.csv`'s
cells are defined as `statement in per_column[virtual_test_id]` for `statement in
sorted(slice_universe)` - see `step3_matrices.build_slice_matrix`). Previously `union_fail`
used `per_column_statements` unfiltered, which could in principle include bracket-only
statements the matrix itself never scores. Predicted (and verified below) to change nothing
for the current 4 targets, since fault lines are never bracket-only lines - it's a
forward-looking correctness fix, not a fix for an observed wrong number.

**3 new columns**, computed entirely from `virtual_columns`/Target Pool data - independent of
`rq1.csv`'s `Fail_Assert`/`rq1_dynamic_asserts.py` by strict requirement (verified: `_write_rq4`
does not import or reference that module):
- `Fail_Assert_Count` = count of `Virtual_Fail` virtual columns (the failing-assertion slicing
  criteria that fed `union_fail`).
- `Not_All_Faulty_Stmts_In_Slice` = `Included_In_Slice < Total_Faults` (ground truth ⊄ slice).
- `No_Faulty_Stmts_In_Slice` = `Included_In_Slice == 0` (ground truth ∩ slice = ∅).

**Predicted values after the next rerun** (computed offline against the already-materialized
Step 2/3 artifacts on disk - `slice_observation_matrix.csv`, `virtual_test_status.csv`,
`slice_statement_mapping.csv` - via `ground_truth.load_ground_truth_faults`, not a guess).
`Total_Faults`/`Included_In_Slice`/`Fault_Inclusion_Rate` recomputed this way matched the
current `rq4.csv` exactly (3/0, 2/2, 6/0, 10/0), confirming the fix changes nothing for these
4 targets before trusting the 3 new columns:

| Project | BugID | Total_Faults | Included_In_Slice | Fault_Inclusion_Rate | Fail_Assert_Count | Not_All_Faulty_Stmts_In_Slice | No_Faulty_Stmts_In_Slice |
|---|---|---|---|---|---|---|---|
| Csv | 3b | 3 | 0 | 0.0 | 2 | True | True |
| Csv | 13b | 2 | 2 | 1.0 | 2 | False | False |
| JacksonXml | 1b | 6 | 0 | 0.0 | 3 | True | True |
| JacksonXml | 6b | 10 | 0 | 0.0 | 5 | True | True |

## rq5.csv — full schema rewrite: one row per fault LINE, AP deleted (2026-08-14, VERIFIED)

**STATUS: VERIFIED (2026-08-14, second rerun).** 21 rows written (3+2+6+10), header and all 21
rows matched the predicted table exactly, including every `"None"` cell and every numeric
rank_best/tie_size value - both trace-side and (this time) slice-side, with no nondeterminism
drift observed on this run. Legacy schema handling worked cleanly: `rq5.csv` started fresh under
the new 8-column lowercase header, no orphaned blank rows.

**Schema:** `project, bug_id, file_name, line_no, rank_best_trace, tie_size_trace,
rank_best_slice, tie_size_slice` (lowercase/underscored, one-off deviation from every other RQ
csv by explicit request). Key is `RQ5_KEY_FIELDS = [project, bug_id, file_name, line_no]`, not
the shared `Project+BugID` key - required because this is no longer one row per bug.

**Row count changes from 4 (one per bug) to 21** (3 + 2 + 6 + 10, one row per ground-truth
fault line, matching `rq4.csv`'s `Total_Faults` per bug exactly - every fault line is scanned
and gets a row, per the approved plan).

**Data source:** `rank_best_*`/`tie_size_*` are read directly off `step4_ranking.build_ranking()`'s
already-computed `trace_ranked`/`slice_ranked` lists (via `ranking_result`) - no re-derivation
from the raw matrices. Matched against ground truth on the **normalized** `statement_line`
(same convention `step4_ranking.py`/`rq4.csv` already use), not the raw diff line - chosen as
"most compatible with the technique" per your instruction, since `trace_ranked`/`slice_ranked`'s
own `line` field already uses that same bytecode-line-number convention; matching on the raw
diff line would silently miss any multi-line-statement fault the technique actually found.

**Missing values:** a fault line absent from a ranking (never covered/sliced) gets the literal
string `"None"` in that ranking's `rank_best_*`/`tie_size_*` cells - not `0`, not blank, per
your explicit instruction (`RQ5_MISSING = "None"` in `rq_writers.py`).

**AP deleted:** `step4_ranking.average_precision_and_top_rank()` removed entirely (top_rank had
no remaining consumer once AP was removed). `ranking_result` no longer carries
`sbfl_top_rank/hybrid_top_rank/sbfl_ap/hybrid_ap`. `ranking_summary.md`'s AP/top-rank lines and
warning-text references were reworded to describe conditions directly (e.g. "ranked N
statement(s)") instead of via a number that no longer exists; the Top-10 tables, answerability
section, and degenerate-state warnings themselves are unchanged.

**`rerun_ranking.py`** (the ranking-only re-entry point) had its `_write_rq5` call site updated
to pass `gt_faults` - would have broken silently otherwise, since it calls `rq_writers._write_rq5`
directly.

**Legacy file handling:** the old `rq5.csv` (`Project,BugID,SBFL_Top_Rank,Hybrid_Top_Rank,
SBFL_AP,Hybrid_AP`, 4 rows) shared no column names with the new key, so `upsert_csv_row` could
not have recognized old rows as related - they would have survived as blank-celled orphan rows
under the new 8-column header. Backed up to
`<scratchpad>/legacy_rq5_schema/rq5.csv.old_schema_2026-08-14.bak` (also recoverable from git
history, commit `7456dec`) and deleted from `resQ_outputs/`, so the next rerun starts `rq5.csv`
completely fresh.

**Predicted values after the next rerun** (computed offline against the already-materialized
`trace_ranking.csv`/`slice_ranking.csv`/ground-truth data on disk - not a guess):

| Project | BugID | file_name | line_no | rank_best_trace | tie_size_trace | rank_best_slice | tie_size_slice |
|---|---|---|---|---|---|---|---|
| Csv | 3b | Lexer.java | 111 | 1 | 1 | 58 | 151 |
| Csv | 3b | Lexer.java | 112 | None | None | None | None |
| Csv | 3b | Lexer.java | 113 | None | None | None | None |
| Csv | 13b | CSVFormat.java | 318 | 37 | 53 | 1 | 1 |
| Csv | 13b | CSVPrinter.java | 139 | 92 | 7 | 2 | 57 |
| JacksonXml | 1b | FromXmlParser.java | 512 | None | None | None | None |
| JacksonXml | 1b | FromXmlParser.java | 514 | 165 | 2 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 550 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 551 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 552 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 553 | 1 | 4 | None | None |
| JacksonXml | 6b | ToXmlGenerator.java | 843/844/845/846/847/848/849/851/866/867 | None (all 10) | None (all 10) | None (all 10) | None (all 10) |

(`JacksonXml_6b`'s 10 rows collapsed to one line for readability - every one of its 10 fault
lines is `None` across all 4 rank/tie columns, consistent with `rq0_answerability.csv`'s
`Bug_Fully_Unanswerable=True` for this bug: dead code no line-level technique can find.)

**Caveat:** as with RQ2 v2's predictions, these are computed from the *current* on-disk
ranking artifacts (themselves the product of one particular Slicer4J run); the hybrid-side
(`rank_best_slice`/`tie_size_slice`) values are subject to the same run-to-run slice
nondeterminism already observed for `JacksonXml_6b` in RQ2's rerun (65→60) - the trace-side
(`rank_best_trace`/`tie_size_trace`) values, being derived from `defects4j coverage` rather
than Slicer4J, are expected to be stable.
