# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultivariateNormalDistribution.java', 183)]

Ground_Truth_Answerable: True

- SBFL   ranked 1460 statement(s)
- Hybrid ranked 35 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 22 | AbstractRealDistribution.java:50 | 1.0 | `@Deprecated` |
| 1 | 22 | AbstractRealDistribution.java:60 | 1.0 | `private double solverAbsoluteAccuracy = SOLVER_DEFAULT_ABSOLUTE_ACCURACY;` |
| 1 | 22 | AbstractRealDistribution.java:76 | 1.0 | `protected AbstractRealDistribution(RandomGenerator rng) {` |
| 1 | 22 | AbstractRealDistribution.java:77 | 1.0 | `random = rng;` |
| 1 | 22 | FastMath.java:1614 | 1.0 | `return 1.0;` |
| 1 | 22 | NormalDistribution.java:44 | 1.0 | `private static final double SQRT2PI = FastMath.sqrt(2 * FastMath.PI);` |
| 1 | 22 | NormalDistribution.java:46 | 1.0 | `private static final double SQRT2 = FastMath.sqrt(2.0);` |
| 1 | 22 | NormalDistribution.java:71 | 1.0 | `this(mean, sd, DEFAULT_INVERSE_ABSOLUTE_ACCURACY);` |
| 1 | 22 | NormalDistribution.java:86 | 1.0 | `this(new Well19937c(), mean, sd, inverseCumAccuracy);` |
| 1 | 22 | NormalDistribution.java:104 | 1.0 | `super(rng);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 35 | AbstractRealDistribution.java:50 | 1.0 | `@Deprecated` |
| 1 | 35 | AbstractRealDistribution.java:60 | 1.0 | `private double solverAbsoluteAccuracy = SOLVER_DEFAULT_ABSOLUTE_ACCURACY;` |
| 1 | 35 | AbstractRealDistribution.java:76 | 1.0 | `protected AbstractRealDistribution(RandomGenerator rng) {` |
| 1 | 35 | AbstractRealDistribution.java:77 | 1.0 | `random = rng;` |
| 1 | 35 | AbstractWell.java:72 | 1.0 | `this(k, m1, m2, m3, null);` |
| 1 | 35 | AbstractWell.java:94 | 1.0 | `protected AbstractWell(final int k, final int m1, final int m2, final int m3, final int[] seed) {` |
| 1 | 35 | AbstractWell.java:100 | 1.0 | `final int r = (k + w - 1) / w;` |
| 1 | 35 | AbstractWell.java:101 | 1.0 | `this.v      = new int[r];` |
| 1 | 35 | AbstractWell.java:102 | 1.0 | `this.index  = 0;` |
| 1 | 35 | AbstractWell.java:106 | 1.0 | `iRm1 = new int[r];` |

