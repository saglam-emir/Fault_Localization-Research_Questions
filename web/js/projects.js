// projects.js - Projects & Buggy Versions explorer.
// Project -> Buggy Version -> Test/Execution Data -> Matrix Construction ->
// Ochiai Scores -> Suspiciousness Ranking. Simple, descriptive, data-focused
// (per the design brief) - minimal charting, mostly structured info panels.

let SUMMARY = null;
let PROJECT_ROWS = [];
const state = { level: 'projects', project: null, bugKey: null };

function fmtNum(v) {
  if (v == null || v === '' || v === 'None') return '—';
  const n = Number(v);
  return Number.isFinite(n) ? RQ.fmt.format(n) : v;
}
function fmtRaw(v) { return (v == null || v === '' || v === 'None') ? '—' : v; }

function showView(name) {
  document.getElementById('view-projects').hidden = name !== 'projects';
  document.getElementById('view-bugs').hidden = name !== 'bugs';
  document.getElementById('view-detail').hidden = name !== 'detail';
}

function renderBreadcrumb() {
  const parts = [`<a data-level="projects">Projects</a>`];
  if (state.project) parts.push(`<span class="sep">›</span>` + (state.level === 'bugs' ? `<span class="current">${state.project}</span>` : `<a data-level="bugs">${state.project}</a>`));
  if (state.bugKey) parts.push(`<span class="sep">›</span><span class="current">${state.bugKey}</span>`);
  const el = document.getElementById('breadcrumb');
  el.innerHTML = parts.join('');
  el.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    if (a.dataset.level === 'projects') goToProjects();
    else if (a.dataset.level === 'bugs') goToBugs(state.project);
  }));
}

function goToProjects() { state.level = 'projects'; state.project = null; state.bugKey = null; renderBreadcrumb(); showView('projects'); }
function goToBugs(project) { state.level = 'bugs'; state.project = project; state.bugKey = null; renderBreadcrumb(); showView('bugs'); renderBugsView(); }
function goToDetail(project, bugId) {
  state.level = 'detail'; state.project = project; state.bugKey = `${project}_${bugId}`;
  renderBreadcrumb(); showView('detail'); renderDetailView();
}

function renderProjectGrid() {
  const el = document.getElementById('project-grid');
  el.innerHTML = SUMMARY.projects.map(p => `
    <div class="project-card" data-project="${p.project}">
      <h3>${p.project}</h3>
      <div class="n">${p.buggy_versions}</div>
      <div class="stat-row">
        <span>buggy versions</span>
        ${p.fail > 0 ? `<span class="fail-tag">${p.fail} FAIL</span>` : `<span style="color:var(--ok)">all OK</span>`}
      </div>
    </div>`).join('');
  el.querySelectorAll('.project-card').forEach(card => card.addEventListener('click', () => goToBugs(card.dataset.project)));
}

function renderBugsView() {
  const rows = PROJECT_ROWS.filter(r => r.project === state.project);
  const ok = rows.filter(r => r.status === 'OK').length;
  const totalFaultLines = rows.reduce((s, r) => s + (r.total_fault_lines || 0), 0);
  document.getElementById('bugs-summary-cards').innerHTML = [
    { n: rows.length, l: 'Buggy Versions' },
    { n: ok, l: 'OK' },
    { n: rows.length - ok, l: 'FAIL' },
    { n: totalFaultLines, l: 'Ground-Truth Fault Lines' },
  ].map(c => `<div class="rq-card-stat"><div class="n">${c.n}</div><div class="l">${c.l}</div></div>`).join('');

  RQ.createDataTable(document.getElementById('bugs-table'), {
    columns: [
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'status', label: 'Status', format: v => `<span class="cat-badge ${v === 'OK' ? 'best' : 'neither'}">${v}</span>` },
      { key: 'pass_tc', label: 'Pass TC', numeric: true, format: fmtNum },
      { key: 'fail_tc', label: 'Fail TC', numeric: true, format: fmtNum },
      { key: 'total_fault_lines', label: 'Fault Lines', numeric: true },
      { key: 'answerable_fault_lines', label: 'Answerable', numeric: true },
      { key: 'elapsed_s', label: 'Runtime (s)', numeric: true, format: fmtNum },
    ],
    rows,
    searchKeys: ['bug_id'],
    pageSize: 25,
    onRowClick: bugId => goToDetail(state.project, bugId),
    rowKey: r => r.bug_id,
  });
}

function kv(items) {
  return `<div class="kv-grid">${items.map(([k, v]) => `<div class="kv-item"><div class="k">${k}</div><div class="v">${v}</div></div>`).join('')}</div>`;
}

function rankingTable(rows) {
  if (!rows || rows.length < 2) return `<p class="muted" style="font-size:13px">Not available for this buggy version.</p>`;
  const [header, ...body] = rows;
  return `<div class="ranking-table-scroll"><table class="ranking-table">
    <thead><tr>${header.map(h => `<th>${h}</th>`).join('')}</tr></thead>
    <tbody>${body.map(row => `<tr>${row.map(c => `<td>${c}</td>`).join('')}</tr>`).join('')}</tbody>
  </table></div>`;
}

