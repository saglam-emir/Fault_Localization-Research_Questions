"""
java_ast.py
============
Static helpers for locating JUnit assertion calls inside a test method's
source and reducing each assertion's checked expression down to the single
local variable Slicer4J can slice on.

No AST library (javalang / JavaParser) is available in this environment, so
this uses brace-matching + regex: reliable enough for JUnit 3/4-style test
methods with single- or multi-line `assertX(...)` calls.

Used by both halves of the assertion-level hybrid approach:
  - Target_Pool construction: failing tests, assertions truncated at the
    line that actually threw (pass `max_line`).
  - Selective slicing on passing tests: full method (no `max_line`).
"""

import re
from pathlib import Path

ASSERTION_TYPES = [
    "assertEquals", "assertTrue", "assertFalse", "assertNull",
    "assertNotNull", "assertArrayEquals", "assertSame", "assertNotSame",
    "assertNotEquals", "assertThat",
]

ASSERT_CALL_RE = re.compile(r"\b(" + "|".join(ASSERTION_TYPES) + r")\s*\((.*?)\)\s*;", re.DOTALL)

METHOD_START_RE = re.compile(r"(?:public|protected)\s+void\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")

# Leftmost simple identifier of a (possibly chained) Java expression, e.g.
#   "result.records.get(1).fields.size()" -> "result"
#   "!list.isEmpty()"                     -> "list"
#   "\"b\""                               -> "" (string literal, no variable)
ROOT_VARIABLE_RE = re.compile(r'^[!(\s]*([A-Za-z_$][A-Za-z0-9_$]*)')


def split_args(arg_str: str):
    """Split assertion arguments on top-level commas (ignoring commas inside
    nested parens/strings).
    """
    args, depth, buf = [], 0, ""
    in_string = False
    for ch in arg_str:
        if ch == '"' and not in_string:
            in_string = True
        elif ch == '"' and in_string:
            in_string = False
        if ch == "," and depth == 0 and not in_string:
            args.append(buf.strip())
            buf = ""
            continue
        if ch in "([" and not in_string:
            depth += 1
        elif ch in ")]" and not in_string:
            depth -= 1
        buf += ch
    if buf.strip():
        args.append(buf.strip())
    return args


def extract_method_body_lines(all_lines, method_name):
    """0-based inclusive (start, end) line range for the first method named
    `method_name`, found via brace matching. None if not found.
    """
    for i, line in enumerate(all_lines):
        m = METHOD_START_RE.search(line)
        if m and m.group(1) == method_name:
            depth, started = 0, False
            for j in range(i, len(all_lines)):
                depth += all_lines[j].count("{") - all_lines[j].count("}")
                if "{" in all_lines[j]:
                    started = True
                if started and depth == 0:
                    return i, j
            return i, len(all_lines) - 1
    return None


def assertion_output_expr(assert_type: str, raw_args):
    """The sub-expression whose runtime value an assertion actually checks,
    e.g. for `assertEquals(expected, actual)` this is `actual`.
    """
    if assert_type in ("assertEquals", "assertNotEquals") and len(raw_args) >= 2:
        return raw_args[1]
    if assert_type in ("assertTrue", "assertFalse", "assertNull", "assertNotNull"):
        return raw_args[0] if raw_args else ""
    if assert_type in ("assertArrayEquals", "assertSame", "assertNotSame") and len(raw_args) >= 2:
        return raw_args[1]
    if assert_type == "assertThat":
        # Hamcrest: assertThat(actual, matcher) or assertThat(reason, actual, matcher).
        if len(raw_args) >= 3:
            return raw_args[1]
        return raw_args[0] if raw_args else ""
    return raw_args[0] if raw_args else ""


def root_variable(expr: str) -> str:
    """Leftmost simple identifier of `expr` - the local variable whose
    dataflow Slicer4J slices backward from. "" if `expr` is a literal.
    """
    m = ROOT_VARIABLE_RE.match(expr.strip())
    return m.group(1) if m else ""


# Matches a local variable declaration/assignment statement, e.g.
#   "String xml = MAPPER.writeValueAsString(...)"  -> "xml"
#   "List<String> out = compute();"                 -> "out"
# capturing the LHS identifier being assigned, not the type token(s) before
# it (unlike ROOT_VARIABLE_RE, which would match the type name here).
_DECL_OR_ASSIGN_RE = re.compile(
    r"^\s*(?:[A-Za-z_$][\w$]*(?:<[^;=]*?>)?(?:\[\])?\s+)*([A-Za-z_$][\w$]*)\s*=[^=]"
)


def synthetic_exception_criterion(src_file: Path, method_name: str, fail_line: int):
    """Fallback pool-criterion for a failing test whose OWN stack-trace line
    is not an assertX(...) call - i.e. the bug throws an exception from
    application code before any assertion is ever reached (no @Test(expected
    = ...), no custom assert library, no try/catch/fail: those all still end
    up on an assertX(...)-bearing line or a line assertion-based parsing
    already handles; a bare exception has no assertion anywhere in its
    causal path by construction).

    Reduces the statement at `fail_line` itself to a slicing variable using
    the same "what does the assignment target, or the statement's leftmost
    identifier" heuristic assertion_output_expr/root_variable use for a real
    assertion's checked expression, so Step 2 still has a real (variable,
    line) pair to seed a backward slice from instead of skipping the test
    entirely. Returns None if `fail_line` cannot be resolved to a usable
    variable (e.g. a bare call with no assignment and no leading
    identifier, or fail_line falls outside the method's own body).
    """
    if not src_file.exists():
        return None
    all_lines = src_file.read_text(encoding="utf-8", errors="replace").splitlines()
    bounds = extract_method_body_lines(all_lines, method_name)
    if not bounds or not (1 <= fail_line <= len(all_lines)):
        return None
    start, end = bounds
    if not (start + 1 <= fail_line <= end + 1):
        return None  # fail_line reported by the stack trace isn't inside this method's own body

    stmt = all_lines[fail_line - 1].strip()
    if not stmt or stmt in ("{", "}"):
        return None

    m = _DECL_OR_ASSIGN_RE.match(stmt)
    variable = m.group(1) if m else root_variable(stmt)
    if not variable:
        return None
    return {"assert_type": "ExceptionSite", "raw_expression": stmt, "variable": variable, "line": fail_line}


def parse_assertions_in_method(src_file: Path, method_name: str, max_line=None):
    """Every assertX(...) call inside one test method's body, in source
    order: [{assert_type, raw_expression, variable, line}]. If `max_line` is
    given, assertions strictly after it are omitted entirely (they never
    executed).
    """
    if not src_file.exists():
        return []

    all_lines = src_file.read_text(encoding="utf-8", errors="replace").splitlines()
    bounds = extract_method_body_lines(all_lines, method_name)
    if not bounds:
        return []
    start, end = bounds
    body_text = "\n".join(all_lines[start: end + 1])

    assertions = []
    for match in ASSERT_CALL_RE.finditer(body_text):
        assert_type = match.group(1)
        raw_args = split_args(match.group(2))
        abs_line_no = start + body_text[: match.start()].count("\n") + 1  # 1-indexed

        if max_line is not None and abs_line_no > max_line:
            continue

        output_expr = assertion_output_expr(assert_type, raw_args)
        assertions.append({
            "assert_type": assert_type,
            "raw_expression": output_expr,
            "variable": root_variable(output_expr),
            "line": abs_line_no,
        })
    return assertions
