# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NormalDistributionImpl.java', 126), ('NormalDistributionImpl.java', 129), ('NormalDistributionImpl.java', 130), ('NormalDistributionImpl.java', 131), ('NormalDistributionImpl.java', 132), ('NormalDistributionImpl.java', 133), ('NormalDistributionImpl.java', 134), ('NormalDistributionImpl.java', 135), ('NormalDistributionImpl.java', 136), ('NormalDistributionImpl.java', 137)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('NormalDistributionImpl.java', 131, '->', 130)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 126), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 129), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 130), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 131), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 132), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 133), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 134), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 135), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 136), ('src/main/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 137)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 1018 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 21 | ContinuedFraction.java:163 | 1.0 | `p2 = p1 / lastScaleFactor + (b / scaleFactor * p0);` |
| 1 | 21 | ContinuedFraction.java:164 | 1.0 | `q2 = q1 / lastScaleFactor + (b / scaleFactor * q0);` |
| 1 | 21 | ContinuedFraction.java:186 | 1.0 | `throw new ConvergenceException(` |
| 1 | 21 | ConvergenceException.java:62 | 1.0 | `super(pattern, arguments);` |
| 1 | 21 | FastMath.java:653 | 1.0 | `final double result = exp(x+40.19140625, extra, hiPrec) / 285040095144011776.0;` |
| 1 | 21 | FastMath.java:654 | 1.0 | `if (hiPrec != null) {` |
| 1 | 21 | FastMath.java:658 | 1.0 | `return result;` |
| 1 | 21 | LocalizedFormats.java:347 | 1.0 | `ResourceBundle bundle =` |
| 1 | 21 | LocalizedFormats.java:354 | 1.0 | `} catch (MissingResourceException mre) {` |
| 1 | 21 | LocalizedFormats.java:360 | 1.0 | `return sourceFormat;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

