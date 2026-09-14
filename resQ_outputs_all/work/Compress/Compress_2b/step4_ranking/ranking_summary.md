# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArArchiveInputStream.java', 42), ('ArArchiveInputStream.java', 46), ('ArArchiveInputStream.java', 60), ('ArArchiveInputStream.java', 62), ('ArArchiveInputStream.java', 83), ('ArArchiveInputStream.java', 84), ('ArArchiveInputStream.java', 85), ('ArArchiveInputStream.java', 77), ('ArArchiveInputStream.java', 78), ('ArArchiveInputStream.java', 114), ('ArArchiveInputStream.java', 117), ('ArArchiveInputStream.java', 132), ('ArArchiveInputStream.java', 133), ('ArArchiveInputStream.java', 134), ('ArArchiveInputStream.java', 129), ('ArArchiveInputStream.java', 143)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 42), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 46), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 60), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 62), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 84), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 85), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 77), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 78), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 117), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 132), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 133), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 134), ('src/main/java/org/apache/commons/compress/archivers/ar/ArArchiveInputStream.java', 129)]

- SBFL   ranked 2891 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ArArchiveInputStream.java:80 | 0.57735 | `return null;` |
| 2 | 37 | ArArchiveInputStream.java:63 | 0.408248 | `if (offset == 0) {` |
| 2 | 37 | ArArchiveInputStream.java:64 | 0.408248 | `final byte[] expected = ArArchiveEntry.HEADER.getBytes();` |
| 2 | 37 | ArArchiveInputStream.java:65 | 0.408248 | `final byte[] realized = new byte[expected.length];` |
| 2 | 37 | ArArchiveInputStream.java:66 | 0.408248 | `final int read = read(realized);` |
| 2 | 37 | ArArchiveInputStream.java:67 | 0.408248 | `if (read != expected.length) {` |
| 2 | 37 | ArArchiveInputStream.java:70 | 0.408248 | `for (int i = 0; i < expected.length; i++) {` |
| 2 | 37 | ArArchiveInputStream.java:71 | 0.408248 | `if (expected[i] != realized[i]) {` |
| 2 | 37 | ArArchiveInputStream.java:79 | 0.408248 | `if (input.available() == 0) {` |
| 2 | 37 | ArArchiveInputStream.java:83 | 0.408248 | `if (offset % 2 != 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

