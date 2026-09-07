# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 112), ('DataUtil.java', 113), ('DataUtil.java', 115), ('DataUtil.java', 116), ('DataUtil.java', 117), ('DataUtil.java', 118), ('XmlDeclaration.java', 46), ('XmlDeclaration.java', 47), ('XmlDeclaration.java', 48), ('XmlDeclaration.java', 49), ('XmlDeclaration.java', 50), ('XmlDeclaration.java', 51), ('XmlDeclaration.java', 52), ('XmlDeclaration.java', 53), ('XmlDeclaration.java', 54), ('XmlDeclaration.java', 55), ('XmlDeclaration.java', 56), ('XmlDeclaration.java', 57), ('XmlDeclaration.java', 58), ('XmlDeclaration.java', 59), ('XmlDeclaration.java', 60), ('XmlDeclaration.java', 61), ('XmlDeclaration.java', 68), ('XmlTreeBuilder.java', 3), ('XmlTreeBuilder.java', 76), ('XmlTreeBuilder.java', 77)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('XmlDeclaration.java', 68, '->', 65)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/parser/XmlTreeBuilder.java', 3)]

- SBFL   ranked 3151 statement(s)
- Hybrid ranked 276 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | XmlDeclaration.java:22 | 0.866025 | `super(baseUri);` |
| 1 | 4 | XmlDeclaration.java:23 | 0.866025 | `Validate.notNull(name);` |
| 1 | 4 | XmlDeclaration.java:24 | 0.866025 | `this.name = name;` |
| 1 | 4 | XmlDeclaration.java:25 | 0.866025 | `this.isProcessingInstruction = isProcessingInstruction;` |
| 5 | 17 | Attributes.java:104 | 0.707107 | `return attributes.size();` |
| 5 | 17 | Element.java:313 | 0.707107 | `Validate.notNull(child);` |
| 5 | 17 | Element.java:315 | 0.707107 | `addChildren(0, child);` |
| 5 | 17 | Element.java:316 | 0.707107 | `return this;` |
| 5 | 17 | XmlDeclaration.java:29 | 0.707107 | `return "#declaration";` |
| 5 | 17 | XmlDeclaration.java:46 | 0.707107 | `final String decl = this.name;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | Node.java:43 | 0.912871 | `this(baseUri, new Attributes());` |
| 1 | 4 | XmlDeclaration.java:22 | 0.912871 | `super(baseUri);` |
| 1 | 4 | XmlDeclaration.java:24 | 0.912871 | `this.name = name;` |
| 1 | 4 | XmlDeclaration.java:25 | 0.912871 | `this.isProcessingInstruction = isProcessingInstruction;` |
| 5 | 11 | Element.java:315 | 0.816497 | `addChildren(0, child);` |
| 5 | 11 | Element.java:316 | 0.816497 | `return this;` |
| 5 | 11 | Node.java:101 | 0.816497 | `return this;` |
| 5 | 11 | Node.java:440 | 0.816497 | `ensureChildNodes();` |
| 5 | 11 | Node.java:441 | 0.816497 | `for (int i = children.length - 1; i >= 0; i--) {` |
| 5 | 11 | Node.java:442 | 0.816497 | `Node in = children[i];` |

