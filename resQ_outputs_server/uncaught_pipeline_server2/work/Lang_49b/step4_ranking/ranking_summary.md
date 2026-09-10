# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Fraction.java', 466)]

Ground_Truth_Answerable: True

- SBFL   ranked 256 statement(s)
- Hybrid ranked 24 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | Fraction.java:466 | 1.0 | `int gcd = greatestCommonDivisor(Math.abs(numerator), denominator);` |
| 1 | 4 | Fraction.java:467 | 1.0 | `if (gcd == 1) {` |
| 1 | 4 | Fraction.java:468 | 1.0 | `return this;` |
| 1 | 4 | Fraction.java:470 | 1.0 | `return Fraction.getFraction(numerator / gcd, denominator / gcd);` |
| 5 | 3 | Fraction.java:146 | 0.447214 | `if (numerator==Integer.MIN_VALUE ||` |
| 5 | 3 | Fraction.java:150 | 0.447214 | `numerator = -numerator;` |
| 5 | 3 | Fraction.java:151 | 0.447214 | `denominator = -denominator;` |
| 8 | 13 | Fraction.java:578 | 0.333333 | `if (u>0) { u=-u; } // make u negative` |
| 8 | 13 | Fraction.java:579 | 0.333333 | `if (v>0) { v=-v; } // make v negative` |
| 8 | 13 | Fraction.java:581 | 0.333333 | `int k=0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Fraction.java:572 | 0.5 | `return 1;` |
| 2 | 1 | Fraction.java:368 | 0.377964 | `return numerator;` |
| 3 | 1 | Fraction.java:468 | 0.288675 | `return this;` |
| 4 | 2 | Fraction.java:467 | 0.25 | `if (gcd == 1) {` |
| 4 | 2 | Fraction.java:571 | 0.25 | `if (Math.abs(u) <= 1 || Math.abs(v) <= 1) {` |
| 6 | 8 | Fraction.java:107 | 0.242536 | `private transient int hashCode = 0;` |
| 6 | 8 | Fraction.java:111 | 0.242536 | `private transient String toString = null;` |
| 6 | 8 | Fraction.java:115 | 0.242536 | `private transient String toProperString = null;` |
| 6 | 8 | Fraction.java:125 | 0.242536 | `super();` |
| 6 | 8 | Fraction.java:126 | 0.242536 | `this.numerator = numerator;` |

