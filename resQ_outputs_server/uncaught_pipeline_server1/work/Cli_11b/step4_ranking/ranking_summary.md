# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 632)]

Ground_Truth_Answerable: True

- SBFL   ranked 491 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | HelpFormatter.java:335 | 0.707107 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 12 | HelpFormatter.java:422 | 0.707107 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 12 | HelpFormatter.java:424 | 0.707107 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 12 | HelpFormatter.java:426 | 0.707107 | `pw.flush();` |
| 1 | 12 | HelpFormatter.java:485 | 0.707107 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 12 | HelpFormatter.java:634 | 0.707107 | `buff.append(" <").append(option.getArgName()).append(">");` |
| 1 | 12 | HelpFormatter.java:654 | 0.707107 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 12 | HelpFormatter.java:656 | 0.707107 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 12 | HelpFormatter.java:769 | 0.707107 | `if (option.hasArgName())` |
| 1 | 12 | HelpFormatter.java:775 | 0.707107 | `optBuf.append(' ');` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

