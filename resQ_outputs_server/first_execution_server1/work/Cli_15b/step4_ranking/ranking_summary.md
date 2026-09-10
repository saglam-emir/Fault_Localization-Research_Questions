# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('WriteableCommandLineImpl.java', 117), ('WriteableCommandLineImpl.java', 118), ('WriteableCommandLineImpl.java', 122), ('WriteableCommandLineImpl.java', 123), ('WriteableCommandLineImpl.java', 124), ('WriteableCommandLineImpl.java', 127), ('WriteableCommandLineImpl.java', 128)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 124), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 127), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 128)]

- SBFL   ranked 1223 statement(s)
- Hybrid ranked 253 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Parser.java:174 | 0.353553 | `this.helpTrigger = helpTrigger;` |
| 2 | 1 | WriteableCommandLineImpl.java:249 | 0.333333 | `defaultValues.put(option, defaults);` |
| 3 | 6 | ArgumentBuilder.java:251 | 0.288675 | `if (defaultValue == null) {` |
| 3 | 6 | ArgumentBuilder.java:255 | 0.288675 | `if (this.defaultValues == null) {` |
| 3 | 6 | ArgumentBuilder.java:256 | 0.288675 | `this.defaultValues = new ArrayList(1);` |
| 3 | 6 | ArgumentBuilder.java:258 | 0.288675 | `this.defaultValues.add(defaultValue);` |
| 3 | 6 | ArgumentBuilder.java:259 | 0.288675 | `return this;` |
| 3 | 6 | CommandLineImpl.java:38 | 0.288675 | `return getValues(getOption(trigger), Collections.EMPTY_LIST);` |
| 9 | 1 | ArgumentImpl.java:129 | 0.258199 | `if (valueDefaults.size() > maximum) {` |
| 10 | 1 | ArgumentImpl.java:125 | 0.25 | `if (valueDefaults.size() < minimum) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CommandLineImpl.java:38 | 0.5 | `return getValues(getOption(trigger), Collections.EMPTY_LIST);` |
| 2 | 57 | ArgumentBuilder.java:255 | 0.316228 | `if (this.defaultValues == null) {` |
| 2 | 57 | ArgumentBuilder.java:256 | 0.316228 | `this.defaultValues = new ArrayList(1);` |
| 2 | 57 | ArgumentBuilder.java:258 | 0.316228 | `this.defaultValues.add(defaultValue);` |
| 2 | 57 | ArgumentBuilder.java:259 | 0.316228 | `return this;` |
| 2 | 57 | ArgumentImpl.java:207 | 0.316228 | `return this.initialSeparator;` |
| 2 | 57 | CommandLineImpl.java:32 | 0.316228 | `public abstract class CommandLineImpl implements CommandLine {` |
| 2 | 57 | DefaultOption.java:132 | 0.316228 | `final String argument = (String) arguments.next();` |
| 2 | 57 | DefaultOption.java:134 | 0.316228 | `if (triggers.contains(argument)) {` |
| 2 | 57 | DefaultOption.java:135 | 0.316228 | `commandLine.addOption(this);` |

