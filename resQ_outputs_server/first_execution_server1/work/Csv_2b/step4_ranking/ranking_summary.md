# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVRecord.java', 85), ('CSVRecord.java', 86)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/csv/CSVRecord.java', 86)]

- SBFL   ranked 428 statement(s)
- Hybrid ranked 8 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CSVRecord.java:84 | 0.267261 | `final Integer index = mapping.get(name);` |
| 1 | 2 | CSVRecord.java:85 | 0.267261 | `return index != null ? values[index.intValue()] : null;` |
| 3 | 1 | CSVRecord.java:80 | 0.25 | `if (mapping == null) {` |
| 4 | 6 | CSVRecord.java:34 | 0.113228 | `private static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 4 | 6 | CSVRecord.java:49 | 0.113228 | `final String comment, final long recordNumber) {` |
| 4 | 6 | CSVRecord.java:50 | 0.113228 | `this.recordNumber = recordNumber;` |
| 4 | 6 | CSVRecord.java:51 | 0.113228 | `this.values = values != null ? values : EMPTY_STRING_ARRAY;` |
| 4 | 6 | CSVRecord.java:52 | 0.113228 | `this.mapping = mapping;` |
| 4 | 6 | CSVRecord.java:53 | 0.113228 | `this.comment = comment;` |
| 10 | 419 | CSVFormat.java:74 | 0.0 | `public static final CSVFormat RFC4180 =` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | CSVRecord.java:49 | 0.316228 | `final String comment, final long recordNumber) {` |
| 1 | 5 | CSVRecord.java:50 | 0.316228 | `this.recordNumber = recordNumber;` |
| 1 | 5 | CSVRecord.java:51 | 0.316228 | `this.values = values != null ? values : EMPTY_STRING_ARRAY;` |
| 1 | 5 | CSVRecord.java:52 | 0.316228 | `this.mapping = mapping;` |
| 1 | 5 | CSVRecord.java:53 | 0.316228 | `this.comment = comment;` |
| 6 | 3 | CSVRecord.java:84 | 0.0 | `final Integer index = mapping.get(name);` |
| 6 | 3 | CSVRecord.java:107 | 0.0 | `return mapping != null ? mapping.containsKey(name) : false;` |
| 6 | 3 | CSVRecord.java:118 | 0.0 | `return isMapped(name) && mapping.get(name).intValue() < values.length;` |

