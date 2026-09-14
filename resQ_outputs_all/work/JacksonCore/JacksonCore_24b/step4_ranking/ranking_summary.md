# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ParserBase.java', 869), ('ParserBase.java', 870), ('ParserBase.java', 871), ('ParserBase.java', 887), ('ParserMinimalBase.java', 565), ('ParserMinimalBase.java', 566), ('ParserMinimalBase.java', 570), ('ParserMinimalBase.java', 582), ('ParserMinimalBase.java', 583), ('ParserMinimalBase.java', 587)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ParserBase.java', 871, '->', 870), ('ParserMinimalBase.java', 566, '->', 565), ('ParserMinimalBase.java', 583, '->', 582)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/base/ParserMinimalBase.java', 570), ('src/main/java/com/fasterxml/jackson/core/base/ParserMinimalBase.java', 587)]

- SBFL   ranked 11083 statement(s)
- Hybrid ranked 1912 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | JsonProcessingException.java:133 | 0.646762 | `@Override public String toString() { return getClass().getName()+": "+getMessage(); }` |
| 2 | 2 | ParserMinimalBase.java:598 | 0.542326 | `int rawLen = rawNum.length();` |
| 2 | 2 | ParserMinimalBase.java:599 | 0.542326 | `if (rawLen < 1000) {` |
| 4 | 4 | ParserBase.java:849 | 0.420084 | `_reportTooLongIntegral(expType, numStr);` |
| 4 | 4 | ParserBase.java:869 | 0.420084 | `final String numDesc = _longIntegerDesc(rawNum);` |
| 4 | 4 | ParserBase.java:870 | 0.420084 | `_reportError("Numeric value (%s) out of range of %s", numDesc,` |
| 4 | 4 | ParserMinimalBase.java:600 | 0.420084 | `return rawNum;` |
| 8 | 3 | ParserBase.java:885 | 0.363803 | `int result = (int) _numberLong;` |
| 8 | 3 | ParserBase.java:886 | 0.363803 | `if (((long) result) != _numberLong) {` |
| 8 | 3 | ParserBase.java:887 | 0.363803 | `_reportError("Numeric value ("+getText()+") out of range of int");` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UTF8StreamJsonParser.java:1443 | 0.5 | `_verifyRootSpace(c);` |
| 2 | 2 | UTF8StreamJsonParser.java:1632 | 0.353553 | `++_inputPtr;` |
| 2 | 2 | UTF8StreamJsonParser.java:1634 | 0.353553 | `switch (ch) {` |
| 4 | 1 | JsonStreamContext.java:89 | 0.253546 | `public final boolean inRoot() { return _type == TYPE_ROOT; }` |
| 5 | 8 | BufferRecycler.java:45 | 0.240192 | `private final static int[] BYTE_BUFFER_LENGTHS = new int[] { 8000, 8000, 2000, 2000 };` |
| 5 | 8 | BufferRecycler.java:90 | 0.240192 | `final int DEF_SIZE = byteBufferLength(ix);` |
| 5 | 8 | BufferRecycler.java:91 | 0.240192 | `if (minSize < DEF_SIZE) {` |
| 5 | 8 | BufferRecycler.java:92 | 0.240192 | `minSize = DEF_SIZE;` |
| 5 | 8 | BufferRecycler.java:95 | 0.240192 | `if (buffer == null || buffer.length < minSize) {` |
| 5 | 8 | BufferRecycler.java:96 | 0.240192 | `buffer = balloc(minSize);` |

