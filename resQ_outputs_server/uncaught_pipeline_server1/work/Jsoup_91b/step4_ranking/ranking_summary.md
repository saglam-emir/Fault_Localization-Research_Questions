# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UncheckedIOException.java', 10), ('CharacterReader.java', 37), ('CharacterReader.java', 452), ('CharacterReader.java', 457), ('CharacterReader.java', 458), ('CharacterReader.java', 459)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/UncheckedIOException.java', 10), ('src/main/java/org/jsoup/parser/CharacterReader.java', 37), ('src/main/java/org/jsoup/parser/CharacterReader.java', 452), ('src/main/java/org/jsoup/parser/CharacterReader.java', 457), ('src/main/java/org/jsoup/parser/CharacterReader.java', 458), ('src/main/java/org/jsoup/parser/CharacterReader.java', 459)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 4353 statement(s)
- Hybrid ranked 147 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | TokeniserState.java:20 | 0.654654 | `t.error(this); // NOT replacement character (oddly?)` |
| 1 | 3 | TokeniserState.java:21 | 0.654654 | `t.emit(r.consume());` |
| 1 | 3 | TokeniserState.java:22 | 0.654654 | `break;` |
| 4 | 1 | HttpConnection.java:309 | 0.534522 | `return res;` |
| 5 | 1 | CharacterReader.java:477 | 0.46291 | `return "";` |
| 6 | 3 | HtmlTreeBuilderState.java:161 | 0.400892 | `return anythingElse(t, tb);` |
| 6 | 3 | HtmlTreeBuilderState.java:240 | 0.400892 | `anythingElse(t, tb);` |
| 6 | 3 | TokeniserState.java:1700 | 0.400892 | `t.emit('&');` |
| 9 | 5 | DataUtil.java:217 | 0.377964 | `return null;` |
| 9 | 5 | HttpConnection.java:182 | 0.377964 | `req.ignoreContentType(ignoreContentType);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 147 | CharacterReader.java:27 | 0.0 | `private int bufMark = -1;` |
| 1 | 147 | CharacterReader.java:28 | 0.0 | `private final String[] stringCache = new String[512]; // holds reused strings in this doc, to lessen garbage` |
| 1 | 147 | CharacterReader.java:30 | 0.0 | `public CharacterReader(Reader input, int sz) {` |
| 1 | 147 | CharacterReader.java:33 | 0.0 | `reader = input;` |
| 1 | 147 | CharacterReader.java:34 | 0.0 | `charBuf = new char[sz > maxBufferLen ? maxBufferLen : sz];` |
| 1 | 147 | CharacterReader.java:40 | 0.0 | `this(input, maxBufferLen);` |
| 1 | 147 | CharacterReader.java:65 | 0.0 | `throw new UncheckedIOException(e);` |
| 1 | 147 | Connection.java:34 | 0.0 | `GET(false), POST(true), PUT(true), DELETE(false), PATCH(true), HEAD(false), OPTIONS(false), TRACE(false);` |
| 1 | 147 | Connection.java:38 | 0.0 | `Method(boolean hasBody) {` |
| 1 | 147 | Connection.java:39 | 0.0 | `this.hasBody = hasBody;` |

