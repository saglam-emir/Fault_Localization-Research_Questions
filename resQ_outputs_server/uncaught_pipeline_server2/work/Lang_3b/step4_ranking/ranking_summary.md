# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 593), ('NumberUtils.java', 597), ('NumberUtils.java', 601), ('NumberUtils.java', 605)]

Ground_Truth_Answerable: True

- SBFL   ranked 942 statement(s)
- Hybrid ranked 90 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | NumberUtils.java:494 | 0.19245 | `dec = str.substring(decPos + 1);` |
| 2 | 3 | NumberUtils.java:573 | 0.166667 | `exp = null;` |
| 2 | 3 | NumberUtils.java:594 | 0.166667 | `if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {` |
| 2 | 3 | NumberUtils.java:595 | 0.166667 | `return f;` |
| 5 | 8 | NumberUtils.java:492 | 0.149071 | `dec = str.substring(decPos + 1, expPos);` |
| 5 | 8 | NumberUtils.java:496 | 0.149071 | `mant = str.substring(0, decPos);` |
| 5 | 8 | NumberUtils.java:497 | 0.149071 | `numDecimals = dec.length(); // gets number of digits past the decimal to ensure no loss of precision for floating point numbers.` |
| 5 | 8 | NumberUtils.java:570 | 0.149071 | `if (expPos > -1 && expPos < str.length() - 1) {` |
| 5 | 8 | NumberUtils.java:571 | 0.149071 | `exp = str.substring(expPos + 1, str.length());` |
| 5 | 8 | NumberUtils.java:575 | 0.149071 | `if (dec == null && exp == null) { // no decimal point and no exponent` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | NumberUtils.java:594 | 1.0 | `if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {` |
| 1 | 2 | NumberUtils.java:595 | 1.0 | `return f;` |
| 3 | 10 | NumberUtils.java:480 | 0.5 | `final int decPos = str.indexOf('.');` |
| 3 | 10 | NumberUtils.java:481 | 0.5 | `final int expPos = str.indexOf('e') + str.indexOf('E') + 1; // assumes both not present` |
| 3 | 10 | NumberUtils.java:486 | 0.5 | `if (decPos > -1) { // there is a decimal point` |
| 3 | 10 | NumberUtils.java:492 | 0.5 | `dec = str.substring(decPos + 1, expPos);` |
| 3 | 10 | NumberUtils.java:496 | 0.5 | `mant = str.substring(0, decPos);` |
| 3 | 10 | NumberUtils.java:570 | 0.5 | `if (expPos > -1 && expPos < str.length() - 1) {` |
| 3 | 10 | NumberUtils.java:571 | 0.5 | `exp = str.substring(expPos + 1, str.length());` |
| 3 | 10 | NumberUtils.java:593 | 0.5 | `final Float f = createFloat(str);` |

