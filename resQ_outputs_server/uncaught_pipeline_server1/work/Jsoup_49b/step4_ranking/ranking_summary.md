# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Node.java', 446), ('Node.java', 445)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Node.java', 445, '->', 441)]

Ground_Truth_Answerable: True

- SBFL   ranked 3143 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Element.java:322 | 0.288675 | `ArrayList<Node> nodes = new ArrayList<Node>(children);` |
| 1 | 5 | Element.java:323 | 0.288675 | `Node[] nodeArray = nodes.toArray(new Node[nodes.size()]);` |
| 1 | 5 | Element.java:324 | 0.288675 | `addChildren(index, nodeArray);` |
| 1 | 5 | Element.java:325 | 0.288675 | `return this;` |
| 1 | 5 | Node.java:457 | 0.288675 | `child.parentNode.removeChild(child);` |
| 6 | 4 | Element.java:317 | 0.258199 | `Validate.notNull(children, "Children collection to be inserted must not be null.");` |
| 6 | 4 | Element.java:318 | 0.258199 | `int currentSize = childNodeSize();` |
| 6 | 4 | Element.java:319 | 0.258199 | `if (index < 0) index += currentSize +1; // roll around` |
| 6 | 4 | Element.java:320 | 0.258199 | `Validate.isTrue(index >= 0 && index <= currentSize, "Insert position out of bounds.");` |
| 10 | 13 | Element.java:459 | 0.204124 | `childNodes.clear();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Element.java:1198 | 1.0 | `return outerHtml();` |

