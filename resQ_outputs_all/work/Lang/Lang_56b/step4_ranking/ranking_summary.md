# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateFormat.java', 140), ('FastDateFormat.java', 144), ('FastDateFormat.java', 1022)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/time/FastDateFormat.java', 140), ('src/java/org/apache/commons/lang/time/FastDateFormat.java', 144), ('src/java/org/apache/commons/lang/time/FastDateFormat.java', 1022)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see answerability_bySlicers.csv).

- SBFL   ranked 585 statement(s)
- Hybrid ranked 25 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 44 | ExceptionUtils.java:62 | 0.707107 | `private static String[] CAUSE_METHOD_NAMES = {` |
| 1 | 44 | ExceptionUtils.java:90 | 0.707107 | `causeMethod = Throwable.class.getMethod("getCause", null);` |
| 1 | 44 | ExceptionUtils.java:94 | 0.707107 | `THROWABLE_CAUSE_METHOD = causeMethod;` |
| 1 | 44 | ExceptionUtils.java:96 | 0.707107 | `causeMethod = Throwable.class.getMethod("initCause", new Class[]{Throwable.class});` |
| 1 | 44 | ExceptionUtils.java:100 | 0.707107 | `THROWABLE_INITCAUSE_METHOD = causeMethod;` |
| 1 | 44 | ExceptionUtils.java:431 | 0.707107 | `return THROWABLE_CAUSE_METHOD != null;` |
| 1 | 44 | NestableDelegate.java:68 | 0.707107 | `private Throwable nestable = null;` |
| 1 | 44 | NestableDelegate.java:78 | 0.707107 | `public static boolean topDown = true;` |
| 1 | 44 | NestableDelegate.java:88 | 0.707107 | `public static boolean trimStackFrames = true;` |
| 1 | 44 | NestableDelegate.java:98 | 0.707107 | `public static boolean matchSubclasses = true;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 15 | FastDateFormat.java:111 | 0.333333 | `private static Map cInstanceCache = new HashMap(7);` |
| 1 | 15 | FastDateFormat.java:167 | 0.333333 | `return getInstance(pattern, null, null);` |
| 1 | 15 | FastDateFormat.java:213 | 0.333333 | `FastDateFormat emptyFormat = new FastDateFormat(pattern, timeZone, locale);` |
| 1 | 15 | FastDateFormat.java:214 | 0.333333 | `FastDateFormat format = (FastDateFormat) cInstanceCache.get(emptyFormat);` |
| 1 | 15 | FastDateFormat.java:215 | 0.333333 | `if (format == null) {` |
| 1 | 15 | FastDateFormat.java:216 | 0.333333 | `format = emptyFormat;` |
| 1 | 15 | FastDateFormat.java:220 | 0.333333 | `return format;` |
| 1 | 15 | FastDateFormat.java:539 | 0.333333 | `super();` |
| 1 | 15 | FastDateFormat.java:543 | 0.333333 | `mPattern = pattern;` |
| 1 | 15 | FastDateFormat.java:545 | 0.333333 | `mTimeZoneForced = (timeZone != null);` |

