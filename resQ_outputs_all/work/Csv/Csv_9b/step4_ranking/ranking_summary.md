# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CSVRecord.java', 180)]

Ground_Truth_Answerable: True

- SBFL   ranked 486 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CSVFormat.java:267 | 0.333333 | `return new CSVFormat(delimiter, null, null, null, null, false, false, null, null, null, false);` |
| 2 | 1 | CSVRecord.java:214 | 0.288675 | `return putIn(new HashMap<String, String>(values.length));` |
| 3 | 1 | CSVRecord.java:180 | 0.258199 | `for (final Entry<String, Integer> entry : mapping.entrySet()) {` |
| 4 | 2 | CSVParser.java:436 | 0.204124 | `next = this.getNextRecord();` |
| 4 | 2 | CSVParser.java:437 | 0.204124 | `if (next == null) {` |
| 6 | 4 | CSVParser.java:431 | 0.149071 | `CSVRecord next = this.current;` |
| 6 | 4 | CSVParser.java:432 | 0.149071 | `this.current = null;` |
| 6 | 4 | CSVParser.java:434 | 0.149071 | `if (next == null) {` |
| 6 | 4 | CSVParser.java:442 | 0.149071 | `return next;` |
| 10 | 6 | CSVParser.java:392 | 0.144338 | `return this.lexer.isClosed();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

