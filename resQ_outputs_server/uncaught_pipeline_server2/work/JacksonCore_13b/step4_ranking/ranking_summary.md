# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonGeneratorImpl.java', 127)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/json/JsonGeneratorImpl.java', 127)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 7049 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | GeneratorBase.java:162 | 1.0 | `final int mask = f.getMask();` |
| 1 | 5 | GeneratorBase.java:163 | 1.0 | `_features &= ~mask;` |
| 1 | 5 | GeneratorBase.java:164 | 1.0 | `if ((mask & DERIVED_FEATURES_MASK) != 0) {` |
| 1 | 5 | GeneratorBase.java:173 | 1.0 | `return this;` |
| 1 | 5 | JsonGeneratorImpl.java:122 | 1.0 | `_cfgUnqNames = false;` |
| 6 | 7 | GeneratorBase.java:143 | 0.447214 | `final int mask = f.getMask();` |
| 6 | 7 | GeneratorBase.java:144 | 0.447214 | `_features |= mask;` |
| 6 | 7 | GeneratorBase.java:145 | 0.447214 | `if ((mask & DERIVED_FEATURES_MASK) != 0) {` |
| 6 | 7 | GeneratorBase.java:157 | 0.447214 | `return this;` |
| 6 | 7 | JsonGeneratorImpl.java:120 | 0.447214 | `super.enable(f);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | ByteQuadsCanonicalizer.java:241 | 1.0 | `_tableInfo = new AtomicReference<TableInfo>(TableInfo.createInitial(sz));` |
| 1 | 7 | ByteQuadsCanonicalizer.java:291 | 1.0 | `return createRoot(seed);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:299 | 1.0 | `return new ByteQuadsCanonicalizer(DEFAULT_T_SIZE, true, seed, true);` |
| 1 | 7 | ByteQuadsCanonicalizer.java:1262 | 1.0 | `return new TableInfo(sz, // hashSize` |
| 1 | 7 | JsonFactory.java:187 | 1.0 | `final protected static ThreadLocal<SoftReference<BufferRecycler>> _recyclerRef` |
| 1 | 7 | JsonFactory.java:206 | 1.0 | `protected final transient ByteQuadsCanonicalizer _byteSymbolCanonicalizer = ByteQuadsCanonicalizer.createRoot();` |
| 1 | 7 | JsonFactory.java:282 | 1.0 | `public JsonFactory() { this(null); }` |

