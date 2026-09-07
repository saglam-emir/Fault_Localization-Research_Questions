# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HtmlTreeBuilder.java', 468), ('HtmlTreeBuilder.java', 469), ('HtmlTreeBuilder.java', 470), ('HtmlTreeBuilder.java', 471)]

Ground_Truth_Answerable: True

- SBFL   ranked 3981 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3981 | Attribute.java:14 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 3981 | Attribute.java:41 | 0.0 | `public Attribute(String key, String val, Attributes parent) {` |
| 1 | 3981 | Attribute.java:42 | 0.0 | `Validate.notNull(key);` |
| 1 | 3981 | Attribute.java:43 | 0.0 | `this.key = key.trim();` |
| 1 | 3981 | Attribute.java:44 | 0.0 | `Validate.notEmpty(key); // trimming could potentially make empty, so validate here` |
| 1 | 3981 | Attribute.java:45 | 0.0 | `this.val = val;` |
| 1 | 3981 | Attribute.java:46 | 0.0 | `this.parent = parent;` |
| 1 | 3981 | Attribute.java:54 | 0.0 | `return key;` |
| 1 | 3981 | Attribute.java:78 | 0.0 | `return val;` |
| 1 | 3981 | Attribute.java:112 | 0.0 | `accum.append(key);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

