# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('IteratorUtils.java', 605), ('IteratorUtils.java', 626), ('IteratorUtils.java', 648)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/main/java/org/apache/commons/collections4/IteratorUtils.java', 626), ('src/main/java/org/apache/commons/collections4/IteratorUtils.java', 648)]

- SBFL   ranked 1438 statement(s)
- Hybrid ranked 89 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | CollatingIterator.java:174 | 0.57735 | `throw new NullPointerException("Iterator must not be null");` |
| 1 | 3 | CollatingIterator.java:366 | 0.57735 | `throw new NullPointerException("You must invoke setComparator() to set a comparator first.");` |
| 1 | 3 | IteratorUtils.java:605 | 0.57735 | `return new CollatingIterator<E>(comparator, iterator1, iterator2);` |
| 4 | 49 | CollatingIterator.java:44 | 0.333333 | `private Comparator<? super E> comparator = null;` |
| 4 | 49 | CollatingIterator.java:47 | 0.333333 | `private List<Iterator<? extends E>> iterators = null;` |
| 4 | 49 | CollatingIterator.java:50 | 0.333333 | `private List<E> values = null;` |
| 4 | 49 | CollatingIterator.java:53 | 0.333333 | `private BitSet valueSet = null;` |
| 4 | 49 | CollatingIterator.java:59 | 0.333333 | `private int lastReturned = -1;` |
| 4 | 49 | CollatingIterator.java:99 | 0.333333 | `public CollatingIterator(final Comparator<? super E> comp, final int initIterCapacity) {` |
| 4 | 49 | CollatingIterator.java:100 | 0.333333 | `iterators = new ArrayList<Iterator<? extends E>>(initIterCapacity);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 16 | CollatingIterator.java:44 | 1.0 | `private Comparator<? super E> comparator = null;` |
| 1 | 16 | CollatingIterator.java:47 | 1.0 | `private List<Iterator<? extends E>> iterators = null;` |
| 1 | 16 | CollatingIterator.java:50 | 1.0 | `private List<E> values = null;` |
| 1 | 16 | CollatingIterator.java:53 | 1.0 | `private BitSet valueSet = null;` |
| 1 | 16 | CollatingIterator.java:59 | 1.0 | `private int lastReturned = -1;` |
| 1 | 16 | CollatingIterator.java:99 | 1.0 | `public CollatingIterator(final Comparator<? super E> comp, final int initIterCapacity) {` |
| 1 | 16 | CollatingIterator.java:100 | 1.0 | `iterators = new ArrayList<Iterator<? extends E>>(initIterCapacity);` |
| 1 | 16 | CollatingIterator.java:101 | 1.0 | `setComparator(comp);` |
| 1 | 16 | CollatingIterator.java:118 | 1.0 | `this(comp, 2);` |
| 1 | 16 | CollatingIterator.java:119 | 1.0 | `addIterator(a);` |

