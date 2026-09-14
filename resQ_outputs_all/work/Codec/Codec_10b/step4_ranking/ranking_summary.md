# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Caverphone.java', 76)]

Ground_Truth_Answerable: True

- SBFL   ranked 64 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Caverphone.java:170 | 0.353553 | `return caverphone(pString);` |
| 2 | 62 | Caverphone.java:41 | 0.333333 | `super();` |
| 2 | 62 | Caverphone.java:54 | 0.333333 | `if( txt == null || txt.length() == 0 ) {` |
| 2 | 62 | Caverphone.java:59 | 0.333333 | `txt = txt.toLowerCase(java.util.Locale.ENGLISH);` |
| 2 | 62 | Caverphone.java:62 | 0.333333 | `txt = txt.replaceAll("[^a-z]", "");` |
| 2 | 62 | Caverphone.java:65 | 0.333333 | `txt = txt.replaceAll("e$", "");             // 2.0 only` |
| 2 | 62 | Caverphone.java:68 | 0.333333 | `txt = txt.replaceAll("^cough", "cou2f");` |
| 2 | 62 | Caverphone.java:69 | 0.333333 | `txt = txt.replaceAll("^rough", "rou2f");` |
| 2 | 62 | Caverphone.java:70 | 0.333333 | `txt = txt.replaceAll("^tough", "tou2f");` |
| 2 | 62 | Caverphone.java:71 | 0.333333 | `txt = txt.replaceAll("^enough", "enou2f");  // 2.0 only` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

