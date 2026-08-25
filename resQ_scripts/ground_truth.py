"""
ground_truth.py
=================
RQ4 needs the actual faulty statement(s) for each bug. Defects4J ships the
human-written fix as a unified diff at
`<D4J_HOME>/framework/projects/<PID>/patches/<bid>.src.patch`.

IMPORTANT, VERIFIED DIRECTION: despite the generic "old file" `---`/"new
file" `+++` diff header naming, Defects4J's own `src.patch` files are
written FIXED -> BUGGY, not the other way around: the `---`/`-` side is the
FIXED revision and the `+++`/`+` side is the BUGGY revision we actually have
checked out. Confirmed directly against this checkout's own git history for
two independent bugs (Csv-3, JacksonXml-1) before relying on it:

    git diff HEAD <fixed_commit_from_defects4j_info> -- <file>

reproduces the *same* hunks as `<bid>.src.patch` with old/new swapped (e.g.
Csv-3's patch blob pair "af99745..0a6a090" == `git diff HEAD FIXED`'s pair
"0a6a090..af99745" reversed) - i.e. HEAD (our buggy checkout) already
matches the patch's `+`/new side, not its `-`/old side. So the buggy-file
ground-truth lines are the `+` lines' NEW-file line numbers, not the `-`
lines' old-file numbers.

Pure-deletion hunks (every changed line is `-`, no `+` lines at all - the
fix only *removes* code) have no line to point to in the buggy version by
definition: the bug there is disappears entirely once fixed, so there is no
"buggy line" narrower than the surrounding statement. As a documented
best-effort fallback, such a hunk is anchored to the last unchanged
(context) line immediately preceding the deleted block, flagged
`approx=True` in the returned rows.

ANSWERABILITY (classify_answerability): an `approx` anchor is sometimes not
just imprecise but genuinely dead - the whole method the anchor used to sit
in was deleted by the fix, and the anchor line is a leftover comment/blank
line inside what's now an empty gap, never a real statement (verified
directly for JacksonXml-6: `writeBinary(InputStream,...)` and its two
helpers are entirely absent from the buggy checkout; the patch's anchor
lines 843-851/866-867 are bare comments with no bytecode, so no
coverage/slice tool can ever report them regardless of technique). No
line-level SBFL or slicing approach can answer that case by construction -
scoring it the same as a genuine missed-but-findable statement (e.g.
Csv-13's CSVFormat.java:319) silently conflates "our technique failed" with
"there was never a line to find." classify_answerability flags exactly the
provable version of this: an `approx` anchor that never appears in the
trace matrix's statement universe - i.e. it did not execute in ANY test,
passing or failing, so it cannot be dead code specific to one run's control
flow, only dead code specific to the buggy build itself.

Deliberately NOT implemented here: substituting a "call site" (nearest
in-project stack frame, polymorphic dispatch site, etc.) as a replacement
ground-truth line for unanswerable bugs. Evaluated and rejected: it is
under-specified (several different frames could be chosen), unstable across
different failing tests of the same bug (unlike the patch, it isn't a fixed
per-bug artifact), and conflates crash-site localization with root-cause
fault localization - a technique that ranks generic exception-wrapping
boilerplate highly would score as a "hit" under that scheme for reasons
unrelated to finding the actual defect. Unanswerable bugs are excluded from
primary scoring instead (see rq_writers.py's rq0_answerability.csv).
"""

import re
from pathlib import Path

from context import D4J_HOME, ENCODING

HUNK_HEADER_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def patch_path(project_id: str, bug_id: str) -> Path:
    return D4J_HOME / "framework" / "projects" / project_id / "patches" / f"{bug_id}.src.patch"


def _new_side_file(diff_line: str):
    """'+++ b/src/main/java/org/apache/commons/csv/Lexer.java' -> that path
    with the 'b/' prefix stripped. None for '+++ /dev/null' (file deleted
    by the fix - can't happen on our buggy-side checkout anyway).
    """
    if not diff_line.startswith("+++ "):
        return None
    raw = diff_line[len("+++ "):].strip()
    if raw == "/dev/null":
        return None
    return raw[2:] if raw.startswith("b/") else raw


