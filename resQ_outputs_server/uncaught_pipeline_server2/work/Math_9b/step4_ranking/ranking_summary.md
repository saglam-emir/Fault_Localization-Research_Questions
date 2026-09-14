# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Line.java', 87)]

Ground_Truth_Answerable: True

- SBFL   ranked 1642 statement(s)
- Hybrid ranked 17 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | Line.java:87 | 1.0 | `final Line reverted = new Line(zero, zero.subtract(direction));` |
| 1 | 4 | Line.java:88 | 1.0 | `return reverted;` |
| 1 | 4 | Vector3D.java:222 | 1.0 | `return new double[] { x, y, z };` |
| 1 | 4 | Vector3D.java:374 | 1.0 | `return new Vector3D(-x, -y, -z);` |
| 5 | 1 | Line.java:95 | 0.316228 | `return direction;` |
| 6 | 8 | Line.java:54 | 0.19245 | `public Line(final Vector3D p1, final Vector3D p2) throws MathIllegalArgumentException {` |
| 6 | 8 | Line.java:55 | 0.19245 | `reset(p1, p2);` |
| 6 | 8 | Line.java:74 | 0.19245 | `final Vector3D delta = p2.subtract(p1);` |
| 6 | 8 | Line.java:75 | 0.19245 | `final double norm2 = delta.getNormSq();` |
| 6 | 8 | Line.java:76 | 0.19245 | `if (norm2 == 0.0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | Line.java:54 | 1.0 | `public Line(final Vector3D p1, final Vector3D p2) throws MathIllegalArgumentException {` |
| 1 | 17 | Line.java:55 | 1.0 | `reset(p1, p2);` |
| 1 | 17 | Line.java:74 | 1.0 | `final Vector3D delta = p2.subtract(p1);` |
| 1 | 17 | Line.java:75 | 1.0 | `final double norm2 = delta.getNormSq();` |
| 1 | 17 | Line.java:79 | 1.0 | `this.direction = new Vector3D(1.0 / FastMath.sqrt(norm2), delta);` |
| 1 | 17 | Line.java:95 | 1.0 | `return direction;` |
| 1 | 17 | Vector3D.java:95 | 1.0 | `public Vector3D(double x, double y, double z) {` |
| 1 | 17 | Vector3D.java:96 | 1.0 | `this.x = x;` |
| 1 | 17 | Vector3D.java:97 | 1.0 | `this.y = y;` |
| 1 | 17 | Vector3D.java:98 | 1.0 | `this.z = z;` |

