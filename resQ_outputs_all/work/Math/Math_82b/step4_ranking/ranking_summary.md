# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimplexSolver.java', 82)]

Ground_Truth_Answerable: True

- SBFL   ranked 273 statement(s)
- Hybrid ranked 131 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | SimplexSolver.java:169 | 0.57735 | `return;` |
| 1 | 2 | SimplexTableau.java:308 | 0.57735 | `return;` |
| 3 | 3 | SimplexSolver.java:152 | 0.333333 | `return false;` |
| 3 | 3 | SimplexSolver.java:191 | 0.333333 | `doIteration(tableau);` |
| 3 | 3 | SimplexTableau.java:170 | 0.333333 | `matrix[row][getSlackVariableOffset() + slackVar++] = 1;  // slack` |
| 6 | 5 | ArrayRealVector.java:338 | 0.301511 | `double[] out = new double[data.length];` |
| 6 | 5 | ArrayRealVector.java:339 | 0.301511 | `for (int i = 0; i < data.length; i++) {` |
| 6 | 5 | ArrayRealVector.java:340 | 0.301511 | `out[i] = data[i] * d;` |
| 6 | 5 | ArrayRealVector.java:342 | 0.301511 | `return new ArrayRealVector(out);` |
| 6 | 5 | SimplexTableau.java:297 | 0.301511 | `return null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 127 | AbstractLinearOptimizer.java:61 | 0.408248 | `protected AbstractLinearOptimizer() {` |
| 1 | 127 | AbstractLinearOptimizer.java:62 | 0.408248 | `setMaxIterations(DEFAULT_MAX_ITERATIONS);` |
| 1 | 127 | AbstractLinearOptimizer.java:67 | 0.408248 | `this.maxIterations = maxIterations;` |
| 1 | 127 | AbstractLinearOptimizer.java:98 | 0.408248 | `this.f                     = f;` |
| 1 | 127 | AbstractLinearOptimizer.java:99 | 0.408248 | `this.constraints           = constraints;` |
| 1 | 127 | AbstractLinearOptimizer.java:100 | 0.408248 | `this.goalType              = goalType;` |
| 1 | 127 | AbstractLinearOptimizer.java:101 | 0.408248 | `this.restrictToNonNegative = restrictToNonNegative;` |
| 1 | 127 | AbstractLinearOptimizer.java:103 | 0.408248 | `iterations  = 0;` |
| 1 | 127 | AbstractLinearOptimizer.java:106 | 0.408248 | `return doOptimize();` |
| 1 | 127 | AbstractRealMatrix.java:43 | 0.408248 | `protected AbstractRealMatrix() {` |

