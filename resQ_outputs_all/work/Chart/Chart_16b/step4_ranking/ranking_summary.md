# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultIntervalCategoryDataset.java', 207), ('DefaultIntervalCategoryDataset.java', 208), ('DefaultIntervalCategoryDataset.java', 338)]

Ground_Truth_Answerable: True

- SBFL   ranked 3369 statement(s)
- Hybrid ranked 65 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DefaultIntervalCategoryDataset.java:207 | 0.755929 | `this.seriesKeys = null;` |
| 1 | 2 | DefaultIntervalCategoryDataset.java:208 | 0.755929 | `this.categoryKeys = null;` |
| 3 | 24 | AbstractDataset.java:94 | 0.617213 | `protected AbstractDataset() {` |
| 3 | 24 | AbstractDataset.java:95 | 0.617213 | `this.group = new DatasetGroup();` |
| 3 | 24 | AbstractDataset.java:96 | 0.617213 | `this.listenerList = new EventListenerList();` |
| 3 | 24 | AbstractSeriesDataset.java:65 | 0.617213 | `super();` |
| 3 | 24 | DataPackageResources.java:50 | 0.617213 | `public class DataPackageResources extends ListResourceBundle {` |
| 3 | 24 | DataPackageResources.java:62 | 0.617213 | `private static final Object[][] CONTENTS = {` |
| 3 | 24 | DataUtilities.java:125 | 0.617213 | `if (data == null) {` |
| 3 | 24 | DataUtilities.java:128 | 0.617213 | `int l1 = data.length;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | DataUtilities.java:128 | 0.400892 | `int l1 = data.length;` |
| 1 | 6 | DataUtilities.java:129 | 0.400892 | `Number[][] result = new Number[l1][];` |
| 1 | 6 | DataUtilities.java:133 | 0.400892 | `return result;` |
| 1 | 6 | DefaultIntervalCategoryDataset.java:91 | 0.400892 | `this(DataUtilities.createNumberArray2D(starts),` |
| 1 | 6 | DefaultIntervalCategoryDataset.java:107 | 0.400892 | `this(null, null, starts, ends);` |
| 1 | 6 | DefaultIntervalCategoryDataset.java:147 | 0.400892 | `this.startData = starts;` |
| 7 | 3 | DefaultIntervalCategoryDataset.java:207 | 0.353553 | `this.seriesKeys = null;` |
| 7 | 3 | DefaultIntervalCategoryDataset.java:208 | 0.353553 | `this.categoryKeys = null;` |
| 7 | 3 | DefaultIntervalCategoryDataset.java:338 | 0.353553 | `if (categoryKeys.length != this.startData[0].length) {` |
| 10 | 6 | AbstractDataset.java:94 | 0.288675 | `protected AbstractDataset() {` |

