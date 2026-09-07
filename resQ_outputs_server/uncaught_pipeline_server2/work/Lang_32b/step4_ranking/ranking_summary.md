# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HashCodeBuilder.java', 104), ('HashCodeBuilder.java', 105), ('HashCodeBuilder.java', 106), ('HashCodeBuilder.java', 107), ('HashCodeBuilder.java', 108), ('HashCodeBuilder.java', 109), ('HashCodeBuilder.java', 152), ('HashCodeBuilder.java', 522), ('HashCodeBuilder.java', 538)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HashCodeBuilder.java', 106, '->', 105)]

Ground_Truth_Answerable: True

- SBFL   ranked 194 statement(s)
- Hybrid ranked 38 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HashCodeBuilder.java:174 | 1.0 | `return;` |
| 2 | 1 | HashCodeBuilder.java:400 | 0.5 | `return reflectionHashCode(17, 37, object, false, null, null);` |
| 3 | 51 | ArrayUtils.java:55 | 0.353553 | `public static final Object[] EMPTY_OBJECT_ARRAY = new Object[0];` |
| 3 | 51 | ArrayUtils.java:59 | 0.353553 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |
| 3 | 51 | ArrayUtils.java:63 | 0.353553 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 3 | 51 | ArrayUtils.java:67 | 0.353553 | `public static final long[] EMPTY_LONG_ARRAY = new long[0];` |
| 3 | 51 | ArrayUtils.java:71 | 0.353553 | `public static final Long[] EMPTY_LONG_OBJECT_ARRAY = new Long[0];` |
| 3 | 51 | ArrayUtils.java:75 | 0.353553 | `public static final int[] EMPTY_INT_ARRAY = new int[0];` |
| 3 | 51 | ArrayUtils.java:79 | 0.353553 | `public static final Integer[] EMPTY_INTEGER_OBJECT_ARRAY = new Integer[0];` |
| 3 | 51 | ArrayUtils.java:83 | 0.353553 | `public static final short[] EMPTY_SHORT_ARRAY = new short[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | HashCodeBuilder.java:104 | 0.258199 | `private static final ThreadLocal<Set<IDKey>> REGISTRY = new ThreadLocal<Set<IDKey>>() {` |
| 1 | 2 | HashCodeBuilder.java:137 | 0.258199 | `return REGISTRY.get();` |
| 3 | 36 | ArrayUtils.java:1627 | 0.0 | `return indexOf(array, objectToFind, 0);` |
| 3 | 36 | ArrayUtils.java:1645 | 0.0 | `if (array == null) {` |
| 3 | 36 | ArrayUtils.java:1651 | 0.0 | `if (objectToFind == null) {` |
| 3 | 36 | ArrayUtils.java:1730 | 0.0 | `return indexOf(array, objectToFind) != INDEX_NOT_FOUND;` |
| 3 | 36 | HashCodeBuilder.java:152 | 0.0 | `return getRegistry().contains(new IDKey(value));` |
| 3 | 36 | HashCodeBuilder.java:173 | 0.0 | `if (isRegistered(object)) {` |
| 3 | 36 | HashCodeBuilder.java:177 | 0.0 | `register(object);` |
| 3 | 36 | HashCodeBuilder.java:178 | 0.0 | `Field[] fields = clazz.getDeclaredFields();` |

