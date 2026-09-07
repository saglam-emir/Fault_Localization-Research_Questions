# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Util.java', 65), ('Util.java', 66), ('Util.java', 67), ('Util.java', 68), ('Util.java', 70), ('Util.java', 72)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Util.java', 66, '->', 65)]

Ground_Truth_Answerable: True

- SBFL   ranked 649 statement(s)
- Hybrid ranked 12 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | HelpFormatter.java:366 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 2 | HelpFormatter.java:791 | 0.57735 | `optBuf.append(' ');` |
| 3 | 75 | HelpFormatter.java:35 | 0.408248 | `public class HelpFormatter` |
| 3 | 75 | HelpFormatter.java:74 | 0.408248 | `public int defaultWidth = DEFAULT_WIDTH;` |
| 3 | 75 | HelpFormatter.java:82 | 0.408248 | `public int defaultLeftPad = DEFAULT_LEFT_PAD;` |
| 3 | 75 | HelpFormatter.java:91 | 0.408248 | `public int defaultDescPad = DEFAULT_DESC_PAD;` |
| 3 | 75 | HelpFormatter.java:99 | 0.408248 | `public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;` |
| 3 | 75 | HelpFormatter.java:107 | 0.408248 | `public String defaultNewLine = System.getProperty("line.separator");` |
| 3 | 75 | HelpFormatter.java:115 | 0.408248 | `public String defaultOptPrefix = DEFAULT_OPT_PREFIX;` |
| 3 | 75 | HelpFormatter.java:123 | 0.408248 | `public String defaultLongOptPrefix = DEFAULT_LONG_OPT_PREFIX;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Util.java:65 | 0.5 | `if (str.startsWith("\""))` |
| 1 | 5 | Util.java:69 | 0.5 | `int length = str.length();` |
| 1 | 5 | Util.java:70 | 0.5 | `if (str.endsWith("\""))` |
| 1 | 5 | Util.java:72 | 0.5 | `str = str.substring(0, length - 1);` |
| 1 | 5 | Util.java:75 | 0.5 | `return str;` |
| 6 | 7 | Util.java:38 | 0.0 | `if (str == null)` |
| 6 | 7 | Util.java:40 | 0.0 | `return null;` |
| 6 | 7 | Util.java:42 | 0.0 | `if (str.startsWith("--"))` |
| 6 | 7 | Util.java:44 | 0.0 | `return str.substring(2, str.length());` |
| 6 | 7 | Util.java:46 | 0.0 | `else if (str.startsWith("-"))` |

