# Ranking Comparison Summary

Ground truth faulty statement(s): [('Lexer.java', 111), ('Lexer.java', 112), ('Lexer.java', 113)]

- SBFL   top rank: 1, AP: 0.3333
- Hybrid top rank: 1, AP: 0.0019

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Lexer.java:111 | 0.612372 | `return c;` |
| 2 | 4 | CSVLexer.java:211 | 0.5 | `final int unescaped = readEscape();` |
| 2 | 4 | CSVLexer.java:212 | 0.5 | `if (unescaped == Constants.END_OF_STREAM) { // unexpected char after escape` |
| 2 | 4 | CSVLexer.java:215 | 0.5 | `tkn.content.append((char) unescaped);` |
| 2 | 4 | CSVLexer.java:217 | 0.5 | `} else if (isQuoteChar(c)) {` |
| 6 | 4 | CSVLexer.java:164 | 0.416025 | `if (unescaped == Constants.END_OF_STREAM) { // unexpected char after escape` |
| 6 | 4 | CSVLexer.java:167 | 0.416025 | `tkn.content.append((char) unescaped);` |
| 6 | 4 | CSVLexer.java:169 | 0.416025 | `c = in.read(); // continue` |
| 6 | 4 | CSVLexer.java:170 | 0.416025 | `} else {` |
| 10 | 3 | CSVLexer.java:163 | 0.400892 | `final int unescaped = readEscape();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 176 | CSVFormat.java:78 | 0.0 | `this(delimiter, null, null, null, null, false, false, null, Constants.EMPTY, null);` |
| 1 | 176 | CSVFormat.java:110 | 0.0 | `String nullToString, final String[] header) {` |
| 1 | 176 | CSVFormat.java:114 | 0.0 | `this.delimiter = delimiter;` |
| 1 | 176 | CSVFormat.java:115 | 0.0 | `this.quoteChar = quoteChar;` |
| 1 | 176 | CSVFormat.java:116 | 0.0 | `this.quotePolicy = quotePolicy;` |
| 1 | 176 | CSVFormat.java:117 | 0.0 | `this.commentStart = commentStart;` |
| 1 | 176 | CSVFormat.java:118 | 0.0 | `this.escape = escape;` |
| 1 | 176 | CSVFormat.java:119 | 0.0 | `this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;` |
| 1 | 176 | CSVFormat.java:120 | 0.0 | `this.ignoreEmptyLines = ignoreEmptyLines;` |
| 1 | 176 | CSVFormat.java:121 | 0.0 | `this.recordSeparator = recordSeparator;` |

