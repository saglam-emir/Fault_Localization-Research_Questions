# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TimeSeries.java', 1057)]

Ground_Truth_Answerable: True

- SBFL   ranked 7320 statement(s)
- Hybrid ranked 233 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | TimeSeries.java:1050 | 0.408248 | `if (start < 0) {` |
| 1 | 10 | TimeSeries.java:1053 | 0.408248 | `if (end < start) {` |
| 1 | 10 | TimeSeries.java:1056 | 0.408248 | `TimeSeries copy = (TimeSeries) super.clone();` |
| 1 | 10 | TimeSeries.java:1057 | 0.408248 | `copy.data = new java.util.ArrayList();` |
| 1 | 10 | TimeSeries.java:1058 | 0.408248 | `if (this.data.size() > 0) {` |
| 1 | 10 | TimeSeries.java:1059 | 0.408248 | `for (int index = start; index <= end; index++) {` |
| 1 | 10 | TimeSeries.java:1060 | 0.408248 | `TimeSeriesDataItem item` |
| 1 | 10 | TimeSeries.java:1062 | 0.408248 | `TimeSeriesDataItem clone = (TimeSeriesDataItem) item.clone();` |
| 1 | 10 | TimeSeries.java:1064 | 0.408248 | `copy.add(clone);` |
| 1 | 10 | TimeSeries.java:1071 | 0.408248 | `return copy;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | Series.java:244 | 0.707107 | `clone.listeners = new EventListenerList();` |
| 1 | 13 | Series.java:245 | 0.707107 | `clone.propertyChangeSupport = new PropertyChangeSupport(clone);` |
| 1 | 13 | Series.java:246 | 0.707107 | `return clone;` |
| 1 | 13 | TimeSeries.java:564 | 0.707107 | `add(item, true);` |
| 1 | 13 | TimeSeries.java:1053 | 0.707107 | `if (end < start) {` |
| 1 | 13 | TimeSeries.java:1056 | 0.707107 | `TimeSeries copy = (TimeSeries) super.clone();` |
| 1 | 13 | TimeSeries.java:1057 | 0.707107 | `copy.data = new java.util.ArrayList();` |
| 1 | 13 | TimeSeries.java:1058 | 0.707107 | `if (this.data.size() > 0) {` |
| 1 | 13 | TimeSeries.java:1059 | 0.707107 | `for (int index = start; index <= end; index++) {` |
| 1 | 13 | TimeSeries.java:1060 | 0.707107 | `TimeSeriesDataItem item` |