def parse_patch(patch_text: str):
    """Return [{file, line, approx}, ...]: one row per buggy-checkout line
    the official fix touches, using the diff's `+` (buggy) side - see the
    module docstring for why `+`, not `-`.
    """
    lines = patch_text.splitlines()
    faults = []
    current_file = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("+++ "):
            current_file = _new_side_file(line)
            i += 1
            continue

        m = HUNK_HEADER_RE.match(line)
        if m and current_file:
            new_line_no = int(m.group(3))
            i += 1
            hunk_added, hunk_anchors = [], []
            in_deletion_run = False
            while i < len(lines) and not lines[i].startswith("@@") and not lines[i].startswith("diff --git"):
                body = lines[i]
                if body.startswith("+") and not body.startswith("+++"):
                    # A '+' immediately resolves any deletion run that led up
                    # to it (a replacement, not a pure removal) - the '+'
                    # line itself is the real fault line, no anchor needed.
                    hunk_added.append(new_line_no)
                    new_line_no += 1
                    in_deletion_run = False
                elif body.startswith("-") and not body.startswith("---"):
                    # Fixed-only line: absent from the buggy file, consumes
                    # no new-file line number. Marks the start of a
                    # (possibly multi-line) pure-deletion run.
                    in_deletion_run = True
                elif body.startswith("\\"):
                    pass  # "\ No newline at end of file" - not a real line
                else:
                    # Context line. If it directly follows an unresolved
                    # deletion run (no '+' appeared before it), it is the
                    # nearest surviving buggy-file line to that removed
                    # statement - record one approximate anchor per run,
                    # not one for the whole hunk.
                    if in_deletion_run:
                        hunk_anchors.append(new_line_no)
                        in_deletion_run = False
                    new_line_no += 1
                i += 1
            if in_deletion_run:
                # Deletion run reaches the end of the hunk with no trailing
                # context line inside it - anchor to the next buggy-file
                # line number anyway (it is still a valid line in the file,
                # just outside this hunk's own displayed context).
                hunk_anchors.append(new_line_no)

            faults.extend({"file": current_file, "line": ln, "approx": False} for ln in hunk_added)
            faults.extend({"file": current_file, "line": ln, "approx": True} for ln in hunk_anchors)
            continue

        i += 1
    return faults


_STMT_TERMINATOR_RE = re.compile(r"[;{}]$|\*/$")
_MAX_STATEMENT_LOOKBACK = 10


def normalize_statement_line(src_path, line_no: int, max_lookback: int = _MAX_STATEMENT_LOOKBACK) -> int:
    """The enclosing Java statement's FIRST physical line for `line_no` in
    `src_path` - i.e. the line javac's bytecode line-number table actually
    attributes a multi-line statement to (confirmed directly for Csv-13:
    the `MYSQL` field's fluent-builder chain spans source lines 318-319;
    javac attributes the whole `putstatic` to 318, while the diff's edit
    point sits on 319 - so a slicer/coverage hit on 318 and a diff-derived
    ground-truth line of 319 are the SAME statement, not a near miss).

    Coverage tools (Cobertura) and Slicer4J both report lines via that same
    bytecode convention; only Defects4J's diff-derived ground truth doesn't
    (it reports wherever the literal text changed). This makes the two
    sides literally not comparable for any multi-line statement without
    normalizing one to the other - deliberately normalizing the ground
    truth side here (never touching what the coverage/slicing tools
    report), so Step 4's line-exact matching stops mistaking "found the
    right statement" for "missed by N lines".

    Heuristic (no AST library available - same constraint java_ast.py
    already documents): walk backward from `line_no` while the PRECEDING
    physical line does not terminate a statement (doesn't end in `;`, `{`,
    `}`, or `*/`) and is not itself blank/a comment line (a genuine
    statement terminator or a comment/blank line both mean "line_no is not
    a continuation of it"). Bounded by `max_lookback` so a misidentified
    boundary can never run away across unrelated code. Returns `line_no`
    unchanged if the source file is unavailable, out of range, or no
    continuation pattern is found within the bound.
    """
    if not src_path or not Path(src_path).exists():
        return line_no
    lines = Path(src_path).read_text(encoding=ENCODING, errors="replace").splitlines()
    if not (1 <= line_no <= len(lines)):
        return line_no

    cur, steps = line_no, 0
    while steps < max_lookback and cur > 1:
        prev = lines[cur - 2].strip()
        prev_is_boundary = (
            prev == "" or prev.startswith("//") or prev.startswith("*") or prev.startswith("/*")
            or bool(_STMT_TERMINATOR_RE.search(prev))
        )
        if prev_is_boundary:
            break
        cur -= 1
        steps += 1
    return cur


