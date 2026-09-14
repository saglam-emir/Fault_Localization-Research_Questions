# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 135), ('TarUtils.java', 136), ('TarUtils.java', 137)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 137)]

- SBFL   ranked 3452 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarUtils.java:136 | 0.57735 | `break;` |
| 2 | 6 | TarUtils.java:107 | 0.408248 | `throw new IllegalArgumentException("Length "+length+" must be at least 2");` |
| 2 | 6 | TarUtils.java:140 | 0.408248 | `throw new IllegalArgumentException(` |
| 2 | 6 | TarUtils.java:245 | 0.408248 | `String string = new String(buffer, offset, length);` |
| 2 | 6 | TarUtils.java:247 | 0.408248 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 2 | 6 | TarUtils.java:248 | 0.408248 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 2 | 6 | TarUtils.java:249 | 0.408248 | `return s;` |
| 8 | 1 | TarUtils.java:117 | 0.235702 | `start++;` |
| 9 | 2 | ArchiveStreamFactory.java:224 | 0.166667 | `if (entryEncoding != null) {` |
| 9 | 2 | ArchiveStreamFactory.java:227 | 0.166667 | `return new TarArchiveInputStream(in);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

