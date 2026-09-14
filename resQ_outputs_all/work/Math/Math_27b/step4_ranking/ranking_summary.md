# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Fraction.java', 597)]

Ground_Truth_Answerable: True

- SBFL   ranked 2923 statement(s)
- Hybrid ranked 3 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Fraction.java:597 | 0.5 | `return multiply(100).doubleValue();` |
| 2 | 1 | Fraction.java:555 | 0.408248 | `return new Fraction(numerator * i, denominator);` |
| 3 | 1 | Fraction.java:319 | 0.136083 | `return (double)numerator / (double)denominator;` |
| 4 | 62 | ArithmeticUtils.java:35 | 0.049266 | `static final long[] FACTORIALS = new long[] {` |
| 4 | 62 | ArithmeticUtils.java:385 | 0.049266 | `int u = p;` |
| 4 | 62 | ArithmeticUtils.java:386 | 0.049266 | `int v = q;` |
| 4 | 62 | ArithmeticUtils.java:387 | 0.049266 | `if ((u == 0) || (v == 0)) {` |
| 4 | 62 | ArithmeticUtils.java:388 | 0.049266 | `if ((u == Integer.MIN_VALUE) || (v == Integer.MIN_VALUE)) {` |
| 4 | 62 | ArithmeticUtils.java:392 | 0.049266 | `return FastMath.abs(u) + FastMath.abs(v);` |
| 4 | 62 | ArithmeticUtils.java:399 | 0.049266 | `if (u > 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Fraction.java:256 | 1.0 | `public Fraction(int num, int den) {` |
| 1 | 3 | Fraction.java:282 | 1.0 | `this.numerator   = num;` |
| 1 | 3 | Fraction.java:283 | 1.0 | `this.denominator = den;` |

