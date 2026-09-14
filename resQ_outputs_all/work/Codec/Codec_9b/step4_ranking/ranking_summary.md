# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 827)]

Ground_Truth_Answerable: True

- SBFL   ranked 361 statement(s)
- Hybrid ranked 25 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Base64.java:829 | 0.707107 | `throw new IllegalArgumentException("Input array too big, the output array would be bigger (" +` |
| 2 | 2 | Base64.java:454 | 0.229416 | `buffer[pos++] = PAD;` |
| 2 | 2 | Base64.java:455 | 0.229416 | `buffer[pos++] = PAD;` |
| 4 | 4 | Base64.java:450 | 0.223607 | `buffer[pos++] = encodeTable[(x >> 2) & MASK_6BITS];` |
| 4 | 4 | Base64.java:451 | 0.223607 | `buffer[pos++] = encodeTable[(x << 4) & MASK_6BITS];` |
| 4 | 4 | Base64.java:453 | 0.223607 | `if (encodeTable == STANDARD_ENCODE_TABLE) {` |
| 4 | 4 | Base64.java:667 | 0.223607 | `return encodeBase64(binaryData, false);` |
| 8 | 1 | Base64.java:976 | 0.188982 | `len += 4 - mod;` |
| 9 | 1 | Base64.java:982 | 0.182574 | `len += chunkSeparator.length;` |
| 10 | 2 | Base64.java:835 | 0.179605 | `Base64 b64 = isChunked ? new Base64(urlSafe) : new Base64(0, CHUNK_SEPARATOR, urlSafe);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | Base64.java:378 | 0.0 | `return buffer != null ? pos - readPos : 0;` |
| 1 | 25 | Base64.java:383 | 0.0 | `if (buffer == null) {` |
| 1 | 25 | Base64.java:384 | 0.0 | `buffer = new byte[DEFAULT_BUFFER_SIZE];` |
| 1 | 25 | Base64.java:385 | 0.0 | `pos = 0;` |
| 1 | 25 | Base64.java:386 | 0.0 | `readPos = 0;` |
| 1 | 25 | Base64.java:407 | 0.0 | `if (buffer != null) {` |
| 1 | 25 | Base64.java:408 | 0.0 | `int len = Math.min(avail(), bAvail);` |
| 1 | 25 | Base64.java:409 | 0.0 | `System.arraycopy(buffer, readPos, b, bPos, len);` |
| 1 | 25 | Base64.java:534 | 0.0 | `if (buffer == null || buffer.length - pos < decodeSize) {` |
| 1 | 25 | Base64.java:535 | 0.0 | `resizeBuffer();` |

