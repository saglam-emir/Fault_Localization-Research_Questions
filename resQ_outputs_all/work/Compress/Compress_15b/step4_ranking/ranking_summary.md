# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveEntry.java', 669), ('ZipArchiveEntry.java', 670), ('ZipArchiveEntry.java', 671), ('ZipArchiveEntry.java', 672), ('ZipArchiveEntry.java', 673), ('ZipArchiveEntry.java', 676)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ZipArchiveEntry.java', 676, '->', 675)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java', 671), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java', 672), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java', 673)]

- SBFL   ranked 2614 statement(s)
- Hybrid ranked 19 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ZipArchiveEntry.java:670 | 1.0 | `return false;` |
| 2 | 4 | ZipArchiveEntry.java:666 | 0.57735 | `String myComment = getComment();` |
| 2 | 4 | ZipArchiveEntry.java:667 | 0.57735 | `String otherComment = other.getComment();` |
| 2 | 4 | ZipArchiveEntry.java:668 | 0.57735 | `if (myComment == null) {` |
| 2 | 4 | ZipArchiveEntry.java:669 | 0.57735 | `if (otherComment != null) {` |
| 6 | 7 | ZipArchiveEntry.java:650 | 0.5 | `if (this == obj) {` |
| 6 | 7 | ZipArchiveEntry.java:653 | 0.5 | `if (obj == null || getClass() != obj.getClass()) {` |
| 6 | 7 | ZipArchiveEntry.java:656 | 0.5 | `ZipArchiveEntry other = (ZipArchiveEntry) obj;` |
| 6 | 7 | ZipArchiveEntry.java:657 | 0.5 | `String myName = getName();` |
| 6 | 7 | ZipArchiveEntry.java:658 | 0.5 | `String otherName = other.getName();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | GeneralPurposeBit.java:52 | 1.0 | `private boolean languageEncodingFlag = false;` |
| 1 | 19 | GeneralPurposeBit.java:53 | 1.0 | `private boolean dataDescriptorFlag = false;` |
| 1 | 19 | GeneralPurposeBit.java:54 | 1.0 | `private boolean encryptionFlag = false;` |
| 1 | 19 | GeneralPurposeBit.java:55 | 1.0 | `private boolean strongEncryptionFlag = false;` |
| 1 | 19 | GeneralPurposeBit.java:57 | 1.0 | `public GeneralPurposeBit() {` |
| 1 | 19 | ZipArchiveEntry.java:69 | 1.0 | `private int method = -1;` |
| 1 | 19 | ZipArchiveEntry.java:77 | 1.0 | `private long size = SIZE_UNKNOWN;` |
| 1 | 19 | ZipArchiveEntry.java:79 | 1.0 | `private int internalAttributes = 0;` |
| 1 | 19 | ZipArchiveEntry.java:80 | 1.0 | `private int platform = PLATFORM_FAT;` |
| 1 | 19 | ZipArchiveEntry.java:81 | 1.0 | `private long externalAttributes = 0;` |

