# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EntityArrays.java', 74), ('EntityArrays.java', 75), ('EntityArrays.java', 76), ('EntityArrays.java', 77), ('EntityArrays.java', 78), ('EntityArrays.java', 79), ('EntityArrays.java', 80), ('EntityArrays.java', 81), ('EntityArrays.java', 82), ('EntityArrays.java', 83), ('EntityArrays.java', 84), ('EntityArrays.java', 85), ('EntityArrays.java', 86), ('EntityArrays.java', 87), ('EntityArrays.java', 88), ('EntityArrays.java', 89), ('EntityArrays.java', 90), ('EntityArrays.java', 91), ('EntityArrays.java', 92), ('EntityArrays.java', 93), ('EntityArrays.java', 94), ('EntityArrays.java', 95), ('EntityArrays.java', 96), ('EntityArrays.java', 97), ('EntityArrays.java', 98), ('EntityArrays.java', 99), ('EntityArrays.java', 100)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('EntityArrays.java', 74, '->', 64), ('EntityArrays.java', 75, '->', 65), ('EntityArrays.java', 76, '->', 66), ('EntityArrays.java', 77, '->', 67), ('EntityArrays.java', 78, '->', 68), ('EntityArrays.java', 79, '->', 69), ('EntityArrays.java', 80, '->', 70), ('EntityArrays.java', 81, '->', 71), ('EntityArrays.java', 82, '->', 72), ('EntityArrays.java', 83, '->', 73), ('EntityArrays.java', 84, '->', 74), ('EntityArrays.java', 85, '->', 75), ('EntityArrays.java', 86, '->', 76), ('EntityArrays.java', 87, '->', 77), ('EntityArrays.java', 88, '->', 78), ('EntityArrays.java', 89, '->', 79), ('EntityArrays.java', 90, '->', 80), ('EntityArrays.java', 91, '->', 81), ('EntityArrays.java', 92, '->', 82), ('EntityArrays.java', 93, '->', 83), ('EntityArrays.java', 94, '->', 84), ('EntityArrays.java', 95, '->', 85), ('EntityArrays.java', 96, '->', 86), ('EntityArrays.java', 97, '->', 87), ('EntityArrays.java', 98, '->', 88), ('EntityArrays.java', 99, '->', 89), ('EntityArrays.java', 100, '->', 90)]

Ground_Truth_Answerable: True

- SBFL   ranked 620 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | EntityArrays.java:30 | 0.218218 | `public static String[][] ISO8859_1_ESCAPE() { return ISO8859_1_ESCAPE.clone(); }` |
| 2 | 15 | EntityArrays.java:31 | 0.208514 | `private static final String[][] ISO8859_1_ESCAPE = {` |
| 2 | 15 | EntityArrays.java:131 | 0.208514 | `private static final String[][] ISO8859_1_UNESCAPE = invert(ISO8859_1_ESCAPE);` |
| 2 | 15 | EntityArrays.java:135 | 0.208514 | `private static final String[][] HTML40_EXTENDED_ESCAPE = {` |
| 2 | 15 | EntityArrays.java:333 | 0.208514 | `private static final String[][] HTML40_EXTENDED_UNESCAPE = invert(HTML40_EXTENDED_ESCAPE);` |
| 2 | 15 | EntityArrays.java:336 | 0.208514 | `private static final String[][] BASIC_ESCAPE = {` |
| 2 | 15 | EntityArrays.java:344 | 0.208514 | `private static final String[][] BASIC_UNESCAPE = invert(BASIC_ESCAPE);` |
| 2 | 15 | EntityArrays.java:347 | 0.208514 | `private static final String[][] APOS_ESCAPE = {` |
| 2 | 15 | EntityArrays.java:352 | 0.208514 | `private static final String[][] APOS_UNESCAPE = invert(APOS_ESCAPE);` |
| 2 | 15 | EntityArrays.java:355 | 0.208514 | `private static final String[][] JAVA_CTRL_CHARS_ESCAPE = {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

