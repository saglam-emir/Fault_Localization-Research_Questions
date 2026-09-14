# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Zip64ExtendedInformationExtraField.java', 259)]

Ground_Truth_Answerable: True

- SBFL   ranked 3030 statement(s)
- Hybrid ranked 359 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | Zip64ExtendedInformationExtraField.java:260 | 1.0 | `throw new ZipException("central directory zip64 extended"` |
| 1 | 16 | ZipEightByteInteger.java:166 | 1.0 | `return getValue(bytes, offset).longValue();` |
| 1 | 16 | ZipEightByteInteger.java:196 | 1.0 | `return getLongValue(bytes, 0);` |
| 1 | 16 | ZipFile.java:615 | 1.0 | `boolean hasUncompressedSize = ze.getSize() == ZIP64_MAGIC;` |
| 1 | 16 | ZipFile.java:616 | 1.0 | `boolean hasCompressedSize = ze.getCompressedSize() == ZIP64_MAGIC;` |
| 1 | 16 | ZipFile.java:617 | 1.0 | `boolean hasRelativeHeaderOffset =` |
| 1 | 16 | ZipFile.java:619 | 1.0 | `z64.reparseCentralDirectoryData(hasUncompressedSize,` |
| 1 | 16 | ZipFile.java:760 | 1.0 | `positionAtCentralDirectory64();` |
| 1 | 16 | ZipFile.java:775 | 1.0 | `skipBytes(ZIP64_EOCDL_LOCATOR_OFFSET` |
| 1 | 16 | ZipFile.java:777 | 1.0 | `archive.readFully(DWORD_BUF);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 359 | AbstractUnicodeExtraField.java:76 | 0.0 | `if (unicodeName == null) {` |
| 1 | 359 | AbstractUnicodeExtraField.java:80 | 0.0 | `data = new byte[5 + unicodeName.length];` |
| 1 | 359 | AbstractUnicodeExtraField.java:109 | 0.0 | `if (unicodeName != null) {` |
| 1 | 359 | AbstractUnicodeExtraField.java:110 | 0.0 | `b = new byte[unicodeName.length];` |
| 1 | 359 | AbstractUnicodeExtraField.java:111 | 0.0 | `System.arraycopy(unicodeName, 0, b, 0, b.length);` |
| 1 | 359 | AbstractUnicodeExtraField.java:113 | 0.0 | `return b;` |
| 1 | 359 | AbstractUnicodeExtraField.java:132 | 0.0 | `if (data == null) {` |
| 1 | 359 | AbstractUnicodeExtraField.java:133 | 0.0 | `this.assembleData();` |
| 1 | 359 | AbstractUnicodeExtraField.java:136 | 0.0 | `if (data != null) {` |
| 1 | 359 | AbstractUnicodeExtraField.java:137 | 0.0 | `b = new byte[data.length];` |

