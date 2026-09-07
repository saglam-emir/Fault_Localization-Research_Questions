# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DocumentType.java', 4), ('DocumentType.java', 21), ('DocumentType.java', 33), ('DocumentType.java', 37)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DocumentType.java', 37, '->', 36)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/DocumentType.java', 4)]

- SBFL   ranked 2035 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DocumentType.java:23 | 0.316228 | `attr("systemId", systemId);` |
| 2 | 8 | Attributes.java:46 | 0.301511 | `Attribute attr = new Attribute(key, value);` |
| 2 | 8 | Attributes.java:47 | 0.301511 | `put(attr);` |
| 2 | 8 | DocumentType.java:19 | 0.301511 | `super(baseUri);` |
| 2 | 8 | DocumentType.java:21 | 0.301511 | `attr("name", name);` |
| 2 | 8 | DocumentType.java:22 | 0.301511 | `attr("publicId", publicId);` |
| 2 | 8 | Node.java:41 | 0.301511 | `this(baseUri, new Attributes());` |
| 2 | 8 | Node.java:95 | 0.301511 | `attributes.put(attributeKey, attributeValue);` |
| 2 | 8 | Node.java:96 | 0.301511 | `return this;` |
| 10 | 10 | Attribute.java:21 | 0.288675 | `public Attribute(String key, String value) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

