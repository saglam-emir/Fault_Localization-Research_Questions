# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 419), ('Base64.java', 420), ('Base64.java', 421), ('Base64.java', 422), ('Base64.java', 423), ('Base64.java', 424), ('Base64.java', 425), ('Base64InputStream.java', 169), ('Base64InputStream.java', 170), ('Base64InputStream.java', 171)]

Ground_Truth_Answerable: True

- SBFL   ranked 375 statement(s)
- Hybrid ranked 17 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Base64.java:334 | 0.707107 | `lineLength = 0;  // disable chunk-separating` |
| 1 | 2 | Base64.java:335 | 0.707107 | `lineSeparator = CHUNK_SEPARATOR;  // this just gets ignored` |
| 3 | 3 | Base64.java:388 | 0.5 | `byte[] b = new byte[buffer.length * DEFAULT_BUFFER_RESIZE_FACTOR];` |
| 3 | 3 | Base64.java:389 | 0.5 | `System.arraycopy(buffer, 0, b, 0, buffer.length);` |
| 3 | 3 | Base64.java:390 | 0.5 | `buffer = b;` |
| 6 | 2 | Base64InputStream.java:109 | 0.447214 | `int r = read(singleByte, 0, 1);` |
| 6 | 2 | Base64InputStream.java:173 | 0.447214 | `base64.encode(buf, 0, c);` |
| 8 | 5 | Base64.java:420 | 0.408248 | `if (out != null && out.length == outAvail) {` |
| 8 | 5 | Base64.java:421 | 0.408248 | `buffer = out;` |
| 8 | 5 | Base64.java:422 | 0.408248 | `pos = outPos;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | Base64.java:91 | 1.0 | `static final byte[] CHUNK_SEPARATOR = {'\r', '\n'};` |
| 1 | 17 | Base64.java:100 | 1.0 | `private static final byte[] STANDARD_ENCODE_TABLE = {` |
| 1 | 17 | Base64.java:304 | 1.0 | `this(lineLength, lineSeparator, false);` |
| 1 | 17 | Base64.java:332 | 1.0 | `public Base64(int lineLength, byte[] lineSeparator, boolean urlSafe) {` |
| 1 | 17 | Base64.java:333 | 1.0 | `if (lineSeparator == null) {` |
| 1 | 17 | Base64.java:334 | 1.0 | `lineLength = 0;  // disable chunk-separating` |
| 1 | 17 | Base64.java:335 | 1.0 | `lineSeparator = CHUNK_SEPARATOR;  // this just gets ignored` |
| 1 | 17 | Base64.java:337 | 1.0 | `this.lineLength = lineLength > 0 ? (lineLength / 4) * 4 : 0;` |
| 1 | 17 | Base64.java:338 | 1.0 | `this.lineSeparator = new byte[lineSeparator.length];` |
| 1 | 17 | Base64.java:340 | 1.0 | `if (lineLength > 0) {` |

