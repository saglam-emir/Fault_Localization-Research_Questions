# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ReaderBasedJsonParser.java', 622), ('ReaderBasedJsonParser.java', 630), ('ReaderBasedJsonParser.java', 635), ('ReaderBasedJsonParser.java', 773), ('ReaderBasedJsonParser.java', 776), ('ReaderBasedJsonParser.java', 780), ('ReaderBasedJsonParser.java', 851), ('ReaderBasedJsonParser.java', 853), ('ReaderBasedJsonParser.java', 857), ('ReaderBasedJsonParser.java', 862), ('ReaderBasedJsonParser.java', 917), ('ReaderBasedJsonParser.java', 967), ('ReaderBasedJsonParser.java', 2672), ('ReaderBasedJsonParser.java', 2673), ('ReaderBasedJsonParser.java', 2671), ('UTF8StreamJsonParser.java', 3622)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ReaderBasedJsonParser.java', 2672, '->', 2671), ('ReaderBasedJsonParser.java', 2673, '->', 2671), ('UTF8StreamJsonParser.java', 3622, '->', 3621)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java', 635), ('src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java', 917)]

- SBFL   ranked 7031 statement(s)
- Hybrid ranked 512 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | JsonFactory.java:881 | 0.707107 | `return createParser(content, 0, content.length);` |
| 1 | 3 | JsonFactory.java:890 | 0.707107 | `if (_inputDecorator != null) { // easier to just wrap in a Reader than extend InputDecorator` |
| 1 | 3 | JsonFactory.java:893 | 0.707107 | `return _createParser(content, offset, len, _createContext(content, true),` |
| 4 | 2 | ReaderBasedJsonParser.java:2670 | 0.57735 | `final Object src = _ioContext.getSourceReference();` |
| 4 | 2 | ReaderBasedJsonParser.java:2671 | 0.57735 | `return new JsonLocation(src,` |
| 6 | 1 | JsonLocation.java:81 | 0.447214 | `public long getCharOffset() { return _totalChars; }` |
| 7 | 4 | ParserBase.java:475 | 0.353553 | `public long getTokenCharacterOffset() { return _tokenInputTotal; }` |
| 7 | 4 | ParserBase.java:476 | 0.353553 | `public int getTokenLineNr() { return _tokenInputRow; }` |
| 7 | 4 | ParserBase.java:479 | 0.353553 | `int col = _tokenInputCol;` |
| 7 | 4 | ParserBase.java:480 | 0.353553 | `return (col < 0) ? col : (col + 1);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | ReaderBasedJsonParser.java:581 | 0.707107 | `return _nextAfterName();` |
| 1 | 5 | ReaderBasedJsonParser.java:709 | 0.707107 | `_nameCopied = false; // need to invalidate if it was copied` |
| 1 | 5 | ReaderBasedJsonParser.java:710 | 0.707107 | `JsonToken t = _nextToken;` |
| 1 | 5 | ReaderBasedJsonParser.java:711 | 0.707107 | `_nextToken = null;` |
| 1 | 5 | ReaderBasedJsonParser.java:721 | 0.707107 | `return (_currToken = t);` |
| 6 | 16 | ReaderBasedJsonParser.java:628 | 0.5 | `if (inObject) {` |
| 6 | 16 | ReaderBasedJsonParser.java:630 | 0.5 | `String name = (i == INT_QUOTE) ? _parseName() : _handleOddName(i);` |
| 6 | 16 | ReaderBasedJsonParser.java:632 | 0.5 | `_currToken = JsonToken.FIELD_NAME;` |
| 6 | 16 | ReaderBasedJsonParser.java:633 | 0.5 | `i = _skipColon();` |
| 6 | 16 | ReaderBasedJsonParser.java:642 | 0.5 | `_tokenIncomplete = true;` |

