# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TarUtils.java', 98), ('TarUtils.java', 101)]

Ground_Truth_Answerable: True

- SBFL   ranked 1759 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | TarUtils.java:94 | 0.301511 | `StringBuffer result = new StringBuffer(length);` |
| 1 | 7 | TarUtils.java:95 | 0.301511 | `int          end = offset + length;` |
| 1 | 7 | TarUtils.java:97 | 0.301511 | `for (int i = offset; i < end; ++i) {` |
| 1 | 7 | TarUtils.java:98 | 0.301511 | `if (buffer[i] == 0) {` |
| 1 | 7 | TarUtils.java:99 | 0.301511 | `break;` |
| 1 | 7 | TarUtils.java:101 | 0.301511 | `result.append((char) buffer[i]);` |
| 1 | 7 | TarUtils.java:104 | 0.301511 | `return result.toString();` |
| 8 | 5 | TarUtils.java:126 | 0.258199 | `for (i = 0; i < length && i < name.length(); ++i) {` |
| 8 | 5 | TarUtils.java:127 | 0.258199 | `buf[offset + i] = (byte) name.charAt(i);` |
| 8 | 5 | TarUtils.java:131 | 0.258199 | `for (; i < length; ++i) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

