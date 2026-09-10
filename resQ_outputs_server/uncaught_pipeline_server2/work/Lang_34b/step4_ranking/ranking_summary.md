# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ToStringStyle.java', 148), ('ToStringStyle.java', 164)]

Ground_Truth_Answerable: True

- SBFL   ranked 1963 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ToStringBuilder.java:155 | 0.897085 | `return ReflectionToStringBuilder.toString(object);` |
| 2 | 1 | ReflectionToStringBuilder.java:123 | 0.882498 | `return toString(object, null, false, false, null);` |
| 3 | 12 | ReflectionToStringBuilder.java:527 | 0.866025 | `this.reflectionAppendArray(this.getObject());` |
| 3 | 12 | ReflectionToStringBuilder.java:528 | 0.866025 | `return;` |
| 3 | 12 | ReflectionToStringBuilder.java:622 | 0.866025 | `this.getStyle().reflectionAppendArrayDetail(this.getStringBuffer(), null, array);` |
| 3 | 12 | ReflectionToStringBuilder.java:623 | 0.866025 | `return this;` |
| 3 | 12 | ToStringStyle.java:923 | 0.866025 | `buffer.append(arrayStart);` |
| 3 | 12 | ToStringStyle.java:924 | 0.866025 | `int length = Array.getLength(array);` |
| 3 | 12 | ToStringStyle.java:925 | 0.866025 | `for (int i = 0; i < length; i++) {` |
| 3 | 12 | ToStringStyle.java:926 | 0.866025 | `Object item = Array.get(array, i);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ToStringStyle.java:107 | 0.0 | `public static final ToStringStyle NO_FIELD_NAMES_STYLE = new NoFieldNameToStringStyle();` |

