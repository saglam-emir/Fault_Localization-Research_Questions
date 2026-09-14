# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastMath.java', 82), ('FastMath.java', 397), ('FastMath.java', 394), ('FastMath.java', 395), ('FastMath.java', 399), ('FastMath.java', 400), ('FastMath.java', 458), ('FastMath.java', 455), ('FastMath.java', 456), ('FastMath.java', 460), ('FastMath.java', 461)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('FastMath.java', 394, '->', 393), ('FastMath.java', 400, '->', 397), ('FastMath.java', 455, '->', 454), ('FastMath.java', 461, '->', 458)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/util/FastMath.java', 82)]

- SBFL   ranked 24946 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | DstNormalization.java:28 | 0.5 | `public enum DstNormalization {` |
| 1 | 3 | DstNormalization.java:41 | 0.5 | `STANDARD_DST_I,` |
| 1 | 3 | DstNormalization.java:56 | 0.5 | `ORTHOGONAL_DST_I` |
| 4 | 3 | DctNormalization.java:28 | 0.433013 | `public enum DctNormalization {` |
| 4 | 3 | DctNormalization.java:46 | 0.433013 | `STANDARD_DCT_I,` |
| 4 | 3 | DctNormalization.java:66 | 0.433013 | `ORTHOGONAL_DCT_I;` |
| 7 | 2 | FastMath.java:870 | 0.1066 | `if (hiPrec != null) {` |
| 7 | 2 | FastMath.java:874 | 0.1066 | `return Double.POSITIVE_INFINITY;` |
| 9 | 2 | FastMath.java:384 | 0.104257 | `if (x != x) {` |
| 9 | 2 | FastMath.java:393 | 0.104257 | `if (x > 20) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

