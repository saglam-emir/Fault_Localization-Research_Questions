# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonAdapterAnnotationTypeAdapterFactory.java', 67), ('JsonAdapterAnnotationTypeAdapterFactory.java', 68)]

Ground_Truth_Answerable: True

- SBFL   ranked 2672 statement(s)
- Hybrid ranked 369 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:59 | 0.516398 | `Class<TypeAdapterFactory> typeAdapterFactory = (Class<TypeAdapterFactory>) value;` |
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:60 | 0.516398 | `typeAdapter = constructorConstructor.get(TypeToken.get(typeAdapterFactory))` |
| 1 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:63 | 0.516398 | `} else {` |
| 4 | 1 | JsonAdapterAnnotationTypeAdapterFactory.java:47 | 0.365148 | `return (TypeAdapter<T>) getTypeAdapter(constructorConstructor, gson, targetType, annotation);` |
| 5 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:53 | 0.298142 | `Class<?> value = annotation.value();` |
| 5 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:55 | 0.298142 | `if (TypeAdapter.class.isAssignableFrom(value)) {` |
| 5 | 3 | JsonAdapterAnnotationTypeAdapterFactory.java:67 | 0.298142 | `typeAdapter = typeAdapter.nullSafe();` |
| 8 | 6 | Gson.java:484 | 0.258199 | `boolean skipPastFound = false;` |
| 8 | 6 | Gson.java:488 | 0.258199 | `if (!factories.contains(skipPast)) skipPastFound = true;` |
| 8 | 6 | Gson.java:490 | 0.258199 | `for (TypeAdapterFactory factory : factories) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | Excluder.java:113 | 0.176777 | `final boolean skipSerialize = excludeClass(rawType, true);` |
| 1 | 9 | Excluder.java:114 | 0.176777 | `final boolean skipDeserialize = excludeClass(rawType, false);` |
| 1 | 9 | Excluder.java:116 | 0.176777 | `if (!skipSerialize && !skipDeserialize) {` |
| 1 | 9 | Excluder.java:120 | 0.176777 | `return new TypeAdapter<T>() {` |
| 1 | 9 | Excluder.java:192 | 0.176777 | `if (version != Excluder.IGNORE_VERSIONS` |
| 1 | 9 | Excluder.java:197 | 0.176777 | `if (!serializeInnerClasses && isInnerClass(clazz)) {` |
| 1 | 9 | Excluder.java:201 | 0.176777 | `if (isAnonymousOrLocal(clazz)) {` |
| 1 | 9 | Excluder.java:202 | 0.176777 | `return true;` |
| 1 | 9 | Excluder.java:216 | 0.176777 | `return !Enum.class.isAssignableFrom(clazz)` |
| 10 | 2 | Gson.java:261 | 0.14825 | `factories.add(new ReflectiveTypeAdapterFactory(` |

