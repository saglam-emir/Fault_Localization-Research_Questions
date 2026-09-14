# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CpioArchiveOutputStream.java', 336), ('TarArchiveOutputStream.java', 126), ('ZipArchiveOutputStream.java', 530), ('ChangeSetPerformer.java', 128)]

Ground_Truth_Answerable: True

- SBFL   ranked 3093 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | ZipFile.java:187 | 0.912871 | `archive.close();` |
| 1 | 8 | ZipFile.java:318 | 0.912871 | `throw new IOException("central directory is empty, can't expand"` |
| 1 | 8 | ZipFile.java:548 | 0.912871 | `archive.seek(0);` |
| 1 | 8 | ZipFile.java:549 | 0.912871 | `final byte[] start = new byte[WORD];` |
| 1 | 8 | ZipFile.java:550 | 0.912871 | `archive.readFully(start);` |
| 1 | 8 | ZipFile.java:551 | 0.912871 | `for (int i = 0; i < start.length; i++) {` |
| 1 | 8 | ZipFile.java:552 | 0.912871 | `if (start[i] != ZipArchiveOutputStream.LFH_SIG[i]) {` |
| 1 | 8 | ZipFile.java:556 | 0.912871 | `return true;` |
| 9 | 21 | ZipArchiveOutputStream.java:244 | 0.821584 | `public ZipArchiveOutputStream(File file) throws IOException {` |
| 9 | 21 | ZipArchiveOutputStream.java:245 | 0.821584 | `OutputStream o = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

