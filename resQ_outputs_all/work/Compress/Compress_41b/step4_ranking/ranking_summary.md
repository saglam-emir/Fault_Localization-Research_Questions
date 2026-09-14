# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ZipArchiveInputStream.java', 249), ('ZipArchiveInputStream.java', 247)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ZipArchiveInputStream.java', 247, '->', 244)]

Ground_Truth_Answerable: True

- SBFL   ranked 7239 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | ExtraFieldUtils.java:91 | 0.154303 | `final UnrecognizedExtraField u = new UnrecognizedExtraField();` |
| 1 | 16 | ExtraFieldUtils.java:92 | 0.154303 | `u.setHeaderId(headerId);` |
| 1 | 16 | ExtraFieldUtils.java:93 | 0.154303 | `return u;` |
| 1 | 16 | UnrecognizedExtraField.java:29 | 0.154303 | `public class UnrecognizedExtraField implements ZipExtraField {` |
| 1 | 16 | UnrecognizedExtraField.java:41 | 0.154303 | `this.headerId = headerId;` |
| 1 | 16 | UnrecognizedExtraField.java:50 | 0.154303 | `return headerId;` |
| 1 | 16 | UnrecognizedExtraField.java:65 | 0.154303 | `localData = ZipUtil.copy(data);` |
| 1 | 16 | UnrecognizedExtraField.java:74 | 0.154303 | `return new ZipShort(localData != null ? localData.length : 0);` |
| 1 | 16 | UnrecognizedExtraField.java:83 | 0.154303 | `return ZipUtil.copy(localData);` |
| 1 | 16 | UnrecognizedExtraField.java:133 | 0.154303 | `final byte[] tmp = new byte[length];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

