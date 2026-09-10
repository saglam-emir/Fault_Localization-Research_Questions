# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringEscapeUtils.java', 86), ('StringEscapeUtils.java', 102), ('StringEscapeUtils.java', 127), ('StringEscapeUtils.java', 143), ('StringEscapeUtils.java', 154), ('StringEscapeUtils.java', 160), ('StringEscapeUtils.java', 178), ('StringEscapeUtils.java', 244), ('StringEscapeUtils.java', 245)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('StringEscapeUtils.java', 244, '->', 243)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/StringEscapeUtils.java', 154), ('src/java/org/apache/commons/lang/StringEscapeUtils.java', 178)]

- SBFL   ranked 1229 statement(s)
- Hybrid ranked 55 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | StringEscapeUtils.java:244 | 0.707107 | `out.write('\\');` |
| 1 | 3 | StringEscapeUtils.java:245 | 0.707107 | `out.write('/');` |
| 1 | 3 | StringEscapeUtils.java:246 | 0.707107 | `break;` |
| 4 | 1 | StringEscapeUtils.java:86 | 0.5 | `return escapeJavaStyleString(str, false);` |
| 5 | 15 | StringEscapeUtils.java:155 | 0.447214 | `if (str == null) {` |
| 5 | 15 | StringEscapeUtils.java:159 | 0.447214 | `StringWriter writer = new StringWriter(str.length() * 2);` |
| 5 | 15 | StringEscapeUtils.java:160 | 0.447214 | `escapeJavaStyleString(writer, str, escapeSingleQuotes);` |
| 5 | 15 | StringEscapeUtils.java:161 | 0.447214 | `return writer.toString();` |
| 5 | 15 | StringEscapeUtils.java:179 | 0.447214 | `if (out == null) {` |
| 5 | 15 | StringEscapeUtils.java:182 | 0.447214 | `if (str == null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | StringEscapeUtils.java:86 | 1.0 | `return escapeJavaStyleString(str, false);` |
| 1 | 11 | StringEscapeUtils.java:159 | 1.0 | `StringWriter writer = new StringWriter(str.length() * 2);` |
| 1 | 11 | StringEscapeUtils.java:160 | 1.0 | `escapeJavaStyleString(writer, str, escapeSingleQuotes);` |
| 1 | 11 | StringEscapeUtils.java:161 | 1.0 | `return writer.toString();` |
| 1 | 11 | StringEscapeUtils.java:182 | 1.0 | `if (str == null) {` |
| 1 | 11 | StringEscapeUtils.java:187 | 1.0 | `for (int i = 0; i < sz; i++) {` |
| 1 | 11 | StringEscapeUtils.java:188 | 1.0 | `char ch = str.charAt(i);` |
| 1 | 11 | StringEscapeUtils.java:228 | 1.0 | `switch (ch) {` |
| 1 | 11 | StringEscapeUtils.java:244 | 1.0 | `out.write('\\');` |
| 1 | 11 | StringEscapeUtils.java:245 | 1.0 | `out.write('/');` |

