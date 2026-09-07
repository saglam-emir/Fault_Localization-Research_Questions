# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeHandler.java', 103)]

Ground_Truth_Answerable: True

- SBFL   ranked 479 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TypeHandler.java:103 | 1.0 | `return null;` |
| 2 | 1 | TypeHandler.java:97 | 0.447214 | `else if (PatternOptionBuilder.URL_VALUE == clazz)` |
| 3 | 1 | TypeHandler.java:93 | 0.408248 | `else if (PatternOptionBuilder.FILES_VALUE == clazz)` |
| 4 | 1 | TypeHandler.java:89 | 0.316228 | `else if (PatternOptionBuilder.EXISTING_FILE_VALUE == clazz)` |
| 5 | 1 | TypeHandler.java:85 | 0.301511 | `else if (PatternOptionBuilder.FILE_VALUE == clazz)` |
| 6 | 1 | TypeHandler.java:81 | 0.267261 | `else if (PatternOptionBuilder.CLASS_VALUE == clazz)` |
| 7 | 1 | TypeHandler.java:77 | 0.258199 | `else if (PatternOptionBuilder.DATE_VALUE == clazz)` |
| 8 | 1 | TypeHandler.java:73 | 0.213201 | `else if (PatternOptionBuilder.NUMBER_VALUE == clazz)` |
| 9 | 1 | TypeHandler.java:69 | 0.196116 | `else if (PatternOptionBuilder.OBJECT_VALUE == clazz)` |
| 10 | 1 | TypeHandler.java:65 | 0.19245 | `if (PatternOptionBuilder.STRING_VALUE == clazz)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

