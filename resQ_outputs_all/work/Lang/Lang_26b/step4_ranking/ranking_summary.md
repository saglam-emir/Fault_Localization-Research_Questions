# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateFormat.java', 820)]

Ground_Truth_Answerable: True

- SBFL   ranked 973 statement(s)
- Hybrid ranked 100 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | FastDateFormat.java:654 | 0.57735 | `rule = selectNumberRule(Calendar.WEEK_OF_YEAR, tokenLen);` |
| 1 | 2 | FastDateFormat.java:655 | 0.57735 | `break;` |
| 3 | 2 | FastDateFormat.java:1130 | 0.408248 | `buffer.append(mValue);` |
| 3 | 2 | FastDateFormat.java:1171 | 0.408248 | `buffer.append(mValues[calendar.get(mField)]);` |
| 5 | 3 | FastDateFormat.java:820 | 0.103695 | `Calendar c = new GregorianCalendar(mTimeZone);` |
| 5 | 3 | FastDateFormat.java:821 | 0.103695 | `c.setTime(date);` |
| 5 | 3 | FastDateFormat.java:822 | 0.103695 | `return applyRules(c, new StringBuffer(mMaxLengthEstimate)).toString();` |
| 8 | 14 | FastDateFormat.java:196 | 0.096225 | `return getInstance(pattern, null, locale);` |
| 8 | 14 | FastDateFormat.java:645 | 0.096225 | `rule = new TextField(Calendar.DAY_OF_WEEK, tokenLen < 4 ? shortWeekdays : weekdays);` |
| 8 | 14 | FastDateFormat.java:646 | 0.096225 | `break;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | FastDateFormat.java:196 | 1.0 | `return getInstance(pattern, null, locale);` |
| 1 | 16 | FastDateFormat.java:584 | 1.0 | `String[] weekdays = symbols.getWeekdays();` |
| 1 | 16 | FastDateFormat.java:645 | 1.0 | `rule = new TextField(Calendar.DAY_OF_WEEK, tokenLen < 4 ? shortWeekdays : weekdays);` |
| 1 | 16 | FastDateFormat.java:687 | 1.0 | `rule = new StringLiteral(sub);` |
| 1 | 16 | FastDateFormat.java:723 | 1.0 | `i++;` |
| 1 | 16 | FastDateFormat.java:738 | 1.0 | `if (i + 1 < length && pattern.charAt(i + 1) == '\'') {` |
| 1 | 16 | FastDateFormat.java:743 | 1.0 | `inLiteral = !inLiteral;` |
| 1 | 16 | FastDateFormat.java:820 | 1.0 | `Calendar c = new GregorianCalendar(mTimeZone);` |
| 1 | 16 | FastDateFormat.java:822 | 1.0 | `return applyRules(c, new StringBuffer(mMaxLengthEstimate)).toString();` |
| 1 | 16 | FastDateFormat.java:1116 | 1.0 | `mValue = value;` |