def load_ground_truth_faults(project_id: str, bug_id: str, logger, checkout_dir=None):
    """Ground-truth faulty (file, line) pairs for one Defects4J bug, resolved
    against its own patch file. `file` is the project-relative path exactly
    as it appears in the buggy checkout (e.g.
    'src/main/java/org/apache/commons/csv/Lexer.java'). `line` is always the
    original diff-derived line, unchanged, for display/audit.

    If `checkout_dir` is given, each fault also gets a `statement_line`
    field - `line` normalized to its enclosing statement's first physical
    line (see normalize_statement_line) - which is what Step 4 actually
    matches ranked statements against. Without `checkout_dir`,
    `statement_line` falls back to `line` unchanged (no normalization
    possible without the source tree to read).
    """
    path = patch_path(project_id, bug_id)
    if not path.exists():
        logger.warning(f"No src patch found for {project_id}-{bug_id} at {path}; RQ4 ground truth will be empty.")
        return []
    faults = parse_patch(path.read_text(encoding=ENCODING, errors="replace"))
    approx = [f for f in faults if f["approx"]]
    if approx:
        logger.info(f"{len(approx)}/{len(faults)} ground-truth fault line(s) are approximate "
                     f"(pure-deletion hunk, anchored to the preceding context line).")

    faults = [
        {**f, "statement_line": normalize_statement_line(Path(checkout_dir) / f["file"], f["line"])
                                 if checkout_dir is not None else f["line"]}
        for f in faults
    ]

    normalized = [f for f in faults if f["statement_line"] != f["line"]]
    if normalized:
        logger.info(f"{len(normalized)}/{len(faults)} ground-truth fault line(s) normalized to their "
                    f"enclosing statement's first line for matching: "
                    f"{[(f['file'], f['line'], '->', f['statement_line']) for f in normalized]}")
    logger.info(f"Loaded {len(faults)} ground-truth fault line(s) for {project_id}-{bug_id} from {path}")
    return faults


_CONTROL_HEADER_RE = re.compile(r"^\s*\}?\s*(?:else\s+)?(?:if|for|while|switch|catch)\s*\(")
_MAX_CONTROL_ANCESTOR_LEVELS = 5


def find_enclosing_executed_control_line(src_path, anchor_line: int, file_basename: str, trace_universe):
    """Correction roadmap Step 2 (omission faults): for an `approx` anchor
    that never executed (see classify_answerability's dead-code check), walk
    OUTWARD through its enclosing brace blocks looking for the nearest
    `if`/`for`/`while`/`switch`/`catch` header that DID execute (appears in
    `trace_universe`).

    Rationale: dynamic slicing/coverage can only ever report on statements
    that ran. A pure-deletion anchor sitting inside dead code (e.g. an
    entirely deleted method - JacksonXml-6) has no live statement to point
    to at all. But a "wrong branch taken" fault (e.g. JacksonXml-1: the
    `if` that should have led to one more call *did* execute, just took the
    wrong path) has a real, executed, structurally-locatable proxy one or
    more brace-levels up from the dead anchor - the guard whose outcome
    controls the missing code. This mirrors normalize_statement_line's
    existing "diff-perspective line vs. bytecode/coverage-perspective line"
    translation, one level higher (nearest live control ancestor instead of
    nearest statement start).

    Bounded to `_MAX_CONTROL_ANCESTOR_LEVELS` enclosing blocks, same
    conservative-lookback philosophy as normalize_statement_line's
    max_lookback - a misidentified boundary can never run away across
    unrelated code. Returns None if the source is unavailable, the anchor
    is out of range, or no executed control ancestor is found within the
    bound (this is a legitimate outcome for truly dead code, e.g.
    JacksonXml-6's deleted method - not every dead anchor has a live
    ancestor to fall back to).
    """
    if not src_path or not Path(src_path).exists():
        return None
    lines = Path(src_path).read_text(encoding=ENCODING, errors="replace").splitlines()
    if not (1 <= anchor_line <= len(lines)):
        return None
    universe = {ln for fn, ln in trace_universe if fn == file_basename}

    depth, levels = 0, 0
    i = anchor_line - 2  # 0-based index of the line just above the anchor
    while i >= 0 and levels < _MAX_CONTROL_ANCESTOR_LEVELS:
        text = lines[i]
        depth += text.count("}") - text.count("{")
        if depth < 0:
            # `text` (1-based line i+1) carries the unmatched '{' that opens
            # the block directly enclosing our current search point.
            header_line_no, header_text = i + 1, text
            if not _CONTROL_HEADER_RE.search(header_text) and i > 0:
                # Allman style: bare '{' on its own line, header above it.
                header_line_no, header_text = i, lines[i - 1]
            if _CONTROL_HEADER_RE.search(header_text):
                stmt_line = normalize_statement_line(src_path, header_line_no)
                if stmt_line in universe:
                    return stmt_line
                if header_line_no in universe:
                    return header_line_no
                # Header found but not executed either (e.g. an outer `if`
                # that also never ran) - keep climbing to the next level.
            depth = 0
            levels += 1
        i -= 1
    return None


