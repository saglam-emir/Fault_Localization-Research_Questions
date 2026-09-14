# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TextBuffer.java', 307)]

Ground_Truth_Answerable: True

- SBFL   ranked 6024 statement(s)
- Hybrid ranked 142 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TextBuffer.java:307 | 0.140028 | `if (!_hasSegments)  return _currentSegment;` |
| 2 | 2 | TextBuffer.java:302 | 0.137361 | `if (_resultArray != null)  return _resultArray;` |
| 2 | 2 | TextBuffer.java:303 | 0.137361 | `if (_resultString != null) {` |
| 4 | 1 | TextBuffer.java:301 | 0.121268 | `if (_inputStart >= 0) return _inputBuffer;` |
| 5 | 7 | TextBuffer.java:156 | 0.097129 | `_inputStart = -1; // indicates shared buffer not used` |
| 5 | 7 | TextBuffer.java:157 | 0.097129 | `_currentSize = 0;` |
| 5 | 7 | TextBuffer.java:158 | 0.097129 | `_inputLen = 0;` |
| 5 | 7 | TextBuffer.java:160 | 0.097129 | `_inputBuffer = null;` |
| 5 | 7 | TextBuffer.java:161 | 0.097129 | `_resultString = null;` |
| 5 | 7 | TextBuffer.java:162 | 0.097129 | `_resultArray = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | TextBuffer.java:156 | 1.0 | `_inputStart = -1; // indicates shared buffer not used` |
| 1 | 10 | TextBuffer.java:157 | 1.0 | `_currentSize = 0;` |
| 1 | 10 | TextBuffer.java:158 | 1.0 | `_inputLen = 0;` |
| 1 | 10 | TextBuffer.java:160 | 1.0 | `_inputBuffer = null;` |
| 1 | 10 | TextBuffer.java:161 | 1.0 | `_resultString = null;` |
| 1 | 10 | TextBuffer.java:162 | 1.0 | `_resultArray = null;` |
| 1 | 10 | TextBuffer.java:301 | 1.0 | `if (_inputStart >= 0) return _inputBuffer;` |
| 1 | 10 | TextBuffer.java:302 | 1.0 | `if (_resultArray != null)  return _resultArray;` |
| 1 | 10 | TextBuffer.java:303 | 1.0 | `if (_resultString != null) {` |
| 1 | 10 | TextBuffer.java:307 | 1.0 | `if (!_hasSegments)  return _currentSegment;` |

