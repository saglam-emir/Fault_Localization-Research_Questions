# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BrentOptimizer.java', 230), ('BrentOptimizer.java', 267)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BrentOptimizer.java', 267, '->', 266)]

Ground_Truth_Answerable: True

- SBFL   ranked 1125 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 31 | FunctionUtils.java:141 | 1.0 | `return new UnivariateFunction() {` |
| 1 | 31 | FunctionUtils.java:144 | 1.0 | `double r = f[0].value(x);` |
| 1 | 31 | FunctionUtils.java:145 | 1.0 | `for (int i = 1; i < f.length; i++) {` |
| 1 | 31 | FunctionUtils.java:146 | 1.0 | `r += f[i].value(x);` |
| 1 | 31 | FunctionUtils.java:148 | 1.0 | `return r;` |
| 1 | 31 | MathArrays.java:166 | 1.0 | `switch (dir) {` |
| 1 | 31 | MathArrays.java:228 | 1.0 | `double previous = val[0];` |
| 1 | 31 | MathArrays.java:229 | 1.0 | `final int max = val.length;` |
| 1 | 31 | MathArrays.java:233 | 1.0 | `for (index = 1; index < max; index++) {` |
| 1 | 31 | MathArrays.java:234 | 1.0 | `switch (dir) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