async function renderDetailView() {
  const el = document.getElementById('detail-content');
  el.innerHTML = `<p class="skeleton">Loading…</p>`;
  let d;
  try {
    d = await fetch(`data/bugs/${state.bugKey}.json`).then(r => r.json());
  } catch (err) {
    el.innerHTML = `<p class="skeleton">Could not load this buggy version's data.</p>`;
    return;
  }

  const sections = [];

  sections.push(`
    <div class="detail-section">
      <h1 style="font-family:var(--font-display);font-size:26px;margin-bottom:6px">${d.project} / ${d.bug_id}</h1>
    </div>`);

  if (d.rq1) {
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Step 1 — Test Execution (RQ1)</span>${kv([
      ['Pass TC', fmtNum(d.rq1.Pass_TC)], ['Fail TC', fmtNum(d.rq1.Fail_TC)],
      ['Pass Assert', fmtNum(d.rq1.Pass_Assert)], ['Fail Assert', fmtNum(d.rq1.Fail_Assert)],
      ['Uncaught Exception', fmtNum(d.rq1.Uncaught_Exception)],
    ])}</div>`);
  }

  if (d.rq2) {
    const ratio = parseFloat(d.rq2.all_reduction_ratio);
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Step 2 — Slicing / Search-Space Reduction (RQ2)</span>${kv([
      ['Full Execution Size', fmtNum(d.rq2.full_execution_size)],
      ['Union All Slice', fmtNum(d.rq2.union_all_slice)],
      ['Union Passing Slice', fmtNum(d.rq2.union_passing_slice)],
      ['Union Failing Slice', fmtNum(d.rq2.union_failing_slice)],
      ['Reduction Ratio', Number.isFinite(ratio) ? RQ.pct(ratio) : '—'],
    ])}</div>`);
  }

  if (d.rq3) {
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Cost — Timing &amp; Memory (RQ3)</span>${kv([
      ['Baseline Time', fmtNum(d.rq3['Baseline_Time_(s)']) + 's'], ['SBFL Time', fmtNum(d.rq3['SBFL_Time_(s)']) + 's'],
      ['Hybrid Time', fmtNum(d.rq3['Hybrid_Time_(s)']) + 's'], ['Avg Slice Time', fmtNum(d.rq3['Avg_Slice_Time_(s)']) + 's'],
      ['Peak Memory', fmtNum((parseFloat(d.rq3['Peak_Memory_(KB)']) / 1024).toFixed(1)) + ' MB'],
    ])}</div>`);
  }

  if (d.rq4_trace || d.rq4_slice) {
    const items = [];
    if (d.rq4_trace) items.push(['Trace: Included / Total', `${fmtNum(d.rq4_trace.Included_In_Slice)} / ${fmtNum(d.rq4_trace.Total_Faults)}`], ['Trace: Any Fault Found', d.rq4_trace.Faulty_Stmts_In_Slice]);
    if (d.rq4_slice) items.push(['Slice: Included / Total', `${fmtNum(d.rq4_slice.Included_In_Slice)} / ${fmtNum(d.rq4_slice.Total_Faults)}`], ['Slice: Any Fault Found', d.rq4_slice.Faulty_Stmts_In_Slice]);
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Fault Inclusion (RQ4)</span>${kv(items)}</div>`);
  }

  if (d.fault_lines && d.fault_lines.length) {
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Fault Localization Ranking (RQ5)</span>
      <div class="ranking-table-scroll"><table class="ranking-table">
        <thead><tr><th>File</th><th>Line</th><th>Rank (Trace)</th><th>Diff (Trace)</th><th>Rank (Slice)</th><th>Diff (Slice)</th><th>Unanswerable</th></tr></thead>
        <tbody>${d.fault_lines.map(f => `<tr>
          <td>${f.file_name}</td><td>${f.line_no}</td>
          <td>${fmtRaw(f.rank_best_trace)}</td><td>${fmtRaw(f.nearest_line_diff_trace)}</td>
          <td>${fmtRaw(f.rank_best_slice)}</td><td>${fmtRaw(f.nearest_line_diff_slice)}</td>
          <td>${fmtRaw(f.unanswerable_reason)}</td>
        </tr>`).join('')}</tbody>
      </table></div>
    </div>`);
  }

  sections.push(`<div class="detail-section"><span class="eyebrow-sm">Step 3 — Trace Statement Matrix / Ochiai Ranking (Top 15)</span>${rankingTable(d.trace_ranking_top)}</div>`);
  sections.push(`<div class="detail-section"><span class="eyebrow-sm">Step 3 — Slice Statement Matrix / Ochiai Ranking (Top 15)</span>${rankingTable(d.slice_ranking_top)}</div>`);

  if (d.ranking_summary_md) {
    sections.push(`<div class="detail-section"><span class="eyebrow-sm">Step 4 — Ranking Summary</span><div class="md-block">${d.ranking_summary_md.replace(/</g, '&lt;')}</div></div>`);
  }

  el.innerHTML = sections.join('');
}

async function init() {
  try {
    [SUMMARY, PROJECT_ROWS] = await Promise.all([
      fetch('data/summary.json').then(r => r.json()),
      fetch('data/projects.json').then(r => r.json()),
    ]);
    renderBreadcrumb();
    renderProjectGrid();
  } catch (err) {
    console.error('Projects verisi yüklenemedi:', err);
    document.getElementById('project-grid').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
