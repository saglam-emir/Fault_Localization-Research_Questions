# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Week.java', 175)]

Ground_Truth_Answerable: True

- SBFL   ranked 95 statement(s)
- Hybrid ranked 52 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 14 | Week.java:175 | 0.57735 | `this(time, RegularTimePeriod.DEFAULT_TIME_ZONE, Locale.getDefault());` |
| 1 | 14 | Week.java:188 | 0.57735 | `public Week(Date time, TimeZone zone, Locale locale) {` |
| 1 | 14 | Week.java:189 | 0.57735 | `if (time == null) {` |
| 1 | 14 | Week.java:192 | 0.57735 | `if (zone == null) {` |
| 1 | 14 | Week.java:195 | 0.57735 | `if (locale == null) {` |
| 1 | 14 | Week.java:198 | 0.57735 | `Calendar calendar = Calendar.getInstance(zone, locale);` |
| 1 | 14 | Week.java:199 | 0.57735 | `calendar.setTime(time);` |
| 1 | 14 | Week.java:204 | 0.57735 | `int tempWeek = calendar.get(Calendar.WEEK_OF_YEAR);` |
| 1 | 14 | Week.java:205 | 0.57735 | `if (tempWeek == 1` |
| 1 | 14 | Week.java:211 | 0.57735 | `this.week = (byte) Math.min(tempWeek, LAST_WEEK_IN_YEAR);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | RegularTimePeriod.java:161 | 0.447214 | `public static final TimeZone DEFAULT_TIME_ZONE = TimeZone.getDefault();` |
| 1 | 10 | Week.java:175 | 0.447214 | `this(time, RegularTimePeriod.DEFAULT_TIME_ZONE, Locale.getDefault());` |
| 1 | 10 | Week.java:188 | 0.447214 | `public Week(Date time, TimeZone zone, Locale locale) {` |
| 1 | 10 | Week.java:198 | 0.447214 | `Calendar calendar = Calendar.getInstance(zone, locale);` |
| 1 | 10 | Week.java:199 | 0.447214 | `calendar.setTime(time);` |
| 1 | 10 | Week.java:204 | 0.447214 | `int tempWeek = calendar.get(Calendar.WEEK_OF_YEAR);` |
| 1 | 10 | Week.java:211 | 0.447214 | `this.week = (byte) Math.min(tempWeek, LAST_WEEK_IN_YEAR);` |
| 1 | 10 | Week.java:212 | 0.447214 | `int yyyy = calendar.get(Calendar.YEAR);` |
| 1 | 10 | Week.java:219 | 0.447214 | `this.year = (short) yyyy;` |
| 1 | 10 | Week.java:221 | 0.447214 | `peg(calendar);` |

