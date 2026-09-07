# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 824), ('HelpFormatter.java', 833), ('HelpFormatter.java', 834), ('HelpFormatter.java', 835), ('HelpFormatter.java', 836)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HelpFormatter.java', 834, '->', 833), ('HelpFormatter.java', 835, '->', 833)]

Ground_Truth_Answerable: True

- SBFL   ranked 524 statement(s)
- Hybrid ranked 55 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | HelpFormatter.java:334 | 0.75 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 5 | HelpFormatter.java:477 | 0.75 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 5 | HelpFormatter.java:640 | 0.75 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 5 | HelpFormatter.java:642 | 0.75 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos, defaultSyntaxPrefix + cmdLineSyntax);` |
| 1 | 5 | HelpFormatter.java:748 | 0.75 | `if (option.hasArgName())` |
| 6 | 23 | HelpFormatter.java:471 | 0.707107 | `if (autoUsage)` |
| 6 | 23 | HelpFormatter.java:480 | 0.707107 | `if ((header != null) && (header.trim().length() > 0))` |
| 6 | 23 | HelpFormatter.java:485 | 0.707107 | `printOptions(pw, width, options, leftPad, descPad);` |
| 6 | 23 | HelpFormatter.java:660 | 0.707107 | `StringBuffer sb = new StringBuffer();` |
| 6 | 23 | HelpFormatter.java:662 | 0.707107 | `renderOptions(sb, width, options, leftPad, descPad);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 46 | HelpFormatter.java:144 | 0.5 | `this.defaultWidth = width;` |
| 1 | 46 | Option.java:56 | 0.5 | `private String argName = "arg";` |
| 1 | 46 | Option.java:68 | 0.5 | `private int numberOfArgs = UNINITIALIZED;` |
| 1 | 46 | Option.java:74 | 0.5 | `private List values = new ArrayList();` |
| 1 | 46 | Option.java:123 | 0.5 | `OptionValidator.validateOption(opt);` |
| 1 | 46 | Option.java:125 | 0.5 | `this.opt = opt;` |
| 1 | 46 | Option.java:126 | 0.5 | `this.longOpt = longOpt;` |
| 1 | 46 | Option.java:129 | 0.5 | `if (hasArg)` |
| 1 | 46 | Option.java:131 | 0.5 | `this.numberOfArgs = 1;` |
| 1 | 46 | Option.java:134 | 0.5 | `this.description = description;` |

