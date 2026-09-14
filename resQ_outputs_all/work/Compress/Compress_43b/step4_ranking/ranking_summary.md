# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveOutputStream.java', 1034), ('ZipArchiveOutputStream.java', 1075), ('ZipArchiveOutputStream.java', 1171), ('ZipArchiveOutputStream.java', 1492), ('ZipArchiveOutputStream.java', 1493)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveOutputStream.java', 1075), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveOutputStream.java', 1171), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveOutputStream.java', 1492), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveOutputStream.java', 1493)]

- SBFL   ranked 7993 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Parameters.java:221 | 0.654654 | `niceBackReferenceLength = Math.max(minBackReferenceLength, maxBackReferenceLength / 8);` |
| 1 | 5 | Parameters.java:222 | 0.654654 | `maxCandidates = Math.max(32, windowSize / 1024);` |
| 1 | 5 | Parameters.java:223 | 0.654654 | `lazyMatches = false;` |
| 1 | 5 | Parameters.java:224 | 0.654654 | `lazyThreshold = minBackReferenceLength;` |
| 1 | 5 | Parameters.java:225 | 0.654654 | `return this;` |
| 6 | 2 | BlockLZ4CompressorOutputStream.java:406 | 0.612372 | `int maxLen = BlockLZ4CompressorInputStream.WINDOW_SIZE - 1;` |
| 6 | 2 | BlockLZ4CompressorOutputStream.java:407 | 0.612372 | `return Parameters.builder(BlockLZ4CompressorInputStream.WINDOW_SIZE)` |
| 8 | 2 | FramedLZ4CompressorOutputStream.java:108 | 0.5 | `this(blockSize, true, false, false);` |
| 8 | 2 | FramedLZ4CompressorOutputStream.java:168 | 0.5 | `return "LZ4 Parameters with BlockSize " + blockSize + ", withContentChecksum " + withContentChecksum` |
| 10 | 20 | FramedLZ4CompressorOutputStream.java:62 | 0.433013 | `public enum BlockSize {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

