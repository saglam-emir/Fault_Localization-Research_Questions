# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('WriteableCommandLine.java', 102), ('WriteableCommandLine.java', 110), ('WriteableCommandLineImpl.java', 51), ('WriteableCommandLineImpl.java', 63), ('WriteableCommandLineImpl.java', 65), ('WriteableCommandLineImpl.java', 66), ('WriteableCommandLineImpl.java', 234), ('WriteableCommandLineImpl.java', 235), ('WriteableCommandLineImpl.java', 236), ('WriteableCommandLineImpl.java', 242), ('WriteableCommandLineImpl.java', 243), ('WriteableCommandLineImpl.java', 245), ('WriteableCommandLineImpl.java', 246), ('GroupImpl.java', 513), ('GroupImpl.java', 514)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('WriteableCommandLineImpl.java', 243, '->', 240)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli2/WriteableCommandLine.java', 102), ('src/java/org/apache/commons/cli2/WriteableCommandLine.java', 110), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 51), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 63), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 65), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 66), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 234), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 235), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 246), ('src/java/org/apache/commons/cli2/option/GroupImpl.java', 514)]

- SBFL   ranked 1422 statement(s)
- Hybrid ranked 363 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | NumberValidator.java:60 | 0.57735 | `private Number minimum = null;` |
| 1 | 6 | NumberValidator.java:63 | 0.57735 | `private Number maximum = null;` |
| 1 | 6 | NumberValidator.java:69 | 0.57735 | `public NumberValidator(final NumberFormat format) {` |
| 1 | 6 | NumberValidator.java:70 | 0.57735 | `setFormat(format);` |
| 1 | 6 | NumberValidator.java:113 | 0.57735 | `return new NumberValidator(NumberFormat.getNumberInstance());` |
| 1 | 6 | NumberValidator.java:162 | 0.57735 | `this.format = format;` |
| 7 | 2 | GroupImpl.java:209 | 0.333333 | `arguments.previous();` |
| 7 | 2 | GroupImpl.java:211 | 0.333333 | `return;` |
| 9 | 3 | ArgumentBuilder.java:218 | 0.288675 | `if (newValidator == null) {` |
| 9 | 3 | ArgumentBuilder.java:221 | 0.288675 | `this.validator = newValidator;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 363 | ArgumentBuilder.java:34 | 0.0 | `private final static ResourceHelper resources = ResourceHelper.getResourceHelper();` |
| 1 | 363 | ArgumentBuilder.java:69 | 0.0 | `public ArgumentBuilder() {` |
| 1 | 363 | ArgumentBuilder.java:70 | 0.0 | `reset();` |
| 1 | 363 | ArgumentBuilder.java:81 | 0.0 | `final Argument argument =` |
| 1 | 363 | ArgumentBuilder.java:94 | 0.0 | `reset();` |
| 1 | 363 | ArgumentBuilder.java:96 | 0.0 | `return argument;` |
| 1 | 363 | ArgumentBuilder.java:104 | 0.0 | `name = "arg";` |
| 1 | 363 | ArgumentBuilder.java:105 | 0.0 | `description = null;` |
| 1 | 363 | ArgumentBuilder.java:106 | 0.0 | `minimum = 0;` |
| 1 | 363 | ArgumentBuilder.java:107 | 0.0 | `maximum = Integer.MAX_VALUE;` |

