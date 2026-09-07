# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMNodePointer.java', 108)]

Ground_Truth_Answerable: True

- SBFL   ranked 5603 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | DOMNodePointer.java:142 | 1.0 | `s1 = s1 == null ? "" : s1.trim();` |
| 1 | 12 | DOMNodePointer.java:143 | 1.0 | `s2 = s2 == null ? "" : s2.trim();` |
| 1 | 12 | DOMNodePointer.java:144 | 1.0 | `return s1.equals(s2);` |
| 1 | 12 | JXPathContextReferenceImpl.java:653 | 1.0 | `return namespaceResolver.getNamespaceURI(prefix);` |
| 1 | 12 | JXPathException.java:88 | 1.0 | `String message = super.getMessage();` |
| 1 | 12 | JXPathException.java:89 | 1.0 | `if (exception == null) {` |
| 1 | 12 | JXPathException.java:90 | 1.0 | `return message;` |
| 1 | 12 | NodeNameTest.java:33 | 1.0 | `public NodeNameTest(QName qname, String namespaceURI) {` |
| 1 | 12 | NodeNameTest.java:34 | 1.0 | `this.qname = qname;` |
| 1 | 12 | NodeNameTest.java:35 | 1.0 | `this.namespaceURI = namespaceURI;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

