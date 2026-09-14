# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SevenZFile.java', 902)]

Ground_Truth_Answerable: True

- SBFL   ranked 5097 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SevenZFile.java:903 | 0.447214 | `throw new IllegalStateException("No current 7z entry (call getNextEntry() first).");` |
| 2 | 8 | BoundedInputStream.java:55 | 0.2 | `return -1;` |
| 2 | 8 | ChecksumVerifyingInputStream.java:53 | 0.2 | `return -1;` |
| 2 | 8 | ChecksumVerifyingInputStream.java:99 | 0.2 | `if (read() >= 0) {` |
| 2 | 8 | ChecksumVerifyingInputStream.java:100 | 0.2 | `return 1;` |
| 2 | 8 | ChecksumVerifyingInputStream.java:102 | 0.2 | `return 0;` |
| 2 | 8 | SevenZFile.java:910 | 0.2 | `final InputStream stream = deferredBlockStreams.remove(0);` |
| 2 | 8 | SevenZFile.java:911 | 0.2 | `IOUtils.skip(stream, Long.MAX_VALUE);` |
| 2 | 8 | SevenZFile.java:912 | 0.2 | `stream.close();` |
| 10 | 1 | SevenZFile.java:839 | 0.182574 | `file.setContentMethods(archive.files[currentEntryIndex - 1].getContentMethods());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

