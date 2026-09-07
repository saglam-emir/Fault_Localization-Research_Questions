# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 730), ('HelpFormatter.java', 900), ('HelpFormatter.java', 901), ('HelpFormatter.java', 902)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/HelpFormatter.java', 900), ('src/main/java/org/apache/commons/cli/HelpFormatter.java', 901), ('src/main/java/org/apache/commons/cli/HelpFormatter.java', 902)]

- SBFL   ranked 551 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HelpFormatter.java:513 | 0.447214 | `printUsage(pw, width, cmdLineSyntax, options);` |
| 2 | 1 | HelpFormatter.java:925 | 0.408248 | `return pos + 1;` |
| 3 | 3 | HelpFormatter.java:522 | 0.377964 | `printWrapped(pw, width, header);` |
| 3 | 3 | HelpFormatter.java:529 | 0.377964 | `printWrapped(pw, width, footer);` |
| 3 | 3 | HelpFormatter.java:715 | 0.377964 | `printWrapped(pw, width, 0, text);` |
| 6 | 1 | HelpFormatter.java:989 | 0.316228 | `--pos;` |
| 7 | 7 | HelpFormatter.java:511 | 0.288675 | `if (autoUsage)` |
| 7 | 7 | HelpFormatter.java:520 | 0.288675 | `if ((header != null) && (header.trim().length() > 0))` |
| 7 | 7 | HelpFormatter.java:525 | 0.288675 | `printOptions(pw, width, options, leftPad, descPad);` |
| 7 | 7 | HelpFormatter.java:527 | 0.288675 | `if ((footer != null) && (footer.trim().length() > 0))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

