# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultiStartUnivariateRealOptimizer.java', 92), ('MultiStartUnivariateRealOptimizer.java', 97)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/optimization/MultiStartUnivariateRealOptimizer.java', 92)]

- SBFL   ranked 413 statement(s)
- Hybrid ranked 100 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 280 | AbstractUnivariateRealOptimizer.java:79 | 1.0 | `checkResultComputed();` |
| 1 | 280 | AbstractUnivariateRealOptimizer.java:80 | 1.0 | `return result;` |
| 1 | 280 | ConvergingAlgorithmImpl.java:78 | 1.0 | `absoluteAccuracy = accuracy;` |
| 1 | 280 | ConvergingAlgorithmImpl.java:83 | 1.0 | `return absoluteAccuracy;` |
| 1 | 280 | ConvergingAlgorithmImpl.java:108 | 1.0 | `relativeAccuracy = accuracy;` |
| 1 | 280 | ConvergingAlgorithmImpl.java:113 | 1.0 | `return relativeAccuracy;` |
| 1 | 280 | LocalizedFormats.java:40 | 1.0 | `public enum LocalizedFormats implements Localizable {` |
| 1 | 280 | LocalizedFormats.java:44 | 1.0 | `ARGUMENT_OUTSIDE_DOMAIN("Argument {0} outside domain [{1} ; {2}]"),` |
| 1 | 280 | LocalizedFormats.java:45 | 1.0 | `ARRAY_SIZES_SHOULD_HAVE_DIFFERENCE_1("array sizes should have difference 1 ({0} != {1} + 1)"),` |
| 1 | 280 | LocalizedFormats.java:46 | 1.0 | `ARRAY_SUMS_TO_ZERO("array sums to zero"),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 36 | AbstractUnivariateRealOptimizer.java:64 | 0.707107 | `resultComputed = false;` |
| 1 | 36 | AbstractUnivariateRealOptimizer.java:65 | 0.707107 | `setMaxEvaluations(Integer.MAX_VALUE);` |
| 1 | 36 | AbstractUnivariateRealOptimizer.java:100 | 0.707107 | `this.iterationCount = iterationCount;` |
| 1 | 36 | AbstractUnivariateRealOptimizer.java:113 | 0.707107 | `this.maxEvaluations = maxEvaluations;` |
| 1 | 36 | BrentOptimizer.java:99 | 0.707107 | `int count = 0;` |
| 1 | 36 | BrentOptimizer.java:180 | 0.707107 | `setResult(x, (goalType == GoalType.MAXIMIZE) ? -fx : fx, count);` |
| 1 | 36 | BrentOptimizer.java:184 | 0.707107 | `++count;` |
| 1 | 36 | ConvergingAlgorithmImpl.java:61 | 0.707107 | `final double defaultAbsoluteAccuracy) {` |
| 1 | 36 | ConvergingAlgorithmImpl.java:62 | 0.707107 | `this.defaultAbsoluteAccuracy = defaultAbsoluteAccuracy;` |
| 1 | 36 | ConvergingAlgorithmImpl.java:66 | 0.707107 | `this.defaultMaximalIterationCount = defaultMaximalIterationCount;` |

