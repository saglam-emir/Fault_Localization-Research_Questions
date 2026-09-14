# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MannWhitneyUTest.java', 173)]

Ground_Truth_Answerable: True

- SBFL   ranked 689 statement(s)
- Hybrid ranked 57 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | FastMath.java:3538 | 1.0 | `if (a < b) {` |
| 1 | 3 | FastMath.java:3539 | 1.0 | `return b;` |
| 1 | 3 | Gamma.java:155 | 1.0 | `ret = Double.NaN;` |
| 4 | 84 | AbstractRealDistribution.java:47 | 0.707107 | `protected final RandomDataImpl randomData = new RandomDataImpl();` |
| 4 | 84 | AbstractRealDistribution.java:50 | 0.707107 | `private double solverAbsoluteAccuracy = SOLVER_DEFAULT_ABSOLUTE_ACCURACY;` |
| 4 | 84 | AbstractRealDistribution.java:53 | 0.707107 | `protected AbstractRealDistribution() { }` |
| 4 | 84 | Erf.java:67 | 0.707107 | `if (FastMath.abs(x) > 40) {` |
| 4 | 84 | Erf.java:70 | 0.707107 | `final double ret = Gamma.regularizedGammaP(0.5, x * x, 1.0e-15, 10000);` |
| 4 | 84 | Erf.java:71 | 0.707107 | `return x < 0 ? -ret : ret;` |
| 4 | 84 | FastMath.java:375 | 0.707107 | `return Math.sqrt(a);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 57 | Erf.java:67 | 1.0 | `if (FastMath.abs(x) > 40) {` |
| 1 | 57 | Erf.java:70 | 1.0 | `final double ret = Gamma.regularizedGammaP(0.5, x * x, 1.0e-15, 10000);` |
| 1 | 57 | Erf.java:71 | 1.0 | `return x < 0 ? -ret : ret;` |
| 1 | 57 | FastMath.java:375 | 1.0 | `return Math.sqrt(a);` |
| 1 | 57 | FastMath.java:3020 | 1.0 | `return (x < 0.0) ? -x : (x == 0.0) ? 0.0 : x; // -0.0 => +0.0` |
| 1 | 57 | FastMath.java:3535 | 1.0 | `if (a > b) {` |
| 1 | 57 | FastMath.java:3538 | 1.0 | `if (a < b) {` |
| 1 | 57 | FastMath.java:3539 | 1.0 | `return b;` |
| 1 | 57 | Gamma.java:154 | 1.0 | `if (Double.isNaN(a) || Double.isNaN(x) || (a <= 0.0) || (x < 0.0)) {` |
| 1 | 57 | Gamma.java:155 | 1.0 | `ret = Double.NaN;` |

