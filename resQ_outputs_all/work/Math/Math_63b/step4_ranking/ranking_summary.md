# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 417)]

Ground_Truth_Answerable: True

- SBFL   ranked 9795 statement(s)
- Hybrid ranked 189 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | MathUtils.java:417 | 0.707107 | `return (Double.isNaN(x) && Double.isNaN(y)) || x == y;` |
| 1 | 8 | MathUtils.java:523 | 0.707107 | `if ((x == null) || (y == null)) {` |
| 1 | 8 | MathUtils.java:524 | 0.707107 | `return !((x == null) ^ (y == null));` |
| 1 | 8 | MathUtils.java:526 | 0.707107 | `if (x.length != y.length) {` |
| 1 | 8 | MathUtils.java:527 | 0.707107 | `return false;` |
| 1 | 8 | MathUtils.java:529 | 0.707107 | `for (int i = 0; i < x.length; ++i) {` |
| 1 | 8 | MathUtils.java:530 | 0.707107 | `if (!equals(x[i], y[i])) {` |
| 1 | 8 | MathUtils.java:534 | 0.707107 | `return true;` |
| 9 | 1 | FastMath.java:2838 | 0.104257 | `y--;` |
| 10 | 2 | Fraction.java:231 | 0.1 | `this.numerator = (int) p2;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | MathUtils.java:534 | 0.57735 | `return true;` |
| 2 | 188 | JDKRandomGenerator.java:28 | 0.0 | `public class JDKRandomGenerator extends Random implements RandomGenerator {` |
| 2 | 188 | MathUtils.java:102 | 0.0 | `long s = (long)x + (long)y;` |
| 2 | 188 | MathUtils.java:106 | 0.0 | `return (int)s;` |
| 2 | 188 | MathUtils.java:120 | 0.0 | `return addAndCheck(a, b, LocalizedFormats.OVERFLOW_IN_ADDITION);` |
| 2 | 188 | MathUtils.java:136 | 0.0 | `if (a > b) {` |
| 2 | 188 | MathUtils.java:138 | 0.0 | `ret = addAndCheck(b, a, pattern);` |
| 2 | 188 | MathUtils.java:142 | 0.0 | `if (a < 0) {` |
| 2 | 188 | MathUtils.java:143 | 0.0 | `if (b < 0) {` |
| 2 | 188 | MathUtils.java:145 | 0.0 | `if (Long.MIN_VALUE - b <= a) {` |

