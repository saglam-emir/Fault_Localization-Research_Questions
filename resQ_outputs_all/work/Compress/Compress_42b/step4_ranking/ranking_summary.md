# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UnixStat.java', 35), ('ZipArchiveEntry.java', 297)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/UnixStat.java', 35)]

- SBFL   ranked 4460 statement(s)
- Hybrid ranked 27 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ZipArchiveEntry.java:297 | 0.5 | `return (getUnixMode() & UnixStat.LINK_FLAG) == UnixStat.LINK_FLAG;` |
| 2 | 1 | ZipArchiveEntry.java:284 | 0.408248 | `return platform != PLATFORM_UNIX ? 0 :` |
| 3 | 2 | ZipFile.java:378 | 0.144338 | `final LinkedList<ZipArchiveEntry> entriesOfThatName = nameMap.get(name);` |
| 3 | 2 | ZipFile.java:379 | 0.144338 | `return entriesOfThatName != null ? entriesOfThatName.getFirst() : null;` |
| 5 | 2 | ZipFile.java:161 | 0.116248 | `this(f, ZipEncodingHelper.UTF8);` |
| 5 | 2 | ZipFile.java:200 | 0.116248 | `this(f, encoding, true);` |
| 7 | 7 | ZipFile.java:887 | 0.102062 | `if (searchedForZip64EOCD) {` |
| 7 | 7 | ZipFile.java:888 | 0.102062 | `skipBytes(ZIP64_EOCDL_LENGTH - WORD);` |
| 7 | 7 | ZipFile.java:890 | 0.102062 | `positionAtCentralDirectory32();` |
| 7 | 7 | ZipFile.java:934 | 0.102062 | `skipBytes(CFD_LOCATOR_OFFSET);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 27 | GeneralPurposeBit.java:72 | 0.0 | `private boolean languageEncodingFlag = false;` |
| 1 | 27 | GeneralPurposeBit.java:73 | 0.0 | `private boolean dataDescriptorFlag = false;` |
| 1 | 27 | GeneralPurposeBit.java:74 | 0.0 | `private boolean encryptionFlag = false;` |
| 1 | 27 | GeneralPurposeBit.java:75 | 0.0 | `private boolean strongEncryptionFlag = false;` |
| 1 | 27 | GeneralPurposeBit.java:79 | 0.0 | `public GeneralPurposeBit() {` |
| 1 | 27 | ZipArchiveEntry.java:70 | 0.0 | `private int method = ZipMethod.UNKNOWN_CODE;` |
| 1 | 27 | ZipArchiveEntry.java:78 | 0.0 | `private long size = SIZE_UNKNOWN;` |
| 1 | 27 | ZipArchiveEntry.java:80 | 0.0 | `private int internalAttributes = 0;` |
| 1 | 27 | ZipArchiveEntry.java:83 | 0.0 | `private int platform = PLATFORM_FAT;` |
| 1 | 27 | ZipArchiveEntry.java:85 | 0.0 | `private long externalAttributes = 0;` |

