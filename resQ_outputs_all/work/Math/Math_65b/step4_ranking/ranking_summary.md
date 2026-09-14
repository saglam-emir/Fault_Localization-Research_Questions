# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('AbstractLeastSquaresOptimizer.java', 240), ('AbstractLeastSquaresOptimizer.java', 241), ('AbstractLeastSquaresOptimizer.java', 242), ('AbstractLeastSquaresOptimizer.java', 243), ('AbstractLeastSquaresOptimizer.java', 244), ('AbstractLeastSquaresOptimizer.java', 245), ('AbstractLeastSquaresOptimizer.java', 258)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/general/AbstractLeastSquaresOptimizer.java', 244)]

- SBFL   ranked 1674 statement(s)
- Hybrid ranked 360 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 48 | AbstractLeastSquaresOptimizer.java:255 | 1.0 | `double chiSquare = 0;` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:256 | 1.0 | `for (int i = 0; i < rows; ++i) {` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:257 | 1.0 | `final double residual = residuals[i];` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:258 | 1.0 | `chiSquare += residual * residual / residualsWeights[i];` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:260 | 1.0 | `return chiSquare;` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:294 | 1.0 | `return inverse.getData();` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:317 | 1.0 | `double[] errors = new double[cols];` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:318 | 1.0 | `final double c = Math.sqrt(getChiSquare() / (rows - cols));` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:319 | 1.0 | `double[][] covar = getCovariances();` |
| 1 | 48 | AbstractLeastSquaresOptimizer.java:320 | 1.0 | `for (int i = 0; i < errors.length; ++i) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 360 | AbstractLeastSquaresOptimizer.java:116 | 0.0 | `protected AbstractLeastSquaresOptimizer() {` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:117 | 0.0 | `setConvergenceChecker(new SimpleVectorialValueChecker());` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:124 | 0.0 | `this.maxIterations = maxIterations;` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:149 | 0.0 | `return objectiveEvaluations;` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:154 | 0.0 | `return jacobianEvaluations;` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:159 | 0.0 | `this.checker = convergenceChecker;` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:173 | 0.0 | `if (++iterations > maxIterations) {` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:184 | 0.0 | `++jacobianEvaluations;` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:185 | 0.0 | `jacobian = jF.value(point);` |
| 1 | 360 | AbstractLeastSquaresOptimizer.java:208 | 0.0 | `if (++objectiveEvaluations > maxEvaluations) {` |

