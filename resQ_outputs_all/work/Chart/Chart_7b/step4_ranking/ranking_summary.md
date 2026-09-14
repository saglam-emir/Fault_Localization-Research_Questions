# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TimePeriodValues.java\t(revision 1086)', 299), ('TimePeriodValues.java\t(revision 1086)', 301)]

Ground_Truth_Answerable: True

- SBFL   ranked 396 statement(s)
- Hybrid ranked 71 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | TimePeriodValues.java:552 | 0.707107 | `return this.maxMiddleIndex;` |
| 2 | 3 | TimePeriodValues.java:267 | 0.447214 | `this.minStartIndex = index;` |
| 2 | 3 | TimePeriodValues.java:292 | 0.447214 | `this.minMiddleIndex = index;` |
| 2 | 3 | TimePeriodValues.java:317 | 0.447214 | `this.minEndIndex = index;` |
| 5 | 6 | SimpleTimePeriod.java:76 | 0.377964 | `public SimpleTimePeriod(long start, long end) {` |
| 5 | 6 | SimpleTimePeriod.java:77 | 0.377964 | `if (start > end) {` |
| 5 | 6 | SimpleTimePeriod.java:80 | 0.377964 | `this.start = start;` |
| 5 | 6 | SimpleTimePeriod.java:81 | 0.377964 | `this.end = end;` |
| 5 | 6 | SimpleTimePeriod.java:100 | 0.377964 | `return new Date(this.start);` |
| 5 | 6 | SimpleTimePeriod.java:120 | 0.377964 | `return new Date(this.end);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | TimePeriodValues.java:316 | 1.0 | `if (end < minEnd) {` |
| 1 | 2 | TimePeriodValues.java:317 | 1.0 | `this.minEndIndex = index;` |
| 3 | 4 | TimePeriodValues.java:267 | 0.707107 | `this.minStartIndex = index;` |
| 3 | 4 | TimePeriodValues.java:290 | 0.707107 | `long minMiddle = s + (e - s) / 2;` |
| 3 | 4 | TimePeriodValues.java:291 | 0.707107 | `if (middle < minMiddle) {` |
| 3 | 4 | TimePeriodValues.java:292 | 0.707107 | `this.minMiddleIndex = index;` |
| 7 | 8 | TimePeriodValues.java:205 | 0.57735 | `return (TimePeriodValue) this.data.get(index);` |
| 7 | 8 | TimePeriodValues.java:264 | 0.57735 | `long minStart = getDataItem(this.minStartIndex).getPeriod()` |
| 7 | 8 | TimePeriodValues.java:286 | 0.57735 | `long s = getDataItem(this.minMiddleIndex).getPeriod().getStart()` |
| 7 | 8 | TimePeriodValues.java:288 | 0.57735 | `long e = getDataItem(this.minMiddleIndex).getPeriod().getEnd()` |

