# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 65), ('TarUtils.java', 66), ('TarUtils.java', 67), ('TarUtils.java', 68), ('TarUtils.java', 69), ('TarUtils.java', 70), ('TarUtils.java', 71), ('TarUtils.java', 72)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 70), ('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 71)]

- SBFL   ranked 2514 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | TarArchiveInputStream.java:200 | 0.408248 | `} catch (IllegalArgumentException e) {` |
| 1 | 4 | TarArchiveInputStream.java:201 | 0.408248 | `IOException ioe = new IOException("Error detected parsing the header");` |
| 1 | 4 | TarArchiveInputStream.java:202 | 0.408248 | `ioe.initCause(e);` |
| 1 | 4 | TarArchiveInputStream.java:203 | 0.408248 | `throw ioe;` |
| 5 | 5 | TarUtils.java:104 | 0.333333 | `throw new IllegalArgumentException(` |
| 5 | 5 | TarUtils.java:167 | 0.333333 | `String string = new String(buffer, offset, length);` |
| 5 | 5 | TarUtils.java:168 | 0.333333 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 5 | 5 | TarUtils.java:169 | 0.333333 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 5 | 5 | TarUtils.java:170 | 0.333333 | `return s;` |
| 10 | 1 | TarArchiveEntry.java:651 | 0.288675 | `return true;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

