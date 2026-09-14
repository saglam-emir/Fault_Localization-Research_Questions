# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArrayRealVector.java', 721), ('OpenMapRealVector.java', 498), ('OpenMapRealVector.java', 499), ('OpenMapRealVector.java', 500), ('OpenMapRealVector.java', 501), ('OpenMapRealVector.java', 502), ('OpenMapRealVector.java', 503), ('OpenMapRealVector.java', 504), ('OpenMapRealVector.java', 505), ('OpenMapRealVector.java', 506)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/linear/OpenMapRealVector.java', 498), ('src/main/java/org/apache/commons/math/linear/OpenMapRealVector.java', 504), ('src/main/java/org/apache/commons/math/linear/OpenMapRealVector.java', 506)]

- SBFL   ranked 4309 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | AbstractRealVector.java:210 | 0.707107 | `double sum = 0;` |
| 1 | 25 | AbstractRealVector.java:211 | 0.707107 | `Iterator<Entry> it = sparseIterator();` |
| 1 | 25 | AbstractRealVector.java:213 | 0.707107 | `while (it.hasNext() && (e = it.next()) != null) {` |
| 1 | 25 | AbstractRealVector.java:214 | 0.707107 | `final double value = e.getValue();` |
| 1 | 25 | AbstractRealVector.java:215 | 0.707107 | `sum += value * value;` |
| 1 | 25 | AbstractRealVector.java:217 | 0.707107 | `return Math.sqrt(sum);` |
| 1 | 25 | AbstractRealVector.java:222 | 0.707107 | `double norm = 0;` |
| 1 | 25 | AbstractRealVector.java:223 | 0.707107 | `Iterator<Entry> it = sparseIterator();` |
| 1 | 25 | AbstractRealVector.java:225 | 0.707107 | `while (it.hasNext() && (e = it.next()) != null) {` |
| 1 | 25 | AbstractRealVector.java:226 | 0.707107 | `norm += Math.abs(e.getValue());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

