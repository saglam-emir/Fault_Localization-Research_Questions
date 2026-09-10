# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 3298), ('StringUtils.java', 3383)]

Ground_Truth_Answerable: True

- SBFL   ranked 4251 statement(s)
- Hybrid ranked 914 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StringUtils.java:3257 | 0.333333 | `return null;` |
| 2 | 13 | StringUtils.java:3256 | 0.235702 | `if (array == null) {` |
| 2 | 13 | StringUtils.java:3260 | 0.235702 | `return join(array, separator, 0, array.length);` |
| 2 | 13 | StringUtils.java:3290 | 0.235702 | `if (array == null) {` |
| 2 | 13 | StringUtils.java:3293 | 0.235702 | `int noOfItems = (endIndex - startIndex);` |
| 2 | 13 | StringUtils.java:3294 | 0.235702 | `if (noOfItems <= 0) {` |
| 2 | 13 | StringUtils.java:3295 | 0.235702 | `return EMPTY;` |
| 2 | 13 | StringUtils.java:3298 | 0.235702 | `StringBuilder buf = new StringBuilder((array[startIndex] == null ? 16 : array[startIndex].toString().length()) + 1);` |
| 2 | 13 | StringUtils.java:3300 | 0.235702 | `for (int i = startIndex; i < endIndex; i++) {` |
| 2 | 13 | StringUtils.java:3301 | 0.235702 | `if (i > startIndex) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 914 | ArrayUtils.java:54 | 0.0 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 1 | 914 | ArrayUtils.java:1400 | 0.0 | `if (array == null) {` |
| 1 | 914 | ArrayUtils.java:1403 | 0.0 | `int i = 0;` |
| 1 | 914 | ArrayUtils.java:1404 | 0.0 | `int j = array.length - 1;` |
| 1 | 914 | ArrayUtils.java:1406 | 0.0 | `while (j > i) {` |
| 1 | 914 | ArrayUtils.java:1407 | 0.0 | `tmp = array[j];` |
| 1 | 914 | ArrayUtils.java:1408 | 0.0 | `array[j] = array[i];` |
| 1 | 914 | ArrayUtils.java:1409 | 0.0 | `array[i] = tmp;` |
| 1 | 914 | CharSequenceUtils.java:70 | 0.0 | `if (cs instanceof String) {` |
| 1 | 914 | CharSequenceUtils.java:71 | 0.0 | `return ((String) cs).indexOf(searchChar, start);` |

