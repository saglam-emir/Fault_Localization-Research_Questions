# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FormElement.java', 89)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/FormElement.java', 89)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 4342 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4342 | Attribute.java:15 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 4342 | Attribute.java:42 | 0.0 | `public Attribute(String key, String val, Attributes parent) {` |
| 1 | 4342 | Attribute.java:43 | 0.0 | `Validate.notNull(key);` |
| 1 | 4342 | Attribute.java:44 | 0.0 | `key = key.trim();` |
| 1 | 4342 | Attribute.java:45 | 0.0 | `Validate.notEmpty(key); // trimming could potentially make empty, so validate here` |
| 1 | 4342 | Attribute.java:46 | 0.0 | `this.key = key;` |
| 1 | 4342 | Attribute.java:47 | 0.0 | `this.val = val;` |
| 1 | 4342 | Attribute.java:48 | 0.0 | `this.parent = parent;` |
| 1 | 4342 | Attribute.java:56 | 0.0 | `return key;` |
| 1 | 4342 | Attribute.java:80 | 0.0 | `return Attributes.checkNotNull(val);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

