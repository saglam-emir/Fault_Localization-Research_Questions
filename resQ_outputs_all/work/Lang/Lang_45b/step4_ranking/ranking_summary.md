# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('WordUtils.java', 616)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/WordUtils.java', 616)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 1130 statement(s)
- Hybrid ranked 132 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | StringUtils.java:851 | 1.0 | `if (str == null || searchStr == null) {` |
| 1 | 23 | StringUtils.java:855 | 1.0 | `if (searchStr.length() == 0 && startPos >= str.length()) {` |
| 1 | 23 | StringUtils.java:858 | 1.0 | `return str.indexOf(searchStr, startPos);` |
| 1 | 23 | WordUtils.java:607 | 1.0 | `if (str == null) {` |
| 1 | 23 | WordUtils.java:608 | 1.0 | `return null;` |
| 1 | 23 | WordUtils.java:610 | 1.0 | `if (str.length() == 0) {` |
| 1 | 23 | WordUtils.java:611 | 1.0 | `return StringUtils.EMPTY;` |
| 1 | 23 | WordUtils.java:618 | 1.0 | `if (upper == -1 || upper > str.length()) {` |
| 1 | 23 | WordUtils.java:619 | 1.0 | `upper = str.length();` |
| 1 | 23 | WordUtils.java:622 | 1.0 | `if (upper < lower) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 132 | StringUtils.java:855 | 0.0 | `if (searchStr.length() == 0 && startPos >= str.length()) {` |
| 1 | 132 | StringUtils.java:858 | 0.0 | `return str.indexOf(searchStr, startPos);` |
| 1 | 132 | StringUtils.java:5279 | 0.0 | `return str == null ? EMPTY : str;` |
| 1 | 132 | SystemUtils.java:614 | 0.0 | `public static final String LINE_SEPARATOR = getSystemProperty("line.separator");` |
| 1 | 132 | SystemUtils.java:1246 | 0.0 | `return System.getProperty(property);` |
| 1 | 132 | WordUtils.java:142 | 0.0 | `return wrap(str, wrapLength, null, false);` |
| 1 | 132 | WordUtils.java:164 | 0.0 | `if (str == null) {` |
| 1 | 132 | WordUtils.java:165 | 0.0 | `return null;` |
| 1 | 132 | WordUtils.java:167 | 0.0 | `if (newLineStr == null) {` |
| 1 | 132 | WordUtils.java:168 | 0.0 | `newLineStr = SystemUtils.LINE_SEPARATOR;` |

