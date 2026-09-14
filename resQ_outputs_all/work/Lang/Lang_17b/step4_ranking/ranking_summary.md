# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CharSequenceTranslator.java', 83), ('CharSequenceTranslator.java', 90), ('CharSequenceTranslator.java', 94), ('CharSequenceTranslator.java', 96), ('CharSequenceTranslator.java', 97), ('CharSequenceTranslator.java', 98), ('CharSequenceTranslator.java', 99), ('CharSequenceTranslator.java', 100), ('CharSequenceTranslator.java', 102), ('CharSequenceTranslator.java', 89)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CharSequenceTranslator.java', 89, '->', 86)]

Ground_Truth_Answerable: True

- SBFL   ranked 678 statement(s)
- Hybrid ranked 35 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StringEscapeUtils.java:506 | 0.707107 | `return ESCAPE_XML.translate(input);` |
| 2 | 1 | AggregateTranslator.java:57 | 0.267261 | `return 0;` |
| 3 | 4 | AggregateTranslator.java:51 | 0.25 | `for (CharSequenceTranslator translator : translators) {` |
| 3 | 4 | AggregateTranslator.java:52 | 0.25 | `int consumed = translator.translate(input, index, out);` |
| 3 | 4 | AggregateTranslator.java:53 | 0.25 | `if(consumed != 0) {` |
| 3 | 4 | LookupTranslator.java:78 | 0.25 | `return 0;` |
| 7 | 6 | LookupTranslator.java:65 | 0.242536 | `int max = longest;` |
| 7 | 6 | LookupTranslator.java:66 | 0.242536 | `if (index + longest > input.length()) {` |
| 7 | 6 | LookupTranslator.java:70 | 0.242536 | `for (int i = max; i >= shortest; i--) {` |
| 7 | 6 | LookupTranslator.java:71 | 0.242536 | `CharSequence subSeq = input.subSequence(index, index + i);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 35 | AggregateTranslator.java:52 | 0.0 | `int consumed = translator.translate(input, index, out);` |
| 1 | 35 | AggregateTranslator.java:57 | 0.0 | `return 0;` |
| 1 | 35 | CharSequenceTranslator.java:54 | 0.0 | `if (input == null) {` |
| 1 | 35 | CharSequenceTranslator.java:58 | 0.0 | `StringWriter writer = new StringWriter(input.length() * 2);` |
| 1 | 35 | CharSequenceTranslator.java:59 | 0.0 | `translate(input, writer);` |
| 1 | 35 | CharSequenceTranslator.java:60 | 0.0 | `return writer.toString();` |
| 1 | 35 | CharSequenceTranslator.java:79 | 0.0 | `if (input == null) {` |
| 1 | 35 | CharSequenceTranslator.java:82 | 0.0 | `int pos = 0;` |
| 1 | 35 | CharSequenceTranslator.java:83 | 0.0 | `int len = Character.codePointCount(input, 0, input.length());` |
| 1 | 35 | CharSequenceTranslator.java:84 | 0.0 | `while (pos < len) {` |

