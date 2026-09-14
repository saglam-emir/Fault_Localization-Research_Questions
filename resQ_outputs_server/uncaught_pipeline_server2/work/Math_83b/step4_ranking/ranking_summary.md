# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexTableau.java', 292), ('SimplexTableau.java', 341), ('SimplexTableau.java', 345)]

Ground_Truth_Answerable: True

- SBFL   ranked 368 statement(s)
- Hybrid ranked 129 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SimplexTableau.java:349 | 0.5 | `coefficients[i] = 0;` |
| 2 | 2 | SimplexSolver.java:151 | 0.353553 | `return false;` |
| 2 | 2 | SimplexSolver.java:190 | 0.353553 | `doIteration(tableau);` |
| 4 | 1 | SimplexTableau.java:297 | 0.316228 | `return null;` |
| 5 | 42 | ArrayRealVector.java:884 | 0.301511 | `checkVectorDimensions(v.length);` |
| 5 | 42 | ArrayRealVector.java:885 | 0.301511 | `double dot = 0;` |
| 5 | 42 | ArrayRealVector.java:886 | 0.301511 | `for (int i = 0; i < data.length; i++) {` |
| 5 | 42 | ArrayRealVector.java:887 | 0.301511 | `dot += data[i] * v[i];` |
| 5 | 42 | ArrayRealVector.java:889 | 0.301511 | `return dot;` |
| 5 | 42 | ArrayRealVector.java:1287 | 0.301511 | `if (data.length != n) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 129 | AbstractLinearOptimizer.java:61 | 0.0 | `protected AbstractLinearOptimizer() {` |
| 1 | 129 | AbstractLinearOptimizer.java:62 | 0.0 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 1 | 129 | AbstractLinearOptimizer.java:67 | 0.0 | `this.maxIterations = maxIterations;` |
| 1 | 129 | AbstractLinearOptimizer.java:98 | 0.0 | `this.f                     = f;` |
| 1 | 129 | AbstractLinearOptimizer.java:99 | 0.0 | `this.constraints           = constraints;` |
| 1 | 129 | AbstractLinearOptimizer.java:100 | 0.0 | `this.goalType              = goalType;` |
| 1 | 129 | AbstractLinearOptimizer.java:101 | 0.0 | `this.restrictToNonNegative = restrictToNonNegative;` |
| 1 | 129 | AbstractLinearOptimizer.java:103 | 0.0 | `iterations  = 0;` |
| 1 | 129 | AbstractLinearOptimizer.java:106 | 0.0 | `return doOptimize();` |
| 1 | 129 | AbstractRealMatrix.java:43 | 0.0 | `protected AbstractRealMatrix() {` |

