# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 133), ('DataUtil.java', 132)]

Ground_Truth_Answerable: True

- SBFL   ranked 2212 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | DataUtil.java:128 | 0.5 | `if (contentType == null) return null;` |
| 1 | 6 | DataUtil.java:129 | 0.5 | `Matcher m = charsetPattern.matcher(contentType);` |
| 1 | 6 | DataUtil.java:130 | 0.5 | `if (m.find()) {` |
| 1 | 6 | DataUtil.java:131 | 0.5 | `String charset = m.group(1).trim();` |
| 1 | 6 | DataUtil.java:132 | 0.5 | `charset = charset.toUpperCase(Locale.ENGLISH);` |
| 1 | 6 | DataUtil.java:133 | 0.5 | `return charset;` |
| 7 | 1 | DataUtil.java:19 | 0.288675 | `private static final Pattern charsetPattern = Pattern.compile("(?i)\\bcharset=\\s*\"?([^\\s;\"]*)");` |
| 8 | 2205 | Attribute.java:21 | 0.0 | `public Attribute(String key, String value) {` |
| 8 | 2205 | Attribute.java:22 | 0.0 | `Validate.notEmpty(key);` |
| 8 | 2205 | Attribute.java:23 | 0.0 | `Validate.notNull(value);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

