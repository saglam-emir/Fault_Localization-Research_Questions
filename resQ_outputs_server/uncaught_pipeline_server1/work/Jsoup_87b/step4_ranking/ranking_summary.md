# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Element.java', 140), ('HtmlTreeBuilder.java', 315), ('HtmlTreeBuilder.java', 337), ('HtmlTreeBuilder.java', 347), ('HtmlTreeBuilder.java', 355), ('HtmlTreeBuilder.java', 378), ('HtmlTreeBuilder.java', 420), ('HtmlTreeBuilder.java', 476), ('HtmlTreeBuilder.java', 517), ('HtmlTreeBuilder.java', 569), ('HtmlTreeBuilder.java', 570), ('HtmlTreeBuilder.java', 581), ('HtmlTreeBuilder.java', 618), ('HtmlTreeBuilder.java', 649), ('HtmlTreeBuilder.java', 689), ('HtmlTreeBuilderState.java', 315), ('HtmlTreeBuilderState.java', 319), ('HtmlTreeBuilderState.java', 339), ('HtmlTreeBuilderState.java', 353), ('HtmlTreeBuilderState.java', 372), ('HtmlTreeBuilderState.java', 398), ('HtmlTreeBuilderState.java', 399), ('HtmlTreeBuilderState.java', 402), ('HtmlTreeBuilderState.java', 531), ('HtmlTreeBuilderState.java', 538), ('HtmlTreeBuilderState.java', 574), ('HtmlTreeBuilderState.java', 598), ('HtmlTreeBuilderState.java', 633), ('HtmlTreeBuilderState.java', 662), ('HtmlTreeBuilderState.java', 675), ('HtmlTreeBuilderState.java', 699), ('HtmlTreeBuilderState.java', 711), ('HtmlTreeBuilderState.java', 721), ('HtmlTreeBuilderState.java', 731), ('HtmlTreeBuilderState.java', 745), ('HtmlTreeBuilderState.java', 768), ('HtmlTreeBuilderState.java', 772), ('HtmlTreeBuilderState.java', 774), ('HtmlTreeBuilderState.java', 887), ('HtmlTreeBuilderState.java', 897), ('HtmlTreeBuilderState.java', 926), ('HtmlTreeBuilderState.java', 954), ('HtmlTreeBuilderState.java', 1007), ('HtmlTreeBuilderState.java', 1018), ('HtmlTreeBuilderState.java', 1089), ('HtmlTreeBuilderState.java', 1173), ('HtmlTreeBuilderState.java', 1240), ('HtmlTreeBuilderState.java', 1244), ('HtmlTreeBuilderState.java', 1246), ('HtmlTreeBuilderState.java', 1269), ('HtmlTreeBuilderState.java', 1271), ('HtmlTreeBuilderState.java', 1277), ('HtmlTreeBuilderState.java', 1296), ('HtmlTreeBuilderState.java', 1383), ('HtmlTreeBuilderState.java', 1388), ('HtmlTreeBuilderState.java', 1393), ('Tag.java', 4), ('Tag.java', 17), ('Tag.java', 28), ('Tag.java', 43)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('HtmlTreeBuilder.java', 570, '->', 569), ('HtmlTreeBuilder.java', 649, '->', 648), ('HtmlTreeBuilderState.java', 1018, '->', 1017), ('HtmlTreeBuilderState.java', 1269, '->', 1268), ('HtmlTreeBuilderState.java', 1277, '->', 1276), ('HtmlTreeBuilderState.java', 1296, '->', 1295)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/Element.java', 140), ('src/main/java/org/jsoup/parser/Tag.java', 4), ('src/main/java/org/jsoup/parser/Tag.java', 28), ('src/main/java/org/jsoup/parser/Tag.java', 43)]

- SBFL   ranked 4315 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4315 | Attribute.java:14 | 0.0 | `public class Attribute implements Map.Entry<String, String>, Cloneable  {` |
| 1 | 4315 | Attribute.java:15 | 0.0 | `private static final String[] booleanAttributes = {` |
| 1 | 4315 | Attribute.java:33 | 0.0 | `this(key, value, null);` |
| 1 | 4315 | Attribute.java:42 | 0.0 | `public Attribute(String key, String val, Attributes parent) {` |
| 1 | 4315 | Attribute.java:43 | 0.0 | `Validate.notNull(key);` |
| 1 | 4315 | Attribute.java:44 | 0.0 | `key = key.trim();` |
| 1 | 4315 | Attribute.java:45 | 0.0 | `Validate.notEmpty(key); // trimming could potentially make empty, so validate here` |
| 1 | 4315 | Attribute.java:46 | 0.0 | `this.key = key;` |
| 1 | 4315 | Attribute.java:47 | 0.0 | `this.val = val;` |
| 1 | 4315 | Attribute.java:48 | 0.0 | `this.parent = parent;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

