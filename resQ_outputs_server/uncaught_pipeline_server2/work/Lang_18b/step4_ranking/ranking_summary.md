# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateFormat.java', 495), ('FastDateFormat.java', 496), ('FastDateFormat.java', 498)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('FastDateFormat.java', 495, '->', 494)]

Ground_Truth_Answerable: True

- SBFL   ranked 967 statement(s)
- Hybrid ranked 120 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | FastDateFormat.java:492 | 0.57735 | `rule = new TextField(Calendar.ERA, ERAs);` |
| 1 | 10 | FastDateFormat.java:493 | 0.57735 | `break;` |
| 1 | 10 | FastDateFormat.java:556 | 0.57735 | `rule = new TimeZoneNameRule(mTimeZone, mLocale, TimeZone.LONG);` |
| 1 | 10 | FastDateFormat.java:696 | 0.57735 | `return format(new Date(millis));` |
| 1 | 10 | FastDateFormat.java:1405 | 0.57735 | `if (mTimeZone.useDaylightTime() && calendar.get(Calendar.DST_OFFSET) != 0) {` |
| 1 | 10 | FastDateFormat.java:1408 | 0.57735 | `buffer.append(mStandard);` |
| 1 | 10 | FastDateFormat.java:1506 | 0.57735 | `if (this == obj) {` |
| 1 | 10 | FastDateFormat.java:1509 | 0.57735 | `if (obj instanceof TimeZoneDisplayKey) {` |
| 1 | 10 | FastDateFormat.java:1510 | 0.57735 | `TimeZoneDisplayKey other = (TimeZoneDisplayKey)obj;` |
| 1 | 10 | FastDateFormat.java:1511 | 0.57735 | `return` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 120 | FastDateFormat.java:107 | 0.0 | `private static final FormatCache<FastDateFormat> cache= new FormatCache<FastDateFormat>() {` |
| 1 | 120 | FastDateFormat.java:110 | 0.0 | `return new FastDateFormat(pattern, timeZone, locale);` |
| 1 | 120 | FastDateFormat.java:159 | 0.0 | `return cache.getInstance(pattern, null, null);` |
| 1 | 120 | FastDateFormat.java:188 | 0.0 | `return cache.getInstance(pattern, null, locale);` |
| 1 | 120 | FastDateFormat.java:235 | 0.0 | `return cache.getDateTimeInstance(style, null, null, locale);` |
| 1 | 120 | FastDateFormat.java:432 | 0.0 | `protected FastDateFormat(String pattern, TimeZone timeZone, Locale locale) {` |
| 1 | 120 | FastDateFormat.java:433 | 0.0 | `mPattern = pattern;` |
| 1 | 120 | FastDateFormat.java:434 | 0.0 | `mTimeZone = timeZone;` |
| 1 | 120 | FastDateFormat.java:435 | 0.0 | `mLocale = locale;` |
| 1 | 120 | FastDateFormat.java:437 | 0.0 | `init();` |

