# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('$Gson$Types.java', 342), ('$Gson$Types.java', 343)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('$Gson$Types.java', 342, '->', 340)]

Ground_Truth_Answerable: True

- SBFL   ranked 559 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | $Gson$Types.java:396 | 0.707107 | `} else if (originalUpperBound.length == 1) {` |
| 2 | 379 | $Gson$Types.java:108 | 0.632456 | `} else if (type instanceof ParameterizedType) {` |
| 2 | 379 | $Gson$Types.java:109 | 0.632456 | `ParameterizedType p = (ParameterizedType) type;` |
| 2 | 379 | $Gson$Types.java:110 | 0.632456 | `return new ParameterizedTypeImpl(p.getOwnerType(),` |
| 2 | 379 | $Gson$Types.java:113 | 0.632456 | `} else if (type instanceof GenericArrayType) {` |
| 2 | 379 | $Gson$Types.java:117 | 0.632456 | `} else if (type instanceof WildcardType) {` |
| 2 | 379 | $Gson$Types.java:118 | 0.632456 | `WildcardType w = (WildcardType) type;` |
| 2 | 379 | $Gson$Types.java:119 | 0.632456 | `return new WildcardTypeImpl(w.getUpperBounds(), w.getLowerBounds());` |
| 2 | 379 | $Gson$Types.java:123 | 0.632456 | `return type;` |
| 2 | 379 | $Gson$Types.java:128 | 0.632456 | `if (type instanceof Class<?>) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

