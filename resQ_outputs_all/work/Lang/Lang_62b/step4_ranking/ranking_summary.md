# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Entities.java', 850), ('Entities.java', 920), ('Entities.java', 925), ('Entities.java', 926)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Entities.java', 920, '->', 916), ('Entities.java', 926, '->', 912)]

Ground_Truth_Answerable: True

- SBFL   ranked 429 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Entities.java:814 | 0.46291 | `int firstAmp = str.indexOf('&');` |
| 1 | 2 | Entities.java:815 | 0.46291 | `if (firstAmp < 0) {` |
| 3 | 1 | Entities.java:816 | 0.435194 | `return str;` |
| 4 | 66 | Entities.java:39 | 0.377964 | `class Entities {` |
| 4 | 66 | Entities.java:41 | 0.377964 | `private static final String[][] BASIC_ARRAY = {` |
| 4 | 66 | Entities.java:48 | 0.377964 | `private static final String[][] APOS_ARRAY = {` |
| 4 | 66 | Entities.java:53 | 0.377964 | `static final String[][] ISO8859_1_ARRAY = {` |
| 4 | 66 | Entities.java:154 | 0.377964 | `static final String[][] HTML40_ARRAY = {` |
| 4 | 66 | Entities.java:366 | 0.377964 | `XML = new Entities();` |
| 4 | 66 | Entities.java:367 | 0.377964 | `XML.addEntities(BASIC_ARRAY);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

