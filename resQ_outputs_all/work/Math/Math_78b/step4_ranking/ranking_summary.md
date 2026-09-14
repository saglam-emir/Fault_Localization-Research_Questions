# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('EventState.java', 191), ('EventState.java', 198), ('EventState.java', 199)]

Statement-line-normalized for matching (multi-line statement, first-line attribution - see ground_truth.normalize_statement_line): [('EventState.java', 191, '->', 188), ('EventState.java', 198, '->', 188), ('EventState.java', 199, '->', 188)]

Ground_Truth_Answerable: True

- SBFL   ranked 2184 statement(s)
- Hybrid ranked 104 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 12 | BrentSolver.java:170 | 1.0 | `if (Math.abs(yMin) <= functionValueAccuracy) {` |
| 1 | 12 | BrentSolver.java:173 | 1.0 | `} else if (Math.abs(yMax) <= functionValueAccuracy) {` |
| 1 | 12 | BrentSolver.java:178 | 1.0 | `throw MathRuntimeException.createIllegalArgumentException(` |
| 1 | 12 | BrentSolver.java:282 | 1.0 | `delta = 0.5 * dx;` |
| 1 | 12 | BrentSolver.java:283 | 1.0 | `oldDelta = delta;` |
| 1 | 12 | MathRuntimeException.java:37 | 1.0 | `public class MathRuntimeException extends RuntimeException {` |
| 1 | 12 | MathRuntimeException.java:102 | 1.0 | `ResourceBundle bundle =` |
| 1 | 12 | MathRuntimeException.java:109 | 1.0 | `} catch (MissingResourceException mre) {` |
| 1 | 12 | MathRuntimeException.java:115 | 1.0 | `return s;` |
| 1 | 12 | MathRuntimeException.java:128 | 1.0 | `return (pattern == null) ? "" : new MessageFormat(translate(pattern, locale), locale).format(arguments);` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 7 | EventState.java:271 | 1.0 | `return pendingEventTime;` |
| 1 | 7 | EventState.java:285 | 1.0 | `t0 = t;` |
| 1 | 7 | EventState.java:286 | 1.0 | `g0 = handler.g(t, y);` |
| 1 | 7 | EventState.java:288 | 1.0 | `if (pendingEvent) {` |
| 1 | 7 | EventState.java:290 | 1.0 | `previousEventTime = t;` |
| 1 | 7 | EventState.java:291 | 1.0 | `g0Positive        = increasing;` |
| 1 | 7 | EventState.java:292 | 1.0 | `nextAction        = handler.eventOccurred(t, y, !(increasing ^ forward));` |
| 8 | 97 | AbstractStepInterpolator.java:119 | 0.57735 | `this.forward      = forward;` |
| 8 | 97 | AbstractStepInterpolator.java:219 | 0.57735 | `currentTime = t;` |
| 8 | 97 | AbstractStepInterpolator.java:235 | 0.57735 | `return currentTime;` |

