# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 3676)]

Ground_Truth_Answerable: True

- SBFL   ranked 4084 statement(s)
- Hybrid ranked 797 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | StringUtils.java:3502 | 0.353553 | `return replaceEach(text, searchList, replacementList, false, 0);` |
| 1 | 3 | StringUtils.java:3648 | 0.353553 | `continue;` |
| 1 | 3 | StringUtils.java:3727 | 0.353553 | `return result;` |
| 4 | 48 | StringUtils.java:3612 | 0.25 | `if (text == null || text.length() == 0 || searchList == null ||` |
| 4 | 48 | StringUtils.java:3615 | 0.25 | `return text;` |
| 4 | 48 | StringUtils.java:3619 | 0.25 | `if (timeToLive < 0) {` |
| 4 | 48 | StringUtils.java:3623 | 0.25 | `int searchLength = searchList.length;` |
| 4 | 48 | StringUtils.java:3624 | 0.25 | `int replacementLength = replacementList.length;` |
| 4 | 48 | StringUtils.java:3627 | 0.25 | `if (searchLength != replacementLength) {` |
| 4 | 48 | StringUtils.java:3635 | 0.25 | `boolean[] noMoreMatchesForReplIndex = new boolean[searchLength];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 797 | ArrayUtils.java:62 | 0.0 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 1 | 797 | ArrayUtils.java:983 | 0.0 | `if (array == null) {` |
| 1 | 797 | ArrayUtils.java:986 | 0.0 | `int i = 0;` |
| 1 | 797 | ArrayUtils.java:987 | 0.0 | `int j = array.length - 1;` |
| 1 | 797 | ArrayUtils.java:989 | 0.0 | `while (j > i) {` |
| 1 | 797 | ArrayUtils.java:990 | 0.0 | `tmp = array[j];` |
| 1 | 797 | ArrayUtils.java:991 | 0.0 | `array[j] = array[i];` |
| 1 | 797 | ArrayUtils.java:992 | 0.0 | `array[i] = tmp;` |
| 1 | 797 | CharUtils.java:443 | 0.0 | `return ch >= 32 && ch < 127;` |
| 1 | 797 | ContextedException.java:83 | 0.0 | `exceptionContext = new DefaultExceptionContext();` |

