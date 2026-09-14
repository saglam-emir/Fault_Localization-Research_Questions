# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVFormat.java', 1039)]

Ground_Truth_Answerable: True

- SBFL   ranked 648 statement(s)
- Hybrid ranked 50 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:1040 | 0.588348 | `quote = true;` |
| 2 | 8 | CSVFormat.java:1078 | 0.400892 | `if (!quote) {` |
| 2 | 8 | CSVFormat.java:1085 | 0.400892 | `out.append(quoteChar);` |
| 2 | 8 | CSVFormat.java:1089 | 0.400892 | `while (pos < end) {` |
| 2 | 8 | CSVFormat.java:1090 | 0.400892 | `final char c = value.charAt(pos);` |
| 2 | 8 | CSVFormat.java:1091 | 0.400892 | `if (c == quoteChar) {` |
| 2 | 8 | CSVFormat.java:1100 | 0.400892 | `pos++;` |
| 2 | 8 | CSVFormat.java:1104 | 0.400892 | `out.append(value, start, pos);` |
| 2 | 8 | CSVFormat.java:1105 | 0.400892 | `out.append(quoteChar);` |
| 10 | 2 | CSVPrinter.java:122 | 0.363803 | `format.print(value, out, newRecord);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVPrinter.java:123 | 0.774597 | `newRecord = false;` |
| 2 | 24 | CSVFormat.java:520 | 0.707107 | `this.delimiter = delimiter;` |
| 2 | 24 | CSVFormat.java:521 | 0.707107 | `this.quoteCharacter = quoteChar;` |
| 2 | 24 | CSVFormat.java:522 | 0.707107 | `this.quoteMode = quoteMode;` |
| 2 | 24 | CSVFormat.java:523 | 0.707107 | `this.commentMarker = commentStart;` |
| 2 | 24 | CSVFormat.java:524 | 0.707107 | `this.escapeCharacter = escape;` |
| 2 | 24 | CSVFormat.java:525 | 0.707107 | `this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;` |
| 2 | 24 | CSVFormat.java:526 | 0.707107 | `this.allowMissingColumnNames = allowMissingColumnNames;` |
| 2 | 24 | CSVFormat.java:527 | 0.707107 | `this.ignoreEmptyLines = ignoreEmptyLines;` |
| 2 | 24 | CSVFormat.java:529 | 0.707107 | `this.nullString = nullString;` |

