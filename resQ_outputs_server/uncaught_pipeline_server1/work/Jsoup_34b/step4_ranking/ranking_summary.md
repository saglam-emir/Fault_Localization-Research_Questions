# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CharacterReader.java', 91)]

Ground_Truth_Answerable: True

- SBFL   ranked 2508 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2508 | Attribute.java:21 | 0.0 | `public Attribute(String key, String value) {` |
| 1 | 2508 | Attribute.java:22 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 2508 | Attribute.java:23 | 0.0 | `Validate.notNull(value);` |
| 1 | 2508 | Attribute.java:24 | 0.0 | `this.key = key.trim().toLowerCase();` |
| 1 | 2508 | Attribute.java:25 | 0.0 | `this.value = value;` |
| 1 | 2508 | Attribute.java:33 | 0.0 | `return key;` |
| 1 | 2508 | Attribute.java:50 | 0.0 | `return value;` |
| 1 | 2508 | Attribute.java:73 | 0.0 | `accum` |
| 1 | 2508 | Attributes.java:17 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 2508 | Attributes.java:20 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

