# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CommandLine.java', 19), ('CommandLine.java', 23), ('CommandLine.java', 46), ('CommandLine.java', 47), ('CommandLine.java', 51), ('CommandLine.java', 69), ('CommandLine.java', 93), ('CommandLine.java', 98), ('CommandLine.java', 149), ('CommandLine.java', 151), ('CommandLine.java', 152), ('CommandLine.java', 153), ('CommandLine.java', 154), ('CommandLine.java', 155), ('CommandLine.java', 156), ('CommandLine.java', 158), ('CommandLine.java', 169), ('CommandLine.java', 170), ('CommandLine.java', 277), ('CommandLine.java', 278), ('CommandLine.java', 279), ('CommandLine.java', 280), ('CommandLine.java', 281), ('CommandLine.java', 282), ('CommandLine.java', 283), ('CommandLine.java', 284), ('CommandLine.java', 285), ('CommandLine.java', 286), ('CommandLine.java', 287), ('CommandLine.java', 298), ('CommandLine.java', 308), ('CommandLine.java', 316)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CommandLine.java', 153, '->', 152), ('CommandLine.java', 280, '->', 279), ('CommandLine.java', 284, '->', 283)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/CommandLine.java', 19), ('src/java/org/apache/commons/cli/CommandLine.java', 23), ('src/java/org/apache/commons/cli/CommandLine.java', 155), ('src/java/org/apache/commons/cli/CommandLine.java', 169), ('src/java/org/apache/commons/cli/CommandLine.java', 170), ('src/java/org/apache/commons/cli/CommandLine.java', 281), ('src/java/org/apache/commons/cli/CommandLine.java', 282), ('src/java/org/apache/commons/cli/CommandLine.java', 283), ('src/java/org/apache/commons/cli/CommandLine.java', 284), ('src/java/org/apache/commons/cli/CommandLine.java', 286), ('src/java/org/apache/commons/cli/CommandLine.java', 308), ('src/java/org/apache/commons/cli/CommandLine.java', 316)]

- SBFL   ranked 571 statement(s)
- Hybrid ranked 121 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | HelpFormatter.java:256 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 29 | HelpFormatter.java:343 | 0.57735 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 29 | HelpFormatter.java:345 | 0.57735 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 29 | HelpFormatter.java:347 | 0.57735 | `pw.flush();` |
| 1 | 29 | HelpFormatter.java:406 | 0.57735 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 29 | HelpFormatter.java:571 | 0.57735 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 29 | HelpFormatter.java:573 | 0.57735 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 29 | HelpFormatter.java:664 | 0.57735 | `option = (Option) i.next();` |
| 1 | 29 | HelpFormatter.java:665 | 0.57735 | `optBuf = new StringBuffer(8);` |
| 1 | 29 | HelpFormatter.java:667 | 0.57735 | `if (option.getOpt() == null)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CommandLine.java:137 | 0.408248 | `return getOptionValue(String.valueOf(opt));` |
| 1 | 2 | CommandLine.java:151 | 0.408248 | `String key = opt;` |
| 3 | 119 | CommandLine.java:43 | 0.353553 | `private List args = new LinkedList();` |
| 3 | 119 | CommandLine.java:46 | 0.353553 | `private Map options = new HashMap();` |
| 3 | 119 | CommandLine.java:47 | 0.353553 | `private Map names = new HashMap();` |
| 3 | 119 | CommandLine.java:51 | 0.353553 | `private Map hashcodeMap = new HashMap();` |
| 3 | 119 | CommandLine.java:123 | 0.353553 | `String[] values = getOptionValues(opt);` |
| 3 | 119 | CommandLine.java:149 | 0.353553 | `opt = Util.stripLeadingHyphens(opt);` |
| 3 | 119 | CommandLine.java:152 | 0.353553 | `if (names.containsKey(opt))` |
| 3 | 119 | CommandLine.java:154 | 0.353553 | `key = (String) names.get(opt);` |

