# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArchiveStreamFactory.java', 244), ('ArchiveStreamFactory.java', 246)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ArchiveStreamFactory.java', 246, '->', 240)]

Ground_Truth_Answerable: True

- SBFL   ranked 4415 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | TarArchiveEntry.java:1006 | 0.57735 | `name = prefix + "/" + name;` |
| 1 | 8 | TarUtils.java:178 | 0.57735 | `return parseBinaryLong(buffer, offset, length, negative);` |
| 1 | 8 | TarUtils.java:186 | 0.57735 | `if (length >= 9) {` |
| 1 | 8 | TarUtils.java:192 | 0.57735 | `long val = 0;` |
| 1 | 8 | TarUtils.java:193 | 0.57735 | `for (int i = 1; i < length; i++) {` |
| 1 | 8 | TarUtils.java:194 | 0.57735 | `val = (val << 8) + (buffer[offset + i] & 0xff);` |
| 1 | 8 | TarUtils.java:196 | 0.57735 | `if (negative) {` |
| 1 | 8 | TarUtils.java:201 | 0.57735 | `return negative ? -val : val;` |
| 9 | 7 | ArchiveStreamFactory.java:242 | 0.408248 | `TarArchiveInputStream tais = new TarArchiveInputStream(new ByteArrayInputStream(tarheader));` |
| 9 | 7 | ArchiveStreamFactory.java:244 | 0.408248 | `tais.getNextEntry();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

