# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexTableau.java', 336), ('SimplexTableau.java', 337), ('SimplexTableau.java', 338), ('SimplexTableau.java', 339), ('SimplexTableau.java', 340), ('SimplexTableau.java', 341), ('SimplexTableau.java', 329), ('SimplexTableau.java', 331), ('SimplexTableau.java', 333)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('SimplexTableau.java', 331, '->', 329)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/optimization/linear/SimplexTableau.java', 340), ('src/java/org/apache/commons/math/optimization/linear/SimplexTableau.java', 341)]

- SBFL   ranked 365 statement(s)
- Hybrid ranked 126 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SimplexTableau.java:339 | 0.57735 | `coefficients[i] = 0;` |
| 2 | 1 | SimplexTableau.java:172 | 0.408248 | `matrix[row][getSlackVariableOffset() + slackVar++] = -1; // excess` |
| 3 | 1 | RealPointValuePair.java:70 | 0.377964 | `return point.clone();` |
| 4 | 1 | SimplexTableau.java:279 | 0.353553 | `return null;` |
| 5 | 23 | LinearObjectiveFunction.java:92 | 0.333333 | `return coefficients.dotProduct(point) + constantTerm;` |
| 5 | 23 | RealPointValuePair.java:48 | 0.333333 | `public RealPointValuePair(final double[] point, final double value) {` |
| 5 | 23 | RealPointValuePair.java:49 | 0.333333 | `this.point = point.clone();` |
| 5 | 23 | RealPointValuePair.java:50 | 0.333333 | `this.value  = value;` |
| 5 | 23 | RealVectorImpl.java:884 | 0.333333 | `checkVectorDimensions(v.length);` |
| 5 | 23 | RealVectorImpl.java:885 | 0.333333 | `double dot = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 126 | AbstractLinearOptimizer.java:61 | 0.0 | `protected AbstractLinearOptimizer() {` |
| 1 | 126 | AbstractLinearOptimizer.java:62 | 0.0 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 1 | 126 | AbstractLinearOptimizer.java:67 | 0.0 | `this.maxIterations = maxIterations;` |
| 1 | 126 | AbstractLinearOptimizer.java:100 | 0.0 | `this.f                     = f;` |
| 1 | 126 | AbstractLinearOptimizer.java:101 | 0.0 | `this.constraints           = constraints;` |
| 1 | 126 | AbstractLinearOptimizer.java:102 | 0.0 | `this.goalType              = goalType;` |
| 1 | 126 | AbstractLinearOptimizer.java:103 | 0.0 | `this.restrictToNonNegative = restrictToNonNegative;` |
| 1 | 126 | AbstractLinearOptimizer.java:105 | 0.0 | `iterations = 0;` |
| 1 | 126 | AbstractLinearOptimizer.java:108 | 0.0 | `return doOptimize();` |
| 1 | 126 | AbstractRealMatrix.java:43 | 0.0 | `protected AbstractRealMatrix() {` |

