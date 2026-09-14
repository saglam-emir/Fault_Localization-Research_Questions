# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarArchiveInputStream.java', 501), ('TarArchiveInputStream.java', 505)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveInputStream.java', 505)]

- SBFL   ranked 6738 statement(s)
- Hybrid ranked 187 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TarArchiveInputStream.java:501 | 0.408248 | `currEntry.setGroupId(Integer.parseInt(val));` |
| 2 | 11 | TarArchiveEntry.java:949 | 0.235702 | `return TarUtils.formatLongOctalBytes(0, outbuf, offset, length);` |
| 2 | 11 | TarArchiveOutputStream.java:288 | 0.235702 | `addPaxHeadersForBigNumbers(paxHeaders, entry);` |
| 2 | 11 | TarArchiveOutputStream.java:585 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "size", entry.getSize(),` |
| 2 | 11 | TarArchiveOutputStream.java:587 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "gid", entry.getLongGroupId(),` |
| 2 | 11 | TarArchiveOutputStream.java:589 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "mtime",` |
| 2 | 11 | TarArchiveOutputStream.java:592 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "uid", entry.getLongUserId(),` |
| 2 | 11 | TarArchiveOutputStream.java:595 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "SCHILY.devmajor",` |
| 2 | 11 | TarArchiveOutputStream.java:597 | 0.235702 | `addPaxHeaderForBigNumber(paxHeaders, "SCHILY.devminor",` |
| 2 | 11 | TarArchiveOutputStream.java:600 | 0.235702 | `failForBigNumber("mode", entry.getMode(), TarConstants.MAXID);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | ArchiveInputStream.java:40 | 0.27735 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 23 | ArchiveInputStream.java:42 | 0.27735 | `private final byte[] SINGLE = new byte[1];` |
| 1 | 23 | ArchiveInputStream.java:46 | 0.27735 | `private long bytesRead = 0;` |
| 1 | 23 | Charsets.java:159 | 0.27735 | `public static final Charset UTF_8 = Charset.forName(CharsetNames.UTF_8);` |
| 1 | 23 | FallbackZipEncoding.java:60 | 0.27735 | `public FallbackZipEncoding(String charsetName) {` |
| 1 | 23 | FallbackZipEncoding.java:61 | 0.27735 | `this.charsetName = charsetName;` |
| 1 | 23 | TarArchiveInputStream.java:52 | 0.27735 | `private final byte[] SMALL_BUF = new byte[SMALL_BUFFER_SIZE];` |
| 1 | 23 | TarArchiveInputStream.java:86 | 0.27735 | `this(is, TarConstants.DEFAULT_BLKSIZE, TarConstants.DEFAULT_RCDSIZE);` |
| 1 | 23 | TarArchiveInputStream.java:128 | 0.27735 | `this(is, blockSize, recordSize, null);` |
| 1 | 23 | TarArchiveInputStream.java:140 | 0.27735 | `String encoding) {` |

