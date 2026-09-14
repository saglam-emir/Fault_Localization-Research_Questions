# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 135), ('TarUtils.java', 137)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TarUtils.java', 137, '->', 135)]

Ground_Truth_Answerable: True

- SBFL   ranked 2661 statement(s)
- Hybrid ranked 57 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | TarArchiveInputStream.java:240 | 0.408248 | `} catch (IllegalArgumentException e) {` |
| 1 | 4 | TarArchiveInputStream.java:241 | 0.408248 | `IOException ioe = new IOException("Error detected parsing the header");` |
| 1 | 4 | TarArchiveInputStream.java:242 | 0.408248 | `ioe.initCause(e);` |
| 1 | 4 | TarArchiveInputStream.java:243 | 0.408248 | `throw ioe;` |
| 5 | 8 | TarBuffer.java:241 | 0.333333 | `if (offset == 0) {` |
| 5 | 8 | TarBuffer.java:253 | 0.333333 | `Arrays.fill(blockBuffer, offset, offset + bytesNeeded, (byte) 0);` |
| 5 | 8 | TarBuffer.java:255 | 0.333333 | `break;` |
| 5 | 8 | TarUtils.java:143 | 0.333333 | `throw new IllegalArgumentException(` |
| 5 | 8 | TarUtils.java:241 | 0.333333 | `String string = new String(buffer, offset, length); // TODO default charset?` |
| 5 | 8 | TarUtils.java:242 | 0.333333 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 57 | TarArchiveEntry.java:331 | 1.0 | `parseTarHeader(headerBuf, encoding);` |
| 1 | 57 | TarArchiveEntry.java:938 | 1.0 | `parseTarHeader(header, encoding, false);` |
| 1 | 57 | TarArchiveEntry.java:951 | 1.0 | `userId = (int) TarUtils.parseOctalOrBinary(header, offset, UIDLEN);` |
| 1 | 57 | TarArchiveInputStream.java:64 | 1.0 | `this(is, TarBuffer.DEFAULT_BLKSIZE, TarBuffer.DEFAULT_RCDSIZE);` |
| 1 | 57 | TarArchiveInputStream.java:105 | 1.0 | `this(is, blockSize, recordSize, null);` |
| 1 | 57 | TarArchiveInputStream.java:118 | 1.0 | `this.buffer = new TarBuffer(is, blockSize, recordSize);` |
| 1 | 57 | TarArchiveInputStream.java:120 | 1.0 | `this.hasHitEOF = false;` |
| 1 | 57 | TarArchiveInputStream.java:212 | 1.0 | `if (hasHitEOF) {` |
| 1 | 57 | TarArchiveInputStream.java:216 | 1.0 | `if (currEntry != null) {` |
| 1 | 57 | TarArchiveInputStream.java:231 | 1.0 | `byte[] headerBuf = getRecord();` |

