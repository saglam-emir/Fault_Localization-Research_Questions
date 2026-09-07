# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 586)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Base64.java', 586, '->', 585)]

Ground_Truth_Answerable: True

- SBFL   ranked 381 statement(s)
- Hybrid ranked 23 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | Base64.java:418 | 0.408248 | `buffer = null;` |
| 1 | 9 | Base64InputStream.java:154 | 0.408248 | `base64.setInitialBuffer(b, offset, len);` |
| 1 | 9 | Base64OutputStream.java:139 | 0.408248 | `if (doEncode) {` |
| 1 | 9 | Base64OutputStream.java:142 | 0.408248 | `base64.decode(b, offset, len);` |
| 1 | 9 | Base64OutputStream.java:144 | 0.408248 | `flush(false);` |
| 1 | 9 | Base64OutputStream.java:160 | 0.408248 | `byte[] buf = new byte[avail];` |
| 1 | 9 | Base64OutputStream.java:161 | 0.408248 | `int c = base64.readResults(buf, 0, avail);` |
| 1 | 9 | Base64OutputStream.java:162 | 0.408248 | `if (c > 0) {` |
| 1 | 9 | Base64OutputStream.java:163 | 0.408248 | `out.write(buf, 0, c);` |
| 10 | 20 | Base64.java:256 | 0.316228 | `this(MIME_CHUNK_SIZE, CHUNK_SEPARATOR, urlSafe);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | Base64.java:91 | 1.0 | `static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};` |
| 1 | 11 | Base64.java:100 | 1.0 | `private static final byte[] STANDARD_ENCODE_TABLE = {` |
| 1 | 11 | Base64.java:256 | 1.0 | `this(MIME_CHUNK_SIZE, CHUNK_SEPARATOR, urlSafe);` |
| 1 | 11 | Base64.java:332 | 1.0 | `public Base64(int lineLength, byte[] lineSeparator, boolean urlSafe) {` |
| 1 | 11 | Base64.java:337 | 1.0 | `this.lineLength = lineLength > 0 ? (lineLength / 4) * 4 : 0;` |
| 1 | 11 | Base64.java:338 | 1.0 | `this.lineSeparator = new byte[lineSeparator.length];` |
| 1 | 11 | Base64.java:339 | 1.0 | `System.arraycopy(lineSeparator, 0, this.lineSeparator, 0, lineSeparator.length);` |
| 1 | 11 | Base64.java:340 | 1.0 | `if (lineLength > 0) {` |
| 1 | 11 | Base64.java:341 | 1.0 | `this.encodeSize = 4 + lineSeparator.length;` |
| 1 | 11 | Base64.java:345 | 1.0 | `this.decodeSize = this.encodeSize - 1;` |

