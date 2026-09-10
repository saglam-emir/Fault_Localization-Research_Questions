# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 1376), ('StringUtils.java', 1377), ('StringUtils.java', 1381), ('StringUtils.java', 1382), ('StringUtils.java', 1383), ('StringUtils.java', 1443), ('StringUtils.java', 1455), ('StringUtils.java', 1457), ('StringUtils.java', 1497), ('StringUtils.java', 1533), ('StringUtils.java', 1534), ('StringUtils.java', 1539), ('StringUtils.java', 1540), ('StringUtils.java', 1576), ('StringUtils.java', 1578), ('StringUtils.java', 1678), ('StringUtils.java', 1679), ('StringUtils.java', 1683), ('StringUtils.java', 1684), ('StringUtils.java', 1686)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('StringUtils.java', 1381, '->', 1380), ('StringUtils.java', 1383, '->', 1380), ('StringUtils.java', 1540, '->', 1538), ('StringUtils.java', 1578, '->', 1576), ('StringUtils.java', 1683, '->', 1682), ('StringUtils.java', 1684, '->', 1682), ('StringUtils.java', 1686, '->', 1682)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/StringUtils.java', 1534)]

- SBFL   ranked 4209 statement(s)
- Hybrid ranked 848 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | StringUtils.java:1674 | 0.342997 | `if (cs == null || searchChars == null) {` |
| 1 | 8 | StringUtils.java:1677 | 0.342997 | `int csLen = cs.length();` |
| 1 | 8 | StringUtils.java:1678 | 0.342997 | `int searchLen = searchChars.length;` |
| 1 | 8 | StringUtils.java:1679 | 0.342997 | `for (int i = 0; i < csLen; i++) {` |
| 1 | 8 | StringUtils.java:1680 | 0.342997 | `char ch = cs.charAt(i);` |
| 1 | 8 | StringUtils.java:1681 | 0.342997 | `for (int j = 0; j < searchLen; j++) {` |
| 1 | 8 | StringUtils.java:1682 | 0.342997 | `if (searchChars[j] == ch) {` |
| 1 | 8 | StringUtils.java:1685 | 0.342997 | `return false;` |
| 9 | 2 | StringUtils.java:1715 | 0.280056 | `if (cs == null || invalidChars == null) {` |
| 9 | 2 | StringUtils.java:1718 | 0.280056 | `return containsNone(cs, invalidChars.toCharArray());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | StringUtils.java:1678 | 0.316228 | `int searchLen = searchChars.length;` |
| 1 | 6 | StringUtils.java:1679 | 0.316228 | `for (int i = 0; i < csLen; i++) {` |
| 1 | 6 | StringUtils.java:1680 | 0.316228 | `char ch = cs.charAt(i);` |
| 1 | 6 | StringUtils.java:1681 | 0.316228 | `for (int j = 0; j < searchLen; j++) {` |
| 1 | 6 | StringUtils.java:1682 | 0.316228 | `if (searchChars[j] == ch) {` |
| 1 | 6 | StringUtils.java:1685 | 0.316228 | `return false;` |
| 7 | 6 | StringUtils.java:1376 | 0.223607 | `int searchLen = searchChars.length;` |
| 7 | 6 | StringUtils.java:1377 | 0.223607 | `for (int i = 0; i < csLen; i++) {` |
| 7 | 6 | StringUtils.java:1378 | 0.223607 | `char ch = cs.charAt(i);` |
| 7 | 6 | StringUtils.java:1379 | 0.223607 | `for (int j = 0; j < searchLen; j++) {` |

