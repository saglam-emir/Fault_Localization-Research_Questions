# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StandardToolTipTagFragmentGenerator.java', 65)]

Ground_Truth_Answerable: True

- SBFL   ranked 2 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | StandardToolTipTagFragmentGenerator.java:54 | 1.0 | `super();` |
| 1 | 2 | StandardToolTipTagFragmentGenerator.java:65 | 1.0 | `return " title=\"" + toolTipText` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | StandardToolTipTagFragmentGenerator.java:54 | 0.0 | `super();` |

