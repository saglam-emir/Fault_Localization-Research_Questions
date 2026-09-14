# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 145)]

Ground_Truth_Answerable: True

- SBFL   ranked 233 statement(s)
- Hybrid ranked 22 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 20 | NumberUtils.java:139 | 0.57735 | `if (val == null) {` |
| 1 | 20 | NumberUtils.java:142 | 0.57735 | `if (val.length() == 0) {` |
| 1 | 20 | NumberUtils.java:145 | 0.57735 | `if (val.startsWith("--")) {` |
| 1 | 20 | NumberUtils.java:152 | 0.57735 | `if (val.startsWith("0x") || val.startsWith("-0x")) {` |
| 1 | 20 | NumberUtils.java:155 | 0.57735 | `char lastChar = val.charAt(val.length() - 1);` |
| 1 | 20 | NumberUtils.java:159 | 0.57735 | `int decPos = val.indexOf('.');` |
| 1 | 20 | NumberUtils.java:160 | 0.57735 | `int expPos = val.indexOf('e') + val.indexOf('E') + 1;` |
| 1 | 20 | NumberUtils.java:162 | 0.57735 | `if (decPos > -1) {` |
| 1 | 20 | NumberUtils.java:174 | 0.57735 | `if (expPos > -1) {` |
| 1 | 20 | NumberUtils.java:179 | 0.57735 | `dec = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 22 | NumberUtils.java:491 | 0.0 | `if (lhs < rhs) {` |
| 1 | 22 | NumberUtils.java:492 | 0.0 | `return -1;` |
| 1 | 22 | NumberUtils.java:494 | 0.0 | `if (lhs > rhs) {` |
| 1 | 22 | NumberUtils.java:495 | 0.0 | `return +1;` |
| 1 | 22 | NumberUtils.java:501 | 0.0 | `long lhsBits = Double.doubleToLongBits(lhs);` |
| 1 | 22 | NumberUtils.java:502 | 0.0 | `long rhsBits = Double.doubleToLongBits(rhs);` |
| 1 | 22 | NumberUtils.java:503 | 0.0 | `if (lhsBits == rhsBits) {` |
| 1 | 22 | NumberUtils.java:504 | 0.0 | `return 0;` |
| 1 | 22 | NumberUtils.java:512 | 0.0 | `if (lhsBits < rhsBits) {` |
| 1 | 22 | NumberUtils.java:513 | 0.0 | `return -1;` |

