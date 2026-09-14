# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CMAESOptimizer.java', 921)]

Ground_Truth_Answerable: True

- SBFL   ranked 1526 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | CMAESOptimizer.java:240 | 1.0 | `this(0);` |
| 1 | 7 | CMAESOptimizer.java:247 | 1.0 | `this(lambda, null, DEFAULT_MAXITERATIONS, DEFAULT_STOPFITNESS,` |
| 1 | 7 | CMAESOptimizer.java:470 | 1.0 | `break generationLoop;` |
| 1 | 7 | CMAESOptimizer.java:476 | 1.0 | `sigma = sigma * Math.exp(0.2+cs/damps);` |
| 1 | 7 | CMAESOptimizer.java:562 | 1.0 | `lambda = 4 + (int) (3. * Math.log(dimension));` |
| 1 | 7 | CMAESOptimizer.java:730 | 1.0 | `negccov = negcovMax;` |
| 1 | 7 | CMAESOptimizer.java:995 | 1.0 | `repaired[i] = 1.0;` |
| 8 | 24 | CMAESOptimizer.java:908 | 0.707107 | `double[] res = new double[x.length];` |
| 8 | 24 | CMAESOptimizer.java:909 | 0.707107 | `for (int i = 0; i < x.length; i++) {` |
| 8 | 24 | CMAESOptimizer.java:910 | 0.707107 | `double diff = boundaries[1][i] - boundaries[0][i];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

