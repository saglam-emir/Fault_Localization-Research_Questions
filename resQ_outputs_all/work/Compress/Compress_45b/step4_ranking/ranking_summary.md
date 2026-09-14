# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 488), ('TarUtils.java', 487)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TarUtils.java', 487, '->', 485)]

Ground_Truth_Answerable: True

- SBFL   ranked 3130 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | TarUtils.java:486 | 0.447214 | `formatLongBinary(value, buf, offset, length, negative);` |
| 1 | 13 | TarUtils.java:497 | 0.447214 | `final int bits = (length - 1) * 8;` |
| 1 | 13 | TarUtils.java:498 | 0.447214 | `final long max = 1l << bits;` |
| 1 | 13 | TarUtils.java:499 | 0.447214 | `long val = Math.abs(value); // Long.MIN_VALUE stays Long.MIN_VALUE` |
| 1 | 13 | TarUtils.java:500 | 0.447214 | `if (val < 0 || val >= max) {` |
| 1 | 13 | TarUtils.java:504 | 0.447214 | `if (negative) {` |
| 1 | 13 | TarUtils.java:505 | 0.447214 | `val ^= max - 1;` |
| 1 | 13 | TarUtils.java:506 | 0.447214 | `val++;` |
| 1 | 13 | TarUtils.java:507 | 0.447214 | `val |= 0xffl << bits;` |
| 1 | 13 | TarUtils.java:509 | 0.447214 | `for (int i = offset + length - 1; i >= offset; i--) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

