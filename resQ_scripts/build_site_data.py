#!/usr/bin/env python3
"""
build_site_data.py
====================
resQ_outputs_all/ (tek konsolide sonuç klasörü - bkz. proje kökündeki
resQ_outputs_all/) icindeki CSV'leri okuyup web/data/ altina web sitesinin
dogrudan tuketecegi JSON dosyalarina donusturur. Statik site build adimi -
canli bir backend yok, bu script her calistirildiginda web/data/ tamamen
yeniden uretilir (idempotent).

Kullanim:
    python3 resQ_scripts/build_site_data.py [<resQ_outputs_all yolu>] [<web/data cikti yolu>]
    (varsayilan: proje kokune gore resQ_outputs_all/ ve web/data/)

Uretilen dosyalar:
    web/data/summary.json              - anasayfa istatistik kartlari
    web/data/projects.json             - Projeler sayfasinin filtrelenebilir
                                          tablosu (bug basina bir satir)
    web/data/bugs/<Proje>_<BugID>.json - buggy version detay sayfasi (lazy-load)
    web/data/research_questions.json   - RQ sayfalarindaki grafik/ozet verisi

Not: work/ altindaki HAM matris dosyalari (step3_matrices/*_observation_matrix.csv
gibi, bazilari 100MB+) buraya hic islenmiyor - sadece rq*.csv'lerdeki zaten
ozetlenmis sayilar ve step4_ranking/*_ranking.csv'nin ilk N satiri kullaniliyor.
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent

TOP_N_RANKING = 15  # detay sayfasinda gosterilecek en supheli N satir


def read_csv(path: Path):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        return list(csv.DictReader(f))


def folder_prefix(project_id: str) -> str:
    return project_id[0].lower() + project_id[1:]


def load_all(src: Path):
    return {
        "rq1": read_csv(src / "rq1.csv"),
        "rq2": read_csv(src / "rq2.csv"),
        "rq3": read_csv(src / "rq3.csv"),
        "rq4_slice": read_csv(src / "rq4_slice.csv"),
        "rq4_trace": read_csv(src / "rq4.trace.csv"),
        "rq5": read_csv(src / "rq5.csv"),
        "answerability": read_csv(src / "answerability_bySlicers.csv"),
        "progress": read_csv(src / "run_group_parallel_progress.csv"),
    }


def index_by_key(rows, key_fn):
    out = {}
    for r in rows:
        out[key_fn(r)] = r
    return out


def build_summary(data, bug_rows):
    total_pass_tc = sum(int(r["Pass_TC"]) for r in data["rq1"])
    total_fail_tc = sum(int(r["Fail_TC"]) for r in data["rq1"])

    # progress.csv upsert semantigi yok (append-only log) - hedef basina
    # SON gorulen satiri esas al.
    last_status = {}
    for r in data["progress"]:
        last_status[r["name"]] = r
    ok = sum(1 for r in last_status.values() if r["status"] == "OK")
    fail = sum(1 for r in last_status.values() if r["status"] == "FAIL")
    total_elapsed_s = sum(int(r["elapsed_s"]) for r in last_status.values())

    projects = sorted({r["Project"] for r in data["rq1"]})

    per_project = []
    for p in projects:
        bugs_in_p = [b for b in bug_rows if b["project"] == p]
        per_project.append({
            "project": p,
            "buggy_versions": len(bugs_in_p),
            "ok": sum(1 for b in bugs_in_p if b["status"] == "OK"),
            "fail": sum(1 for b in bugs_in_p if b["status"] == "FAIL"),
        })

    return {
        "generated_at": None,  # main()'de doldurulur
        "total_projects": len(projects),
        "total_buggy_versions": len(bug_rows),
        "total_test_cases": total_pass_tc + total_fail_tc,
        "total_pass_tc": total_pass_tc,
        "total_fail_tc": total_fail_tc,
        "total_ok": ok,
        "total_fail": fail,
        "total_ground_truth_fault_lines": len(data["rq5"]),
        "total_elapsed_seconds": total_elapsed_s,
        "projects": per_project,
    }


def build_bug_rows(data):
    """Bug (Project+BugID) basina bir satir - Projeler sayfasinin ham verisi."""
    rq1_idx = index_by_key(data["rq1"], lambda r: (r["Project"], r["BugID"]))
    rq4s_idx = index_by_key(data["rq4_slice"], lambda r: (r["Project"], r["BugID"]))
    rq4t_idx = index_by_key(data["rq4_trace"], lambda r: (r["Project"], r["BugID"]))

    # rq5 satirlari bug basina cogul - grupla
    rq5_by_bug = defaultdict(list)
    for r in data["rq5"]:
        rq5_by_bug[(r["project"], r["bug_id"])].append(r)

    # progress.csv: hedef adi "<Proje>_<BugID>" -> son durum + sure
    last_status = {}
    for r in data["progress"]:
        last_status[r["name"]] = r

    rows = []
    all_keys = set(rq1_idx) | {(r["Project"], r["BugID"]) for r in data["rq4_slice"] + data["rq4_trace"]}
    for (project, bug_id) in sorted(all_keys, key=lambda k: (k[0], int(k[1].rstrip("b") or 0))):
        name = f"{project}_{bug_id}"
        rq1 = rq1_idx.get((project, bug_id), {})
        rq4s = rq4s_idx.get((project, bug_id), {})
        rq4t = rq4t_idx.get((project, bug_id), {})
        fault_rows = rq5_by_bug.get((project, bug_id), [])
        answerable_count = sum(1 for r in fault_rows if not r.get("unanswerable_reason"))
        prog = last_status.get(name, {})

        rows.append({
            "project": project,
            "bug_id": bug_id,
            "name": name,
            "status": prog.get("status", "OK" if rq1 else "UNKNOWN"),
            "elapsed_s": int(prog["elapsed_s"]) if prog.get("elapsed_s") else None,
            "pass_tc": int(rq1["Pass_TC"]) if rq1 else None,
            "fail_tc": int(rq1["Fail_TC"]) if rq1 else None,
            "uncaught_exception": int(rq1["Uncaught_Exception"]) if rq1 else None,
            "total_fault_lines": len(fault_rows),
            "answerable_fault_lines": answerable_count,
            "slice_all_faults_found": rq4s.get("All_Faulty_Stmts_In_Slice") == "True" if rq4s else None,
            "slice_any_fault_found": rq4s.get("Faulty_Stmts_In_Slice") == "True" if rq4s else None,
            "trace_all_faults_found": rq4t.get("All_Faulty_Stmts_In_Slice") == "True" if rq4t else None,
            "trace_any_fault_found": rq4t.get("Faulty_Stmts_In_Slice") == "True" if rq4t else None,
        })
    return rows


def load_ranking_top_n(bug_dir: Path, kind: str, n: int):
    """kind: 'trace' veya 'slice'. ranking csv'sinin ilk n satirini okur."""
    path = bug_dir / "step4_ranking" / f"{kind}_ranking.csv"
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        rows = [row for _, row in zip(range(n), reader)]
    return rows


