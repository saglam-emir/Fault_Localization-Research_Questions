# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('HelpFormatter.java', 812)]

Ground_Truth_Answerable: True

- SBFL   ranked 477 statement(s)
- Hybrid ranked 96 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 10 | HelpFormatter.java:301 | 0.707107 | `printHelp(defaultWidth, cmdLineSyntax, null, options, null, false);` |
| 1 | 10 | HelpFormatter.java:388 | 0.707107 | `PrintWriter pw = new PrintWriter(System.out);` |
| 1 | 10 | HelpFormatter.java:390 | 0.707107 | `printHelp(pw, width, cmdLineSyntax, header, options, defaultLeftPad,` |
| 1 | 10 | HelpFormatter.java:392 | 0.707107 | `pw.flush();` |
| 1 | 10 | HelpFormatter.java:451 | 0.707107 | `printUsage(pw, width, cmdLineSyntax);` |
| 1 | 10 | HelpFormatter.java:620 | 0.707107 | `int argPos = cmdLineSyntax.indexOf(' ') + 1;` |
| 1 | 10 | HelpFormatter.java:622 | 0.707107 | `printWrapped(pw, width, defaultSyntaxPrefix.length() + argPos,` |
| 1 | 10 | HelpFormatter.java:735 | 0.707107 | `if (option.hasArgName())` |
| 1 | 10 | HelpFormatter.java:741 | 0.707107 | `optBuf.append(' ');` |
| 1 | 10 | Option.java:333 | 0.707107 | `return (this.argName != null && this.argName.length() > 0);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | HelpFormatter.java:803 | 0.267261 | `sb.append(rtrim(text.substring(0, pos))).append(defaultNewLine);` |
| 1 | 12 | HelpFormatter.java:807 | 0.267261 | `final String padding = createPadding(nextLineTabStop);` |
| 1 | 12 | HelpFormatter.java:811 | 0.267261 | `text = padding + text.substring(pos).trim();` |
| 1 | 12 | HelpFormatter.java:812 | 0.267261 | `pos = findWrapPos(text, width, nextLineTabStop);` |
| 1 | 12 | HelpFormatter.java:814 | 0.267261 | `if (pos == -1)` |
| 1 | 12 | HelpFormatter.java:816 | 0.267261 | `sb.append(text);` |
| 1 | 12 | HelpFormatter.java:855 | 0.267261 | `pos = startPos + width;` |
| 1 | 12 | HelpFormatter.java:860 | 0.267261 | `&& (c != '\n') && (c != '\r'))` |
| 1 | 12 | HelpFormatter.java:862 | 0.267261 | `--pos;` |
| 1 | 12 | HelpFormatter.java:866 | 0.267261 | `if (pos > startPos)` |

