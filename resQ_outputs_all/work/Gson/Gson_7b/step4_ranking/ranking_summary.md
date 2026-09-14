# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonReader.java', 954), ('JsonReader.java', 956), ('JsonReader.java', 1182), ('JsonReader.java', 1184)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JsonReader.java', 956, '->', 951), ('JsonReader.java', 1184, '->', 1179)]

Ground_Truth_Answerable: True

- SBFL   ranked 2815 statement(s)
- Hybrid ranked 645 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | JsonReader.java:1607 | 0.377964 | `} else if (p == PEEKED_UNQUOTED_NAME) {` |
| 1 | 2 | JsonReader.java:1608 | 0.377964 | `reader.peeked = PEEKED_UNQUOTED;` |
| 3 | 1 | JsonReader.java:1193 | 0.353553 | `throw new IllegalStateException("Expected an int but was " + peek()` |
| 4 | 2 | ConstructorConstructor.java:201 | 0.288675 | `return (T) new LinkedHashMap<Object, Object>();` |
| 4 | 2 | JsonReader.java:965 | 0.288675 | `throw new IllegalStateException("Expected a long but was " + peek()` |
| 6 | 1 | ConstructorConstructor.java:199 | 0.258199 | `return new ObjectConstructor<T>() {` |
| 7 | 2 | JsonReader.java:1182 | 0.25 | `} else if (p == PEEKED_SINGLE_QUOTED || p == PEEKED_DOUBLE_QUOTED) {` |
| 7 | 2 | JsonReader.java:1605 | 0.25 | `} else if (p == PEEKED_SINGLE_QUOTED_NAME) {` |
| 9 | 1 | JsonReader.java:1179 | 0.208514 | `if (p == PEEKED_NUMBER) {` |
| 10 | 2 | Gson.java:891 | 0.196116 | `} catch (IllegalStateException e) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Gson.java:187 | 0.816497 | `this(Excluder.DEFAULT, FieldNamingPolicy.IDENTITY,` |
| 2 | 644 | ConstructorConstructor.java:51 | 0.0 | `public ConstructorConstructor(Map<Type, InstanceCreator<?>> instanceCreators) {` |
| 2 | 644 | ConstructorConstructor.java:52 | 0.0 | `this.instanceCreators = instanceCreators;` |
| 2 | 644 | ConstructorConstructor.java:56 | 0.0 | `final Type type = typeToken.getType();` |
| 2 | 644 | ConstructorConstructor.java:57 | 0.0 | `final Class<? super T> rawType = typeToken.getRawType();` |
| 2 | 644 | ConstructorConstructor.java:62 | 0.0 | `final InstanceCreator<T> typeCreator = (InstanceCreator<T>) instanceCreators.get(type);` |
| 2 | 644 | ConstructorConstructor.java:63 | 0.0 | `if (typeCreator != null) {` |
| 2 | 644 | ConstructorConstructor.java:73 | 0.0 | `final InstanceCreator<T> rawTypeCreator =` |
| 2 | 644 | ConstructorConstructor.java:75 | 0.0 | `if (rawTypeCreator != null) {` |
| 2 | 644 | ConstructorConstructor.java:83 | 0.0 | `ObjectConstructor<T> defaultConstructor = newDefaultConstructor(rawType);` |

