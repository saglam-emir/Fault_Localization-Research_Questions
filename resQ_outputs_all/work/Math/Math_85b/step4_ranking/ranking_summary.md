# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UnivariateRealSolverUtils.java', 198)]

Ground_Truth_Answerable: True

- SBFL   ranked 610 statement(s)
- Hybrid ranked 9 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | AbstractContinuousDistribution.java:88 | 1.0 | `}  catch (ConvergenceException ex) {` |
| 1 | 25 | AbstractContinuousDistribution.java:97 | 1.0 | `if (Math.abs(rootFindingFunction.value(lowerBound)) < 1E-6) {` |
| 1 | 25 | AbstractContinuousDistribution.java:100 | 1.0 | `if (Math.abs(rootFindingFunction.value(upperBound)) < 1E-6) {` |
| 1 | 25 | AbstractContinuousDistribution.java:104 | 1.0 | `throw new MathException(ex);` |
| 1 | 25 | MathException.java:119 | 1.0 | `super(rootCause);` |
| 1 | 25 | MathException.java:120 | 1.0 | `this.pattern   = getMessage();` |
| 1 | 25 | MathException.java:121 | 1.0 | `this.arguments = new Object[0];` |
| 1 | 25 | MathException.java:166 | 1.0 | `return buildMessage(locale, pattern, arguments);` |
| 1 | 25 | MathException.java:172 | 1.0 | `return getMessage(Locale.getDefault());` |
| 1 | 25 | MathException.java:190 | 1.0 | `synchronized (out) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | AbstractContinuousDistribution.java:46 | 1.0 | `super();` |
| 1 | 9 | AbstractDistribution.java:39 | 1.0 | `super();` |
| 1 | 9 | NormalDistributionImpl.java:43 | 1.0 | `private double mean = 0;` |
| 1 | 9 | NormalDistributionImpl.java:46 | 1.0 | `private double standardDeviation = 1;` |
| 1 | 9 | NormalDistributionImpl.java:54 | 1.0 | `super();` |
| 1 | 9 | NormalDistributionImpl.java:55 | 1.0 | `setMean(mean);` |
| 1 | 9 | NormalDistributionImpl.java:56 | 1.0 | `setStandardDeviation(sd);` |
| 1 | 9 | NormalDistributionImpl.java:80 | 1.0 | `this.mean = mean;` |
| 1 | 9 | NormalDistributionImpl.java:102 | 1.0 | `standardDeviation = sd;` |

