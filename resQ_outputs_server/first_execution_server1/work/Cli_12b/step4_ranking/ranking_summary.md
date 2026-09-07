# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('GnuParser.java', 81), ('GnuParser.java', 84)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('GnuParser.java', 84, '->', 81)]

Ground_Truth_Answerable: True

- SBFL   ranked 471 statement(s)
- Hybrid ranked 10 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | OptionBuilder.java:104 | 0.534522 | `OptionBuilder.numberOfArgs = 1;` |
| 1 | 3 | OptionBuilder.java:106 | 0.534522 | `return instance;` |
| 1 | 3 | OptionBuilder.java:319 | 0.534522 | `return create(String.valueOf(opt));` |
| 4 | 1 | GnuParser.java:81 | 0.53033 | `if (options.hasOption(arg.substring(0, 2)))` |
| 5 | 12 | GnuParser.java:85 | 0.5 | `tokens.add(arg.substring(0, 2)); // -D` |
| 5 | 12 | GnuParser.java:86 | 0.5 | `tokens.add(arg.substring(2)); // property=value` |
| 5 | 12 | HelpFormatter.java:335 | 0.5 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 5 | 12 | HelpFormatter.java:422 | 0.5 | `PrintWriter pw = new PrintWriter(System.out);` |
| 5 | 12 | HelpFormatter.java:424 | 0.5 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 5 | 12 | HelpFormatter.java:426 | 0.5 | `pw.flush();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | GnuParser.java:31 | 0.774597 | `public class GnuParser extends Parser {` |
| 2 | 1 | Parser.java:34 | 0.654654 | `public abstract class Parser implements CommandLineParser {` |
| 3 | 1 | Parser.java:86 | 0.57735 | `return parse(options, arguments, null, false);` |
| 4 | 4 | CommandLine.java:47 | 0.471405 | `private List args = new LinkedList();` |
| 4 | 4 | CommandLine.java:50 | 0.471405 | `private Set options = new HashSet();` |
| 4 | 4 | Parser.java:158 | 0.471405 | `cmd = new CommandLine();` |
| 4 | 4 | Parser.java:241 | 0.471405 | `return cmd;` |
| 8 | 3 | Parser.java:105 | 0.0 | `return parse(options, arguments, properties, false);` |
| 8 | 3 | PosixParser.java:31 | 0.0 | `public class PosixParser extends Parser {` |
| 8 | 3 | PosixParser.java:34 | 0.0 | `private ArrayList tokens = new ArrayList();` |

