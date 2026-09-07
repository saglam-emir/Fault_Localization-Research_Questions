# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationRelationalExpression.java', 76), ('CoreOperationRelationalExpression.java', 77)]

Ground_Truth_Answerable: True

- SBFL   ranked 4025 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | CoreOperationRelationalExpression.java:64 | 1.0 | `((InitialContext) right).reset();` |
| 1 | 10 | CoreOperationRelationalExpression.java:67 | 1.0 | `return findMatch((Iterator) left, (Iterator) right);` |
| 1 | 10 | CoreOperationRelationalExpression.java:101 | 1.0 | `HashSet left = new HashSet();` |
| 1 | 10 | CoreOperationRelationalExpression.java:102 | 1.0 | `while (lit.hasNext()) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:103 | 1.0 | `left.add(lit.next());` |
| 1 | 10 | CoreOperationRelationalExpression.java:105 | 1.0 | `while (rit.hasNext()) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:106 | 1.0 | `if (containsMatch(left.iterator(), rit.next())) {` |
| 1 | 10 | CoreOperationRelationalExpression.java:107 | 1.0 | `return true;` |
| 1 | 10 | ValueUtils.java:144 | 1.0 | `return 1;` |
| 1 | 10 | VariablePointer.java:264 | 1.0 | `return (actual ? System.identityHashCode(variables) : 0)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

