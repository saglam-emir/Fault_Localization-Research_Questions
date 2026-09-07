# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LocaleUtils.java', 97), ('LocaleUtils.java', 128)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/lang3/LocaleUtils.java', 128)]

- SBFL   ranked 187 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | LocaleUtils.java:99 | 0.57735 | `throw new IllegalArgumentException("Invalid locale format: " + str);` |
| 2 | 6 | LocaleUtils.java:89 | 0.447214 | `if (str == null) {` |
| 2 | 6 | LocaleUtils.java:92 | 0.447214 | `final int len = str.length();` |
| 2 | 6 | LocaleUtils.java:93 | 0.447214 | `if (len < 2) {` |
| 2 | 6 | LocaleUtils.java:96 | 0.447214 | `final char ch0 = str.charAt(0);` |
| 2 | 6 | LocaleUtils.java:97 | 0.447214 | `final char ch1 = str.charAt(1);` |
| 2 | 6 | LocaleUtils.java:98 | 0.447214 | `if (!Character.isLowerCase(ch0) || !Character.isLowerCase(ch1)) {` |
| 8 | 8 | LocaleUtils.java:42 | 0.27735 | `private static final ConcurrentMap<String, List<Locale>> cLanguagesByCountry =` |
| 8 | 8 | LocaleUtils.java:46 | 0.27735 | `private static final ConcurrentMap<String, List<Locale>> cCountriesByLanguage =` |
| 8 | 8 | LocaleUtils.java:193 | 0.27735 | `return SyncAvoid.AVAILABLE_LOCALE_LIST;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

