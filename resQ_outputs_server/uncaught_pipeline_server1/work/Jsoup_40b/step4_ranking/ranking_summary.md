# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DocumentType.java', 22)]

Ground_Truth_Answerable: True

- SBFL   ranked 2585 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Validate.java:92 | 0.57735 | `throw new IllegalArgumentException("String must not be empty");` |
| 2 | 2 | DocumentType.java:20 | 0.166667 | `super(baseUri);` |
| 2 | 2 | DocumentType.java:22 | 0.166667 | `Validate.notEmpty(name);` |
| 4 | 1 | Node.java:42 | 0.109109 | `this(baseUri, new Attributes());` |
| 5 | 10 | Attributes.java:17 | 0.089087 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 5 | 10 | Attributes.java:20 | 0.089087 | `private LinkedHashMap<String, Attribute> attributes = null;` |
| 5 | 10 | Node.java:32 | 0.089087 | `protected Node(String baseUri, Attributes attributes) {` |
| 5 | 10 | Node.java:33 | 0.089087 | `Validate.notNull(baseUri);` |
| 5 | 10 | Node.java:34 | 0.089087 | `Validate.notNull(attributes);` |
| 5 | 10 | Node.java:36 | 0.089087 | `childNodes = new ArrayList<Node>(4);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

