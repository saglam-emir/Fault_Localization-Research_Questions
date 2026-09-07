# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Element.java', 89), ('Element.java', 1402), ('Element.java', 1408), ('Element.java', 1409), ('Element.java', 1414), ('Element.java', 1411)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/nodes/Element.java', 1411)]

- SBFL   ranked 2776 statement(s)
- Hybrid ranked 429 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | ConstrainableInputStream.java:18 | 0.922958 | `super(in, bufferSize);` |
| 1 | 29 | ConstrainableInputStream.java:19 | 0.922958 | `Validate.isTrue(maxSize >= 0);` |
| 1 | 29 | ConstrainableInputStream.java:20 | 0.922958 | `remaining = maxSize;` |
| 1 | 29 | ConstrainableInputStream.java:21 | 0.922958 | `capped = maxSize != 0;` |
| 1 | 29 | ConstrainableInputStream.java:26 | 0.922958 | `if (Thread.interrupted() || remaining < 0)` |
| 1 | 29 | ConstrainableInputStream.java:29 | 0.922958 | `final int read = super.read(b, off, len);` |
| 1 | 29 | ConstrainableInputStream.java:30 | 0.922958 | `if (capped) {` |
| 1 | 29 | ConstrainableInputStream.java:33 | 0.922958 | `return read;` |
| 1 | 29 | DataUtil.java:94 | 0.922958 | `if (input == null) // empty body` |
| 1 | 29 | DataUtil.java:97 | 0.922958 | `if (!(input instanceof ConstrainableInputStream))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | Element.java:40 | 0.204124 | `public class Element extends Node {` |
| 1 | 23 | Element.java:280 | 0.204124 | `for (int i = 0; i < size; i++) {` |
| 1 | 23 | Element.java:281 | 0.204124 | `final Node node = childNodes.get(i);` |
| 1 | 23 | Element.java:283 | 0.204124 | `children.add((Element) node);` |
| 1 | 23 | Element.java:285 | 0.204124 | `shadowChildrenRef = new WeakReference<>(children);` |
| 1 | 23 | Element.java:690 | 0.204124 | `return null;` |
| 1 | 23 | Element.java:1399 | 0.204124 | `Element clone = (Element) super.doClone(parent);` |
| 1 | 23 | Element.java:1402 | 0.204124 | `clone.childNodes = new NodeList(childNodes.size());` |
| 1 | 23 | HtmlTreeBuilder.java:166 | 0.204124 | `return doc;` |
| 1 | 23 | HtmlTreeBuilderState.java:25 | 0.204124 | `tb.getDocument().appendChild(doctype);` |

