# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationRelationalExpression.java', 88), ('CoreOperationRelationalExpression.java', 138)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/compiler/CoreOperationRelationalExpression.java', 138)]

- SBFL   ranked 3898 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CoreOperationRelationalExpression.java:88 | 1.0 | `return containsMatch((Iterator) right, left);` |
| 2 | 13 | CoreOperationAdd.java:39 | 0.707107 | `double s = 0.0;` |
| 2 | 13 | CoreOperationAdd.java:40 | 0.707107 | `for (int i = 0; i < args.length; i++) {` |
| 2 | 13 | CoreOperationAdd.java:41 | 0.707107 | `s += InfoSetUtil.doubleValue(args[i].computeValue(context));` |
| 2 | 13 | CoreOperationAdd.java:43 | 0.707107 | `return new Double(s);` |
| 2 | 13 | CoreOperationRelationalExpression.java:79 | 0.707107 | `((InitialContext) right).reset();` |
| 2 | 13 | InfoSetUtil.java:123 | 0.707107 | `if (object instanceof EvalContext) {` |
| 2 | 13 | InfoSetUtil.java:124 | 0.707107 | `EvalContext ctx = (EvalContext) object;` |
| 2 | 13 | InfoSetUtil.java:125 | 0.707107 | `Pointer ptr = ctx.getSingleNodePointer();` |
| 2 | 13 | InfoSetUtil.java:126 | 0.707107 | `return ptr == null ? Double.NaN : doubleValue(ptr);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

