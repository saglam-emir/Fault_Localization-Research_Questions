# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Parser.java', 290)]

Ground_Truth_Answerable: True

- SBFL   ranked 650 statement(s)
- Hybrid ranked 246 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | HelpFormatter.java:366 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 4 | HelpFormatter.java:791 | 0.57735 | `optBuf.append(' ');` |
| 1 | 4 | Parser.java:284 | 0.57735 | `else if (!("yes".equalsIgnoreCase(value)` |
| 1 | 4 | Parser.java:290 | 0.57735 | `break;` |
| 5 | 75 | HelpFormatter.java:35 | 0.408248 | `public class HelpFormatter` |
| 5 | 75 | HelpFormatter.java:74 | 0.408248 | `public int defaultWidth = DEFAULT_WIDTH;` |
| 5 | 75 | HelpFormatter.java:82 | 0.408248 | `public int defaultLeftPad = DEFAULT_LEFT_PAD;` |
| 5 | 75 | HelpFormatter.java:91 | 0.408248 | `public int defaultDescPad = DEFAULT_DESC_PAD;` |
| 5 | 75 | HelpFormatter.java:99 | 0.408248 | `public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;` |
| 5 | 75 | HelpFormatter.java:107 | 0.408248 | `public String defaultNewLine = System.getProperty("line.separator");` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Parser.java:242 | 0.707107 | `checkRequiredOptions();` |
| 2 | 2 | Parser.java:241 | 0.5 | `processProperties(properties);` |
| 2 | 2 | Parser.java:254 | 0.5 | `if (properties == null)` |
| 4 | 3 | Parser.java:54 | 0.408248 | `return options;` |
| 4 | 3 | PosixParser.java:54 | 0.408248 | `eatTheRest = false;` |
| 4 | 3 | PosixParser.java:99 | 0.408248 | `this.options = options;` |
| 7 | 16 | Option.java:159 | 0.316228 | `return longOpt;` |
| 7 | 16 | OptionBuilder.java:75 | 0.316228 | `longopt = null;` |
| 7 | 16 | OptionBuilder.java:82 | 0.316228 | `optionalArg = false;` |
| 7 | 16 | OptionBuilder.java:170 | 0.316228 | `OptionBuilder.valuesep = sep;` |

