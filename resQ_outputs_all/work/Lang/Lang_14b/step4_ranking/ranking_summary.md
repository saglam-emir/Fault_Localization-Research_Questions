# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StringUtils.java', 788), ('StringUtils.java', 789)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/StringUtils.java', 789)]

- SBFL   ranked 5340 statement(s)
- Hybrid ranked 911 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | StringUtils.java:782 | 0.235702 | `if (cs1 == cs2) {` |
| 1 | 4 | StringUtils.java:783 | 0.235702 | `return true;` |
| 1 | 4 | StringUtils.java:785 | 0.235702 | `if (cs1 == null || cs2 == null) {` |
| 1 | 4 | StringUtils.java:788 | 0.235702 | `return cs1.equals(cs2);` |
| 5 | 1 | StringUtils.java:148 | 0.019309 | `private static final Pattern WHITESPACE_BLOCK = Pattern.compile("\\s+");` |
| 6 | 5335 | AggregateTranslator.java:40 | 0.0 | `public AggregateTranslator(CharSequenceTranslator... translators) {` |
| 6 | 5335 | AggregateTranslator.java:41 | 0.0 | `this.translators = ArrayUtils.clone(translators);` |
| 6 | 5335 | AggregateTranslator.java:51 | 0.0 | `for (CharSequenceTranslator translator : translators) {` |
| 6 | 5335 | AggregateTranslator.java:52 | 0.0 | `int consumed = translator.translate(input, index, out);` |
| 6 | 5335 | AggregateTranslator.java:53 | 0.0 | `if(consumed != 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StringUtils.java:788 | 0.408248 | `return cs1.equals(cs2);` |
| 2 | 910 | ArrayUtils.java:57 | 0.0 | `public static final String[] EMPTY_STRING_ARRAY = new String[0];` |
| 2 | 910 | ArrayUtils.java:1403 | 0.0 | `if (array == null) {` |
| 2 | 910 | ArrayUtils.java:1406 | 0.0 | `int i = 0;` |
| 2 | 910 | ArrayUtils.java:1407 | 0.0 | `int j = array.length - 1;` |
| 2 | 910 | ArrayUtils.java:1409 | 0.0 | `while (j > i) {` |
| 2 | 910 | ArrayUtils.java:1410 | 0.0 | `tmp = array[j];` |
| 2 | 910 | ArrayUtils.java:1411 | 0.0 | `array[j] = array[i];` |
| 2 | 910 | ArrayUtils.java:1412 | 0.0 | `array[i] = tmp;` |
| 2 | 910 | CharSequenceUtils.java:70 | 0.0 | `if (cs instanceof String) {` |

