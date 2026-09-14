# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EigenDecompositionImpl.java', 1135)]

Ground_Truth_Answerable: True

- SBFL   ranked 1474 statement(s)
- Hybrid ranked 5 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 31 | EigenDecompositionImpl.java:871 | 1.0 | `i0 = 1 + i / 4;` |
| 1 | 31 | EigenDecompositionImpl.java:872 | 1.0 | `break;` |
| 1 | 31 | EigenDecompositionImpl.java:944 | 1.0 | `work[i + 2] = -0.0;` |
| 1 | 31 | EigenDecompositionImpl.java:945 | 1.0 | `d = work[i];` |
| 1 | 31 | EigenDecompositionImpl.java:957 | 1.0 | `work[i]     = -0.0;` |
| 1 | 31 | EigenDecompositionImpl.java:958 | 1.0 | `work[j]     = d;` |
| 1 | 31 | EigenDecompositionImpl.java:959 | 1.0 | `work[j + 2] = 0.0;` |
| 1 | 31 | EigenDecompositionImpl.java:960 | 1.0 | `d = work[i + 2];` |
| 1 | 31 | EigenDecompositionImpl.java:1055 | 1.0 | `dMin2 = Math.min(dMin2, work[l - 1]);` |
| 1 | 31 | EigenDecompositionImpl.java:1056 | 1.0 | `work[l - 1] =` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 5 | EigenDecompositionImpl.java:193 | 0.707107 | `this.main      = main.clone();` |
| 1 | 5 | EigenDecompositionImpl.java:205 | 0.707107 | `decompose();` |
| 1 | 5 | EigenDecompositionImpl.java:246 | 0.707107 | `findEigenvalues();` |
| 1 | 5 | EigenDecompositionImpl.java:312 | 0.707107 | `return realEigenvalues.clone();` |
| 1 | 5 | EigenDecompositionImpl.java:619 | 0.707107 | `realEigenvalues = new double[main.length];` |

