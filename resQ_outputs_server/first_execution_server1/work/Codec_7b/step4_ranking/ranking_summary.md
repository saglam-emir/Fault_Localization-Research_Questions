# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Base64.java', 670)]

Ground_Truth_Answerable: True

- SBFL   ranked 384 statement(s)
- Hybrid ranked 30 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Base64.java:670 | 0.707107 | `return StringUtils.newStringUtf8(encodeBase64(binaryData, true));` |
| 1 | 2 | Base64.java:934 | 0.707107 | `return StringUtils.newStringUtf8(encode(pArray));` |
| 3 | 1 | StringUtils.java:283 | 0.426401 | `return StringUtils.newString(bytes, CharEncoding.UTF_8);` |
| 4 | 15 | Hex.java:48 | 0.408248 | `private static final char[] DIGITS_LOWER = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};` |
| 4 | 15 | Hex.java:53 | 0.408248 | `private static final char[] DIGITS_UPPER = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};` |
| 4 | 15 | Hex.java:68 | 0.408248 | `int len = data.length;` |
| 4 | 15 | Hex.java:70 | 0.408248 | `if ((len & 0x01) != 0) {` |
| 4 | 15 | Hex.java:74 | 0.408248 | `byte[] out = new byte[len >> 1];` |
| 4 | 15 | Hex.java:77 | 0.408248 | `for (int i = 0, j = 0; j < len; i++) {` |
| 4 | 15 | Hex.java:78 | 0.408248 | `int f = toDigit(data[j], j) << 4;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | StringUtils.java:129 | 0.707107 | `return StringUtils.getBytesUnchecked(string, CharEncoding.UTF_8);` |
| 1 | 3 | StringUtils.java:152 | 0.707107 | `if (string == null) {` |
| 1 | 3 | StringUtils.java:156 | 0.707107 | `return string.getBytes(charsetName);` |
| 4 | 27 | Base64.java:378 | 0.0 | `return buffer != null ? pos - readPos : 0;` |
| 4 | 27 | Base64.java:383 | 0.0 | `if (buffer == null) {` |
| 4 | 27 | Base64.java:388 | 0.0 | `byte[] b = new byte[buffer.length * DEFAULT_BUFFER_RESIZE_FACTOR];` |
| 4 | 27 | Base64.java:389 | 0.0 | `System.arraycopy(buffer, 0, b, 0, buffer.length);` |
| 4 | 27 | Base64.java:390 | 0.0 | `buffer = b;` |
| 4 | 27 | Base64.java:407 | 0.0 | `if (buffer != null) {` |
| 4 | 27 | Base64.java:408 | 0.0 | `int len = Math.min(avail(), bAvail);` |

