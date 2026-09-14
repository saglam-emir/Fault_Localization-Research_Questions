# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PosixParser.java', 305), ('PosixParser.java', 309)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/PosixParser.java', 309)]

- SBFL   ranked 565 statement(s)
- Hybrid ranked 8 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 27 | HelpFormatter.java:256 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 27 | HelpFormatter.java:343 | 0.57735 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 27 | HelpFormatter.java:345 | 0.57735 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 27 | HelpFormatter.java:347 | 0.57735 | `pw.flush();` |
| 1 | 27 | HelpFormatter.java:406 | 0.57735 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 27 | HelpFormatter.java:571 | 0.57735 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 27 | HelpFormatter.java:573 | 0.57735 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 27 | HelpFormatter.java:664 | 0.57735 | `option = (Option) i.next();` |
| 1 | 27 | HelpFormatter.java:665 | 0.57735 | `optBuf = new StringBuffer(8);` |
| 1 | 27 | HelpFormatter.java:667 | 0.57735 | `if (option.getOpt() == null)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Parser.java:32 | 0.316228 | `public abstract class Parser implements CommandLineParser {` |
| 1 | 3 | PosixParser.java:30 | 0.316228 | `public class PosixParser extends Parser {` |
| 1 | 3 | PosixParser.java:33 | 0.316228 | `private ArrayList tokens = new ArrayList();` |
| 4 | 5 | CommandLine.java:43 | 0.0 | `private List args = new LinkedList();` |
| 4 | 5 | CommandLine.java:46 | 0.0 | `private Set options = new HashSet();` |
| 4 | 5 | Parser.java:70 | 0.0 | `return parse(options, arguments, null, false);` |
| 4 | 5 | Parser.java:136 | 0.0 | `cmd = new CommandLine();` |
| 4 | 5 | Parser.java:219 | 0.0 | `return cmd;` |

