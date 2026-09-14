# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMAttributeIterator.java', 22), ('DOMAttributeIterator.java', 111), ('JDOMAttributeIterator.java', 23), ('JDOMAttributeIterator.java', 52), ('JDOMAttributeIterator.java', 58), ('JDOMAttributeIterator.java', 114)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JDOMAttributeIterator.java', 52, '->', 47), ('JDOMAttributeIterator.java', 58, '->', 47)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/model/dom/DOMAttributeIterator.java', 22), ('src/java/org/apache/commons/jxpath/ri/model/jdom/JDOMAttributeIterator.java', 23)]

- SBFL   ranked 2893 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2893 | AbstractFactory.java:32 | 0.0 | `public abstract class AbstractFactory {` |
| 1 | 2893 | AttributeContext.java:34 | 0.0 | `private boolean setStarted = false;` |
| 1 | 2893 | AttributeContext.java:43 | 0.0 | `super(parentContext);` |
| 1 | 2893 | AttributeContext.java:44 | 0.0 | `this.nodeTest = nodeTest;` |
| 1 | 2893 | AttributeContext.java:48 | 0.0 | `return currentNodePointer;` |
| 1 | 2893 | AttributeContext.java:52 | 0.0 | `setStarted = false;` |
| 1 | 2893 | AttributeContext.java:53 | 0.0 | `iterator = null;` |
| 1 | 2893 | AttributeContext.java:54 | 0.0 | `super.reset();` |
| 1 | 2893 | AttributeContext.java:71 | 0.0 | `super.setPosition(getCurrentPosition() + 1);` |
| 1 | 2893 | AttributeContext.java:72 | 0.0 | `if (!setStarted) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

