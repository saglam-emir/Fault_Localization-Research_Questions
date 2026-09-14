# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVPrinter.java', 70)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/csv/CSVPrinter.java', 70)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 554 statement(s)
- Hybrid ranked 68 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVPrinter.java:125 | 0.447214 | `out.append(value, offset, offset + len);` |
| 2 | 2 | CSVFormat.java:560 | 0.333333 | `return escape != null;` |
| 2 | 2 | CSVPrinter.java:122 | 0.333333 | `} else if (format.isEscaping()) {` |
| 4 | 1 | CSVFormat.java:318 | 0.301511 | `if (!dupCheck.add(hdr)) {` |
| 5 | 1 | CSVFormat.java:322 | 0.25 | `this.header = header.clone();` |
| 6 | 3 | CSVFormat.java:316 | 0.242536 | `Set<String> dupCheck = new HashSet<String>();` |
| 6 | 3 | CSVFormat.java:317 | 0.242536 | `for(String hdr : header) {` |
| 6 | 3 | CSVFormat.java:789 | 0.242536 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 9 | 3 | CSVPrinter.java:367 | 0.218218 | `for (final Object value : values) {` |
| 9 | 3 | CSVPrinter.java:368 | 0.218218 | `print(value);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | CSVFormat.java:322 | 1.0 | `this.header = header.clone();` |
| 1 | 5 | CSVFormat.java:789 | 1.0 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 1 | 5 | CSVPrinter.java:338 | 1.0 | `newRecord = true;` |
| 1 | 5 | CSVPrinter.java:368 | 1.0 | `print(value);` |
| 1 | 5 | CSVPrinter.java:370 | 1.0 | `println();` |
| 6 | 3 | CSVFormat.java:865 | 0.301511 | `return new CSVFormat(delimiter, quoteChar, quotePolicy, commentStart, escape,` |
| 6 | 3 | CSVPrinter.java:111 | 0.301511 | `this.print(value, strValue, 0, strValue.length());` |
| 6 | 3 | CSVPrinter.java:127 | 0.301511 | `newRecord = false;` |
| 9 | 11 | CSVFormat.java:304 | 0.242536 | `this.delimiter = delimiter;` |
| 9 | 11 | CSVFormat.java:305 | 0.242536 | `this.quoteChar = quoteChar;` |

