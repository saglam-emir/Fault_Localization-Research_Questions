# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Parser.java', 322), ('Parser.java', 320)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Parser.java', 320, '->', 317)]

Ground_Truth_Answerable: True

- SBFL   ranked 616 statement(s)
- Hybrid ranked 86 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | HelpFormatter.java:301 | 0.5 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 10 | HelpFormatter.java:388 | 0.5 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 10 | HelpFormatter.java:390 | 0.5 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 10 | HelpFormatter.java:392 | 0.5 | `pw.flush();` |
| 1 | 10 | HelpFormatter.java:451 | 0.5 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 10 | HelpFormatter.java:620 | 0.5 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 10 | HelpFormatter.java:622 | 0.5 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 10 | HelpFormatter.java:735 | 0.5 | `if (option.hasArgName())` |
| 1 | 10 | HelpFormatter.java:741 | 0.5 | `optBuf.append(' ');` |
| 1 | 10 | Option.java:333 | 0.5 | `return (this.argName != null && this.argName.length() > 0);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | OptionBuilder.java:71 | 1.0 | `description = null;` |
| 1 | 8 | OptionBuilder.java:72 | 1.0 | `argName = "arg";` |
| 1 | 8 | OptionBuilder.java:73 | 1.0 | `longopt = null;` |
| 1 | 8 | OptionBuilder.java:74 | 1.0 | `type = null;` |
| 1 | 8 | OptionBuilder.java:76 | 1.0 | `numberOfArgs = Option.UNINITIALIZED;` |
| 1 | 8 | OptionBuilder.java:80 | 1.0 | `optionalArg = false;` |
| 1 | 8 | OptionBuilder.java:81 | 1.0 | `valuesep = (char) 0;` |
| 1 | 8 | OptionBuilder.java:368 | 1.0 | `OptionBuilder.reset();` |
| 9 | 78 | CommandLine.java:47 | 0.707107 | `private List args = new LinkedList();` |
| 9 | 78 | CommandLine.java:50 | 0.707107 | `private Set options = new HashSet();` |

