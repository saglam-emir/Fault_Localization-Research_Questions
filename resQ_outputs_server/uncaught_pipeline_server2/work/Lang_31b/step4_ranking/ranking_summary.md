# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 1446), ('StringUtils.java', 1450), ('StringUtils.java', 1451), ('StringUtils.java', 1453)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('StringUtils.java', 1450, '->', 1449), ('StringUtils.java', 1451, '->', 1449), ('StringUtils.java', 1453, '->', 1449)]

Ground_Truth_Answerable: True

- SBFL   ranked 4188 statement(s)
- Hybrid ranked 842 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | StringUtils.java:1441 | 0.272166 | `if (isEmpty(cs) || ArrayUtils.isEmpty(searchChars)) {` |
| 1 | 8 | StringUtils.java:1444 | 0.272166 | `int csLength = cs.length();` |
| 1 | 8 | StringUtils.java:1445 | 0.272166 | `int searchLength = searchChars.length;` |
| 1 | 8 | StringUtils.java:1446 | 0.272166 | `for (int i = 0; i < csLength; i++) {` |
| 1 | 8 | StringUtils.java:1447 | 0.272166 | `char ch = cs.charAt(i);` |
| 1 | 8 | StringUtils.java:1448 | 0.272166 | `for (int j = 0; j < searchLength; j++) {` |
| 1 | 8 | StringUtils.java:1449 | 0.272166 | `if (searchChars[j] == ch) {` |
| 1 | 8 | StringUtils.java:1452 | 0.272166 | `return true;` |
| 9 | 2 | StringUtils.java:1487 | 0.235702 | `if (searchChars == null) {` |
| 9 | 2 | StringUtils.java:1490 | 0.235702 | `return containsAny(cs, searchChars.toCharArray());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | StringUtils.java:1445 | 0.408248 | `int searchLength = searchChars.length;` |
| 1 | 6 | StringUtils.java:1446 | 0.408248 | `for (int i = 0; i < csLength; i++) {` |
| 1 | 6 | StringUtils.java:1447 | 0.408248 | `char ch = cs.charAt(i);` |
| 1 | 6 | StringUtils.java:1448 | 0.408248 | `for (int j = 0; j < searchLength; j++) {` |
| 1 | 6 | StringUtils.java:1449 | 0.408248 | `if (searchChars[j] == ch) {` |
| 1 | 6 | StringUtils.java:1452 | 0.408248 | `return true;` |
| 7 | 1 | StringUtils.java:1490 | 0.204124 | `return containsAny(cs, searchChars.toCharArray());` |
| 8 | 1 | StringUtils.java:1487 | 0.182574 | `if (searchChars == null) {` |
| 9 | 834 | ArrayUtils.java:64 | 0.0 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 9 | 834 | ArrayUtils.java:1394 | 0.0 | `if (array == null) {` |

