# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 82), ('Complex.java', 105), ('Complex.java', 256), ('Complex.java', 257), ('Complex.java', 293)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/complex/Complex.java', 82), ('src/main/java/org/apache/commons/math/complex/Complex.java', 105)]

- SBFL   ranked 1635 statement(s)
- Hybrid ranked 11 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:1179 | 0.816497 | `return "(" + real + ", " + imaginary + ")";` |
| 2 | 1 | Complex.java:257 | 0.57735 | `return NaN;` |
| 3 | 2 | FastMath.java:2991 | 0.408248 | `if (y < 0.0 || invy < 0.0) {` |
| 3 | 2 | FastMath.java:2994 | 0.408248 | `return Math.PI;` |
| 5 | 1 | Complex.java:583 | 0.333333 | `return this.add(I).divide(I.subtract(this)).log()` |
| 6 | 1 | Complex.java:256 | 0.298142 | `if (divisor.getReal() == 0.0 && divisor.getImaginary() == 0.0) {` |
| 7 | 1 | Complex.java:579 | 0.288675 | `if (isNaN) {` |
| 8 | 2 | Complex.java:251 | 0.280056 | `MathUtils.checkNotNull(divisor);` |
| 8 | 2 | Complex.java:252 | 0.280056 | `if (isNaN || divisor.isNaN) {` |
| 10 | 3 | Complex.java:268 | 0.258199 | `double q = c / d;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:64 | 0.707107 | `public static final Complex INF = new Complex(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY);` |
| 2 | 5 | Complex.java:98 | 0.171499 | `public Complex(double real, double imaginary) {` |
| 2 | 5 | Complex.java:99 | 0.171499 | `this.real = real;` |
| 2 | 5 | Complex.java:100 | 0.171499 | `this.imaginary = imaginary;` |
| 2 | 5 | Complex.java:102 | 0.171499 | `isNaN = Double.isNaN(real) || Double.isNaN(imaginary);` |
| 2 | 5 | Complex.java:103 | 0.171499 | `isInfinite = !isNaN &&` |
| 7 | 5 | Complex.java:61 | 0.0 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |
| 7 | 5 | Complex.java:529 | 0.0 | `if (isNaN) {` |
| 7 | 5 | Complex.java:554 | 0.0 | `if (isNaN) {` |
| 7 | 5 | Complex.java:746 | 0.0 | `if (isNaN) {` |

