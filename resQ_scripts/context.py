"""
context.py
==========
Everything a single buggy-version run needs, bundled into one small object
(`RunContext`) instead of a module-level config singleton. The pipeline runs
all 4 target bug versions in one Python process (see run_pipeline.py), so a
global `config` module (as a single-project prototype might use) would have
its paths overwritten by the second target; every step function below
therefore takes an explicit `ctx` argument instead.

RQ3 (computational overhead) needs wall-clock time and peak memory numbers
gathered *while* Steps 1-4 run, not recomputed afterwards by re-running
anything. `ctx.metrics` is the single place every step records those numbers
into, and rq_writers.py reads them back out at the end.
"""

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path

ENCODING = "utf-8"

# ---------------------------------------------------------------------------
# Tool locations / global settings (same for every target, overridable via
# environment variables so this works on a different machine without edits).
# ---------------------------------------------------------------------------
DEFECTS4J_CMD = os.environ.get("DEFECTS4J_CMD", "defects4j")
JAVA8_HOME = os.environ.get("JAVA8_HOME", "")

SLICER4J_HOME = os.environ.get("SLICER4J_HOME", os.path.expanduser("~/SFL_Slicing/tools/Slicer4J"))
SLICER4J_SCRIPT = os.environ.get("SLICER4J_SCRIPT", str(Path(SLICER4J_HOME) / "scripts" / "slicer4j.py"))
SLICER4J_TIMEOUT_SEC = int(os.environ.get("SLICER4J_TIMEOUT_SEC", "600"))
SLICER4J_MAX_ATTEMPTS = int(os.environ.get("SLICER4J_MAX_ATTEMPTS", "5"))

TEST_TIMEOUT_SEC = int(os.environ.get("TEST_TIMEOUT_SEC", "300"))

# D4J framework root, needed to locate a bug's official src patch (ground
# truth for RQ4). `defects4j` lives at <D4J_HOME>/framework/bin/defects4j.
D4J_HOME = Path(os.environ.get(
    "D4J_HOME",
    Path(os.path.expanduser("~/SFL_Slicing/tools/defects4j")),
))


@dataclass
class Metrics:
    """Timing/memory numbers accumulated across Steps 1-4 for one target,
    consumed by rq_writers.py to fill in rq3.csv.
    """
    baseline_time_sec: float = 0.0        # one untraced `defects4j test` run
    sbfl_time_sec: float = 0.0            # traditional SBFL: all `defects4j coverage -t` calls
    hybrid_extra_time_sec: float = 0.0    # hybrid-only extra: per-test runs + all Slicer4J calls
    slice_call_count: int = 0
    slice_time_total_sec: float = 0.0
    peak_memory_kb: float = 0.0

    def note_memory(self, kb):
        if kb is not None and kb > self.peak_memory_kb:
            self.peak_memory_kb = kb

    @property
    def hybrid_time_sec(self) -> float:
        # The hybrid approach still has to know which tests pass/fail, so it
        # is charged the same per-test execution time as SBFL plus its own
        # slicing overhead, not "SBFL_Time + Hybrid_Time" double counted.
        return self.sbfl_time_sec + self.hybrid_extra_time_sec

    @property
    def avg_slice_time_sec(self) -> float:
        return (self.slice_time_total_sec / self.slice_call_count) if self.slice_call_count else 0.0


@dataclass
class RunContext:
    name: str                # e.g. "Csv_3b" - used as the working-dir name and RQ row BugID label
    project_id: str          # Defects4J project id, e.g. "Csv"
    bug_id: str               # numeric bug id, e.g. "3"
    variant: str              # "b" (buggy) - defects4j vid = f"{bug_id}{variant}"
    checkout_dir: Path        # the already-checked-out buggy project root
    work_dir: Path            # resQ_outputs/work/<name>/ - all intermediate artifacts for this target
    logger: logging.Logger = field(default=None)
    metrics: Metrics = field(default_factory=Metrics)

    @property
    def vid(self) -> str:
        return f"{self.bug_id}{self.variant}"

    def __post_init__(self):
        for d in (self.step1_dir, self.step2_dir, self.step3_dir, self.step4_dir,
                  self.slice_lines_dir, self.slice_code_dir,
                  self.slicer_failing_dir, self.slicer_passed_dir, self.dep_dir):
            d.mkdir(parents=True, exist_ok=True)

    # -- intermediate-artifact locations, mirroring the original prototype's
    #    pipeline_outputs/stepNN_results/ layout, all nested under this
    #    target's own work_dir so 4 targets never collide with each other.
    @property
    def step1_dir(self) -> Path:
        return self.work_dir / "step1_tests"

    @property
    def step2_dir(self) -> Path:
        return self.work_dir / "step2_slicing"

    @property
    def step3_dir(self) -> Path:
        return self.work_dir / "step3_matrices"

    @property
    def step4_dir(self) -> Path:
        return self.work_dir / "step4_ranking"

    @property
    def slice_lines_dir(self) -> Path:
        return self.step2_dir / "slice_lines"

    @property
    def slice_code_dir(self) -> Path:
        return self.step2_dir / "slice_code"

    @property
    def slicer_failing_dir(self) -> Path:
        return self.step2_dir / "_slicer4j_failing"

    @property
    def slicer_passed_dir(self) -> Path:
        return self.step2_dir / "_slicer4j_passed"

    @property
    def dep_dir(self) -> Path:
        return self.step2_dir / "_dep_jars"
