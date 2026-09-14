# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ExtendedMessageFormat.java', 422)]

Ground_Truth_Answerable: True

- SBFL   ranked 231 statement(s)
- Hybrid ranked 77 statement(s)

> **WARNING**: every Virtual_Fail column covers zero statements in the slice universe (only passing-test slices contributed). Every statement therefore scores Ochiai=0.0 and ties for rank 1 - any rq5.csv rank_best_slice=1 for this bug is a degenerate tie-break artifact, not genuine localization - see step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | ExtendedMessageFormat.java:158 | 0.57735 | `appendQuotedString(pattern, pos, stripCustom, true);` |
| 1 | 6 | ExtendedMessageFormat.java:159 | 0.57735 | `break;` |
| 1 | 6 | ExtendedMessageFormat.java:419 | 0.57735 | `int start = pos.getIndex();` |
| 1 | 6 | ExtendedMessageFormat.java:420 | 0.57735 | `char[] c = pattern.toCharArray();` |
| 1 | 6 | ExtendedMessageFormat.java:421 | 0.57735 | `if (escapingOn && c[start] == QUOTE) {` |
| 1 | 6 | ExtendedMessageFormat.java:422 | 0.57735 | `return appendTo == null ? null : appendTo.append(QUOTE);` |
| 7 | 1 | ExtendedMessageFormat.java:112 | 0.333333 | `this(pattern, Locale.getDefault(), registry);` |
| 8 | 12 | ExtendedMessageFormat.java:148 | 0.288675 | `ArrayList foundFormats = new ArrayList();` |
| 8 | 12 | ExtendedMessageFormat.java:149 | 0.288675 | `ArrayList foundDescriptions = new ArrayList();` |
| 8 | 12 | ExtendedMessageFormat.java:150 | 0.288675 | `StringBuffer stripCustom = new StringBuffer(pattern.length());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 77 | ExtendedMessageFormat.java:112 | 0.0 | `this(pattern, Locale.getDefault(), registry);` |
| 1 | 77 | ExtendedMessageFormat.java:124 | 0.0 | `super(DUMMY_PATTERN);` |
| 1 | 77 | ExtendedMessageFormat.java:125 | 0.0 | `setLocale(locale);` |
| 1 | 77 | ExtendedMessageFormat.java:126 | 0.0 | `this.registry = registry;` |
| 1 | 77 | ExtendedMessageFormat.java:127 | 0.0 | `applyPattern(pattern);` |
| 1 | 77 | ExtendedMessageFormat.java:143 | 0.0 | `if (registry == null) {` |
| 1 | 77 | ExtendedMessageFormat.java:148 | 0.0 | `ArrayList foundFormats = new ArrayList();` |
| 1 | 77 | ExtendedMessageFormat.java:149 | 0.0 | `ArrayList foundDescriptions = new ArrayList();` |
| 1 | 77 | ExtendedMessageFormat.java:150 | 0.0 | `StringBuffer stripCustom = new StringBuffer(pattern.length());` |
| 1 | 77 | ExtendedMessageFormat.java:152 | 0.0 | `ParsePosition pos = new ParsePosition(0);` |

