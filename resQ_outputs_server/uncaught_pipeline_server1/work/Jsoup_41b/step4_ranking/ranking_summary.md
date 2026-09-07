# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Element.java', 1175)]

Ground_Truth_Answerable: True

- SBFL   ranked 2971 statement(s)
- Hybrid ranked 6 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | Attribute.java:129 | 0.57735 | `if (this == o) return true;` |
| 1 | 6 | Attribute.java:130 | 0.57735 | `if (!(o instanceof Attribute)) return false;` |
| 1 | 6 | Attribute.java:132 | 0.57735 | `Attribute attribute = (Attribute) o;` |
| 1 | 6 | Attribute.java:134 | 0.57735 | `if (key != null ? !key.equals(attribute.key) : attribute.key != null) return false;` |
| 1 | 6 | Attribute.java:135 | 0.57735 | `if (value != null ? !value.equals(attribute.value) : attribute.value != null) return false;` |
| 1 | 6 | Attribute.java:137 | 0.57735 | `return true;` |
| 7 | 1 | Element.java:1164 | 0.408248 | `return outerHtml();` |
| 8 | 3 | Node.java:558 | 0.333333 | `StringBuilder accum = new StringBuilder(128);` |
| 8 | 3 | Node.java:559 | 0.333333 | `outerHtml(accum);` |
| 8 | 3 | Node.java:560 | 0.333333 | `return accum.toString();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | Collector.java:23 | 0.707107 | `Elements elements = new Elements();` |
| 1 | 6 | Collector.java:25 | 0.707107 | `return elements;` |
| 1 | 6 | Element.java:255 | 0.707107 | `return Selector.select(cssQuery, this);` |
| 1 | 6 | Elements.java:18 | 0.707107 | `public Elements() {` |
| 1 | 6 | Selector.java:96 | 0.707107 | `return new Selector(query, root).select();` |
| 1 | 6 | Selector.java:118 | 0.707107 | `return Collector.collect(evaluator, root);` |

