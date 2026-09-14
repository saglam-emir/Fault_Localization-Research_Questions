# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BaseOptimizer.java', 51), ('NonLinearConjugateGradientOptimizer.java', 214), ('NonLinearConjugateGradientOptimizer.java', 217), ('NonLinearConjugateGradientOptimizer.java', 223), ('NonLinearConjugateGradientOptimizer.java', 277), ('CMAESOptimizer.java', 388), ('PowellOptimizer.java', 191), ('PowellOptimizer.java', 193), ('PowellOptimizer.java', 227), ('SimplexOptimizer.java', 158), ('SimplexOptimizer.java', 175), ('GaussNewtonOptimizer.java', 106), ('GaussNewtonOptimizer.java', 108), ('GaussNewtonOptimizer.java', 160), ('LevenbergMarquardtOptimizer.java', 322), ('LevenbergMarquardtOptimizer.java', 325), ('LevenbergMarquardtOptimizer.java', 489)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CMAESOptimizer.java', 388, '->', 387)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/optim/nonlinear/scalar/gradient/NonLinearConjugateGradientOptimizer.java', 217), ('src/main/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/PowellOptimizer.java', 191), ('src/main/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/PowellOptimizer.java', 193), ('src/main/java/org/apache/commons/math3/optim/nonlinear/scalar/noderiv/PowellOptimizer.java', 227), ('src/main/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/GaussNewtonOptimizer.java', 106), ('src/main/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/GaussNewtonOptimizer.java', 160), ('src/main/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/LevenbergMarquardtOptimizer.java', 325), ('src/main/java/org/apache/commons/math3/optim/nonlinear/vector/jacobian/LevenbergMarquardtOptimizer.java', 489)]

- SBFL   ranked 4455 statement(s)
- Hybrid ranked 1111 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | BaseOptimizer.java:93 | 1.0 | `return iterations.getCount();` |
| 2 | 1 | CMAESOptimizer.java:451 | 0.784465 | `if (bestFitness < (isMinimize ? stopFitness : -stopFitness)) {` |
| 3 | 104 | CMAESOptimizer.java:1109 | 0.759555 | `final double[][] d = new double[m.getRowDimension()][1];` |
| 3 | 104 | CMAESOptimizer.java:1110 | 0.759555 | `for (int i = 0; i < m.getColumnDimension(); i++) {` |
| 3 | 104 | EigenDecomposition.java:579 | 0.759555 | `realEigenvalues[i] = main[i];` |
| 3 | 104 | EigenDecomposition.java:580 | 0.759555 | `e[i] = secondary[i];` |
| 3 | 104 | EigenDecomposition.java:612 | 0.759555 | `double delta = FastMath.abs(realEigenvalues[m]) +` |
| 3 | 104 | EigenDecomposition.java:614 | 0.759555 | `if (FastMath.abs(e[m]) + delta == delta) {` |
| 3 | 104 | EigenDecomposition.java:615 | 0.759555 | `break;` |
| 3 | 104 | EigenDecomposition.java:619 | 0.759555 | `if (its == maxIter) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | BaseOptimizer.java:93 | 0.5547 | `return iterations.getCount();` |
| 1 | 2 | BaseOptimizer.java:141 | 0.5547 | `iterations.resetCount();` |
| 3 | 2 | Incrementor.java:114 | 0.224133 | `return count;` |
| 3 | 2 | Incrementor.java:164 | 0.224133 | `count = 0;` |
| 5 | 1 | SimplexOptimizer.java:122 | 0.209657 | `return super.optimize(optData);` |
| 6 | 1 | MultivariateOptimizer.java:64 | 0.202548 | `return super.optimize(optData);` |
| 7 | 1 | BaseMultivariateOptimizer.java:66 | 0.194602 | `return super.optimize(optData);` |
| 8 | 2 | GoalType.java:28 | 0.065372 | `public enum GoalType implements OptimizationData {` |
| 8 | 2 | GoalType.java:32 | 0.065372 | `MINIMIZE` |
| 10 | 1102 | AbstractConvergenceChecker.java:45 | 0.0 | `final double absoluteThreshold) {` |

