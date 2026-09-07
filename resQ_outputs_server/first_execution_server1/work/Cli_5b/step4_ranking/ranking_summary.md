# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Util.java', 36)]

Ground_Truth_Answerable: True

- SBFL   ranked 589 statement(s)
- Hybrid ranked 106 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 27 | HelpFormatter.java:257 | 0.5 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 27 | HelpFormatter.java:344 | 0.5 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 27 | HelpFormatter.java:346 | 0.5 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 27 | HelpFormatter.java:348 | 0.5 | `pw.flush();` |
| 1 | 27 | HelpFormatter.java:407 | 0.5 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 27 | HelpFormatter.java:572 | 0.5 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 27 | HelpFormatter.java:574 | 0.5 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 27 | HelpFormatter.java:665 | 0.5 | `option = (Option) i.next();` |
| 1 | 27 | HelpFormatter.java:666 | 0.5 | `optBuf = new StringBuffer(8);` |
| 1 | 27 | HelpFormatter.java:668 | 0.5 | `if (option.getOpt() == null)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | PosixParser.java:31 | 0.223607 | `public class PosixParser extends Parser {` |
| 1 | 2 | PosixParser.java:34 | 0.223607 | `private ArrayList tokens = new ArrayList();` |
| 3 | 6 | CommandLine.java:44 | 0.204124 | `private List args = new LinkedList();` |
| 3 | 6 | CommandLine.java:47 | 0.204124 | `private Set options = new HashSet();` |
| 3 | 6 | Parser.java:33 | 0.204124 | `public abstract class Parser implements CommandLineParser {` |
| 3 | 6 | Parser.java:71 | 0.204124 | `return parse(options, arguments, null, false);` |
| 3 | 6 | Parser.java:144 | 0.204124 | `cmd = new CommandLine();` |
| 3 | 6 | Parser.java:227 | 0.204124 | `return cmd;` |
| 9 | 98 | CommandLine.java:68 | 0.0 | `return options.contains( resolveOption(opt));` |
| 9 | 98 | CommandLine.java:167 | 0.0 | `for ( Iterator it = options.iterator(); it.hasNext(); )` |

