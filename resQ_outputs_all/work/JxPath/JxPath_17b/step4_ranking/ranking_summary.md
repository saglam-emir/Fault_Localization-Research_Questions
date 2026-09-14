# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMAttributeIterator.java', 84), ('DOMAttributeIterator.java', 87), ('DOMAttributeIterator.java', 88), ('DOMAttributeIterator.java', 89), ('DOMAttributeIterator.java', 91), ('DOMAttributeIterator.java', 92), ('DOMAttributeIterator.java', 93), ('DOMAttributeIterator.java', 94), ('DOMAttributeIterator.java', 95), ('DOMAttributeIterator.java', 155), ('JDOMAttributeIterator.java', 70), ('JDOMAttributeIterator.java', 74), ('JDOMAttributeIterator.java', 82), ('JDOMAttributeIterator.java', 117)]

Ground_Truth_Answerable: True

- SBFL   ranked 3019 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3019 | AbstractFactory.java:32 | 0.0 | `public abstract class AbstractFactory {` |
| 1 | 3019 | AttributeContext.java:34 | 0.0 | `private boolean setStarted = false;` |
| 1 | 3019 | AttributeContext.java:43 | 0.0 | `super(parentContext);` |
| 1 | 3019 | AttributeContext.java:44 | 0.0 | `this.nodeTest = nodeTest;` |
| 1 | 3019 | AttributeContext.java:48 | 0.0 | `return currentNodePointer;` |
| 1 | 3019 | AttributeContext.java:52 | 0.0 | `setStarted = false;` |
| 1 | 3019 | AttributeContext.java:53 | 0.0 | `iterator = null;` |
| 1 | 3019 | AttributeContext.java:54 | 0.0 | `super.reset();` |
| 1 | 3019 | AttributeContext.java:71 | 0.0 | `super.setPosition(getCurrentPosition() + 1);` |
| 1 | 3019 | AttributeContext.java:72 | 0.0 | `if (!setStarted) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

