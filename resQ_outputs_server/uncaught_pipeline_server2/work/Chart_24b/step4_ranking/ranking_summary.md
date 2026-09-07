# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('GrayPaintScale.java', 126)]

Ground_Truth_Answerable: True

- SBFL   ranked 1202 statement(s)
- Hybrid ranked 6 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | GrayPaintScale.java:124 | 1.0 | `double v = Math.max(value, this.lowerBound);` |
| 1 | 4 | GrayPaintScale.java:125 | 1.0 | `v = Math.min(v, this.upperBound);` |
| 1 | 4 | GrayPaintScale.java:126 | 1.0 | `int g = (int) ((value - this.lowerBound) / (this.upperBound` |
| 1 | 4 | GrayPaintScale.java:128 | 1.0 | `return new Color(g, g, g);` |
| 5 | 1 | GrayPaintScale.java:72 | 0.333333 | `this(0.0, 1.0);` |
| 6 | 4 | GrayPaintScale.java:84 | 0.316228 | `public GrayPaintScale(double lowerBound, double upperBound) {` |
| 6 | 4 | GrayPaintScale.java:85 | 0.316228 | `if (lowerBound >= upperBound) {` |
| 6 | 4 | GrayPaintScale.java:89 | 0.316228 | `this.lowerBound = lowerBound;` |
| 6 | 4 | GrayPaintScale.java:90 | 0.316228 | `this.upperBound = upperBound;` |
| 10 | 1193 | AbstractBlock.java:111 | 0.0 | `protected AbstractBlock() {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | GrayPaintScale.java:72 | 0.0 | `this(0.0, 1.0);` |
| 1 | 6 | GrayPaintScale.java:89 | 0.0 | `this.lowerBound = lowerBound;` |
| 1 | 6 | GrayPaintScale.java:90 | 0.0 | `this.upperBound = upperBound;` |
| 1 | 6 | GrayPaintScale.java:124 | 0.0 | `double v = Math.max(value, this.lowerBound);` |
| 1 | 6 | GrayPaintScale.java:126 | 0.0 | `int g = (int) ((value - this.lowerBound) / (this.upperBound` |
| 1 | 6 | GrayPaintScale.java:128 | 0.0 | `return new Color(g, g, g);` |

