# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 543), ('MathUtils.java', 714)]

Ground_Truth_Answerable: True

- SBFL   ranked 5070 statement(s)
- Hybrid ranked 181 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | MathUtils.java:710 | 0.707107 | `if (a==0 || b==0){` |
| 1 | 4 | MathUtils.java:711 | 0.707107 | `return 0;` |
| 1 | 4 | MathUtils.java:713 | 0.707107 | `int lcm = Math.abs(mulAndCheck(a / gcd(a, b), b));` |
| 1 | 4 | MathUtils.java:714 | 0.707107 | `return lcm;` |
| 5 | 3 | MathUtils.java:560 | 0.262613 | `u /= 2;` |
| 5 | 3 | MathUtils.java:561 | 0.262613 | `v /= 2;` |
| 5 | 3 | MathUtils.java:562 | 0.262613 | `k++; // cast out twos.` |
| 8 | 1 | MathUtils.java:578 | 0.206284 | `t /= 2; // cast out twos` |
| 9 | 18 | MathUtils.java:540 | 0.181071 | `int u = p;` |
| 9 | 18 | MathUtils.java:541 | 0.181071 | `int v = q;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 181 | JDKRandomGenerator.java:28 | 0.0 | `public class JDKRandomGenerator extends Random implements RandomGenerator {` |
| 1 | 181 | MathUtils.java:98 | 0.0 | `return addAndCheck(a, b, "overflow: add");` |
| 1 | 181 | MathUtils.java:114 | 0.0 | `if (a > b) {` |
| 1 | 181 | MathUtils.java:116 | 0.0 | `ret = addAndCheck(b, a, msg);` |
| 1 | 181 | MathUtils.java:120 | 0.0 | `if (a < 0) {` |
| 1 | 181 | MathUtils.java:121 | 0.0 | `if (b < 0) {` |
| 1 | 181 | MathUtils.java:123 | 0.0 | `if (Long.MIN_VALUE - b <= a) {` |
| 1 | 181 | MathUtils.java:124 | 0.0 | `ret = a + b;` |
| 1 | 181 | MathUtils.java:130 | 0.0 | `ret = a + b;` |
| 1 | 181 | MathUtils.java:137 | 0.0 | `if (a <= Long.MAX_VALUE - b) {` |

