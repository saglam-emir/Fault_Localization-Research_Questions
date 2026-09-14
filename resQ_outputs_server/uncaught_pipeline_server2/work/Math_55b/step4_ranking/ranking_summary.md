# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Vector3D.java', 459), ('Vector3D.java', 462), ('Vector3D.java', 473), ('Vector3D.java', 470), ('Vector3D.java', 471)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/geometry/Vector3D.java', 459), ('src/main/java/org/apache/commons/math/geometry/Vector3D.java', 462), ('src/main/java/org/apache/commons/math/geometry/Vector3D.java', 470), ('src/main/java/org/apache/commons/math/geometry/Vector3D.java', 471)]

- SBFL   ranked 1380 statement(s)
- Hybrid ranked 5 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Vector3D.java:473 | 0.5 | `return new Vector3D(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x);` |
| 2 | 3 | Vector3D.java:181 | 0.235702 | `return x;` |
| 2 | 3 | Vector3D.java:189 | 0.235702 | `return y;` |
| 2 | 3 | Vector3D.java:197 | 0.235702 | `return z;` |
| 5 | 29 | CompositeFormat.java:56 | 0.176777 | `final NumberFormat nf = NumberFormat.getInstance(locale);` |
| 5 | 29 | CompositeFormat.java:57 | 0.176777 | `nf.setMaximumFractionDigits(2);` |
| 5 | 29 | CompositeFormat.java:58 | 0.176777 | `return nf;` |
| 5 | 29 | Vector3D.java:35 | 0.176777 | `public static final Vector3D ZERO   = new Vector3D(0, 0, 0);` |
| 5 | 29 | Vector3D.java:38 | 0.176777 | `public static final Vector3D PLUS_I = new Vector3D(1, 0, 0);` |
| 5 | 29 | Vector3D.java:41 | 0.176777 | `public static final Vector3D MINUS_I = new Vector3D(-1, 0, 0);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | Vector3D.java:93 | 1.0 | `public Vector3D(double x, double y, double z) {` |
| 1 | 5 | Vector3D.java:94 | 1.0 | `this.x = x;` |
| 1 | 5 | Vector3D.java:95 | 1.0 | `this.y = y;` |
| 1 | 5 | Vector3D.java:96 | 1.0 | `this.z = z;` |
| 1 | 5 | Vector3D.java:473 | 1.0 | `return new Vector3D(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x);` |

