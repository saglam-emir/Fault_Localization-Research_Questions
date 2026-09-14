# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PoissonDistributionImpl.java', 22), ('PoissonDistributionImpl.java', 94)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/distribution/PoissonDistributionImpl.java', 22)]

- SBFL   ranked 805 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 272 | LocalizedFormats.java:39 | 1.0 | `public enum LocalizedFormats implements Localizable {` |
| 1 | 272 | LocalizedFormats.java:44 | 1.0 | `ARGUMENT_OUTSIDE_DOMAIN("Argument {0} outside domain [{1} ; {2}]"),` |
| 1 | 272 | LocalizedFormats.java:45 | 1.0 | `ARRAY_SIZES_SHOULD_HAVE_DIFFERENCE_1("array sizes should have difference 1 ({0} != {1} + 1)"),` |
| 1 | 272 | LocalizedFormats.java:46 | 1.0 | `ARRAY_SUMS_TO_ZERO("array sums to zero"),` |
| 1 | 272 | LocalizedFormats.java:47 | 1.0 | `ASSYMETRIC_EIGEN_NOT_SUPPORTED("eigen decomposition of assymetric matrices not supported yet"),` |
| 1 | 272 | LocalizedFormats.java:48 | 1.0 | `AT_LEAST_ONE_COLUMN("matrix must have at least one column"),` |
| 1 | 272 | LocalizedFormats.java:49 | 1.0 | `AT_LEAST_ONE_ROW("matrix must have at least one row"),` |
| 1 | 272 | LocalizedFormats.java:50 | 1.0 | `BANDWIDTH_OUT_OF_INTERVAL("bandwidth must be in the interval [0,1], but got {0}"),` |
| 1 | 272 | LocalizedFormats.java:51 | 1.0 | `BINOMIAL_INVALID_PARAMETERS_ORDER("must have n >= k for binomial coefficient (n,k), got n = {0}, k = {1}"),` |
| 1 | 272 | LocalizedFormats.java:52 | 1.0 | `BINOMIAL_NEGATIVE_PARAMETER("must have n >= 0 for binomial coefficient (n,k), got n = {0}"),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

