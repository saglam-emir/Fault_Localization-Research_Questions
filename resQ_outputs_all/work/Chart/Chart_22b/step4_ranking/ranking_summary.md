# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('KeyedObjects2D.java', 231), ('KeyedObjects2D.java', 233), ('KeyedObjects2D.java', 318), ('KeyedObjects2D.java', 319), ('KeyedObjects2D.java', 320), ('KeyedObjects2D.java', 345), ('KeyedObjects2D.java', 378)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('source/org/jfree/data/KeyedObjects2D.java', 318), ('source/org/jfree/data/KeyedObjects2D.java', 319), ('source/org/jfree/data/KeyedObjects2D.java', 320)]

- SBFL   ranked 4542 statement(s)
- Hybrid ranked 63 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | UnknownKeyException.java:56 | 0.816497 | `super(message);` |
| 2 | 10 | KeyedObjects.java:171 | 0.57735 | `throw new UnknownKeyException("The key (" + key` |
| 2 | 10 | KeyedObjects.java:266 | 0.57735 | `int index = getIndex(key);` |
| 2 | 10 | KeyedObjects.java:267 | 0.57735 | `if (index < 0) {` |
| 2 | 10 | KeyedObjects.java:268 | 0.57735 | `throw new UnknownKeyException("The key (" + key.toString()` |
| 2 | 10 | KeyedObjects2D.java:370 | 0.57735 | `int index = getColumnIndex(columnKey);` |
| 2 | 10 | KeyedObjects2D.java:371 | 0.57735 | `if (index < 0) {` |
| 2 | 10 | KeyedObjects2D.java:375 | 0.57735 | `Iterator iterator = this.rows.iterator();` |
| 2 | 10 | KeyedObjects2D.java:376 | 0.57735 | `while (iterator.hasNext()) {` |
| 2 | 10 | KeyedObjects2D.java:377 | 0.57735 | `KeyedObjects rowData = (KeyedObjects) iterator.next();` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 13 | KeyedObjects.java:67 | 0.478091 | `public KeyedObjects() {` |
| 1 | 13 | KeyedObjects.java:68 | 0.478091 | `this.data = new java.util.ArrayList();` |
| 1 | 13 | KeyedObjects2D.java:74 | 0.478091 | `public KeyedObjects2D() {` |
| 1 | 13 | KeyedObjects2D.java:76 | 0.478091 | `this.columnKeys = new java.util.ArrayList();` |
| 1 | 13 | KeyedObjects2D.java:77 | 0.478091 | `this.rows = new java.util.ArrayList();` |
| 1 | 13 | KeyedObjects2D.java:269 | 0.478091 | `int rowIndex = this.rowKeys.indexOf(rowKey);` |
| 1 | 13 | KeyedObjects2D.java:270 | 0.478091 | `if (rowIndex >= 0) {` |
| 1 | 13 | KeyedObjects2D.java:274 | 0.478091 | `this.rowKeys.add(rowKey);` |
| 1 | 13 | KeyedObjects2D.java:275 | 0.478091 | `row = new KeyedObjects();` |
| 1 | 13 | KeyedObjects2D.java:276 | 0.478091 | `this.rows.add(row);` |

