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


def load_ground_truth_faults(project_id: str, bug_id: str, logger):
    """Ground-truth faulty (file, line) pairs for one Defects4J bug, resolved
    against its own patch file. `file` is the project-relative path exactly
    as it appears in the buggy checkout (e.g.
    'src/main/java/org/apache/commons/csv/Lexer.java').
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
    logger.info(f"Loaded {len(faults)} ground-truth fault line(s) for {project_id}-{bug_id} from {path}")
    return faults
