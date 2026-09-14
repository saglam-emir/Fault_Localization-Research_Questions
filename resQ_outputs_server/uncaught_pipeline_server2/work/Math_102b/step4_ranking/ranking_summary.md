# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ChiSquareTestImpl.java', 74), ('ChiSquareTestImpl.java', 77), ('ChiSquareTestImpl.java', 79)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ChiSquareTestImpl.java', 79, '->', 76)]

Ground_Truth_Answerable: True

- SBFL   ranked 511 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | ChiSquareTestImpl.java:66 | 1.0 | `if ((expected.length < 2) || (expected.length != observed.length)) {` |
| 1 | 13 | ChiSquareTestImpl.java:70 | 1.0 | `if (!isPositive(expected) || !isNonNegative(observed)) {` |
| 1 | 13 | ChiSquareTestImpl.java:74 | 1.0 | `double sumSq = 0.0d;` |
| 1 | 13 | ChiSquareTestImpl.java:75 | 1.0 | `double dev = 0.0d;` |
| 1 | 13 | ChiSquareTestImpl.java:76 | 1.0 | `for (int i = 0; i < observed.length; i++) {` |
| 1 | 13 | ChiSquareTestImpl.java:77 | 1.0 | `dev = ((double) observed[i] - expected[i]);` |
| 1 | 13 | ChiSquareTestImpl.java:78 | 1.0 | `sumSq += dev * dev / expected[i];` |
| 1 | 13 | ChiSquareTestImpl.java:80 | 1.0 | `return sumSq;` |
| 1 | 13 | ChiSquareTestImpl.java:97 | 1.0 | `distribution.setDegreesOfFreedom(expected.length - 1.0);` |
| 1 | 13 | ChiSquareTestImpl.java:98 | 1.0 | `return 1.0 - distribution.cumulativeProbability(` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

