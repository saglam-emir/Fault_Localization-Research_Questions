# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PosixParser.java', 128), ('PosixParser.java', 213), ('PosixParser.java', 214), ('PosixParser.java', 215), ('PosixParser.java', 216), ('PosixParser.java', 241)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('PosixParser.java', 214, '->', 213), ('PosixParser.java', 241, '->', 238)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/cli/PosixParser.java', 213), ('src/java/org/apache/commons/cli/PosixParser.java', 214), ('src/java/org/apache/commons/cli/PosixParser.java', 216)]

- SBFL   ranked 643 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | HelpFormatter.java:335 | 0.57735 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 12 | HelpFormatter.java:422 | 0.57735 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 12 | HelpFormatter.java:424 | 0.57735 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 12 | HelpFormatter.java:426 | 0.57735 | `pw.flush();` |
| 1 | 12 | HelpFormatter.java:485 | 0.57735 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 12 | HelpFormatter.java:654 | 0.57735 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 12 | HelpFormatter.java:656 | 0.57735 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 12 | HelpFormatter.java:769 | 0.57735 | `if (option.hasArgName())` |
| 1 | 12 | HelpFormatter.java:775 | 0.57735 | `optBuf.append(' ');` |
| 1 | 12 | Option.java:334 | 0.57735 | `return (this.argName != null && this.argName.length() > 0);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

