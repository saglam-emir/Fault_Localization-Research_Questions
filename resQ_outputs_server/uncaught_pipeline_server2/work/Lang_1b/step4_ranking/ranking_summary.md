# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 468), ('NumberUtils.java', 471), ('NumberUtils.java', 467)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('NumberUtils.java', 467, '->', 466)]

Ground_Truth_Answerable: True

- SBFL   ranked 944 statement(s)
- Hybrid ranked 90 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | NumberUtils.java:462 | 0.166667 | `pfxLen += pfx.length();` |
| 1 | 6 | NumberUtils.java:463 | 0.166667 | `break;` |
| 1 | 6 | NumberUtils.java:467 | 0.166667 | `final int hexDigits = str.length() - pfxLen;` |
| 1 | 6 | NumberUtils.java:468 | 0.166667 | `if (hexDigits > 16) { // too many for Long` |
| 1 | 6 | NumberUtils.java:471 | 0.166667 | `if (hexDigits > 8) { // too many for an int` |
| 1 | 6 | NumberUtils.java:474 | 0.166667 | `return createInteger(str);` |
| 7 | 2 | NumberUtils.java:680 | 0.149071 | `if (str == null) {` |
| 7 | 2 | NumberUtils.java:684 | 0.149071 | `return Integer.decode(str);` |
| 9 | 7 | NumberUtils.java:451 | 0.105409 | `if (str == null) {` |
| 9 | 7 | NumberUtils.java:454 | 0.105409 | `if (StringUtils.isBlank(str)) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 90 | NumberUtils.java:34 | 0.0 | `public static final Long LONG_ZERO = Long.valueOf(0L);` |
| 1 | 90 | NumberUtils.java:36 | 0.0 | `public static final Long LONG_ONE = Long.valueOf(1L);` |
| 1 | 90 | NumberUtils.java:38 | 0.0 | `public static final Long LONG_MINUS_ONE = Long.valueOf(-1L);` |
| 1 | 90 | NumberUtils.java:40 | 0.0 | `public static final Integer INTEGER_ZERO = Integer.valueOf(0);` |
| 1 | 90 | NumberUtils.java:42 | 0.0 | `public static final Integer INTEGER_ONE = Integer.valueOf(1);` |
| 1 | 90 | NumberUtils.java:44 | 0.0 | `public static final Integer INTEGER_MINUS_ONE = Integer.valueOf(-1);` |
| 1 | 90 | NumberUtils.java:46 | 0.0 | `public static final Short SHORT_ZERO = Short.valueOf((short) 0);` |
| 1 | 90 | NumberUtils.java:48 | 0.0 | `public static final Short SHORT_ONE = Short.valueOf((short) 1);` |
| 1 | 90 | NumberUtils.java:50 | 0.0 | `public static final Short SHORT_MINUS_ONE = Short.valueOf((short) -1);` |
| 1 | 90 | NumberUtils.java:52 | 0.0 | `public static final Byte BYTE_ZERO = Byte.valueOf((byte) 0);` |

