# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MinMaxCategoryRenderer.java', 435)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('source/org/jfree/chart/renderer/category/MinMaxCategoryRenderer.java', 435)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 3194 statement(s)
- Hybrid ranked 30 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | AbstractRenderer.java:2339 | 1.0 | `Object[] ls = this.listenerList.getListenerList();` |
| 1 | 7 | AbstractRenderer.java:2340 | 1.0 | `for (int i = ls.length - 2; i >= 0; i -= 2) {` |
| 1 | 7 | MinMaxCategoryRenderer.java:169 | 1.0 | `if (this.plotLines != draw) {` |
| 1 | 7 | MinMaxCategoryRenderer.java:170 | 1.0 | `this.plotLines = draw;` |
| 1 | 7 | MinMaxCategoryRenderer.java:171 | 1.0 | `this.notifyListeners(new RendererChangeEvent(this));` |
| 1 | 7 | RendererChangeEvent.java:63 | 1.0 | `super(renderer);` |
| 1 | 7 | RendererChangeEvent.java:64 | 1.0 | `this.renderer = renderer;` |
| 8 | 9 | ChartChangeEvent.java:71 | 0.707107 | `this(source, null, ChartChangeEventType.GENERAL);` |
| 8 | 9 | ChartChangeEvent.java:95 | 0.707107 | `super(source);` |
| 8 | 9 | ChartChangeEvent.java:96 | 0.707107 | `this.chart = chart;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | AbstractCategoryItemRenderer.java:231 | 1.0 | `this.itemLabelGeneratorList = new ObjectList();` |
| 1 | 25 | AbstractCategoryItemRenderer.java:232 | 1.0 | `this.toolTipGeneratorList = new ObjectList();` |
| 1 | 25 | AbstractCategoryItemRenderer.java:233 | 1.0 | `this.urlGeneratorList = new ObjectList();` |
| 1 | 25 | AbstractCategoryItemRenderer.java:234 | 1.0 | `this.legendItemLabelGenerator` |
| 1 | 25 | AbstractCategoryItemRenderer.java:237 | 1.0 | `this.foregroundAnnotations = new ArrayList();` |
| 1 | 25 | AbstractObjectList.java:77 | 1.0 | `this(DEFAULT_INITIAL_CAPACITY);` |
| 1 | 25 | AbstractObjectList.java:86 | 1.0 | `this (initialCapacity, initialCapacity);` |
| 1 | 25 | AbstractObjectList.java:95 | 1.0 | `protected AbstractObjectList(int initialCapacity, int increment) {` |
| 1 | 25 | AbstractRenderer.java:355 | 1.0 | `this.basePositiveItemLabelPosition = new ItemLabelPosition(` |
| 1 | 25 | AbstractRenderer.java:358 | 1.0 | `this.negativeItemLabelPositionList = new ObjectList();` |

