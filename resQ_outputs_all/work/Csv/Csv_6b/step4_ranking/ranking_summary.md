# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVRecord.java', 182), ('CSVRecord.java', 183)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('CSVRecord.java', 183, '->', 180)]

Ground_Truth_Answerable: True

- SBFL   ranked 482 statement(s)
- Hybrid ranked 103 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVRecord.java:212 | 0.333333 | `return putIn(new HashMap<String, String>(values.length));` |
| 2 | 3 | CSVRecord.java:180 | 0.288675 | `for (final Entry<String, Integer> entry : mapping.entrySet()) {` |
| 2 | 3 | CSVRecord.java:181 | 0.288675 | `final int col = entry.getValue().intValue();` |
| 2 | 3 | CSVRecord.java:182 | 0.288675 | `map.put(entry.getKey(), values[col]);` |
| 5 | 3 | CSVFormat.java:496 | 0.258199 | `return skipHeaderRecord;` |
| 5 | 3 | CSVParser.java:355 | 0.258199 | `if (this.format.getSkipHeaderRecord()) {` |
| 5 | 3 | CSVParser.java:358 | 0.258199 | `header = formatHeader;` |
| 8 | 2 | CSVParser.java:416 | 0.218218 | `next = this.getNextRecord();` |
| 8 | 2 | CSVParser.java:417 | 0.218218 | `if (next == null) {` |
| 10 | 10 | CSVFormat.java:646 | 0.182574 | `final Set<String> set = new HashSet<String>(header.length);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 103 | CSVFormat.java:174 | 1.0 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null,` |
| 1 | 103 | CSVFormat.java:300 | 1.0 | `this.delimiter = delimiter;` |
| 1 | 103 | CSVFormat.java:301 | 1.0 | `this.quoteChar = quoteChar;` |
| 1 | 103 | CSVFormat.java:304 | 1.0 | `this.escape = escape;` |
| 1 | 103 | CSVFormat.java:306 | 1.0 | `this.ignoreEmptyLines = ignoreEmptyLines;` |
| 1 | 103 | CSVFormat.java:308 | 1.0 | `this.nullString = nullString;` |
| 1 | 103 | CSVFormat.java:309 | 1.0 | `this.header = header == null ? null : header.clone();` |
| 1 | 103 | CSVFormat.java:405 | 1.0 | `return delimiter;` |
| 1 | 103 | CSVFormat.java:414 | 1.0 | `return escape;` |
| 1 | 103 | CSVFormat.java:423 | 1.0 | `return header != null ? header.clone() : null;` |

