"""
targets.py
==========
The 4 buggy versions this pipeline currently runs on (task-scoped subset of
the much larger defect_projects/ checkout pool). Adding a 5th target later
is a one-line addition here - nothing else in the pipeline hardcodes this
list.
"""

from pathlib import Path

RESQ_ROOT = Path(__file__).resolve().parent.parent
DEFECT_PROJECTS_DIR = RESQ_ROOT / "defect_projects"

TARGETS = [
    {
        "name": "Csv_3b",
        "project_id": "Csv",
        "bug_id": "3",
        "variant": "b",
        "checkout_dir": DEFECT_PROJECTS_DIR / "Csv" / "csv_3b",
    },
    {
        "name": "Csv_13b",
        "project_id": "Csv",
        "bug_id": "13",
        "variant": "b",
        "checkout_dir": DEFECT_PROJECTS_DIR / "Csv" / "csv_13b",
    },
    {
        "name": "JacksonXml_1b",
        "project_id": "JacksonXml",
        "bug_id": "1",
        "variant": "b",
        "checkout_dir": DEFECT_PROJECTS_DIR / "JacksonXml" / "jacksonXml_1b",
    },
    {
        "name": "JacksonXml_6b",
        "project_id": "JacksonXml",
        "bug_id": "6",
        "variant": "b",
        "checkout_dir": DEFECT_PROJECTS_DIR / "JacksonXml" / "jacksonXml_6b",
    },
]
