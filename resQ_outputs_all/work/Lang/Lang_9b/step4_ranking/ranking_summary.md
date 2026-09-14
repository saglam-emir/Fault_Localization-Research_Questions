# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateParser.java', 144)]

Ground_Truth_Answerable: True

- SBFL   ranked 1206 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | FastDateParser.java:180 | 0.57735 | `return parsePattern;` |
| 2 | 1 | FastDateParser.java:260 | 0.140028 | `return date;` |
| 3 | 11 | FastDateParser.java:250 | 0.136083 | `Date date= parse(source, new ParsePosition(0));` |
| 3 | 11 | FastDateParser.java:251 | 0.136083 | `if(date==null) {` |
| 3 | 11 | FastDateParser.java:282 | 0.136083 | `Calendar cal= Calendar.getInstance(timeZone, locale);` |
| 3 | 11 | FastDateParser.java:283 | 0.136083 | `cal.clear();` |
| 3 | 11 | FastDateParser.java:285 | 0.136083 | `for(int i=0; i<strategies.length;) {` |
| 3 | 11 | FastDateParser.java:286 | 0.136083 | `Strategy strategy= strategies[i++];` |
| 3 | 11 | FastDateParser.java:287 | 0.136083 | `strategy.setCalendar(this, cal, matcher.group(i));` |
| 3 | 11 | FastDateParser.java:289 | 0.136083 | `pos.setIndex(offset+matcher.end());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

