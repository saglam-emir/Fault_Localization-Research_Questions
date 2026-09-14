# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('BaseSecantSolver.java', 185), ('BaseSecantSolver.java', 187), ('BaseSecantSolver.java', 189)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('BaseSecantSolver.java', 185, '->', 178), ('BaseSecantSolver.java', 187, '->', 178), ('BaseSecantSolver.java', 189, '->', 178)]

Ground_Truth_Answerable: True

- SBFL   ranked 1406 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 354 | ArgUtils.java:42 | 0.707107 | `final List<Object> list = new ArrayList<Object>();` |
| 1 | 354 | ArgUtils.java:43 | 0.707107 | `if (array != null) {` |
| 1 | 354 | ArgUtils.java:44 | 0.707107 | `for (Object o : array) {` |
| 1 | 354 | ArgUtils.java:45 | 0.707107 | `if (o instanceof Object[]) {` |
| 1 | 354 | ArgUtils.java:46 | 0.707107 | `for (Object oR : flatten((Object[]) o)) {` |
| 1 | 354 | ArgUtils.java:50 | 0.707107 | `list.add(o);` |
| 1 | 354 | ArgUtils.java:54 | 0.707107 | `return list.toArray();` |
| 1 | 354 | BaseAbstractUnivariateRealSolver.java:295 | 0.707107 | `} catch (MaxCountExceededException e) {` |
| 1 | 354 | BaseAbstractUnivariateRealSolver.java:296 | 0.707107 | `throw new TooManyEvaluationsException(e.getMax());` |
| 1 | 354 | BaseSecantSolver.java:68 | 0.707107 | `super(absoluteAccuracy);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

