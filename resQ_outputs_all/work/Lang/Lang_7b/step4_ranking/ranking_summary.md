# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 452), ('NumberUtils.java', 453), ('NumberUtils.java', 454), ('NumberUtils.java', 721), ('NumberUtils.java', 725)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/math/NumberUtils.java', 721)]

- SBFL   ranked 949 statement(s)
- Hybrid ranked 82 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | NumberUtils.java:458 | 0.333333 | `hexDigits--;` |
| 1 | 6 | NumberUtils.java:486 | 0.333333 | `throw new NumberFormatException(str + " is not a valid number.");` |
| 1 | 6 | NumberUtils.java:511 | 0.333333 | `} catch (NumberFormatException nfe) { // NOPMD` |
| 1 | 6 | NumberUtils.java:514 | 0.333333 | `return createBigInteger(numeric);` |
| 1 | 6 | NumberUtils.java:587 | 0.333333 | `if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {` |
| 1 | 6 | NumberUtils.java:588 | 0.333333 | `return d;` |
| 7 | 144 | JavaVersion.java:27 | 0.235702 | `public enum JavaVersion {` |
| 7 | 144 | JavaVersion.java:32 | 0.235702 | `JAVA_0_9(1.5f, "0.9"),` |
| 7 | 144 | JavaVersion.java:37 | 0.235702 | `JAVA_1_1(1.1f, "1.1"),` |
| 7 | 144 | JavaVersion.java:42 | 0.235702 | `JAVA_1_2(1.2f, "1.2"),` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 82 | BooleanUtils.java:42 | 0.0 | `super();` |
| 1 | 82 | JavaVersion.java:47 | 0.0 | `JAVA_1_3(1.3f, "1.3"),` |
| 1 | 82 | JavaVersion.java:72 | 0.0 | `JAVA_1_8(1.8f, "1.8");` |
| 1 | 82 | JavaVersion.java:90 | 0.0 | `this.value = value;` |
| 1 | 82 | JavaVersion.java:105 | 0.0 | `return this.value >= requiredVersion.value;` |
| 1 | 82 | NumberUtils.java:77 | 0.0 | `super();` |
| 1 | 82 | NumberUtils.java:446 | 0.0 | `if (str == null) {` |
| 1 | 82 | NumberUtils.java:447 | 0.0 | `return null;` |
| 1 | 82 | NumberUtils.java:449 | 0.0 | `if (StringUtils.isBlank(str)) {` |
| 1 | 82 | NumberUtils.java:452 | 0.0 | `if (str.startsWith("--")) {` |

