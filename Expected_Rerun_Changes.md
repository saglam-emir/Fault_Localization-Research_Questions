# RQ Methodology History & Current Status

**Purpose of this file changed on 2026-08-25.** It started as a temporary
"prediction vs. actual rerun" tracking file (see the dated sections below).
The full 4-target rerun those sections were waiting on has now actually
happened (**2026-08-24, `python3 run_pipeline.py`, no target arg, all 4
targets `OK`**), so nothing in this file is a prediction any more - every
number below is either what actually landed in `resQ_outputs/*.csv` on
disk, or a deliberately preserved historical record.

**This file is being kept (not deleted) for a second reason:** `rq1.csv`
and `rq2.csv` each went through multiple genuinely different computation
methodologies during this internship, not just bug fixes. That history -
what each methodology counted, why it was replaced, and the concrete
before/after numbers - is exactly the kind of material an end-of-internship
report needs ("we tried X, found it measured the wrong thing because Y,
switched to Z"). Deleting this file would lose that trail. **Do not delete
this file; keep appending to it if rq1/rq2's methodology changes again.**

---

## Current status summary (as of the 2026-08-24 full rerun)

All 4 targets (`Csv_3b`, `Csv_13b`, `JacksonXml_1b`, `JacksonXml_6b`) ran
to completion with no `StepFailure`/crash. Current on-disk values:

**rq0_answerability.csv** *(now gitignored - see "Repo housekeeping" at the
bottom; kept on disk, just no longer version-controlled)*

| Project | BugID | Total_Fault_Lines | Unanswerable_Fault_Lines | Bug_Fully_Unanswerable |
|---|---|---|---|---|
| Csv | 3b | 3 | 0 | False |
| Csv | 13b | 2 | 0 | False |
| JacksonXml | 1b | 6 | 0 | False |
| JacksonXml | 6b | 10 | 10 | True |

**rq1.csv** (methodology: static assertion-count, "v3" below)

| Project | BugID | Pass_TC | Fail_TC | Pass_Assert | Fail_Assert |
|---|---|---|---|---|---|
| Csv | 3b | 73 | 4 | 249 | 2 |
| Csv | 13b | 208 | 4 | 402 | 2 |
| JacksonXml | 1b | 131 | 6 | 373 | 3 |
| JacksonXml | 6b | 174 | 11 | 481 | 0 |

**rq2.csv** (methodology: "v3" swapped column mapping, see rq2 section below)

| Project | BugID | Full_Execution_Size | Union_Passing_Slices | Union_Failing_Slices | Union_All_Slices | Reduction_Ratio | Pass_TC_Slices | Fail_TC_Slices |
|---|---|---|---|---|---|---|---|---|
| Csv | 3b | 443 | 204 | 148 | 211 | 0.523702 | 211 | 57 |
| Csv | 13b | 609 | 1 | 59 | 59 | 0.90312 | 1 | 59 |
| JacksonXml | 1b | 1198 | 120 | 107 | 124 | 0.896494 | 124 | 107 |
| JacksonXml | 6b | 1334 | 65 | 4 | 65 | 0.951274 | 65 | 4 |

**rq3.csv** (wall-clock/RSS measurements - expect run-to-run jitter, not deterministic)

| Project | BugID | Baseline_Time_(s) | SBFL_Time_(s) | Hybrid_Time_(s) | Avg_Slice_Time_(s) | Peak_Memory_(KB) |
|---|---|---|---|---|---|---|
| Csv | 3b | 4.903 | 285.153 | 1291.759 | 7.887 | 811928.0 |
| Csv | 13b | 5.798 | 775.09 | 1548.1 | 7.474 | 924524.0 |
| JacksonXml | 1b | 15.063 | 553.546 | 1770.754 | 7.092 | 1223568.0 |
| JacksonXml | 6b | 19.881 | 751.219 | 2253.53 | 7.34 | 1408432.0 |

**rq4.csv**

| Project | BugID | Total_Faults | Included_In_Slice | Fault_Inclusion_Rate | Fail_Assert_Count | Not_All_Faulty_Stmts_In_Slice | No_Faulty_Stmts_In_Slice |
|---|---|---|---|---|---|---|---|
| Csv | 3b | 2 | 0 | 0.0 | 2 | True | True |
| Csv | 13b | 2 | 2 | 1.0 | 2 | False | False |
| JacksonXml | 1b | 6 | 0 | 0.0 | 3 | True | True |
| JacksonXml | 6b | 10 | 0 | 0.0 | 5 | True | True |

**rq5.csv** (21 rows → 20 rows this run - see "Ground-truth proxy fix" below for why)

| Project | BugID | file_name | line_no | rank_best_trace | tie_size_trace | rank_best_slice | tie_size_slice |
|---|---|---|---|---|---|---|---|
| Csv | 3b | Lexer.java | 90 | 10 | 3 | 58 | 154 |
| Csv | 3b | Lexer.java | 111 | 1 | 1 | 58 | 154 |
| Csv | 13b | CSVFormat.java | 318 | 37 | 53 | 1 | 1 |
| Csv | 13b | CSVPrinter.java | 139 | 92 | 7 | 2 | 57 |
| JacksonXml | 1b | FromXmlParser.java | 510 | 258 | 21 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 514 | 165 | 2 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 550 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 551 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 552 | 1 | 4 | None | None |
| JacksonXml | 1b | FromXmlParser.java | 553 | 1 | 4 | None | None |
| JacksonXml | 6b | ToXmlGenerator.java | 843/844/845/846/847/848/849/851/866/867 | None (all 10) | None (all 10) | None (all 10) | None (all 10) |

**Ground-truth proxy fix (new this rerun, affects rq0/rq4/rq5 together):**
`ground_truth.apply_control_dependence_proxy` now resolves an otherwise-dead
("approximate", pure-deletion) fault anchor to the nearest *executed*
control-dependence-ancestor statement instead of leaving it permanently
unanswerable. This rescued 3 fault lines across 2 bugs:
- **Csv/3b:** `Lexer.java:112` and `:113` (both dead) both resolved to the
  *same* ancestor line, `:90` - so `rq5.csv`'s two `None` rows collapsed
  into one real row (`:90`, now ranked), and `rq4.csv`'s `Total_Faults`
  dropped 3→2 (it counts *distinct* resolved `(file, line)` pairs, so two
  raw fault lines sharing one resolved line count once). `rq0.csv` still
  reports `Total_Fault_Lines=3` (it counts raw, non-deduplicated fault
  entries), just with `Unanswerable_Fault_Lines` now `0` instead of `2`.
- **JacksonXml/1b:** `FromXmlParser.java:512` (dead) resolved to `:510`,
  which did *not* collide with any other fault line, so `rq4.csv`'s
  `Total_Faults` stayed at 6 and `rq5.csv`'s row count stayed at 6 for this
  bug - only the line number and rank changed (`None` → `rank_best_trace=258`,
  still `None` on the slice side).
- `Csv/13b` and `JacksonXml_6b` were unaffected (13b had no unanswerable
  lines to begin with; 6b's 10 lines are genuinely dead code with no
  executed ancestor to proxy to - `Bug_Fully_Unanswerable` stays `True`).

---

## RQ1.csv — methodology history

Three genuinely different computation methodologies, in chronological
order. **v3 (static, below) is CURRENT/FINAL** as of the 2026-08-24 rerun.

### v3 — static assertion-count (CURRENT/FINAL, verified 2026-08-24)

**Why v2 (dynamic trace) was replaced** - found wrong on two independent
axes while cross-checking `rq1.csv` against the RQ1 task description:

1. **Granularity mismatch.** The task requires "each assertion gets its own
   slice" - i.e. one countable observation per *static* `assertX(...)` call
   site. v2's dynamic-trace mechanism instead counted every *runtime
   execution* of that line, so an assertion inside a loop iterating N times
   counted N times instead of once - inflating `Pass_Assert` by roughly
   2-5x with no connection to how many slices the technique actually
   produces.
2. **A silent self-contradiction on `Fail_Assert`.** For at least one case
   (Csv-3b's `testBackslashEscaping`), v2's dynamic trace and Step 1's own
   Target Pool *disagreed* about whether the same assertion passed or
   failed - Target Pool said `Correct` (based on the test's own stack-trace
   failure line), the trace said the chronologically-last hit was the
   failure (based on an *unbounded* re-scan of all assertion lines in the
   method, not fail-line-bounded like Step 1's). Only one can be right;
   Target Pool is what Step 2 actually slices on, so it is authoritative.

Also clarified against the task description: `Fail_TC` and `Fail_Assert`
are **not** expected to always be equal, contrary to a footnote in an
earlier draft of the RQ1 description. Some Defects4J bugs fail every one of
their triggering tests via an *uncaught exception*, never reaching an
`assertX(...)` call at all (`JacksonXml_6b`: all 11 failing tests are
exception-driven, 0 involve a real assertion failing) - those correctly
contribute 0 to `Fail_Assert` while still counting toward `Fail_TC`.

**Logic** (`rq1_dynamic_asserts.compute`, takes `target_pool` as a third
argument):

```
fail_assert = count(Target Pool rows with status=="Incorrect")
pass_assert = count(Target Pool rows with status=="Correct")
            + count(static, variable-resolvable assertX(...) call sites
                    across EVERY PASSING test's own method body - not just
                    the subset Step 2's 2b/2c selects as slicing criteria)
```

No Slicer4J run is issued by this module any more (v2's whole
`_assert_trace_only`/`_trace_only_attempt` mechanism is gone) - it costs
nothing beyond AST parses Step 1 already pays for. Output file renamed:
`assertion_execution_counts.csv` → `assertion_counts.csv`.

**VERIFIED 2026-08-24** - the actual full rerun's static counts matched the
offline hand-computed prediction exactly for all 4 targets:

| Project | BugID | Pass_TC | Fail_TC | Pass_Assert (v2, dynamic) | **Pass_Assert (v3, static)** | Fail_Assert (v2) | **Fail_Assert (v3)** |
|---|---|---|---|---|---|---|---|
| Csv | 3b | 73 | 4 | 1264 | **249** | 3 | **2** |
| Csv | 13b | 208 | 4 | 1759 | **402** | 2 | **2** |
| JacksonXml | 1b | 131 | 6 | 809 | **373** | 3 | **3** |
| JacksonXml | 6b | 174 | 11 | 1046 | **481** | 0 | **0** |

(The pre-migration offline prediction table used `819` for JacksonXml/1b's
v2 `Pass_Assert` rather than the `809` actually seen in the pre-rerun
committed `rq1.csv` - a 10-count drift consistent with v2's own dynamic-trace
nondeterminism, not a discrepancy in v3. v3's own numbers are deterministic
static AST counts and reproduced exactly.)

**Root cause of the Csv/3b `Fail_Assert` 3→2 change, confirmed against
`target_variable_pool.csv`:** of Csv/3b's 3 genuine ground-truth failing
tests, only 2 (`testEscapedMySqlNullValue`, `testEscapedCharacter`) throw
directly from an `assertThat(...)` call inside the test method - the third
(`testBackslashEscaping`) actually fails inside a helper method
(`Utils.compare(...)`, called via `assertArrayEquals`), which Step 1's
AST-based Target Pool scan cannot see as a direct call site in the test
body, so it contributes only a `Correct` row (from an earlier, unrelated
assertion in the same test that did hold) and zero `Incorrect` rows - 0
contribution to `Fail_Assert`, per this methodology's own documented rule
("a failing test that crashed before reaching any assertX(...) call
contributes 0"). A 4th test (`CSVFileParserTest::testCSVFile`) shows up as
`FAIL` in the per-test *isolated* run (`Pass_TC`/`Fail_TC`'s source) but is
**not** one of Defects4J's genuine ground-truth failing tests (an
order-dependent flaky test - logged as a "Discrepancy" warning during the
rerun) and correctly contributes nothing to either `Pass_Assert` or
`Fail_Assert` under v3, since Target Pool is scoped to genuine failing
tests only.

### v2 — dynamic bytecode-trace execution count (HISTORICAL, commit `c133ac1`, superseded 2026-08-2x)

Read Slicer4J's own bytecode-level dynamic execution trace
(`trace.log_icdg.log`, a byproduct of every backward slice it runs) and
counted **every dynamic hit** on an `assertX(...)` line, once per loop
iteration actually executed. For a passing test Step 2 never sliced (the
large majority), one throwaway "trace-only" Slicer4J run was issued purely
to obtain its trace (bypassing `ctx.metrics` so it didn't pollute RQ3).
Classification: every hit was a Pass except, for a failing test, the
chronologically last hit (the exact instruction whose `AssertionError`
ended the method).

**Rationale at the time:** v1 (below) was scoped only to Step 1/2's
selective Target-Pool/slicing-criterion set, undercounting the "how many
assertions does the suite actually execute" question the task intended.
v2 widened the count to every dynamic hit, suite-wide.

**Verified values (2026-08-14 rerun, before v2 was itself found wrong):**
`Pass_Assert` moved 49→1264, 11→1759, 92→809, 49→1046 across the 4 targets
(8x-160x larger than v1). One value flagged as worth a second look at the
time, not a defect: `JacksonXml_6b`'s `Fail_Assert` went 5→0 despite 11
failing tests - correctly consistent with none of those 11 tests' traces
ever hitting an `assertX(...)` line before throwing (all exception-driven,
confirmed again under v3 above).

### v1 — Target-Pool-scoped selective count (HISTORICAL, pre-`c133ac1`)

```
pass_assert = count(Target Pool rows with status=="Correct") + count(passed_variable_matches)
fail_assert = count(Target Pool rows with status=="Incorrect")
```

i.e. scoped only to the assertions Step 1/2 actually selected as
slicing-criterion candidates (`passed_variable_matches` = the passing-test
assertions whose variable name matched the Target Pool), not every
assertion the suite executed or every assertion in a passing test's body.
Values at the time: Csv/3b 49/2, Csv/13b 11/2, JacksonXml/1b 92/3,
JacksonXml/6b 49/5.

**Summary for the report:** v1 undercounted (too narrow a scope), v2
overcounted (wrong granularity - dynamic hits instead of static call
sites, plus a Target-Pool disagreement bug), v3 is the methodology that
actually matches the RQ1 task description's "each assertion = one
observation" framing and is internally consistent with what Step 2 slices
on.

---

## RQ2.csv — methodology history

Three generations of `RQ2_FIELDS`/`_write_rq2`. **v3 (below) is
CURRENT/FINAL** as of the 2026-08-25 code change + 2026-08-24 rerun data
(the code change was made and the data regenerated in the same rerun this
file's "current status" table above reflects).

### v3 — swapped column-to-grouping mapping (CURRENT/FINAL, code changed 2026-08-25)

**This supersedes v2's column mapping below on the basis of separate,
user-supplied project documentation** (not a bug found by re-reading the
code or re-deriving from data) that defines the two column pairs the
opposite way from how v2 built them. Formulas, unchanged in *mechanism*
from v2, just swapped in which one populates which column:

```
Union_Passing_Slices / Union_Failing_Slices =
    per-virtual-column slice statements, unioned by GROUPING ON THE VIRTUAL
    COLUMN'S SOURCE TEST CASE'S OVERALL OUTCOME (test_results PASS/FAIL)

Pass_TC_Slices / Fail_TC_Slices =
    the SAME per-virtual-column slice statements, unioned by GROUPING ON
    THE INDIVIDUAL ASSERTION'S OWN OUTCOME (virtual_status: Virtual_Pass/
    Virtual_Fail)

Union_All_Slices = Union_Passing_Slices ∪ Union_Failing_Slices (i.e. now
    built from the TC-grouped sets, not the assertion-grouped sets)
Reduction_Ratio  = 1 - |Union_All_Slices| / Full_Execution_Size (same
    formula, now over the TC-grouped union)
```

**⚠️ Known open tension, flagged explicitly for the report:** this mapping
is the *exact opposite* of what v2 below was deliberately designed and
verified to do - v2's own commit message picked the `_TC_` substring
specifically so a reader would recognize "`_TC_` = grouped by test case"
by analogy with `rq1.csv`'s `Pass_TC`/`Fail_TC`, and v2 was confirmed
correct via an actual verified rerun (2026-08-14, numbers below matched
predictions exactly). When this contradiction surfaced during the
2026-08-25 session, the decision was made to trust the newer,
user-supplied documentation over v2's in-repo design rationale and keep
v3's mapping - see that session's transcript for the full back-and-forth.
**For the report:** this is worth stating as an explicit methodological
decision point, not silently resolved - both mappings are internally
consistent and individually well-reasoned; they simply disagree with each
other on what `Union_Passing_Slices` vs. `Pass_TC_Slices` should mean, and
v3 was chosen on external-documentation authority rather than re-deriving
which one the original task intended.

**Current values (2026-08-24 rerun, v3 mapping in effect):**

| Project | BugID | Full_Execution_Size | Union_Passing_Slices (TC-grouped) | Union_Failing_Slices (TC-grouped) | Union_All_Slices | Reduction_Ratio | Pass_TC_Slices (assertion-grouped) | Fail_TC_Slices (assertion-grouped) |
|---|---|---|---|---|---|---|---|---|
| Csv | 3b | 443 | 204 | 148 | 211 | 0.523702 | 211 | 57 |
| Csv | 13b | 609 | 1 | 59 | 59 | 0.90312 | 1 | 59 |
| JacksonXml | 1b | 1198 | 120 | 107 | 124 | 0.896494 | 124 | 107 |
| JacksonXml | 6b | 1334 | 65 | 4 | 65 | 0.951274 | 65 | 4 |

(Sanity check: for Csv/3b and JacksonXml/1b, note this table's
`Union_Passing_Slices`/`Union_Failing_Slices` columns numerically equal
v2's verified `Pass_TC_Slices`/`Fail_TC_Slices` values below, and vice
versa - a pure relabeling of which grouping populates which column name,
not a change in either grouping's own computation.)

### v2 — differentiated columns, original mapping (HISTORICAL, verified 2026-08-14, superseded 2026-08-25)

**STATUS AT THE TIME: VERIFIED (2026-08-14, second rerun).** `Pass_TC_Slices`/
`Fail_TC_Slices` matched the predicted table exactly for all 4 targets
(201/148, 1/59, 120/107, 65/4 under v2's mapping), confirming both the
divergence cases (`Csv_3b`, `JacksonXml_1b`) and non-divergence cases
(`Csv_13b`, `JacksonXml_6b`).

**Why v1 (aliasing, further below) needed fixing:** v1 aliased "Union
statements in slices of passing/failing assertions" onto the *exact same*
Python variables as `Union_Passing_Slices`/`Union_Failing_Slices` - same
computation, second dict key, not the "these mean different things" the
schema was supposed to express.

**v2's mapping (original, pre-swap):**

```
Union_Passing_Slices / Union_Failing_Slices =
    per-virtual-column slice statements, grouped by THE INDIVIDUAL
    ASSERTION'S OWN OUTCOME (virtual_status: Virtual_Pass/Virtual_Fail).
    Virtual_Pass = this specific criterion evaluated true at runtime;
    Virtual_Fail = this specific criterion is the one that threw. A single
    FAILING test contributes to BOTH buckets: every assertion reached
    before the failure line is individually Correct/Virtual_Pass (Step 1's
    Target Variable Pool), and only the one at the failure line is
    Virtual_Fail.

Pass_TC_Slices / Fail_TC_Slices =
    the SAME per-virtual-column slice statements, grouped by whether the
    virtual column's SOURCE TEST CASE, taken as a whole, passed or failed
    per Step 1's test_results - not by the individual assertion's outcome.
    Concretely: a Correct/Virtual_Pass assertion drawn from an otherwise-
    FAILING test counted toward Union_Passing_Slices (assertion-outcome
    view) but toward Fail_TC_Slices (source-test-outcome view), since the
    test it came from still failed overall. The two views could only
    diverge on virtual columns built from a failing test's Target Pool
    rows (Step 2a) - every virtual column from a passing test's assertion
    scan (2b/2c) is trivially Virtual_Pass AND from a passing test case,
    so it agreed under both groupings.
```

**Naming rationale at the time (now inverted by v3 above):** "shortened,
underscore-separated, and deliberately reuses RQ1's established `_TC`/
`Assert` vocabulary (`Pass_TC`/`Fail_TC` = test-case counts) so a reader of
both CSVs recognizes `_TC_` as 'grouped by test case' on sight, distinct
from the assertion-level `Union_Passing_Slices`/`Union_Failing_Slices` next
to it."

**Verified divergence table (2026-08-14):**

| Project | BugID | Union_Passing_Slices | Union_Failing_Slices | Pass_TC_Slices | Fail_TC_Slices | Diverges? |
|---|---|---|---|---|---|---|
| Csv | 3b | 208 | 57 | 201 | 148 | Yes - 7 statements move out of the passing bucket, growing the failing bucket by 91 |
| Csv | 13b | 1 | 59 | 1 | 59 | No - this bug's failing-test criteria contribute no `Correct` rows |
| JacksonXml | 1b | 124 | 107 | 120 | 107 | Yes - 4 statements move out of the passing bucket, already inside the failing bucket |
| JacksonXml | 6b | 60 | 4 | 60 | 4 | No - same as Csv_13b |

(`JacksonXml_6b`'s `Union_Passing_Slices` shows `60` here vs. `65` in the
current-status table above - ordinary Slicer4J run-to-run slice
nondeterminism between the 2026-08-14 and 2026-08-24 reruns, not a v2/v3
mapping effect; see the caveat under v1 below, and `Daily_Activity_Report.md`'s
note on Soot's own documented multi-threaded instrumentation flakiness.)

### v1 — alias columns (HISTORICAL, verified then superseded same day, 2026-08-14)

Added three doc-facing column names as pure aliases of the 5 pre-existing
columns (`Statements executed` → `Full_Execution_Size`, `Union statements
in slices of passing/failing assertions` → `Union_Passing_Slices`/
`Union_Failing_Slices` - same numbers, no new computation). Deleted the
same day once review found the two "assertions" columns needed genuinely
different values, not aliases (→ v2 above). `Statements executed` had no
replacement - `Full_Execution_Size` already covers that meaning.

**Caveat carried forward from this generation, still relevant:**
Slicer4J's dynamic slicing has real run-to-run nondeterminism (observed:
`JacksonXml_6b`'s `Union_Passing_Slices` 65→60→65 across three different
reruns) - any single rerun's `rq2.csv`/`rq5.csv` slice-side numbers should
be read as "this run's slice," not as a perfectly reproducible constant,
even with the methodology otherwise unchanged.

---

## Repo housekeeping (2026-08-25)

- `.gitignore`: added `resQ_outputs/work/**/result_s_*.csv` (Slicer4J's
  own timestamped per-criterion raw result dumps - thousands of files,
  transient instrumentation noise) and `resQ_outputs/rq0_answerability.csv`
  (auxiliary answerability classification, not one of the 5 core RQs -
  excluded from version control per request; the file itself still lives
  on disk and is regenerated every rerun, it is just no longer tracked).
  `git rm --cached` was run once to stop tracking the already-committed
  `rq0_answerability.csv`.
- `assertion_execution_counts.csv` → `assertion_counts.csv` rename (from
  RQ1 v3 above) means the old file is left stale under
  `resQ_outputs/work/<target>/step2_slicing/` - harmless, ignore it.
