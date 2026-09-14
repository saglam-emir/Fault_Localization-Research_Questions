# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveInputStream.java', 415), ('ZipArchiveInputStream.java', 440), ('ZipArchiveInputStream.java', 809)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ZipArchiveInputStream.java', 415, '->', 414)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java', 440), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveInputStream.java', 809)]

- SBFL   ranked 7949 statement(s)
- Hybrid ranked 25 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Parameters.java:221 | 0.654654 | `niceBackReferenceLength = Math.max(minBackReferenceLength, maxBackReferenceLength / 8);` |
| 1 | 5 | Parameters.java:222 | 0.654654 | `maxCandidates = Math.max(32, windowSize / 1024);` |
| 1 | 5 | Parameters.java:223 | 0.654654 | `lazyMatches = false;` |
| 1 | 5 | Parameters.java:224 | 0.654654 | `lazyThreshold = minBackReferenceLength;` |
| 1 | 5 | Parameters.java:225 | 0.654654 | `return this;` |
| 6 | 2 | BlockLZ4CompressorOutputStream.java:409 | 0.612372 | `int maxLen = BlockLZ4CompressorInputStream.WINDOW_SIZE - 1;` |
| 6 | 2 | BlockLZ4CompressorOutputStream.java:410 | 0.612372 | `return Parameters.builder(BlockLZ4CompressorInputStream.WINDOW_SIZE)` |
| 8 | 2 | FramedLZ4CompressorOutputStream.java:108 | 0.5 | `this(blockSize, true, false, false);` |
| 8 | 2 | FramedLZ4CompressorOutputStream.java:168 | 0.5 | `return "LZ4 Parameters with BlockSize " + blockSize + ", withContentChecksum " + withContentChecksum` |
| 10 | 20 | FramedLZ4CompressorOutputStream.java:62 | 0.433013 | `public enum BlockSize {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | ArchiveInputStream.java:40 | 0.57735 | `public abstract class ArchiveInputStream extends InputStream {` |
| 1 | 25 | ArchiveInputStream.java:42 | 0.57735 | `private final byte[] single = new byte[1];` |
| 1 | 25 | ArchiveInputStream.java:46 | 0.57735 | `private long bytesRead = 0;` |
| 1 | 25 | ZipArchiveInputStream.java:93 | 0.57735 | `private final Inflater inf = new Inflater(true);` |
| 1 | 25 | ZipArchiveInputStream.java:96 | 0.57735 | `private final ByteBuffer buf = ByteBuffer.allocate(ZipArchiveOutputStream.BUFFER_SIZE);` |
| 1 | 25 | ZipArchiveInputStream.java:99 | 0.57735 | `private CurrentEntry current = null;` |
| 1 | 25 | ZipArchiveInputStream.java:102 | 0.57735 | `private boolean closed = false;` |
| 1 | 25 | ZipArchiveInputStream.java:105 | 0.57735 | `private boolean hitCentralDirectory = false;` |
| 1 | 25 | ZipArchiveInputStream.java:112 | 0.57735 | `private ByteArrayInputStream lastStoredEntry = null;` |
| 1 | 25 | ZipArchiveInputStream.java:115 | 0.57735 | `private boolean allowStoredEntriesWithDataDescriptor = false;` |

