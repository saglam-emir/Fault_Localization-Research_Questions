# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeAdapters.java', 833), ('TypeAdapters.java', 835)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/bind/TypeAdapters.java', 835)]

- SBFL   ranked 2656 statement(s)
- Hybrid ranked 365 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TypeAdapters.java:833 | 0.196116 | `return (TypeAdapter<T2>) typeAdapter;` |
| 2 | 1 | JsonReader.java:575 | 0.114708 | `checkLenient();` |
| 3 | 1 | TypeAdapters.java:647 | 0.1 | `return new JsonPrimitive(in.nextString());` |
| 4 | 1 | TypeAdapters.java:645 | 0.082199 | `switch (in.peek()) {` |
| 5 | 1 | TypeAdapters.java:98 | 0.079057 | `switch (tokenType) {` |
| 6 | 2 | JsonReader.java:574 | 0.06868 | `if (stackSize == 1) {` |
| 6 | 2 | JsonReader.java:577 | 0.06868 | `return peeked = PEEKED_DOUBLE_QUOTED;` |
| 8 | 1 | JsonReader.java:827 | 0.067116 | `result = nextQuotedValue('"');` |
| 9 | 1 | Gson.java:177 | 0.065094 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 10 | 2 | JsonPrimitive.java:64 | 0.064018 | `public JsonPrimitive(String string) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gson.java:177 | 0.090536 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 2 | 364 | ArrayTypeAdapter.java:39 | 0.0 | `public static final TypeAdapterFactory FACTORY = new TypeAdapterFactory() {` |
| 2 | 364 | ArrayTypeAdapter.java:42 | 0.0 | `Type type = typeToken.getType();` |
| 2 | 364 | ArrayTypeAdapter.java:43 | 0.0 | `if (!(type instanceof GenericArrayType || type instanceof Class && ((Class<?>) type).isArray())) {` |
| 2 | 364 | ArrayTypeAdapter.java:47 | 0.0 | `Type componentType = $Gson$Types.getArrayComponentType(type);` |
| 2 | 364 | ArrayTypeAdapter.java:48 | 0.0 | `TypeAdapter<?> componentTypeAdapter = gson.getAdapter(TypeToken.get(componentType));` |
| 2 | 364 | ArrayTypeAdapter.java:49 | 0.0 | `return new ArrayTypeAdapter(` |
| 2 | 364 | ArrayTypeAdapter.java:57 | 0.0 | `public ArrayTypeAdapter(Gson context, TypeAdapter<E> componentTypeAdapter, Class<E> componentType) {` |
| 2 | 364 | ArrayTypeAdapter.java:58 | 0.0 | `this.componentTypeAdapter =` |
| 2 | 364 | ArrayTypeAdapter.java:60 | 0.0 | `this.componentType = componentType;` |

