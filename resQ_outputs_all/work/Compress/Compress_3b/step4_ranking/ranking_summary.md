# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveOutputStream.java', 55), ('TarArchiveOutputStream.java', 112), ('TarArchiveOutputStream.java', 187), ('TarArchiveOutputStream.java', 217)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 55), ('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 187), ('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 217)]

- SBFL   ranked 3081 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | ArArchiveOutputStream.java:169 | 0.57735 | `if(haveUnclosedEntry) {` |
| 1 | 4 | ArArchiveOutputStream.java:170 | 0.57735 | `throw new IOException("This archives contains unclosed entries.");` |
| 1 | 4 | CpioArchiveOutputStream.java:318 | 0.57735 | `throw new IOException("This archives contains unclosed entries.");` |
| 1 | 4 | ZipArchiveOutputStream.java:336 | 0.57735 | `throw new IOException("This archives contains unclosed entries.");` |
| 5 | 3 | CpioArchiveEntry.java:235 | 0.333333 | `this(FORMAT_NEW);` |
| 5 | 3 | CpioArchiveEntry.java:236 | 0.333333 | `this.name = name;` |
| 5 | 3 | JarArchiveEntry.java:44 | 0.333333 | `super(name);` |
| 8 | 1 | JarArchiveEntry.java:80 | 0.288675 | `return super.hashCode();` |
| 9 | 10 | JarArchiveOutputStream.java:46 | 0.235702 | `if (!jarMarkerAdded) {` |
| 9 | 10 | JarArchiveOutputStream.java:47 | 0.235702 | `((ZipArchiveEntry)ze).addAsFirstExtraField(JarMarker.getInstance());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

