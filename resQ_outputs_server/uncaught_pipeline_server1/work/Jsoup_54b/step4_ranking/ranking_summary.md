# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('W3CDom.java', 126)]

Ground_Truth_Answerable: True

- SBFL   ranked 1752 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 84 | Collector.java:23 | 1.0 | `Elements elements = new Elements();` |
| 1 | 84 | Collector.java:24 | 1.0 | `new NodeTraversor(new Accumulator(root, elements, eval)).traverse(root);` |
| 1 | 84 | Collector.java:25 | 1.0 | `return elements;` |
| 1 | 84 | Collector.java:33 | 1.0 | `Accumulator(Element root, Elements elements, Evaluator eval) {` |
| 1 | 84 | Collector.java:34 | 1.0 | `this.root = root;` |
| 1 | 84 | Collector.java:35 | 1.0 | `this.elements = elements;` |
| 1 | 84 | Collector.java:36 | 1.0 | `this.eval = eval;` |
| 1 | 84 | Collector.java:40 | 1.0 | `if (node instanceof Element) {` |
| 1 | 84 | Collector.java:41 | 1.0 | `Element el = (Element) node;` |
| 1 | 84 | Collector.java:42 | 1.0 | `if (eval.matches(root, el))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | Collector.java:23 | 0.0 | `Elements elements = new Elements();` |
| 1 | 7 | Collector.java:25 | 0.0 | `return elements;` |
| 1 | 7 | Element.java:286 | 0.0 | `return Selector.select(cssQuery, this);` |
| 1 | 7 | Elements.java:18 | 0.0 | `public Elements() {` |
| 1 | 7 | Elements.java:465 | 0.0 | `return isEmpty() ? null : get(0);` |
| 1 | 7 | Selector.java:107 | 0.0 | `return new Selector(query, root).select();` |
| 1 | 7 | Selector.java:149 | 0.0 | `return Collector.collect(evaluator, root);` |

