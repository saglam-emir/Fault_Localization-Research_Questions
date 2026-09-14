# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BorderArrangement.java', 455)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BorderArrangement.java', 455, '->', 454)]

Ground_Truth_Answerable: True

- SBFL   ranked 11808 statement(s)
- Hybrid ranked 144 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 66 | AbstractBlock.java:438 | 0.707107 | `return null;` |
| 1 | 66 | AbstractBlock.java:443 | 0.707107 | `lowerBound = trimToContentWidth(r.getLowerBound());` |
| 1 | 66 | AbstractBlock.java:453 | 0.707107 | `return null;` |
| 1 | 66 | BorderArrangement.java:147 | 0.707107 | `else if (w == LengthConstraintType.FIXED) {` |
| 1 | 66 | BorderArrangement.java:148 | 0.707107 | `if (h == LengthConstraintType.NONE) {` |
| 1 | 66 | BorderArrangement.java:149 | 0.707107 | `contentSize = arrangeFN(container, g2, constraint.getWidth());` |
| 1 | 66 | BorderArrangement.java:151 | 0.707107 | `else if (h == LengthConstraintType.FIXED) {` |
| 1 | 66 | BorderArrangement.java:152 | 0.707107 | `contentSize = arrangeFF(container, g2, constraint);` |
| 1 | 66 | BorderArrangement.java:277 | 0.707107 | `double[] w = new double[5];` |
| 1 | 66 | BorderArrangement.java:278 | 0.707107 | `double[] h = new double[5];` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 144 | AbstractBlock.java:109 | 0.0 | `protected AbstractBlock() {` |
| 1 | 144 | AbstractBlock.java:110 | 0.0 | `this.id = null;` |
| 1 | 144 | AbstractBlock.java:111 | 0.0 | `this.width = 0.0;` |
| 1 | 144 | AbstractBlock.java:112 | 0.0 | `this.height = 0.0;` |
| 1 | 144 | AbstractBlock.java:113 | 0.0 | `this.bounds = new Rectangle2D.Float();` |
| 1 | 144 | AbstractBlock.java:114 | 0.0 | `this.margin = RectangleInsets.ZERO_INSETS;` |
| 1 | 144 | AbstractBlock.java:115 | 0.0 | `this.frame = BlockBorder.NONE;` |
| 1 | 144 | AbstractBlock.java:116 | 0.0 | `this.padding = RectangleInsets.ZERO_INSETS;` |
| 1 | 144 | AbstractBlock.java:151 | 0.0 | `return this.width;` |
| 1 | 144 | AbstractBlock.java:162 | 0.0 | `this.width = width;` |

