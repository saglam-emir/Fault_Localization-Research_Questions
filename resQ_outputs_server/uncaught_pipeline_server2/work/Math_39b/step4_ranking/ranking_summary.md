# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EmbeddedRungeKuttaIntegrator.java', 250)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('EmbeddedRungeKuttaIntegrator.java', 250, '->', 226)]

Ground_Truth_Answerable: True

- SBFL   ranked 3380 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | FastMath.java:3252 | 0.707107 | `if (Double.isNaN(d) || Double.isNaN(direction)) {` |
| 1 | 9 | FastMath.java:3254 | 0.707107 | `} else if (d == direction) {` |
| 1 | 9 | FastMath.java:3256 | 0.707107 | `} else if (Double.isInfinite(d)) {` |
| 1 | 9 | FastMath.java:3258 | 0.707107 | `} else if (d == 0) {` |
| 1 | 9 | FastMath.java:3259 | 0.707107 | `return (direction < 0) ? -Double.MIN_VALUE : Double.MIN_VALUE;` |
| 1 | 9 | FastMath.java:3264 | 0.707107 | `final long bits = Double.doubleToLongBits(d);` |
| 1 | 9 | FastMath.java:3265 | 0.707107 | `final long sign = bits & 0x8000000000000000L;` |
| 1 | 9 | FastMath.java:3266 | 0.707107 | `if ((direction < d) ^ (sign == 0L)) {` |
| 1 | 9 | FastMath.java:3267 | 0.707107 | `return Double.longBitsToDouble(sign | ((bits & 0x7fffffffffffffffL) + 1));` |
| 10 | 19 | DormandPrince853StepInterpolator.java:244 | 0.131306 | `super(interpolator);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

