# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NumericEntityUnescaper.java', 40), ('NumericEntityUnescaper.java', 54), ('NumericEntityUnescaper.java', 50), ('NumericEntityUnescaper.java', 80), ('NumericEntityUnescaper.java', 79)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('NumericEntityUnescaper.java', 50, '->', 45), ('NumericEntityUnescaper.java', 79, '->', 40)]

Ground_Truth_Answerable: True

- SBFL   ranked 633 statement(s)
- Hybrid ranked 2 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | NumericEntityUnescaper.java:41 | 0.57735 | `int start = index + 2;` |
| 1 | 3 | NumericEntityUnescaper.java:42 | 0.57735 | `boolean isHex = false;` |
| 1 | 3 | NumericEntityUnescaper.java:44 | 0.57735 | `char firstChar = input.charAt(start);` |
| 4 | 2 | NumericEntityUnescaper.java:46 | 0.5 | `start++;` |
| 4 | 2 | NumericEntityUnescaper.java:47 | 0.5 | `isHex = true;` |
| 6 | 1 | NumericEntityUnescaper.java:82 | 0.471405 | `return 0;` |
| 7 | 2 | NumericEntityUnescaper.java:38 | 0.426401 | `int seqEnd = input.length();` |
| 7 | 2 | NumericEntityUnescaper.java:40 | 0.426401 | `if(input.charAt(index) == '&' && index < seqEnd - 1 && input.charAt(index + 1) == '#') {` |
| 9 | 1 | CharSequenceTranslator.java:89 | 0.365148 | `out.write(Character.toChars(Character.codePointAt(input, i)));` |
| 10 | 7 | CharSequenceTranslator.java:54 | 0.316228 | `if (input == null) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CharSequenceTranslator.java:32 | 1.0 | `public abstract class CharSequenceTranslator {` |
| 1 | 2 | NumericEntityUnescaper.java:31 | 1.0 | `public class NumericEntityUnescaper extends CharSequenceTranslator {` |

