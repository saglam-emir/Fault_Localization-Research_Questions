# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 184), ('MathUtils.java', 185), ('MathUtils.java', 186), ('MathUtils.java', 187), ('MathUtils.java', 188), ('MathUtils.java', 190), ('MathUtils.java', 196), ('MathUtils.java', 197), ('MathUtils.java', 199), ('MathUtils.java', 205), ('MathUtils.java', 208), ('MathUtils.java', 236), ('MathUtils.java', 234), ('MathUtils.java', 235), ('MathUtils.java', 277), ('MathUtils.java', 282)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('MathUtils.java', 187, '->', 186)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/util/MathUtils.java', 188), ('src/java/org/apache/commons/math/util/MathUtils.java', 190), ('src/java/org/apache/commons/math/util/MathUtils.java', 196), ('src/java/org/apache/commons/math/util/MathUtils.java', 197), ('src/java/org/apache/commons/math/util/MathUtils.java', 199), ('src/java/org/apache/commons/math/util/MathUtils.java', 205), ('src/java/org/apache/commons/math/util/MathUtils.java', 234), ('src/java/org/apache/commons/math/util/MathUtils.java', 235), ('src/java/org/apache/commons/math/util/MathUtils.java', 277), ('src/java/org/apache/commons/math/util/MathUtils.java', 282)]

- SBFL   ranked 4911 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | MathUtils.java:182 | 0.707107 | `return n;` |
| 1 | 2 | MathUtils.java:208 | 0.707107 | `return result;` |
| 3 | 5 | MathUtils.java:95 | 0.57735 | `return addAndCheck(a, b, "overflow: add");` |
| 3 | 5 | MathUtils.java:179 | 0.57735 | `return 1;` |
| 3 | 5 | MathUtils.java:181 | 0.57735 | `if ((k == 1) || (k == n - 1)) {` |
| 3 | 5 | MathUtils.java:184 | 0.57735 | `long result = Math.round(binomialCoefficientDouble(n, k));` |
| 3 | 5 | MathUtils.java:185 | 0.57735 | `if (result == Long.MAX_VALUE) {` |
| 8 | 9 | MathUtils.java:111 | 0.5 | `if (a > b) {` |
| 8 | 9 | MathUtils.java:113 | 0.5 | `ret = addAndCheck(b, a, msg);` |
| 8 | 9 | MathUtils.java:117 | 0.5 | `if (a < 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | MathUtils.java:95 | 1.0 | `return addAndCheck(a, b, "overflow: add");` |
| 1 | 7 | MathUtils.java:111 | 1.0 | `if (a > b) {` |
| 1 | 7 | MathUtils.java:113 | 1.0 | `ret = addAndCheck(b, a, msg);` |
| 1 | 7 | MathUtils.java:117 | 1.0 | `if (a < 0) {` |
| 1 | 7 | MathUtils.java:134 | 1.0 | `if (a <= Long.MAX_VALUE - b) {` |
| 1 | 7 | MathUtils.java:135 | 1.0 | `ret = a + b;` |
| 1 | 7 | MathUtils.java:141 | 1.0 | `return ret;` |

