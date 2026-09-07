# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('FilteringParserDelegate.java', 238), ('FilteringParserDelegate.java', 248)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('FilteringParserDelegate.java', 248, '->', 238)]

Ground_Truth_Answerable: True

- SBFL   ranked 1268 statement(s)
- Hybrid ranked 427 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | FilteringParserDelegate.java:148 | 0.816497 | `@Override public JsonToken getCurrentToken() { return _currToken; }` |
| 2 | 6 | FilteringParserDelegate.java:239 | 0.707107 | `if (_headContext.isStartHandled()) {` |
| 2 | 6 | FilteringParserDelegate.java:240 | 0.707107 | `return (_currToken = null);` |
| 2 | 6 | FilteringParserDelegate.java:587 | 0.707107 | `t = _nextTokenWithBuffering(_headContext);` |
| 2 | 6 | FilteringParserDelegate.java:588 | 0.707107 | `if (t != null) {` |
| 2 | 6 | FilteringParserDelegate.java:589 | 0.707107 | `_currToken = t;` |
| 2 | 6 | FilteringParserDelegate.java:590 | 0.707107 | `return t;` |
| 8 | 10 | FilteringParserDelegate.java:429 | 0.654654 | `_currToken = t;` |
| 8 | 10 | FilteringParserDelegate.java:430 | 0.654654 | `return t;` |
| 8 | 10 | FilteringParserDelegate.java:634 | 0.654654 | `f = _headContext.checkValue(_itemFilter);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 11 | FilteringParserDelegate.java:239 | 0.707107 | `if (_headContext.isStartHandled()) {` |
| 1 | 11 | FilteringParserDelegate.java:240 | 0.707107 | `return (_currToken = null);` |
| 1 | 11 | FilteringParserDelegate.java:588 | 0.707107 | `if (t != null) {` |
| 1 | 11 | FilteringParserDelegate.java:589 | 0.707107 | `_currToken = t;` |
| 1 | 11 | FilteringParserDelegate.java:751 | 0.707107 | `if (t != null) {` |
| 1 | 11 | FilteringParserDelegate.java:752 | 0.707107 | `return t;` |
| 1 | 11 | FilteringParserDelegate.java:794 | 0.707107 | `if ((_currToken != JsonToken.START_OBJECT)` |
| 1 | 11 | FilteringParserDelegate.java:803 | 0.707107 | `JsonToken t = nextToken();` |
| 1 | 11 | FilteringParserDelegate.java:804 | 0.707107 | `if (t == null) { // not ideal but for now, just return` |
| 1 | 11 | FilteringParserDelegate.java:805 | 0.707107 | `return this;` |

