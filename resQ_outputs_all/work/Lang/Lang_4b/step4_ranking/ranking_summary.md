# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LookupTranslator.java', 31), ('LookupTranslator.java', 46), ('LookupTranslator.java', 51), ('LookupTranslator.java', 77)]

Ground_Truth_Answerable: True

- SBFL   ranked 1589 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | LookupTranslator.java:76 | 0.2 | `final CharSequence subSeq = input.subSequence(index, index + i);` |
| 1 | 4 | LookupTranslator.java:77 | 0.2 | `final CharSequence result = lookupMap.get(subSeq);` |
| 1 | 4 | LookupTranslator.java:78 | 0.2 | `if (result != null) {` |
| 1 | 4 | LookupTranslator.java:83 | 0.2 | `return 0;` |
| 5 | 3 | LookupTranslator.java:70 | 0.196116 | `int max = longest;` |
| 5 | 3 | LookupTranslator.java:71 | 0.196116 | `if (index + longest > input.length()) {` |
| 5 | 3 | LookupTranslator.java:75 | 0.196116 | `for (int i = max; i >= shortest; i--) {` |
| 8 | 15 | CharSequenceTranslator.java:32 | 0.179605 | `public abstract class CharSequenceTranslator {` |
| 8 | 15 | LookupTranslator.java:45 | 0.179605 | `public LookupTranslator(final CharSequence[]... lookup) {` |
| 8 | 15 | LookupTranslator.java:46 | 0.179605 | `lookupMap = new HashMap<CharSequence, CharSequence>();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

