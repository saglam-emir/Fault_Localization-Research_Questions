# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Parser.java', 298)]

Ground_Truth_Answerable: True

- SBFL   ranked 587 statement(s)
- Hybrid ranked 79 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 33 | HelpFormatter.java:257 | 0.5 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 33 | HelpFormatter.java:344 | 0.5 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 33 | HelpFormatter.java:346 | 0.5 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 33 | HelpFormatter.java:348 | 0.5 | `pw.flush();` |
| 1 | 33 | HelpFormatter.java:407 | 0.5 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 33 | HelpFormatter.java:572 | 0.5 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 33 | HelpFormatter.java:574 | 0.5 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 33 | HelpFormatter.java:665 | 0.5 | `option = (Option) i.next();` |
| 1 | 33 | HelpFormatter.java:666 | 0.5 | `optBuf = new StringBuffer(8);` |
| 1 | 33 | HelpFormatter.java:668 | 0.5 | `if (option.getOpt() == null)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 71 | CommandLine.java:44 | 1.0 | `private List args = new LinkedList();` |
| 1 | 71 | CommandLine.java:47 | 1.0 | `private Set options = new HashSet();` |
| 1 | 71 | MissingOptionException.java:36 | 1.0 | `super(message);` |
| 1 | 71 | Option.java:55 | 1.0 | `private String argName = "arg";` |
| 1 | 71 | Option.java:70 | 1.0 | `private int numberOfArgs = UNINITIALIZED;` |
| 1 | 71 | Option.java:76 | 1.0 | `private ArrayList values = new ArrayList();` |
| 1 | 71 | Option.java:93 | 1.0 | `this(opt, null, false, description);` |
| 1 | 71 | Option.java:128 | 1.0 | `OptionValidator.validateOption(opt);` |
| 1 | 71 | Option.java:130 | 1.0 | `this.opt = opt;` |
| 1 | 71 | Option.java:131 | 1.0 | `this.longOpt = longOpt;` |

