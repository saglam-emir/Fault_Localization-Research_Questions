# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 345), ('MathUtils.java', 346), ('MathUtils.java', 377), ('MathUtils.java', 397)]

Ground_Truth_Answerable: True

- SBFL   ranked 4906 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | MathUtils.java:350 | 1.0 | `return factorials[n];` |
| 2 | 9 | MathUtils.java:345 | 0.707107 | `long result = Math.round(factorialDouble(n));` |
| 2 | 9 | MathUtils.java:346 | 0.707107 | `if (result == Long.MAX_VALUE) {` |
| 2 | 9 | MathUtils.java:374 | 0.707107 | `if (n < 0) {` |
| 2 | 9 | MathUtils.java:377 | 0.707107 | `return Math.floor(Math.exp(factorialLog(n)) + 0.5);` |
| 2 | 9 | MathUtils.java:394 | 0.707107 | `if (n < 0) {` |
| 2 | 9 | MathUtils.java:397 | 0.707107 | `double logSum = 0;` |
| 2 | 9 | MathUtils.java:398 | 0.707107 | `for (int i = 2; i <= n; i++) {` |
| 2 | 9 | MathUtils.java:399 | 0.707107 | `logSum += Math.log((double)i);` |
| 2 | 9 | MathUtils.java:401 | 0.707107 | `return logSum;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

