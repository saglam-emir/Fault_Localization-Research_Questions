# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 129), ('TarUtils.java', 131), ('TarUtils.java', 133), ('TarUtils.java', 134), ('TarUtils.java', 135), ('TarUtils.java', 136), ('TarUtils.java', 137), ('TarUtils.java', 138)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TarUtils.java', 133, '->', 132)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 131), ('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 134)]

- SBFL   ranked 3099 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarUtils.java:132 | 0.5 | `throw new IllegalArgumentException(` |
| 2 | 4 | TarUtils.java:250 | 0.288675 | `String string = new String(buffer, offset, length);` |
| 2 | 4 | TarUtils.java:252 | 0.288675 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 2 | 4 | TarUtils.java:253 | 0.288675 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 2 | 4 | TarUtils.java:254 | 0.288675 | `return s;` |
| 6 | 2 | ArchiveStreamFactory.java:76 | 0.154713 | `public class ArchiveStreamFactory {` |
| 6 | 2 | ArchiveStreamFactory.java:117 | 0.154713 | `private String entryEncoding = null;` |
| 8 | 4 | TarUtils.java:116 | 0.076249 | `while (start < end){` |
| 8 | 4 | TarUtils.java:117 | 0.076249 | `if (buffer[start] == ' '){` |
| 8 | 4 | TarUtils.java:128 | 0.076249 | `byte trailer = buffer[end - 1];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

