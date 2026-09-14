# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Variance.java', 520)]

Ground_Truth_Answerable: True

- SBFL   ranked 4115 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4115 | AbstractContinuousDistribution.java:50 | 0.0 | `protected final RandomDataImpl randomData = new RandomDataImpl();` |
| 1 | 4115 | AbstractContinuousDistribution.java:55 | 0.0 | `private double solverAbsoluteAccuracy = SOLVER_DEFAULT_ABSOLUTE_ACCURACY;` |
| 1 | 4115 | AbstractContinuousDistribution.java:59 | 0.0 | `protected AbstractContinuousDistribution() {}` |
| 1 | 4115 | AbstractDistribution.java:36 | 0.0 | `private double numericalMean = Double.NaN;` |
| 1 | 4115 | AbstractDistribution.java:39 | 0.0 | `private boolean numericalMeanIsCalculated = false;` |
| 1 | 4115 | AbstractDistribution.java:42 | 0.0 | `private double numericalVariance = Double.NaN;` |
| 1 | 4115 | AbstractDistribution.java:45 | 0.0 | `private boolean numericalVarianceIsCalculated = false;` |
| 1 | 4115 | AbstractDistribution.java:51 | 0.0 | `super();` |
| 1 | 4115 | AbstractIntegrator.java:85 | 0.0 | `public AbstractIntegrator(final String name) {` |
| 1 | 4115 | AbstractIntegrator.java:86 | 0.0 | `this.name = name;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

