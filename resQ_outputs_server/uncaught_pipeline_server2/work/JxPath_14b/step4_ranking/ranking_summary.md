# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CoreFunction.java', 656), ('CoreFunction.java', 662), ('CoreFunction.java', 668)]

Ground_Truth_Answerable: True

- SBFL   ranked 5321 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 169 | CoreFunction.java:150 | 1.0 | `switch(functionCode) {` |
| 1 | 169 | CoreFunction.java:153 | 1.0 | `return true;` |
| 1 | 169 | CoreFunction.java:236 | 1.0 | `return functionConcat(context);` |
| 1 | 169 | CoreFunction.java:238 | 1.0 | `return functionStartsWith(context);` |
| 1 | 169 | CoreFunction.java:242 | 1.0 | `return functionSubstringBefore(context);` |
| 1 | 169 | CoreFunction.java:244 | 1.0 | `return functionSubstringAfter(context);` |
| 1 | 169 | CoreFunction.java:246 | 1.0 | `return functionSubstring(context);` |
| 1 | 169 | CoreFunction.java:248 | 1.0 | `return functionStringLength(context);` |
| 1 | 169 | CoreFunction.java:250 | 1.0 | `return functionNormalizeSpace(context);` |
| 1 | 169 | CoreFunction.java:252 | 1.0 | `return functionTranslate(context);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

