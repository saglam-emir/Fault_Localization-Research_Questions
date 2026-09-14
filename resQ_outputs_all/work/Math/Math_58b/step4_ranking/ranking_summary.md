# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('GaussianFitter.java', 121)]

Ground_Truth_Answerable: True

- SBFL   ranked 1158 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 144 | FastMath.java:3830 | 1.0 | `if (a < b) {` |
| 1 | 144 | FastMath.java:3831 | 1.0 | `return a;` |
| 1 | 144 | Gaussian.java:183 | 1.0 | `throw new NotStrictlyPositiveException(param[2]);` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:384 | 1.0 | `double tmp =` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:386 | 1.0 | `if ((0.1 * cost >= previousCost) || (tmp < 0.1)) {` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:389 | 1.0 | `delta = tmp * FastMath.min(delta, 10.0 * lmNorm);` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:390 | 1.0 | `lmPar /= tmp;` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:391 | 1.0 | `} else if ((lmPar == 0) || (ratio >= 0.75)) {` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:417 | 1.0 | `cost = previousCost;` |
| 1 | 144 | LevenbergMarquardtOptimizer.java:418 | 1.0 | `for (int j = 0; j < solvedCols; ++j) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

