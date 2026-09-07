# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Evaluator.java', 9), ('Evaluator.java', 754), ('Evaluator.java', 755), ('Evaluator.java', 756), ('QueryParser.java', 203)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/select/Evaluator.java', 9), ('src/main/java/org/jsoup/select/Evaluator.java', 754), ('src/main/java/org/jsoup/select/Evaluator.java', 755), ('src/main/java/org/jsoup/select/Evaluator.java', 756), ('src/main/java/org/jsoup/select/QueryParser.java', 203)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 4033 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4033 | Attribute.java:13 | 0.0 | `public class Attribute implements Map.Entry<String, String>, Cloneable  {` |
| 1 | 4033 | Attribute.java:14 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 4033 | Attribute.java:32 | 0.0 | `this(key, value, null);` |
| 1 | 4033 | Attribute.java:41 | 0.0 | `public Attribute(String key, String val, Attributes parent) {` |
| 1 | 4033 | Attribute.java:42 | 0.0 | `Validate.notNull(key);` |
| 1 | 4033 | Attribute.java:43 | 0.0 | `this.key = key.trim();` |
| 1 | 4033 | Attribute.java:44 | 0.0 | `Validate.notEmpty(key); // trimming could potentially make empty, so validate here` |
| 1 | 4033 | Attribute.java:45 | 0.0 | `this.val = val;` |
| 1 | 4033 | Attribute.java:46 | 0.0 | `this.parent = parent;` |
| 1 | 4033 | Attribute.java:54 | 0.0 | `return key;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

