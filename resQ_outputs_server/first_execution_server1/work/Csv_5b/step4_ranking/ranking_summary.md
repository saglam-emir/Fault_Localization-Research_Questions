# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVPrinter.java', 325), ('CSVPrinter.java', 326)]

Ground_Truth_Answerable: True

- SBFL   ranked 536 statement(s)
- Hybrid ranked 2 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | CSVFormat.java:380 | 0.707107 | `final StringWriter out = new StringWriter();` |
| 1 | 3 | CSVFormat.java:382 | 0.707107 | `new CSVPrinter(out, this).printRecord(values);` |
| 1 | 3 | CSVFormat.java:383 | 0.707107 | `return out.toString().trim();` |
| 4 | 1 | CSVFormat.java:881 | 0.57735 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 5 | 1 | CSVPrinter.java:120 | 0.5 | `out.append(value, offset, offset + len);` |
| 6 | 2 | CSVFormat.java:534 | 0.353553 | `return escape != null;` |
| 6 | 2 | CSVPrinter.java:117 | 0.353553 | `} else if (format.isEscaping()) {` |
| 8 | 3 | CSVFormat.java:646 | 0.301511 | `final Set<String> set = new HashSet<String>(header.length);` |
| 8 | 3 | CSVFormat.java:647 | 0.301511 | `set.addAll(Arrays.asList(header));` |
| 8 | 3 | CSVFormat.java:648 | 0.301511 | `if (set.size() != header.length) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CSVFormat.java:380 | 0.707107 | `final StringWriter out = new StringWriter();` |
| 1 | 2 | CSVFormat.java:383 | 0.707107 | `return out.toString().trim();` |

