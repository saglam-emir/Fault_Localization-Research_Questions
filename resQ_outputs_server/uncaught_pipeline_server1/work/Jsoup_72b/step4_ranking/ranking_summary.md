# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('CharacterReader.java', 427)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/jsoup/parser/CharacterReader.java', 427)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 4041 statement(s)
- Hybrid ranked 27 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | CharacterReader.java:127 | 0.447214 | `return -1;` |
| 1 | 2 | CharacterReader.java:167 | 0.447214 | `return consumeToEnd();` |
| 3 | 2 | CharacterReader.java:254 | 0.258199 | `bufferUp();` |
| 3 | 2 | CharacterReader.java:255 | 0.258199 | `String data = cacheString(charBuf, stringCache, bufPos, bufLength - bufPos);` |
| 5 | 3 | CharacterReader.java:335 | 0.076696 | `return true;` |
| 5 | 3 | CharacterReader.java:388 | 0.076696 | `bufPos += seq.length();` |
| 5 | 3 | CharacterReader.java:389 | 0.076696 | `return true;` |
| 8 | 7 | CharacterReader.java:327 | 0.071611 | `bufferUp();` |
| 8 | 7 | CharacterReader.java:328 | 0.071611 | `int scanLength = seq.length();` |
| 8 | 7 | CharacterReader.java:329 | 0.071611 | `if (scanLength > bufLength - bufPos)` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 27 | CharacterReader.java:28 | 0.0 | `private final String[] stringCache = new String[512]; // holds reused strings in this doc, to lessen garbage` |
| 1 | 27 | CharacterReader.java:30 | 0.0 | `public CharacterReader(Reader input, int sz) {` |
| 1 | 27 | CharacterReader.java:33 | 0.0 | `reader = input;` |
| 1 | 27 | CharacterReader.java:34 | 0.0 | `charBuf = new char[sz > maxBufferLen ? maxBufferLen : sz];` |
| 1 | 27 | CharacterReader.java:35 | 0.0 | `bufferUp();` |
| 1 | 27 | CharacterReader.java:43 | 0.0 | `this(new StringReader(input), input.length());` |
| 1 | 27 | CharacterReader.java:47 | 0.0 | `if (bufPos < bufSplitPoint)` |
| 1 | 27 | CharacterReader.java:51 | 0.0 | `readerPos += bufPos;` |
| 1 | 27 | CharacterReader.java:54 | 0.0 | `bufLength = reader.read(charBuf);` |
| 1 | 27 | CharacterReader.java:55 | 0.0 | `reader.reset();` |

