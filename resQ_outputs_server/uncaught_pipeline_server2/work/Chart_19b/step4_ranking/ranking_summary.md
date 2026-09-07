# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CategoryPlot.java', 698), ('CategoryPlot.java', 973)]

Ground_Truth_Answerable: True

- SBFL   ranked 13155 statement(s)
- Hybrid ranked 586 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | CategoryPlot.java:698 | 0.5 | `return this.domainAxes.indexOf(axis);` |
| 1 | 6 | CategoryPlot.java:973 | 0.5 | `int result = this.rangeAxes.indexOf(axis);` |
| 1 | 6 | CategoryPlot.java:974 | 0.5 | `if (result < 0) { // try the parent plot` |
| 1 | 6 | CategoryPlot.java:975 | 0.5 | `Plot parent = getParent();` |
| 1 | 6 | CategoryPlot.java:976 | 0.5 | `if (parent instanceof CategoryPlot) {` |
| 1 | 6 | CategoryPlot.java:981 | 0.5 | `return result;` |
| 7 | 3 | CategoryPlot.java:657 | 0.223607 | `axis.setPlot(this);` |
| 7 | 3 | CategoryPlot.java:661 | 0.223607 | `axis.configure();` |
| 7 | 3 | CategoryPlot.java:662 | 0.223607 | `axis.addChangeListener(this);` |
| 10 | 1 | NumberAxis.java:431 | 0.182574 | `r = getDefaultAutoRange();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 586 | AbstractCategoryItemRenderer.java:228 | 0.0 | `protected AbstractCategoryItemRenderer() {` |
| 1 | 586 | AbstractCategoryItemRenderer.java:229 | 0.0 | `this.itemLabelGeneratorList = new ObjectList();` |
| 1 | 586 | AbstractDataset.java:94 | 0.0 | `protected AbstractDataset() {` |
| 1 | 586 | AbstractDataset.java:95 | 0.0 | `this.group = new DatasetGroup();` |
| 1 | 586 | AbstractDataset.java:96 | 0.0 | `this.listenerList = new EventListenerList();` |
| 1 | 586 | AbstractDataset.java:132 | 0.0 | `this.listenerList.add(DatasetChangeListener.class, listener);` |
| 1 | 586 | AbstractDataset.java:144 | 0.0 | `this.listenerList.remove(DatasetChangeListener.class, listener);` |
| 1 | 586 | AbstractDataset.java:170 | 0.0 | `notifyListeners(new DatasetChangeEvent(this, this));` |
| 1 | 586 | AbstractIntervalXYDataset.java:51 | 0.0 | `public abstract class AbstractIntervalXYDataset extends AbstractXYDataset` |
| 1 | 586 | AbstractObjectList.java:66 | 0.0 | `private int size = 0;` |

