# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Frequency.java', 110), ('Frequency.java', 111)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/math/stat/Frequency.java', 111)]

- SBFL   ranked 93 statement(s)
- Hybrid ranked 42 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Frequency.java:110 | 0.707107 | `addValue((Comparable<?>) v);` |
| 2 | 2 | Frequency.java:57 | 0.377964 | `public Frequency() {` |
| 2 | 2 | Frequency.java:58 | 0.377964 | `freqTable = new TreeMap();` |
| 4 | 90 | Frequency.java:66 | 0.0 | `public Frequency(Comparator comparator) {` |
| 4 | 90 | Frequency.java:67 | 0.0 | `freqTable = new TreeMap(comparator);` |
| 4 | 90 | Frequency.java:78 | 0.0 | `NumberFormat nf = NumberFormat.getPercentInstance();` |
| 4 | 90 | Frequency.java:79 | 0.0 | `StringBuffer outBuffer = new StringBuffer();` |
| 4 | 90 | Frequency.java:80 | 0.0 | `outBuffer.append("Value \t Freq. \t Pct. \t Cum Pct. \n");` |
| 4 | 90 | Frequency.java:81 | 0.0 | `Iterator iter = freqTable.keySet().iterator();` |
| 4 | 90 | Frequency.java:82 | 0.0 | `while (iter.hasNext()) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Frequency.java:57 | 1.0 | `public Frequency() {` |
| 2 | 1 | Frequency.java:58 | 0.408248 | `freqTable = new TreeMap();` |
| 3 | 40 | Frequency.java:174 | 0.0 | `addValue(Character.valueOf(v));` |
| 3 | 40 | Frequency.java:192 | 0.0 | `return freqTable.keySet().iterator();` |
| 3 | 40 | Frequency.java:203 | 0.0 | `long result = 0;` |
| 3 | 40 | Frequency.java:204 | 0.0 | `Iterator iterator = freqTable.values().iterator();` |
| 3 | 40 | Frequency.java:205 | 0.0 | `while (iterator.hasNext())  {` |
| 3 | 40 | Frequency.java:206 | 0.0 | `result += ((Long) iterator.next()).longValue();` |
| 3 | 40 | Frequency.java:208 | 0.0 | `return result;` |
| 3 | 40 | Frequency.java:219 | 0.0 | `if (v instanceof Integer) {` |

