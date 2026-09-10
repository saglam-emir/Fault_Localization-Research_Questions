# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Entities.java', 828), ('Entities.java', 831)]

Ground_Truth_Answerable: True

- SBFL   ranked 447 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Entities.java:863 | 0.435194 | `return str;` |
| 2 | 2 | Entities.java:861 | 0.385758 | `int firstAmp = str.indexOf('&');` |
| 2 | 2 | Entities.java:862 | 0.385758 | `if (firstAmp < 0) {` |
| 4 | 66 | Entities.java:43 | 0.369274 | `class Entities {` |
| 4 | 66 | Entities.java:45 | 0.369274 | `private static final String[][] BASIC_ARRAY = {{"quot", "34"}, // " - double-quote` |
| 4 | 66 | Entities.java:51 | 0.369274 | `private static final String[][] APOS_ARRAY = {{"apos", "39"}, // XML apostrophe` |
| 4 | 66 | Entities.java:55 | 0.369274 | `static final String[][] ISO8859_1_ARRAY = {{"nbsp", "160"}, // non-breaking space` |
| 4 | 66 | Entities.java:155 | 0.369274 | `static final String[][] HTML40_ARRAY = {` |
| 4 | 66 | Entities.java:374 | 0.369274 | `XML = new Entities();` |
| 4 | 66 | Entities.java:375 | 0.369274 | `XML.addEntities(BASIC_ARRAY);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

