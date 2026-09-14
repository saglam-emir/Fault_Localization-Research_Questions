# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonWriteContext.java', 169)]

Ground_Truth_Answerable: True

- SBFL   ranked 4649 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UTF8JsonGenerator.java:1039 | 0.408248 | `_outputStream.flush();` |
| 2 | 7 | UTF8JsonGenerator.java:1036 | 0.353553 | `_flushBuffer();` |
| 2 | 7 | UTF8JsonGenerator.java:1037 | 0.353553 | `if (_outputStream != null) {` |
| 2 | 7 | UTF8JsonGenerator.java:1038 | 0.353553 | `if (isEnabled(Feature.FLUSH_PASSED_TO_STREAM)) {` |
| 2 | 7 | WriterBasedJsonGenerator.java:833 | 0.353553 | `_flushBuffer();` |
| 2 | 7 | WriterBasedJsonGenerator.java:834 | 0.353553 | `if (_writer != null) {` |
| 2 | 7 | WriterBasedJsonGenerator.java:835 | 0.353553 | `if (isEnabled(Feature.FLUSH_PASSED_TO_STREAM)) {` |
| 2 | 7 | WriterBasedJsonGenerator.java:836 | 0.353553 | `_writer.flush();` |
| 9 | 7 | UTF8JsonGenerator.java:431 | 0.25 | `text.getChars(0, len, _charBuffer, 0);` |
| 9 | 7 | UTF8JsonGenerator.java:433 | 0.25 | `if (len > _outputMaxContiguous) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | BytesToNameCanonicalizer.java:288 | 1.0 | `_tableInfo = new AtomicReference<TableInfo>(initTableInfo(sz));` |
| 1 | 7 | BytesToNameCanonicalizer.java:325 | 1.0 | `return new TableInfo(0, // count` |
| 1 | 7 | BytesToNameCanonicalizer.java:353 | 1.0 | `return createRoot(seed);` |
| 1 | 7 | BytesToNameCanonicalizer.java:361 | 1.0 | `return new BytesToNameCanonicalizer(DEFAULT_T_SIZE, true, seed, true);` |
| 1 | 7 | JsonFactory.java:175 | 1.0 | `final protected static ThreadLocal<SoftReference<BufferRecycler>> _recyclerRef` |
| 1 | 7 | JsonFactory.java:192 | 1.0 | `protected final transient BytesToNameCanonicalizer _rootByteSymbols = BytesToNameCanonicalizer.createRoot();` |
| 1 | 7 | JsonFactory.java:268 | 1.0 | `public JsonFactory() { this(null); }` |

