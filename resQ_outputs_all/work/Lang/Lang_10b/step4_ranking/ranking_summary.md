# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateParser.java', 304), ('FastDateParser.java', 307), ('FastDateParser.java', 308), ('FastDateParser.java', 309), ('FastDateParser.java', 310), ('FastDateParser.java', 311), ('FastDateParser.java', 312), ('FastDateParser.java', 313), ('FastDateParser.java', 314)]

Ground_Truth_Answerable: True

- SBFL   ranked 1209 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | FastDateParser.java:180 | 0.57735 | `return parsePattern;` |
| 2 | 4 | FastDateParser.java:685 | 0.19245 | `KeyValue[] textKeyValues= parser.getDisplayNames(field);` |
| 2 | 4 | FastDateParser.java:686 | 0.19245 | `int idx= Arrays.binarySearch(textKeyValues, new KeyValue(value, -1), IGNORE_CASE_COMPARATOR);` |
| 2 | 4 | FastDateParser.java:687 | 0.19245 | `if(idx<0) {` |
| 2 | 4 | FastDateParser.java:696 | 0.19245 | `cal.set(field, textKeyValues[idx].value);` |
| 6 | 1 | FastDateParser.java:850 | 0.154303 | `return iValue-1;` |
| 7 | 3 | FastDateParser.java:250 | 0.140028 | `Date date= parse(source, new ParsePosition(0));` |
| 7 | 3 | FastDateParser.java:251 | 0.140028 | `if(date==null) {` |
| 7 | 3 | FastDateParser.java:260 | 0.140028 | `return date;` |
| 10 | 11 | FastDateParser.java:276 | 0.136083 | `int offset= pos.getIndex();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

