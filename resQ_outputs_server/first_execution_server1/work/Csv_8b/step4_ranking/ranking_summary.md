# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVFormat.java', 316), ('CSVFormat.java', 665), ('CSVFormat.java', 666), ('CSVFormat.java', 667), ('CSVFormat.java', 668), ('CSVFormat.java', 669), ('CSVFormat.java', 670), ('CSVFormat.java', 671)]

Ground_Truth_Answerable: True

- SBFL   ranked 554 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:669 | 0.57735 | `throw new IllegalStateException("The header contains duplicate names: " + Arrays.toString(header));` |
| 2 | 3 | CSVFormat.java:666 | 0.160128 | `final Set<String> set = new HashSet<String>(header.length);` |
| 2 | 3 | CSVFormat.java:667 | 0.160128 | `set.addAll(Arrays.asList(header));` |
| 2 | 3 | CSVFormat.java:668 | 0.160128 | `if (set.size() != header.length) {` |
| 5 | 2 | CSVFormat.java:316 | 0.144338 | `this.header = header.clone();` |
| 5 | 2 | CSVFormat.java:773 | 0.144338 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 7 | 1 | CSVFormat.java:665 | 0.06415 | `if (header != null) {` |
| 8 | 1 | CSVFormat.java:661 | 0.063758 | `if (escape == null && quotePolicy == Quote.NONE) {` |
| 9 | 1 | CSVFormat.java:656 | 0.062994 | `if (escape != null && escape.equals(commentStart)) {` |
| 10 | 1 | CSVFormat.java:651 | 0.062257 | `if (quoteChar != null && quoteChar.equals(commentStart)) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:174 | 0.288675 | `public static final CSVFormat DEFAULT = new CSVFormat(COMMA, DOUBLE_QUOTE_CHAR, null, null, null,` |

