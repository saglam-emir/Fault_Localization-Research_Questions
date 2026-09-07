# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Option.java', 206), ('Option.java', 216), ('WriteableCommandLineImpl.java', 74), ('GroupImpl.java', 92), ('OptionImpl.java', 36), ('OptionImpl.java', 128), ('OptionImpl.java', 129)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('GroupImpl.java', 92, '->', 90)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli2/Option.java', 206), ('src/java/org/apache/commons/cli2/Option.java', 216), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 74), ('src/java/org/apache/commons/cli2/option/OptionImpl.java', 36), ('src/java/org/apache/commons/cli2/option/OptionImpl.java', 128), ('src/java/org/apache/commons/cli2/option/OptionImpl.java', 129)]

- SBFL   ranked 1465 statement(s)
- Hybrid ranked 354 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | GroupImpl.java:465 | 0.547723 | `return minimum;` |
| 1 | 2 | GroupImpl.java:473 | 0.547723 | `return getMinimum() > 0;` |
| 3 | 4 | GroupBuilder.java:95 | 0.474342 | `this.minimum = newMinimum;` |
| 3 | 4 | GroupBuilder.java:96 | 0.474342 | `return this;` |
| 3 | 4 | GroupBuilder.java:105 | 0.474342 | `this.maximum = newMaximum;` |
| 3 | 4 | GroupBuilder.java:106 | 0.474342 | `return this;` |
| 7 | 3 | ArgumentImpl.java:159 | 0.4 | `arguments.previous();` |
| 7 | 3 | ArgumentImpl.java:161 | 0.4 | `break;` |
| 7 | 3 | GroupImpl.java:274 | 0.4 | `throw new OptionException(this, ResourceConstants.MISSING_OPTION);` |
| 10 | 1 | GroupImpl.java:285 | 0.307794 | `return name;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Parser.java:38 | 0.288675 | `public class Parser {` |
| 2 | 353 | ArgumentBuilder.java:34 | 0.0 | `private final static ResourceHelper resources = ResourceHelper.getResourceHelper();` |
| 2 | 353 | ArgumentBuilder.java:69 | 0.0 | `public ArgumentBuilder() {` |
| 2 | 353 | ArgumentBuilder.java:70 | 0.0 | `reset();` |
| 2 | 353 | ArgumentBuilder.java:81 | 0.0 | `final Argument argument =` |
| 2 | 353 | ArgumentBuilder.java:94 | 0.0 | `reset();` |
| 2 | 353 | ArgumentBuilder.java:96 | 0.0 | `return argument;` |
| 2 | 353 | ArgumentBuilder.java:104 | 0.0 | `name = "arg";` |
| 2 | 353 | ArgumentBuilder.java:105 | 0.0 | `description = null;` |
| 2 | 353 | ArgumentBuilder.java:106 | 0.0 | `minimum = 0;` |

