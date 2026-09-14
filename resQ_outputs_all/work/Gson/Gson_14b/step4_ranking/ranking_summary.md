# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('$Gson$Types.java', 79), ('$Gson$Types.java', 80), ('$Gson$Types.java', 90), ('$Gson$Types.java', 91)]

Ground_Truth_Answerable: True

- SBFL   ranked 560 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | $Gson$Preconditions.java:38 | 1.0 | `if (obj == null) {` |
| 1 | 19 | $Gson$Preconditions.java:41 | 1.0 | `return obj;` |
| 1 | 19 | $Gson$Preconditions.java:45 | 1.0 | `if (!condition) {` |
| 1 | 19 | $Gson$Types.java:44 | 1.0 | `static final Type[] EMPTY_TYPE_ARRAY = new Type[] {};` |
| 1 | 19 | $Gson$Types.java:100 | 1.0 | `if (type instanceof Class) {` |
| 1 | 19 | $Gson$Types.java:101 | 1.0 | `Class<?> c = (Class<?>) type;` |
| 1 | 19 | $Gson$Types.java:102 | 1.0 | `return c.isArray() ? new GenericArrayTypeImpl(canonicalize(c.getComponentType())) : c;` |
| 1 | 19 | $Gson$Types.java:104 | 1.0 | `} else if (type instanceof ParameterizedType) {` |
| 1 | 19 | $Gson$Types.java:109 | 1.0 | `} else if (type instanceof GenericArrayType) {` |
| 1 | 19 | $Gson$Types.java:113 | 1.0 | `} else if (type instanceof WildcardType) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

