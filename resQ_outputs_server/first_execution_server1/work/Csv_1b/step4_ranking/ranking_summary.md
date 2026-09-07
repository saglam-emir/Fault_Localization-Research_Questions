# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ExtendedBufferedReader.java', 58)]

Ground_Truth_Answerable: True

- SBFL   ranked 359 statement(s)
- Hybrid ranked 119 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVParser.java:249 | 0.57735 | `return lexer.getLineNumber();` |
| 2 | 1 | CSVParser.java:107 | 0.288675 | `this(new StringReader(input), format);` |
| 3 | 1 | Lexer.java:60 | 0.25 | `return in.getLineNumber();` |
| 4 | 1 | ExtendedBufferedReader.java:159 | 0.242536 | `return lineCounter;` |
| 5 | 4 | ExtendedBufferedReader.java:146 | 0.213201 | `super.mark(1);` |
| 5 | 4 | ExtendedBufferedReader.java:147 | 0.213201 | `int c = super.read();` |
| 5 | 4 | ExtendedBufferedReader.java:148 | 0.213201 | `super.reset();` |
| 5 | 4 | ExtendedBufferedReader.java:150 | 0.213201 | `return c;` |
| 9 | 5 | CSVLexer.java:141 | 0.208514 | `tkn.type = EORECORD;` |
| 9 | 5 | CSVLexer.java:142 | 0.208514 | `break;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVLexer.java:158 | 0.267261 | `c = in.read();` |
| 2 | 38 | CSVLexer.java:51 | 0.235702 | `int c = in.read();` |
| 2 | 38 | CSVLexer.java:52 | 0.235702 | `boolean eol = isEndOfLine(c);` |
| 2 | 38 | CSVLexer.java:53 | 0.235702 | `c = in.readAgain();` |
| 2 | 38 | CSVLexer.java:75 | 0.235702 | `if (isEndOfFile(lastChar) || (!isDelimiter(lastChar) && isEndOfFile(c))) {` |
| 2 | 38 | CSVLexer.java:82 | 0.235702 | `while (tkn.type == INVALID) {` |
| 2 | 38 | CSVLexer.java:92 | 0.235702 | `if (isCommentStart(c)) {` |
| 2 | 38 | CSVLexer.java:96 | 0.235702 | `} else if (isDelimiter(c)) {` |
| 2 | 38 | CSVLexer.java:99 | 0.235702 | `} else if (eol) {` |
| 2 | 38 | CSVLexer.java:103 | 0.235702 | `} else if (isEncapsulator(c)) {` |

