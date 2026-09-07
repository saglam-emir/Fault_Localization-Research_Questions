# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ReaderBasedJsonParser.java', 1418), ('UTF8StreamJsonParser.java', 1544)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ReaderBasedJsonParser.java', 1418, '->', 1417), ('UTF8StreamJsonParser.java', 1544, '->', 1543)]

Ground_Truth_Answerable: True

- SBFL   ranked 7124 statement(s)
- Hybrid ranked 119 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ReaderBasedJsonParser.java:1266 | 0.447214 | `return _parseNumber2(neg, startPtr);` |
| 2 | 1 | ReaderBasedJsonParser.java:1418 | 0.353553 | `outBuf[outPtr++] = c;` |
| 3 | 6 | ReaderBasedJsonParser.java:1240 | 0.301511 | `_inputPtr = ptr;` |
| 3 | 6 | ReaderBasedJsonParser.java:1241 | 0.301511 | `return _parseFloat(ch, startPtr, ptr, false, intLen);` |
| 3 | 6 | ReaderBasedJsonParser.java:1265 | 0.301511 | `if (ptr >= inputLen) {` |
| 3 | 6 | ReaderBasedJsonParser.java:1268 | 0.301511 | `ch = (int) _inputBuffer[ptr++];` |
| 3 | 6 | ReaderBasedJsonParser.java:1269 | 0.301511 | `if (ch < INT_0 || ch > INT_9) {` |
| 3 | 6 | ReaderBasedJsonParser.java:1272 | 0.301511 | `++fractLen;` |
| 9 | 3 | ReaderBasedJsonParser.java:1258 | 0.288675 | `final int inputLen = _inputEnd;` |
| 9 | 3 | ReaderBasedJsonParser.java:1259 | 0.288675 | `int fractLen = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 119 | BufferRecycler.java:46 | 1.0 | `private final static int[] CHAR_BUFFER_LENGTHS = new int[] { 4000, 4000, 200, 200 };` |
| 1 | 119 | BufferRecycler.java:62 | 1.0 | `this(4, 4);` |
| 1 | 119 | BufferRecycler.java:71 | 1.0 | `protected BufferRecycler(int bbCount, int cbCount) {` |
| 1 | 119 | BufferRecycler.java:72 | 1.0 | `_byteBuffers = new byte[bbCount][];` |
| 1 | 119 | BufferRecycler.java:73 | 1.0 | `_charBuffers = new char[cbCount][];` |
| 1 | 119 | BufferRecycler.java:114 | 1.0 | `return allocCharBuffer(ix, 0);` |
| 1 | 119 | BufferRecycler.java:118 | 1.0 | `final int DEF_SIZE = charBufferLength(ix);` |
| 1 | 119 | BufferRecycler.java:119 | 1.0 | `if (minSize < DEF_SIZE) {` |
| 1 | 119 | BufferRecycler.java:120 | 1.0 | `minSize = DEF_SIZE;` |
| 1 | 119 | BufferRecycler.java:122 | 1.0 | `char[] buffer = _charBuffers[ix];` |

