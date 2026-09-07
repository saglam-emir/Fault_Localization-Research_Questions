# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ReaderBasedJsonParser.java', 952), ('ReaderBasedJsonParser.java', 1081), ('ReaderBasedJsonParser.java', 1162), ('ReaderBasedJsonParser.java', 1163), ('UTF8StreamJsonParser.java', 1244), ('UTF8StreamJsonParser.java', 1280), ('UTF8StreamJsonParser.java', 1407), ('UTF8StreamJsonParser.java', 1421), ('UTF8StreamJsonParser.java', 1422), ('UTF8StreamJsonParser.java', 1423), ('UTF8StreamJsonParser.java', 2575), ('UTF8StreamJsonParser.java', 2576), ('UTF8StreamJsonParser.java', 2577)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('ReaderBasedJsonParser.java', 1081, '->', 1079), ('UTF8StreamJsonParser.java', 1407, '->', 1404), ('UTF8StreamJsonParser.java', 2575, '->', 2574)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java', 1162), ('src/main/java/com/fasterxml/jackson/core/json/ReaderBasedJsonParser.java', 1163), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 1244), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 1280), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 1421), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 1422), ('src/main/java/com/fasterxml/jackson/core/json/UTF8StreamJsonParser.java', 1423)]

- SBFL   ranked 5302 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ReaderBasedJsonParser.java:897 | 0.267261 | `break int_loop;` |
| 2 | 1 | UTF8StreamJsonParser.java:1228 | 0.235702 | `break;` |
| 3 | 6 | ParserBase.java:529 | 0.166667 | `_numberNegative = negative;` |
| 3 | 6 | ParserBase.java:530 | 0.166667 | `_intLength = intLen;` |
| 3 | 6 | ParserBase.java:531 | 0.166667 | `_fractLength = 0;` |
| 3 | 6 | ParserBase.java:532 | 0.166667 | `_expLength = 0;` |
| 3 | 6 | ParserBase.java:533 | 0.166667 | `_numTypesValid = NR_UNKNOWN; // to force parsing` |
| 3 | 6 | ParserBase.java:534 | 0.166667 | `return JsonToken.VALUE_NUMBER_INT;` |
| 9 | 3 | UTF8StreamJsonParser.java:1230 | 0.150756 | `++intLen;` |
| 9 | 3 | UTF8StreamJsonParser.java:1231 | 0.150756 | `if (outPtr >= outBuf.length) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

