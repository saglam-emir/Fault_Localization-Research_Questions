# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 491), ('NumberUtils.java', 1388)]

Ground_Truth_Answerable: True

- SBFL   ranked 894 statement(s)
- Hybrid ranked 61 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 30 | NumberUtils.java:450 | 0.5 | `return null;` |
| 1 | 30 | NumberUtils.java:463 | 0.5 | `return createInteger(str);` |
| 1 | 30 | NumberUtils.java:474 | 0.5 | `if (expPos > -1) {` |
| 1 | 30 | NumberUtils.java:475 | 0.5 | `if (expPos < decPos) {` |
| 1 | 30 | NumberUtils.java:478 | 0.5 | `dec = str.substring(decPos + 1, expPos);` |
| 1 | 30 | NumberUtils.java:480 | 0.5 | `dec = str.substring(decPos + 1);` |
| 1 | 30 | NumberUtils.java:482 | 0.5 | `mant = str.substring(0, decPos);` |
| 1 | 30 | NumberUtils.java:493 | 0.5 | `exp = str.substring(expPos + 1, str.length() - 1);` |
| 1 | 30 | NumberUtils.java:518 | 0.5 | `Float f = NumberUtils.createFloat(numeric);` |
| 1 | 30 | NumberUtils.java:519 | 0.5 | `if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 61 | BooleanUtils.java:44 | 0.0 | `super();` |
| 1 | 61 | NumberUtils.java:85 | 0.0 | `super();` |
| 1 | 61 | NumberUtils.java:449 | 0.0 | `if (str == null) {` |
| 1 | 61 | NumberUtils.java:450 | 0.0 | `return null;` |
| 1 | 61 | NumberUtils.java:452 | 0.0 | `if (StringUtils.isBlank(str)) {` |
| 1 | 61 | NumberUtils.java:455 | 0.0 | `if (str.startsWith("--")) {` |
| 1 | 61 | NumberUtils.java:462 | 0.0 | `if (str.startsWith("0x") || str.startsWith("-0x")) {` |
| 1 | 61 | NumberUtils.java:465 | 0.0 | `char lastChar = str.charAt(str.length() - 1);` |
| 1 | 61 | NumberUtils.java:469 | 0.0 | `int decPos = str.indexOf('.');` |
| 1 | 61 | NumberUtils.java:470 | 0.0 | `int expPos = str.indexOf('e') + str.indexOf('E') + 1;` |

