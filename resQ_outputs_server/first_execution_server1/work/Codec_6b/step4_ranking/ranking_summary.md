# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64InputStream.java', 148), ('Base64InputStream.java', 164), ('Base64InputStream.java', 178)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Base64InputStream.java', 148, '->', 139)]

Ground_Truth_Answerable: True

- SBFL   ranked 188 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | Base64.java:418 | 0.5 | `buffer = null;` |
| 1 | 15 | Base64.java:439 | 0.5 | `if (out != null && out.length == outAvail) {` |
| 1 | 15 | Base64.java:440 | 0.5 | `buffer = out;` |
| 1 | 15 | Base64.java:441 | 0.5 | `pos = outPos;` |
| 1 | 15 | Base64.java:442 | 0.5 | `readPos = outPos;` |
| 1 | 15 | Base64.java:558 | 0.5 | `if (buffer == null || buffer.length - pos < decodeSize) {` |
| 1 | 15 | Base64.java:561 | 0.5 | `byte b = in[inPos++];` |
| 1 | 15 | Base64.java:562 | 0.5 | `if (b == PAD) {` |
| 1 | 15 | Base64.java:567 | 0.5 | `if (b >= 0 && b < DECODE_TABLE.length) {` |
| 1 | 15 | Base64.java:568 | 0.5 | `int result = DECODE_TABLE[b];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

