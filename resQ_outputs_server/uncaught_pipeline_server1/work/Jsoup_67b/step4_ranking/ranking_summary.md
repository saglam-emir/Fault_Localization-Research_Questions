# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HtmlTreeBuilder.java', 42), ('HtmlTreeBuilder.java', 468)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/parser/HtmlTreeBuilder.java', 42)]

- SBFL   ranked 3124 statement(s)
- Hybrid ranked 313 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 44 | ConstrainableInputStream.java:22 | 0.945905 | `private long timeout = -1; // optional max time of request` |
| 1 | 44 | ConstrainableInputStream.java:27 | 0.945905 | `super(in, bufferSize);` |
| 1 | 44 | ConstrainableInputStream.java:28 | 0.945905 | `Validate.isTrue(maxSize >= 0);` |
| 1 | 44 | ConstrainableInputStream.java:29 | 0.945905 | `this.maxSize = maxSize;` |
| 1 | 44 | ConstrainableInputStream.java:30 | 0.945905 | `remaining = maxSize;` |
| 1 | 44 | ConstrainableInputStream.java:31 | 0.945905 | `capped = maxSize != 0;` |
| 1 | 44 | ConstrainableInputStream.java:32 | 0.945905 | `startTime = System.nanoTime();` |
| 1 | 44 | ConstrainableInputStream.java:43 | 0.945905 | `return in instanceof ConstrainableInputStream` |
| 1 | 44 | ConstrainableInputStream.java:44 | 0.945905 | `? (ConstrainableInputStream) in` |
| 1 | 44 | ConstrainableInputStream.java:45 | 0.945905 | `: new ConstrainableInputStream(in, bufferSize, maxSize);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | HttpConnection.java:73 | 0.327327 | `Connection con = new HttpConnection();` |
| 1 | 6 | HttpConnection.java:74 | 0.327327 | `con.url(url);` |
| 1 | 6 | HttpConnection.java:75 | 0.327327 | `return con;` |
| 1 | 6 | HttpConnection.java:119 | 0.327327 | `private HttpConnection() {` |
| 1 | 6 | HttpConnection.java:136 | 0.327327 | `return this;` |
| 1 | 6 | Jsoup.java:73 | 0.327327 | `return HttpConnection.connect(url);` |
| 7 | 3 | HttpConnection.java:152 | 0.188982 | `return this;` |
| 7 | 3 | HttpConnection.java:173 | 0.188982 | `return this;` |
| 7 | 3 | HttpConnection.java:198 | 0.188982 | `return this;` |
| 10 | 304 | Attributes.java:32 | 0.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |

