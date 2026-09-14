# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 305)]

Ground_Truth_Answerable: True

- SBFL   ranked 2619 statement(s)
- Hybrid ranked 20 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | DstNormalization.java:28 | 0.707107 | `public enum DstNormalization {` |
| 1 | 3 | DstNormalization.java:41 | 0.707107 | `STANDARD_DST_I,` |
| 1 | 3 | DstNormalization.java:56 | 0.707107 | `ORTHOGONAL_DST_I` |
| 4 | 3 | DctNormalization.java:28 | 0.612372 | `public enum DctNormalization {` |
| 4 | 3 | DctNormalization.java:46 | 0.612372 | `STANDARD_DCT_I,` |
| 4 | 3 | DctNormalization.java:66 | 0.612372 | `ORTHOGONAL_DCT_I;` |
| 7 | 2 | Complex.java:305 | 0.353553 | `return NaN;` |
| 7 | 2 | Complex.java:1228 | 0.353553 | `return "(" + real + ", " + imaginary + ")";` |
| 9 | 1 | Complex.java:304 | 0.158114 | `if (real == 0.0 && imaginary == 0.0) {` |
| 10 | 1 | Complex.java:300 | 0.144338 | `if (isNaN) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:69 | 0.333333 | `public static final Complex ZERO = new Complex(0.0, 0.0);` |
| 2 | 1 | Complex.java:67 | 0.223607 | `public static final Complex ONE = new Complex(1.0, 0.0);` |
| 3 | 1 | Complex.java:59 | 0.208514 | `public static final Complex I = new Complex(0.0, 1.0);` |
| 4 | 5 | Complex.java:98 | 0.152499 | `public Complex(double real, double imaginary) {` |
| 4 | 5 | Complex.java:99 | 0.152499 | `this.real = real;` |
| 4 | 5 | Complex.java:100 | 0.152499 | `this.imaginary = imaginary;` |
| 4 | 5 | Complex.java:102 | 0.152499 | `isNaN = Double.isNaN(real) || Double.isNaN(imaginary);` |
| 4 | 5 | Complex.java:103 | 0.152499 | `isInfinite = !isNaN &&` |
| 9 | 12 | Complex.java:62 | 0.0 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |
| 9 | 12 | Complex.java:116 | 0.0 | `if (isNaN) {` |

