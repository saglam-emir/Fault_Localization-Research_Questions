# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UTF8StreamJsonParser.java', 125), ('UTF8StreamJsonParser.java', 126)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 125)]

- SBFL   ranked 4575 statement(s)
- Hybrid ranked 364 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | ByteSourceJsonBootstrapper.java:501 | 0.707107 | `count = -1;` |
| 1 | 5 | JsonFactory.java:817 | 0.707107 | `IOContext ctxt = _createContext(data, true);` |
| 1 | 5 | JsonFactory.java:819 | 0.707107 | `if (_inputDecorator != null) {` |
| 1 | 5 | JsonFactory.java:825 | 0.707107 | `return _createParser(data, offset, len, ctxt);` |
| 1 | 5 | JsonLocation.java:89 | 0.707107 | `return _totalBytes;` |
| 6 | 5 | ParserBase.java:422 | 0.57735 | `public long getTokenCharacterOffset() { return _tokenInputTotal; }` |
| 6 | 5 | ParserBase.java:423 | 0.57735 | `public int getTokenLineNr() { return _tokenInputRow; }` |
| 6 | 5 | ParserBase.java:426 | 0.57735 | `int col = _tokenInputCol;` |
| 6 | 5 | ParserBase.java:427 | 0.57735 | `return (col < 0) ? col : (col + 1);` |
| 6 | 5 | UTF8StreamJsonParser.java:606 | 0.57735 | `return new JsonLocation(_ioContext.getSourceReference(),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonFactory.java:817 | 1.0 | `IOContext ctxt = _createContext(data, true);` |
| 1 | 3 | JsonFactory.java:819 | 1.0 | `if (_inputDecorator != null) {` |
| 1 | 3 | JsonFactory.java:825 | 1.0 | `return _createParser(data, offset, len, ctxt);` |
| 4 | 1 | UTF8StreamJsonParser.java:606 | 0.353553 | `return new JsonLocation(_ioContext.getSourceReference(),` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:96 | 0.333333 | `_context = ctxt;` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:97 | 0.333333 | `_in = null;` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:98 | 0.333333 | `_inputBuffer = inputBuffer;` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:99 | 0.333333 | `_inputPtr = inputStart;` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:100 | 0.333333 | `_inputEnd = (inputStart + inputLen);` |
| 5 | 8 | ByteSourceJsonBootstrapper.java:102 | 0.333333 | `_inputProcessed = -inputStart;` |

