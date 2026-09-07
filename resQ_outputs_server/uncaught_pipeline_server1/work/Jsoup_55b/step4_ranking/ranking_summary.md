# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TokeniserState.java', 883)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TokeniserState.java', 883, '->', 871)]

Ground_Truth_Answerable: True

- SBFL   ranked 3212 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3212 | Attribute.java:15 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 3212 | Attribute.java:31 | 0.0 | `public Attribute(String key, String value) {` |
| 1 | 3212 | Attribute.java:32 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 3212 | Attribute.java:33 | 0.0 | `Validate.notNull(value);` |
| 1 | 3212 | Attribute.java:34 | 0.0 | `this.key = key.trim();` |
| 1 | 3212 | Attribute.java:35 | 0.0 | `this.value = value;` |
| 1 | 3212 | Attribute.java:43 | 0.0 | `return key;` |
| 1 | 3212 | Attribute.java:51 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 3212 | Attribute.java:52 | 0.0 | `this.key = key.trim();` |
| 1 | 3212 | Attribute.java:60 | 0.0 | `return value;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

