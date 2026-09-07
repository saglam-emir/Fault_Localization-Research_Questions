# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ParserMinimalBase.java', 392), ('ParserMinimalBase.java', 400), ('ReaderBasedJsonParser.java', 253), ('ReaderBasedJsonParser.java', 266), ('UTF8StreamJsonParser.java', 305), ('UTF8StreamJsonParser.java', 319)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/base/ParserMinimalBase.java', 392), ('src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java', 266), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 319)]

- SBFL   ranked 6373 statement(s)
- Hybrid ranked 95 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | JsonToken.java:199 | 1.0 | `public final boolean isScalarValue() { return _isScalar; }` |
| 1 | 4 | ParserMinimalBase.java:397 | 1.0 | `if (_currToken == JsonToken.VALUE_STRING) {` |
| 1 | 4 | ParserMinimalBase.java:400 | 1.0 | `if (_currToken == null || _currToken == JsonToken.VALUE_NULL || !_currToken.isScalarValue()) {` |
| 1 | 4 | ParserMinimalBase.java:401 | 1.0 | `return defaultValue;` |
| 5 | 4 | ReaderBasedJsonParser.java:246 | 0.707107 | `if (_currToken == JsonToken.VALUE_STRING) {` |
| 5 | 4 | ReaderBasedJsonParser.java:253 | 0.707107 | `return super.getValueAsString(null);` |
| 5 | 4 | UTF8StreamJsonParser.java:298 | 0.707107 | `if (_currToken == JsonToken.VALUE_STRING) {` |
| 5 | 4 | UTF8StreamJsonParser.java:305 | 0.707107 | `return super.getValueAsString(null);` |
| 9 | 1 | UTF8StreamJsonParser.java:369 | 0.223607 | `return _parsingContext.getCurrentName();` |
| 10 | 3 | JsonToken.java:166 | 0.213201 | `public final int id() { return _id; }` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 95 | ByteQuadsCanonicalizer.java:239 | 1.0 | `private ByteQuadsCanonicalizer(int sz, boolean intern, int seed, boolean failOnDoS) {` |
| 1 | 95 | ByteQuadsCanonicalizer.java:240 | 1.0 | `_parent = null;` |
| 1 | 95 | ByteQuadsCanonicalizer.java:241 | 1.0 | `_seed = seed;` |
| 1 | 95 | ByteQuadsCanonicalizer.java:242 | 1.0 | `_intern = intern;` |
| 1 | 95 | ByteQuadsCanonicalizer.java:243 | 1.0 | `_failOnDoS = failOnDoS;` |
| 1 | 95 | ByteQuadsCanonicalizer.java:258 | 1.0 | `_tableInfo = new AtomicReference<TableInfo>(TableInfo.createInitial(sz));` |
| 1 | 95 | ByteQuadsCanonicalizer.java:305 | 1.0 | `long now = System.currentTimeMillis();` |
| 1 | 95 | ByteQuadsCanonicalizer.java:307 | 1.0 | `int seed = (((int) now) + ((int) (now >>> 32))) | 1;` |
| 1 | 95 | ByteQuadsCanonicalizer.java:308 | 1.0 | `return createRoot(seed);` |
| 1 | 95 | ByteQuadsCanonicalizer.java:316 | 1.0 | `return new ByteQuadsCanonicalizer(DEFAULT_T_SIZE, true, seed, true);` |

