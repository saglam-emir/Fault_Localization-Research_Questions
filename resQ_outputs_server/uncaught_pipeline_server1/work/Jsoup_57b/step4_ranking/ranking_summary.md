# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Attributes.java', 125)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Attributes.java', 125, '->', 124)]

Ground_Truth_Answerable: True

- SBFL   ranked 3275 statement(s)
- Hybrid ranked 17 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | Attributes.java:119 | 0.57735 | `Validate.notEmpty(key);` |
| 1 | 9 | Attributes.java:120 | 0.57735 | `if (attributes == null)` |
| 1 | 9 | Attributes.java:122 | 0.57735 | `for (Iterator<String> it = attributes.keySet().iterator(); it.hasNext(); ) {` |
| 1 | 9 | Attributes.java:123 | 0.57735 | `String attrKey = it.next();` |
| 1 | 9 | Attributes.java:124 | 0.57735 | `if (attrKey.equalsIgnoreCase(key))` |
| 1 | 9 | Attributes.java:125 | 0.57735 | `attributes.remove(attrKey);` |
| 1 | 9 | Node.java:127 | 0.57735 | `Validate.notNull(attributeKey);` |
| 1 | 9 | Node.java:128 | 0.57735 | `attributes.removeIgnoreCase(attributeKey);` |
| 1 | 9 | Node.java:129 | 0.57735 | `return this;` |
| 10 | 3 | TokeniserState.java:614 | 0.288675 | `t.emitTagPending();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | Collector.java:23 | 1.0 | `Elements elements = new Elements();` |
| 1 | 7 | Collector.java:25 | 1.0 | `return elements;` |
| 1 | 7 | Element.java:287 | 1.0 | `return Selector.select(cssQuery, this);` |
| 1 | 7 | Elements.java:18 | 1.0 | `public Elements() {` |
| 1 | 7 | Elements.java:465 | 1.0 | `return isEmpty() ? null : get(0);` |
| 1 | 7 | Selector.java:107 | 1.0 | `return new Selector(query, root).select();` |
| 1 | 7 | Selector.java:149 | 1.0 | `return Collector.collect(evaluator, root);` |
| 8 | 10 | Attributes.java:30 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 8 | 10 | Attributes.java:33 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |
| 8 | 10 | Attributes.java:77 | 0.0 | `put(attr);` |

