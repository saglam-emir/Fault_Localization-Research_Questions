# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ByteQuadsCanonicalizer.java', 882)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ByteQuadsCanonicalizer.java', 882, '->', 876)]

Ground_Truth_Answerable: True

- SBFL   ranked 7226 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | ByteQuadsCanonicalizer.java:641 | 1.0 | `for (offset = _spilloverStart(); offset < _spilloverEnd; offset += 4) {` |
| 1 | 8 | ByteQuadsCanonicalizer.java:642 | 1.0 | `if ((q1 == hashArea[offset]) && (1 == hashArea[offset+3])) {` |
| 1 | 8 | ByteQuadsCanonicalizer.java:646 | 1.0 | `return null;` |
| 1 | 8 | ByteQuadsCanonicalizer.java:931 | 1.0 | `if (_failOnDoS) {` |
| 1 | 8 | ByteQuadsCanonicalizer.java:932 | 1.0 | `_reportTooManyCollisions();` |
| 1 | 8 | ByteQuadsCanonicalizer.java:936 | 1.0 | `_needRehash = true;` |
| 1 | 8 | ByteQuadsCanonicalizer.java:1183 | 1.0 | `if (_hashSize <= 1024) { // would have spill-over area of 128 entries` |
| 1 | 8 | ByteQuadsCanonicalizer.java:1184 | 1.0 | `return;` |
| 9 | 9 | ByteQuadsCanonicalizer.java:497 | 0.447214 | `return _findSecondary(offset, q1);` |
| 9 | 9 | ByteQuadsCanonicalizer.java:626 | 0.447214 | `int offset = _tertiaryStart + ((origOffset >> (_tertiaryShift + 2)) << _tertiaryShift);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

