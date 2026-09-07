# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('NodePointer.java', 665), ('NodePointer.java', 666), ('NodePointer.java', 667)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('NodePointer.java', 666, '->', 665), ('NodePointer.java', 667, '->', 665)]

Ground_Truth_Answerable: True

- SBFL   ranked 5447 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 35 | CoreOperationUnion.java:35 | 1.0 | `EvalContext argCtxs[] = new EvalContext[args.length];` |
| 1 | 35 | CoreOperationUnion.java:36 | 1.0 | `for (int i = 0; i < args.length; i++) {` |
| 1 | 35 | CoreOperationUnion.java:37 | 1.0 | `Object value = args[i].compute(context);` |
| 1 | 35 | CoreOperationUnion.java:38 | 1.0 | `if (value instanceof EvalContext) {` |
| 1 | 35 | CoreOperationUnion.java:39 | 1.0 | `argCtxs[i] = (EvalContext) value;` |
| 1 | 35 | CoreOperationUnion.java:45 | 1.0 | `return new UnionContext(context.getRootContext(), argCtxs);` |
| 1 | 35 | DOMNodePointer.java:68 | 1.0 | `super(null, locale);` |
| 1 | 35 | DOMNodePointer.java:69 | 1.0 | `this.node = node;` |
| 1 | 35 | DOMNodePointer.java:574 | 1.0 | `return System.identityHashCode(node);` |
| 1 | 35 | DOMNodePointer.java:578 | 1.0 | `return object == this || object instanceof DOMNodePointer && node == ((DOMNodePointer) object).node;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | CoreOperation.java:35 | 1.0 | `return computeValue(context);` |
| 1 | 7 | Expression.java:85 | 1.0 | `Object result = compute(context);` |
| 1 | 7 | Expression.java:86 | 1.0 | `if (result == null) {` |
| 1 | 7 | Expression.java:89 | 1.0 | `if (result instanceof EvalContext) {` |
| 1 | 7 | Expression.java:90 | 1.0 | `return (EvalContext) result;` |
| 1 | 7 | JXPathContextReferenceImpl.java:540 | 1.0 | `return iteratePointers(xpath, compileExpression(xpath));` |
| 1 | 7 | JXPathContextReferenceImpl.java:544 | 1.0 | `return expr.iteratePointers(getEvalContext());` |

