# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DiscreteDistribution.java', 181), ('DiscreteDistribution.java', 187)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/math3/distribution/DiscreteDistribution.java', 181)]

- SBFL   ranked 609 statement(s)
- Hybrid ranked 46 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DiscreteDistribution.java:69 | 1.0 | `this(new Well19937c(), samples);` |
| 1 | 5 | DiscreteDistribution.java:182 | 1.0 | `if (sampleSize <= 0) {` |
| 1 | 5 | DiscreteDistribution.java:187 | 1.0 | `final T[]out = (T[]) java.lang.reflect.Array.newInstance(singletons.get(0).getClass(), sampleSize);` |
| 1 | 5 | DiscreteDistribution.java:189 | 1.0 | `for (int i = 0; i < sampleSize; i++) {` |
| 1 | 5 | DiscreteDistribution.java:190 | 1.0 | `out[i] = sample();` |
| 6 | 27 | BitsStreamGenerator.java:90 | 0.57735 | `final long high = ((long) next(26)) << 26;` |
| 6 | 27 | BitsStreamGenerator.java:91 | 0.57735 | `final int  low  = next(26);` |
| 6 | 27 | BitsStreamGenerator.java:92 | 0.57735 | `return (high | low) * 0x1.0p-52d;` |
| 6 | 27 | DiscreteDistribution.java:157 | 0.57735 | `final double randomValue = random.nextDouble();` |
| 6 | 27 | DiscreteDistribution.java:158 | 0.57735 | `double sum = 0;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 46 | AbstractWell.java:72 | 1.0 | `this(k, m1, m2, m3, null);` |
| 1 | 46 | AbstractWell.java:94 | 1.0 | `protected AbstractWell(final int k, final int m1, final int m2, final int m3, final int[] seed) {` |
| 1 | 46 | AbstractWell.java:100 | 1.0 | `final int r = (k + w - 1) / w;` |
| 1 | 46 | AbstractWell.java:101 | 1.0 | `this.v      = new int[r];` |
| 1 | 46 | AbstractWell.java:102 | 1.0 | `this.index  = 0;` |
| 1 | 46 | AbstractWell.java:106 | 1.0 | `iRm1 = new int[r];` |
| 1 | 46 | AbstractWell.java:107 | 1.0 | `iRm2 = new int[r];` |
| 1 | 46 | AbstractWell.java:108 | 1.0 | `i1   = new int[r];` |
| 1 | 46 | AbstractWell.java:109 | 1.0 | `i2   = new int[r];` |
| 1 | 46 | AbstractWell.java:110 | 1.0 | `i3   = new int[r];` |

