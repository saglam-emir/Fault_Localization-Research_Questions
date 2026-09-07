# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('$Gson$Types.java', 278), ('$Gson$Types.java', 279)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/$Gson$Types.java', 278)]

- SBFL   ranked 1307 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 50 | $Gson$Types.java:320 | 1.0 | `if (context == Properties.class) {` |
| 1 | 50 | $Gson$Types.java:324 | 1.0 | `Type mapType = getSupertype(context, contextRawType, Map.class);` |
| 1 | 50 | $Gson$Types.java:326 | 1.0 | `if (mapType instanceof ParameterizedType) {` |
| 1 | 50 | $Gson$Types.java:327 | 1.0 | `ParameterizedType mapParameterizedType = (ParameterizedType) mapType;` |
| 1 | 50 | $Gson$Types.java:328 | 1.0 | `return mapParameterizedType.getActualTypeArguments();` |
| 1 | 50 | ConstructorConstructor.java:179 | 1.0 | `if (ConcurrentNavigableMap.class.isAssignableFrom(rawType)) {` |
| 1 | 50 | ConstructorConstructor.java:185 | 1.0 | `} else if (ConcurrentMap.class.isAssignableFrom(rawType)) {` |
| 1 | 50 | ConstructorConstructor.java:191 | 1.0 | `} else if (SortedMap.class.isAssignableFrom(rawType)) {` |
| 1 | 50 | ConstructorConstructor.java:197 | 1.0 | `} else if (type instanceof ParameterizedType && !(String.class.isAssignableFrom(` |
| 1 | 50 | ConstructorConstructor.java:205 | 1.0 | `return new ObjectConstructor<T>() {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

