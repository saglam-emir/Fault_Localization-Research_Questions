# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ReflectiveTypeAdapterFactory.java', 122), ('ReflectiveTypeAdapterFactory.java', 123)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ReflectiveTypeAdapterFactory.java', 123, '->', 122)]

Ground_Truth_Answerable: True

- SBFL   ranked 2698 statement(s)
- Hybrid ranked 188 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:59 | 0.288675 | `Class<TypeAdapterFactory> typeAdapterFactory = (Class<TypeAdapterFactory>) value;` |
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:60 | 0.288675 | `typeAdapter = constructorConstructor.get(TypeToken.get(typeAdapterFactory))` |
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:63 | 0.288675 | `} else {` |
| 4 | 1 | ReflectiveTypeAdapterFactory.java:111 | 0.267261 | `mapped = getTypeAdapter(constructorConstructor, context, fieldType, annotation);` |
| 5 | 5 | JsonAdapterAnnotationTypeAdapterFactory.java:53 | 0.171499 | `Class<?> value = annotation.value();` |
| 5 | 5 | JsonAdapterAnnotationTypeAdapterFactory.java:55 | 0.171499 | `if (TypeAdapter.class.isAssignableFrom(value)) {` |
| 5 | 5 | JsonAdapterAnnotationTypeAdapterFactory.java:67 | 0.171499 | `if (typeAdapter != null) {` |
| 5 | 5 | JsonAdapterAnnotationTypeAdapterFactory.java:68 | 0.171499 | `typeAdapter = typeAdapter.nullSafe();` |
| 5 | 5 | JsonAdapterAnnotationTypeAdapterFactory.java:70 | 0.171499 | `return typeAdapter;` |
| 10 | 1 | TypeAdapters.java:328 | 0.097129 | `out.value(value);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gson.java:580 | 0.088388 | `return toJson(src, src.getClass());` |
| 2 | 1 | Gson.java:577 | 0.086711 | `if (src == null) {` |
| 3 | 2 | Gson.java:599 | 0.078326 | `StringWriter writer = new StringWriter();` |
| 3 | 2 | Gson.java:601 | 0.078326 | `return writer.toString();` |
| 5 | 184 | CollectionTypeAdapterFactory.java:61 | 0.0 | `private static final class Adapter<E> extends TypeAdapter<Collection<E>> {` |
| 5 | 184 | Excluder.java:133 | 0.0 | `if (skipSerialize) {` |
| 5 | 184 | Excluder.java:134 | 0.0 | `out.nullValue();` |
| 5 | 184 | Gson.java:173 | 0.0 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 5 | 184 | Gson.java:535 | 0.0 | `if (src == null) {` |
| 5 | 184 | Gson.java:538 | 0.0 | `return toJsonTree(src, src.getClass());` |

