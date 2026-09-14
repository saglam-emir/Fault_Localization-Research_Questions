# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveEntry.java', 859)]

Ground_Truth_Answerable: True

- SBFL   ranked 3488 statement(s)
- Hybrid ranked 15 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarArchiveEntry.java:860 | 0.447214 | `return true;` |
| 2 | 7 | TarArchiveInputStream.java:285 | 0.258199 | `} catch (final IllegalArgumentException e) {` |
| 2 | 7 | TarArchiveInputStream.java:286 | 0.258199 | `throw new IOException("Error detected parsing the header", e);` |
| 2 | 7 | TarUtils.java:140 | 0.258199 | `throw new IllegalArgumentException(` |
| 2 | 7 | TarUtils.java:245 | 0.258199 | `String string = new String(buffer, offset, length);` |
| 2 | 7 | TarUtils.java:247 | 0.258199 | `string=string.replaceAll("\0", "{NUL}"); // Replace NULs to allow string to be printed` |
| 2 | 7 | TarUtils.java:248 | 0.258199 | `final String s = "Invalid byte "+currentByte+" at offset "+(current-offset)+" in '"+string+"' len="+length;` |
| 2 | 7 | TarUtils.java:249 | 0.258199 | `return s;` |
| 9 | 8 | TarArchiveInputStream.java:213 | 0.223607 | `return 0;` |
| 9 | 8 | TarUtils.java:175 | 0.223607 | `return parseBinaryLong(buffer, offset, length, negative);` |

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

