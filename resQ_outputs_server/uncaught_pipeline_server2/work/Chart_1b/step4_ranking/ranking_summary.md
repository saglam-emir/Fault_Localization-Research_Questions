# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('AbstractCategoryItemRenderer.java', 1797)]

Ground_Truth_Answerable: True

- SBFL   ranked 15150 statement(s)
- Hybrid ranked 833 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | AbstractCategoryItemRenderer.java:1793 | 0.57735 | `return result;` |
| 2 | 1 | CategoryPlot.java:1613 | 0.258199 | `setRenderer(0, renderer, true);` |
| 3 | 10 | CategoryPlot.java:1665 | 0.204124 | `CategoryItemRenderer existing` |
| 3 | 10 | CategoryPlot.java:1667 | 0.204124 | `if (existing != null) {` |
| 3 | 10 | CategoryPlot.java:1672 | 0.204124 | `this.renderers.set(index, renderer);` |
| 3 | 10 | CategoryPlot.java:1673 | 0.204124 | `if (renderer != null) {` |
| 3 | 10 | CategoryPlot.java:1674 | 0.204124 | `renderer.setPlot(this);` |
| 3 | 10 | CategoryPlot.java:1675 | 0.204124 | `renderer.addChangeListener(this);` |
| 3 | 10 | CategoryPlot.java:1678 | 0.204124 | `configureDomainAxes();` |
| 3 | 10 | CategoryPlot.java:1679 | 0.204124 | `configureRangeAxes();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | AbstractCategoryItemRenderer.java:1791 | 1.0 | `LegendItemCollection result = new LegendItemCollection();` |
| 1 | 15 | AbstractCategoryItemRenderer.java:1792 | 1.0 | `if (this.plot == null) {` |
| 1 | 15 | AbstractCategoryItemRenderer.java:1795 | 1.0 | `int index = this.plot.getIndexOf(this);` |
| 1 | 15 | AbstractCategoryItemRenderer.java:1796 | 1.0 | `CategoryDataset dataset = this.plot.getDataset(index);` |
| 1 | 15 | AbstractCategoryItemRenderer.java:1797 | 1.0 | `if (dataset != null) {` |
| 1 | 15 | AbstractCategoryItemRenderer.java:1798 | 1.0 | `return result;` |
| 1 | 15 | CategoryPlot.java:600 | 1.0 | `this.datasets.set(0, dataset);` |
| 1 | 15 | CategoryPlot.java:1321 | 1.0 | `if (this.datasets.size() > index) {` |
| 1 | 15 | CategoryPlot.java:1322 | 1.0 | `result = (CategoryDataset) this.datasets.get(index);` |
| 1 | 15 | CategoryPlot.java:1324 | 1.0 | `return result;` |

