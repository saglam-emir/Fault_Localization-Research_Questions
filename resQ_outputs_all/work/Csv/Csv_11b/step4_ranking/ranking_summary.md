# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVParser.java', 384)]

Ground_Truth_Answerable: True

- SBFL   ranked 563 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CSVFormat.java:828 | 0.408248 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 1 | 2 | CSVParser.java:259 | 0.408248 | `this.record.add(input.equalsIgnoreCase(nullString) ? null : input);` |
| 3 | 1 | CSVFormat.java:877 | 0.235702 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 4 | 5 | CSVParser.java:368 | 0.182574 | `final CSVRecord nextRecord = this.nextRecord();` |
| 4 | 5 | CSVParser.java:369 | 0.182574 | `if (nextRecord != null) {` |
| 4 | 5 | CSVParser.java:370 | 0.182574 | `headerRecord = nextRecord.values();` |
| 4 | 5 | CSVParser.java:372 | 0.182574 | `} else {` |
| 4 | 5 | Lexer.java:145 | 0.182574 | `token.type = TOKEN;` |
| 9 | 11 | CSVFormat.java:611 | 0.149071 | `return new CSVParser(in, this);` |
| 9 | 11 | CSVParser.java:363 | 0.149071 | `hdrMap = new LinkedHashMap<String, Integer>();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:175 | 0.288675 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null,` |

