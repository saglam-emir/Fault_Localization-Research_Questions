# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 339)]

Ground_Truth_Answerable: True

- SBFL   ranked 1407 statement(s)
- Hybrid ranked 37 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | HmacAlgorithms.java:117 | 0.676123 | `return name;` |
| 2 | 9 | HmacAlgorithms.java:37 | 0.450749 | `public enum HmacAlgorithms {` |
| 2 | 9 | HmacAlgorithms.java:45 | 0.450749 | `HMAC_MD5("HmacMD5"),` |
| 2 | 9 | HmacAlgorithms.java:53 | 0.450749 | `HMAC_SHA_1("HmacSHA1"),` |
| 2 | 9 | HmacAlgorithms.java:62 | 0.450749 | `HMAC_SHA_224("HmacSHA224"),` |
| 2 | 9 | HmacAlgorithms.java:70 | 0.450749 | `HMAC_SHA_256("HmacSHA256"),` |
| 2 | 9 | HmacAlgorithms.java:78 | 0.450749 | `HMAC_SHA_384("HmacSHA384"),` |
| 2 | 9 | HmacAlgorithms.java:86 | 0.450749 | `HMAC_SHA_512("HmacSHA512");` |
| 2 | 9 | HmacAlgorithms.java:90 | 0.450749 | `private HmacAlgorithms(final String algorithm) {` |
| 2 | 9 | HmacAlgorithms.java:91 | 0.450749 | `this.name = algorithm;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 37 | Base64.java:74 | 0.0 | `static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};` |
| 1 | 37 | Base64.java:438 | 0.0 | `final byte[] buffer = ensureBufferSize(decodeSize, context);` |
| 1 | 37 | Base64.java:439 | 0.0 | `final byte b = in[inPos++];` |
| 1 | 37 | Base64.java:448 | 0.0 | `context.modulus = (context.modulus+1) % BYTES_PER_ENCODED_BLOCK;` |
| 1 | 37 | Base64.java:450 | 0.0 | `if (context.modulus == 0) {` |
| 1 | 37 | Base64.java:451 | 0.0 | `buffer[context.pos++] = (byte) ((context.ibitWorkArea >> 16) & MASK_8BITS);` |
| 1 | 37 | Base64.java:452 | 0.0 | `buffer[context.pos++] = (byte) ((context.ibitWorkArea >> 8) & MASK_8BITS);` |
| 1 | 37 | Base64.java:453 | 0.0 | `buffer[context.pos++] = (byte) (context.ibitWorkArea & MASK_8BITS);` |
| 1 | 37 | Base64.java:467 | 0.0 | `switch (context.modulus) {` |
| 1 | 37 | Base64.java:474 | 0.0 | `buffer[context.pos++] = (byte) ((context.ibitWorkArea) & MASK_8BITS);` |

