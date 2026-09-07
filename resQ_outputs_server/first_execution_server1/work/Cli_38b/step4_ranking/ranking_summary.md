# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultParser.java', 310), ('DefaultParser.java', 312)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/DefaultParser.java', 312)]

- SBFL   ranked 383 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | DefaultParser.java:308 | 0.707107 | `int pos = token.indexOf("=");` |
| 1 | 14 | DefaultParser.java:309 | 0.707107 | `String optName = pos == -1 ? token.substring(1) : token.substring(1, pos);` |
| 1 | 14 | DefaultParser.java:310 | 0.707107 | `return options.hasShortOption(optName);` |
| 1 | 14 | DefaultParser.java:326 | 0.707107 | `int pos = token.indexOf("=");` |
| 1 | 14 | DefaultParser.java:327 | 0.707107 | `String t = pos == -1 ? token : token.substring(0, pos);` |
| 1 | 14 | DefaultParser.java:329 | 0.707107 | `if (!options.getMatchingOptions(t).isEmpty())` |
| 1 | 14 | DefaultParser.java:334 | 0.707107 | `else if (getLongPrefix(token) != null && !token.startsWith("--"))` |
| 1 | 14 | DefaultParser.java:340 | 0.707107 | `return false;` |
| 1 | 14 | DefaultParser.java:577 | 0.707107 | `String t = Util.stripLeadingHyphens(token);` |
| 1 | 14 | DefaultParser.java:580 | 0.707107 | `String opt = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | CommandLine.java:46 | 0.447214 | `private final List<String> args = new LinkedList<String>();` |
| 1 | 7 | CommandLine.java:49 | 0.447214 | `private final List<Option> options = new ArrayList<Option>();` |
| 1 | 7 | DefaultParser.java:31 | 0.447214 | `public class DefaultParser implements CommandLineParser` |
| 1 | 7 | DefaultParser.java:60 | 0.447214 | `return parse(options, arguments, null);` |
| 1 | 7 | DefaultParser.java:76 | 0.447214 | `return parse(options, arguments, properties, false);` |
| 1 | 7 | DefaultParser.java:114 | 0.447214 | `cmd = new CommandLine();` |
| 1 | 7 | DefaultParser.java:132 | 0.447214 | `return cmd;` |

