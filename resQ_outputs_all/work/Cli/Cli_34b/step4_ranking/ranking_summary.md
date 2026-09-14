# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Option.java', 72), ('OptionBuilder.java', 84)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/Option.java', 72)]

- SBFL   ranked 793 statement(s)
- Hybrid ranked 226 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 52 | DefaultParser.java:33 | 0.57735 | `public class DefaultParser implements CommandLineParser` |
| 1 | 52 | DefaultParser.java:59 | 0.57735 | `return parse(options, arguments, null);` |
| 1 | 52 | DefaultParser.java:75 | 0.57735 | `return parse(options, arguments, properties, false);` |
| 1 | 52 | DefaultParser.java:100 | 0.57735 | `this.options = options;` |
| 1 | 52 | DefaultParser.java:101 | 0.57735 | `this.stopAtNonOption = stopAtNonOption;` |
| 1 | 52 | DefaultParser.java:102 | 0.57735 | `skipParsing = false;` |
| 1 | 52 | DefaultParser.java:103 | 0.57735 | `currentOption = null;` |
| 1 | 52 | DefaultParser.java:104 | 0.57735 | `expectedOpts = new ArrayList(options.getRequiredOptions());` |
| 1 | 52 | DefaultParser.java:107 | 0.57735 | `for (Iterator it = options.getOptionGroups().iterator(); it.hasNext();)` |
| 1 | 52 | DefaultParser.java:113 | 0.57735 | `cmd = new CommandLine();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DefaultParser.java:33 | 0.5 | `public class DefaultParser implements CommandLineParser` |
| 1 | 5 | DefaultParser.java:59 | 0.5 | `return parse(options, arguments, null);` |
| 1 | 5 | DefaultParser.java:75 | 0.5 | `return parse(options, arguments, properties, false);` |
| 1 | 5 | DefaultParser.java:113 | 0.5 | `cmd = new CommandLine();` |
| 1 | 5 | DefaultParser.java:131 | 0.5 | `return cmd;` |
| 6 | 1 | OptionBuilder.java:111 | 0.353553 | `OptionBuilder.numberOfArgs = 1;` |
| 7 | 3 | OptionBuilder.java:84 | 0.267261 | `type = null;` |
| 7 | 3 | OptionBuilder.java:85 | 0.267261 | `required = false;` |
| 7 | 3 | OptionBuilder.java:371 | 0.267261 | `OptionBuilder.reset();` |
| 10 | 2 | OptionBuilder.java:87 | 0.176777 | `optionalArg = false;` |

