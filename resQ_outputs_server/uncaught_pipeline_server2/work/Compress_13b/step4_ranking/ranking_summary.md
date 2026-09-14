# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveEntry.java', 512)]

Ground_Truth_Answerable: True

- SBFL   ranked 2586 statement(s)
- Hybrid ranked 364 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | ZipUtil.java:129 | 0.57735 | `ze.setName(newName);` |
| 1 | 6 | ZipUtil.java:154 | 0.57735 | `CRC32 crc32 = new CRC32();` |
| 1 | 6 | ZipUtil.java:155 | 0.57735 | `crc32.update(orig);` |
| 1 | 6 | ZipUtil.java:156 | 0.57735 | `long origCRC32 = crc32.getValue();` |
| 1 | 6 | ZipUtil.java:158 | 0.57735 | `if (origCRC32 == f.getNameCRC32()) {` |
| 1 | 6 | ZipUtil.java:160 | 0.57735 | `return ZipEncodingHelper` |
| 7 | 6 | AbstractUnicodeExtraField.java:90 | 0.426401 | `return nameCRC32;` |
| 7 | 6 | AbstractUnicodeExtraField.java:106 | 0.426401 | `byte[] b = null;` |
| 7 | 6 | AbstractUnicodeExtraField.java:107 | 0.426401 | `if (unicodeName != null) {` |
| 7 | 6 | AbstractUnicodeExtraField.java:108 | 0.426401 | `b = new byte[unicodeName.length];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 364 | AbstractUnicodeExtraField.java:74 | 0.0 | `if (unicodeName == null) {` |
| 1 | 364 | AbstractUnicodeExtraField.java:78 | 0.0 | `data = new byte[5 + unicodeName.length];` |
| 1 | 364 | AbstractUnicodeExtraField.java:107 | 0.0 | `if (unicodeName != null) {` |
| 1 | 364 | AbstractUnicodeExtraField.java:108 | 0.0 | `b = new byte[unicodeName.length];` |
| 1 | 364 | AbstractUnicodeExtraField.java:109 | 0.0 | `System.arraycopy(unicodeName, 0, b, 0, b.length);` |
| 1 | 364 | AbstractUnicodeExtraField.java:111 | 0.0 | `return b;` |
| 1 | 364 | AbstractUnicodeExtraField.java:130 | 0.0 | `if (data == null) {` |
| 1 | 364 | AbstractUnicodeExtraField.java:131 | 0.0 | `this.assembleData();` |
| 1 | 364 | AbstractUnicodeExtraField.java:134 | 0.0 | `if (data != null) {` |
| 1 | 364 | AbstractUnicodeExtraField.java:135 | 0.0 | `b = new byte[data.length];` |

