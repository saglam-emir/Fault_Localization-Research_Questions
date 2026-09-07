# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDatePrinter.java', 1098), ('FastDatePrinter.java', 1112), ('FastDatePrinter.java', 1134)]

Ground_Truth_Answerable: True

- SBFL   ranked 1151 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | FastDateParser.java:570 | 0.57735 | `return false;` |
| 1 | 5 | FastDatePrinter.java:1004 | 0.57735 | `int value = calendar.get(Calendar.HOUR);` |
| 1 | 5 | FastDatePrinter.java:1005 | 0.57735 | `if (value == 0) {` |
| 1 | 5 | FastDatePrinter.java:1006 | 0.57735 | `value = calendar.getLeastMaximum(Calendar.HOUR) + 1;` |
| 1 | 5 | FastDatePrinter.java:1008 | 0.57735 | `mRule.appendTo(buffer, value);` |
| 6 | 2 | FastDatePrinter.java:1134 | 0.408248 | `if (zone.useDaylightTime()` |
| 6 | 2 | FastDatePrinter.java:1138 | 0.408248 | `buffer.append(getTimeZoneDisplay(zone, false, mStyle, mLocale));` |
| 8 | 4 | FastDatePrinter.java:1238 | 0.333333 | `if (this == obj) {` |
| 8 | 4 | FastDatePrinter.java:1241 | 0.333333 | `if (obj instanceof TimeZoneDisplayKey) {` |
| 8 | 4 | FastDatePrinter.java:1242 | 0.333333 | `TimeZoneDisplayKey other = (TimeZoneDisplayKey)obj;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

