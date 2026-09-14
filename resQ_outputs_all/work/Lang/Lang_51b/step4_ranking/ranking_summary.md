# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BooleanUtils.java', 682)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BooleanUtils.java', 682, '->', 662)]

Ground_Truth_Answerable: True

- SBFL   ranked 1043 statement(s)
- Hybrid ranked 123 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | BooleanUtils.java:656 | 1.0 | `if (str == "true") {` |
| 1 | 19 | BooleanUtils.java:657 | 1.0 | `return true;` |
| 1 | 19 | BooleanUtils.java:659 | 1.0 | `if (str == null) {` |
| 1 | 19 | BooleanUtils.java:660 | 1.0 | `return false;` |
| 1 | 19 | BooleanUtils.java:662 | 1.0 | `switch (str.length()) {` |
| 1 | 19 | BooleanUtils.java:664 | 1.0 | `char ch0 = str.charAt(0);` |
| 1 | 19 | BooleanUtils.java:665 | 1.0 | `char ch1 = str.charAt(1);` |
| 1 | 19 | BooleanUtils.java:666 | 1.0 | `return` |
| 1 | 19 | BooleanUtils.java:671 | 1.0 | `char ch = str.charAt(0);` |
| 1 | 19 | BooleanUtils.java:672 | 1.0 | `if (ch == 'y') {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 123 | BooleanUtils.java:64 | 0.0 | `if (bool == null) {` |
| 1 | 123 | BooleanUtils.java:65 | 0.0 | `return null;` |
| 1 | 123 | BooleanUtils.java:67 | 0.0 | `return (bool.booleanValue() ? Boolean.FALSE : Boolean.TRUE);` |
| 1 | 123 | BooleanUtils.java:87 | 0.0 | `if (bool == null) {` |
| 1 | 123 | BooleanUtils.java:88 | 0.0 | `return false;` |
| 1 | 123 | BooleanUtils.java:90 | 0.0 | `return bool.booleanValue() ? true : false;` |
| 1 | 123 | BooleanUtils.java:108 | 0.0 | `return !isTrue(bool);` |
| 1 | 123 | BooleanUtils.java:126 | 0.0 | `if (bool == null) {` |
| 1 | 123 | BooleanUtils.java:127 | 0.0 | `return false;` |
| 1 | 123 | BooleanUtils.java:129 | 0.0 | `return bool.booleanValue() ? false : true;` |

