# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BZip2CompressorInputStream.java', 168)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/compressors/bzip2/BZip2CompressorInputStream.java', 168)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 3306 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 215 | BZip2CompressorOutputStream.java:463 | 1.0 | `endBlock();` |
| 1 | 215 | BZip2CompressorOutputStream.java:464 | 1.0 | `initBlock();` |
| 1 | 215 | BZip2CompressorOutputStream.java:465 | 1.0 | `writeRun();` |
| 1 | 215 | BZip2CompressorOutputStream.java:831 | 1.0 | `short cost0 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:832 | 1.0 | `short cost1 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:833 | 1.0 | `short cost2 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:834 | 1.0 | `short cost3 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:835 | 1.0 | `short cost4 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:836 | 1.0 | `short cost5 = 0;` |
| 1 | 215 | BZip2CompressorOutputStream.java:838 | 1.0 | `for (int i = gs; i <= ge; i++) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

