# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultiDirectional.java', 64), ('MultiDirectional.java', 92), ('MultiDirectional.java', 94)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('MultiDirectional.java', 92, '->', 90)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/direct/MultiDirectional.java', 64)]

- SBFL   ranked 156 statement(s)
- Hybrid ranked 70 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 54 | ConvergenceException.java:45 | 0.707107 | `super(pattern, arguments);` |
| 1 | 54 | ConvergenceException.java:53 | 0.707107 | `super(cause);` |
| 1 | 54 | DirectSearchOptimizer.java:142 | 0.707107 | `final int n = steps.length;` |
| 1 | 54 | DirectSearchOptimizer.java:143 | 0.707107 | `startConfiguration = new double[n][n];` |
| 1 | 54 | DirectSearchOptimizer.java:144 | 0.707107 | `for (int i = 0; i < n; ++i) {` |
| 1 | 54 | DirectSearchOptimizer.java:145 | 0.707107 | `final double[] vertexI = startConfiguration[i];` |
| 1 | 54 | DirectSearchOptimizer.java:146 | 0.707107 | `for (int j = 0; j < i + 1; ++j) {` |
| 1 | 54 | DirectSearchOptimizer.java:147 | 0.707107 | `if (steps[j] == 0.0) {` |
| 1 | 54 | DirectSearchOptimizer.java:152 | 0.707107 | `System.arraycopy(steps, 0, vertexI, 0, j + 1);` |
| 1 | 54 | DirectSearchOptimizer.java:278 | 0.707107 | `final double v1 = o1.getValue();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | DirectSearchOptimizer.java:116 | 0.5 | `protected DirectSearchOptimizer() {` |
| 1 | 6 | DirectSearchOptimizer.java:220 | 0.5 | `this.maxIterations = maxIterations;` |
| 1 | 6 | DirectSearchOptimizer.java:250 | 0.5 | `this.checker = checker;` |
| 1 | 6 | SimpleScalarValueChecker.java:65 | 0.5 | `final double absoluteThreshold) {` |
| 1 | 6 | SimpleScalarValueChecker.java:66 | 0.5 | `this.relativeThreshold = relativeThreshold;` |
| 1 | 6 | SimpleScalarValueChecker.java:67 | 0.5 | `this.absoluteThreshold = absoluteThreshold;` |
| 7 | 3 | DirectSearchOptimizer.java:245 | 0.288675 | `return evaluations;` |
| 7 | 3 | DirectSearchOptimizer.java:287 | 0.288675 | `evaluations = 0;` |
| 7 | 3 | DirectSearchOptimizer.java:345 | 0.288675 | `if (++evaluations > maxEvaluations) {` |
| 10 | 2 | DirectSearchOptimizer.java:142 | 0.235702 | `final int n = steps.length;` |

