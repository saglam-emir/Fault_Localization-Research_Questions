# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('IOUtils.java', 104)]

Ground_Truth_Answerable: True

- SBFL   ranked 6543 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | IOUtils.java:99 | 0.298142 | `break;` |
| 2 | 2 | IOUtils.java:97 | 0.1557 | `long skipped = input.skip(numToSkip);` |
| 2 | 2 | IOUtils.java:98 | 0.1557 | `if (skipped == 0) {` |
| 4 | 3 | IOUtils.java:95 | 0.149071 | `long available = numToSkip;` |
| 4 | 3 | IOUtils.java:96 | 0.149071 | `while (numToSkip > 0) {` |
| 4 | 3 | IOUtils.java:104 | 0.149071 | `return available - numToSkip;` |
| 7 | 2 | ArchiveStreamFactory.java:77 | 0.090867 | `public class ArchiveStreamFactory {` |
| 7 | 2 | ArchiveStreamFactory.java:123 | 0.090867 | `private String entryEncoding = null;` |
| 9 | 1 | IOUtils.java:101 | 0.083045 | `numToSkip -= skipped;` |
| 10 | 6534 | AES256SHA256Decoder.java:31 | 0.0 | `class AES256SHA256Decoder extends CoderBase {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

