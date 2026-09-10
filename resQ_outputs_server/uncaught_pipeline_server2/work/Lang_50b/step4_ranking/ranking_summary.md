# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateFormat.java', 285), ('FastDateFormat.java', 286), ('FastDateFormat.java', 292), ('FastDateFormat.java', 293), ('FastDateFormat.java', 294), ('FastDateFormat.java', 289), ('FastDateFormat.java', 465), ('FastDateFormat.java', 466), ('FastDateFormat.java', 471), ('FastDateFormat.java', 472), ('FastDateFormat.java', 473), ('FastDateFormat.java', 468)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/time/FastDateFormat.java', 294), ('src/java/org/apache/commons/lang/time/FastDateFormat.java', 289), ('src/java/org/apache/commons/lang/time/FastDateFormat.java', 473), ('src/java/org/apache/commons/lang/time/FastDateFormat.java', 468)]

- SBFL   ranked 597 statement(s)
- Hybrid ranked 168 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | FastDateFormat.java:620 | 0.707107 | `rule = new TextField(Calendar.MONTH, months);` |
| 2 | 4 | FastDateFormat.java:1708 | 0.57735 | `public Pair(Object obj1, Object obj2) {` |
| 2 | 4 | FastDateFormat.java:1709 | 0.57735 | `mObj1 = obj1;` |
| 2 | 4 | FastDateFormat.java:1710 | 0.57735 | `mObj2 = obj2;` |
| 2 | 4 | FastDateFormat.java:1738 | 0.57735 | `return` |
| 6 | 35 | FastDateFormat.java:234 | 0.5 | `return getDateInstance(style, null, null);` |
| 6 | 35 | FastDateFormat.java:293 | 0.5 | `locale = Locale.getDefault();` |
| 6 | 35 | FastDateFormat.java:408 | 0.5 | `return getDateTimeInstance(dateStyle, timeStyle, null, null);` |
| 6 | 35 | FastDateFormat.java:425 | 0.5 | `return getDateTimeInstance(dateStyle, timeStyle, null, locale);` |
| 6 | 35 | FastDateFormat.java:461 | 0.5 | `Object key = new Pair(new Integer(dateStyle), new Integer(timeStyle));` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | FastDateFormat.java:585 | 0.707107 | `String[] months = symbols.getMonths();` |
| 1 | 11 | FastDateFormat.java:587 | 0.707107 | `String[] weekdays = symbols.getWeekdays();` |
| 1 | 11 | FastDateFormat.java:620 | 0.707107 | `rule = new TextField(Calendar.MONTH, months);` |
| 1 | 11 | FastDateFormat.java:648 | 0.707107 | `rule = new TextField(Calendar.DAY_OF_WEEK, tokenLen < 4 ? shortWeekdays : weekdays);` |
| 1 | 11 | FastDateFormat.java:690 | 0.707107 | `rule = new StringLiteral(sub);` |
| 1 | 11 | FastDateFormat.java:1112 | 0.707107 | `StringLiteral(String value) {` |
| 1 | 11 | FastDateFormat.java:1113 | 0.707107 | `mValue = value;` |
| 1 | 11 | FastDateFormat.java:1120 | 0.707107 | `return mValue.length();` |
| 1 | 11 | FastDateFormat.java:1708 | 0.707107 | `public Pair(Object obj1, Object obj2) {` |
| 1 | 11 | FastDateFormat.java:1709 | 0.707107 | `mObj1 = obj1;` |

