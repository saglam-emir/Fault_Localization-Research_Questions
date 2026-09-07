# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ConstructorConstructor.java', 36), ('ConstructorConstructor.java', 175)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/ConstructorConstructor.java', 36)]

- SBFL   ranked 2615 statement(s)
- Hybrid ranked 205 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | JsonReader.java:1190 | 0.436436 | `peekedString = nextQuotedValue(p == PEEKED_SINGLE_QUOTED ? '\'' : '"');` |
| 1 | 5 | JsonReader.java:1192 | 0.436436 | `result = Integer.parseInt(peekedString);` |
| 1 | 5 | JsonReader.java:1193 | 0.436436 | `peeked = PEEKED_NONE;` |
| 1 | 5 | JsonReader.java:1194 | 0.436436 | `pathIndices[stackSize - 1]++;` |
| 1 | 5 | JsonReader.java:1195 | 0.436436 | `return result;` |
| 6 | 2 | ConstructorConstructor.java:176 | 0.408248 | `return new ObjectConstructor<T>() {` |
| 6 | 2 | ConstructorConstructor.java:178 | 0.408248 | `return (T) new TreeMap<Object, Object>();` |
| 8 | 1 | JsonReader.java:1189 | 0.320256 | `} else if (p == PEEKED_SINGLE_QUOTED || p == PEEKED_DOUBLE_QUOTED) {` |
| 9 | 1 | JsonReader.java:1611 | 0.280056 | `reader.peeked = PEEKED_DOUBLE_QUOTED;` |
| 10 | 1 | JsonReader.java:1186 | 0.272166 | `if (p == PEEKED_NUMBER) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 20 | Gson.java:112 | 1.0 | `private final ThreadLocal<Map<TypeToken<?>, FutureTypeAdapter<?>>> calls` |
| 1 | 20 | Gson.java:115 | 1.0 | `private final Map<TypeToken<?>, TypeAdapter<?>> typeTokenCache` |
| 1 | 20 | Gson.java:337 | 1.0 | `if (cached != null) {` |
| 1 | 20 | Gson.java:341 | 1.0 | `Map<TypeToken<?>, FutureTypeAdapter<?>> threadCalls = calls.get();` |
| 1 | 20 | Gson.java:343 | 1.0 | `if (threadCalls == null) {` |
| 1 | 20 | Gson.java:344 | 1.0 | `threadCalls = new HashMap<TypeToken<?>, FutureTypeAdapter<?>>();` |
| 1 | 20 | Gson.java:345 | 1.0 | `calls.set(threadCalls);` |
| 1 | 20 | Gson.java:350 | 1.0 | `FutureTypeAdapter<T> ongoingCall = (FutureTypeAdapter<T>) threadCalls.get(type);` |
| 1 | 20 | Gson.java:356 | 1.0 | `FutureTypeAdapter<T> call = new FutureTypeAdapter<T>();` |
| 1 | 20 | Gson.java:357 | 1.0 | `threadCalls.put(type, call);` |

