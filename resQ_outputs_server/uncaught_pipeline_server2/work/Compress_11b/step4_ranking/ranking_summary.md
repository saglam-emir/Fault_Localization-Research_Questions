# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArchiveStreamFactory.java', 240), ('ArchiveStreamFactory.java', 249)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/ArchiveStreamFactory.java', 240), ('src/main/java/org/apache/commons/compress/archivers/ArchiveStreamFactory.java', 249)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 4410 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarArchiveInputStream.java:520 | 0.57735 | `return false;` |
| 2 | 2 | ArchiveStreamFactory.java:243 | 0.408248 | `return new TarArchiveInputStream(in);` |
| 2 | 2 | TarArchiveEntry.java:916 | 0.408248 | `return 0;` |
| 4 | 5 | ArchiveStreamFactory.java:241 | 0.333333 | `TarArchiveInputStream tais = new TarArchiveInputStream(new ByteArrayInputStream(tarheader));` |
| 4 | 5 | ArchiveStreamFactory.java:242 | 0.333333 | `tais.getNextEntry();` |
| 4 | 5 | TarBuffer.java:243 | 0.333333 | `if (offset == 0) {` |
| 4 | 5 | TarBuffer.java:255 | 0.333333 | `Arrays.fill(blockBuffer, offset, offset + bytesNeeded, (byte) 0);` |
| 4 | 5 | TarBuffer.java:257 | 0.333333 | `break;` |
| 9 | 6 | ArchiveStreamFactory.java:232 | 0.258199 | `final byte[] tarheader = new byte[512];` |
| 9 | 6 | ArchiveStreamFactory.java:233 | 0.258199 | `in.mark(tarheader.length);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

