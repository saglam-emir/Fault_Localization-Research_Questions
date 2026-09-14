# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('SimpleRegression.java', 264)]

Ground_Truth_Answerable: True

- SBFL   ranked 253 statement(s)
- Hybrid ranked 16 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | SimpleRegression.java:60 | 0.333333 | `private double sumX = 0d;` |
| 1 | 23 | SimpleRegression.java:63 | 0.333333 | `private double sumXX = 0d;` |
| 1 | 23 | SimpleRegression.java:66 | 0.333333 | `private double sumY = 0d;` |
| 1 | 23 | SimpleRegression.java:69 | 0.333333 | `private double sumYY = 0d;` |
| 1 | 23 | SimpleRegression.java:72 | 0.333333 | `private double sumXY = 0d;` |
| 1 | 23 | SimpleRegression.java:75 | 0.333333 | `private long n = 0;` |
| 1 | 23 | SimpleRegression.java:78 | 0.333333 | `private double xbar = 0;` |
| 1 | 23 | SimpleRegression.java:81 | 0.333333 | `private double ybar = 0;` |
| 1 | 23 | SimpleRegression.java:89 | 0.333333 | `super();` |
| 1 | 23 | SimpleRegression.java:106 | 0.333333 | `if (n == 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | SimpleRegression.java:63 | 1.0 | `private double sumXX = 0d;` |
| 1 | 16 | SimpleRegression.java:69 | 1.0 | `private double sumYY = 0d;` |
| 1 | 16 | SimpleRegression.java:72 | 1.0 | `private double sumXY = 0d;` |
| 1 | 16 | SimpleRegression.java:75 | 1.0 | `private long n = 0;` |
| 1 | 16 | SimpleRegression.java:106 | 1.0 | `if (n == 0) {` |
| 1 | 16 | SimpleRegression.java:107 | 1.0 | `xbar = x;` |
| 1 | 16 | SimpleRegression.java:108 | 1.0 | `ybar = y;` |
| 1 | 16 | SimpleRegression.java:110 | 1.0 | `double dx = x - xbar;` |
| 1 | 16 | SimpleRegression.java:111 | 1.0 | `double dy = y - ybar;` |
| 1 | 16 | SimpleRegression.java:112 | 1.0 | `sumXX += dx * dx * (double) n / (double) (n + 1.0);` |

