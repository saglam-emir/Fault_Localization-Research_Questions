# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonWriter.java', 495)]

Ground_Truth_Answerable: True

- SBFL   ranked 2938 statement(s)
- Hybrid ranked 51 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | JsonWriter.java:496 | 0.5 | `throw new IllegalArgumentException("Numeric values must be finite, but was " + value);` |
| 2 | 2 | JsonWriter.java:494 | 0.288675 | `writeDeferredName();` |
| 2 | 2 | JsonWriter.java:495 | 0.288675 | `if (Double.isNaN(value) || Double.isInfinite(value)) {` |
| 4 | 2 | JsonWriter.java:287 | 0.056433 | `writeDeferredName();` |
| 4 | 2 | JsonWriter.java:288 | 0.056433 | `return open(EMPTY_ARRAY, "[");` |
| 6 | 4 | JsonWriter.java:325 | 0.039528 | `beforeValue();` |
| 6 | 4 | JsonWriter.java:326 | 0.039528 | `push(empty);` |
| 6 | 4 | JsonWriter.java:327 | 0.039528 | `out.write(openBracket);` |
| 6 | 4 | JsonWriter.java:328 | 0.039528 | `return this;` |
| 10 | 1 | JsonWriter.java:235 | 0.034964 | `this.lenient = lenient;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 19 | JsonWriter.java:167 | 0.447214 | `private int[] stack = new int[32];` |
| 1 | 19 | JsonWriter.java:168 | 0.447214 | `private int stackSize = 0;` |
| 1 | 19 | JsonWriter.java:170 | 0.447214 | `push(EMPTY_DOCUMENT);` |
| 1 | 19 | JsonWriter.java:182 | 0.447214 | `private String separator = ":";` |
| 1 | 19 | JsonWriter.java:190 | 0.447214 | `private boolean serializeNulls = true;` |
| 1 | 19 | JsonWriter.java:197 | 0.447214 | `public JsonWriter(Writer out) {` |
| 1 | 19 | JsonWriter.java:201 | 0.447214 | `this.out = out;` |
| 1 | 19 | JsonWriter.java:235 | 0.447214 | `this.lenient = lenient;` |
| 1 | 19 | JsonWriter.java:287 | 0.447214 | `writeDeferredName();` |
| 1 | 19 | JsonWriter.java:288 | 0.447214 | `return open(EMPTY_ARRAY, "[");` |

