# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberInput.java', 295), ('NumberInput.java', 296), ('NumberInput.java', 305), ('NumberInput.java', 306), ('NumberInput.java', 308), ('TextBuffer.java', 390), ('TextBuffer.java', 394)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/io/NumberInput.java', 296), ('src/main/java/com/fasterxml/jackson/core/io/NumberInput.java', 305), ('src/main/java/com/fasterxml/jackson/core/io/NumberInput.java', 306), ('src/main/java/com/fasterxml/jackson/core/io/NumberInput.java', 308)]

- SBFL   ranked 4992 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | ReaderBasedJsonParser.java:1367 | 1.0 | `if (isEnabled(Feature.ALLOW_NON_NUMERIC_NUMBERS)) {` |
| 1 | 3 | ReaderBasedJsonParser.java:1368 | 1.0 | `return resetAsNaN("NaN", Double.NaN);` |
| 1 | 3 | ReaderBasedJsonParser.java:1370 | 1.0 | `_reportError("Non-standard token 'NaN': enable JsonParser.Feature.ALLOW_NON_NUMERIC_NUMBERS to allow");` |
| 4 | 12 | ParserBase.java:562 | 0.707107 | `_textBuffer.resetWithString(valueStr);` |
| 4 | 12 | ParserBase.java:563 | 0.707107 | `_numberDouble = value;` |
| 4 | 12 | ParserBase.java:564 | 0.707107 | `_numTypesValid = NR_DOUBLE;` |
| 4 | 12 | ParserBase.java:565 | 0.707107 | `return JsonToken.VALUE_NUMBER_FLOAT;` |
| 4 | 12 | ReaderBasedJsonParser.java:1366 | 0.707107 | `_matchToken("NaN", 1);` |
| 4 | 12 | TextBuffer.java:215 | 0.707107 | `_inputBuffer = null;` |
| 4 | 12 | TextBuffer.java:216 | 0.707107 | `_inputStart = -1;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

