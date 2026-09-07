# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('MultiValueMap.java', 568)]

Ground_Truth_Answerable: False
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/collections4/map/MultiValueMap.java', 568)]

> **WARNING**: every ground-truth fault line for this bug is an approximate pure-deletion anchor that never executed in any test (dead code in the buggy build, not a wrong-but-live statement - typically an entire deleted method). No line-level SBFL or slicing technique can find this by construction. The rank_best values in rq5.csv for this bug are not a meaningful measure of either technique's capability and should be excluded from primary cross-bug scoring (see rq0_answerability.csv).

- SBFL   ranked 481 statement(s)
- Hybrid ranked 9 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | MultiValueMap.java:163 | 0.707107 | `out.defaultWriteObject();` |
| 1 | 2 | MultiValueMap.java:164 | 0.707107 | `out.writeObject(map);` |
| 3 | 5 | AbstractMapDecorator.java:51 | 0.408248 | `super();` |
| 3 | 5 | AbstractMapDecorator.java:127 | 0.408248 | `if (object == this) {` |
| 3 | 5 | AbstractMapDecorator.java:130 | 0.408248 | `return decorated().equals(object);` |
| 3 | 5 | MultiValueMap.java:177 | 0.408248 | `in.defaultReadObject();` |
| 3 | 5 | MultiValueMap.java:178 | 0.408248 | `map = (Map<K, Object>) in.readObject(); // (1)` |
| 8 | 1 | AbstractMapDecorator.java:118 | 0.196116 | `return decorated().size();` |
| 9 | 1 | MultiValueMap.java:106 | 0.158114 | `return new MultiValueMap<K, V>(map, new ReflectionFactory<C>(collectionClass));` |
| 10 | 5 | MultiValueMap.java:147 | 0.123091 | `super((Map<K, Object>) map);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 9 | AbstractIterableMap.java:28 | 0.0 | `public abstract class AbstractIterableMap<K, V> implements IterableMap<K, V> {` |
| 1 | 9 | AbstractMapDecorator.java:51 | 0.0 | `super();` |
| 1 | 9 | AbstractMapDecorator.java:60 | 0.0 | `protected AbstractMapDecorator(final Map<K, V> map) {` |
| 1 | 9 | AbstractMapDecorator.java:64 | 0.0 | `this.map = map;` |
| 1 | 9 | MultiValueMap.java:106 | 0.0 | `return new MultiValueMap<K, V>(map, new ReflectionFactory<C>(collectionClass));` |
| 1 | 9 | MultiValueMap.java:147 | 0.0 | `super((Map<K, Object>) map);` |
| 1 | 9 | MultiValueMap.java:151 | 0.0 | `this.collectionFactory = collectionFactory;` |
| 1 | 9 | MultiValueMap.java:555 | 0.0 | `public ReflectionFactory(final Class<T> clazz) {` |
| 1 | 9 | MultiValueMap.java:556 | 0.0 | `this.clazz = clazz;` |

