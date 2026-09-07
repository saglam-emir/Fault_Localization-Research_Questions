# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Entities.java', 3), ('Entities.java', 61), ('Entities.java', 103), ('Entities.java', 104), ('Entities.java', 105), ('Entities.java', 106), ('Entities.java', 107), ('Entities.java', 108), ('Entities.java', 109), ('Entities.java', 110), ('Entities.java', 111), ('Entities.java', 112), ('Entities.java', 113), ('Entities.java', 114), ('Entities.java', 115), ('Entities.java', 116), ('Entities.java', 117), ('Entities.java', 118), ('Entities.java', 119), ('Entities.java', 120), ('Entities.java', 121), ('Entities.java', 122), ('Entities.java', 123), ('Entities.java', 124), ('Entities.java', 125), ('Entities.java', 126), ('Entities.java', 127), ('Entities.java', 128), ('Entities.java', 129), ('Parser.java', 133), ('Tokeniser.java', 136), ('Tokeniser.java', 139), ('Tokeniser.java', 140), ('Tokeniser.java', 141), ('Tokeniser.java', 142), ('Tokeniser.java', 143), ('Tokeniser.java', 144), ('Tokeniser.java', 145), ('Tokeniser.java', 146), ('Tokeniser.java', 147), ('Tokeniser.java', 152), ('Tokeniser.java', 238)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Entities.java', 104, '->', 103), ('Entities.java', 119, '->', 118), ('Tokeniser.java', 142, '->', 141), ('Tokeniser.java', 152, '->', 151)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/Entities.java', 3), ('src/main/java/org/jsoup/nodes/Entities.java', 61), ('src/main/java/org/jsoup/parser/Parser.java', 133), ('src/main/java/org/jsoup/parser/Tokeniser.java', 238)]

- SBFL   ranked 2216 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2216 | Attribute.java:21 | 0.0 | `public Attribute(String key, String value) {` |
| 1 | 2216 | Attribute.java:22 | 0.0 | `Validate.notEmpty(key);` |
| 1 | 2216 | Attribute.java:23 | 0.0 | `Validate.notNull(value);` |
| 1 | 2216 | Attribute.java:24 | 0.0 | `this.key = key.trim().toLowerCase();` |
| 1 | 2216 | Attribute.java:25 | 0.0 | `this.value = value;` |
| 1 | 2216 | Attribute.java:33 | 0.0 | `return key;` |
| 1 | 2216 | Attribute.java:50 | 0.0 | `return value;` |
| 1 | 2216 | Attribute.java:73 | 0.0 | `accum` |
| 1 | 2216 | Attributes.java:17 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 2216 | Attributes.java:20 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

