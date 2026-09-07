# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreOperationCompare.java', 57), ('CoreOperationCompare.java', 61)]

Ground_Truth_Answerable: True

- SBFL   ranked 5521 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CoreOperationCompare.java:58 | 0.707107 | `l = ((EvalContext) l).getSingleNodePointer();` |
| 2 | 4 | CoreOperationCompare.java:76 | 0.5 | `if (!(l instanceof Iterator) && (r instanceof Iterator)) {` |
| 2 | 4 | CoreOperationCompare.java:79 | 0.5 | `if (l instanceof Iterator && r instanceof Iterator) {` |
| 2 | 4 | CoreOperationCompare.java:82 | 0.5 | `return equal(l, r);` |
| 2 | 4 | InfoSetUtil.java:62 | 0.5 | `return String.valueOf(object);` |
| 6 | 4 | InfoSetUtil.java:48 | 0.447214 | `if (object instanceof Boolean) {` |
| 6 | 4 | InfoSetUtil.java:51 | 0.447214 | `if (object == null) {` |
| 6 | 4 | InfoSetUtil.java:54 | 0.447214 | `if (object instanceof NodePointer) {` |
| 6 | 4 | InfoSetUtil.java:57 | 0.447214 | `if (object instanceof EvalContext) {` |
| 10 | 2 | Expression.java:143 | 0.408248 | `Object o = iterator.next();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

