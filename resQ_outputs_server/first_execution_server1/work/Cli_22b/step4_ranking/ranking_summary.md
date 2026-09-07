# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PosixParser.java', 41), ('PosixParser.java', 116), ('PosixParser.java', 120), ('PosixParser.java', 146), ('PosixParser.java', 147), ('PosixParser.java', 148), ('PosixParser.java', 149), ('PosixParser.java', 152), ('PosixParser.java', 184), ('PosixParser.java', 186), ('PosixParser.java', 188), ('PosixParser.java', 211), ('PosixParser.java', 243), ('PosixParser.java', 262)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('PosixParser.java', 120, '->', 109), ('PosixParser.java', 147, '->', 146)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/PosixParser.java', 41), ('src/java/org/apache/commons/cli/PosixParser.java', 188), ('src/java/org/apache/commons/cli/PosixParser.java', 211)]

- SBFL   ranked 638 statement(s)
- Hybrid ranked 119 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | HelpFormatter.java:334 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 11 | HelpFormatter.java:416 | 0.57735 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 11 | HelpFormatter.java:418 | 0.57735 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad, defaultDescPad, footer, autoUsage);` |
| 1 | 11 | HelpFormatter.java:419 | 0.57735 | `pw.flush();` |
| 1 | 11 | HelpFormatter.java:477 | 0.57735 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 11 | HelpFormatter.java:640 | 0.57735 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 11 | HelpFormatter.java:642 | 0.57735 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos, defaultSyntaxPrefix + cmdLineSyntax);` |
| 1 | 11 | HelpFormatter.java:748 | 0.57735 | `if (option.hasArgName())` |
| 1 | 11 | HelpFormatter.java:754 | 0.57735 | `optBuf.append(' ');` |
| 1 | 11 | Option.java:329 | 0.57735 | `return argName != null && argName.length() > 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Parser.java:119 | 0.707107 | `return parse(options, arguments, null, stopAtNonOption);` |
| 2 | 2 | PosixParser.java:32 | 0.25 | `public class PosixParser extends Parser` |
| 2 | 2 | PosixParser.java:35 | 0.25 | `private List tokens = new ArrayList();` |
| 4 | 5 | CommandLine.java:48 | 0.235702 | `private List args = new LinkedList();` |
| 4 | 5 | CommandLine.java:51 | 0.235702 | `private List options = new ArrayList();` |
| 4 | 5 | Parser.java:34 | 0.235702 | `public abstract class Parser implements CommandLineParser` |
| 4 | 5 | Parser.java:152 | 0.235702 | `cmd = new CommandLine();` |
| 4 | 5 | Parser.java:233 | 0.235702 | `return cmd;` |
| 9 | 111 | CommandLine.java:69 | 0.0 | `return options.contains(resolveOption(opt));` |
| 9 | 111 | CommandLine.java:173 | 0.0 | `for (Iterator it = options.iterator(); it.hasNext();)` |