def apply_control_dependence_proxy(faults, checkout_dir, trace_universe, logger):
    """For every fault that classify_answerability would otherwise mark
    unanswerable (an `approx` pure-deletion anchor that never executed
    anywhere), try find_enclosing_executed_control_line and, if it finds a
    live control ancestor, adopt it as this fault's `statement_line` -
    exactly the same field normalize_statement_line already sets and that
    step4_ranking.py / rq_writers._write_rq4 already match against, so this
    flows through the existing RQ0/RQ4/RQ5 logic and CSV schemas completely
    unchanged; no new columns, no separate code path.

    Faults that are not `approx`, or whose current statement_line already
    executed somewhere, are left untouched - this only ever improves a
    fault that would otherwise be a guaranteed, unrecoverable miss.
    """
    universe = {(file, int(line)) for file, line in trace_universe}
    out, upgraded = [], []
    for f in faults:
        basename = Path(f["file"]).name
        stmt_line = f.get("statement_line", f["line"])
        already_live = (basename, f["line"]) in universe or (basename, stmt_line) in universe
        if not f["approx"] or already_live:
            out.append(f)
            continue
        src_path = Path(checkout_dir) / f["file"] if checkout_dir is not None else None
        proxy_line = find_enclosing_executed_control_line(src_path, stmt_line, basename, trace_universe)
        if proxy_line is None:
            out.append(f)
            continue
        upgraded.append((f["file"], f["line"], proxy_line))
        out.append({**f, "statement_line": proxy_line})

    if upgraded:
        logger.info(f"{len(upgraded)} otherwise-unanswerable ground-truth fault line(s) matched to their "
                    f"nearest executed control-dependence ancestor instead (control_dependence_proxy): "
                    f"{upgraded}")
    return out


def classify_answerability(faults, trace_universe, logger):
    """Per-fault `answerable` flag + bug-level `bug_fully_unanswerable` verdict.

    `trace_universe` is the trace (SBFL) matrix's statement universe -
    every (file_basename, line) that executed with hits>0 in at least one
    test, passing or failing (see step3_matrices.build_trace_matrix). It is
    the broadest "did this line ever run at all, by any test" signal this
    pipeline computes, so it is the right oracle for "is this anchor
    provably dead code" - a slice-matrix-only check would be narrower and
    could mistake "not selected by our slicing criteria" for "never
    executed anywhere", which is a different (and not what we want to
    detect here) failure mode.

    A fault row is unanswerable only when ALL hold:
      - it is `approx` (a pure-deletion hunk's anchor, not a real edited
        line - see module docstring), AND
      - neither its raw diff `line` NOR its normalized `statement_line`
        (when present - see normalize_statement_line) appears in
        trace_universe. Checking both, not just `line`, avoids a false
        "unanswerable" verdict for an anchor that's itself the continuation
        line of a multi-line statement whose coverage hit lands on the
        statement's first line instead.
    A non-approx fault (a genuine `+` edit line) is never marked
    unanswerable here, even if some *other* run never covered it - that is
    an ordinary "technique missed a real, live line" outcome, not a
    ground-truth representation problem, and must keep counting normally
    against RQ4/RQ5.

    Returns [{"file", "line", "approx", "answerable"}, ...] (same order/
    length as `faults`) plus logs a bug-level verdict. Callers combine the
    per-row list with `all(not f["answerable"] for f in faults)` for the
    bug-level flag (empty `faults` is a separate "no ground truth" case,
    deliberately not conflated with "unanswerable" - see rq_writers.py).
    """
    # trace_universe is already [(file_basename, line), ...] - see
    # step3_matrices.build_trace_matrix's `ordered` / trace_statement_mapping.csv.
    universe = {(file, int(line)) for file, line in trace_universe}
    out = []
    for f in faults:
        basename = Path(f["file"]).name
        never_ran = (basename, f["line"]) not in universe and (basename, f.get("statement_line", f["line"])) not in universe
        dead = f["approx"] and never_ran
        out.append({**f, "answerable": not dead})

    unanswerable = [f for f in out if not f["answerable"]]
    if unanswerable:
        logger.warning(
            f"{len(unanswerable)}/{len(out)} ground-truth fault line(s) are UNANSWERABLE: approximate "
            f"anchors that never executed in any test (dead code in the buggy build - most likely an "
            f"entire deleted method, not a wrong-but-live statement). No line-level SBFL or slicing "
            f"technique can find these by construction: {[(f['file'], f['line']) for f in unanswerable]}"
        )
    if out and all(not f["answerable"] for f in out):
        logger.warning(
            "ALL ground-truth fault lines for this bug are unanswerable - this bug should be excluded "
            "from primary SBFL/Hybrid comparison scoring (see rq0_answerability.csv), not counted as "
            "either technique 'failing to find' a findable defect."
        )
    return out
