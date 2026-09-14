# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PosixParser.java', 114), ('PosixParser.java', 116), ('PosixParser.java', 117), ('PosixParser.java', 121)]

Ground_Truth_Answerable: True

- SBFL   ranked 642 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | HelpFormatter.java:335 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 10 | HelpFormatter.java:422 | 0.57735 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 10 | HelpFormatter.java:424 | 0.57735 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 10 | HelpFormatter.java:426 | 0.57735 | `pw.flush();` |
| 1 | 10 | HelpFormatter.java:485 | 0.57735 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 10 | HelpFormatter.java:654 | 0.57735 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 10 | HelpFormatter.java:656 | 0.57735 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 10 | HelpFormatter.java:769 | 0.57735 | `if (option.hasArgName())` |
| 1 | 10 | HelpFormatter.java:775 | 0.57735 | `optBuf.append(' ');` |
| 1 | 10 | Option.java:334 | 0.57735 | `return (this.argName != null && this.argName.length() > 0);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

