# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('WriteableCommandLine.java', 47), ('WriteableCommandLineImpl.java', 132), ('WriteableCommandLineImpl.java', 133), ('WriteableCommandLineImpl.java', 135), ('ArgumentImpl.java', 144)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli2/WriteableCommandLine.java', 47), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 132), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 133), ('src/java/org/apache/commons/cli2/commandline/WriteableCommandLineImpl.java', 135)]

- SBFL   ranked 1395 statement(s)
- Hybrid ranked 338 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | ArgumentImpl.java:245 | 0.333333 | `throw new OptionException(option, ResourceConstants.ARGUMENT_UNEXPECTED_VALUE,` |
| 1 | 5 | GroupImpl.java:142 | 0.333333 | `return true;` |
| 1 | 5 | SourceDestArgument.java:123 | 0.333333 | `commandLine.addValue(source, i.next());` |
| 1 | 5 | SourceDestArgument.java:127 | 0.333333 | `commandLine.addValue(dest, i.next());` |
| 1 | 5 | SourceDestArgument.java:136 | 0.333333 | `return source.canProcess(commandLine, arg) || dest.canProcess(commandLine, arg);` |
| 6 | 7 | SourceDestArgument.java:115 | 0.288675 | `final List values = commandLine.getValues(option);` |
| 6 | 7 | SourceDestArgument.java:117 | 0.288675 | `final int limit = values.size() - dest.getMinimum();` |
| 6 | 7 | SourceDestArgument.java:118 | 0.288675 | `int count = 0;` |
| 6 | 7 | SourceDestArgument.java:120 | 0.288675 | `final Iterator i = values.iterator();` |
| 6 | 7 | SourceDestArgument.java:122 | 0.288675 | `while (count++ < limit) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 22 | ArgumentBuilder.java:94 | 1.0 | `reset();` |
| 1 | 22 | ArgumentBuilder.java:160 | 1.0 | `this.minimum = newMinimum;` |
| 1 | 22 | ArgumentBuilder.java:161 | 1.0 | `return this;` |
| 1 | 22 | ArgumentBuilder.java:174 | 1.0 | `this.maximum = newMaximum;` |
| 1 | 22 | ArgumentBuilder.java:175 | 1.0 | `return this;` |
| 1 | 22 | ArgumentImpl.java:232 | 1.0 | `validate(commandLine, this);` |
| 1 | 22 | ArgumentImpl.java:245 | 1.0 | `throw new OptionException(option, ResourceConstants.ARGUMENT_UNEXPECTED_VALUE,` |
| 1 | 22 | ArgumentImpl.java:272 | 1.0 | `final int max = (maximum == Integer.MAX_VALUE) ? 2 : maximum;` |
| 1 | 22 | ArgumentImpl.java:274 | 1.0 | `int i = 0;` |
| 1 | 22 | ArgumentImpl.java:277 | 1.0 | `while (i < max) {` |

