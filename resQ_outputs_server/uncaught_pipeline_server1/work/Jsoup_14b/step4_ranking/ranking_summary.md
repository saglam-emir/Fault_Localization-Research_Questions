# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Tokeniser.java', 197), ('TokeniserState.java', 218), ('TokeniserState.java', 220)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TokeniserState.java', 218, '->', 215), ('TokeniserState.java', 220, '->', 215)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/parser/Tokeniser.java', 197)]

- SBFL   ranked 2137 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2137 | Attribute.java:21 | 0.0 | `public Attribute(String key, String value) {` |
| 1 | 2137 | Attribute.java:22 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 2137 | Attribute.java:23 | 0.0 | `Validate.notNull(value);` |
| 1 | 2137 | Attribute.java:24 | 0.0 | `this.key = key.trim().toLowerCase();` |
| 1 | 2137 | Attribute.java:25 | 0.0 | `this.value = value;` |
| 1 | 2137 | Attribute.java:33 | 0.0 | `return key;` |
| 1 | 2137 | Attribute.java:50 | 0.0 | `return value;` |
| 1 | 2137 | Attributes.java:17 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 2137 | Attributes.java:20 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |
| 1 | 2137 | Attributes.java:31 | 0.0 | `Validate.notEmpty(key);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

