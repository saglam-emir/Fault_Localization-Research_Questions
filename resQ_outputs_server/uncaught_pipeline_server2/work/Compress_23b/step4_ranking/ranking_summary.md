# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Coders.java', 112)]

Ground_Truth_Answerable: True

- SBFL   ranked 1921 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SevenZFile.java:104 | 0.707107 | `this.file.close();` |
| 2 | 16 | Coders.java:109 | 0.447214 | `byte propsByte = coder.properties[0];` |
| 2 | 16 | Coders.java:110 | 0.447214 | `long dictSize = coder.properties[1];` |
| 2 | 16 | Coders.java:111 | 0.447214 | `for (int i = 1; i < 4; i++) {` |
| 2 | 16 | Coders.java:112 | 0.447214 | `dictSize |= (coder.properties[i + 1] << (8 * i));` |
| 2 | 16 | Coders.java:114 | 0.447214 | `if (dictSize > LZMAInputStream.DICT_SIZE_MAX) {` |
| 2 | 16 | Coders.java:117 | 0.447214 | `return new LZMAInputStream(in, -1, propsByte, (int) dictSize);` |
| 2 | 16 | SevenZFile.java:190 | 0.447214 | `nextHeaderInputStream =` |
| 2 | 16 | SevenZFile.java:263 | 0.447214 | `readStreamsInfo(header, archive);` |
| 2 | 16 | SevenZFile.java:266 | 0.447214 | `final Folder folder = archive.folders[0];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

