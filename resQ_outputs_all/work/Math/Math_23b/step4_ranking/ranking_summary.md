# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BrentOptimizer.java', 151), ('BrentOptimizer.java', 237), ('BrentOptimizer.java', 234), ('BrentOptimizer.java', 274), ('BrentOptimizer.java', 277)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BrentOptimizer.java', 234, '->', 160), ('BrentOptimizer.java', 274, '->', 273), ('BrentOptimizer.java', 277, '->', 273)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/optimization/univariate/BrentOptimizer.java', 151)]

- SBFL   ranked 1130 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 34 | FunctionUtils.java:141 | 0.707107 | `return new UnivariateFunction() {` |
| 1 | 34 | FunctionUtils.java:144 | 0.707107 | `double r = f[0].value(x);` |
| 1 | 34 | FunctionUtils.java:145 | 0.707107 | `for (int i = 1; i < f.length; i++) {` |
| 1 | 34 | FunctionUtils.java:146 | 0.707107 | `r += f[i].value(x);` |
| 1 | 34 | FunctionUtils.java:148 | 0.707107 | `return r;` |
| 1 | 34 | MathArrays.java:143 | 0.707107 | `public static enum OrderDirection {` |
| 1 | 34 | MathArrays.java:145 | 0.707107 | `INCREASING,` |
| 1 | 34 | MathArrays.java:147 | 0.707107 | `DECREASING` |
| 1 | 34 | MathArrays.java:166 | 0.707107 | `switch (dir) {` |
| 1 | 34 | MathArrays.java:234 | 0.707107 | `double previous = val[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

