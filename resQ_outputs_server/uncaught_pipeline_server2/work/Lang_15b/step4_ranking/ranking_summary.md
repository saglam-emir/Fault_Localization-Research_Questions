# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('TypeUtils.java', 219), ('TypeUtils.java', 220), ('TypeUtils.java', 221), ('TypeUtils.java', 675)]

Ground_Truth_Answerable: True

- SBFL   ranked 470 statement(s)
- Hybrid ranked 124 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | TypeUtils.java:612 | 1.0 | `ParameterizedType parameterizedOwnerType = (ParameterizedType) ownerType;` |
| 1 | 3 | TypeUtils.java:613 | 1.0 | `typeVarAssigns = getTypeArguments(parameterizedOwnerType,` |
| 1 | 3 | TypeUtils.java:615 | 1.0 | `} else {` |
| 4 | 1 | TypeUtils.java:676 | 0.816497 | `return typeVarAssigns;` |
| 5 | 173 | AggregateTranslator.java:40 | 0.707107 | `public AggregateTranslator(CharSequenceTranslator... translators) {` |
| 5 | 173 | AggregateTranslator.java:41 | 0.707107 | `this.translators = ArrayUtils.clone(translators);` |
| 5 | 173 | AggregateTranslator.java:51 | 0.707107 | `for (CharSequenceTranslator translator : translators) {` |
| 5 | 173 | AggregateTranslator.java:52 | 0.707107 | `int consumed = translator.translate(input, index, out);` |
| 5 | 173 | AggregateTranslator.java:53 | 0.707107 | `if(consumed != 0) {` |
| 5 | 173 | AggregateTranslator.java:54 | 0.707107 | `return consumed;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | TypeUtils.java:671 | 0.5 | `HashMap<TypeVariable<?>, Type> typeVarAssigns = subtypeVarAssigns == null ? new HashMap<TypeVariable<?>, Type>()` |
| 1 | 2 | TypeUtils.java:676 | 0.5 | `return typeVarAssigns;` |
| 3 | 18 | ClassUtils.java:589 | 0.316228 | `return isAssignable(cls, toClass, SystemUtils.isJavaVersionAtLeast(JavaVersion.JAVA_1_5));` |
| 3 | 18 | ClassUtils.java:620 | 0.316228 | `if (toClass == null) {` |
| 3 | 18 | ClassUtils.java:624 | 0.316228 | `if (cls == null) {` |
| 3 | 18 | ClassUtils.java:628 | 0.316228 | `if (autoboxing) {` |
| 3 | 18 | ClassUtils.java:629 | 0.316228 | `if (cls.isPrimitive() && !toClass.isPrimitive()) {` |
| 3 | 18 | ClassUtils.java:635 | 0.316228 | `if (toClass.isPrimitive() && !cls.isPrimitive()) {` |
| 3 | 18 | ClassUtils.java:642 | 0.316228 | `if (cls.equals(toClass)) {` |
| 3 | 18 | ClassUtils.java:645 | 0.316228 | `if (cls.isPrimitive()) {` |

