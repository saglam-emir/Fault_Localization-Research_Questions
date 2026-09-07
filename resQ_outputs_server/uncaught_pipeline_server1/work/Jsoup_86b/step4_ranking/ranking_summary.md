# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('Comment.java', 78)]

Ground_Truth_Answerable: True

- SBFL   ranked 4256 statement(s)
- Hybrid ranked 691 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 3 | TokeniserState.java:115 | 0.447214 | `t.error(this);` |
| 1 | 3 | TokeniserState.java:116 | 0.447214 | `t.emit('<'); // char that got us here` |
| 1 | 3 | TokeniserState.java:117 | 0.447214 | `t.transition(Data);` |
| 4 | 2 | Comment.java:79 | 0.2 | `Element el = doc.child(0);` |
| 4 | 2 | XmlTreeBuilder.java:95 | 0.2 | `XmlDeclaration decl = comment.asXmlDeclaration(); // else, we couldn't parse it as a decl, so leave as a comment` |
| 6 | 12 | Comment.java:66 | 0.182574 | `String data = getData();` |
| 6 | 12 | Comment.java:67 | 0.182574 | `return (data.length() > 1 && (data.startsWith("!") || data.startsWith("?")));` |
| 6 | 12 | Comment.java:75 | 0.182574 | `String data = getData();` |
| 6 | 12 | Comment.java:76 | 0.182574 | `Document doc = Jsoup.parse("<" + data.substring(1, data.length() -1) + ">", baseUri(), Parser.xmlParser());` |
| 6 | 12 | Comment.java:77 | 0.182574 | `XmlDeclaration decl = null;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | ParseErrorList.java:15 | 0.57735 | `super(initialCapacity);` |
| 1 | 12 | ParseErrorList.java:16 | 0.57735 | `this.maxSize = maxSize;` |
| 1 | 12 | ParseErrorList.java:28 | 0.57735 | `return new ParseErrorList(0, 0);` |
| 1 | 12 | ParseSettings.java:22 | 0.57735 | `preserveCase = new ParseSettings(true, true);` |
| 1 | 12 | ParseSettings.java:33 | 0.57735 | `public ParseSettings(boolean tag, boolean attribute) {` |
| 1 | 12 | ParseSettings.java:35 | 0.57735 | `preserveAttributeCase = attribute;` |
| 1 | 12 | Parser.java:24 | 0.57735 | `public Parser(TreeBuilder treeBuilder) {` |
| 1 | 12 | Parser.java:26 | 0.57735 | `settings = treeBuilder.defaultSettings();` |
| 1 | 12 | Parser.java:27 | 0.57735 | `errors = ParseErrorList.noTracking();` |
| 1 | 12 | Parser.java:216 | 0.57735 | `return new Parser(new XmlTreeBuilder());` |

