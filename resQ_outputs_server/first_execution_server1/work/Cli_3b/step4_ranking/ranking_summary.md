# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeHandler.java', 25), ('TypeHandler.java', 162)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/TypeHandler.java', 25)]

- SBFL   ranked 260 statement(s)
- Hybrid ranked 8 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 260 | CommandLine.java:43 | 1.0 | `private List args = new LinkedList();` |
| 1 | 260 | CommandLine.java:46 | 1.0 | `private Set options = new HashSet();` |
| 1 | 260 | CommandLine.java:67 | 1.0 | `return options.contains( resolveOption(opt));` |
| 1 | 260 | CommandLine.java:78 | 1.0 | `return hasOption(String.valueOf(opt));` |
| 1 | 260 | CommandLine.java:89 | 1.0 | `String res = getOptionValue(opt);` |
| 1 | 260 | CommandLine.java:91 | 1.0 | `Option option = resolveOption(opt);` |
| 1 | 260 | CommandLine.java:92 | 1.0 | `if (option == null)` |
| 1 | 260 | CommandLine.java:97 | 1.0 | `Object type = option.getType();` |
| 1 | 260 | CommandLine.java:99 | 1.0 | `return (res == null)        ? null : TypeHandler.createValue(res, type);` |
| 1 | 260 | CommandLine.java:110 | 1.0 | `return getOptionObject(String.valueOf(opt));` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | CommandLine.java:43 | 0.301511 | `private List args = new LinkedList();` |
| 1 | 8 | CommandLine.java:46 | 0.301511 | `private Set options = new HashSet();` |
| 1 | 8 | Parser.java:32 | 0.301511 | `public abstract class Parser implements CommandLineParser {` |
| 1 | 8 | Parser.java:70 | 0.301511 | `return parse(options, arguments, null, false);` |
| 1 | 8 | Parser.java:143 | 0.301511 | `cmd = new CommandLine();` |
| 1 | 8 | Parser.java:226 | 0.301511 | `return cmd;` |
| 1 | 8 | PosixParser.java:30 | 0.301511 | `public class PosixParser extends Parser {` |
| 1 | 8 | PosixParser.java:33 | 0.301511 | `private ArrayList tokens = new ArrayList();` |

