# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Gamma.java', 37)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/special/Gamma.java', 37)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 864 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gamma.java:200 | 0.377964 | `return regularizedGammaQ(a, x, DEFAULT_EPSILON, Integer.MAX_VALUE);` |
| 2 | 6 | Gamma.java:237 | 0.267261 | `} else if (x < a || a < 1.0) {` |
| 2 | 6 | Gamma.java:243 | 0.267261 | `ContinuedFraction cf = new ContinuedFraction() {` |
| 2 | 6 | Gamma.java:248 | 0.267261 | `return ((2.0 * n) + 1.0) - a + x;` |
| 2 | 6 | Gamma.java:252 | 0.267261 | `return n * (a - n);` |
| 2 | 6 | Gamma.java:256 | 0.267261 | `ret = 1.0 / cf.evaluate(x, epsilon, maxIterations);` |
| 2 | 6 | Gamma.java:257 | 0.267261 | `ret = Math.exp(-x + (a * Math.log(x)) - logGamma(a)) * ret;` |
| 8 | 1 | Gamma.java:235 | 0.258199 | `} else if (x == 0.0) {` |
| 9 | 1 | Gamma.java:120 | 0.235702 | `return regularizedGammaP(a, x, DEFAULT_EPSILON, Integer.MAX_VALUE);` |
| 10 | 9 | Gamma.java:168 | 0.229416 | `double n = 0.0; // current element index` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

