# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVFormat.java', 1189), ('CSVFormat.java', 1190), ('CSVFormat.java', 1191)]

Ground_Truth_Answerable: True

- SBFL   ranked 703 statement(s)
- Hybrid ranked 51 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:1190 | 0.235702 | `quote = true;` |
| 2 | 8 | CSVFormat.java:1228 | 0.107211 | `if (!quote) {` |
| 2 | 8 | CSVFormat.java:1235 | 0.107211 | `out.append(quoteChar);` |
| 2 | 8 | CSVFormat.java:1239 | 0.107211 | `while (pos < end) {` |
| 2 | 8 | CSVFormat.java:1240 | 0.107211 | `final char c = value.charAt(pos);` |
| 2 | 8 | CSVFormat.java:1241 | 0.107211 | `if (c == quoteChar) {` |
| 2 | 8 | CSVFormat.java:1250 | 0.107211 | `pos++;` |
| 2 | 8 | CSVFormat.java:1254 | 0.107211 | `out.append(value, start, pos);` |
| 2 | 8 | CSVFormat.java:1255 | 0.107211 | `out.append(quoteChar);` |
| 10 | 2 | CSVFormat.java:1220 | 0.08165 | `out.append(value, start, end);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | CSVFormat.java:489 | 0.218218 | `public static final CSVFormat TDF = DEFAULT` |
| 1 | 4 | CSVFormat.java:863 | 0.218218 | `return recordSeparator;` |
| 1 | 4 | CSVFormat.java:1769 | 0.218218 | `return this.withIgnoreSurroundingSpaces(true);` |
| 1 | 4 | CSVFormat.java:1781 | 0.218218 | `return new CSVFormat(delimiter, quoteCharacter, quoteMode, commentMarker, escapeCharacter,` |
| 5 | 3 | CSVFormat.java:244 | 0.179605 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null, false, true, CRLF,` |
| 5 | 3 | CSVFormat.java:633 | 0.179605 | `final boolean trailingDelimiter, final boolean autoFlush) {` |
| 5 | 3 | CSVFormat.java:642 | 0.179605 | `this.recordSeparator = recordSeparator;` |
| 8 | 44 | CSVFormat.java:634 | 0.0 | `this.delimiter = delimiter;` |
| 8 | 44 | CSVFormat.java:635 | 0.0 | `this.quoteCharacter = quoteChar;` |
| 8 | 44 | CSVFormat.java:636 | 0.0 | `this.quoteMode = quoteMode;` |