def build_bug_detail(project, bug_id, data, work_dir: Path):
    name = f"{project}_{bug_id}"
    key = (project, bug_id)

    def find_one(rows, proj_field="Project", bug_field="BugID"):
        for r in rows:
            if r.get(proj_field) == project and r.get(bug_field) == bug_id:
                return r
        return None

    fault_rows = [r for r in data["rq5"] if r["project"] == project and r["bug_id"] == bug_id]
    answerability_rows = [r for r in data["answerability"] if r["Project"] == project and r["BugID"] == bug_id]

    bug_dir = work_dir / project / name
    ranking_summary_md = None
    rs_path = bug_dir / "step4_ranking" / "ranking_summary.md"
    if rs_path.exists():
        ranking_summary_md = rs_path.read_text(encoding="utf-8", errors="replace")

    return {
        "project": project,
        "bug_id": bug_id,
        "name": name,
        "rq1": find_one(data["rq1"]),
        "rq2": find_one(data["rq2"], "project", "bug_id"),
        "rq3": find_one(data["rq3"]),
        "rq4_slice": find_one(data["rq4_slice"]),
        "rq4_trace": find_one(data["rq4_trace"]),
        "fault_lines": fault_rows,
        "answerability": answerability_rows,
        "ranking_summary_md": ranking_summary_md,
        "trace_ranking_top": load_ranking_top_n(bug_dir, "trace", TOP_N_RANKING),
        "slice_ranking_top": load_ranking_top_n(bug_dir, "slice", TOP_N_RANKING),
    }


