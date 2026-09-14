# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ClassUtils.java', 910)]

Ground_Truth_Answerable: True

- SBFL   ranked 1353 statement(s)
- Hybrid ranked 198 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | ClassUtils.java:903 | 1.0 | `if (array == null) {` |
| 1 | 8 | ClassUtils.java:904 | 1.0 | `return null;` |
| 1 | 8 | ClassUtils.java:905 | 1.0 | `} else if (array.length == 0) {` |
| 1 | 8 | ClassUtils.java:906 | 1.0 | `return ArrayUtils.EMPTY_CLASS_ARRAY;` |
| 1 | 8 | ClassUtils.java:908 | 1.0 | `Class<?>[] classes = new Class[array.length];` |
| 1 | 8 | ClassUtils.java:909 | 1.0 | `for (int i = 0; i < array.length; i++) {` |
| 1 | 8 | ClassUtils.java:910 | 1.0 | `classes[i] = array[i].getClass();` |
| 1 | 8 | ClassUtils.java:912 | 1.0 | `return classes;` |
| 9 | 19 | ArrayUtils.java:55 | 0.156174 | `public static final Object[] EMPTY_OBJECT_ARRAY = new Object[0];` |
| 9 | 19 | ArrayUtils.java:59 | 0.156174 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 198 | ArrayUtils.java:59 | 0.0 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |
| 1 | 198 | ArrayUtils.java:1207 | 0.0 | `return false;` |
| 1 | 198 | ArrayUtils.java:1209 | 0.0 | `return true;` |
| 1 | 198 | ClassUtils.java:73 | 0.0 | `private static final Map<Class<?>, Class<?>> primitiveWrapperMap = new HashMap<Class<?>, Class<?>>();` |
| 1 | 198 | ClassUtils.java:75 | 0.0 | `primitiveWrapperMap.put(Boolean.TYPE, Boolean.class);` |
| 1 | 198 | ClassUtils.java:76 | 0.0 | `primitiveWrapperMap.put(Byte.TYPE, Byte.class);` |
| 1 | 198 | ClassUtils.java:77 | 0.0 | `primitiveWrapperMap.put(Character.TYPE, Character.class);` |
| 1 | 198 | ClassUtils.java:78 | 0.0 | `primitiveWrapperMap.put(Short.TYPE, Short.class);` |
| 1 | 198 | ClassUtils.java:79 | 0.0 | `primitiveWrapperMap.put(Integer.TYPE, Integer.class);` |
| 1 | 198 | ClassUtils.java:80 | 0.0 | `primitiveWrapperMap.put(Long.TYPE, Long.class);` |

