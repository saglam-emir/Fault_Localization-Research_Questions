# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Fraction.java', 259), ('Fraction.java', 260)]

Ground_Truth_Answerable: True

- SBFL   ranked 1306 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | Fraction.java:259 | 1.0 | `double nOd = doubleValue();` |
| 1 | 3 | Fraction.java:260 | 1.0 | `double dOn = object.doubleValue();` |
| 1 | 3 | Fraction.java:261 | 1.0 | `return (nOd < dOn) ? -1 : ((nOd > dOn) ? +1 : 0);` |
| 4 | 1 | Fraction.java:270 | 0.19245 | `return (double)numerator / (double)denominator;` |
| 5 | 1 | MathUtils.java:604 | 0.154303 | `t /= 2; // cast out twos` |
| 6 | 33 | Fraction.java:33 | 0.133631 | `public static final Fraction TWO = new Fraction(2, 1);` |
| 6 | 33 | Fraction.java:36 | 0.133631 | `public static final Fraction ONE = new Fraction(1, 1);` |
| 6 | 33 | Fraction.java:39 | 0.133631 | `public static final Fraction ZERO = new Fraction(0, 1);` |
| 6 | 33 | Fraction.java:42 | 0.133631 | `public static final Fraction MINUS_ONE = new Fraction(-1, 1);` |
| 6 | 33 | Fraction.java:209 | 0.133631 | `super();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Fraction.java:261 | 0.447214 | `return (nOd < dOn) ? -1 : ((nOd > dOn) ? +1 : 0);` |
| 2 | 6 | Fraction.java:209 | 0.0 | `super();` |
| 2 | 6 | Fraction.java:234 | 0.0 | `this.numerator = num;` |
| 2 | 6 | Fraction.java:235 | 0.0 | `this.denominator = den;` |
| 2 | 6 | Fraction.java:259 | 0.0 | `double nOd = doubleValue();` |
| 2 | 6 | Fraction.java:260 | 0.0 | `double dOn = object.doubleValue();` |
| 2 | 6 | Fraction.java:270 | 0.0 | `return (double)numerator / (double)denominator;` |

