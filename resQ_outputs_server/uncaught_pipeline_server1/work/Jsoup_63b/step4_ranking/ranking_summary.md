# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HtmlTreeBuilder.java', 227), ('HtmlTreeBuilder.java', 229), ('HtmlTreeBuilder.java', 231), ('HtmlTreeBuilder.java', 232), ('Tokeniser.java', 36), ('Tokeniser.java', 44), ('Tokeniser.java', 45), ('Tokeniser.java', 46), ('Tokeniser.java', 47), ('Tokeniser.java', 76), ('Tokeniser.java', 77), ('Tokeniser.java', 124), ('Tokeniser.java', 125), ('Tokeniser.java', 126)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Tokeniser.java', 36, '->', 33), ('Tokeniser.java', 77, '->', 76)]

Ground_Truth_Answerable: True

- SBFL   ranked 2576 statement(s)
- Hybrid ranked 135 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 29 | ConstrainableInputStream.java:18 | 0.957427 | `super(in, bufferSize);` |
| 1 | 29 | ConstrainableInputStream.java:19 | 0.957427 | `Validate.isTrue(maxSize >= 0);` |
| 1 | 29 | ConstrainableInputStream.java:20 | 0.957427 | `remaining = maxSize;` |
| 1 | 29 | ConstrainableInputStream.java:21 | 0.957427 | `capped = maxSize != 0;` |
| 1 | 29 | ConstrainableInputStream.java:26 | 0.957427 | `if (Thread.interrupted() || remaining < 0)` |
| 1 | 29 | ConstrainableInputStream.java:29 | 0.957427 | `final int read = super.read(b, off, len);` |
| 1 | 29 | ConstrainableInputStream.java:30 | 0.957427 | `if (capped) {` |
| 1 | 29 | ConstrainableInputStream.java:33 | 0.957427 | `return read;` |
| 1 | 29 | DataUtil.java:94 | 0.957427 | `if (input == null) // empty body` |
| 1 | 29 | DataUtil.java:97 | 0.957427 | `if (!(input instanceof ConstrainableInputStream))` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 135 | Attributes.java:30 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 135 | Attributes.java:33 | 0.0 | `private LinkedHashMap<String, Attribute> attributes = null;` |
| 1 | 135 | ChangeNotifyingArrayList.java:11 | 0.0 | `super(initialCapacity);` |
| 1 | 135 | ChangeNotifyingArrayList.java:30 | 0.0 | `onContentsChanged();` |
| 1 | 135 | ChangeNotifyingArrayList.java:31 | 0.0 | `super.add(index, element);` |
| 1 | 135 | Collector.java:23 | 0.0 | `Elements elements = new Elements();` |
| 1 | 135 | Collector.java:25 | 0.0 | `return elements;` |
| 1 | 135 | Document.java:31 | 0.0 | `super(Tag.valueOf("#root", ParseSettings.htmlDefault), baseUri);` |
| 1 | 135 | Document.java:43 | 0.0 | `Document doc = new Document(baseUri);` |
| 1 | 135 | Document.java:44 | 0.0 | `Element html = doc.appendElement("html");` |

