# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArrayUtils.java', 2962), ('ArrayUtils.java', 2963), ('ArrayUtils.java', 2964)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang3/ArrayUtils.java', 2963)]

- SBFL   ranked 4428 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ArrayUtils.java:2954 | 0.353553 | `if (array1 == null) {` |
| 1 | 7 | ArrayUtils.java:2956 | 0.353553 | `} else if (array2 == null) {` |
| 1 | 7 | ArrayUtils.java:2959 | 0.353553 | `final Class<?> type1 = array1.getClass().getComponentType();` |
| 1 | 7 | ArrayUtils.java:2960 | 0.353553 | `T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);` |
| 1 | 7 | ArrayUtils.java:2961 | 0.353553 | `System.arraycopy(array1, 0, joinedArray, 0, array1.length);` |
| 1 | 7 | ArrayUtils.java:2962 | 0.353553 | `System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);` |
| 1 | 7 | ArrayUtils.java:2964 | 0.353553 | `return joinedArray;` |
| 8 | 19 | ArrayUtils.java:54 | 0.039904 | `public static final Object[] EMPTY_OBJECT_ARRAY = new Object[0];` |
| 8 | 19 | ArrayUtils.java:58 | 0.039904 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |
| 8 | 19 | ArrayUtils.java:62 | 0.039904 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ArrayUtils.java:2954 | 0.0 | `if (array1 == null) {` |
| 1 | 7 | ArrayUtils.java:2956 | 0.0 | `} else if (array2 == null) {` |
| 1 | 7 | ArrayUtils.java:2959 | 0.0 | `final Class<?> type1 = array1.getClass().getComponentType();` |
| 1 | 7 | ArrayUtils.java:2960 | 0.0 | `T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);` |
| 1 | 7 | ArrayUtils.java:2961 | 0.0 | `System.arraycopy(array1, 0, joinedArray, 0, array1.length);` |
| 1 | 7 | ArrayUtils.java:2962 | 0.0 | `System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);` |
| 1 | 7 | ArrayUtils.java:2964 | 0.0 | `return joinedArray;` |

