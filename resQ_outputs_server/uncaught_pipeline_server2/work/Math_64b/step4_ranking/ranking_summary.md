# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LevenbergMarquardtOptimizer.java', 258), ('LevenbergMarquardtOptimizer.java', 270), ('LevenbergMarquardtOptimizer.java', 278), ('LevenbergMarquardtOptimizer.java', 316), ('LevenbergMarquardtOptimizer.java', 324), ('LevenbergMarquardtOptimizer.java', 346), ('LevenbergMarquardtOptimizer.java', 344), ('LevenbergMarquardtOptimizer.java', 365), ('LevenbergMarquardtOptimizer.java', 421), ('LevenbergMarquardtOptimizer.java', 423), ('LevenbergMarquardtOptimizer.java', 424), ('LevenbergMarquardtOptimizer.java', 434), ('LevenbergMarquardtOptimizer.java', 442), ('LevenbergMarquardtOptimizer.java', 443), ('LevenbergMarquardtOptimizer.java', 444), ('LevenbergMarquardtOptimizer.java', 445)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('LevenbergMarquardtOptimizer.java', 344, '->', 333), ('LevenbergMarquardtOptimizer.java', 421, '->', 412), ('LevenbergMarquardtOptimizer.java', 423, '->', 412), ('LevenbergMarquardtOptimizer.java', 424, '->', 412), ('LevenbergMarquardtOptimizer.java', 434, '->', 412)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/general/LevenbergMarquardtOptimizer.java', 442), ('src/main/java/org/apache/commons/math/optimization/general/LevenbergMarquardtOptimizer.java', 445)]

- SBFL   ranked 1276 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | LevenbergMarquardtOptimizer.java:402 | 0.353553 | `tmp = 0.1;` |
| 2 | 2 | LevenbergMarquardtOptimizer.java:627 | 0.333333 | `} else if (fp < 0) {` |
| 2 | 2 | LevenbergMarquardtOptimizer.java:628 | 0.333333 | `paru = Math.min(paru, lmPar);` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:605 | 0.308607 | `for (int j = 0; j < solvedCols; ++j) {` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:606 | 0.308607 | `int pj = permutation[j];` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:607 | 0.308607 | `work1[pj] = work3[pj] * diag[pj] / dxNorm;` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:609 | 0.308607 | `for (int j = 0; j < solvedCols; ++j) {` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:610 | 0.308607 | `int pj = permutation[j];` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:611 | 0.308607 | `work1[pj] /= work2[j];` |
| 4 | 16 | LevenbergMarquardtOptimizer.java:612 | 0.308607 | `double tmp = work1[pj];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

