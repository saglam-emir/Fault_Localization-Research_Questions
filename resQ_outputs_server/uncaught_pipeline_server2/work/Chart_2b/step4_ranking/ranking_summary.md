# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DatasetUtilities.java', 755), ('DatasetUtilities.java', 757), ('DatasetUtilities.java', 759), ('DatasetUtilities.java', 761), ('DatasetUtilities.java', 1242), ('DatasetUtilities.java', 1244), ('DatasetUtilities.java', 1246), ('DatasetUtilities.java', 1248)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DatasetUtilities.java', 759, '->', 757), ('DatasetUtilities.java', 1246, '->', 1244)]

Ground_Truth_Answerable: True

- SBFL   ranked 16684 statement(s)
- Hybrid ranked 1167 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 21 | XYInterval.java:78 | 0.707107 | `double yHigh) {` |
| 1 | 21 | XYInterval.java:79 | 0.707107 | `this.xLow = xLow;` |
| 1 | 21 | XYInterval.java:80 | 0.707107 | `this.xHigh = xHigh;` |
| 1 | 21 | XYInterval.java:81 | 0.707107 | `this.y = y;` |
| 1 | 21 | XYInterval.java:82 | 0.707107 | `this.yLow = yLow;` |
| 1 | 21 | XYInterval.java:83 | 0.707107 | `this.yHigh = yHigh;` |
| 1 | 21 | XYIntervalDataItem.java:64 | 0.707107 | `super(new Double(x), new XYInterval(xLow, xHigh, y, yLow, yHigh));` |
| 1 | 21 | XYIntervalSeries.java:64 | 0.707107 | `this(key, true, true);` |
| 1 | 21 | XYIntervalSeries.java:79 | 0.707107 | `super(key, autoSort, allowDuplicateXValues);` |
| 1 | 21 | XYIntervalSeries.java:94 | 0.707107 | `super.add(new XYIntervalDataItem(x, xLow, xHigh, y, yLow, yHigh), true);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DatasetUtilities.java:780 | 0.707107 | `return null;` |
| 2 | 1 | DatasetUtilities.java:726 | 0.316228 | `return iterateDomainBounds(dataset, true);` |
| 3 | 1 | DatasetUtilities.java:1284 | 0.267261 | `return null;` |
| 4 | 3 | DatasetUtilities.java:745 | 0.162221 | `double minimum = Double.POSITIVE_INFINITY;` |
| 4 | 3 | DatasetUtilities.java:746 | 0.162221 | `double maximum = Double.NEGATIVE_INFINITY;` |
| 4 | 3 | DatasetUtilities.java:779 | 0.162221 | `if (minimum > maximum) {` |
| 7 | 1 | DatasetUtilities.java:1213 | 0.147442 | `return iterateRangeBounds(dataset, true);` |
| 8 | 2 | DatasetUtilities.java:1231 | 0.107833 | `double minimum = Double.POSITIVE_INFINITY;` |
| 8 | 2 | DatasetUtilities.java:1283 | 0.107833 | `if (minimum == Double.POSITIVE_INFINITY) {` |
| 10 | 1158 | AbstractCategoryDataset.java:64 | 0.0 | `super();` |

