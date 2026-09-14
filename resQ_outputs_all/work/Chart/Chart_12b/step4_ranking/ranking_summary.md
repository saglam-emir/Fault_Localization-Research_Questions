# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultiplePiePlot.java', 145)]

Ground_Truth_Answerable: True

- SBFL   ranked 11238 statement(s)
- Hybrid ranked 717 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | MultiplePiePlot.java:166 | 0.57735 | `return this.dataset;` |
| 2 | 3 | AbstractDataset.java:160 | 0.333333 | `List list = Arrays.asList(this.listenerList.getListenerList());` |
| 2 | 3 | AbstractDataset.java:161 | 0.333333 | `return list.contains(listener);` |
| 2 | 3 | MultiplePiePlot.java:135 | 0.333333 | `this(null);` |
| 5 | 22 | JFreeChart.java:664 | 0.288675 | `removeSubtitle(getLegend());` |
| 5 | 22 | JFreeChart.java:795 | 0.288675 | `this.subtitles.remove(title);` |
| 5 | 22 | JFreeChart.java:796 | 0.288675 | `fireChartChanged();` |
| 5 | 22 | LegendTitle.java:542 | 0.288675 | `return true;` |
| 5 | 22 | MultiplePiePlot.java:111 | 0.288675 | `private double limit = 0.0;` |
| 5 | 22 | MultiplePiePlot.java:144 | 0.288675 | `super();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DefaultCategoryDataset.java:73 | 0.707107 | `public DefaultCategoryDataset() {` |
| 2 | 1 | AbstractDataset.java:94 | 0.333333 | `protected AbstractDataset() {` |
| 3 | 715 | AbstractBlock.java:109 | 0.0 | `protected AbstractBlock() {` |
| 3 | 715 | AbstractBlock.java:110 | 0.0 | `this.id = null;` |
| 3 | 715 | AbstractBlock.java:111 | 0.0 | `this.width = 0.0;` |
| 3 | 715 | AbstractBlock.java:112 | 0.0 | `this.height = 0.0;` |
| 3 | 715 | AbstractBlock.java:113 | 0.0 | `this.bounds = new Rectangle2D.Float();` |
| 3 | 715 | AbstractBlock.java:114 | 0.0 | `this.margin = RectangleInsets.ZERO_INSETS;` |
| 3 | 715 | AbstractBlock.java:115 | 0.0 | `this.frame = BlockBorder.NONE;` |
| 3 | 715 | AbstractBlock.java:116 | 0.0 | `this.padding = RectangleInsets.ZERO_INSETS;` |

