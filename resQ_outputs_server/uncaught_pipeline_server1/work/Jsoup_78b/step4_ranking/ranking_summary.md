# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 3), ('DataUtil.java', 151), ('DataUtil.java', 152), ('DataUtil.java', 153)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DataUtil.java', 152, '->', 147)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/helper/DataUtil.java', 3)]

- SBFL   ranked 3477 statement(s)
- Hybrid ranked 15 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | HttpConnection.java:798 | 0.57735 | `} catch (IOException e){` |
| 1 | 3 | HttpConnection.java:801 | 0.57735 | `conn.disconnect();` |
| 1 | 3 | HttpConnection.java:802 | 0.57735 | `throw e;` |
| 4 | 5 | HttpConnection.java:158 | 0.333333 | `req.timeout(millis);` |
| 4 | 5 | HttpConnection.java:159 | 0.333333 | `return this;` |
| 4 | 5 | HttpConnection.java:583 | 0.333333 | `Validate.isTrue(millis >= 0, "Timeout milliseconds must be 0 (infinite) or greater");` |
| 4 | 5 | HttpConnection.java:584 | 0.333333 | `timeoutMilliseconds = millis;` |
| 4 | 5 | HttpConnection.java:585 | 0.333333 | `return this;` |
| 9 | 1 | HttpConnection.java:719 | 0.218218 | `Validate.isFalse(hasRequestBody, "Cannot set a request body for HTTP method " + req.method());` |
| 10 | 1 | HttpConnection.java:725 | 0.174078 | `else if (methodHasBody)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | CharacterReader.java:30 | 0.0 | `public CharacterReader(Reader input, int sz) {` |
| 1 | 15 | CharacterReader.java:43 | 0.0 | `this(new StringReader(input), input.length());` |
| 1 | 15 | Document.java:195 | 0.0 | `return super.html(); // no outer wrapper tag` |
| 1 | 15 | Document.java:377 | 0.0 | `private boolean prettyPrint = true;` |
| 1 | 15 | Document.java:479 | 0.0 | `return prettyPrint;` |
| 1 | 15 | Element.java:1400 | 0.0 | `StringBuilder accum = StringUtil.stringBuilder();` |
| 1 | 15 | Element.java:1402 | 0.0 | `return getOutputSettings().prettyPrint() ? accum.toString().trim() : accum.toString();` |
| 1 | 15 | Entities.java:21 | 0.0 | `public class Entities {` |
| 1 | 15 | Entities.java:41 | 0.0 | `extended(EntitiesData.fullPoints, 2125);` |
| 1 | 15 | Entities.java:52 | 0.0 | `load(this, file, size);` |

