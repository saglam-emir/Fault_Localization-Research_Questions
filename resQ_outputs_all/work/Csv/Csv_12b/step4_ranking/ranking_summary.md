# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVFormat.java', 219)]

Ground_Truth_Answerable: True

- SBFL   ranked 563 statement(s)
- Hybrid ranked 140 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVParser.java:367 | 0.333333 | `throw new IllegalArgumentException("The header contains a duplicate name: \"" + header +` |
| 2 | 1 | CSVFormat.java:505 | 0.288675 | `return allowMissingColumnNames;` |
| 3 | 4 | CSVParser.java:348 | 0.174078 | `final CSVRecord nextRecord = this.nextRecord();` |
| 3 | 4 | CSVParser.java:349 | 0.174078 | `if (nextRecord != null) {` |
| 3 | 4 | CSVParser.java:350 | 0.174078 | `headerRecord = nextRecord.values();` |
| 3 | 4 | CSVParser.java:352 | 0.174078 | `} else {` |
| 7 | 1 | Lexer.java:145 | 0.149071 | `token.type = TOKEN;` |
| 8 | 11 | CSVParser.java:343 | 0.144338 | `hdrMap = new LinkedHashMap<String, Integer>();` |
| 8 | 11 | CSVParser.java:345 | 0.144338 | `String[] headerRecord = null;` |
| 8 | 11 | CSVParser.java:346 | 0.144338 | `if (formatHeader.length == 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:219 | 1.0 | `public static final CSVFormat EXCEL = DEFAULT.withIgnoreEmptyLines(false);` |
| 2 | 139 | CSVFormat.java:175 | 0.0 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null,` |
| 2 | 139 | CSVFormat.java:234 | 0.0 | `public static final CSVFormat TDF =` |
| 2 | 139 | CSVFormat.java:345 | 0.0 | `final boolean allowMissingColumnNames) {` |
| 2 | 139 | CSVFormat.java:349 | 0.0 | `this.delimiter = delimiter;` |
| 2 | 139 | CSVFormat.java:350 | 0.0 | `this.quoteCharacter = quoteChar;` |
| 2 | 139 | CSVFormat.java:351 | 0.0 | `this.quoteMode = quoteMode;` |
| 2 | 139 | CSVFormat.java:352 | 0.0 | `this.commentMarker = commentStart;` |
| 2 | 139 | CSVFormat.java:353 | 0.0 | `this.escapeCharacter = escape;` |
| 2 | 139 | CSVFormat.java:354 | 0.0 | `this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;` |

