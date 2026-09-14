# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EqualsBuilder.java', 380), ('EqualsBuilder.java', 382)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('EqualsBuilder.java', 380, '->', 379)]

Ground_Truth_Answerable: True

- SBFL   ranked 2270 statement(s)
- Hybrid ranked 288 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | EqualsBuilder.java:372 | 0.176777 | `return this;` |
| 2 | 1 | EqualsBuilder.java:381 | 0.158114 | `isEquals = lhs.equals(rhs);` |
| 3 | 6 | EqualsBuilder.java:368 | 0.104257 | `if (isEquals == false) {` |
| 3 | 6 | EqualsBuilder.java:371 | 0.104257 | `if (lhs == rhs) {` |
| 3 | 6 | EqualsBuilder.java:374 | 0.104257 | `if (lhs == null || rhs == null) {` |
| 3 | 6 | EqualsBuilder.java:378 | 0.104257 | `Class lhsClass = lhs.getClass();` |
| 3 | 6 | EqualsBuilder.java:379 | 0.104257 | `if (!lhsClass.isArray()) {` |
| 3 | 6 | EqualsBuilder.java:408 | 0.104257 | `return this;` |
| 9 | 1 | EqualsBuilder.java:831 | 0.089803 | `return this.isEquals;` |
| 10 | 2 | EqualsBuilder.java:92 | 0.089087 | `private boolean isEquals = true;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | EqualsBuilder.java:381 | 0.235702 | `isEquals = lhs.equals(rhs);` |
| 2 | 3 | EqualsBuilder.java:368 | 0.154303 | `if (isEquals == false) {` |
| 2 | 3 | EqualsBuilder.java:371 | 0.154303 | `if (lhs == rhs) {` |
| 2 | 3 | EqualsBuilder.java:374 | 0.154303 | `if (lhs == null || rhs == null) {` |
| 5 | 2 | EqualsBuilder.java:378 | 0.123091 | `Class lhsClass = lhs.getClass();` |
| 5 | 2 | EqualsBuilder.java:379 | 0.123091 | `if (!lhsClass.isArray()) {` |
| 7 | 1 | EqualsBuilder.java:100 | 0.09325 | `public EqualsBuilder() {` |
| 8 | 1 | EqualsBuilder.java:92 | 0.078567 | `private boolean isEquals = true;` |
| 9 | 280 | ArrayUtils.java:144 | 0.0 | `super();` |
| 9 | 280 | CompareToBuilder.java:111 | 0.0 | `comparison = 0;` |

