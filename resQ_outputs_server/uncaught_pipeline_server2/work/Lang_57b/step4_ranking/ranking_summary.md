# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('LocaleUtils.java', 223)]

Ground_Truth_Answerable: True

- SBFL   ranked 5 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | LocaleUtils.java:47 | 1.0 | `private static final Map cLanguagesByCountry = Collections.synchronizedMap(new HashMap());` |
| 1 | 5 | LocaleUtils.java:49 | 1.0 | `private static final Map cCountriesByLanguage = Collections.synchronizedMap(new HashMap());` |
| 1 | 5 | LocaleUtils.java:51 | 1.0 | `List list = Arrays.asList(Locale.getAvailableLocales());` |
| 1 | 5 | LocaleUtils.java:52 | 1.0 | `cAvailableLocaleList = Collections.unmodifiableList(list);` |
| 1 | 5 | LocaleUtils.java:223 | 1.0 | `return cAvailableLocaleSet.contains(locale);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

