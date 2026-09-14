# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 1624), ('MathUtils.java', 1626)]

Ground_Truth_Answerable: True

- SBFL   ranked 7914 statement(s)
- Hybrid ranked 69 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 25 | Cluster.java:45 | 0.5 | `public Cluster(final T center) {` |
| 1 | 25 | Cluster.java:46 | 0.5 | `this.center = center;` |
| 1 | 25 | Cluster.java:47 | 0.5 | `points = new ArrayList<T>();` |
| 1 | 25 | Cluster.java:71 | 0.5 | `return center;` |
| 1 | 25 | EuclideanIntegerPoint.java:30 | 0.5 | `public class EuclideanIntegerPoint implements Clusterable<EuclideanIntegerPoint>, Serializable {` |
| 1 | 25 | KMeansPlusPlusClusterer.java:40 | 0.5 | `public KMeansPlusPlusClusterer(final Random random) {` |
| 1 | 25 | KMeansPlusPlusClusterer.java:41 | 0.5 | `this.random = random;` |
| 1 | 25 | KMeansPlusPlusClusterer.java:56 | 0.5 | `List<Cluster<T>> clusters = chooseInitialCenters(points, k, random);` |
| 1 | 25 | KMeansPlusPlusClusterer.java:57 | 0.5 | `assignPointsToClusters(clusters, points);` |
| 1 | 25 | KMeansPlusPlusClusterer.java:89 | 0.5 | `for (final T p : points) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | KMeansPlusPlusClusterer.java:40 | 0.707107 | `public KMeansPlusPlusClusterer(final Random random) {` |
| 1 | 2 | KMeansPlusPlusClusterer.java:41 | 0.707107 | `this.random = random;` |
| 3 | 67 | Cluster.java:45 | 0.0 | `public Cluster(final T center) {` |
| 3 | 67 | Cluster.java:46 | 0.0 | `this.center = center;` |
| 3 | 67 | Cluster.java:47 | 0.0 | `points = new ArrayList<T>();` |
| 3 | 67 | Cluster.java:55 | 0.0 | `points.add(point);` |
| 3 | 67 | Cluster.java:63 | 0.0 | `return points;` |
| 3 | 67 | Cluster.java:71 | 0.0 | `return center;` |
| 3 | 67 | EuclideanIntegerPoint.java:30 | 0.0 | `public class EuclideanIntegerPoint implements Clusterable<EuclideanIntegerPoint>, Serializable {` |
| 3 | 67 | EuclideanIntegerPoint.java:43 | 0.0 | `public EuclideanIntegerPoint(final int[] point) {` |

