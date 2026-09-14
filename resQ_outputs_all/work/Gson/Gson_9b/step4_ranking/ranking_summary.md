# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonTreeWriter.java', 162), ('TypeAdapters.java', 165), ('TypeAdapters.java', 166), ('TypeAdapters.java', 167), ('TypeAdapters.java', 168), ('JsonWriter.java', 476)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/bind/JsonTreeWriter.java', 162), ('gson/src/main/java/com/google/gson/stream/JsonWriter.java', 476)]

- SBFL   ranked 2753 statement(s)
- Hybrid ranked 51 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | JsonWriter.java:467 | 0.099015 | `out.write(value ? "true" : "false");` |
| 1 | 2 | JsonWriter.java:468 | 0.099015 | `return this;` |
| 3 | 2 | JsonWriter.java:465 | 0.098058 | `writeDeferredName();` |
| 3 | 2 | JsonWriter.java:466 | 0.098058 | `beforeValue();` |
| 5 | 3 | JsonWriter.java:637 | 0.068041 | `out.append(',');` |
| 5 | 3 | JsonWriter.java:638 | 0.068041 | `newline();` |
| 5 | 3 | JsonWriter.java:639 | 0.068041 | `break;` |
| 8 | 3 | JsonWriter.java:632 | 0.060634 | `replaceTop(NONEMPTY_ARRAY);` |
| 8 | 3 | JsonWriter.java:633 | 0.060634 | `newline();` |
| 8 | 3 | JsonWriter.java:634 | 0.060634 | `break;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 51 | Excluder.java:50 | 0.0 | `public final class Excluder implements TypeAdapterFactory, Cloneable {` |
| 1 | 51 | Excluder.java:52 | 0.0 | `public static final Excluder DEFAULT = new Excluder();` |
| 1 | 51 | Excluder.java:133 | 0.0 | `if (skipSerialize) {` |
| 1 | 51 | Excluder.java:134 | 0.0 | `out.nullValue();` |
| 1 | 51 | Gson.java:171 | 0.0 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 1 | 51 | Gson.java:185 | 0.0 | `this.serializeNulls = serializeNulls;` |
| 1 | 51 | Gson.java:187 | 0.0 | `this.htmlSafe = htmlSafe;` |
| 1 | 51 | Gson.java:639 | 0.0 | `boolean oldLenient = writer.isLenient();` |
| 1 | 51 | Gson.java:640 | 0.0 | `writer.setLenient(true);` |
| 1 | 51 | Gson.java:641 | 0.0 | `boolean oldHtmlSafe = writer.isHtmlSafe();` |

