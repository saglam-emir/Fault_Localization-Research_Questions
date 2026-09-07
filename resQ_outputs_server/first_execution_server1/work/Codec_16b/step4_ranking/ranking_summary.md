# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base32.java', 99)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Base32.java', 99, '->', 94)]

Ground_Truth_Answerable: True

- SBFL   ranked 282 statement(s)
- Hybrid ranked 1 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Base32.java:309 | 0.447214 | `throw new IllegalArgumentException("pad must not be in alphabet or whitespace");` |
| 2 | 1 | Base32.java:193 | 0.316228 | `this(0, null, useHex, pad);` |
| 3 | 2 | Base32.java:284 | 0.258199 | `this.encodeTable = HEX_ENCODE_TABLE;` |
| 3 | 2 | Base32.java:285 | 0.258199 | `this.decodeTable = HEX_DECODE_TABLE;` |
| 5 | 2 | Base32.java:303 | 0.089443 | `this.encodeSize = BYTES_PER_ENCODED_BLOCK;` |
| 5 | 2 | Base32.java:304 | 0.089443 | `this.lineSeparator = null;` |
| 7 | 19 | Base32.java:60 | 0.080322 | `private static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};` |
| 7 | 19 | Base32.java:67 | 0.080322 | `private static final byte[] DECODE_TABLE = {` |
| 7 | 19 | Base32.java:81 | 0.080322 | `private static final byte[] ENCODE_TABLE = {` |
| 7 | 19 | Base32.java:92 | 0.080322 | `private static final byte[] HEX_DECODE_TABLE = {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Charsets.java:155 | 0.0 | `public static final Charset UTF_8 = Charset.forName(CharEncoding.UTF_8);` |

