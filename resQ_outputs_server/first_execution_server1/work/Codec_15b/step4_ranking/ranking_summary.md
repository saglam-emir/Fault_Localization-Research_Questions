# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Soundex.java', 188), ('Soundex.java', 189), ('Soundex.java', 190), ('Soundex.java', 191), ('Soundex.java', 192), ('Soundex.java', 195)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Soundex.java', 195, '->', 189)]

Ground_Truth_Answerable: True

- SBFL   ranked 171 statement(s)
- Hybrid ranked 1 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Soundex.java:193 | 0.5 | `return 0;` |
| 2 | 3 | Soundex.java:190 | 0.377964 | `final char preHWChar = str.charAt(index - 2);` |
| 2 | 3 | Soundex.java:191 | 0.377964 | `final char firstCode = this.map(preHWChar);` |
| 2 | 3 | Soundex.java:192 | 0.377964 | `if (firstCode == mappedChar || 'H' == preHWChar || 'W' == preHWChar) {` |
| 5 | 1 | Soundex.java:167 | 0.229416 | `return soundex(str);` |
| 6 | 1 | SoundexUtils.java:54 | 0.218218 | `return str.toUpperCase(java.util.Locale.ENGLISH);` |
| 7 | 7 | Soundex.java:188 | 0.213201 | `final char hwChar = str.charAt(index - 1);` |
| 7 | 7 | Soundex.java:189 | 0.213201 | `if ('H' == hwChar || 'W' == hwChar) {` |
| 7 | 7 | Soundex.java:273 | 0.213201 | `mapped = getMappingCode(str, incount++);` |
| 7 | 7 | Soundex.java:274 | 0.213201 | `if (mapped != 0) {` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | Soundex.java:81 | 0.110432 | `public Soundex() {` |

