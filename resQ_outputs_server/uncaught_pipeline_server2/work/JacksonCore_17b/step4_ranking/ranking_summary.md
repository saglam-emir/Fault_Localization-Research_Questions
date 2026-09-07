# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('UTF8JsonGenerator.java', 534), ('UTF8JsonGenerator.java', 536), ('UTF8JsonGenerator.java', 528), ('UTF8JsonGenerator.java', 532), ('UTF8JsonGenerator.java', 539), ('UTF8JsonGenerator.java', 672), ('UTF8JsonGenerator.java', 1887)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('UTF8JsonGenerator.java', 1887, '->', 1886)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/json/UTF8JsonGenerator.java', 528), ('src/main/java/com/fasterxml/jackson/core/json/UTF8JsonGenerator.java', 532), ('src/main/java/com/fasterxml/jackson/core/json/UTF8JsonGenerator.java', 672)]

- SBFL   ranked 7075 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | GeneratorBase.java:298 | 1.0 | `_verifyValueWrite("write raw value");` |
| 1 | 4 | GeneratorBase.java:299 | 1.0 | `writeRaw(text, offset, len);` |
| 1 | 4 | JsonProcessingException.java:127 | 1.0 | `@Override public String toString() { return getClass().getName()+": "+getMessage(); }` |
| 1 | 4 | UTF8JsonGenerator.java:1887 | 1.0 | `_reportError("Split surrogate on writeRaw() input (last character)");` |
| 5 | 16 | UTF8JsonGenerator.java:572 | 0.707107 | `if (_outputEnd < len3) { // wouldn't be enough...` |
| 5 | 16 | UTF8JsonGenerator.java:573 | 0.707107 | `_writeSegmentedRaw(cbuf, offset, len);` |
| 5 | 16 | UTF8JsonGenerator.java:629 | 0.707107 | `final int end = _outputEnd;` |
| 5 | 16 | UTF8JsonGenerator.java:630 | 0.707107 | `final byte[] bbuf = _outputBuffer;` |
| 5 | 16 | UTF8JsonGenerator.java:631 | 0.707107 | `final int inputEnd = offset + len;` |
| 5 | 16 | UTF8JsonGenerator.java:634 | 0.707107 | `while (offset < inputEnd) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

