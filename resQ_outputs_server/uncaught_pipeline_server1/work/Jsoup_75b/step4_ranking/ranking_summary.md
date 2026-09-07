# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Attributes.java', 319), ('Attributes.java', 320)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('Attributes.java', 320, '->', 319)]

Ground_Truth_Answerable: True

- SBFL   ranked 4170 statement(s)
- Hybrid ranked 329 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | Attribute.java:179 | 0.447214 | `return Arrays.binarySearch(booleanAttributes, key) >= 0;` |
| 1 | 2 | TokeniserState.java:770 | 0.447214 | `t.tagPending.setEmptyAttributeValue();` |
| 3 | 19 | Collector.java:56 | 0.258199 | `FirstFinder finder = new FirstFinder(root, eval);` |
| 3 | 19 | Collector.java:57 | 0.258199 | `NodeTraversor.filter(finder, root);` |
| 3 | 19 | Collector.java:58 | 0.258199 | `return finder.match;` |
| 3 | 19 | Collector.java:61 | 0.258199 | `private static class FirstFinder implements NodeFilter {` |
| 3 | 19 | Collector.java:63 | 0.258199 | `private Element match = null;` |
| 3 | 19 | Collector.java:66 | 0.258199 | `FirstFinder(Element root, Evaluator eval) {` |
| 3 | 19 | Collector.java:67 | 0.258199 | `this.root = root;` |
| 3 | 19 | Collector.java:68 | 0.258199 | `this.eval = eval;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 329 | Attributes.java:32 | 1.0 | `public class Attributes implements Iterable<Attribute>, Cloneable {` |
| 1 | 329 | Attributes.java:38 | 1.0 | `private static final String[] Empty = {};` |
| 1 | 329 | Attributes.java:42 | 1.0 | `private int size = 0; // number of slots used (not capacity, which is keys.length` |
| 1 | 329 | Attributes.java:43 | 1.0 | `String[] keys = Empty;` |
| 1 | 329 | Attributes.java:44 | 1.0 | `String[] vals = Empty;` |
| 1 | 329 | ChangeNotifyingArrayList.java:11 | 1.0 | `super(initialCapacity);` |
| 1 | 329 | CharacterReader.java:28 | 1.0 | `private final String[] stringCache = new String[512]; // holds reused strings in this doc, to lessen garbage` |
| 1 | 329 | CharacterReader.java:33 | 1.0 | `reader = input;` |
| 1 | 329 | CharacterReader.java:34 | 1.0 | `charBuf = new char[sz > maxBufferLen ? maxBufferLen : sz];` |
| 1 | 329 | CharacterReader.java:35 | 1.0 | `bufferUp();` |

