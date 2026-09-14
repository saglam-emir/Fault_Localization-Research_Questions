# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TextBuffer.java', 586), ('TextBuffer.java', 585)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/util/TextBuffer.java', 585)]

- SBFL   ranked 5523 statement(s)
- Hybrid ranked 30 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | TextBuffer.java:582 | 0.707107 | `final char[] curr = _currentSegment;` |
| 1 | 4 | TextBuffer.java:584 | 0.707107 | `final int len = curr.length;` |
| 1 | 4 | TextBuffer.java:586 | 0.707107 | `int newLen = (len == MAX_SEGMENT_LEN) ? (MAX_SEGMENT_LEN+1) : Math.min(MAX_SEGMENT_LEN, len + (len >> 1));` |
| 1 | 4 | TextBuffer.java:587 | 0.707107 | `return (_currentSegment = Arrays.copyOf(curr, newLen));` |
| 5 | 2 | TextBuffer.java:515 | 0.316228 | `unshare(1);` |
| 5 | 2 | TextBuffer.java:641 | 0.316228 | `_currentSegment = buf(needed);` |
| 7 | 11 | TextBuffer.java:631 | 0.27735 | `int sharedLen = _inputLen;` |
| 7 | 11 | TextBuffer.java:632 | 0.27735 | `_inputLen = 0;` |
| 7 | 11 | TextBuffer.java:633 | 0.27735 | `char[] inputBuf = _inputBuffer;` |
| 7 | 11 | TextBuffer.java:634 | 0.27735 | `_inputBuffer = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 30 | BufferRecycler.java:46 | 1.0 | `private final static int[] CHAR_BUFFER_LENGTHS = new int[] { 4000, 4000, 200, 200 };` |
| 1 | 30 | BufferRecycler.java:62 | 1.0 | `this(4, 4);` |
| 1 | 30 | BufferRecycler.java:71 | 1.0 | `protected BufferRecycler(int bbCount, int cbCount) {` |
| 1 | 30 | BufferRecycler.java:72 | 1.0 | `_byteBuffers = new byte[bbCount][];` |
| 1 | 30 | BufferRecycler.java:73 | 1.0 | `_charBuffers = new char[cbCount][];` |
| 1 | 30 | BufferRecycler.java:118 | 1.0 | `final int DEF_SIZE = charBufferLength(ix);` |
| 1 | 30 | BufferRecycler.java:119 | 1.0 | `if (minSize < DEF_SIZE) {` |
| 1 | 30 | BufferRecycler.java:120 | 1.0 | `minSize = DEF_SIZE;` |
| 1 | 30 | BufferRecycler.java:122 | 1.0 | `char[] buffer = _charBuffers[ix];` |
| 1 | 30 | BufferRecycler.java:123 | 1.0 | `if (buffer == null || buffer.length < minSize) {` |

