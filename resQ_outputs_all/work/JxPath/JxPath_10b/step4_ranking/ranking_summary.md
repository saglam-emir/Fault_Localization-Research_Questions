# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationRelationalExpression.java', 42)]

Ground_Truth_Answerable: True

- SBFL   ranked 4078 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | EvalContext.java:303 | 1.0 | `return false;` |
| 1 | 7 | InfoSetUtil.java:52 | 1.0 | `return "";` |
| 1 | 7 | InfoSetUtil.java:106 | 1.0 | `return 0.0;` |
| 1 | 7 | InfoSetUtil.java:123 | 1.0 | `return doubleValue(stringValue(object));` |
| 1 | 7 | NullPointer.java:56 | 1.0 | `return null;` |
| 1 | 7 | NullPointer.java:133 | 1.0 | `return 0;` |
| 1 | 7 | TreeCompiler.java:190 | 1.0 | `return false;` |
| 8 | 42 | InfoSetUtil.java:48 | 0.707107 | `if (object instanceof Boolean) {` |
| 8 | 42 | InfoSetUtil.java:51 | 0.707107 | `if (object == null) {` |
| 8 | 42 | InfoSetUtil.java:105 | 0.707107 | `if (object.equals("")) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

