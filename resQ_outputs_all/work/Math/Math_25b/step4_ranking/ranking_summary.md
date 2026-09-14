# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HarmonicFitter.java', 323), ('HarmonicFitter.java', 325)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HarmonicFitter.java', 323, '->', 300), ('HarmonicFitter.java', 325, '->', 300)]

Ground_Truth_Answerable: True

- SBFL   ranked 1124 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | FastMath.java:2215 | 0.707107 | `long bits = Double.doubleToLongBits(x);` |
| 1 | 9 | FastMath.java:2216 | 0.707107 | `if (bits < 0) {` |
| 1 | 9 | FastMath.java:2219 | 0.707107 | `return 0.0;` |
| 1 | 9 | FastMath.java:2560 | 0.707107 | `final double result = x * y;` |
| 1 | 9 | FastMath.java:2561 | 0.707107 | `final double invx = 1d / x;` |
| 1 | 9 | FastMath.java:2562 | 0.707107 | `final double invy = 1d / y;` |
| 1 | 9 | FastMath.java:2564 | 0.707107 | `if (invx == 0) { // X is infinite` |
| 1 | 9 | FastMath.java:2572 | 0.707107 | `if (x < 0 || invx < 0) {` |
| 1 | 9 | FastMath.java:2579 | 0.707107 | `return result;` |
| 10 | 2 | HarmonicFitter.java:326 | 0.353553 | `a = FastMath.sqrt(c1 / c2);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

