# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XYPlot.java', 4493), ('XYPlot.java', 4501)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('XYPlot.java', 4501, '->', 4472)]

Ground_Truth_Answerable: True

- SBFL   ranked 15206 statement(s)
- Hybrid ranked 1034 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | DatasetUtilities.java:647 | 0.957427 | `return findDomainBounds(dataset, true);` |
| 1 | 2 | XYPlot.java:4479 | 0.957427 | `result = Range.combine(result,` |
| 3 | 17 | XYSeries.java:192 | 0.870388 | `return this.minX;` |
| 3 | 17 | XYSeries.java:207 | 0.870388 | `return this.maxX;` |
| 3 | 17 | XYSeriesCollection.java:577 | 0.870388 | `if (includeInterval) {` |
| 3 | 17 | XYSeriesCollection.java:578 | 0.870388 | `return this.intervalDelegate.getDomainBounds(includeInterval);` |
| 3 | 17 | XYSeriesCollection.java:581 | 0.870388 | `double lower = Double.POSITIVE_INFINITY;` |
| 3 | 17 | XYSeriesCollection.java:582 | 0.870388 | `double upper = Double.NEGATIVE_INFINITY;` |
| 3 | 17 | XYSeriesCollection.java:583 | 0.870388 | `int seriesCount = getSeriesCount();` |
| 3 | 17 | XYSeriesCollection.java:584 | 0.870388 | `for (int s = 0; s < seriesCount; s++) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | PlotOrientation.java:61 | 0.550019 | `public static final PlotOrientation VERTICAL` |
| 1 | 3 | PlotOrientation.java:72 | 0.550019 | `private PlotOrientation(String name) {` |
| 1 | 3 | PlotOrientation.java:73 | 0.550019 | `this.name = name;` |
| 4 | 174 | ChartFactory.java:1729 | 0.377964 | `NumberAxis xAxis = new NumberAxis(xAxisLabel);` |
| 4 | 174 | ChartFactory.java:1730 | 0.377964 | `xAxis.setAutoRangeIncludesZero(false);` |
| 4 | 174 | ChartFactory.java:1731 | 0.377964 | `NumberAxis yAxis = new NumberAxis(yAxisLabel);` |
| 4 | 174 | ChartFactory.java:1732 | 0.377964 | `XYItemRenderer renderer = new XYLineAndShapeRenderer(true, false);` |
| 4 | 174 | ChartFactory.java:1733 | 0.377964 | `XYPlot plot = new XYPlot(dataset, xAxis, yAxis, renderer);` |
| 4 | 174 | ChartFactory.java:1734 | 0.377964 | `plot.setOrientation(orientation);` |
| 4 | 174 | ChartFactory.java:1742 | 0.377964 | `JFreeChart chart = new JFreeChart(title, JFreeChart.DEFAULT_TITLE_FONT,` |

