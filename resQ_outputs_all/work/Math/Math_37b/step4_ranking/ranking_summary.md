# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 1018), ('Complex.java', 1021), ('Complex.java', 1063), ('Complex.java', 1066)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/complex/Complex.java', 1021)]

- SBFL   ranked 1449 statement(s)
- Hybrid ranked 53 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | Complex.java:1178 | 0.392232 | `if (Double.isNaN(realPart) ||` |
| 1 | 4 | Complex.java:1182 | 0.392232 | `return new Complex(realPart, imaginaryPart);` |
| 1 | 4 | FastMath.java:393 | 0.392232 | `return exp(x)/2.0;` |
| 1 | 4 | FastMath.java:453 | 0.392232 | `return exp(x)/2.0;` |
| 5 | 8 | Complex.java:1022 | 0.320256 | `double real2 = 2.0 * real;` |
| 5 | 8 | Complex.java:1023 | 0.320256 | `double imaginary2 = 2.0 * imaginary;` |
| 5 | 8 | Complex.java:1024 | 0.320256 | `double d = FastMath.cos(real2) + FastMath.cosh(imaginary2);` |
| 5 | 8 | Complex.java:1026 | 0.320256 | `return createComplex(FastMath.sin(real2) / d,` |
| 5 | 8 | Complex.java:1066 | 0.320256 | `double real2 = 2.0 * real;` |
| 5 | 8 | Complex.java:1067 | 0.320256 | `double imaginary2 = 2.0 * imaginary;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:98 | 0.197066 | `public Complex(double real, double imaginary) {` |
| 2 | 1 | Complex.java:69 | 0.162221 | `public static final Complex ZERO = new Complex(0.0, 0.0);` |
| 3 | 1 | Complex.java:103 | 0.123091 | `isInfinite = !isNaN &&` |
| 4 | 1 | Complex.java:100 | 0.119523 | `this.imaginary = imaginary;` |
| 5 | 1 | Complex.java:99 | 0.11547 | `this.real = real;` |
| 6 | 1 | Complex.java:102 | 0.113228 | `isNaN = Double.isNaN(real) || Double.isNaN(imaginary);` |
| 7 | 47 | Complex.java:59 | 0.0 | `public static final Complex I = new Complex(0.0, 1.0);` |
| 7 | 47 | Complex.java:62 | 0.0 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |
| 7 | 47 | Complex.java:67 | 0.0 | `public static final Complex ONE = new Complex(1.0, 0.0);` |
| 7 | 47 | Complex.java:116 | 0.0 | `if (isNaN) {` |

