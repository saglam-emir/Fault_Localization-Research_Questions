# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LevenbergMarquardtOptimizer.java', 166), ('LevenbergMarquardtOptimizer.java', 247), ('LevenbergMarquardtOptimizer.java', 252), ('LevenbergMarquardtOptimizer.java', 303), ('LevenbergMarquardtOptimizer.java', 345), ('LevenbergMarquardtOptimizer.java', 419), ('LevenbergMarquardtOptimizer.java', 413), ('LevenbergMarquardtOptimizer.java', 414), ('LevenbergMarquardtOptimizer.java', 421)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('LevenbergMarquardtOptimizer.java', 345, '->', 312), ('LevenbergMarquardtOptimizer.java', 413, '->', 312), ('LevenbergMarquardtOptimizer.java', 414, '->', 312), ('LevenbergMarquardtOptimizer.java', 421, '->', 312)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/general/LevenbergMarquardtOptimizer.java', 247)]

- SBFL   ranked 881 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | LevenbergMarquardtOptimizer.java:381 | 0.353553 | `tmp = 0.1;` |
| 1 | 3 | LevenbergMarquardtOptimizer.java:607 | 0.353553 | `} else if (fp < 0) {` |
| 1 | 3 | LevenbergMarquardtOptimizer.java:608 | 0.353553 | `paru = Math.min(paru, lmPar);` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:510 | 0.333333 | `for (int j = 0; j < solvedCols; ++j) {` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:511 | 0.333333 | `int pj = permutation[j];` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:512 | 0.333333 | `work1[pj] *= diag[pj] / dxNorm;` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:514 | 0.333333 | `sum2 = 0;` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:515 | 0.333333 | `for (int j = 0; j < solvedCols; ++j) {` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:516 | 0.333333 | `int pj = permutation[j];` |
| 4 | 29 | LevenbergMarquardtOptimizer.java:517 | 0.333333 | `double sum = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

