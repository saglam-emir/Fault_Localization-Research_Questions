# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DateUtils.java', 624), ('DateUtils.java', 631), ('DateUtils.java', 633), ('DateUtils.java', 635), ('DateUtils.java', 637), ('DateUtils.java', 639), ('DateUtils.java', 709), ('DateUtils.java', 710)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DateUtils.java', 710, '->', 642)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/time/DateUtils.java', 624), ('src/java/org/apache/commons/lang/time/DateUtils.java', 631), ('src/java/org/apache/commons/lang/time/DateUtils.java', 633), ('src/java/org/apache/commons/lang/time/DateUtils.java', 635), ('src/java/org/apache/commons/lang/time/DateUtils.java', 637), ('src/java/org/apache/commons/lang/time/DateUtils.java', 639)]

- SBFL   ranked 502 statement(s)
- Hybrid ranked 13 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DateUtils.java:543 | 0.707107 | `if (date == null) {` |
| 1 | 5 | DateUtils.java:546 | 0.707107 | `Calendar gval = Calendar.getInstance();` |
| 1 | 5 | DateUtils.java:547 | 0.707107 | `gval.setTime(date);` |
| 1 | 5 | DateUtils.java:548 | 0.707107 | `modify(gval, field, false);` |
| 1 | 5 | DateUtils.java:549 | 0.707107 | `return gval.getTime();` |
| 6 | 16 | DateUtils.java:620 | 0.447214 | `if (val.get(Calendar.YEAR) > 280000000) {` |
| 6 | 16 | DateUtils.java:641 | 0.447214 | `boolean roundUp = false;` |
| 6 | 16 | DateUtils.java:642 | 0.447214 | `for (int i = 0; i < fields.length; i++) {` |
| 6 | 16 | DateUtils.java:643 | 0.447214 | `for (int j = 0; j < fields[i].length; j++) {` |
| 6 | 16 | DateUtils.java:644 | 0.447214 | `if (fields[i][j] == field) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | DateUtils.java:72 | 1.0 | `private static final int[][] fields = {` |
| 1 | 13 | DateUtils.java:546 | 1.0 | `Calendar gval = Calendar.getInstance();` |
| 1 | 13 | DateUtils.java:547 | 1.0 | `gval.setTime(date);` |
| 1 | 13 | DateUtils.java:548 | 1.0 | `modify(gval, field, false);` |
| 1 | 13 | DateUtils.java:549 | 1.0 | `return gval.getTime();` |
| 1 | 13 | DateUtils.java:642 | 1.0 | `for (int i = 0; i < fields.length; i++) {` |
| 1 | 13 | DateUtils.java:643 | 1.0 | `for (int j = 0; j < fields[i].length; j++) {` |
| 1 | 13 | DateUtils.java:644 | 1.0 | `if (fields[i][j] == field) {` |
| 1 | 13 | DateUtils.java:668 | 1.0 | `boolean offsetSet = false;` |
| 1 | 13 | DateUtils.java:700 | 1.0 | `if (!offsetSet) {` |

