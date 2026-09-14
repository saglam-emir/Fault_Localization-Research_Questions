# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DateUtils.java', 645), ('DateUtils.java', 654), ('DateUtils.java', 643), ('DateUtils.java', 652)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/time/DateUtils.java', 645), ('src/java/org/apache/commons/lang/time/DateUtils.java', 654)]

- SBFL   ranked 524 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DateUtils.java:676 | 0.5 | `if (field == DateUtils.SEMI_MONTH) {` |
| 1 | 2 | DateUtils.java:689 | 0.5 | `val.add(fields[i][0], 1);` |
| 3 | 5 | DateUtils.java:437 | 0.408248 | `if (date == null) {` |
| 3 | 5 | DateUtils.java:440 | 0.408248 | `Calendar gval = Calendar.getInstance();` |
| 3 | 5 | DateUtils.java:441 | 0.408248 | `gval.setTime(date);` |
| 3 | 5 | DateUtils.java:442 | 0.408248 | `modify(gval, field, true);` |
| 3 | 5 | DateUtils.java:443 | 0.408248 | `return gval.getTime();` |
| 8 | 31 | DateUtils.java:621 | 0.288675 | `if (val.get(Calendar.YEAR) > 280000000) {` |
| 8 | 31 | DateUtils.java:625 | 0.288675 | `if (field == Calendar.MILLISECOND) {` |
| 8 | 31 | DateUtils.java:635 | 0.288675 | `Date date = val.getTime();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

