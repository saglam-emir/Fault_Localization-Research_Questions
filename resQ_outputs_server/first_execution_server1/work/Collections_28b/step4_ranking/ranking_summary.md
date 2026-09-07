# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('AbstractPatriciaTrie.java', 2262)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/collections4/trie/AbstractPatriciaTrie.java', 2262)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 463 statement(s)
- Hybrid ranked 118 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | AbstractPatriciaTrie.java:518 | 0.408248 | `child.predecessor = parent;` |
| 1 | 17 | AbstractPatriciaTrie.java:1590 | 0.408248 | `if (current == null) {` |
| 1 | 17 | AbstractPatriciaTrie.java:1594 | 0.408248 | `if (expectedModCount != AbstractPatriciaTrie.this.modCount) {` |
| 1 | 17 | AbstractPatriciaTrie.java:1598 | 0.408248 | `final TrieEntry<K, V> node = current;` |
| 1 | 17 | AbstractPatriciaTrie.java:1599 | 0.408248 | `current = null;` |
| 1 | 17 | AbstractPatriciaTrie.java:1600 | 0.408248 | `AbstractPatriciaTrie.this.removeEntry(node);` |
| 1 | 17 | AbstractPatriciaTrie.java:1602 | 0.408248 | `expectedModCount = AbstractPatriciaTrie.this.modCount;` |
| 1 | 17 | AbstractPatriciaTrie.java:2374 | 0.408248 | `next = null;` |
| 1 | 17 | AbstractPatriciaTrie.java:2388 | 0.408248 | `boolean needsFixing = false;` |
| 1 | 17 | AbstractPatriciaTrie.java:2389 | 0.408248 | `final int bitIdx = subtree.bitIndex;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 118 | AbstractBitwiseTrie.java:89 | 0.0 | `if (key == null) {` |
| 1 | 118 | AbstractBitwiseTrie.java:93 | 0.0 | `return keyAnalyzer.lengthInBits(key);` |
| 1 | 118 | AbstractBitwiseTrie.java:111 | 0.0 | `if (key == null) { // root's might be null!` |
| 1 | 118 | AbstractBitwiseTrie.java:114 | 0.0 | `return keyAnalyzer.isBitSet(key, bitIndex, lengthInBits);` |
| 1 | 118 | AbstractBitwiseTrie.java:121 | 0.0 | `return keyAnalyzer.bitIndex(key, 0, lengthInBits(key), foundKey, 0, lengthInBits(foundKey));` |
| 1 | 118 | AbstractBitwiseTrie.java:128 | 0.0 | `if (key == null) {` |
| 1 | 118 | AbstractBitwiseTrie.java:130 | 0.0 | `} else if (other == null) {` |
| 1 | 118 | AbstractBitwiseTrie.java:134 | 0.0 | `return keyAnalyzer.compare(key, other) == 0;` |
| 1 | 118 | AbstractBitwiseTrie.java:159 | 0.0 | `public BasicEntry(final K key, final V value) {` |
| 1 | 118 | AbstractBitwiseTrie.java:160 | 0.0 | `this.key = key;` |

