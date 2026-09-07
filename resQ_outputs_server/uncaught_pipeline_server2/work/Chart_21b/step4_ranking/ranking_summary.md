# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultBoxAndWhiskerCategoryDataset.java', 157), ('DefaultBoxAndWhiskerCategoryDataset.java', 188), ('DefaultBoxAndWhiskerCategoryDataset.java', 741), ('DefaultBoxAndWhiskerCategoryDataset.java', 742)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('source/org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java', 157), ('source/org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java', 188), ('source/org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.java', 742)]

- SBFL   ranked 3942 statement(s)
- Hybrid ranked 48 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DefaultBoxAndWhiskerCategoryDataset.java:173 | 1.0 | `this.maximumRangeValue = maxval;` |
| 1 | 5 | DefaultBoxAndWhiskerCategoryDataset.java:174 | 1.0 | `this.maximumRangeValueRow = r;` |
| 1 | 5 | DefaultBoxAndWhiskerCategoryDataset.java:175 | 1.0 | `this.maximumRangeValueColumn = c;` |
| 1 | 5 | Range.java:335 | 1.0 | `return false;` |
| 1 | 5 | Range.java:365 | 1.0 | `return ("Range[" + this.lower + "," + this.upper + "]");` |
| 6 | 7 | DefaultBoxAndWhiskerCategoryDataset.java:155 | 0.707107 | `updateBounds();` |
| 6 | 7 | DefaultBoxAndWhiskerCategoryDataset.java:183 | 0.707107 | `else if (minval < this.minimumRangeValue) {` |
| 6 | 7 | DefaultBoxAndWhiskerCategoryDataset.java:740 | 0.707107 | `this.minimumRangeValue = Double.NaN;` |
| 6 | 7 | DefaultBoxAndWhiskerCategoryDataset.java:741 | 0.707107 | `this.maximumRangeValue = Double.NaN;` |
| 6 | 7 | KeyedObject.java:103 | 0.707107 | `this.object = object;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | BoxAndWhiskerItem.java:147 | 0.377964 | `this(new Double(mean), new Double(median), new Double(q1),` |
| 2 | 3 | Range.java:85 | 0.288675 | `public Range(double lower, double upper) {` |
| 2 | 3 | Range.java:91 | 0.288675 | `this.lower = lower;` |
| 2 | 3 | Range.java:92 | 0.288675 | `this.upper = upper;` |
| 5 | 44 | AbstractDataset.java:96 | 0.0 | `protected AbstractDataset() {` |
| 5 | 44 | AbstractDataset.java:97 | 0.0 | `this.group = new DatasetGroup();` |
| 5 | 44 | AbstractDataset.java:98 | 0.0 | `this.listenerList = new EventListenerList();` |
| 5 | 44 | AbstractDataset.java:172 | 0.0 | `notifyListeners(new DatasetChangeEvent(this, this));` |
| 5 | 44 | BoxAndWhiskerItem.java:121 | 0.0 | `this.minOutlier = minOutlier;` |
| 5 | 44 | BoxAndWhiskerItem.java:122 | 0.0 | `this.maxOutlier = maxOutlier;` |

