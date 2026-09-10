# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PatternBuilder.java', 19), ('PatternBuilder.java', 21), ('PatternBuilder.java', 67)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli2/builder/PatternBuilder.java', 19), ('src/java/org/apache/commons/cli2/builder/PatternBuilder.java', 21)]

- SBFL   ranked 285 statement(s)
- Hybrid ranked 165 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 285 | ArgumentBuilder.java:34 | 1.0 | `private final static ResourceHelper resources = ResourceHelper.getResourceHelper();` |
| 1 | 285 | ArgumentBuilder.java:69 | 1.0 | `public ArgumentBuilder() {` |
| 1 | 285 | ArgumentBuilder.java:70 | 1.0 | `reset();` |
| 1 | 285 | ArgumentBuilder.java:81 | 1.0 | `final Argument argument =` |
| 1 | 285 | ArgumentBuilder.java:94 | 1.0 | `reset();` |
| 1 | 285 | ArgumentBuilder.java:96 | 1.0 | `return argument;` |
| 1 | 285 | ArgumentBuilder.java:104 | 1.0 | `name = "arg";` |
| 1 | 285 | ArgumentBuilder.java:105 | 1.0 | `description = null;` |
| 1 | 285 | ArgumentBuilder.java:106 | 1.0 | `minimum = 0;` |
| 1 | 285 | ArgumentBuilder.java:107 | 1.0 | `maximum = Integer.MAX_VALUE;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | GroupImpl.java:441 | 1.0 | `return options;` |
| 2 | 139 | ArgumentBuilder.java:34 | 0.707107 | `private final static ResourceHelper resources = ResourceHelper.getResourceHelper();` |
| 2 | 139 | ArgumentBuilder.java:69 | 0.707107 | `public ArgumentBuilder() {` |
| 2 | 139 | ArgumentBuilder.java:81 | 0.707107 | `final Argument argument =` |
| 2 | 139 | ArgumentBuilder.java:96 | 0.707107 | `return argument;` |
| 2 | 139 | ArgumentBuilder.java:104 | 0.707107 | `name = "arg";` |
| 2 | 139 | ArgumentBuilder.java:105 | 0.707107 | `description = null;` |
| 2 | 139 | ArgumentBuilder.java:108 | 0.707107 | `initialSeparator = ArgumentImpl.DEFAULT_INITIAL_SEPARATOR;` |
| 2 | 139 | ArgumentBuilder.java:109 | 0.707107 | `subsequentSeparator = ArgumentImpl.DEFAULT_SUBSEQUENT_SEPARATOR;` |
| 2 | 139 | ArgumentBuilder.java:111 | 0.707107 | `consumeRemaining = "--";` |

