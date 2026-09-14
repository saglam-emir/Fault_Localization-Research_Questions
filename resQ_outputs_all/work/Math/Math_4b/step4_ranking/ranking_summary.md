# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SubLine.java', 114), ('SubLine.java', 118)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/geometry/euclidean/twod/SubLine.java', 118)]

- SBFL   ranked 1770 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | Line.java:156 | 0.267261 | `return distance(p) < 1.0e-10;` |
| 1 | 13 | Line.java:195 | 0.267261 | `final double cos = direction.dotProduct(line.direction);` |
| 1 | 13 | Line.java:196 | 0.267261 | `final double n = 1 - cos * cos;` |
| 1 | 13 | Line.java:197 | 0.267261 | `if (n < Precision.EPSILON) {` |
| 1 | 13 | Line.java:203 | 0.267261 | `final double a        = delta0.dotProduct(direction);` |
| 1 | 13 | Line.java:204 | 0.267261 | `final double b        = delta0.dotProduct(line.direction);` |
| 1 | 13 | Line.java:206 | 0.267261 | `return new Vector3D(1, zero, (a - b * cos) / n, direction);` |
| 1 | 13 | Line.java:217 | 0.267261 | `return line.contains(closest) ? closest : null;` |
| 1 | 13 | SubLine.java:113 | 0.267261 | `Vector3D v1D = line.intersection(subLine.line);` |
| 1 | 13 | SubLine.java:114 | 0.267261 | `` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | SubLine.java:56 | 0.333333 | `this(new Line(start, end), buildIntervalSet(start, end));` |

