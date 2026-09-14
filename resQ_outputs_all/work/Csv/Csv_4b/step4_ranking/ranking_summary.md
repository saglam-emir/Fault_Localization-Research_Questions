# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVParser.java', 288)]

Ground_Truth_Answerable: True

- SBFL   ranked 524 statement(s)
- Hybrid ranked 128 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVParser.java:288 | 0.408248 | `return new LinkedHashMap<String, Integer>(this.headerMap);` |
| 2 | 1 | CSVParser.java:172 | 0.107211 | `return new CSVParser(new StringReader(string), format);` |
| 3 | 1 | CSVParser.java:170 | 0.105409 | `Assertions.notNull(format, "format");` |
| 4 | 1 | CSVParser.java:169 | 0.103695 | `Assertions.notNull(string, "string");` |
| 5 | 20 | CSVParser.java:241 | 0.091287 | `format.validate();` |
| 5 | 20 | CSVParser.java:242 | 0.091287 | `this.format = format;` |
| 5 | 20 | CSVParser.java:243 | 0.091287 | `this.lexer = new Lexer(format, new ExtendedBufferedReader(reader));` |
| 5 | 20 | CSVParser.java:244 | 0.091287 | `this.headerMap = this.initializeHeader();` |
| 5 | 20 | CSVParser.java:325 | 0.091287 | `Map<String, Integer> hdrMap = null;` |
| 5 | 20 | CSVParser.java:326 | 0.091287 | `final String[] formatHeader = this.format.getHeader();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 42 | CSVFormat.java:174 | 0.267261 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null,` |
| 1 | 42 | CSVFormat.java:300 | 0.267261 | `this.delimiter = delimiter;` |
| 1 | 42 | CSVFormat.java:301 | 0.267261 | `this.quoteChar = quoteChar;` |
| 1 | 42 | CSVFormat.java:303 | 0.267261 | `this.commentStart = commentStart;` |
| 1 | 42 | CSVFormat.java:304 | 0.267261 | `this.escape = escape;` |
| 1 | 42 | CSVFormat.java:305 | 0.267261 | `this.ignoreSurroundingSpaces = ignoreSurroundingSpaces;` |
| 1 | 42 | CSVFormat.java:306 | 0.267261 | `this.ignoreEmptyLines = ignoreEmptyLines;` |
| 1 | 42 | CSVFormat.java:396 | 0.267261 | `return commentStart;` |
| 1 | 42 | CSVFormat.java:405 | 0.267261 | `return delimiter;` |
| 1 | 42 | CSVFormat.java:414 | 0.267261 | `return escape;` |

