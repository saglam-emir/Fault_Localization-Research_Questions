# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CpioArchiveInputStream.java', 331), ('CpioArchiveInputStream.java', 347), ('CpioArchiveInputStream.java', 361), ('CpioArchiveInputStream.java', 373), ('CpioArchiveInputStream.java', 387), ('CpioArchiveInputStream.java', 399)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/cpio/CpioArchiveInputStream.java', 361), ('src/main/java/org/apache/commons/compress/archivers/cpio/CpioArchiveInputStream.java', 373)]

- SBFL   ranked 5375 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CpioArchiveEntry.java:766 | 0.57735 | `throw new IllegalArgumentException(` |
| 2 | 4 | CpioArchiveInputStream.java:157 | 0.154303 | `ensureOpen();` |
| 2 | 4 | CpioArchiveInputStream.java:158 | 0.154303 | `while (read(this.tmpbuf, 0, this.tmpbuf.length) != -1) { // NOPMD` |
| 2 | 4 | CpioArchiveInputStream.java:162 | 0.154303 | `this.entryEOF = true;` |
| 2 | 4 | CpioArchiveInputStream.java:189 | 0.154303 | `closeEntry();` |
| 6 | 16 | CpioArchiveInputStream.java:252 | 0.149071 | `ensureOpen();` |
| 6 | 16 | CpioArchiveInputStream.java:253 | 0.149071 | `if (off < 0 || len < 0 || off > b.length - len) {` |
| 6 | 16 | CpioArchiveInputStream.java:255 | 0.149071 | `} else if (len == 0) {` |
| 6 | 16 | CpioArchiveInputStream.java:259 | 0.149071 | `if (this.entry == null || this.entryEOF) {` |
| 6 | 16 | CpioArchiveInputStream.java:262 | 0.149071 | `if (this.entryBytesRead == this.entry.getSize()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

