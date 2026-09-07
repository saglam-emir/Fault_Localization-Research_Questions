# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('PiePlot.java', 1378), ('PiePlot.java', 2051), ('PiePlot.java', 2053)]

Ground_Truth_Answerable: True

- SBFL   ranked 11201 statement(s)
- Hybrid ranked 9 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DatasetUtilities.java:153 | 0.57735 | `throw new IllegalArgumentException("Null 'dataset' argument.");` |
| 1 | 2 | PiePlot.java:2613 | 0.57735 | `return result;` |
| 3 | 23 | PiePlot.java:670 | 0.408248 | `return this.interiorGap;` |
| 3 | 23 | PiePlot.java:1398 | 0.408248 | `return this.labelGenerator;` |
| 3 | 23 | PiePlot.java:1423 | 0.408248 | `return this.labelGap;` |
| 3 | 23 | PiePlot.java:1448 | 0.408248 | `return this.maximumLabelWidth;` |
| 3 | 23 | PiePlot3D.java:230 | 0.408248 | `RectangleInsets insets = getInsets();` |
| 3 | 23 | PiePlot3D.java:231 | 0.408248 | `insets.trim(plotArea);` |
| 3 | 23 | PiePlot3D.java:233 | 0.408248 | `Rectangle2D originalPlotArea = (Rectangle2D) plotArea.clone();` |
| 3 | 23 | PiePlot3D.java:234 | 0.408248 | `if (info != null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | ChartFactory.java:694 | 1.0 | `PiePlot3D plot = new PiePlot3D(dataset);` |
| 1 | 9 | DatasetUtilities.java:152 | 1.0 | `if (dataset == null) {` |
| 1 | 9 | DatasetUtilities.java:153 | 1.0 | `throw new IllegalArgumentException("Null 'dataset' argument.");` |
| 1 | 9 | JFreeChart.java:1219 | 1.0 | `this.plot.draw(g2, plotArea, anchor, null, plotInfo);` |
| 1 | 9 | PiePlot.java:493 | 1.0 | `this.dataset = dataset;` |
| 1 | 9 | PiePlot.java:551 | 1.0 | `return this.dataset;` |
| 1 | 9 | PiePlot.java:2051 | 1.0 | `state.setTotal(DatasetUtilities.calculatePieDatasetTotal(` |
| 1 | 9 | PiePlot3D.java:151 | 1.0 | `super(dataset);` |
| 1 | 9 | PiePlot3D.java:280 | 1.0 | `PiePlotState state = initialise(g2, plotArea, this, null, info);` |

