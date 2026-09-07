# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultParser.java', 150), ('DefaultParser.java', 152), ('DefaultParser.java', 155), ('DefaultParser.java', 156), ('Parser.java', 263), ('Parser.java', 265), ('Parser.java', 268), ('Parser.java', 269)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Parser.java', 268, '->', 263), ('Parser.java', 269, '->', 263)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/DefaultParser.java', 155), ('src/main/java/org/apache/commons/cli/DefaultParser.java', 156)]

- SBFL   ranked 654 statement(s)
- Hybrid ranked 8 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | HelpFormatter.java:366 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 3 | HelpFormatter.java:791 | 0.57735 | `optBuf.append(' ');` |
| 1 | 3 | Parser.java:286 | 0.57735 | `else if (!("yes".equalsIgnoreCase(value)` |
| 4 | 84 | HelpFormatter.java:35 | 0.408248 | `public class HelpFormatter` |
| 4 | 84 | HelpFormatter.java:74 | 0.408248 | `public int defaultWidth = DEFAULT_WIDTH;` |
| 4 | 84 | HelpFormatter.java:82 | 0.408248 | `public int defaultLeftPad = DEFAULT_LEFT_PAD;` |
| 4 | 84 | HelpFormatter.java:91 | 0.408248 | `public int defaultDescPad = DEFAULT_DESC_PAD;` |
| 4 | 84 | HelpFormatter.java:99 | 0.408248 | `public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;` |
| 4 | 84 | HelpFormatter.java:107 | 0.408248 | `public String defaultNewLine = System.getProperty("line.separator");` |
| 4 | 84 | HelpFormatter.java:115 | 0.408248 | `public String defaultOptPrefix = DEFAULT_OPT_PREFIX;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Parser.java:35 | 0.408248 | `public abstract class Parser implements CommandLineParser` |
| 1 | 3 | PosixParser.java:33 | 0.408248 | `public class PosixParser extends Parser` |
| 1 | 3 | PosixParser.java:36 | 0.408248 | `private List tokens = new ArrayList();` |
| 4 | 5 | CommandLine.java:49 | 0.0 | `private List args = new LinkedList();` |
| 4 | 5 | CommandLine.java:52 | 0.0 | `private List options = new ArrayList();` |
| 4 | 5 | Parser.java:103 | 0.0 | `return parse(options, arguments, properties, false);` |
| 4 | 5 | Parser.java:163 | 0.0 | `cmd = new CommandLine();` |
| 4 | 5 | Parser.java:244 | 0.0 | `return cmd;` |

