# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HypergeometricDistribution.java', 268)]

Ground_Truth_Answerable: True

- SBFL   ranked 659 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | AbstractIntegerDistribution.java:130 | 1.0 | `double k = FastMath.sqrt((1.0 - p) / p);` |
| 1 | 29 | AbstractIntegerDistribution.java:131 | 1.0 | `double tmp = mu - k * sigma;` |
| 1 | 29 | AbstractIntegerDistribution.java:132 | 1.0 | `if (tmp > lower) {` |
| 1 | 29 | AbstractIntegerDistribution.java:135 | 1.0 | `k = 1.0 / k;` |
| 1 | 29 | AbstractIntegerDistribution.java:136 | 1.0 | `tmp = mu + k * sigma;` |
| 1 | 29 | AbstractIntegerDistribution.java:137 | 1.0 | `if (tmp < upper) {` |
| 1 | 29 | AbstractIntegerDistribution.java:138 | 1.0 | `upper = ((int) Math.ceil(tmp)) - 1;` |
| 1 | 29 | AbstractIntegerDistribution.java:193 | 1.0 | `return inverseCumulativeProbability(random.nextDouble());` |
| 1 | 29 | BitsStreamGenerator.java:90 | 1.0 | `final long high = ((long) next(26)) << 26;` |
| 1 | 29 | BitsStreamGenerator.java:91 | 1.0 | `final int  low  = next(26);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

