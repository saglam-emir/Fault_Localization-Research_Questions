# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TimeSeries.java', 857)]

Ground_Truth_Answerable: True

- SBFL   ranked 6375 statement(s)
- Hybrid ranked 67 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TimeSeries.java:880 | 0.5 | `throw new IllegalArgumentException("Requires start <= end.");` |
| 2 | 1 | TimeSeries.java:857 | 0.408248 | `Object clone = createCopy(0, getItemCount() - 1);` |
| 3 | 2 | TimeSeries.java:876 | 0.316228 | `if (start < 0) {` |
| 3 | 2 | TimeSeries.java:879 | 0.316228 | `if (end < start) {` |
| 5 | 1 | TimeSeries.java:140 | 0.213201 | `this(name, DEFAULT_DOMAIN_DESCRIPTION, DEFAULT_RANGE_DESCRIPTION,` |
| 6 | 1 | TimeSeries.java:141 | 0.204124 | `Day.class);` |
| 7 | 4 | Day.java:83 | 0.182574 | `protected static final DateFormat DATE_FORMAT` |
| 7 | 4 | Day.java:88 | 0.182574 | `DATE_FORMAT_SHORT = DateFormat.getDateInstance(DateFormat.SHORT);` |
| 7 | 4 | Day.java:92 | 0.182574 | `DATE_FORMAT_MEDIUM = DateFormat.getDateInstance(DateFormat.MEDIUM);` |
| 7 | 4 | Day.java:96 | 0.182574 | `DATE_FORMAT_LONG = DateFormat.getDateInstance(DateFormat.LONG);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 67 | Day.java:122 | 0.0 | `public Day(int day, int month, int year) {` |
| 1 | 67 | Day.java:123 | 0.0 | `this.serialDate = SerialDate.createInstance(day, month, year);` |
| 1 | 67 | Day.java:404 | 0.0 | `if (o1 instanceof Day) {` |
| 1 | 67 | Day.java:406 | 0.0 | `result = -d.getSerialDate().compare(this.serialDate);` |
| 1 | 67 | Day.java:423 | 0.0 | `return result;` |
| 1 | 67 | RegularTimePeriod.java:70 | 0.0 | `public abstract class RegularTimePeriod implements TimePeriod, Comparable,` |
| 1 | 67 | SerialDate.java:145 | 0.0 | `static final int[] AGGREGATE_DAYS_TO_END_OF_PRECEDING_MONTH =` |
| 1 | 67 | SerialDate.java:526 | 0.0 | `final int leap4 = (yyyy - 1896) / 4;` |
| 1 | 67 | SerialDate.java:527 | 0.0 | `final int leap100 = (yyyy - 1800) / 100;` |
| 1 | 67 | SerialDate.java:528 | 0.0 | `final int leap400 = (yyyy - 1600) / 400;` |

