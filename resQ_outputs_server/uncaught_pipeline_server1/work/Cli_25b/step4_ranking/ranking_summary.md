# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 825)]

Ground_Truth_Answerable: True

- SBFL   ranked 526 statement(s)
- Hybrid ranked 92 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HelpFormatter.java:758 | 0.816497 | `optBuf.append(' ');` |
| 2 | 3 | HelpFormatter.java:624 | 0.57735 | `buff.append(" <").append(option.getArgName()).append(">");` |
| 2 | 3 | HelpFormatter.java:752 | 0.57735 | `if (option.hasArgName())` |
| 2 | 3 | HelpFormatter.java:825 | 0.57735 | `nextLineTabStop = width - 1;` |
| 5 | 24 | HelpFormatter.java:475 | 0.547723 | `if (autoUsage)` |
| 5 | 24 | HelpFormatter.java:484 | 0.547723 | `if ((header != null) && (header.trim().length() > 0))` |
| 5 | 24 | HelpFormatter.java:489 | 0.547723 | `printOptions(pw, width, options, leftPad, descPad);` |
| 5 | 24 | HelpFormatter.java:491 | 0.547723 | `if ((footer != null) && (footer.trim().length() > 0))` |
| 5 | 24 | HelpFormatter.java:664 | 0.547723 | `StringBuffer sb = new StringBuffer();` |
| 5 | 24 | HelpFormatter.java:666 | 0.547723 | `renderOptions(sb, width, options, leftPad, descPad);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 92 | HelpFormatter.java:104 | 0.0 | `public String defaultNewLine = System.getProperty("line.separator");` |
| 1 | 92 | HelpFormatter.java:135 | 0.0 | `protected Comparator optionComparator = new OptionComparator();` |
| 1 | 92 | HelpFormatter.java:234 | 0.0 | `return defaultNewLine;` |
| 1 | 92 | HelpFormatter.java:304 | 0.0 | `return optionComparator;` |
| 1 | 92 | HelpFormatter.java:716 | 0.0 | `final String lpad = createPadding(leftPad);` |
| 1 | 92 | HelpFormatter.java:717 | 0.0 | `final String dpad = createPadding(descPad);` |
| 1 | 92 | HelpFormatter.java:723 | 0.0 | `int max = 0;` |
| 1 | 92 | HelpFormatter.java:725 | 0.0 | `List prefixList = new ArrayList();` |
| 1 | 92 | HelpFormatter.java:727 | 0.0 | `List optList = options.helpOptions();` |
| 1 | 92 | HelpFormatter.java:729 | 0.0 | `Collections.sort(optList, getOptionComparator());` |

