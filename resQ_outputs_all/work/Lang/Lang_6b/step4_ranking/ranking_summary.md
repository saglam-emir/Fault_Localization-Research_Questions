# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CharSequenceTranslator.java', 95)]

Ground_Truth_Answerable: True

- SBFL   ranked 1583 statement(s)
- Hybrid ranked 127 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StringEscapeUtils.java:556 | 0.707107 | `return ESCAPE_CSV.translate(input);` |
| 2 | 14 | StringEscapeUtils.java:156 | 0.57735 | `if(index != 0) {` |
| 2 | 14 | StringEscapeUtils.java:160 | 0.57735 | `if (StringUtils.containsNone(input.toString(), CSV_SEARCH_CHARS)) {` |
| 2 | 14 | StringEscapeUtils.java:161 | 0.57735 | `out.write(input.toString());` |
| 2 | 14 | StringEscapeUtils.java:167 | 0.57735 | `return input.length();` |
| 2 | 14 | StringUtils.java:1737 | 0.57735 | `if (cs == null || searchChars == null) {` |
| 2 | 14 | StringUtils.java:1740 | 0.57735 | `int csLen = cs.length();` |
| 2 | 14 | StringUtils.java:1741 | 0.57735 | `int csLast = csLen - 1;` |
| 2 | 14 | StringUtils.java:1742 | 0.57735 | `int searchLen = searchChars.length;` |
| 2 | 14 | StringUtils.java:1743 | 0.57735 | `int searchLast = searchLen - 1;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 127 | AggregateTranslator.java:52 | 0.0 | `int consumed = translator.translate(input, index, out);` |
| 1 | 127 | AggregateTranslator.java:53 | 0.0 | `if(consumed != 0) {` |
| 1 | 127 | AggregateTranslator.java:54 | 0.0 | `return consumed;` |
| 1 | 127 | AggregateTranslator.java:57 | 0.0 | `return 0;` |
| 1 | 127 | CharSequenceTranslator.java:54 | 0.0 | `if (input == null) {` |
| 1 | 127 | CharSequenceTranslator.java:55 | 0.0 | `return null;` |
| 1 | 127 | CharSequenceTranslator.java:58 | 0.0 | `StringWriter writer = new StringWriter(input.length() * 2);` |
| 1 | 127 | CharSequenceTranslator.java:59 | 0.0 | `translate(input, writer);` |
| 1 | 127 | CharSequenceTranslator.java:60 | 0.0 | `return writer.toString();` |
| 1 | 127 | CharSequenceTranslator.java:79 | 0.0 | `if (input == null) {` |

