# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NamespaceResolver.java', 47), ('NamespaceResolver.java', 108), ('NamespaceResolver.java', 117), ('NamespaceResolver.java', 118), ('NamespaceResolver.java', 119), ('NamespaceResolver.java', 120), ('NamespaceResolver.java', 121), ('NamespaceResolver.java', 122), ('NamespaceResolver.java', 123), ('NamespaceResolver.java', 116), ('NamespaceResolver.java', 132), ('NamespaceResolver.java', 141), ('NamespaceResolver.java', 142), ('NamespaceResolver.java', 143), ('NamespaceResolver.java', 144), ('NamespaceResolver.java', 145), ('NamespaceResolver.java', 146), ('NamespaceResolver.java', 147), ('NamespaceResolver.java', 148), ('NamespaceResolver.java', 149), ('NamespaceResolver.java', 150), ('NamespaceResolver.java', 151), ('NamespaceResolver.java', 139), ('NamespaceResolver.java', 159), ('NamespaceResolver.java', 160), ('NamespaceResolver.java', 161), ('NamespaceResolver.java', 162), ('NamespaceResolver.java', 200), ('DOMNodePointer.java', 29), ('DOMNodePointer.java', 61), ('DOMNodePointer.java', 189), ('DOMNodePointer.java', 415)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/NamespaceResolver.java', 47), ('src/java/org/apache/commons/jxpath/ri/NamespaceResolver.java', 108), ('src/java/org/apache/commons/jxpath/ri/NamespaceResolver.java', 132), ('src/java/org/apache/commons/jxpath/ri/NamespaceResolver.java', 139), ('src/java/org/apache/commons/jxpath/ri/model/dom/DOMNodePointer.java', 29), ('src/java/org/apache/commons/jxpath/ri/model/dom/DOMNodePointer.java', 61), ('src/java/org/apache/commons/jxpath/ri/model/dom/DOMNodePointer.java', 189)]

- SBFL   ranked 5639 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 41 | DOMAttributeIterator.java:99 | 1.0 | `return false;` |
| 1 | 41 | DOMAttributeIterator.java:130 | 1.0 | `return null;` |
| 1 | 41 | DOMNodePointer.java:191 | 1.0 | `if (prefix == null || prefix.equals("")) {` |
| 1 | 41 | DOMNodePointer.java:195 | 1.0 | `if (prefix.equals("xml")) {` |
| 1 | 41 | DOMNodePointer.java:199 | 1.0 | `if (prefix.equals("xmlns")) {` |
| 1 | 41 | DOMNodePointer.java:203 | 1.0 | `String namespace = null;` |
| 1 | 41 | DOMNodePointer.java:204 | 1.0 | `if (namespaces == null) {` |
| 1 | 41 | DOMNodePointer.java:205 | 1.0 | `namespaces = new HashMap();` |
| 1 | 41 | DOMNodePointer.java:211 | 1.0 | `if (namespace == null) {` |
| 1 | 41 | DOMNodePointer.java:212 | 1.0 | `String qname = "xmlns:" + prefix;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

