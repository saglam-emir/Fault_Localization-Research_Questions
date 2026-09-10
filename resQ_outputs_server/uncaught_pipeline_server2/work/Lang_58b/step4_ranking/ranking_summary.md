# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 454), ('NumberUtils.java', 455)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('NumberUtils.java', 454, '->', 450), ('NumberUtils.java', 455, '->', 450)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/math/NumberUtils.java', 454), ('src/java/org/apache/commons/lang/math/NumberUtils.java', 455)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 1283 statement(s)
- Hybrid ranked 139 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | NumberUtils.java:464 | 0.267261 | `*  <li>It returns <code>0</code> if the values are equal.` |
| 1 | 2 | NumberUtils.java:1508 | 0.267261 | `` |
| 3 | 18 | NumberUtils.java:401 | 0.218218 | `* <p>Gets the minimum of three <code>int</code> values.</p>` |
| 3 | 18 | NumberUtils.java:404 | 0.218218 | `* @param b  value 2` |
| 3 | 18 | NumberUtils.java:418 | 0.218218 | `/**` |
| 3 | 18 | NumberUtils.java:419 | 0.218218 | `* <p>Gets the maximum of three <code>long</code> values.</p>` |
| 3 | 18 | NumberUtils.java:421 | 0.218218 | `* @param a  value 1` |
| 3 | 18 | NumberUtils.java:433 | 0.218218 | `return a;` |
| 3 | 18 | NumberUtils.java:436 | 0.218218 | `/**` |
| 3 | 18 | NumberUtils.java:438 | 0.218218 | `*` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 139 | NumberUtils.java:41 | 0.0 | `* Instead, the class should be used as <code>NumberUtils.stringToInt("6");</code>.</p>` |
| 1 | 139 | NumberUtils.java:43 | 0.0 | `* <p>This constructor is public to permit tools that require a JavaBean instance` |
| 1 | 139 | NumberUtils.java:45 | 0.0 | `*/` |
| 1 | 139 | NumberUtils.java:47 | 0.0 | `super();` |
| 1 | 139 | NumberUtils.java:49 | 0.0 | `` |
| 1 | 139 | NumberUtils.java:51 | 0.0 | `` |
| 1 | 139 | NumberUtils.java:53 | 0.0 | `* <p>Convert a <code>String</code> to an <code>int</code>, returning` |
| 1 | 139 | NumberUtils.java:55 | 0.0 | `*` |
| 1 | 139 | NumberUtils.java:57 | 0.0 | `* @return the int represented by the string, or <code>zero</code> if` |
| 1 | 139 | NumberUtils.java:59 | 0.0 | `*/` |

