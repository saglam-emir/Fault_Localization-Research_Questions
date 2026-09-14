# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 260), ('Complex.java', 297)]

Ground_Truth_Answerable: True

- SBFL   ranked 1636 statement(s)
- Hybrid ranked 11 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Complex.java:260 | 0.57735 | `return isZero ? NaN : INF;` |
| 1 | 2 | Complex.java:1183 | 0.57735 | `return "(" + real + ", " + imaginary + ")";` |
| 3 | 1 | Complex.java:587 | 0.333333 | `return this.add(I).divide(I.subtract(this)).log()` |
| 4 | 1 | Complex.java:258 | 0.298142 | `if (divisor.isZero) {` |
| 5 | 4 | Complex.java:329 | 0.288675 | `return isNaN;` |
| 5 | 4 | Complex.java:583 | 0.288675 | `if (isNaN) {` |
| 5 | 4 | FastMath.java:1284 | 0.288675 | `if (hiPrec != null) {` |
| 5 | 4 | FastMath.java:1288 | 0.288675 | `return Double.POSITIVE_INFINITY;` |
| 9 | 2 | Complex.java:253 | 0.280056 | `MathUtils.checkNotNull(divisor);` |
| 9 | 2 | Complex.java:254 | 0.280056 | `if (isNaN || divisor.isNaN) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:61 | 0.176777 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |
| 2 | 6 | Complex.java:99 | 0.166667 | `public Complex(double real, double imaginary) {` |
| 2 | 6 | Complex.java:100 | 0.166667 | `this.real = real;` |
| 2 | 6 | Complex.java:101 | 0.166667 | `this.imaginary = imaginary;` |
| 2 | 6 | Complex.java:103 | 0.166667 | `isNaN = Double.isNaN(real) || Double.isNaN(imaginary);` |
| 2 | 6 | Complex.java:104 | 0.166667 | `isInfinite = !isNaN &&` |
| 2 | 6 | Complex.java:106 | 0.166667 | `isZero = real == 0 && imaginary == 0;` |
| 8 | 4 | Complex.java:533 | 0.0 | `if (isNaN) {` |
| 8 | 4 | Complex.java:558 | 0.0 | `if (isNaN) {` |
| 8 | 4 | Complex.java:750 | 0.0 | `if (isNaN) {` |

