# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LocaleUtils.java', 114)]

Ground_Truth_Answerable: True

- SBFL   ranked 166 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | LocaleUtils.java:116 | 0.707107 | `throw new IllegalArgumentException("Invalid locale format: " + str);` |
| 2 | 4 | LocaleUtils.java:110 | 0.57735 | `if (str.charAt(2) != '_') {` |
| 2 | 4 | LocaleUtils.java:113 | 0.57735 | `char ch3 = str.charAt(3);` |
| 2 | 4 | LocaleUtils.java:114 | 0.57735 | `char ch4 = str.charAt(4);` |
| 2 | 4 | LocaleUtils.java:115 | 0.57735 | `if (ch3 < 'A' || ch3 > 'Z' || ch4 < 'A' || ch4 > 'Z') {` |
| 6 | 7 | LocaleUtils.java:95 | 0.5 | `if (str == null) {` |
| 6 | 7 | LocaleUtils.java:98 | 0.5 | `int len = str.length();` |
| 6 | 7 | LocaleUtils.java:99 | 0.5 | `if (len != 2 && len != 5 && len < 7) {` |
| 6 | 7 | LocaleUtils.java:102 | 0.5 | `char ch0 = str.charAt(0);` |
| 6 | 7 | LocaleUtils.java:103 | 0.5 | `char ch1 = str.charAt(1);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

