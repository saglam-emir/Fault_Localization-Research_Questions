# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringEscapeUtils.java', 236)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('StringEscapeUtils.java', 236, '->', 221)]

Ground_Truth_Answerable: True

- SBFL   ranked 1010 statement(s)
- Hybrid ranked 168 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | StringEscapeUtils.java:122 | 1.0 | `return escapeJavaStyleString(str, true);` |
| 1 | 3 | StringEscapeUtils.java:138 | 1.0 | `escapeJavaStyleString(out, str, true);` |
| 1 | 3 | StringEscapeUtils.java:224 | 1.0 | `out.write('\\');` |
| 4 | 5 | StringEscapeUtils.java:150 | 0.707107 | `return null;` |
| 4 | 5 | StringEscapeUtils.java:173 | 0.707107 | `throw new IllegalArgumentException("The Writer must not be null");` |
| 4 | 5 | StringEscapeUtils.java:229 | 0.707107 | `out.write('\\');` |
| 4 | 5 | StringEscapeUtils.java:230 | 0.707107 | `out.write('"');` |
| 4 | 5 | StringEscapeUtils.java:231 | 0.707107 | `break;` |
| 9 | 3 | StringEscapeUtils.java:223 | 0.57735 | `if (escapeSingleQuote) {` |
| 9 | 3 | StringEscapeUtils.java:226 | 0.57735 | `out.write('\'');` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 168 | Entities.java:45 | 0.0 | `private static final String[][] BASIC_ARRAY = {{"quot", "34"}, // " - double-quote` |
| 1 | 168 | Entities.java:51 | 0.0 | `private static final String[][] APOS_ARRAY = {{"apos", "39"}, // XML apostrophe` |
| 1 | 168 | Entities.java:55 | 0.0 | `static final String[][] ISO8859_1_ARRAY = {{"nbsp", "160"}, // non-breaking space` |
| 1 | 168 | Entities.java:155 | 0.0 | `static final String[][] HTML40_ARRAY = {` |
| 1 | 168 | Entities.java:374 | 0.0 | `XML = new Entities();` |
| 1 | 168 | Entities.java:375 | 0.0 | `XML.addEntities(BASIC_ARRAY);` |
| 1 | 168 | Entities.java:376 | 0.0 | `XML.addEntities(APOS_ARRAY);` |
| 1 | 168 | Entities.java:386 | 0.0 | `HTML40 = new Entities();` |
| 1 | 168 | Entities.java:387 | 0.0 | `fillWithHtml40Entities(HTML40);` |
| 1 | 168 | Entities.java:399 | 0.0 | `entities.addEntities(BASIC_ARRAY);` |

