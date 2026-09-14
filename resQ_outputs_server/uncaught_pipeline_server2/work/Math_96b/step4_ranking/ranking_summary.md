# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 258)]

Ground_Truth_Answerable: True

- SBFL   ranked 436 statement(s)
- Hybrid ranked 22 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | Complex.java:277 | 0.707107 | `if (isNaN()) {` |
| 1 | 4 | Complex.java:280 | 0.707107 | `return 37 * (17 * MathUtils.hash(imaginary) +` |
| 1 | 4 | MathUtils.java:459 | 0.707107 | `long bits = Double.doubleToLongBits(value);` |
| 1 | 4 | MathUtils.java:460 | 0.707107 | `return (int)(bits ^ (bits >>> 32));` |
| 5 | 1 | Complex.java:258 | 0.353553 | `ret = (Double.doubleToRawLongBits(real) == Double.doubleToRawLongBits(rhs.getReal())) && (Double.doubleToRawLongBits(imaginary) == Double.doubleToRawLongBits(rhs.getImaginary()));` |
| 6 | 1 | Complex.java:255 | 0.333333 | `if (rhs.isNaN()) {` |
| 7 | 1 | Complex.java:254 | 0.316228 | `Complex rhs = (Complex)other;` |
| 8 | 1 | Complex.java:250 | 0.301511 | `} else if (other == null) {` |
| 9 | 2 | Complex.java:248 | 0.267261 | `if (this == other) {` |
| 9 | 2 | Complex.java:266 | 0.267261 | `return ret;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Complex.java:76 | 0.353553 | `super();` |
| 1 | 3 | Complex.java:77 | 0.353553 | `this.real = real;` |
| 1 | 3 | Complex.java:78 | 0.353553 | `this.imaginary = imaginary;` |
| 4 | 19 | Complex.java:51 | 0.0 | `public static final Complex INF = new Complex(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY);` |
| 4 | 19 | Complex.java:57 | 0.0 | `public static final Complex ZERO = new Complex(0.0, 0.0);` |
| 4 | 19 | Complex.java:92 | 0.0 | `if (isNaN()) {` |
| 4 | 19 | Complex.java:96 | 0.0 | `if (isInfinite()) {` |
| 4 | 19 | Complex.java:100 | 0.0 | `if (Math.abs(real) < Math.abs(imaginary)) {` |
| 4 | 19 | Complex.java:101 | 0.0 | `if (imaginary == 0.0) {` |
| 4 | 19 | Complex.java:105 | 0.0 | `return (Math.abs(imaginary) * Math.sqrt(1 + q*q));` |

