# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('OptionGroup.java', 22), ('OptionGroup.java', 24), ('OptionGroup.java', 37), ('Options.java', 24), ('Options.java', 61)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/OptionGroup.java', 24)]

- SBFL   ranked 826 statement(s)
- Hybrid ranked 68 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Option.java:893 | 0.5 | `return required(true);` |
| 2 | 4 | Option.java:833 | 0.353553 | `this.argName = argName;` |
| 2 | 4 | Option.java:834 | 0.353553 | `return this;` |
| 2 | 4 | OptionGroup.java:121 | 0.353553 | `this.required = required;` |
| 2 | 4 | Options.java:73 | 0.353553 | `requiredOpts.add(group);` |
| 6 | 2 | Option.java:845 | 0.316228 | `this.description = description;` |
| 6 | 2 | Option.java:846 | 0.316228 | `return this;` |
| 8 | 1 | Option.java:964 | 0.288675 | `return hasArg(true);` |
| 9 | 2 | Option.java:857 | 0.267261 | `this.longOpt = longOpt;` |
| 9 | 2 | Option.java:858 | 0.267261 | `return this;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 68 | Option.java:42 | 1.0 | `public class Option implements Cloneable, Serializable` |
| 1 | 68 | Option.java:72 | 1.0 | `private int numberOfArgs = UNINITIALIZED;` |
| 1 | 68 | Option.java:75 | 1.0 | `private Class<?> type = String.class;` |
| 1 | 68 | Option.java:78 | 1.0 | `private List<String> values = new ArrayList<String>();` |
| 1 | 68 | Option.java:90 | 1.0 | `this.argName = builder.argName;` |
| 1 | 68 | Option.java:91 | 1.0 | `this.description = builder.description;` |
| 1 | 68 | Option.java:92 | 1.0 | `this.longOpt = builder.longOpt;` |
| 1 | 68 | Option.java:93 | 1.0 | `this.numberOfArgs = builder.numberOfArgs;` |
| 1 | 68 | Option.java:94 | 1.0 | `this.opt = builder.opt;` |
| 1 | 68 | Option.java:95 | 1.0 | `this.optionalArg = builder.optionalArg;` |

