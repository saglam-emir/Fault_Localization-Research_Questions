# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Lexer.java', 111), ('Lexer.java', 112), ('Lexer.java', 113)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Lexer.java', 112, '->', 90), ('Lexer.java', 113, '->', 90)]

Ground_Truth_Answerable: True

- SBFL   ranked 443 statement(s)
- Hybrid ranked 211 statement(s)

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
| 1 | 3 | CSVFormat.java:263 | 0.426401 | `return withEscape(Character.valueOf(escape));` |
| 1 | 3 | CSVFormat.java:279 | 0.426401 | `this.escape = escape;` |
| 1 | 3 | CSVLexer.java:169 | 0.426401 | `c = in.read(); // continue` |
| 4 | 1 | CSVFormat.java:527 | 0.316228 | `public static final CSVFormat MYSQL =` |
| 5 | 2 | CSVLexer.java:156 | 0.308607 | `tkn.type = EOF;` |
| 5 | 2 | CSVLexer.java:157 | 0.308607 | `tkn.isReady = true; // There is data at EOF` |
| 7 | 2 | CSVFormat.java:442 | 0.208514 | `return new CSVFormatBuilder(COMMA, DOUBLE_QUOTE_CHAR, null, null, null, false, true, CRLF, Constants.EMPTY,` |
| 7 | 2 | Constants.java:36 | 0.208514 | `static final Character DOUBLE_QUOTE_CHAR = Character.valueOf('"');` |
| 9 | 3 | CSVFormat.java:115 | 0.206284 | `this.quoteChar = quoteChar;` |
| 9 | 3 | Token.java:29 | 0.206284 | `final class Token {` |

