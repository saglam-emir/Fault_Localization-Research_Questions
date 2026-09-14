# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveOutputStream.java', 108), ('TarArchiveOutputStream.java', 109), ('TarArchiveOutputStream.java', 330)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 108), ('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 109)]

- SBFL   ranked 4097 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarArchiveEntry.java:260 | 0.333333 | `this(file, normalizeFileName(file.getPath(), false));` |
| 2 | 4 | TarArchiveEntry.java:289 | 0.258199 | `this.mode = DEFAULT_FILE_MODE;` |
| 2 | 4 | TarArchiveEntry.java:290 | 0.258199 | `this.linkFlag = LF_NORMAL;` |
| 2 | 4 | TarArchiveEntry.java:291 | 0.258199 | `this.size = file.length();` |
| 2 | 4 | TarArchiveEntry.java:292 | 0.258199 | `this.name = fileName;` |
| 6 | 1 | TarArchiveEntry.java:642 | 0.235702 | `return file.isDirectory();` |
| 7 | 7 | TarArchiveEntry.java:271 | 0.218218 | `this();` |
| 7 | 7 | TarArchiveEntry.java:273 | 0.218218 | `this.file = file;` |
| 7 | 7 | TarArchiveEntry.java:275 | 0.218218 | `this.linkName = "";` |
| 7 | 7 | TarArchiveEntry.java:277 | 0.218218 | `if (file.isDirectory()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

