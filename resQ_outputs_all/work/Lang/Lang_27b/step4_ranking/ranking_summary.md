# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumberUtils.java', 479), ('NumberUtils.java', 489)]

Ground_Truth_Answerable: True

- SBFL   ranked 906 statement(s)
- Hybrid ranked 61 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 120 | NumberUtils.java:512 | 0.377964 | `} catch (NumberFormatException nfe) {` |
| 1 | 120 | NumberUtils.java:515 | 0.377964 | `return createBigInteger(numeric);` |
| 1 | 120 | NumberUtils.java:588 | 0.377964 | `if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {` |
| 1 | 120 | NumberUtils.java:589 | 0.377964 | `return d;` |
| 1 | 120 | SystemUtils.java:104 | 0.377964 | `public static final String AWT_TOOLKIT = getSystemProperty("awt.toolkit");` |
| 1 | 120 | SystemUtils.java:127 | 0.377964 | `public static final String FILE_ENCODING = getSystemProperty("file.encoding");` |
| 1 | 120 | SystemUtils.java:146 | 0.377964 | `public static final String FILE_SEPARATOR = getSystemProperty("file.separator");` |
| 1 | 120 | SystemUtils.java:165 | 0.377964 | `public static final String JAVA_AWT_FONTS = getSystemProperty("java.awt.fonts");` |
| 1 | 120 | SystemUtils.java:184 | 0.377964 | `public static final String JAVA_AWT_GRAPHICSENV = getSystemProperty("java.awt.graphicsenv");` |
| 1 | 120 | SystemUtils.java:206 | 0.377964 | `public static final String JAVA_AWT_HEADLESS = getSystemProperty("java.awt.headless");` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 61 | BooleanUtils.java:45 | 0.0 | `super();` |
| 1 | 61 | NumberUtils.java:85 | 0.0 | `super();` |
| 1 | 61 | NumberUtils.java:453 | 0.0 | `if (str == null) {` |
| 1 | 61 | NumberUtils.java:454 | 0.0 | `return null;` |
| 1 | 61 | NumberUtils.java:456 | 0.0 | `if (StringUtils.isBlank(str)) {` |
| 1 | 61 | NumberUtils.java:459 | 0.0 | `if (str.startsWith("--")) {` |
| 1 | 61 | NumberUtils.java:466 | 0.0 | `if (str.startsWith("0x") || str.startsWith("-0x")) {` |
| 1 | 61 | NumberUtils.java:469 | 0.0 | `char lastChar = str.charAt(str.length() - 1);` |
| 1 | 61 | NumberUtils.java:473 | 0.0 | `int decPos = str.indexOf('.');` |
| 1 | 61 | NumberUtils.java:474 | 0.0 | `int expPos = str.indexOf('e') + str.indexOf('E') + 1;` |

