# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TimeSeries.java', 944)]

Ground_Truth_Answerable: True

- SBFL   ranked 6456 statement(s)
- Hybrid ranked 2 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | TimeSeries.java:883 | 0.5 | `throw new IllegalArgumentException("Requires start <= end.");` |
| 1 | 16 | TimeSeries.java:921 | 0.5 | `if (start == null) {` |
| 1 | 16 | TimeSeries.java:924 | 0.5 | `if (end == null) {` |
| 1 | 16 | TimeSeries.java:927 | 0.5 | `if (start.compareTo(end) > 0) {` |
| 1 | 16 | TimeSeries.java:931 | 0.5 | `boolean emptyRange = false;` |
| 1 | 16 | TimeSeries.java:932 | 0.5 | `int startIndex = getIndex(start);` |
| 1 | 16 | TimeSeries.java:933 | 0.5 | `if (startIndex < 0) {` |
| 1 | 16 | TimeSeries.java:934 | 0.5 | `startIndex = -(startIndex + 1);` |
| 1 | 16 | TimeSeries.java:935 | 0.5 | `if (startIndex == this.data.size()) {` |
| 1 | 16 | TimeSeries.java:939 | 0.5 | `int endIndex = getIndex(end);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Day.java:122 | 1.0 | `public Day(int day, int month, int year) {` |
| 1 | 2 | RegularTimePeriod.java:70 | 1.0 | `public abstract class RegularTimePeriod implements TimePeriod, Comparable,` |

