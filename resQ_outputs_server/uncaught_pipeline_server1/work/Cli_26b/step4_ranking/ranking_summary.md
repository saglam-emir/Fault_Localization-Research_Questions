# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('OptionBuilder.java', 349), ('OptionBuilder.java', 348), ('OptionBuilder.java', 359), ('OptionBuilder.java', 361)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/OptionBuilder.java', 348), ('src/java/org/apache/commons/cli/OptionBuilder.java', 359), ('src/java/org/apache/commons/cli/OptionBuilder.java', 361)]

- SBFL   ranked 711 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HelpFormatter.java:758 | 0.707107 | `optBuf.append(' ');` |
| 2 | 1 | HelpFormatter.java:752 | 0.57735 | `if (option.hasArgName())` |
| 3 | 2 | HelpFormatter.java:624 | 0.5 | `buff.append(" <").append(option.getArgName()).append(">");` |
| 3 | 2 | Option.java:329 | 0.5 | `return argName != null && argName.length() > 0;` |
| 5 | 24 | HelpFormatter.java:475 | 0.447214 | `if (autoUsage)` |
| 5 | 24 | HelpFormatter.java:484 | 0.447214 | `if ((header != null) && (header.trim().length() > 0))` |
| 5 | 24 | HelpFormatter.java:489 | 0.447214 | `printOptions(pw, width, options, leftPad, descPad);` |
| 5 | 24 | HelpFormatter.java:491 | 0.447214 | `if ((footer != null) && (footer.trim().length() > 0))` |
| 5 | 24 | HelpFormatter.java:664 | 0.447214 | `StringBuffer sb = new StringBuffer();` |
| 5 | 24 | HelpFormatter.java:666 | 0.447214 | `renderOptions(sb, width, options, leftPad, descPad);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

