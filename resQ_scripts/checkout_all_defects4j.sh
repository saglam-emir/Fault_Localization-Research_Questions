#!/usr/bin/env bash
#
# checkout_all_defects4j.sh
#
# Checks out every ACTIVE buggy version of every Defects4J (v2.x) project
# into a per-project directory structure:
#
#   defect_projects/<Project>/<projectFolder>_<id>b
#
# e.g. defect_projects/Lang/lang_1b, defect_projects/Csv/csv_13b
#
# The project list and the bug-id list for each project are discovered
# dynamically from the installed `defects4j` binary (nothing is hardcoded),
# so re-running this script against a different Defects4J checkout/version
# will automatically pick up whatever projects/bugs it exposes.
#
# Usage:
#   ./checkout_all_defects4j.sh                 # full run, wipes defect_projects/ first
#   ./checkout_all_defects4j.sh --resume         # skip dirs that already exist
#   ./checkout_all_defects4j.sh --jobs 4         # override parallelism (default 8)
#   ./checkout_all_defects4j.sh --project Lang   # only this project (repeatable)
#   ./checkout_all_defects4j.sh --dry-run        # just print the plan, checkout nothing

set -uo pipefail

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DEST_ROOT="$ROOT_DIR/defect_projects"
LOG_DIR="$ROOT_DIR/resQ_outputs/defects4j_checkout_logs"
JOBS=8
RESUME=0
DRY_RUN=0
declare -a ONLY_PROJECTS=()

if ! command -v defects4j >/dev/null 2>&1; then
    echo "ERROR: 'defects4j' not found on PATH. Source framework/util/defects4j-init.sh or add framework/bin to PATH." >&2
    exit 1
fi

# ----------------------------------------------------------------------------
# Args
# ----------------------------------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --resume) RESUME=1; shift ;;
        --jobs) JOBS="$2"; shift 2 ;;
        --project) ONLY_PROJECTS+=("$2"); shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

mkdir -p "$DEST_ROOT" "$LOG_DIR"

# ----------------------------------------------------------------------------
# Discover projects
# ----------------------------------------------------------------------------
if [[ ${#ONLY_PROJECTS[@]} -gt 0 ]]; then
    PROJECTS=("${ONLY_PROJECTS[@]}")
else
    mapfile -t PROJECTS < <(defects4j pids)
fi

echo "Discovered ${#PROJECTS[@]} project(s): ${PROJECTS[*]}"

# lower-cases only the first character of a Defects4J project id, e.g.
# JacksonXml -> jacksonXml, Csv -> csv, Lang -> lang
folder_prefix() {
    local pid="$1"
    printf '%s%s' "$(tr '[:upper:]' '[:lower:]' <<<"${pid:0:1}")" "${pid:1}"
}

# ----------------------------------------------------------------------------
# Build the full job list: one line "PID BUGID DEST_DIR" per buggy version
# ----------------------------------------------------------------------------
JOB_LIST="$(mktemp)"
trap 'rm -f "$JOB_LIST"' EXIT

TOTAL_BUGS=0
for pid in "${PROJECTS[@]}"; do
    prefix="$(folder_prefix "$pid")"
    mkdir -p "$DEST_ROOT/$pid"
    bids="$(defects4j bids -p "$pid" 2>/dev/null)"
    if [[ -z "$bids" ]]; then
        echo "WARNING: no active bug ids found for project '$pid' — skipping" >&2
        continue
    fi
    n=0
    while read -r bid; do
        [[ -z "$bid" ]] && continue
        dest="$DEST_ROOT/$pid/${prefix}_${bid}b"
        echo "$pid $bid $dest" >> "$JOB_LIST"
        n=$((n+1))
    done <<< "$bids"
    echo "  $pid: $n active buggy version(s)"
    TOTAL_BUGS=$((TOTAL_BUGS + n))
done

echo "Total buggy versions to checkout: $TOTAL_BUGS"

if [[ $DRY_RUN -eq 1 ]]; then
    echo "--dry-run: plan only, nothing checked out. Job list:"
    cat "$JOB_LIST"
    exit 0
fi

# ----------------------------------------------------------------------------
# Wipe destination (unless resuming) — only the projects we're about to
# (re)generate, so a --project-scoped run doesn't nuke unrelated projects.
# ----------------------------------------------------------------------------
if [[ $RESUME -eq 0 ]]; then
    echo "Cleaning previous checkouts under: $DEST_ROOT"
    for pid in "${PROJECTS[@]}"; do
        rm -rf "${DEST_ROOT:?}/$pid"
        mkdir -p "$DEST_ROOT/$pid"
    done
fi

# ----------------------------------------------------------------------------
# Worker: checkout one buggy version
# ----------------------------------------------------------------------------
export RESUME
checkout_one() {
    local pid="$1" bid="$2" dest="$3"
    local log="$LOG_DIR/${pid}_${bid}b.log"

    if [[ $RESUME -eq 1 && -d "$dest" && -n "$(ls -A "$dest" 2>/dev/null)" ]]; then
        echo "SKIP $pid ${bid}b (already exists)"
        return 0
    fi

    rm -rf "$dest"
    if defects4j checkout -p "$pid" -v "${bid}b" -w "$dest" > "$log" 2>&1; then
        echo "OK   $pid ${bid}b -> $dest"
        return 0
    else
        echo "FAIL $pid ${bid}b (see $log)"
        return 1
    fi
}
export -f checkout_one
export LOG_DIR

# ----------------------------------------------------------------------------
# Run, in parallel, streaming progress + collecting a summary
# ----------------------------------------------------------------------------
RESULT_FILE="$LOG_DIR/_results.txt"
: > "$RESULT_FILE"

echo "Checking out $TOTAL_BUGS buggy version(s) with $JOBS parallel job(s)..."
cat "$JOB_LIST" | xargs -P "$JOBS" -L 1 bash -c 'checkout_one "$@"' _ | tee -a "$RESULT_FILE"

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
OK_COUNT=$(grep -c '^OK ' "$RESULT_FILE" || true)
SKIP_COUNT=$(grep -c '^SKIP ' "$RESULT_FILE" || true)
FAIL_COUNT=$(grep -c '^FAIL ' "$RESULT_FILE" || true)

echo
echo "================ SUMMARY ================"
echo "Total planned : $TOTAL_BUGS"
echo "Checked out   : $OK_COUNT"
echo "Skipped       : $SKIP_COUNT"
echo "Failed        : $FAIL_COUNT"
if [[ "$FAIL_COUNT" -gt 0 ]]; then
    echo
    echo "Failures:"
    grep '^FAIL ' "$RESULT_FILE"
    echo
    echo "Per-failure logs are in: $LOG_DIR"
fi
echo "==========================================="

[[ "$FAIL_COUNT" -eq 0 ]]
