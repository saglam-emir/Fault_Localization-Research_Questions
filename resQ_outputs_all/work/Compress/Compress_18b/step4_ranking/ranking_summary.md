# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveOutputStream.java', 457), ('TarArchiveOutputStream.java', 459)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 457)]

- SBFL   ranked 4459 statement(s)
- Hybrid ranked 40 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | TarArchiveEntry.java:734 | 0.57735 | `return true;` |
| 1 | 2 | TarArchiveOutputStream.java:387 | 0.57735 | `throw new IOException("request to write '" + numToWrite` |
| 3 | 1 | TarArchiveOutputStream.java:304 | 0.408248 | `paxHeaders.put("path", entryName);` |
| 4 | 3 | TarArchiveEntry.java:761 | 0.333333 | `return linkFlag == LF_SYMLINK;` |
| 4 | 3 | TarArchiveEntry.java:770 | 0.333333 | `return linkFlag == LF_LINK;` |
| 4 | 3 | TarArchiveOutputStream.java:185 | 0.333333 | `addPaxHeadersForNonAsciiNames = b;` |
| 7 | 1 | TarArchiveOutputStream.java:324 | 0.235702 | `currSize = 0;` |
| 8 | 8 | NioZipEncoding.java:59 | 0.218218 | `CharsetEncoder enc = this.charset.newEncoder();` |
| 8 | 8 | NioZipEncoding.java:60 | 0.218218 | `enc.onMalformedInput(CodingErrorAction.REPORT);` |
| 8 | 8 | NioZipEncoding.java:61 | 0.218218 | `enc.onUnmappableCharacter(CodingErrorAction.REPORT);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 40 | ArchiveOutputStream.java:49 | 1.0 | `public abstract class ArchiveOutputStream extends OutputStream {` |
| 1 | 40 | ArchiveOutputStream.java:52 | 1.0 | `private final byte[] oneByte = new byte[1];` |
| 1 | 40 | ArchiveOutputStream.java:56 | 1.0 | `private long bytesWritten = 0;` |
| 1 | 40 | CountingOutputStream.java:31 | 1.0 | `private long bytesWritten = 0;` |
| 1 | 40 | CountingOutputStream.java:34 | 1.0 | `super(out);` |
| 1 | 40 | FallbackZipEncoding.java:60 | 1.0 | `public FallbackZipEncoding(String charset) {` |
| 1 | 40 | FallbackZipEncoding.java:61 | 1.0 | `this.charset = charset;` |
| 1 | 40 | TarArchiveOutputStream.java:70 | 1.0 | `private int       longFileMode = LONGFILE_ERROR;` |
| 1 | 40 | TarArchiveOutputStream.java:71 | 1.0 | `private int       bigNumberMode = BIGNUMBER_ERROR;` |
| 1 | 40 | TarArchiveOutputStream.java:73 | 1.0 | `private boolean closed = false;` |

