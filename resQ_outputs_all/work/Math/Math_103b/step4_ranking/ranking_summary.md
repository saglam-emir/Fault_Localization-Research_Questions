# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NormalDistributionImpl.java', 109), ('NormalDistributionImpl.java', 111)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/distribution/NormalDistributionImpl.java', 111)]

- SBFL   ranked 151 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 28 | ConvergenceException.java:44 | 1.0 | `super(pattern, arguments);` |
| 1 | 28 | Gamma.java:180 | 1.0 | `throw new MaxIterationsExceededException(maxIterations);` |
| 1 | 28 | MathException.java:47 | 1.0 | `boolean flag = false;` |
| 1 | 28 | MathException.java:49 | 1.0 | `Throwable.class.getDeclaredMethod("getCause", new Class[0]);` |
| 1 | 28 | MathException.java:50 | 1.0 | `flag = true;` |
| 1 | 28 | MathException.java:54 | 1.0 | `JDK_SUPPORTS_NESTED = flag;` |
| 1 | 28 | MathException.java:57 | 1.0 | `private static ResourceBundle cachedResources = null;` |
| 1 | 28 | MathException.java:83 | 1.0 | `if ((cachedResources == null) || (! cachedResources.getLocale().equals(locale))) {` |
| 1 | 28 | MathException.java:85 | 1.0 | `cachedResources =` |
| 1 | 28 | MathException.java:94 | 1.0 | `} catch (MissingResourceException mre) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

