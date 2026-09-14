# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveInputStream.java', 184)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java', 184)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 6547 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ZipArchiveInputStream.java:431 | 0.5 | `toRead = (int) (csize - current.bytesRead);` |
| 2 | 60 | X7875_NewUnix.java:123 | 0.353553 | `int uidSize = trimLeadingZeroesForceMinLength(uid.toByteArray()).length;` |
| 2 | 60 | X7875_NewUnix.java:124 | 0.353553 | `int gidSize = trimLeadingZeroesForceMinLength(gid.toByteArray()).length;` |
| 2 | 60 | X7875_NewUnix.java:127 | 0.353553 | `return new ZipShort(3 + uidSize + gidSize);` |
| 2 | 60 | X7875_NewUnix.java:147 | 0.353553 | `byte[] uidBytes = uid.toByteArray();` |
| 2 | 60 | X7875_NewUnix.java:148 | 0.353553 | `byte[] gidBytes = gid.toByteArray();` |
| 2 | 60 | X7875_NewUnix.java:153 | 0.353553 | `uidBytes = trimLeadingZeroesForceMinLength(uidBytes);` |
| 2 | 60 | X7875_NewUnix.java:154 | 0.353553 | `gidBytes = trimLeadingZeroesForceMinLength(gidBytes);` |
| 2 | 60 | X7875_NewUnix.java:161 | 0.353553 | `byte[] data = new byte[3 + uidBytes.length + gidBytes.length];` |
| 2 | 60 | X7875_NewUnix.java:164 | 0.353553 | `reverse(uidBytes);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

