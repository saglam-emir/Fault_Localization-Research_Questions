# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Frequency.java', 110), ('Frequency.java', 121)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/stat/Frequency.java', 110)]

- SBFL   ranked 92 statement(s)
- Hybrid ranked 42 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Frequency.java:132 | 0.707107 | `} catch (ClassCastException ex) {` |
| 1 | 2 | Frequency.java:134 | 0.707107 | `throw new IllegalArgumentException("Value not comparable to existing values.");` |
| 3 | 3 | Frequency.java:121 | 0.408248 | `Object obj = v;` |
| 3 | 3 | Frequency.java:122 | 0.408248 | `if (v instanceof Integer) {` |
| 3 | 3 | Frequency.java:126 | 0.408248 | `Long count = (Long) freqTable.get(obj);` |
| 6 | 2 | Frequency.java:57 | 0.377964 | `public Frequency() {` |
| 6 | 2 | Frequency.java:58 | 0.377964 | `freqTable = new TreeMap();` |
| 8 | 85 | Frequency.java:66 | 0.0 | `public Frequency(Comparator comparator) {` |
| 8 | 85 | Frequency.java:67 | 0.0 | `freqTable = new TreeMap(comparator);` |
| 8 | 85 | Frequency.java:78 | 0.0 | `NumberFormat nf = NumberFormat.getPercentInstance();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Frequency.java:57 | 1.0 | `public Frequency() {` |
| 2 | 1 | Frequency.java:58 | 0.408248 | `freqTable = new TreeMap();` |
| 3 | 40 | Frequency.java:171 | 0.0 | `addValue(Character.valueOf(v));` |
| 3 | 40 | Frequency.java:189 | 0.0 | `return freqTable.keySet().iterator();` |
| 3 | 40 | Frequency.java:200 | 0.0 | `long result = 0;` |
| 3 | 40 | Frequency.java:201 | 0.0 | `Iterator iterator = freqTable.values().iterator();` |
| 3 | 40 | Frequency.java:202 | 0.0 | `while (iterator.hasNext())  {` |
| 3 | 40 | Frequency.java:203 | 0.0 | `result += ((Long) iterator.next()).longValue();` |
| 3 | 40 | Frequency.java:205 | 0.0 | `return result;` |
| 3 | 40 | Frequency.java:216 | 0.0 | `if (v instanceof Integer) {` |

