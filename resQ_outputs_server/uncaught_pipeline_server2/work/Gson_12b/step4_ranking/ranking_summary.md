# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonTreeReader.java', 262), ('JsonTreeReader.java', 263), ('JsonTreeReader.java', 264), ('JsonTreeReader.java', 265)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JsonTreeReader.java', 263, '->', 257)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('gson/src/main/java/com/google/gson/internal/bind/JsonTreeReader.java', 265)]

- SBFL   ranked 2803 statement(s)
- Hybrid ranked 22 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | LinkedTreeMap.java:382 | 0.57735 | `pivotLeft.parent = root;` |
| 2 | 3 | JsonTreeReader.java:257 | 0.436436 | `if (peek() == JsonToken.NAME) {` |
| 2 | 3 | JsonTreeReader.java:261 | 0.436436 | `popStack();` |
| 2 | 3 | JsonTreeReader.java:262 | 0.436436 | `pathNames[stackSize - 1] = "null";` |
| 5 | 2 | JsonObject.java:101 | 0.408248 | `add(property, createJsonElement(value));` |
| 5 | 2 | LinkedTreeMap.java:326 | 0.408248 | `rotateLeft(node); // AVL right right` |
| 7 | 1 | JsonTreeReader.java:126 | 0.264906 | `return JsonToken.BEGIN_OBJECT;` |
| 8 | 12 | JsonArray.java:67 | 0.258199 | `elements.add(character == null ? JsonNull.INSTANCE : new JsonPrimitive(character));` |
| 8 | 12 | JsonArray.java:85 | 0.258199 | `elements.add(string == null ? JsonNull.INSTANCE : new JsonPrimitive(string));` |
| 8 | 12 | LinkedTreeMap.java:295 | 0.258199 | `assert (parent.right == node);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 22 | JsonReader.java:230 | 1.0 | `private boolean lenient = false;` |
| 1 | 22 | JsonReader.java:238 | 1.0 | `private final char[] buffer = new char[1024];` |
| 1 | 22 | JsonReader.java:239 | 1.0 | `private int pos = 0;` |
| 1 | 22 | JsonReader.java:240 | 1.0 | `private int limit = 0;` |
| 1 | 22 | JsonReader.java:242 | 1.0 | `private int lineNumber = 0;` |
| 1 | 22 | JsonReader.java:243 | 1.0 | `private int lineStart = 0;` |
| 1 | 22 | JsonReader.java:245 | 1.0 | `int peeked = PEEKED_NONE;` |
| 1 | 22 | JsonReader.java:269 | 1.0 | `private int[] stack = new int[32];` |
| 1 | 22 | JsonReader.java:270 | 1.0 | `private int stackSize = 0;` |
| 1 | 22 | JsonReader.java:272 | 1.0 | `stack[stackSize++] = JsonScope.EMPTY_DOCUMENT;` |

