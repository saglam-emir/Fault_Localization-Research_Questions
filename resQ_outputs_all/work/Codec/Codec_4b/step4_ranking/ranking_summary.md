# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 225)]

Ground_Truth_Answerable: True

- SBFL   ranked 381 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Base64.java:931 | 0.816497 | `return pArray;` |
| 2 | 1 | Base64.java:906 | 0.5 | `return encode((byte[]) pObject);` |
| 3 | 1 | Base64.java:903 | 0.408248 | `if (!(pObject instanceof byte[])) {` |
| 4 | 2 | Base64.java:485 | 0.365148 | `System.arraycopy(lineSeparator, 0, buffer, pos, lineSeparator.length);` |
| 4 | 2 | Base64.java:486 | 0.365148 | `pos += lineSeparator.length;` |
| 6 | 2 | Base64.java:469 | 0.353553 | `buffer[pos++] = PAD;` |
| 6 | 2 | Base64.java:470 | 0.353553 | `buffer[pos++] = PAD;` |
| 8 | 3 | Base64.java:465 | 0.342997 | `buffer[pos++] = encodeTable[(x >> 2) & MASK_6BITS];` |
| 8 | 3 | Base64.java:466 | 0.342997 | `buffer[pos++] = encodeTable[(x << 4) & MASK_6BITS];` |
| 8 | 3 | Base64.java:468 | 0.342997 | `if (encodeTable == STANDARD_ENCODE_TABLE) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

