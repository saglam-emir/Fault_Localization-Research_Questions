# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ShapeUtilities.java', 275)]

Ground_Truth_Answerable: True

- SBFL   ranked 16260 statement(s)
- Hybrid ranked 57 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 18 | ShapeUtilities.java:265 | 0.176777 | `if (p1 == null) {` |
| 1 | 18 | ShapeUtilities.java:268 | 0.176777 | `if (p2 == null) {` |
| 1 | 18 | ShapeUtilities.java:271 | 0.176777 | `if (p1.getWindingRule() != p2.getWindingRule()) {` |
| 1 | 18 | ShapeUtilities.java:274 | 0.176777 | `PathIterator iterator1 = p1.getPathIterator(null);` |
| 1 | 18 | ShapeUtilities.java:275 | 0.176777 | `PathIterator iterator2 = p1.getPathIterator(null);` |
| 1 | 18 | ShapeUtilities.java:276 | 0.176777 | `double[] d1 = new double[6];` |
| 1 | 18 | ShapeUtilities.java:277 | 0.176777 | `double[] d2 = new double[6];` |
| 1 | 18 | ShapeUtilities.java:278 | 0.176777 | `boolean done = iterator1.isDone() && iterator2.isDone();` |
| 1 | 18 | ShapeUtilities.java:279 | 0.176777 | `while (!done) {` |
| 1 | 18 | ShapeUtilities.java:280 | 0.176777 | `if (iterator1.isDone() != iterator2.isDone()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 18 | ShapeUtilities.java:265 | 0.707107 | `if (p1 == null) {` |
| 1 | 18 | ShapeUtilities.java:268 | 0.707107 | `if (p2 == null) {` |
| 1 | 18 | ShapeUtilities.java:271 | 0.707107 | `if (p1.getWindingRule() != p2.getWindingRule()) {` |
| 1 | 18 | ShapeUtilities.java:274 | 0.707107 | `PathIterator iterator1 = p1.getPathIterator(null);` |
| 1 | 18 | ShapeUtilities.java:275 | 0.707107 | `PathIterator iterator2 = p1.getPathIterator(null);` |
| 1 | 18 | ShapeUtilities.java:276 | 0.707107 | `double[] d1 = new double[6];` |
| 1 | 18 | ShapeUtilities.java:277 | 0.707107 | `double[] d2 = new double[6];` |
| 1 | 18 | ShapeUtilities.java:278 | 0.707107 | `boolean done = iterator1.isDone() && iterator2.isDone();` |
| 1 | 18 | ShapeUtilities.java:279 | 0.707107 | `while (!done) {` |
| 1 | 18 | ShapeUtilities.java:280 | 0.707107 | `if (iterator1.isDone() != iterator2.isDone()) {` |

