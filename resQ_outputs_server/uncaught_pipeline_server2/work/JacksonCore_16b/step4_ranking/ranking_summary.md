# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('JsonParserSequence.java', 35), ('JsonParserSequence.java', 45), ('JsonParserSequence.java', 104), ('JsonParserSequence.java', 107), ('JsonParserSequence.java', 108), ('JsonParserSequence.java', 109), ('JsonParserSequence.java', 110), ('JsonParserSequence.java', 112), ('JsonParserSequence.java', 106)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('JsonParserSequence.java', 104, '->', 103)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/util/JsonParserSequence.java', 35)]

- SBFL   ranked 542 statement(s)
- Hybrid ranked 237 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 57 | ParserBase.java:588 | 1.0 | `if (fractLen < 1 && expLen < 1) { // integer` |
| 1 | 57 | ParserBase.java:589 | 1.0 | `return resetInt(negative, intLen);` |
| 1 | 57 | ReaderBasedJsonParser.java:1293 | 1.0 | `_inputPtr = startPtr;` |
| 1 | 57 | ReaderBasedJsonParser.java:1294 | 1.0 | `return _parseNumber2(false, startPtr);` |
| 1 | 57 | ReaderBasedJsonParser.java:1311 | 1.0 | `_verifyRootSpace(ch);` |
| 1 | 57 | ReaderBasedJsonParser.java:1439 | 1.0 | `_inputPtr = neg ? (startPtr+1) : startPtr;` |
| 1 | 57 | ReaderBasedJsonParser.java:1440 | 1.0 | `char[] outBuf = _textBuffer.emptyAndGetCurrentSegment();` |
| 1 | 57 | ReaderBasedJsonParser.java:1441 | 1.0 | `int outPtr = 0;` |
| 1 | 57 | ReaderBasedJsonParser.java:1444 | 1.0 | `if (neg) {` |
| 1 | 57 | ReaderBasedJsonParser.java:1449 | 1.0 | `int intLen = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 31 | JsonStreamContext.java:68 | 1.0 | `public final boolean inRoot() { return _type == TYPE_ROOT; }` |
| 1 | 31 | ParserBase.java:588 | 1.0 | `if (fractLen < 1 && expLen < 1) { // integer` |
| 1 | 31 | ParserBase.java:589 | 1.0 | `return resetInt(negative, intLen);` |
| 1 | 31 | ParserBase.java:596 | 1.0 | `_numberNegative = negative;` |
| 1 | 31 | ParserBase.java:597 | 1.0 | `_intLength = intLen;` |
| 1 | 31 | ParserBase.java:598 | 1.0 | `_fractLength = 0;` |
| 1 | 31 | ParserBase.java:599 | 1.0 | `_expLength = 0;` |
| 1 | 31 | ParserBase.java:600 | 1.0 | `_numTypesValid = NR_UNKNOWN; // to force parsing` |
| 1 | 31 | ReaderBasedJsonParser.java:232 | 1.0 | `_currInputProcessed += bufSize;` |
| 1 | 31 | ReaderBasedJsonParser.java:238 | 1.0 | `_nameStartOffset -= bufSize;` |

