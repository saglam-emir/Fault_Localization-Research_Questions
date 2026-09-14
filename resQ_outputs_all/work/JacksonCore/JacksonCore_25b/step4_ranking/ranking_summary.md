# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ReaderBasedJsonParser.java', 1963)]

Ground_Truth_Answerable: True

- SBFL   ranked 10914 statement(s)
- Hybrid ranked 1934 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | ReaderBasedJsonParser.java:1805 | 0.316228 | `int start = _inputPtr-1;` |
| 1 | 13 | ReaderBasedJsonParser.java:1806 | 0.316228 | `_inputPtr = ptr;` |
| 1 | 13 | ReaderBasedJsonParser.java:1807 | 0.316228 | `return _handleOddName2(start, hash, codes);` |
| 1 | 13 | ReaderBasedJsonParser.java:1950 | 0.316228 | `_textBuffer.resetWithShared(_inputBuffer, startPtr, (_inputPtr - startPtr));` |
| 1 | 13 | ReaderBasedJsonParser.java:1951 | 0.316228 | `char[] outBuf = _textBuffer.getCurrentSegment();` |
| 1 | 13 | ReaderBasedJsonParser.java:1952 | 0.316228 | `int outPtr = _textBuffer.getCurrentSegmentSize();` |
| 1 | 13 | ReaderBasedJsonParser.java:1953 | 0.316228 | `final int maxCode = codes.length;` |
| 1 | 13 | ReaderBasedJsonParser.java:1956 | 0.316228 | `if (_inputPtr >= _inputEnd) {` |
| 1 | 13 | ReaderBasedJsonParser.java:1957 | 0.316228 | `if (!_loadMore()) { // acceptable for now (will error out later)` |
| 1 | 13 | ReaderBasedJsonParser.java:1961 | 0.316228 | `char c = _inputBuffer[_inputPtr];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonFactory.java:581 | 1.0 | `return state ? enable(f) : disable(f);` |
| 1 | 3 | JsonFactory.java:589 | 1.0 | `_parserFeatures |= f.getMask();` |
| 1 | 3 | JsonParser.java:102 | 1.0 | `ALLOW_UNQUOTED_FIELD_NAMES(false),` |
| 4 | 4 | ReaderBasedJsonParser.java:2344 | 0.160128 | `if (i > INT_SPACE) {` |
| 4 | 4 | ReaderBasedJsonParser.java:2362 | 0.160128 | `while (_inputPtr < _inputEnd) {` |
| 4 | 4 | ReaderBasedJsonParser.java:2363 | 0.160128 | `i = (int) _inputBuffer[_inputPtr++];` |
| 4 | 4 | ReaderBasedJsonParser.java:2369 | 0.160128 | `return i;` |
| 8 | 4 | ReaderBasedJsonParser.java:243 | 0.125 | `int count = _reader.read(_inputBuffer, 0, _inputBuffer.length);` |
| 8 | 4 | ReaderBasedJsonParser.java:245 | 0.125 | `_inputPtr = 0;` |
| 8 | 4 | ReaderBasedJsonParser.java:246 | 0.125 | `_inputEnd = count;` |

