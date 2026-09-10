# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FastDateFormat.java', 872)]

Ground_Truth_Answerable: True

- SBFL   ranked 699 statement(s)
- Hybrid ranked 26 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | FastDateFormat.java:642 | 0.57735 | `rule = selectNumberRule(Calendar.MILLISECOND, tokenLen);` |
| 1 | 4 | FastDateFormat.java:643 | 0.57735 | `break;` |
| 1 | 4 | FastDateFormat.java:872 | 0.57735 | `calendar = (Calendar) calendar.clone();` |
| 1 | 4 | FastDateFormat.java:873 | 0.57735 | `calendar.setTimeZone(mTimeZone);` |
| 5 | 1 | FastDateFormat.java:182 | 0.408248 | `return getInstance(pattern, timeZone, null);` |
| 6 | 4 | FastDateFormat.java:1300 | 0.333333 | `for (int i = mSize; --i >= 2; ) {` |
| 6 | 4 | FastDateFormat.java:1301 | 0.333333 | `buffer.append('0');` |
| 6 | 4 | FastDateFormat.java:1303 | 0.333333 | `buffer.append((char)(value / 10 + '0'));` |
| 6 | 4 | FastDateFormat.java:1304 | 0.333333 | `buffer.append((char)(value % 10 + '0'));` |
| 10 | 3 | FastDateFormat.java:1423 | 0.103695 | `appendTo(buffer, calendar.get(Calendar.MONTH) + 1);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 26 | FastDateFormat.java:111 | 1.0 | `private static final Map<FastDateFormat, FastDateFormat> cInstanceCache = new HashMap<FastDateFormat, FastDateFormat>(7);` |
| 1 | 26 | FastDateFormat.java:182 | 1.0 | `return getInstance(pattern, timeZone, null);` |
| 1 | 26 | FastDateFormat.java:213 | 1.0 | `FastDateFormat emptyFormat = new FastDateFormat(pattern, timeZone, locale);` |
| 1 | 26 | FastDateFormat.java:214 | 1.0 | `FastDateFormat format = cInstanceCache.get(emptyFormat);` |
| 1 | 26 | FastDateFormat.java:215 | 1.0 | `if (format == null) {` |
| 1 | 26 | FastDateFormat.java:216 | 1.0 | `format = emptyFormat;` |
| 1 | 26 | FastDateFormat.java:217 | 1.0 | `format.init();  // convert shell format into usable one` |
| 1 | 26 | FastDateFormat.java:220 | 1.0 | `return format;` |
| 1 | 26 | FastDateFormat.java:535 | 1.0 | `super();` |
| 1 | 26 | FastDateFormat.java:539 | 1.0 | `mPattern = pattern;` |

