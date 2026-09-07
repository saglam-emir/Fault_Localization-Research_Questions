# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 937), ('HelpFormatter.java', 938), ('HelpFormatter.java', 939), ('HelpFormatter.java', 940), ('HelpFormatter.java', 941)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HelpFormatter.java', 938, '->', 937), ('HelpFormatter.java', 939, '->', 937)]

Ground_Truth_Answerable: True

- SBFL   ranked 553 statement(s)
- Hybrid ranked 10 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | HelpFormatter.java:936 | 1.0 | `pos = startPos + width;` |
| 1 | 3 | HelpFormatter.java:938 | 1.0 | `&& (c != '\n') && (c != '\r'))` |
| 1 | 3 | HelpFormatter.java:940 | 1.0 | `++pos;` |
| 4 | 1 | HelpFormatter.java:942 | 0.707107 | `return pos == text.length() ? -1 : pos;` |
| 5 | 4 | HelpFormatter.java:919 | 0.392232 | `pos = startPos + width;` |
| 5 | 4 | HelpFormatter.java:924 | 0.392232 | `&& (c != '\n') && (c != '\r'))` |
| 5 | 4 | HelpFormatter.java:926 | 0.392232 | `--pos;` |
| 5 | 4 | HelpFormatter.java:930 | 0.392232 | `if (pos > startPos)` |
| 9 | 2 | HelpFormatter.java:907 | 0.267261 | `if (((pos = text.indexOf('\n', startPos)) != -1 && pos <= width)` |
| 9 | 2 | HelpFormatter.java:912 | 0.267261 | `else if (startPos + width >= text.length())` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | HelpFormatter.java:36 | 1.0 | `public class HelpFormatter` |
| 1 | 10 | HelpFormatter.java:75 | 1.0 | `public int defaultWidth = DEFAULT_WIDTH;` |
| 1 | 10 | HelpFormatter.java:83 | 1.0 | `public int defaultLeftPad = DEFAULT_LEFT_PAD;` |
| 1 | 10 | HelpFormatter.java:92 | 1.0 | `public int defaultDescPad = DEFAULT_DESC_PAD;` |
| 1 | 10 | HelpFormatter.java:100 | 1.0 | `public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;` |
| 1 | 10 | HelpFormatter.java:108 | 1.0 | `public String defaultNewLine = System.getProperty("line.separator");` |
| 1 | 10 | HelpFormatter.java:116 | 1.0 | `public String defaultOptPrefix = DEFAULT_OPT_PREFIX;` |
| 1 | 10 | HelpFormatter.java:124 | 1.0 | `public String defaultLongOptPrefix = DEFAULT_LONG_OPT_PREFIX;` |
| 1 | 10 | HelpFormatter.java:127 | 1.0 | `private String longOptSeparator = DEFAULT_LONG_OPT_SEPARATOR;` |
| 1 | 10 | HelpFormatter.java:135 | 1.0 | `public String defaultArgName = DEFAULT_ARG_NAME;` |

