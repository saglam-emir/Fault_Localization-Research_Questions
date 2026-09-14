# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastMath.java', 313), ('FastMath.java', 1541)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/util/FastMath.java', 313)]

- SBFL   ranked 24962 statement(s)
- Hybrid ranked 634 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | DstNormalization.java:28 | 0.516398 | `public enum DstNormalization {` |
| 1 | 3 | DstNormalization.java:41 | 0.516398 | `STANDARD_DST_I,` |
| 1 | 3 | DstNormalization.java:56 | 0.516398 | `ORTHOGONAL_DST_I` |
| 4 | 3 | DctNormalization.java:28 | 0.447214 | `public enum DctNormalization {` |
| 4 | 3 | DctNormalization.java:46 | 0.447214 | `STANDARD_DCT_I,` |
| 4 | 3 | DctNormalization.java:66 | 0.447214 | `ORTHOGONAL_DCT_I;` |
| 7 | 1 | FastMath.java:1542 | 0.258199 | `return pow(-x, y);` |
| 8 | 1 | FastMath.java:1541 | 0.11547 | `if (y >= TWO_POWER_52 || y <= -TWO_POWER_52) {` |
| 9 | 3 | MersenneTwister.java:131 | 0.037662 | `public MersenneTwister(long seed) {` |
| 9 | 3 | MersenneTwister.java:132 | 0.037662 | `mt = new int[N];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 634 | AbstractDifferentiableUnivariateSolver.java:32 | 0.0 | `@Deprecated` |
| 1 | 634 | AbstractDifferentiableUnivariateSolver.java:45 | 0.0 | `super(absoluteAccuracy);` |
| 1 | 634 | AbstractDifferentiableUnivariateSolver.java:71 | 0.0 | `incrementEvaluationCount();` |
| 1 | 634 | AbstractDifferentiableUnivariateSolver.java:81 | 0.0 | `super.setup(maxEval, f, min, max, startValue);` |
| 1 | 634 | AbstractDifferentiableUnivariateSolver.java:82 | 0.0 | `functionDerivative = f.derivative();` |
| 1 | 634 | AbstractIntegerDistribution.java:46 | 0.0 | `@Deprecated` |
| 1 | 634 | AbstractIntegerDistribution.java:64 | 0.0 | `protected AbstractIntegerDistribution(RandomGenerator rng) {` |
| 1 | 634 | AbstractIntegerDistribution.java:65 | 0.0 | `random = rng;` |
| 1 | 634 | AbstractIntegrator.java:223 | 0.0 | `final ExpandableStatefulODE expandableODE = new ExpandableStatefulODE(equations);` |
| 1 | 634 | AbstractIntegrator.java:231 | 0.0 | `System.arraycopy(expandableODE.getPrimaryState(), 0, y, 0, y.length);` |

