# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Axis.java', 1192), ('Axis.java', 1197)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Axis.java', 1197, '->', 1190)]

Ground_Truth_Answerable: True

- SBFL   ranked 14297 statement(s)
- Hybrid ranked 367 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | CategoryPlot.java:2547 | 0.957427 | `state = new PlotRenderingInfo(null);` |
| 2 | 130 | AxisState.java:184 | 0.916667 | `return this.max;` |
| 2 | 130 | AxisState.java:193 | 0.916667 | `this.max = max;` |
| 2 | 130 | CategoryAxis.java:736 | 0.916667 | `if (space == null) {` |
| 2 | 130 | CategoryAxis.java:741 | 0.916667 | `if (!isVisible()) {` |
| 2 | 130 | CategoryAxis.java:746 | 0.916667 | `double tickLabelHeight = 0.0;` |
| 2 | 130 | CategoryAxis.java:747 | 0.916667 | `double tickLabelWidth = 0.0;` |
| 2 | 130 | CategoryAxis.java:748 | 0.916667 | `if (isTickLabelsVisible()) {` |
| 2 | 130 | CategoryAxis.java:749 | 0.916667 | `g2.setFont(getTickLabelFont());` |
| 2 | 130 | CategoryAxis.java:750 | 0.916667 | `AxisState state = new AxisState();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 26 | AbstractObjectList.java:111 | 0.953463 | `result = this.objects[index];` |
| 1 | 26 | AbstractObjectList.java:113 | 0.953463 | `return result;` |
| 1 | 26 | AbstractObjectList.java:132 | 0.953463 | `this.size = Math.max(this.size, index + 1);` |
| 1 | 26 | AbstractObjectList.java:149 | 0.953463 | `return this.size;` |
| 1 | 26 | Axis.java:276 | 0.953463 | `this.visible = DEFAULT_AXIS_VISIBLE;` |
| 1 | 26 | Axis.java:314 | 0.953463 | `return this.visible;` |
| 1 | 26 | Axis.java:1191 | 0.953463 | `ChartRenderingInfo owner = plotState.getOwner();` |
| 1 | 26 | Axis.java:1192 | 0.953463 | `EntityCollection entities = owner.getEntityCollection();` |
| 1 | 26 | AxisCollection.java:132 | 0.953463 | `if (edge == RectangleEdge.TOP) {` |
| 1 | 26 | AxisLocation.java:63 | 0.953463 | `public static final AxisLocation TOP_OR_LEFT = new AxisLocation(` |

