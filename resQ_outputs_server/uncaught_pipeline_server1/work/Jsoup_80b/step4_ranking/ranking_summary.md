# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('XmlTreeBuilder.java', 91), ('XmlTreeBuilder.java', 94)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('XmlTreeBuilder.java', 94, '->', 89)]

Ground_Truth_Answerable: True

- SBFL   ranked 4154 statement(s)
- Hybrid ranked 500 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | TokeniserState.java:789 | 0.447214 | `t.eofError(this);` |
| 1 | 3 | TokeniserState.java:790 | 0.447214 | `t.transition(Data);` |
| 1 | 3 | TokeniserState.java:791 | 0.447214 | `break;` |
| 4 | 4 | XmlTreeBuilder.java:88 | 0.223607 | `String data = comment.getData();` |
| 4 | 4 | XmlTreeBuilder.java:89 | 0.223607 | `if (data.length() > 1 && (data.startsWith("!") || data.startsWith("?"))) {` |
| 4 | 4 | XmlTreeBuilder.java:90 | 0.223607 | `Document doc = Jsoup.parse("<" + data.substring(1, data.length() -1) + ">", baseUri, Parser.xmlParser());` |
| 4 | 4 | XmlTreeBuilder.java:91 | 0.223607 | `Element el = doc.child(0);` |
| 8 | 5 | Tokeniser.java:233 | 0.2 | `if (errors.canAddError())` |
| 8 | 5 | XmlTreeBuilder.java:49 | 0.2 | `insert(token.asComment());` |
| 8 | 5 | XmlTreeBuilder.java:84 | 0.2 | `Comment comment = new Comment(commentToken.getData());` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 4 | ParseSettings.java:22 | 0.707107 | `preserveCase = new ParseSettings(true, true);` |
| 1 | 4 | Parser.java:214 | 0.707107 | `return new Parser(new XmlTreeBuilder());` |
| 1 | 4 | XmlTreeBuilder.java:18 | 0.707107 | `public class XmlTreeBuilder extends TreeBuilder {` |
| 1 | 4 | XmlTreeBuilder.java:20 | 0.707107 | `return ParseSettings.preserveCase;` |
| 5 | 6 | ParseSettings.java:33 | 0.447214 | `public ParseSettings(boolean tag, boolean attribute) {` |
| 5 | 6 | ParseSettings.java:35 | 0.447214 | `preserveAttributeCase = attribute;` |
| 5 | 6 | Parser.java:19 | 0.447214 | `private int maxErrors = DEFAULT_MAX_ERRORS;` |
| 5 | 6 | Parser.java:27 | 0.447214 | `public Parser(TreeBuilder treeBuilder) {` |
| 5 | 6 | Parser.java:28 | 0.447214 | `this.treeBuilder = treeBuilder;` |
| 5 | 6 | Parser.java:29 | 0.447214 | `settings = treeBuilder.defaultSettings();` |

