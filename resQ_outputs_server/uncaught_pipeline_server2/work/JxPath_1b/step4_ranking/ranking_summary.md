# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('DOMNodePointer.java', 116), ('JDOMNodePointer.java', 376)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('DOMNodePointer.java', 116, '->', 115), ('JDOMNodePointer.java', 376, '->', 375)]

Ground_Truth_Answerable: True

- SBFL   ranked 5470 statement(s)
- Hybrid ranked 75 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 26 | AttributeContext.java:34 | 1.0 | `private boolean setStarted = false;` |
| 1 | 26 | AttributeContext.java:43 | 1.0 | `super(parentContext);` |
| 1 | 26 | AttributeContext.java:44 | 1.0 | `this.nodeTest = nodeTest;` |
| 1 | 26 | AttributeContext.java:48 | 1.0 | `return currentNodePointer;` |
| 1 | 26 | AttributeContext.java:52 | 1.0 | `setStarted = false;` |
| 1 | 26 | AttributeContext.java:53 | 1.0 | `iterator = null;` |
| 1 | 26 | AttributeContext.java:54 | 1.0 | `super.reset();` |
| 1 | 26 | AttributeContext.java:71 | 1.0 | `super.setPosition(getCurrentPosition() + 1);` |
| 1 | 26 | AttributeContext.java:72 | 1.0 | `if (!setStarted) {` |
| 1 | 26 | AttributeContext.java:73 | 1.0 | `setStarted = true;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 75 | AbstractFactory.java:32 | 1.0 | `public abstract class AbstractFactory {` |
| 1 | 75 | BeanPointerFactory.java:33 | 1.0 | `public class BeanPointerFactory implements NodePointerFactory {` |
| 1 | 75 | CollectionPointerFactory.java:32 | 1.0 | `public class CollectionPointerFactory implements NodePointerFactory {` |
| 1 | 75 | ContainerPointer.java:41 | 1.0 | `super(null, locale);` |
| 1 | 75 | ContainerPointer.java:42 | 1.0 | `this.container = container;` |
| 1 | 75 | ContainerPointerFactory.java:32 | 1.0 | `public class ContainerPointerFactory implements NodePointerFactory {` |
| 1 | 75 | ContainerPointerFactory.java:45 | 1.0 | `if (bean instanceof Container) {` |
| 1 | 75 | ContainerPointerFactory.java:46 | 1.0 | `return new ContainerPointer((Container) bean, locale);` |
| 1 | 75 | DocumentContainer.java:92 | 1.0 | `public DocumentContainer(URL xmlURL, String model) {` |
| 1 | 75 | DocumentContainer.java:93 | 1.0 | `this.xmlURL = xmlURL;` |

