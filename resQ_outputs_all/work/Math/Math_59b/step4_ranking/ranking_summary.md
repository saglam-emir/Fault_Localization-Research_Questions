# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastMath.java', 3482)]

Ground_Truth_Answerable: True

- SBFL   ranked 17957 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | FastMath.java:3446 | 0.57735 | `return (a <= b) ? a : (Float.isNaN(a + b) ? Float.NaN : b);` |
| 1 | 2 | FastMath.java:3482 | 0.57735 | `return (a <= b) ? b : (Float.isNaN(a + b) ? Float.NaN : b);` |
| 3 | 582 | Dfp.java:202 | 0.107211 | `this(field, (long) x);` |
| 3 | 582 | Dfp.java:209 | 0.107211 | `protected Dfp(final DfpField field, long x) {` |
| 3 | 582 | Dfp.java:212 | 0.107211 | `mant = new int[field.getRadixDigits()];` |
| 3 | 582 | Dfp.java:213 | 0.107211 | `nans = FINITE;` |
| 3 | 582 | Dfp.java:214 | 0.107211 | `this.field = field;` |
| 3 | 582 | Dfp.java:216 | 0.107211 | `boolean isLongMin = false;` |
| 3 | 582 | Dfp.java:217 | 0.107211 | `if (x == Long.MIN_VALUE) {` |
| 3 | 582 | Dfp.java:225 | 0.107211 | `if (x < 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

