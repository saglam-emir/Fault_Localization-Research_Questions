# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultParser.java', 302), ('DefaultParser.java', 305)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/DefaultParser.java', 305)]

- SBFL   ranked 370 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | DefaultParser.java:319 | 1.0 | `int pos = token.indexOf("=");` |
| 1 | 15 | DefaultParser.java:320 | 1.0 | `String t = pos == -1 ? token : token.substring(0, pos);` |
| 1 | 15 | DefaultParser.java:322 | 1.0 | `if (!options.getMatchingOptions(t).isEmpty())` |
| 1 | 15 | DefaultParser.java:327 | 1.0 | `else if (getLongPrefix(token) != null && !token.startsWith("--"))` |
| 1 | 15 | DefaultParser.java:333 | 1.0 | `return false;` |
| 1 | 15 | DefaultParser.java:570 | 1.0 | `String t = Util.stripLeadingHyphens(token);` |
| 1 | 15 | DefaultParser.java:573 | 1.0 | `String opt = null;` |
| 1 | 15 | DefaultParser.java:574 | 1.0 | `for (i = t.length() - 2; i > 1; i--)` |
| 1 | 15 | DefaultParser.java:576 | 1.0 | `String prefix = t.substring(0, i);` |
| 1 | 15 | DefaultParser.java:577 | 1.0 | `if (options.hasLongOption(prefix))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | CommandLine.java:46 | 0.0 | `private final List<String> args = new LinkedList<String>();` |
| 1 | 7 | CommandLine.java:49 | 0.0 | `private final List<Option> options = new ArrayList<Option>();` |
| 1 | 7 | DefaultParser.java:31 | 0.0 | `public class DefaultParser implements CommandLineParser` |
| 1 | 7 | DefaultParser.java:60 | 0.0 | `return parse(options, arguments, null);` |
| 1 | 7 | DefaultParser.java:76 | 0.0 | `return parse(options, arguments, properties, false);` |
| 1 | 7 | DefaultParser.java:114 | 0.0 | `cmd = new CommandLine();` |
| 1 | 7 | DefaultParser.java:132 | 0.0 | `return cmd;` |

