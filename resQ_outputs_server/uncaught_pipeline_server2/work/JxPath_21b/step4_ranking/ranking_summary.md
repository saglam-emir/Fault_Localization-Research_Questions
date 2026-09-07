# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PropertyPointer.java', 152)]

Ground_Truth_Answerable: True

- SBFL   ranked 5608 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ValueUtils.java:142 | 0.816497 | `return 0;` |
| 2 | 3 | VariablePointer.java:308 | 0.707107 | `if (index != WHOLE_COLLECTION) {` |
| 2 | 3 | XPathParser.java:117 | 0.707107 | `jj_consume_token(FUNCTION_NULL);` |
| 2 | 3 | XPathParser.java:118 | 0.707107 | `break;` |
| 5 | 1 | XPathParserTokenManager.java:638 | 0.5 | `return jjStartNfaWithStates_0(3, 71, 12);` |
| 6 | 1 | VariablePointer.java:324 | 0.408248 | `return getValuePointer().childIterator(test, reverse, startWith);` |
| 7 | 16 | CoreOperationCompare.java:108 | 0.353553 | `return findMatch((Iterator) l, (Iterator) r);` |
| 7 | 16 | CoreOperationCompare.java:142 | 0.353553 | `HashSet left = new HashSet();` |
| 7 | 16 | CoreOperationCompare.java:143 | 0.353553 | `while (lit.hasNext()) {` |
| 7 | 16 | CoreOperationCompare.java:146 | 0.353553 | `while (rit.hasNext()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

