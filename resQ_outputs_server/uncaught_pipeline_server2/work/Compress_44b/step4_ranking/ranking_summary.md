# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ChecksumCalculatingInputStream.java', 35), ('ChecksumCalculatingInputStream.java', 36)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/utils/ChecksumCalculatingInputStream.java', 35), ('src/main/java/org/apache/commons/compress/utils/ChecksumCalculatingInputStream.java', 36)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 1257 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | FramedLZ4CompressorOutputStream.java:108 | 0.707107 | `this(blockSize, true, false, false);` |
| 1 | 7 | FramedLZ4CompressorOutputStream.java:168 | 0.707107 | `return "LZ4 Parameters with BlockSize " + blockSize + ", withContentChecksum " + withContentChecksum` |
| 1 | 7 | Parameters.java:221 | 0.707107 | `niceBackReferenceLength = Math.max(minBackReferenceLength, maxBackReferenceLength / 8);` |
| 1 | 7 | Parameters.java:222 | 0.707107 | `maxCandidates = Math.max(32, windowSize / 1024);` |
| 1 | 7 | Parameters.java:223 | 0.707107 | `lazyMatches = false;` |
| 1 | 7 | Parameters.java:224 | 0.707107 | `lazyThreshold = minBackReferenceLength;` |
| 1 | 7 | Parameters.java:225 | 0.707107 | `return this;` |
| 8 | 16 | FramedLZ4CompressorOutputStream.java:62 | 0.612372 | `public enum BlockSize {` |
| 8 | 16 | FramedLZ4CompressorOutputStream.java:64 | 0.612372 | `K64(64 * 1024, 4),` |
| 8 | 16 | FramedLZ4CompressorOutputStream.java:66 | 0.612372 | `K256(256 * 1024, 5),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

