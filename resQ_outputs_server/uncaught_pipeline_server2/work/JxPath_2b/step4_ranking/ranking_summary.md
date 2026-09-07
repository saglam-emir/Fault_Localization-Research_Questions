# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Expression.java', 19), ('Expression.java', 77), ('Expression.java', 88), ('Expression.java', 145)]

Ground_Truth_Answerable: True
Unanswerable fault line(s) (dead code in the buggy build - see ground_truth_answerability.csv): [('src/java/org/apache/commons/jxpath/ri/compiler/Expression.java', 19)]

- SBFL   ranked 5484 statement(s)
- Hybrid ranked 77 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 17 | BasicNodeSet.java:76 | 1.0 | `return pointers.toString();` |
| 1 | 17 | NodePointer.java:511 | 1.0 | `NodePointer valuePointer = getValuePointer();` |
| 1 | 17 | NodePointer.java:512 | 1.0 | `if (valuePointer != null && valuePointer != this) {` |
| 1 | 17 | NodePointer.java:513 | 1.0 | `return valuePointer.childIterator(test, reverse, startWith);` |
| 1 | 17 | NodeSetContext.java:30 | 1.0 | `private boolean startedSet = false;` |
| 1 | 17 | NodeSetContext.java:34 | 1.0 | `super(parentContext);` |
| 1 | 17 | NodeSetContext.java:35 | 1.0 | `this.nodeSet = nodeSet;` |
| 1 | 17 | NodeSetContext.java:43 | 1.0 | `if (position == 0) {` |
| 1 | 17 | NodeSetContext.java:48 | 1.0 | `return (NodePointer) nodeSet.getPointers().get(position - 1);` |
| 1 | 17 | NodeSetContext.java:52 | 1.0 | `super.setPosition(position);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 77 | BeanPointer.java:46 | 1.0 | `super(null, locale);` |
| 1 | 77 | BeanPointer.java:47 | 1.0 | `this.name = name;` |
| 1 | 77 | BeanPointer.java:48 | 1.0 | `this.bean = bean;` |
| 1 | 77 | BeanPointer.java:49 | 1.0 | `this.beanInfo = beanInfo;` |
| 1 | 77 | BeanPointerFactory.java:33 | 1.0 | `public class BeanPointerFactory implements NodePointerFactory {` |
| 1 | 77 | BeanPointerFactory.java:46 | 1.0 | `JXPathBeanInfo bi = JXPathIntrospector.getBeanInfo(bean.getClass());` |
| 1 | 77 | BeanPointerFactory.java:47 | 1.0 | `return new BeanPointer(name, bean, bi, locale);` |
| 1 | 77 | CollectionPointerFactory.java:32 | 1.0 | `public class CollectionPointerFactory implements NodePointerFactory {` |
| 1 | 77 | ContainerPointerFactory.java:32 | 1.0 | `public class ContainerPointerFactory implements NodePointerFactory {` |
| 1 | 77 | DynamicPointerFactory.java:36 | 1.0 | `public class DynamicPointerFactory implements NodePointerFactory {` |

