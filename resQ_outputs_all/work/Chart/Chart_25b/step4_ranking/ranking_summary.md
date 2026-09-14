# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StatisticalBarRenderer.java', 259), ('StatisticalBarRenderer.java', 315), ('StatisticalBarRenderer.java', 344), ('StatisticalBarRenderer.java', 403), ('StatisticalBarRenderer.java', 459), ('StatisticalBarRenderer.java', 487)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('source/org/jfree/chart/renderer/category/StatisticalBarRenderer.java', 259), ('source/org/jfree/chart/renderer/category/StatisticalBarRenderer.java', 344), ('source/org/jfree/chart/renderer/category/StatisticalBarRenderer.java', 403), ('source/org/jfree/chart/renderer/category/StatisticalBarRenderer.java', 487)]

- SBFL   ranked 3503 statement(s)
- Hybrid ranked 362 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2546 | AbstractBlock.java:111 | 0.894427 | `protected AbstractBlock() {` |
| 1 | 2546 | AbstractBlock.java:112 | 0.894427 | `this.id = null;` |
| 1 | 2546 | AbstractBlock.java:113 | 0.894427 | `this.width = 0.0;` |
| 1 | 2546 | AbstractBlock.java:114 | 0.894427 | `this.height = 0.0;` |
| 1 | 2546 | AbstractBlock.java:115 | 0.894427 | `this.bounds = new Rectangle2D.Float();` |
| 1 | 2546 | AbstractBlock.java:116 | 0.894427 | `this.margin = RectangleInsets.ZERO_INSETS;` |
| 1 | 2546 | AbstractBlock.java:117 | 0.894427 | `this.frame = BlockBorder.NONE;` |
| 1 | 2546 | AbstractBlock.java:118 | 0.894427 | `this.padding = RectangleInsets.ZERO_INSETS;` |
| 1 | 2546 | AbstractBlock.java:211 | 0.894427 | `if (margin == null) {` |
| 1 | 2546 | AbstractBlock.java:214 | 0.894427 | `this.margin = margin;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 330 | AbstractCategoryItemRenderer.java:230 | 1.0 | `protected AbstractCategoryItemRenderer() {` |
| 1 | 330 | AbstractCategoryItemRenderer.java:231 | 1.0 | `this.itemLabelGeneratorList = new ObjectList();` |
| 1 | 330 | AbstractCategoryItemRenderer.java:248 | 1.0 | `return 1;` |
| 1 | 330 | AbstractDataset.java:96 | 1.0 | `protected AbstractDataset() {` |
| 1 | 330 | AbstractDataset.java:97 | 1.0 | `this.group = new DatasetGroup();` |
| 1 | 330 | AbstractDataset.java:98 | 1.0 | `this.listenerList = new EventListenerList();` |
| 1 | 330 | AbstractDataset.java:134 | 1.0 | `this.listenerList.add(DatasetChangeListener.class, listener);` |
| 1 | 330 | AbstractDataset.java:172 | 1.0 | `notifyListeners(new DatasetChangeEvent(this, this));` |
| 1 | 330 | AbstractObjectList.java:68 | 1.0 | `private int size = 0;` |
| 1 | 330 | AbstractObjectList.java:71 | 1.0 | `private int increment = DEFAULT_INITIAL_CAPACITY;` |

