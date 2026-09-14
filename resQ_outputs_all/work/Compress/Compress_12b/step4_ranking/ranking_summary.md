# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveInputStream.java', 198)]

Ground_Truth_Answerable: True

- SBFL   ranked 4419 statement(s)
- Hybrid ranked 282 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | TarUtils.java:99 | 0.57735 | `throw new IllegalArgumentException(` |
| 1 | 5 | TarUtils.java:162 | 0.57735 | `String string = new String(buffer, offset, length);` |
| 1 | 5 | TarUtils.java:163 | 0.57735 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 1 | 5 | TarUtils.java:164 | 0.57735 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 1 | 5 | TarUtils.java:165 | 0.57735 | `return s;` |
| 6 | 1 | ArchiveStreamFactory.java:135 | 0.235702 | `return new TarArchiveInputStream(in);` |
| 7 | 1 | TarArchiveInputStream.java:395 | 0.174078 | `return getNextTarEntry();` |
| 8 | 1 | ArchiveStreamFactory.java:74 | 0.136931 | `public class ArchiveStreamFactory {` |
| 9 | 74 | TarArchiveEntry.java:313 | 0.136083 | `this();` |
| 9 | 74 | TarArchiveEntry.java:314 | 0.136083 | `parseTarHeader(headerBuf);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 24 | ArchiveInputStream.java:40 | 1.0 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 24 | ArchiveInputStream.java:42 | 1.0 | `private byte[] SINGLE = new byte[1];` |
| 1 | 24 | ArchiveInputStream.java:46 | 1.0 | `private long bytesRead = 0;` |
| 1 | 24 | ArchiveStreamFactory.java:74 | 1.0 | `public class ArchiveStreamFactory {` |
| 1 | 24 | ArchiveStreamFactory.java:128 | 1.0 | `if (AR.equalsIgnoreCase(archiverName)) {` |
| 1 | 24 | ArchiveStreamFactory.java:131 | 1.0 | `if (ZIP.equalsIgnoreCase(archiverName)) {` |
| 1 | 24 | ArchiveStreamFactory.java:134 | 1.0 | `if (TAR.equalsIgnoreCase(archiverName)) {` |
| 1 | 24 | ArchiveStreamFactory.java:135 | 1.0 | `return new TarArchiveInputStream(in);` |
| 1 | 24 | TarArchiveInputStream.java:61 | 1.0 | `this(is, TarBuffer.DEFAULT_BLKSIZE, TarBuffer.DEFAULT_RCDSIZE);` |
| 1 | 24 | TarArchiveInputStream.java:79 | 1.0 | `public TarArchiveInputStream(InputStream is, int blockSize, int recordSize) {` |

