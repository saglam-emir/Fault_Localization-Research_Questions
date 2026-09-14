# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BigFraction.java', 686), ('BigFraction.java', 688), ('BigFraction.java', 733), ('BigFraction.java', 735)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math/fraction/BigFraction.java', 686), ('src/main/java/org/apache/commons/math/fraction/BigFraction.java', 733)]

- SBFL   ranked 2905 statement(s)
- Hybrid ranked 10 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | BigFraction.java:732 | 0.5 | `float result = numerator.floatValue() / denominator.floatValue();` |
| 1 | 2 | BigFraction.java:735 | 0.5 | `return result;` |
| 3 | 32 | BigFraction.java:44 | 0.162221 | `public static final BigFraction TWO = new BigFraction(2);` |
| 3 | 32 | BigFraction.java:47 | 0.162221 | `public static final BigFraction ONE = new BigFraction(1);` |
| 3 | 32 | BigFraction.java:50 | 0.162221 | `public static final BigFraction ZERO = new BigFraction(0);` |
| 3 | 32 | BigFraction.java:53 | 0.162221 | `public static final BigFraction MINUS_ONE = new BigFraction(-1);` |
| 3 | 32 | BigFraction.java:56 | 0.162221 | `public static final BigFraction FOUR_FIFTHS = new BigFraction(4, 5);` |
| 3 | 32 | BigFraction.java:59 | 0.162221 | `public static final BigFraction ONE_FIFTH = new BigFraction(1, 5);` |
| 3 | 32 | BigFraction.java:62 | 0.162221 | `public static final BigFraction ONE_HALF = new BigFraction(1, 2);` |
| 3 | 32 | BigFraction.java:65 | 0.162221 | `public static final BigFraction ONE_QUARTER = new BigFraction(1, 4);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 8 | BigFraction.java:83 | 1.0 | `public static final BigFraction TWO_THIRDS = new BigFraction(2, 3);` |
| 1 | 8 | BigFraction.java:122 | 1.0 | `if (BigInteger.ZERO.equals(den)) {` |
| 1 | 8 | BigFraction.java:125 | 1.0 | `if (BigInteger.ZERO.equals(num)) {` |
| 1 | 8 | BigFraction.java:131 | 1.0 | `final BigInteger gcd = num.gcd(den);` |
| 1 | 8 | BigFraction.java:138 | 1.0 | `if (BigInteger.ZERO.compareTo(den) > 0) {` |
| 1 | 8 | BigFraction.java:144 | 1.0 | `numerator   = num;` |
| 1 | 8 | BigFraction.java:145 | 1.0 | `denominator = den;` |
| 1 | 8 | BigFraction.java:381 | 1.0 | `this(BigInteger.valueOf(num), BigInteger.valueOf(den));` |
| 9 | 2 | BigFraction.java:685 | 0.707107 | `double result = numerator.doubleValue() / denominator.doubleValue();` |
| 9 | 2 | BigFraction.java:732 | 0.707107 | `float result = numerator.floatValue() / denominator.floatValue();` |

