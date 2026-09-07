# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Attributes.java', 6), ('Attributes.java', 118), ('Attributes.java', 123), ('Attributes.java', 239), ('Attributes.java', 397), ('HtmlTreeBuilder.java', 199), ('ParseSettings.java', 38), ('Token.java', 116), ('XmlTreeBuilder.java', 78)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/Attributes.java', 6), ('src/main/java/org/jsoup/nodes/Attributes.java', 123), ('src/main/java/org/jsoup/nodes/Attributes.java', 239), ('src/main/java/org/jsoup/nodes/Attributes.java', 397), ('src/main/java/org/jsoup/parser/HtmlTreeBuilder.java', 199), ('src/main/java/org/jsoup/parser/ParseSettings.java', 38), ('src/main/java/org/jsoup/parser/XmlTreeBuilder.java', 78)]

- SBFL   ranked 4390 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4390 | Attribute.java:14 | 0.0 | `public class Attribute implements Map.Entry<String, String>, Cloneable  {` |
| 1 | 4390 | Attribute.java:15 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 4390 | Attribute.java:33 | 0.0 | `this(key, value, null);` |
| 1 | 4390 | Attribute.java:42 | 0.0 | `public Attribute(String key, String val, Attributes parent) {` |
| 1 | 4390 | Attribute.java:43 | 0.0 | `Validate.notNull(key);` |
| 1 | 4390 | Attribute.java:44 | 0.0 | `key = key.trim();` |
| 1 | 4390 | Attribute.java:45 | 0.0 | `Validate.notEmpty(key); // trimming could potentially make empty, so validate here` |
| 1 | 4390 | Attribute.java:46 | 0.0 | `this.key = key;` |
| 1 | 4390 | Attribute.java:47 | 0.0 | `this.val = val;` |
| 1 | 4390 | Attribute.java:48 | 0.0 | `this.parent = parent;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

