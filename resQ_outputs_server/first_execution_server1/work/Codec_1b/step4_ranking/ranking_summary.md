# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Caverphone.java', 59), ('Metaphone.java', 88), ('SoundexUtils.java', 53)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/codec/language/Metaphone.java', 88)]

- SBFL   ranked 651 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 651 | Caverphone.java:41 | 0.0 | `super();` |
| 1 | 651 | Caverphone.java:54 | 0.0 | `if( txt == null || txt.length() == 0 ) {` |
| 1 | 651 | Caverphone.java:59 | 0.0 | `txt = txt.toLowerCase();` |
| 1 | 651 | Caverphone.java:62 | 0.0 | `txt = txt.replaceAll("[^a-z]", "");` |
| 1 | 651 | Caverphone.java:65 | 0.0 | `txt = txt.replaceAll("e$", "");             // 2.0 only` |
| 1 | 651 | Caverphone.java:68 | 0.0 | `txt = txt.replaceAll("^cough", "cou2f");` |
| 1 | 651 | Caverphone.java:69 | 0.0 | `txt = txt.replaceAll("^rough", "rou2f");` |
| 1 | 651 | Caverphone.java:70 | 0.0 | `txt = txt.replaceAll("^tough", "tou2f");` |
| 1 | 651 | Caverphone.java:71 | 0.0 | `txt = txt.replaceAll("^enough", "enou2f");  // 2.0 only` |
| 1 | 651 | Caverphone.java:72 | 0.0 | `txt = txt.replaceAll("^trough", "trou2f");  // 2.0 only - note the spec says ^enough here again, c+p error I assume` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

