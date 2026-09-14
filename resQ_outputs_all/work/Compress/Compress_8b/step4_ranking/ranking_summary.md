# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 53), ('TarUtils.java', 58), ('TarUtils.java', 59), ('TarUtils.java', 64), ('TarUtils.java', 65), ('TarUtils.java', 66), ('TarUtils.java', 67), ('TarUtils.java', 68), ('TarUtils.java', 70), ('TarUtils.java', 76), ('TarUtils.java', 57), ('TarUtils.java', 62), ('TarUtils.java', 72), ('TarUtils.java', 74), ('TarUtils.java', 75)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TarUtils.java', 62, '->', 57), ('TarUtils.java', 72, '->', 57), ('TarUtils.java', 74, '->', 57), ('TarUtils.java', 75, '->', 57)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 67), ('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 70)]

- SBFL   ranked 1760 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | TarUtils.java:52 | 0.27735 | `long    result = 0;` |
| 1 | 6 | TarUtils.java:53 | 0.27735 | `boolean stillPadding = true;` |
| 1 | 6 | TarUtils.java:54 | 0.27735 | `int     end = offset + length;` |
| 1 | 6 | TarUtils.java:55 | 0.27735 | `int     start = offset;` |
| 1 | 6 | TarUtils.java:57 | 0.27735 | `for (int i = start; i < end; i++){` |
| 1 | 6 | TarUtils.java:86 | 0.27735 | `return result;` |
| 7 | 1754 | AbstractUnicodeExtraField.java:34 | 0.0 | `protected AbstractUnicodeExtraField() {` |
| 7 | 1754 | ArArchiveEntry.java:83 | 0.0 | `this(name, length, 0, 0, DEFAULT_MODE,` |
| 7 | 1754 | ArArchiveEntry.java:98 | 0.0 | `int mode, long lastModified) {` |
| 7 | 1754 | ArArchiveEntry.java:99 | 0.0 | `this.name = name;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

