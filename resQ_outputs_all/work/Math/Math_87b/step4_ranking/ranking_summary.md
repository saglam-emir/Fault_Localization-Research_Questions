# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexTableau.java', 275), ('SimplexTableau.java', 276), ('SimplexTableau.java', 278), ('SimplexTableau.java', 280)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/optimization/linear/SimplexTableau.java', 278), ('src/java/org/apache/commons/math/optimization/linear/SimplexTableau.java', 280)]

- SBFL   ranked 365 statement(s)
- Hybrid ranked 129 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | SimplexSolver.java:168 | 0.707107 | `return;` |
| 1 | 2 | SimplexTableau.java:291 | 0.707107 | `return;` |
| 3 | 2 | SimplexSolver.java:151 | 0.377964 | `return false;` |
| 3 | 2 | SimplexSolver.java:190 | 0.377964 | `doIteration(tableau);` |
| 5 | 1 | RealPointValuePair.java:70 | 0.353553 | `return point.clone();` |
| 6 | 23 | LinearObjectiveFunction.java:92 | 0.316228 | `return coefficients.dotProduct(point) + constantTerm;` |
| 6 | 23 | RealPointValuePair.java:48 | 0.316228 | `public RealPointValuePair(final double[] point, final double value) {` |
| 6 | 23 | RealPointValuePair.java:49 | 0.316228 | `this.point = point.clone();` |
| 6 | 23 | RealPointValuePair.java:50 | 0.316228 | `this.value  = value;` |
| 6 | 23 | RealVectorImpl.java:884 | 0.316228 | `checkVectorDimensions(v.length);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 128 | AbstractLinearOptimizer.java:61 | 0.5 | `protected AbstractLinearOptimizer() {` |
| 1 | 128 | AbstractLinearOptimizer.java:62 | 0.5 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 1 | 128 | AbstractLinearOptimizer.java:67 | 0.5 | `this.maxIterations = maxIterations;` |
| 1 | 128 | AbstractLinearOptimizer.java:100 | 0.5 | `this.f                     = f;` |
| 1 | 128 | AbstractLinearOptimizer.java:101 | 0.5 | `this.constraints           = constraints;` |
| 1 | 128 | AbstractLinearOptimizer.java:102 | 0.5 | `this.goalType              = goalType;` |
| 1 | 128 | AbstractLinearOptimizer.java:103 | 0.5 | `this.restrictToNonNegative = restrictToNonNegative;` |
| 1 | 128 | AbstractLinearOptimizer.java:105 | 0.5 | `iterations = 0;` |
| 1 | 128 | AbstractLinearOptimizer.java:108 | 0.5 | `return doOptimize();` |
| 1 | 128 | AbstractRealMatrix.java:43 | 0.5 | `protected AbstractRealMatrix() {` |

