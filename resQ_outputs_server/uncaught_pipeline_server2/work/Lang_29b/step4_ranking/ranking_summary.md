# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SystemUtils.java', 1672)]

Ground_Truth_Answerable: True

- SBFL   ranked 3884 statement(s)
- Hybrid ranked 30 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SystemUtils.java:1673 | 0.316228 | `return toVersionInt(toJavaVersionIntArray(version, JAVA_VERSION_TRIM_SIZE));` |
| 2 | 1 | SystemUtils.java:1717 | 0.223607 | `return ArrayUtils.EMPTY_INT_ARRAY;` |
| 3 | 19 | ArrayUtils.java:56 | 0.021979 | `public static final Object[] EMPTY_OBJECT_ARRAY = new Object[0];` |
| 3 | 19 | ArrayUtils.java:60 | 0.021979 | `public static final Class<?>[] EMPTY_CLASS_ARRAY = new Class[0];` |
| 3 | 19 | ArrayUtils.java:64 | 0.021979 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 3 | 19 | ArrayUtils.java:68 | 0.021979 | `public static final long[] EMPTY_LONG_ARRAY = new long[0];` |
| 3 | 19 | ArrayUtils.java:72 | 0.021979 | `public static final Long[] EMPTY_LONG_OBJECT_ARRAY = new Long[0];` |
| 3 | 19 | ArrayUtils.java:76 | 0.021979 | `public static final int[] EMPTY_INT_ARRAY = new int[0];` |
| 3 | 19 | ArrayUtils.java:80 | 0.021979 | `public static final Integer[] EMPTY_INTEGER_OBJECT_ARRAY = new Integer[0];` |
| 3 | 19 | ArrayUtils.java:84 | 0.021979 | `public static final short[] EMPTY_SHORT_ARRAY = new short[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 30 | ArrayUtils.java:76 | 0.0 | `public static final int[] EMPTY_INT_ARRAY = new int[0];` |
| 1 | 30 | SystemUtils.java:943 | 0.0 | `public static final float JAVA_VERSION_FLOAT = getJavaVersionAsFloat();` |
| 1 | 30 | SystemUtils.java:964 | 0.0 | `public static final int JAVA_VERSION_INT = getJavaVersionAsInt();` |
| 1 | 30 | SystemUtils.java:1534 | 0.0 | `return JAVA_VERSION_FLOAT >= requiredVersion;` |
| 1 | 30 | SystemUtils.java:1556 | 0.0 | `return JAVA_VERSION_INT >= requiredVersion;` |
| 1 | 30 | SystemUtils.java:1574 | 0.0 | `if (version == null) {` |
| 1 | 30 | SystemUtils.java:1575 | 0.0 | `return false;` |
| 1 | 30 | SystemUtils.java:1577 | 0.0 | `return version.startsWith(versionPrefix);` |
| 1 | 30 | SystemUtils.java:1600 | 0.0 | `return osName.startsWith(osNamePrefix) && osVersion.startsWith(osVersionPrefix);` |
| 1 | 30 | SystemUtils.java:1616 | 0.0 | `if (osName == null) {` |