def build_research_questions(data, bug_rows):
    # RQ4: proje basina inclusion-rate dagilimi (slice ve trace ayri ayri)
    def rq4_breakdown(rows):
        by_project = defaultdict(lambda: {"all_found": 0, "some_found": 0, "none_found": 0, "n": 0})
        for r in rows:
            b = by_project[r["Project"]]
            b["n"] += 1
            if r["All_Faulty_Stmts_In_Slice"] == "True":
                b["all_found"] += 1
            elif r["Faulty_Stmts_In_Slice"] == "True":
                b["some_found"] += 1
            else:
                b["none_found"] += 1
        return by_project

    rq4_slice_bd = rq4_breakdown(data["rq4_slice"])
    rq4_trace_bd = rq4_breakdown(data["rq4_trace"])

    # RQ5: answerability kirilimi + diff-distance histogrami (sadece answerable, hit olmayan satirlar)
    unanswerable_reasons = defaultdict(int)
    diff_trace_hist = defaultdict(int)
    diff_slice_hist = defaultdict(int)
    answerable_hit_trace = answerable_miss_trace = 0
    answerable_hit_slice = answerable_miss_slice = 0

    for r in data["rq5"]:
        reason = r.get("unanswerable_reason")
        if reason:
            unanswerable_reasons[reason] += 1
            continue
        if r.get("rank_best_trace") not in ("", "None", None):
            answerable_hit_trace += 1
        else:
            answerable_miss_trace += 1
            d = r.get("nearest_line_diff_trace")
            if d not in ("", "None", None):
                try:
                    diff_trace_hist[abs(int(d))] += 1
                except ValueError:
                    pass
        if r.get("rank_best_slice") not in ("", "None", None):
            answerable_hit_slice += 1
        else:
            answerable_miss_slice += 1
            d = r.get("nearest_line_diff_slice")
            if d not in ("", "None", None):
                try:
                    diff_slice_hist[abs(int(d))] += 1
                except ValueError:
                    pass

    # RQ2: proje basina ortalama daralma orani
    rq2_by_project = defaultdict(list)
    for r in data["rq2"]:
        rq2_by_project[r["project"]].append(float(r["all_reduction_ratio"]))
    rq2_avg = {p: round(sum(v) / len(v), 4) for p, v in rq2_by_project.items() if v}

    return {
        "rq4_slice_by_project": {p: v for p, v in rq4_slice_bd.items()},
        "rq4_trace_by_project": {p: v for p, v in rq4_trace_bd.items()},
        "rq5_answerable_hit_trace": answerable_hit_trace,
        "rq5_answerable_miss_trace": answerable_miss_trace,
        "rq5_answerable_hit_slice": answerable_hit_slice,
        "rq5_answerable_miss_slice": answerable_miss_slice,
        "rq5_unanswerable_reasons": dict(unanswerable_reasons),
        "rq5_diff_distance_histogram_trace": dict(sorted(diff_trace_hist.items())),
        "rq5_diff_distance_histogram_slice": dict(sorted(diff_slice_hist.items())),
        "rq2_avg_reduction_ratio_by_project": rq2_avg,
    }


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT_DIR / "resQ_outputs_all"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT_DIR / "web" / "data"
    if not src.is_dir():
        print(f"HATA: kaynak bulunamadi: {src}", file=sys.stderr)
        sys.exit(1)

    out.mkdir(parents=True, exist_ok=True)
    (out / "bugs").mkdir(parents=True, exist_ok=True)

    print(f"Kaynak: {src}")
    data = load_all(src)

    bug_rows = build_bug_rows(data)
    summary = build_summary(data, bug_rows)
    import datetime
    summary["generated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  summary.json yazildi ({summary['total_projects']} proje, {summary['total_buggy_versions']} buggy version)")

    (out / "projects.json").write_text(json.dumps(bug_rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  projects.json yazildi ({len(bug_rows)} satir)")

    rq = build_research_questions(data, bug_rows)
    (out / "research_questions.json").write_text(json.dumps(rq, indent=2, ensure_ascii=False), encoding="utf-8")
    print("  research_questions.json yazildi")

    work_dir = src / "work"
    n_bugs = 0
    for row in bug_rows:
        detail = build_bug_detail(row["project"], row["bug_id"], data, work_dir)
        (out / "bugs" / f"{row['name']}.json").write_text(
            json.dumps(detail, indent=2, ensure_ascii=False), encoding="utf-8")
        n_bugs += 1
    print(f"  bugs/*.json yazildi ({n_bugs} dosya)")


if __name__ == "__main__":
    main()
