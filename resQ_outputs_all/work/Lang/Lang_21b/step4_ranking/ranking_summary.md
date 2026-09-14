# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DateUtils.java', 265)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DateUtils.java', 265, '->', 262)]

Ground_Truth_Answerable: True

- SBFL   ranked 634 statement(s)
- Hybrid ranked 14 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DateUtils.java:259 | 0.707107 | `if (cal1 == null || cal2 == null) {` |
| 1 | 2 | DateUtils.java:262 | 0.707107 | `return (cal1.get(Calendar.MILLISECOND) == cal2.get(Calendar.MILLISECOND) &&` |
| 3 | 2 | DateUtils.java:60 | 0.067729 | `public static final TimeZone UTC_TIME_ZONE = TimeZone.getTimeZone("GMT");` |
| 3 | 2 | DateUtils.java:88 | 0.067729 | `private static final int[][] fields = {` |
| 5 | 630 | DateFormatUtils.java:44 | 0.0 | `public static final FastDateFormat ISO_DATETIME_FORMAT` |
| 5 | 630 | DateFormatUtils.java:51 | 0.0 | `public static final FastDateFormat ISO_DATETIME_TIME_ZONE_FORMAT` |
| 5 | 630 | DateFormatUtils.java:58 | 0.0 | `public static final FastDateFormat ISO_DATE_FORMAT` |
| 5 | 630 | DateFormatUtils.java:67 | 0.0 | `public static final FastDateFormat ISO_DATE_TIME_ZONE_FORMAT` |
| 5 | 630 | DateFormatUtils.java:74 | 0.0 | `public static final FastDateFormat ISO_TIME_FORMAT` |
| 5 | 630 | DateFormatUtils.java:81 | 0.0 | `public static final FastDateFormat ISO_TIME_TIME_ZONE_FORMAT` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | DateUtils.java:179 | 0.0 | `Calendar cal1 = Calendar.getInstance();` |
| 1 | 14 | DateUtils.java:180 | 0.0 | `cal1.setTime(date1);` |
| 1 | 14 | DateUtils.java:181 | 0.0 | `Calendar cal2 = Calendar.getInstance();` |
| 1 | 14 | DateUtils.java:182 | 0.0 | `cal2.setTime(date2);` |
| 1 | 14 | DateUtils.java:183 | 0.0 | `return isSameDay(cal1, cal2);` |
| 1 | 14 | DateUtils.java:203 | 0.0 | `return (cal1.get(Calendar.ERA) == cal2.get(Calendar.ERA) &&` |
| 1 | 14 | DateUtils.java:224 | 0.0 | `return date1.getTime() == date2.getTime();` |
| 1 | 14 | DateUtils.java:242 | 0.0 | `return cal1.getTime().getTime() == cal2.getTime().getTime();` |
| 1 | 14 | DateUtils.java:1315 | 0.0 | `return getFragment(date, fragment, Calendar.SECOND);` |
| 1 | 14 | DateUtils.java:1355 | 0.0 | `return getFragment(date, fragment, Calendar.MINUTE);` |

