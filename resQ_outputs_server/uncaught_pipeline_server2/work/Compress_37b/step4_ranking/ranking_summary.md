# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveInputStream.java', 462)]

Ground_Truth_Answerable: True

- SBFL   ranked 6853 statement(s)
- Hybrid ranked 72 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarArchiveInputStream.java:472 | 0.288675 | `headers.remove(keyword);` |
| 2 | 7 | TarUtils.java:175 | 0.235702 | `return parseBinaryLong(buffer, offset, length, negative);` |
| 2 | 7 | TarUtils.java:183 | 0.235702 | `if (length >= 9) {` |
| 2 | 7 | TarUtils.java:189 | 0.235702 | `long val = 0;` |
| 2 | 7 | TarUtils.java:190 | 0.235702 | `for (int i = 1; i < length; i++) {` |
| 2 | 7 | TarUtils.java:191 | 0.235702 | `val = (val << 8) + (buffer[offset + i] & 0xff);` |
| 2 | 7 | TarUtils.java:193 | 0.235702 | `if (negative) {` |
| 2 | 7 | TarUtils.java:198 | 0.235702 | `return negative ? -val : val;` |
| 9 | 2 | TarUtils.java:173 | 0.166667 | `final boolean negative = buffer[offset] == (byte) 0xff;` |
| 9 | 2 | TarUtils.java:174 | 0.166667 | `if (length < 9) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | ArchiveInputStream.java:40 | 1.0 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 14 | ArchiveInputStream.java:42 | 1.0 | `private final byte[] SINGLE = new byte[1];` |
| 1 | 14 | ArchiveInputStream.java:46 | 1.0 | `private long bytesRead = 0;` |
| 1 | 14 | TarArchiveInputStream.java:52 | 1.0 | `private final byte[] SMALL_BUF = new byte[SMALL_BUFFER_SIZE];` |
| 1 | 14 | TarArchiveInputStream.java:82 | 1.0 | `private Map<String, String> globalPaxHeaders = new HashMap<String, String>();` |
| 1 | 14 | TarArchiveInputStream.java:89 | 1.0 | `this(is, TarConstants.DEFAULT_BLKSIZE, TarConstants.DEFAULT_RCDSIZE);` |
| 1 | 14 | TarArchiveInputStream.java:131 | 1.0 | `this(is, blockSize, recordSize, null);` |
| 1 | 14 | TarArchiveInputStream.java:143 | 1.0 | `final String encoding) {` |
| 1 | 14 | TarArchiveInputStream.java:144 | 1.0 | `this.is = is;` |
| 1 | 14 | TarArchiveInputStream.java:145 | 1.0 | `this.hasHitEOF = false;` |

