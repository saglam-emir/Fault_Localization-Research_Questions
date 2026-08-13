# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVFormat.java', 319), ('CSVPrinter.java', 139)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CSVFormat.java', 319, '->', 318)]

Ground_Truth_Answerable: True

- SBFL   top rank: 37, AP: 0.0158
- Hybrid top rank: 1, AP: 0.5000

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CSVPrinter.java:212 | 0.353553 | `quote = !(object instanceof Number);` |
| 1 | 2 | CSVPrinter.java:213 | 0.353553 | `break;` |
| 3 | 3 | CSVPrinter.java:126 | 0.25 | `final String nullString = format.getNullString();` |
| 3 | 3 | CSVPrinter.java:127 | 0.25 | `strValue = nullString == null ? Constants.EMPTY : nullString;` |
| 3 | 3 | CSVPrinter.java:128 | 0.25 | `} else {` |
| 6 | 1 | CSVFormat.java:1176 | 0.188982 | `return new CSVFormat(delimiter, quoteCharacter, quoteMode, commentMarker, escapeCharacter,` |
| 7 | 1 | CSVFormat.java:1221 | 0.129099 | `return new CSVFormat(delimiter, quoteCharacter, quoteModePolicy, commentMarker, escapeCharacter,` |
| 8 | 1 | CSVFormat.java:632 | 0.128037 | `return nullString;` |
| 9 | 1 | CSVFormat.java:659 | 0.124035 | `return recordSeparator;` |
| 10 | 8 | CSVPrinter.java:270 | 0.117851 | `if (!quote) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:318 | 0.707107 | `public static final CSVFormat MYSQL = DEFAULT.withDelimiter(TAB).withEscape(BACKSLASH).withIgnoreEmptyLines(false)` |
| 2 | 1 | CSVFormat.java:229 | 0.0 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null, false, true,` |

