# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveEntry.java', 64), ('ZipArchiveEntry.java', 462), ('ZipArchiveEntry.java', 463), ('ZipArchiveEntry.java', 466)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java', 64), ('src/main/java/org/apache/commons/compress/archivers/zip/ZipArchiveEntry.java', 466)]

- SBFL   ranked 2002 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | ZipArchiveEntry.java:455 | 0.57735 | `if (this == obj) {` |
| 1 | 6 | ZipArchiveEntry.java:458 | 0.57735 | `if (obj == null || getClass() != obj.getClass()) {` |
| 1 | 6 | ZipArchiveEntry.java:461 | 0.57735 | `ZipArchiveEntry other = (ZipArchiveEntry) obj;` |
| 1 | 6 | ZipArchiveEntry.java:462 | 0.57735 | `if (name == null) {` |
| 1 | 6 | ZipArchiveEntry.java:463 | 0.57735 | `if (other.name != null) {` |
| 1 | 6 | ZipArchiveEntry.java:469 | 0.57735 | `return true;` |
| 7 | 7 | ZipArchiveEntry.java:50 | 0.136083 | `private int method = -1;` |
| 7 | 7 | ZipArchiveEntry.java:52 | 0.136083 | `private int internalAttributes = 0;` |
| 7 | 7 | ZipArchiveEntry.java:53 | 0.136083 | `private int platform = PLATFORM_FAT;` |
| 7 | 7 | ZipArchiveEntry.java:54 | 0.136083 | `private long externalAttributes = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ZipArchiveEntry.java:50 | 1.0 | `private int method = -1;` |
| 1 | 7 | ZipArchiveEntry.java:52 | 1.0 | `private int internalAttributes = 0;` |
| 1 | 7 | ZipArchiveEntry.java:53 | 1.0 | `private int platform = PLATFORM_FAT;` |
| 1 | 7 | ZipArchiveEntry.java:54 | 1.0 | `private long externalAttributes = 0;` |
| 1 | 7 | ZipArchiveEntry.java:55 | 1.0 | `private LinkedHashMap/*<ZipShort, ZipExtraField>*/ extraFields = null;` |
| 1 | 7 | ZipArchiveEntry.java:56 | 1.0 | `private String name = null;` |
| 1 | 7 | ZipArchiveEntry.java:63 | 1.0 | `super(name);` |

