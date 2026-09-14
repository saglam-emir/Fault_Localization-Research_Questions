# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BrentOptimizer.java', 44), ('BrentOptimizer.java', 46), ('BrentOptimizer.java', 47), ('BrentOptimizer.java', 57), ('BrentOptimizer.java', 58), ('BrentOptimizer.java', 59), ('BrentOptimizer.java', 60), ('BrentOptimizer.java', 62), ('BrentOptimizer.java', 65), ('BrentOptimizer.java', 66), ('BrentOptimizer.java', 67), ('BrentOptimizer.java', 94), ('BrentOptimizer.java', 95), ('BrentOptimizer.java', 119), ('BrentOptimizer.java', 120), ('BrentOptimizer.java', 126), ('BrentOptimizer.java', 127), ('BrentOptimizer.java', 200), ('BrentOptimizer.java', 201), ('BrentOptimizer.java', 238), ('BrentOptimizer.java', 241), ('BrentOptimizer.java', 243)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BrentOptimizer.java', 62, '->', 61), ('BrentOptimizer.java', 94, '->', 93), ('BrentOptimizer.java', 95, '->', 93), ('BrentOptimizer.java', 238, '->', 237)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 57), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 58), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 59), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 65), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 67), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 94), ('src/main/java/org/apache/commons/math/optimization/univariate/BrentOptimizer.java', 95)]

- SBFL   ranked 762 statement(s)
- Hybrid ranked 155 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | AbstractUnivariateRealOptimizer.java:152 | 0.866025 | `return evaluations;` |
| 2 | 1 | ConvergingAlgorithmImpl.java:82 | 0.75 | `return iterationCount;` |
| 3 | 40 | AbstractUnivariateRealOptimizer.java:105 | 0.707107 | `if (functionValue == Double.NaN) {` |
| 3 | 40 | AbstractUnivariateRealOptimizer.java:113 | 0.707107 | `return functionValue;` |
| 3 | 40 | JDKRandomGenerator.java:28 | 0.707107 | `public class JDKRandomGenerator extends Random implements RandomGenerator {` |
| 3 | 40 | MultiStartUnivariateRealOptimizer.java:80 | 0.707107 | `final RandomGenerator generator) {` |
| 3 | 40 | MultiStartUnivariateRealOptimizer.java:81 | 0.707107 | `this.optimizer        = optimizer;` |
| 3 | 40 | MultiStartUnivariateRealOptimizer.java:82 | 0.707107 | `this.totalIterations  = 0;` |
| 3 | 40 | MultiStartUnivariateRealOptimizer.java:83 | 0.707107 | `this.starts           = starts;` |
| 3 | 40 | MultiStartUnivariateRealOptimizer.java:84 | 0.707107 | `this.generator        = generator;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | AbstractUnivariateRealOptimizer.java:97 | 0.57735 | `if (!resultComputed) {` |
| 1 | 2 | MultiStartUnivariateRealOptimizer.java:308 | 0.57735 | `return optima[0];` |
| 3 | 11 | AbstractUnivariateRealOptimizer.java:142 | 0.408248 | `this.maxEvaluations = maxEvaluations;` |
| 3 | 11 | AbstractUnivariateRealOptimizer.java:152 | 0.408248 | `return evaluations;` |
| 3 | 11 | JDKRandomGenerator.java:28 | 0.408248 | `public class JDKRandomGenerator extends Random implements RandomGenerator {` |
| 3 | 11 | MultiStartUnivariateRealOptimizer.java:84 | 0.408248 | `this.generator        = generator;` |
| 3 | 11 | MultiStartUnivariateRealOptimizer.java:122 | 0.408248 | `return totalEvaluations;` |
| 3 | 11 | MultiStartUnivariateRealOptimizer.java:234 | 0.408248 | `totalEvaluations = 0;` |
| 3 | 11 | MultiStartUnivariateRealOptimizer.java:237 | 0.408248 | `for (int i = 0; i < starts; ++i) {` |
| 3 | 11 | MultiStartUnivariateRealOptimizer.java:242 | 0.408248 | `final double bound1 = (i == 0) ? min : min + generator.nextDouble() * (max - min);` |

