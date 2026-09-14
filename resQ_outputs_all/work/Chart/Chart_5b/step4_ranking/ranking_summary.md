# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XYSeries.java', 548), ('XYSeries.java', 544)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('source/org/jfree/data/xy/XYSeries.java', 544)]

- SBFL   ranked 9294 statement(s)
- Hybrid ranked 59 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | XYSeries.java:527 | 0.408248 | `return addOrUpdate(new Double(x), new Double(y));` |
| 1 | 2 | XYSeries.java:564 | 0.408248 | `this.data.add(-index - 1, new XYDataItem(x, y));` |
| 3 | 2 | XYSeries.java:563 | 0.333333 | `if (this.autoSort) {` |
| 3 | 2 | XYSeries.java:570 | 0.333333 | `if (getItemCount() > this.maximumItemCount) {` |
| 5 | 6 | XYSeries.java:541 | 0.288675 | `if (x == null) {` |
| 5 | 6 | XYSeries.java:546 | 0.288675 | `XYDataItem overwritten = null;` |
| 5 | 6 | XYSeries.java:547 | 0.288675 | `int index = indexOf(x);` |
| 5 | 6 | XYSeries.java:548 | 0.288675 | `if (index >= 0 && !this.allowDuplicateXValues) {` |
| 5 | 6 | XYSeries.java:574 | 0.288675 | `fireSeriesChanged();` |
| 5 | 6 | XYSeries.java:575 | 0.288675 | `return overwritten;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | XYSeries.java:527 | 0.447214 | `return addOrUpdate(new Double(x), new Double(y));` |
| 1 | 2 | XYSeries.java:546 | 0.447214 | `XYDataItem overwritten = null;` |
| 3 | 1 | XYSeries.java:575 | 0.377964 | `return overwritten;` |
| 4 | 1 | XYSeries.java:564 | 0.353553 | `this.data.add(-index - 1, new XYDataItem(x, y));` |
| 5 | 1 | XYSeries.java:590 | 0.333333 | `return Collections.binarySearch(this.data, new XYDataItem(x, null));` |
| 6 | 3 | XYSeries.java:548 | 0.288675 | `if (index >= 0 && !this.allowDuplicateXValues) {` |
| 6 | 3 | XYSeries.java:563 | 0.288675 | `if (this.autoSort) {` |
| 6 | 3 | XYSeries.java:570 | 0.288675 | `if (getItemCount() > this.maximumItemCount) {` |
| 9 | 2 | XYSeries.java:547 | 0.267261 | `int index = indexOf(x);` |
| 9 | 2 | XYSeries.java:574 | 0.267261 | `fireSeriesChanged();` |

