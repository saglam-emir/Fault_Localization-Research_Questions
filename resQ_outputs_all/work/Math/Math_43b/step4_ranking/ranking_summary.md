# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SummaryStatistics.java', 158), ('SummaryStatistics.java', 161), ('SummaryStatistics.java', 164)]

Ground_Truth_Answerable: True

- SBFL   ranked 2498 statement(s)
- Hybrid ranked 42 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SummaryStatistics.java:643 | 0.707107 | `if (n > 0) {` |
| 2 | 4 | SummaryStatistics.java:577 | 0.57735 | `checkEmpty();` |
| 2 | 4 | SummaryStatistics.java:578 | 0.57735 | `this.geoMeanImpl = geoMeanImpl;` |
| 2 | 4 | SummaryStatistics.java:635 | 0.57735 | `checkEmpty();` |
| 2 | 4 | SummaryStatistics.java:636 | 0.57735 | `this.varianceImpl = varianceImpl;` |
| 6 | 5 | SummaryStatistics.java:607 | 0.408248 | `this.meanImpl = meanImpl;` |
| 6 | 5 | Variance.java:124 | 0.408248 | `public Variance(boolean isBiasCorrected) {` |
| 6 | 5 | Variance.java:125 | 0.408248 | `moment = new SecondMoment();` |
| 6 | 5 | Variance.java:126 | 0.408248 | `this.isBiasCorrected = isBiasCorrected;` |
| 6 | 5 | Variance.java:420 | 0.408248 | `var = (accum - (accum2 * accum2 / len)) / len;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | AbstractStorelessUnivariateStatistic.java:35 | 1.0 | `public abstract class AbstractStorelessUnivariateStatistic` |
| 2 | 1 | AbstractUnivariateStatistic.java:39 | 0.866025 | `public abstract class AbstractUnivariateStatistic` |
| 3 | 18 | AbstractUnivariateStatistic.java:137 | 0.57735 | `return test(values, begin, length, false);` |
| 3 | 18 | AbstractUnivariateStatistic.java:180 | 0.57735 | `if (length == 0 && !allowEmpty) {` |
| 3 | 18 | AbstractUnivariateStatistic.java:184 | 0.57735 | `return true;` |
| 3 | 18 | FirstMoment.java:79 | 0.57735 | `public FirstMoment() {` |
| 3 | 18 | GeometricMean.java:65 | 0.57735 | `public GeometricMean() {` |
| 3 | 18 | Mean.java:79 | 0.57735 | `public Mean() {` |
| 3 | 18 | Mean.java:80 | 0.57735 | `incMoment = true;` |
| 3 | 18 | SecondMoment.java:60 | 0.57735 | `super();` |

