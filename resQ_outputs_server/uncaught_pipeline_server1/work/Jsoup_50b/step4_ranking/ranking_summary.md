# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 93), ('DataUtil.java', 126), ('DataUtil.java', 127), ('DataUtil.java', 128), ('DataUtil.java', 129), ('DataUtil.java', 130), ('DataUtil.java', 131), ('DataUtil.java', 132)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/helper/DataUtil.java', 93)]

- SBFL   ranked 2693 statement(s)
- Hybrid ranked 119 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | CharacterReader.java:164 | 0.707107 | `break;` |
| 1 | 7 | TokeniserState.java:20 | 0.707107 | `t.error(this); // NOT replacement character (oddly?)` |
| 1 | 7 | TokeniserState.java:21 | 0.707107 | `t.emit(r.consume());` |
| 1 | 7 | TokeniserState.java:22 | 0.707107 | `break;` |
| 1 | 7 | TokeniserState.java:157 | 0.707107 | `t.error(this);` |
| 1 | 7 | TokeniserState.java:158 | 0.707107 | `t.emit('<'); // char that got us here` |
| 1 | 7 | TokeniserState.java:159 | 0.707107 | `t.transition(Data);` |
| 8 | 3 | HtmlTreeBuilderState.java:154 | 0.57735 | `return anythingElse(t, tb);` |
| 8 | 3 | HtmlTreeBuilderState.java:233 | 0.57735 | `anythingElse(t, tb);` |
| 8 | 3 | HtmlTreeBuilderState.java:1467 | 0.57735 | `return false;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 119 | Attributes.java:19 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 119 | Attributes.java:22 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |
| 1 | 119 | Collector.java:23 | 0.0 | `Elements elements = new Elements();` |
| 1 | 119 | Collector.java:25 | 0.0 | `return elements;` |
| 1 | 119 | DataUtil.java:94 | 0.0 | `if (charsetName == null) { // determine from meta. safe parse as UTF-8` |
| 1 | 119 | DataUtil.java:97 | 0.0 | `doc = parser.parseInput(docData, baseUri);` |
| 1 | 119 | DataUtil.java:137 | 0.0 | `return doc;` |
| 1 | 119 | Document.java:30 | 0.0 | `super(Tag.valueOf("#root"), baseUri);` |
| 1 | 119 | Document.java:42 | 0.0 | `Document doc = new Document(baseUri);` |
| 1 | 119 | Document.java:43 | 0.0 | `Element html = doc.appendElement("html");` |

