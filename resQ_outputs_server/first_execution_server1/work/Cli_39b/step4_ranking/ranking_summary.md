# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeHandler.java', 92), ('TypeHandler.java', 234)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/cli/TypeHandler.java', 234)]

- SBFL   ranked 474 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | PatternOptionBuilder.java:111 | 1.0 | `return PatternOptionBuilder.EXISTING_FILE_VALUE;` |
| 1 | 2 | TypeHandler.java:92 | 1.0 | `return createFile(str);` |
| 3 | 1 | TypeHandler.java:224 | 0.816497 | `return new File(str);` |
| 4 | 2 | TypeHandler.java:86 | 0.707107 | `else if (PatternOptionBuilder.FILE_VALUE == clazz)` |
| 4 | 2 | TypeHandler.java:90 | 0.707107 | `else if (PatternOptionBuilder.EXISTING_FILE_VALUE == clazz)` |
| 6 | 2 | TypeHandler.java:78 | 0.632456 | `else if (PatternOptionBuilder.DATE_VALUE == clazz)` |
| 6 | 2 | TypeHandler.java:82 | 0.632456 | `else if (PatternOptionBuilder.CLASS_VALUE == clazz)` |
| 8 | 5 | PosixParser.java:148 | 0.534522 | `processOptionToken(token, stopAtNonOption);` |
| 8 | 5 | PosixParser.java:225 | 0.534522 | `if (stopAtNonOption && !options.hasOption(token))` |
| 8 | 5 | PosixParser.java:230 | 0.534522 | `if (options.hasOption(token))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

