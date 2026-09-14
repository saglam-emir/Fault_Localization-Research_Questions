# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ProperFractionFormat.java', 165), ('ProperFractionFormat.java', 166), ('ProperFractionFormat.java', 200), ('ProperFractionFormat.java', 201)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/fraction/ProperFractionFormat.java', 165), ('src/java/org/apache/commons/math/fraction/ProperFractionFormat.java', 166), ('src/java/org/apache/commons/math/fraction/ProperFractionFormat.java', 200), ('src/java/org/apache/commons/math/fraction/ProperFractionFormat.java', 201)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 145 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | FractionFormat.java:290 | 0.57735 | `pos.setIndex(initialIndex);` |
| 1 | 15 | FractionFormat.java:291 | 0.57735 | `pos.setErrorIndex(startIndex);` |
| 1 | 15 | FractionFormat.java:292 | 0.57735 | `return null;` |
| 1 | 15 | MathUtils.java:680 | 0.57735 | `return (x == 0) ? 0 : (x > 0) ? 1 : -1;` |
| 1 | 15 | ProperFractionFormat.java:168 | 0.57735 | `int startIndex = pos.getIndex();` |
| 1 | 15 | ProperFractionFormat.java:169 | 0.57735 | `char c = parseNextCharacter(source, pos);` |
| 1 | 15 | ProperFractionFormat.java:170 | 0.57735 | `switch (c) {` |
| 1 | 15 | ProperFractionFormat.java:177 | 0.57735 | `break;` |
| 1 | 15 | ProperFractionFormat.java:188 | 0.57735 | `parseAndIgnoreWhitespace(source, pos);` |
| 1 | 15 | ProperFractionFormat.java:191 | 0.57735 | `Number den = getDenominatorFormat().parse(source, pos);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

