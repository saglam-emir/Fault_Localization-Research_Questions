# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MathUtils.java', 412)]

Ground_Truth_Answerable: True

- SBFL   ranked 4908 statement(s)
- Hybrid ranked 164 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | MathUtils.java:430 | 0.218218 | `u /= 2;` |
| 1 | 3 | MathUtils.java:431 | 0.218218 | `v /= 2;` |
| 1 | 3 | MathUtils.java:432 | 0.218218 | `k++; // cast out twos.` |
| 4 | 1 | MathUtils.java:450 | 0.182574 | `u = -t;` |
| 5 | 1 | MathUtils.java:446 | 0.171499 | `t /= 2; // cast out twos` |
| 6 | 16 | MathUtils.java:412 | 0.147442 | `if (u * v == 0) {` |
| 6 | 16 | MathUtils.java:413 | 0.147442 | `return (Math.abs(u) + Math.abs(v));` |
| 6 | 16 | MathUtils.java:420 | 0.147442 | `if (u > 0) {` |
| 6 | 16 | MathUtils.java:421 | 0.147442 | `u = -u;` |
| 6 | 16 | MathUtils.java:423 | 0.147442 | `if (v > 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | MathUtils.java:413 | 0.223607 | `return (Math.abs(u) + Math.abs(v));` |
| 2 | 1 | MathUtils.java:412 | 0.213201 | `if (u * v == 0) {` |
| 3 | 162 | JDKRandomGenerator.java:28 | 0.0 | `public class JDKRandomGenerator extends Random implements RandomGenerator {` |
| 3 | 162 | MathUtils.java:77 | 0.0 | `long s = (long)x + (long)y;` |
| 3 | 162 | MathUtils.java:81 | 0.0 | `return (int)s;` |
| 3 | 162 | MathUtils.java:95 | 0.0 | `return addAndCheck(a, b, "overflow: add");` |
| 3 | 162 | MathUtils.java:111 | 0.0 | `if (a > b) {` |
| 3 | 162 | MathUtils.java:113 | 0.0 | `ret = addAndCheck(b, a, msg);` |
| 3 | 162 | MathUtils.java:117 | 0.0 | `if (a < 0) {` |
| 3 | 162 | MathUtils.java:118 | 0.0 | `if (b < 0) {` |

