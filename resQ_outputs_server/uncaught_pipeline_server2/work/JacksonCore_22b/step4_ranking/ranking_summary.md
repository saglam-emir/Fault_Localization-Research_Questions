# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FilteringParserDelegate.java', 417), ('FilteringParserDelegate.java', 440), ('FilteringParserDelegate.java', 441), ('FilteringParserDelegate.java', 575), ('FilteringParserDelegate.java', 600), ('FilteringParserDelegate.java', 601), ('FilteringParserDelegate.java', 717), ('FilteringParserDelegate.java', 732), ('FilteringParserDelegate.java', 733), ('FilteringParserDelegate.java', 771)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('FilteringParserDelegate.java', 441, '->', 438), ('FilteringParserDelegate.java', 601, '->', 598), ('FilteringParserDelegate.java', 733, '->', 730)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/com/fasterxml/jackson/core/filter/FilteringParserDelegate.java', 771)]

- SBFL   ranked 1345 statement(s)
- Hybrid ranked 555 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | FilteringParserDelegate.java:139 | 0.957427 | `return _matchCount;` |
| 2 | 7 | GeneratorBase.java:174 | 0.92582 | `final int mask = f.getMask();` |
| 2 | 7 | GeneratorBase.java:175 | 0.92582 | `_features &= ~mask;` |
| 2 | 7 | GeneratorBase.java:176 | 0.92582 | `if ((mask & DERIVED_FEATURES_MASK) != 0) {` |
| 2 | 7 | GeneratorBase.java:185 | 0.92582 | `return this;` |
| 2 | 7 | JsonGeneratorImpl.java:140 | 0.92582 | `super.disable(f);` |
| 2 | 7 | JsonGeneratorImpl.java:141 | 0.92582 | `if (f == Feature.QUOTE_FIELD_NAMES) {` |
| 2 | 7 | JsonGeneratorImpl.java:144 | 0.92582 | `return this;` |
| 9 | 1 | TokenFilter.java:66 | 0.894427 | `return this;` |
| 10 | 8 | TokenFilterContext.java:83 | 0.848668 | `_type = type;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | FilteringParserDelegate.java:374 | 0.816497 | `boolean returnEnd = _headContext.isStartHandled();` |
| 1 | 6 | FilteringParserDelegate.java:379 | 0.816497 | `_headContext = _headContext.getParent();` |
| 1 | 6 | FilteringParserDelegate.java:380 | 0.816497 | `_itemFilter = _headContext.getFilter();` |
| 1 | 6 | FilteringParserDelegate.java:381 | 0.816497 | `if (returnEnd) {` |
| 1 | 6 | FilteringParserDelegate.java:382 | 0.816497 | `return (_currToken = t);` |
| 1 | 6 | TokenFilterContext.java:282 | 0.816497 | `public boolean isStartHandled() { return _startHandled; }` |
| 7 | 3 | ReaderBasedJsonParser.java:232 | 0.783349 | `final int bufSize = _inputEnd;` |
| 7 | 3 | ReaderBasedJsonParser.java:235 | 0.783349 | `_currInputRowStart -= bufSize;` |
| 7 | 3 | ReaderBasedJsonParser.java:2331 | 0.783349 | `if (!_loadMore()) {` |
| 10 | 6 | FilteringParserDelegate.java:290 | 0.7698 | `_currToken = t;` |

