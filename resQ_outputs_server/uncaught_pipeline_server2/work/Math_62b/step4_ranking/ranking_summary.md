# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultiStartUnivariateRealOptimizer.java', 146), ('MultiStartUnivariateRealOptimizer.java', 160), ('MultiStartUnivariateRealOptimizer.java', 161), ('MultiStartUnivariateRealOptimizer.java', 162)]

Ground_Truth_Answerable: True

- SBFL   ranked 560 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 448 | AbstractUnivariateRealOptimizer.java:36 | 0.707107 | `public abstract class AbstractUnivariateRealOptimizer` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:41 | 0.707107 | `private final Incrementor evaluations = new Incrementor();` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:55 | 0.707107 | `evaluations.setMaximalCount(maxEvaluations);` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:60 | 0.707107 | `return evaluations.getMaximalCount();` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:65 | 0.707107 | `return evaluations.getCount();` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:72 | 0.707107 | `return goal;` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:78 | 0.707107 | `return searchMin;` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:84 | 0.707107 | `return searchMax;` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:90 | 0.707107 | `return searchStart;` |
| 1 | 448 | AbstractUnivariateRealOptimizer.java:106 | 0.707107 | `evaluations.incrementCount();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

