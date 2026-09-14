# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeInfoFactory.java', 93), ('TypeInfoFactory.java', 94), ('TypeInfoFactory.java', 95), ('TypeInfoFactory.java', 113), ('TypeInfoFactory.java', 109), ('TypeInfoFactory.java', 110), ('TypeInfoFactory.java', 111), ('TypeInfoFactory.java', 112)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('TypeInfoFactory.java', 93, '->', 80), ('TypeInfoFactory.java', 94, '->', 80), ('TypeInfoFactory.java', 95, '->', 80)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/TypeInfoFactory.java', 109), ('gson/src/main/java/com/google/gson/TypeInfoFactory.java', 110), ('gson/src/main/java/com/google/gson/TypeInfoFactory.java', 111), ('gson/src/main/java/com/google/gson/TypeInfoFactory.java', 112)]

- SBFL   ranked 1816 statement(s)
- Hybrid ranked 13 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TypeInfoFactory.java:97 | 1.0 | `throw new UnsupportedOperationException("Expecting parameterized type, got " + parentType` |
| 2 | 1 | TypeInfoFactory.java:80 | 0.213201 | `if (parentType instanceof ParameterizedType) {` |
| 3 | 1 | TypeInfoFactory.java:79 | 0.185695 | `} else if (typeToEvaluate instanceof TypeVariable<?>) {` |
| 4 | 1 | TypeInfoFactory.java:69 | 0.182574 | `} else if (typeToEvaluate instanceof GenericArrayType) {` |
| 5 | 1 | TypeInfoFactory.java:62 | 0.145865 | `} else if (typeToEvaluate instanceof ParameterizedType) {` |
| 6 | 1 | JsonSerializationVisitor.java:68 | 0.095346 | `assignToRoot(new JsonObject());` |
| 7 | 2 | JsonSerializationVisitor.java:165 | 0.086711 | `return false;` |
| 7 | 2 | JsonSerializationVisitor.java:178 | 0.086711 | `return null;` |
| 9 | 2 | DisjunctionExclusionStrategy.java:41 | 0.074536 | `return false;` |
| 9 | 2 | ObjectNavigator.java:156 | 0.074536 | `TypeInfo fieldTypeInfo = TypeInfoFactory.getTypeInfoForField(f, objTypePair.type);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gson.java:151 | 0.408248 | `this(DEFAULT_EXCLUSION_STRATEGY, DEFAULT_EXCLUSION_STRATEGY, DEFAULT_NAMING_POLICY,` |
| 2 | 12 | Gson.java:203 | 0.0 | `if (src == null) {` |
| 2 | 12 | Gson.java:206 | 0.0 | `return toJsonTree(src, src.getClass());` |
| 2 | 12 | Gson.java:226 | 0.0 | `if (src == null) {` |
| 2 | 12 | Gson.java:231 | 0.0 | `return context.serialize(src, typeOfSrc, true);` |
| 2 | 12 | Gson.java:248 | 0.0 | `if (src == null) {` |
| 2 | 12 | Gson.java:251 | 0.0 | `return toJson(src, src.getClass());` |
| 2 | 12 | Gson.java:270 | 0.0 | `StringWriter writer = new StringWriter();` |
| 2 | 12 | Gson.java:272 | 0.0 | `return writer.toString();` |
| 2 | 12 | Gson.java:336 | 0.0 | `StringWriter writer = new StringWriter();` |

