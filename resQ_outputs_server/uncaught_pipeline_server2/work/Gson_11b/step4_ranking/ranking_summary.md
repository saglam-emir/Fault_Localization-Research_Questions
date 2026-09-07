# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeAdapters.java', 371)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TypeAdapters.java', 371, '->', 370)]

Ground_Truth_Answerable: True

- SBFL   ranked 2796 statement(s)
- Hybrid ranked 157 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TypeAdapters.java:373 | 0.408248 | `throw new JsonSyntaxException("Expecting number, got: " + jsonToken);` |
| 2 | 4 | JsonParseException.java:42 | 0.288675 | `super(msg);` |
| 2 | 4 | JsonSyntaxException.java:30 | 0.288675 | `super(msg);` |
| 2 | 4 | TypeAdapters.java:365 | 0.288675 | `JsonToken jsonToken = in.peek();` |
| 2 | 4 | TypeAdapters.java:366 | 0.288675 | `switch (jsonToken) {` |
| 6 | 1 | JsonReader.java:1571 | 0.090536 | `return;` |
| 7 | 2 | JsonReader.java:1279 | 0.076249 | `limit -= pos;` |
| 7 | 2 | JsonReader.java:1280 | 0.076249 | `System.arraycopy(buffer, pos, buffer, 0, limit);` |
| 9 | 1 | JsonReader.java:570 | 0.065938 | `return peeked = PEEKED_DOUBLE_QUOTED;` |
| 10 | 1 | Gson.java:174 | 0.063119 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gson.java:174 | 1.0 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 2 | 156 | Excluder.java:125 | 0.0 | `if (skipDeserialize) {` |
| 2 | 156 | Excluder.java:127 | 0.0 | `return null;` |
| 2 | 156 | Gson.java:334 | 0.0 | `return new TypeAdapter<Number>() {` |
| 2 | 156 | Gson.java:336 | 0.0 | `if (in.peek() == JsonToken.NULL) {` |
| 2 | 156 | Gson.java:340 | 0.0 | `return in.nextLong();` |
| 2 | 156 | Gson.java:728 | 0.0 | `JsonReader jsonReader = new JsonReader(reader);` |
| 2 | 156 | Gson.java:773 | 0.0 | `Object object = fromJson(json, (Type) classOfT);` |
| 2 | 156 | Gson.java:774 | 0.0 | `return Primitives.wrap(classOfT).cast(object);` |
| 2 | 156 | Gson.java:797 | 0.0 | `if (json == null) {` |

