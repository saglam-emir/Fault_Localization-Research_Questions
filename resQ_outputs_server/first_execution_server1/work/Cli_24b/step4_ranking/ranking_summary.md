# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 825), ('HelpFormatter.java', 826)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HelpFormatter.java', 826, '->', 825)]

Ground_Truth_Answerable: True

- SBFL   ranked 526 statement(s)
- Hybrid ranked 9 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HelpFormatter.java:758 | 0.816497 | `optBuf.append(' ');` |
| 2 | 3 | HelpFormatter.java:624 | 0.57735 | `buff.append(" <").append(option.getArgName()).append(">");` |
| 2 | 3 | HelpFormatter.java:752 | 0.57735 | `if (option.hasArgName())` |
| 2 | 3 | HelpFormatter.java:825 | 0.57735 | `throw new IllegalStateException("Total width is less than the width of the argument and indent " +` |
| 5 | 21 | HelpFormatter.java:475 | 0.547723 | `if (autoUsage)` |
| 5 | 21 | HelpFormatter.java:484 | 0.547723 | `if ((header != null) && (header.trim().length() > 0))` |
| 5 | 21 | HelpFormatter.java:489 | 0.547723 | `printOptions(pw, width, options, leftPad, descPad);` |
| 5 | 21 | HelpFormatter.java:664 | 0.547723 | `StringBuffer sb = new StringBuffer();` |
| 5 | 21 | HelpFormatter.java:666 | 0.547723 | `renderOptions(sb, width, options, leftPad, descPad);` |
| 5 | 21 | HelpFormatter.java:733 | 0.547723 | `Option option = (Option) i.next();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | HelpFormatter.java:35 | 0.0 | `public class HelpFormatter` |
| 1 | 9 | HelpFormatter.java:71 | 0.0 | `public int defaultWidth = DEFAULT_WIDTH;` |
| 1 | 9 | HelpFormatter.java:79 | 0.0 | `public int defaultLeftPad = DEFAULT_LEFT_PAD;` |
| 1 | 9 | HelpFormatter.java:88 | 0.0 | `public int defaultDescPad = DEFAULT_DESC_PAD;` |
| 1 | 9 | HelpFormatter.java:96 | 0.0 | `public String defaultSyntaxPrefix = DEFAULT_SYNTAX_PREFIX;` |
| 1 | 9 | HelpFormatter.java:104 | 0.0 | `public String defaultNewLine = System.getProperty("line.separator");` |
| 1 | 9 | HelpFormatter.java:112 | 0.0 | `public String defaultOptPrefix = DEFAULT_OPT_PREFIX;` |
| 1 | 9 | HelpFormatter.java:120 | 0.0 | `public String defaultLongOptPrefix = DEFAULT_LONG_OPT_PREFIX;` |
| 1 | 9 | HelpFormatter.java:128 | 0.0 | `public String defaultArgName = DEFAULT_ARG_NAME;` |

