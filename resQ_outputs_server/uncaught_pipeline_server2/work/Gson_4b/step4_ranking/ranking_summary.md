# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonReader.java', 574), ('JsonReader.java', 575), ('JsonReader.java', 576), ('JsonReader.java', 585), ('JsonReader.java', 586), ('JsonReader.java', 587), ('JsonWriter.java', 325), ('JsonWriter.java', 418), ('JsonWriter.java', 435), ('JsonWriter.java', 454), ('JsonWriter.java', 466), ('JsonWriter.java', 483), ('JsonWriter.java', 495), ('JsonWriter.java', 518), ('JsonWriter.java', 613), ('JsonWriter.java', 622), ('JsonWriter.java', 623), ('JsonWriter.java', 624), ('JsonWriter.java', 625)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JsonReader.java', 574, '->', 573), ('JsonWriter.java', 613, '->', 612), ('JsonWriter.java', 622, '->', 621), ('JsonWriter.java', 624, '->', 623)]

Ground_Truth_Answerable: True

- SBFL   ranked 2842 statement(s)
- Hybrid ranked 565 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | JsonWriter.java:623 | 0.5 | `throw new IllegalStateException(` |
| 2 | 1 | JsonReader.java:1422 | 0.182574 | `throw syntaxError("Use JsonReader.setLenient(true) to accept malformed JSON");` |
| 3 | 1 | JsonReader.java:1572 | 0.13484 | `throw new MalformedJsonException(message` |
| 4 | 1 | MalformedJsonException.java:29 | 0.133631 | `super(msg);` |
| 5 | 1 | JsonReader.java:586 | 0.109764 | `checkLenient();` |
| 6 | 1 | JsonReader.java:854 | 0.1066 | `p = doPeek();` |
| 7 | 2 | JsonReader.java:1317 | 0.099015 | `return lineNumber + 1;` |
| 7 | 2 | JsonReader.java:1321 | 0.099015 | `return pos - lineStart + 1;` |
| 9 | 4 | JsonReader.java:1475 | 0.097129 | `StringBuilder result = new StringBuilder().append('$');` |
| 9 | 4 | JsonReader.java:1476 | 0.097129 | `for (int i = 0, size = stackSize; i < size; i++) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | JsonWriter.java:167 | 0.57735 | `private int[] stack = new int[32];` |
| 1 | 8 | JsonWriter.java:168 | 0.57735 | `private int stackSize = 0;` |
| 1 | 8 | JsonWriter.java:170 | 0.57735 | `push(EMPTY_DOCUMENT);` |
| 1 | 8 | JsonWriter.java:182 | 0.57735 | `private String separator = ":";` |
| 1 | 8 | JsonWriter.java:190 | 0.57735 | `private boolean serializeNulls = true;` |
| 1 | 8 | JsonWriter.java:197 | 0.57735 | `public JsonWriter(Writer out) {` |
| 1 | 8 | JsonWriter.java:201 | 0.57735 | `this.out = out;` |
| 1 | 8 | JsonWriter.java:359 | 0.57735 | `stack[stackSize++] = newTop;` |
| 9 | 6 | JsonReader.java:230 | 0.06816 | `private boolean lenient = false;` |
| 9 | 6 | JsonReader.java:242 | 0.06816 | `private int lineNumber = 0;` |

