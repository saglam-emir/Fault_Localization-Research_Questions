# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DataUtil.java', 5), ('DataUtil.java', 136)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/helper/DataUtil.java', 5)]

- SBFL   ranked 3516 statement(s)
- Hybrid ranked 493 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | DataUtil.java:65 | 0.333333 | `return parseInputStream(in, charsetName, baseUri, Parser.htmlParser());` |
| 1 | 5 | HtmlTreeBuilderState.java:22 | 0.333333 | `tb.insert(t.asComment());` |
| 1 | 5 | HtmlTreeBuilderState.java:161 | 0.333333 | `return anythingElse(t, tb);` |
| 1 | 5 | HtmlTreeBuilderState.java:240 | 0.333333 | `anythingElse(t, tb);` |
| 1 | 5 | Jsoup.java:118 | 0.333333 | `return DataUtil.load(in, charsetName, baseUri);` |
| 6 | 8 | DataUtil.java:132 | 0.288675 | `Node first = doc.childNode(0);` |
| 6 | 8 | DataUtil.java:133 | 0.288675 | `XmlDeclaration decl = null;` |
| 6 | 8 | DataUtil.java:134 | 0.288675 | `if (first instanceof XmlDeclaration)` |
| 6 | 8 | DataUtil.java:136 | 0.288675 | `if (decl != null) {` |
| 6 | 8 | Document.java:76 | 0.288675 | `return findFirstElementByTagName("body", this);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 80 | CharacterReader.java:131 | 1.0 | `for (int i = bufPos; i < bufLength; i++) {` |
| 1 | 80 | CharacterReader.java:132 | 1.0 | `if (c == charBuf[i])` |
| 1 | 80 | CharacterReader.java:133 | 1.0 | `return i - bufPos;` |
| 1 | 80 | CharacterReader.java:169 | 1.0 | `int offset = nextIndexOf(c);` |
| 1 | 80 | CharacterReader.java:170 | 1.0 | `if (offset != -1) {` |
| 1 | 80 | CharacterReader.java:171 | 1.0 | `String consumed = cacheString(charBuf, stringCache, bufPos, offset);` |
| 1 | 80 | CharacterReader.java:172 | 1.0 | `bufPos += offset;` |
| 1 | 80 | CharacterReader.java:230 | 1.0 | `final int start = bufPos;` |
| 1 | 80 | CharacterReader.java:238 | 1.0 | `bufPos++;` |
| 1 | 80 | CharacterReader.java:241 | 1.0 | `return bufPos > start ? cacheString(charBuf, stringCache, start, bufPos -start) : "";` |

