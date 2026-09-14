# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SevenZOutputFile.java', 639), ('SevenZOutputFile.java', 640), ('SevenZOutputFile.java', 646)]

Ground_Truth_Answerable: True

- SBFL   ranked 1841 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | SevenZFile.java:104 | 1.0 | `this.file.close();` |
| 1 | 8 | SevenZOutputFile.java:624 | 1.0 | `firstByte |= mask;` |
| 1 | 8 | SevenZOutputFile.java:625 | 1.0 | `mask >>>= 1;` |
| 1 | 8 | SevenZOutputFile.java:629 | 1.0 | `header.write((int) (0xff & value));` |
| 1 | 8 | SevenZOutputFile.java:630 | 1.0 | `value >>>= 8;` |
| 1 | 8 | SevenZOutputFile.java:641 | 1.0 | `header.write(cache);` |
| 1 | 8 | SevenZOutputFile.java:642 | 1.0 | `shift = 7;` |
| 1 | 8 | SevenZOutputFile.java:643 | 1.0 | `cache = 0;` |
| 9 | 15 | SevenZOutputFile.java:164 | 0.942809 | `write(b, 0, b.length);` |
| 9 | 15 | SevenZOutputFile.java:422 | 0.942809 | `header.write(NID.kEmptyFile);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

