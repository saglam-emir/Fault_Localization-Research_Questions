# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ArchiveStreamFactory.java', 297), ('ArchiveStreamFactory.java', 298), ('ArchiveStreamFactory.java', 360), ('ArchiveStreamFactory.java', 361), ('CpioArchiveInputStream.java', 97), ('CpioArchiveInputStream.java', 155), ('CpioArchiveOutputStream.java', 98), ('CpioArchiveOutputStream.java', 162), ('DumpArchiveInputStream.java', 80), ('DumpArchiveInputStream.java', 104), ('TarArchiveInputStream.java', 79), ('TarArchiveInputStream.java', 142), ('TarArchiveOutputStream.java', 90), ('TarArchiveOutputStream.java', 155), ('ZipArchiveInputStream.java', 65), ('ZipArchiveInputStream.java', 184)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ArchiveStreamFactory.java', 298, '->', 296)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/cpio/CpioArchiveInputStream.java', 97), ('src/main/java/org/apache/commons/compress/archivers/cpio/CpioArchiveOutputStream.java', 98), ('src/main/java/org/apache/commons/compress/archivers/dump/DumpArchiveInputStream.java', 80), ('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveInputStream.java', 79), ('src/main/java/org/apache/commons/compress/archivers/tar/TarArchiveOutputStream.java', 90), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java', 65)]

- SBFL   ranked 6897 statement(s)
- Hybrid ranked 173 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CpioArchiveInputStream.java:122 | 0.57735 | `this(in, BLOCK_SIZE, encoding);` |
| 2 | 15 | ArchiveStreamFactory.java:209 | 0.408248 | `if (entryEncoding != null) {` |
| 2 | 15 | ArchiveStreamFactory.java:210 | 0.408248 | `return new ArjArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:212 | 0.408248 | `return new ArjArchiveInputStream(in);` |
| 2 | 15 | ArchiveStreamFactory.java:217 | 0.408248 | `return new ZipArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:224 | 0.408248 | `return new TarArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:231 | 0.408248 | `return new JarArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:238 | 0.408248 | `return new CpioArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:245 | 0.408248 | `return new DumpArchiveInputStream(in, entryEncoding);` |
| 2 | 15 | ArchiveStreamFactory.java:285 | 0.408248 | `zip.setEncoding(entryEncoding);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 173 | ArchiveInputStream.java:40 | 0.57735 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 173 | ArchiveInputStream.java:42 | 0.57735 | `private final byte[] SINGLE = new byte[1];` |
| 1 | 173 | ArchiveInputStream.java:46 | 0.57735 | `private long bytesRead = 0;` |
| 1 | 173 | ArchiveOutputStream.java:47 | 0.57735 | `public abstract class ArchiveOutputStream extends OutputStream {` |
| 1 | 173 | ArchiveOutputStream.java:50 | 0.57735 | `private final byte[] oneByte = new byte[1];` |
| 1 | 173 | ArchiveOutputStream.java:54 | 0.57735 | `private long bytesWritten = 0;` |
| 1 | 173 | ArchiveStreamFactory.java:129 | 0.57735 | `private volatile String entryEncoding = null;` |
| 1 | 173 | ArchiveStreamFactory.java:135 | 0.57735 | `this(null);` |
| 1 | 173 | ArchiveStreamFactory.java:146 | 0.57735 | `super();` |
| 1 | 173 | ArchiveStreamFactory.java:147 | 0.57735 | `this.encoding = encoding;` |

