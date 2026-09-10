# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StrBuilder.java', 1673), ('StrBuilder.java', 1730)]

Ground_Truth_Answerable: True

- SBFL   ranked 1324 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | StrBuilder.java:1672 | 0.5 | `char[] thisBuf = buffer;` |
| 1 | 4 | StrBuilder.java:1673 | 0.5 | `for (int i = 0; i < thisBuf.length; i++) {` |
| 1 | 4 | StrBuilder.java:1674 | 0.5 | `if (thisBuf[i] == ch) {` |
| 1 | 4 | StrBuilder.java:1675 | 0.5 | `return true;` |
| 5 | 6 | StrBuilder.java:1202 | 0.408248 | `int len = (str == null ? 0 : str.length());` |
| 5 | 6 | StrBuilder.java:1203 | 0.408248 | `if (len > 0) {` |
| 5 | 6 | StrBuilder.java:1204 | 0.408248 | `int index = indexOf(str, 0);` |
| 5 | 6 | StrBuilder.java:1205 | 0.408248 | `if (index >= 0) {` |
| 5 | 6 | StrBuilder.java:1206 | 0.408248 | `deleteImpl(index, index + len, len);` |
| 5 | 6 | StrBuilder.java:1209 | 0.408248 | `return this;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

