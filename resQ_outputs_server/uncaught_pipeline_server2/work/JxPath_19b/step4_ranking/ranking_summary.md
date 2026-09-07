# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMNodePointer.java', 560), ('DOMNodePointer.java', 561), ('DOMNodePointer.java', 562), ('DOMNodePointer.java', 564), ('DOMNodePointer.java', 571), ('JDOMNodePointer.java', 696), ('JDOMNodePointer.java', 697), ('JDOMNodePointer.java', 709)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JDOMNodePointer.java', 697, '->', 696)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/model/dom/DOMNodePointer.java', 571), ('src/java/org/apache/commons/jxpath/ri/model/jdom/JDOMNodePointer.java', 709)]

- SBFL   ranked 5641 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | NamespaceResolver.java:156 | 1.0 | `String prefix = getExternallyRegisteredPrefix(namespaceURI);` |
| 1 | 4 | NamespaceResolver.java:157 | 1.0 | `return prefix == null && pointer != null ? getPrefix(pointer,` |
| 1 | 4 | NamespaceResolver.java:168 | 1.0 | `String prefix = (String) reverseMap.get(namespaceURI);` |
| 1 | 4 | NamespaceResolver.java:169 | 1.0 | `return prefix == null && parent != null ? parent` |
| 5 | 2 | Path.java:293 | 0.816497 | `String namespaceURI = context.getJXPathContext()` |
| 5 | 2 | Path.java:295 | 0.816497 | `nodeTest = new NodeNameTest(qname, namespaceURI);` |
| 7 | 58 | ContainerPointer.java:164 | 0.707107 | `return parent == null ? "/" : parent.asPath();` |
| 7 | 58 | DOMNodePointer.java:513 | 0.707107 | `String prefix = getNamespaceResolver().getPrefix(nsURI);` |
| 7 | 58 | DOMNodePointer.java:514 | 0.707107 | `if (prefix != null) {` |
| 7 | 58 | DOMNodePointer.java:515 | 0.707107 | `buffer.append(prefix);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

