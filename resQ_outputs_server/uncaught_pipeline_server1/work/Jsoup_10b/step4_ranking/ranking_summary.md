# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Node.java', 173)]

Ground_Truth_Answerable: True

- SBFL   ranked 1101 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1101 | Attribute.java:21 | 0.0 | `public Attribute(String key, String value) {` |
| 1 | 1101 | Attribute.java:22 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 1101 | Attribute.java:23 | 0.0 | `Validate.notNull(value);` |
| 1 | 1101 | Attribute.java:24 | 0.0 | `this.key = key.trim().toLowerCase();` |
| 1 | 1101 | Attribute.java:25 | 0.0 | `this.value = value;` |
| 1 | 1101 | Attribute.java:33 | 0.0 | `return key;` |
| 1 | 1101 | Attribute.java:50 | 0.0 | `return value;` |
| 1 | 1101 | Attribute.java:95 | 0.0 | `String value = Entities.unescape(encodedValue);` |
| 1 | 1101 | Attribute.java:96 | 0.0 | `return new Attribute(unencodedKey, value);` |
| 1 | 1101 | Attribute.java:118 | 0.0 | `int result = key != null ? key.hashCode() : 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

