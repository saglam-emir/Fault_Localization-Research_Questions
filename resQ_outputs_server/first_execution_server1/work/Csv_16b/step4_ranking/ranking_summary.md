# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVParser.java', 289), ('CSVParser.java', 357), ('CSVParser.java', 523), ('CSVParser.java', 571)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/csv/CSVParser.java', 289), ('src/main/java/org/apache/commons/csv/CSVParser.java', 571)]

- SBFL   ranked 608 statement(s)
- Hybrid ranked 216 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | CSVParser.java:537 | 0.160128 | `if (CSVParser.this.isClosed()) {` |
| 1 | 5 | CSVParser.java:540 | 0.160128 | `if (this.current == null) {` |
| 1 | 5 | CSVParser.java:541 | 0.160128 | `this.current = this.getNextRecord();` |
| 1 | 5 | CSVParser.java:544 | 0.160128 | `return this.current != null;` |
| 1 | 5 | CSVRecord.java:79 | 0.160128 | `return values[i];` |
| 6 | 1 | CSVFormat.java:1018 | 0.125988 | `return new CSVParser(in, this);` |
| 7 | 4 | CSVParser.java:552 | 0.123091 | `CSVRecord next = this.current;` |
| 7 | 4 | CSVParser.java:553 | 0.123091 | `this.current = null;` |
| 7 | 4 | CSVParser.java:555 | 0.123091 | `if (next == null) {` |
| 7 | 4 | CSVParser.java:563 | 0.123091 | `return next;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVParser.java:544 | 0.408248 | `return this.current != null;` |
| 2 | 1 | CSVParser.java:462 | 0.267261 | `Map<String, Integer> hdrMap = null;` |
| 3 | 4 | CSVParser.java:506 | 0.179605 | `return this.lexer.isClosed();` |
| 3 | 4 | CSVParser.java:537 | 0.179605 | `if (CSVParser.this.isClosed()) {` |
| 3 | 4 | CSVParser.java:540 | 0.179605 | `if (this.current == null) {` |
| 3 | 4 | CSVParser.java:541 | 0.179605 | `this.current = this.getNextRecord();` |
| 7 | 1 | Lexer.java:196 | 0.120386 | `token.type = EORECORD;` |
| 8 | 1 | CSVFormat.java:1018 | 0.119523 | `return new CSVParser(in, this);` |
| 9 | 3 | CSVParser.java:523 | 0.117041 | `return new Iterator<CSVRecord>() {` |
| 9 | 3 | CSVParser.java:528 | 0.117041 | `return CSVParser.this.nextRecord();` |

