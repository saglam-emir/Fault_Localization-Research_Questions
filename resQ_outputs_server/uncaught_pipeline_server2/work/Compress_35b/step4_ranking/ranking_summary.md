# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 594), ('TarUtils.java', 602), ('TarUtils.java', 603), ('TarUtils.java', 604), ('TarUtils.java', 605), ('TarUtils.java', 606)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarUtils.java', 606)]

- SBFL   ranked 3498 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | ArchiveStreamFactory.java:377 | 0.223607 | `TarArchiveInputStream tais = null;` |
| 1 | 6 | ArchiveStreamFactory.java:379 | 0.223607 | `tais = new TarArchiveInputStream(new ByteArrayInputStream(tarheader));` |
| 1 | 6 | ArchiveStreamFactory.java:381 | 0.223607 | `if (tais.getNextTarEntry().isCheckSumOK()) {` |
| 1 | 6 | IOUtils.java:199 | 0.223607 | `if (c != null) {` |
| 1 | 6 | IOUtils.java:201 | 0.223607 | `c.close();` |
| 1 | 6 | TarArchiveEntry.java:1129 | 0.223607 | `return 0;` |
| 7 | 3 | ArchiveStreamFactory.java:397 | 0.2 | `throw new ArchiveException("No Archiver found for the stream signature");` |
| 7 | 3 | TarArchiveInputStream.java:720 | 0.2 | `if (ArchiveUtils.matchAsciiBuffer(TarConstants.MAGIC_ANT,` |
| 7 | 3 | TarArchiveInputStream.java:728 | 0.2 | `return false;` |
| 10 | 1 | ArchiveStreamFactory.java:376 | 0.182574 | `if (signatureLength >= 512) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

