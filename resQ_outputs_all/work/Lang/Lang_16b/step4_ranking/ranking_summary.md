# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 458)]

Ground_Truth_Answerable: True

- SBFL   ranked 962 statement(s)
- Hybrid ranked 51 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 23 | NumberUtils.java:459 | 0.235702 | `return createInteger(str);` |
| 1 | 23 | NumberUtils.java:470 | 0.235702 | `if (expPos > -1) {` |
| 1 | 23 | NumberUtils.java:476 | 0.235702 | `dec = str.substring(decPos + 1);` |
| 1 | 23 | NumberUtils.java:478 | 0.235702 | `mant = str.substring(0, decPos);` |
| 1 | 23 | NumberUtils.java:481 | 0.235702 | `if (expPos > str.length()) {` |
| 1 | 23 | NumberUtils.java:484 | 0.235702 | `mant = str.substring(0, expPos);` |
| 1 | 23 | NumberUtils.java:517 | 0.235702 | `Float f = NumberUtils.createFloat(numeric);` |
| 1 | 23 | NumberUtils.java:518 | 0.235702 | `if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {` |
| 1 | 23 | NumberUtils.java:521 | 0.235702 | `return f;` |
| 1 | 23 | NumberUtils.java:531 | 0.235702 | `Double d = NumberUtils.createDouble(numeric);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 51 | NumberUtils.java:445 | 0.0 | `if (str == null) {` |
| 1 | 51 | NumberUtils.java:448 | 0.0 | `if (StringUtils.isBlank(str)) {` |
| 1 | 51 | NumberUtils.java:451 | 0.0 | `if (str.startsWith("--")) {` |
| 1 | 51 | NumberUtils.java:458 | 0.0 | `if (str.startsWith("0x") || str.startsWith("-0x")) {` |
| 1 | 51 | NumberUtils.java:461 | 0.0 | `char lastChar = str.charAt(str.length() - 1);` |
| 1 | 51 | NumberUtils.java:465 | 0.0 | `int decPos = str.indexOf('.');` |
| 1 | 51 | NumberUtils.java:476 | 0.0 | `dec = str.substring(decPos + 1);` |
| 1 | 51 | NumberUtils.java:478 | 0.0 | `mant = str.substring(0, decPos);` |
| 1 | 51 | NumberUtils.java:490 | 0.0 | `if (!Character.isDigit(lastChar) && lastChar != '.') {` |
| 1 | 51 | NumberUtils.java:497 | 0.0 | `String numeric = str.substring(0, str.length() - 1);` |

