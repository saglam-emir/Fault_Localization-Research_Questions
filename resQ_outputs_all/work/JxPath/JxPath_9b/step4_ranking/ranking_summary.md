# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationCompare.java', 37), ('CoreOperationCompare.java', 39), ('CoreOperationCompare.java', 40), ('CoreOperationCompare.java', 41), ('CoreOperationCompare.java', 43), ('CoreOperationCompare.java', 123), ('CoreOperationCompare.java', 124), ('CoreOperationCompare.java', 125), ('CoreOperationCompare.java', 126), ('CoreOperationCompare.java', 127), ('CoreOperationCompare.java', 136), ('CoreOperationCompare.java', 137), ('CoreOperationCompare.java', 138), ('CoreOperationCompare.java', 140), ('CoreOperationCompare.java', 142), ('CoreOperationCompare.java', 143), ('CoreOperationCompare.java', 144), ('CoreOperationCompare.java', 147), ('CoreOperationCompare.java', 148), ('CoreOperationCompare.java', 150), ('CoreOperationCompare.java', 146), ('CoreOperationEqual.java', 19), ('CoreOperationEqual.java', 32), ('CoreOperationEqual.java', 33), ('CoreOperationEqual.java', 34), ('CoreOperationNotEqual.java', 19), ('CoreOperationNotEqual.java', 29), ('CoreOperationNotEqual.java', 32), ('CoreOperationNotEqual.java', 33), ('CoreOperationNotEqual.java', 34)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CoreOperationCompare.java', 148, '->', 147)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationCompare.java', 37), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationCompare.java', 39), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationCompare.java', 41), ('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationCompare.java', 43)]

- SBFL   ranked 5550 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | CoreOperationCompare.java:125 | 1.0 | `return true;` |
| 1 | 10 | CoreOperationRelationalExpression.java:64 | 1.0 | `((InitialContext) right).reset();` |
| 1 | 10 | CoreOperationRelationalExpression.java:67 | 1.0 | `return findMatch((Iterator) left, (Iterator) right);` |
| 1 | 10 | CoreOperationRelationalExpression.java:77 | 1.0 | `return false;` |
| 1 | 10 | CoreOperationRelationalExpression.java:107 | 1.0 | `HashSet left = new HashSet();` |
| 1 | 10 | CoreOperationRelationalExpression.java:108 | 1.0 | `while (lit.hasNext()) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:109 | 1.0 | `left.add(lit.next());` |
| 1 | 10 | CoreOperationRelationalExpression.java:111 | 1.0 | `while (rit.hasNext()) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:112 | 1.0 | `if (containsMatch(left.iterator(), rit.next())) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:116 | 1.0 | `return false;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

