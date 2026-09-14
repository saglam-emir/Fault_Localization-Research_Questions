# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMNodePointer.java', 296), ('DOMNodePointer.java', 297), ('DOMNodePointer.java', 301), ('DOMNodePointer.java', 311), ('DOMNodePointer.java', 638), ('DOMNodePointer.java', 639), ('DOMNodePointer.java', 643), ('DOMNodePointer.java', 647), ('DOMNodePointer.java', 653), ('DOMNodePointer.java', 654), ('DOMNodePointer.java', 655), ('DOMNodePointer.java', 656), ('DOMNodePointer.java', 658), ('DOMNodePointer.java', 660), ('DOMNodePointer.java', 632), ('DOMNodePointer.java', 641), ('JDOMNodePointer.java', 240), ('JDOMNodePointer.java', 250), ('JDOMNodePointer.java', 251), ('JDOMNodePointer.java', 252), ('JDOMNodePointer.java', 253), ('JDOMNodePointer.java', 256), ('JDOMNodePointer.java', 257), ('JDOMNodePointer.java', 258), ('JDOMNodePointer.java', 259), ('JDOMNodePointer.java', 260), ('JDOMNodePointer.java', 262), ('JDOMNodePointer.java', 249), ('JDOMNodePointer.java', 436), ('JDOMNodePointer.java', 440), ('JDOMNodePointer.java', 441), ('JDOMNodePointer.java', 756)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JDOMNodePointer.java', 441, '->', 440)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/model/dom/DOMNodePointer.java', 311), ('src/java/org/apache/commons/jxpath/ri/model/jdom/JDOMNodePointer.java', 249)]

- SBFL   ranked 5391 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | AttributeContext.java:86 | 0.866025 | `return false;` |
| 2 | 1 | CoreOperationCompare.java:92 | 0.816497 | `return false;` |
| 3 | 6 | LocationPath.java:40 | 0.774597 | `return !absolute || super.computeContextDependent();` |
| 3 | 6 | TreeCompiler.java:197 | 0.774597 | `return false;` |
| 3 | 6 | XPathParser.java:42 | 0.774597 | `jj_consume_token(TEXT);` |
| 3 | 6 | XPathParser.java:43 | 0.774597 | `break;` |
| 3 | 6 | XPathParser.java:60 | 0.774597 | `jj_consume_token(FUNCTION_ID);` |
| 3 | 6 | XPathParser.java:61 | 0.774597 | `break;` |
| 9 | 24 | CoreOperationCompare.java:74 | 0.738549 | `return contains((Iterator) l, r);` |
| 9 | 24 | CoreOperationCompare.java:86 | 0.738549 | `while (it.hasNext()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

