# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FilteringParserDelegate.java', 227), ('FilteringParserDelegate.java', 228), ('FilteringParserDelegate.java', 230)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/filter/FilteringParserDelegate.java', 227), ('src/main/java/com/fasterxml/jackson/core/filter/FilteringParserDelegate.java', 228), ('src/main/java/com/fasterxml/jackson/core/filter/FilteringParserDelegate.java', 230)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 1247 statement(s)
- Hybrid ranked 7 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | SerializedString.java:87 | 0.707107 | `public final String getValue() { return _value; }` |
| 1 | 10 | WriterBasedJsonGenerator.java:406 | 0.707107 | `int len = text.length();` |
| 1 | 10 | WriterBasedJsonGenerator.java:407 | 0.707107 | `int room = _outputEnd - _outputTail;` |
| 1 | 10 | WriterBasedJsonGenerator.java:409 | 0.707107 | `if (room == 0) {` |
| 1 | 10 | WriterBasedJsonGenerator.java:414 | 0.707107 | `if (room >= len) {` |
| 1 | 10 | WriterBasedJsonGenerator.java:415 | 0.707107 | `text.getChars(0, len, _outputBuffer, _outputTail);` |
| 1 | 10 | WriterBasedJsonGenerator.java:416 | 0.707107 | `_outputTail += len;` |
| 1 | 10 | WriterBasedJsonGenerator.java:777 | 0.707107 | `if (_rootValueSeparator != null) {` |
| 1 | 10 | WriterBasedJsonGenerator.java:778 | 0.707107 | `writeRaw(_rootValueSeparator.getValue());` |
| 1 | 10 | WriterBasedJsonGenerator.java:780 | 0.707107 | `return;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ByteQuadsCanonicalizer.java:241 | 0.0 | `_tableInfo = new AtomicReference<TableInfo>(TableInfo.createInitial(sz));` |
| 1 | 7 | ByteQuadsCanonicalizer.java:291 | 0.0 | `return createRoot(seed);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:299 | 0.0 | `return new ByteQuadsCanonicalizer(DEFAULT_T_SIZE, true, seed, true);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1262 | 0.0 | `return new TableInfo(sz, // hashSize` |
| 1 | 7 | JsonFactory.java:187 | 0.0 | `final protected static ThreadLocal<SoftReference<BufferRecycler>> _recyclerRef` |
| 1 | 7 | JsonFactory.java:206 | 0.0 | `protected final transient ByteQuadsCanonicalizer _byteSymbolCanonicalizer = ByteQuadsCanonicalizer.createRoot();` |
| 1 | 7 | JsonFactory.java:282 | 0.0 | `public JsonFactory() { this(null); }` |

