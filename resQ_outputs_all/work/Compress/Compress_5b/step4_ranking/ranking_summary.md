# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveInputStream.java', 239), ('ZipArchiveInputStream.java', 240)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java', 240)]

- SBFL   ranked 3145 statement(s)
- Hybrid ranked 45 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | ZipArchiveInputStream.java:203 | 0.333333 | `int csize = (int) current.getSize();` |
| 1 | 5 | ZipArchiveInputStream.java:204 | 0.333333 | `if (readBytesOfEntry >= csize) {` |
| 1 | 5 | ZipArchiveInputStream.java:205 | 0.333333 | `return -1;` |
| 1 | 5 | ZipArchiveInputStream.java:307 | 0.333333 | `inB = readBytesOfEntry;` |
| 1 | 5 | ZipEncodingHelper.java:240 | 0.333333 | `encoding = System.getProperty("file.encoding");` |
| 6 | 6 | ZipArchiveInputStream.java:154 | 0.235702 | `current.setCrc(ZipLong.getValue(lfh, off));` |
| 6 | 6 | ZipArchiveInputStream.java:155 | 0.235702 | `off += WORD;` |
| 6 | 6 | ZipArchiveInputStream.java:157 | 0.235702 | `current.setCompressedSize(ZipLong.getValue(lfh, off));` |
| 6 | 6 | ZipArchiveInputStream.java:158 | 0.235702 | `off += WORD;` |
| 6 | 6 | ZipArchiveInputStream.java:160 | 0.235702 | `current.setSize(ZipLong.getValue(lfh, off));` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 45 | ArchiveInputStream.java:40 | 0.0 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 45 | ArchiveInputStream.java:42 | 0.0 | `private byte[] SINGLE = new byte[1];` |
| 1 | 45 | ArchiveInputStream.java:46 | 0.0 | `private int bytesRead = 0;` |
| 1 | 45 | NioZipEncoding.java:50 | 0.0 | `public NioZipEncoding(Charset charset) {` |
| 1 | 45 | NioZipEncoding.java:51 | 0.0 | `this.charset = charset;` |
| 1 | 45 | ZipArchiveInputStream.java:61 | 0.0 | `private final Inflater inf = new Inflater(true);` |
| 1 | 45 | ZipArchiveInputStream.java:62 | 0.0 | `private final CRC32 crc = new CRC32();` |
| 1 | 45 | ZipArchiveInputStream.java:64 | 0.0 | `private final byte[] buf = new byte[ZipArchiveOutputStream.BUFFER_SIZE];` |
| 1 | 45 | ZipArchiveInputStream.java:66 | 0.0 | `private ZipArchiveEntry current = null;` |
| 1 | 45 | ZipArchiveInputStream.java:67 | 0.0 | `private boolean closed = false;` |

