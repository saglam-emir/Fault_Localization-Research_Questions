# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ClassUtils.java', 191), ('ClassUtils.java', 193), ('ClassUtils.java', 194), ('ClassUtils.java', 195), ('ClassUtils.java', 203), ('ClassUtils.java', 245), ('ClassUtils.java', 250), ('ClassUtils.java', 251)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/ClassUtils.java', 191), ('src/java/org/apache/commons/lang/ClassUtils.java', 193), ('src/java/org/apache/commons/lang/ClassUtils.java', 194), ('src/java/org/apache/commons/lang/ClassUtils.java', 195), ('src/java/org/apache/commons/lang/ClassUtils.java', 250), ('src/java/org/apache/commons/lang/ClassUtils.java', 251)]

- SBFL   ranked 1336 statement(s)
- Hybrid ranked 170 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | ClassUtils.java:170 | 0.707107 | `return StringUtils.EMPTY;` |
| 1 | 2 | ClassUtils.java:230 | 0.707107 | `return StringUtils.EMPTY;` |
| 3 | 2 | ClassUtils.java:229 | 0.5 | `if (cls == null) {` |
| 3 | 2 | ClassUtils.java:232 | 0.5 | `return getPackageName(cls.getName());` |
| 5 | 5 | ClassUtils.java:201 | 0.288675 | `out = out.replace(INNER_CLASS_SEPARATOR_CHAR, PACKAGE_SEPARATOR_CHAR);` |
| 5 | 5 | ClassUtils.java:245 | 0.288675 | `if (className == null) {` |
| 5 | 5 | ClassUtils.java:252 | 0.288675 | `int i = className.lastIndexOf(PACKAGE_SEPARATOR_CHAR);` |
| 5 | 5 | ClassUtils.java:253 | 0.288675 | `if (i == -1) {` |
| 5 | 5 | ClassUtils.java:256 | 0.288675 | `return className.substring(0, i);` |
| 10 | 29 | ClassUtils.java:58 | 0.160128 | `public static final String PACKAGE_SEPARATOR = String.valueOf(PACKAGE_SEPARATOR_CHAR);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ClassUtils.java:232 | 0.408248 | `return getPackageName(cls.getName());` |
| 2 | 1 | ClassUtils.java:229 | 0.353553 | `if (cls == null) {` |
| 3 | 1 | ClassUtils.java:172 | 0.267261 | `return getShortClassName(cls.getName());` |
| 4 | 1 | ClassUtils.java:169 | 0.25 | `if (cls == null) {` |
| 5 | 1 | ClassUtils.java:256 | 0.196116 | `return className.substring(0, i);` |
| 6 | 1 | ClassUtils.java:203 | 0.166667 | `return out;` |
| 7 | 4 | ClassUtils.java:196 | 0.158114 | `int lastDotIdx = className.lastIndexOf(PACKAGE_SEPARATOR_CHAR);` |
| 7 | 4 | ClassUtils.java:199 | 0.158114 | `String out = className.substring(lastDotIdx + 1);` |
| 7 | 4 | ClassUtils.java:252 | 0.158114 | `int i = className.lastIndexOf(PACKAGE_SEPARATOR_CHAR);` |
| 7 | 4 | ClassUtils.java:253 | 0.158114 | `if (i == -1) {` |

