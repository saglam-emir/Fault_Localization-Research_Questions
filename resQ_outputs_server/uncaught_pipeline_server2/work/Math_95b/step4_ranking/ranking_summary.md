# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FDistributionImpl.java', 144), ('FDistributionImpl.java', 146), ('FDistributionImpl.java', 148)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/distribution/FDistributionImpl.java', 144), ('src/java/org/apache/commons/math/distribution/FDistributionImpl.java', 146)]

- SBFL   ranked 683 statement(s)
- Hybrid ranked 133 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UnivariateRealSolverUtils.java:179 | 1.0 | `throw new IllegalArgumentException` |
| 2 | 18 | AbstractContinuousDistribution.java:61 | 0.707107 | `if (p < 0.0 || p > 1.0) {` |
| 2 | 18 | AbstractContinuousDistribution.java:67 | 0.707107 | `UnivariateRealFunction rootFindingFunction =` |
| 2 | 18 | AbstractContinuousDistribution.java:68 | 0.707107 | `new UnivariateRealFunction() {` |
| 2 | 18 | AbstractContinuousDistribution.java:80 | 0.707107 | `double lowerBound = getDomainLowerBound(p);` |
| 2 | 18 | AbstractContinuousDistribution.java:81 | 0.707107 | `double upperBound = getDomainUpperBound(p);` |
| 2 | 18 | AbstractContinuousDistribution.java:82 | 0.707107 | `double[] bracket = null;` |
| 2 | 18 | AbstractContinuousDistribution.java:84 | 0.707107 | `bracket = UnivariateRealSolverUtils.bracket(` |
| 2 | 18 | FDistributionImpl.java:106 | 0.707107 | `return super.inverseCumulativeProbability(p);` |
| 2 | 18 | FDistributionImpl.java:119 | 0.707107 | `return 0.0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | AbstractContinuousDistribution.java:45 | 0.707107 | `super();` |
| 1 | 8 | AbstractDistribution.java:38 | 0.707107 | `super();` |
| 1 | 8 | FDistributionImpl.java:50 | 0.707107 | `super();` |
| 1 | 8 | FDistributionImpl.java:51 | 0.707107 | `setNumeratorDegreesOfFreedom(numeratorDegreesOfFreedom);` |
| 1 | 8 | FDistributionImpl.java:52 | 0.707107 | `setDenominatorDegreesOfFreedom(denominatorDegreesOfFreedom);` |
| 1 | 8 | FDistributionImpl.java:72 | 0.707107 | `if (x <= 0.0) {` |
| 1 | 8 | FDistributionImpl.java:162 | 0.707107 | `this.numeratorDegreesOfFreedom = degreesOfFreedom;` |
| 1 | 8 | FDistributionImpl.java:184 | 0.707107 | `this.denominatorDegreesOfFreedom = degreesOfFreedom;` |
| 9 | 125 | AbstractContinuousDistribution.java:67 | 0.0 | `UnivariateRealFunction rootFindingFunction =` |
| 9 | 125 | AbstractContinuousDistribution.java:68 | 0.0 | `new UnivariateRealFunction() {` |

