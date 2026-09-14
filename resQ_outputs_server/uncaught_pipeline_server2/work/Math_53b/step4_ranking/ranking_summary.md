# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Complex.java', 153)]

Ground_Truth_Answerable: True

- SBFL   ranked 1609 statement(s)
- Hybrid ranked 34 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Complex.java:152 | 0.158114 | `MathUtils.checkNotNull(rhs);` |
| 1 | 2 | Complex.java:153 | 0.158114 | `return createComplex(real + rhs.getReal(),` |
| 3 | 1 | Complex.java:319 | 0.144338 | `return isNaN;` |
| 4 | 1 | MathUtils.java:2331 | 0.1066 | `if (o == null) {` |
| 5 | 1 | MathUtils.java:85 | 0.088388 | `private static final long[] FACTORIALS = new long[] {` |
| 6 | 1 | Complex.java:997 | 0.084515 | `return new Complex(realPart, imaginaryPart);` |
| 7 | 1 | Complex.java:308 | 0.08165 | `return real;` |
| 8 | 1 | Complex.java:299 | 0.081111 | `return imaginary;` |
| 9 | 10 | Complex.java:52 | 0.066227 | `public static final Complex I = new Complex(0.0, 1.0);` |
| 9 | 10 | Complex.java:56 | 0.066227 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Complex.java:153 | 0.447214 | `return createComplex(real + rhs.getReal(),` |
| 2 | 1 | Complex.java:308 | 0.377964 | `return real;` |
| 3 | 1 | Complex.java:299 | 0.353553 | `return imaginary;` |
| 4 | 1 | Complex.java:997 | 0.25 | `return new Complex(realPart, imaginaryPart);` |
| 5 | 5 | Complex.java:90 | 0.169031 | `super();` |
| 5 | 5 | Complex.java:91 | 0.169031 | `this.real = real;` |
| 5 | 5 | Complex.java:92 | 0.169031 | `this.imaginary = imaginary;` |
| 5 | 5 | Complex.java:94 | 0.169031 | `isNaN = Double.isNaN(real) || Double.isNaN(imaginary);` |
| 5 | 5 | Complex.java:95 | 0.169031 | `isInfinite = !isNaN &&` |
| 10 | 25 | Complex.java:56 | 0.0 | `public static final Complex NaN = new Complex(Double.NaN, Double.NaN);` |

