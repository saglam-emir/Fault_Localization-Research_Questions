# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NonBlockingJsonParser.java', 108)]

Ground_Truth_Answerable: True

- SBFL   ranked 11137 statement(s)
- Hybrid ranked 489 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | ByteSourceJsonBootstrapper.java:151 | 0.243432 | `int i16 = ((_inputBuffer[_inputPtr] & 0xFF) << 8)` |
| 1 | 2 | ByteSourceJsonBootstrapper.java:153 | 0.243432 | `if (checkUTF16(i16)) {` |
| 3 | 1 | ByteSourceJsonBootstrapper.java:525 | 0.239046 | `return false;` |
| 4 | 3 | UTF8DataInputJsonParser.java:165 | 0.13408 | `protected void _closeInput() throws IOException { }` |
| 4 | 3 | UTF8DataInputJsonParser.java:176 | 0.13408 | `super._releaseBuffers();` |
| 4 | 3 | UTF8DataInputJsonParser.java:178 | 0.13408 | `_symbols.release();` |
| 7 | 116 | ByteQuadsCanonicalizer.java:222 | 0.13375 | `private ByteQuadsCanonicalizer(int sz, boolean intern, int seed, boolean failOnDoS) {` |
| 7 | 116 | ByteQuadsCanonicalizer.java:223 | 0.13375 | `_parent = null;` |
| 7 | 116 | ByteQuadsCanonicalizer.java:224 | 0.13375 | `_seed = seed;` |
| 7 | 116 | ByteQuadsCanonicalizer.java:225 | 0.13375 | `_intern = intern;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | NonBlockingJsonParserBase.java:344 | 1.0 | `int row = Math.max(_currInputRow, _currInputRowAlt);` |
| 2 | 56 | JsonFactory.java:1087 | 0.707107 | `_requireJSONFactory("Non-blocking source not (yet?) supported for this format (%s)");` |
| 2 | 56 | JsonFactory.java:1088 | 0.707107 | `IOContext ctxt = _createNonBlockingContext(null);` |
| 2 | 56 | JsonFactory.java:1089 | 0.707107 | `ByteQuadsCanonicalizer can = _byteSymbolCanonicalizer.makeChild(_factoryFeatures);` |
| 2 | 56 | JsonFactory.java:1090 | 0.707107 | `return new NonBlockingJsonParser(ctxt, _parserFeatures, can);` |
| 2 | 56 | JsonFactory.java:1697 | 0.707107 | `BufferRecycler recycler = new BufferRecycler();` |
| 2 | 56 | JsonFactory.java:1698 | 0.707107 | `return new IOContext(recycler, srcRef, false);` |
| 2 | 56 | JsonReadContext.java:114 | 0.707107 | `JsonReadContext ctxt = _child;` |
| 2 | 56 | JsonReadContext.java:115 | 0.707107 | `if (ctxt == null) {` |
| 2 | 56 | JsonReadContext.java:116 | 0.707107 | `_child = ctxt = new JsonReadContext(this,` |

