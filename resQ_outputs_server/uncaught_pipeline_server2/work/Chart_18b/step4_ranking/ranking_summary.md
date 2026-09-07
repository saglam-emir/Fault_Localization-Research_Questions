# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DefaultKeyedValues.java', 318), ('DefaultKeyedValues.java', 320), ('DefaultKeyedValues.java', 335), ('DefaultKeyedValues2D.java', 455), ('DefaultKeyedValues2D.java', 458), ('DefaultKeyedValues2D.java', 459)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DefaultKeyedValues2D.java', 459, '->', 456)]

Ground_Truth_Answerable: True

- SBFL   ranked 10880 statement(s)
- Hybrid ranked 196 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 6 | DefaultKeyedValues.java:316 | 0.894427 | `this.keys.remove(index);` |
| 1 | 6 | DefaultKeyedValues.java:317 | 0.894427 | `this.values.remove(index);` |
| 1 | 6 | DefaultKeyedValues.java:318 | 0.894427 | `if (index < this.keys.size()) {` |
| 1 | 6 | DefaultKeyedValues.java:333 | 0.894427 | `int index = getIndex(key);` |
| 1 | 6 | DefaultKeyedValues.java:334 | 0.894427 | `if (index < 0) {` |
| 1 | 6 | DefaultKeyedValues.java:337 | 0.894427 | `removeValue(index);` |
| 7 | 1 | DefaultKeyedValues.java:335 | 0.774597 | `return;` |
| 8 | 5 | DefaultKeyedValues2D.java:455 | 0.632456 | `Iterator iterator = this.rows.iterator();` |
| 8 | 5 | DefaultKeyedValues2D.java:456 | 0.632456 | `while (iterator.hasNext()) {` |
| 8 | 5 | DefaultKeyedValues2D.java:457 | 0.632456 | `DefaultKeyedValues rowData = (DefaultKeyedValues) iterator.next();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | DefaultCategoryDataset.java:351 | 0.5 | `fireDatasetChanged();` |
| 2 | 1 | DefaultKeyedValues.java:333 | 0.353553 | `int index = getIndex(key);` |
| 3 | 1 | DefaultKeyedValues.java:197 | 0.204124 | `addValue(key, new Double(value));` |
| 4 | 1 | DefaultKeyedValues.java:157 | 0.188982 | `return i.intValue();` |
| 5 | 1 | DefaultCategoryDataset.java:219 | 0.176777 | `fireDatasetChanged();` |
| 6 | 1 | DefaultKeyedValues.java:209 | 0.166667 | `setValue(key, value);` |
| 7 | 2 | DefaultKeyedValues.java:238 | 0.160128 | `this.keys.add(key);` |
| 7 | 2 | DefaultKeyedValues.java:240 | 0.160128 | `this.indexMap.put(key, new Integer(this.keys.size() - 1));` |
| 9 | 2 | DefaultKeyedValues.java:232 | 0.158114 | `int keyIndex = getIndex(key);` |
| 9 | 2 | DefaultKeyedValues.java:233 | 0.158114 | `if (keyIndex >= 0) {` |

