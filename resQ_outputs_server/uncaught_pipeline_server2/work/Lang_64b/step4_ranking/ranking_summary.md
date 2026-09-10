# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ValuedEnum.java', 183), ('ValuedEnum.java', 192), ('ValuedEnum.java', 193), ('ValuedEnum.java', 194), ('ValuedEnum.java', 195)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/lang/enums/ValuedEnum.java', 192), ('src/java/org/apache/commons/lang/enums/ValuedEnum.java', 193), ('src/java/org/apache/commons/lang/enums/ValuedEnum.java', 194), ('src/java/org/apache/commons/lang/enums/ValuedEnum.java', 195)]

- SBFL   ranked 161 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ValuedEnum.java:183 | 0.447214 | `return iValue - ((ValuedEnum) other).iValue;` |
| 2 | 2 | ValuedEnum.java:126 | 0.223607 | `super(name);` |
| 2 | 2 | ValuedEnum.java:127 | 0.223607 | `iValue = value;` |
| 4 | 1 | Enum.java:519 | 0.131306 | `return getClass();` |
| 5 | 20 | Enum.java:279 | 0.125 | `final Map map = new HashMap();` |
| 5 | 20 | Enum.java:283 | 0.125 | `final Map unmodifiableMap = Collections.unmodifiableMap(map);` |
| 5 | 20 | Enum.java:287 | 0.125 | `final List list = new ArrayList(25);` |
| 5 | 20 | Enum.java:291 | 0.125 | `final List unmodifiableList = Collections.unmodifiableList(list);` |
| 5 | 20 | Enum.java:297 | 0.125 | `super();` |
| 5 | 20 | Enum.java:314 | 0.125 | `iName = name;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

