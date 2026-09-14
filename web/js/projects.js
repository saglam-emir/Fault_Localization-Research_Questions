// projects.js - Projects & Buggy Versions explorer.
// Projects -> Buggy Version -> [Overview | Matrix | Ochiai Ranking].
// Simple, descriptive, data-focused (per the design brief) - status values
// are only ever "Completed" (pipeline reached this stage, status OK) or
// "Not Available" (status FAIL - nothing further to distinguish honestly,
// no per-stage success tracking exists in the data).

let SUMMARY = null;
let PROJECT_ROWS = [];
const state = { level: 'projects', project: null, bugKey: null, bugId: null, detailTab: 'overview', matrixApproach: 'trace', matrixZoom: 'md', ochiaiApproach: 'trace', ochiaiTopN: 10 };
let CURRENT_DETAIL = null; // cached bug JSON for the open detail view
let CURRENT_MATRIX = null; // cached matrix JSON for the open detail view

function fmtNum(v) { return (v == null || v === '' || v === 'None') ? '—' : (Number.isFinite(Number(v)) ? RQ.fmt.format(Number(v)) : v); }
function fmtRaw(v) { return (v == null || v === '' || v === 'None') ? '—' : v; }
function stageStatus(row) { return row && row.status === 'OK' ? 'Completed' : 'Not Available'; }
function badge(label) { return `<span class="cat-badge ${label === 'Completed' ? 'completed' : 'notavailable'}">${label}</span>`; }
function colors() { const cs = getComputedStyle(document.documentElement); return { accent: cs.getPropertyValue('--accent').trim(), ok: cs.getPropertyValue('--ok').trim(), fail: cs.getPropertyValue('--fail').trim() }; }

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

// Only these 3 fields make a "place" - detailTab/matrixApproach/etc. are
// filters within a place, not navigation, and stay out of history so Back
// undoes drill-down one screen at a time instead of stepping through
// every tab/control click too.
function navSnapshot() { return { level: state.level, project: state.project, bugId: state.bugId }; }

function goToProjects(push = true) {
  state.level = 'projects'; state.project = null; state.bugKey = null; state.bugId = null;
  renderBreadcrumb(); showView('projects');
  if (push) RQ.pushNav(navSnapshot());
}
function goToBugs(project, push = true) {
  state.level = 'bugs'; state.project = project; state.bugKey = null; state.bugId = null;
  renderBreadcrumb(); showView('bugs'); renderBugsView();
  if (push) RQ.pushNav(navSnapshot());
}
function goToDetail(project, bugId, push = true) {
  state.level = 'detail'; state.project = project; state.bugId = bugId; state.bugKey = `${project}_${bugId}`; state.detailTab = 'overview';
  renderBreadcrumb(); showView('detail'); renderDetailView();
  if (push) RQ.pushNav(navSnapshot());
}

// Browser Back/Forward restores a previously-captured place without
// re-pushing it (push=false) - re-pushing here would grow the stack
// instead of walking it.
function restoreNav(s) {
  if (!s || s.level === 'projects') { goToProjects(false); return; }
  if (s.level === 'bugs') { goToBugs(s.project, false); return; }
  goToDetail(s.project, s.bugId, false);
}

// ==================================================== PROJECTS OVERVIEW
function renderOverviewSummary() {
  const completed = PROJECT_ROWS.filter(r => r.status === 'OK').length;
  const cards = [
    { value: SUMMARY.total_projects, label: 'Total Projects' },
    { value: PROJECT_ROWS.length, label: 'Total Buggy Versions' },
    { value: completed, label: 'Completed Buggy Versions' },
    { value: PROJECT_ROWS.length - completed, label: 'Failed / Incomplete' },
  ];
  RQ.renderStatCards(document.getElementById('projects-summary-cards'), cards);
}

function renderProjectBarChart() {
  const c = colors();
  const sorted = [...SUMMARY.projects].sort((a, b) => b.buggy_versions - a.buggy_versions);
  RQ.renderStackedBarList(document.getElementById('project-bar-chart'), {
    categories: sorted.map(p => p.project),
    series: [{ name: 'Buggy Versions', color: c.accent, values: sorted.map(p => p.buggy_versions) }],
    onCategoryClick: goToBugs,
  });
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

// ========================================================== BUGS TABLE
function renderBugsView() {
  const rows = PROJECT_ROWS.filter(r => r.project === state.project);
  const ok = rows.filter(r => r.status === 'OK').length;
  const totalFaultLines = rows.reduce((s, r) => s + (r.total_fault_lines || 0), 0);
  RQ.renderStatCards(document.getElementById('bugs-summary-cards'), [
    { value: rows.length, label: 'Buggy Versions' }, { value: ok, label: 'Completed' }, { value: rows.length - ok, label: 'Not Available' },
    { value: totalFaultLines, label: 'Ground-Truth Fault Lines' },
  ]);

  RQ.createDataTable(document.getElementById('bugs-table'), {
    columns: [
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'tests', label: 'Tests', numeric: true },
      { key: 'pass_tc', label: 'Passing', numeric: true, format: fmtNum },
      { key: 'fail_tc', label: 'Failing', numeric: true, format: fmtNum },
      { key: 'executed_statements', label: 'Executed Statements', numeric: true, format: fmtNum },
      { key: 'matrix_status', label: 'Matrix Status', format: badge },
      { key: 'ochiai_status', label: 'Ochiai Status', format: badge },
    ],
    rows: rows.map(r => ({ ...r, tests: (r.pass_tc || 0) + (r.fail_tc || 0), matrix_status: stageStatus(r), ochiai_status: stageStatus(r) })),
    searchKeys: ['bug_id'],
    pageSize: 25,
    onRowClick: bugId => goToDetail(state.project, bugId),
    rowKey: r => r.bug_id,
  });
}

// =========================================================== DETAIL
async function renderDetailView() {
  const el = document.getElementById('detail-content');
  el.innerHTML = `<p class="skeleton">Loading…</p>`;
  const row = PROJECT_ROWS.find(r => r.project === state.project && `${r.project}_${r.bug_id}` === state.bugKey);

  let d = null, m = null;
  try { d = await fetch(`data/bugs/${state.bugKey}.json`).then(r => r.json()); } catch (e) { /* ignore */ }
  try {
    const res = await fetch(`data/matrix/${state.bugKey}.json`);
    if (res.ok) m = await res.json();
  } catch (e) { /* ignore - not available for FAILed bugs */ }
  CURRENT_DETAIL = d; CURRENT_MATRIX = m;

  if (!d) { el.innerHTML = `<p class="skeleton">Could not load this buggy version's data.</p>`; return; }

  el.innerHTML = `
    <h1 style="font-family:var(--font-display);font-size:26px;margin-bottom:18px">${d.project} / ${d.bug_id}</h1>
    <div class="pipeline" id="pipeline-cards" style="margin-bottom:26px"></div>
    <div class="detail-tabs" id="detail-tabs"></div>
    <div id="detail-tab-content"></div>
  `;
  renderPipelineCards(d, row, m);
  RQ.renderSegmented(document.getElementById('detail-tabs'), [
    { value: 'overview', label: 'Overview' }, { value: 'matrix', label: 'Matrix' }, { value: 'ochiai', label: 'Ochiai Ranking' },
  ], state.detailTab, v => { state.detailTab = v; renderDetailTabContent(); });
  document.getElementById('detail-tabs').className = 'detail-tabs';
  document.querySelectorAll('#detail-tabs button').forEach(b => b.className = b.classList.contains('active') ? 'active' : '');
  renderDetailTabContent();
}

function renderPipelineCards(d, row, m) {
  const bestTrace = d.trace_ranking_top?.[1]; // [0] is header
  const stages = [
    { t: 'Test Execution', v: d.rq1 ? `${fmtNum(d.rq1.Pass_TC)} pass / ${fmtNum(d.rq1.Fail_TC)} fail` : '—' },
    { t: 'Execution Data', v: d.rq2 ? `${fmtNum(d.rq2.full_execution_size)} statements` : '—' },
    { t: 'Matrix Construction', v: m?.trace ? `${fmtNum(m.trace.total_rows)} × ${fmtNum(m.trace.total_cols)}` : 'Not available' },
    { t: 'Ochiai Calculation', v: (d.trace_ranking_top?.length > 1) ? `${d.trace_ranking_top.length - 1}+ statements ranked` : 'Not available' },
    { t: 'Suspiciousness Ranking', v: bestTrace ? `top score ${parseFloat(bestTrace[5]).toFixed(3)}` : 'Not available' },
  ];
  document.getElementById('pipeline-cards').innerHTML = stages.map((s, i) => `
    <div class="pipe-step"><div class="idx">0${i + 1}</div><h4>${s.t}</h4><p>${s.v}</p></div>
    ${i < stages.length - 1 ? '<div class="pipe-arrow">→</div>' : ''}`).join('');
}

function renderDetailTabContent() {
  const el = document.getElementById('detail-tab-content');
  document.querySelectorAll('#detail-tabs button').forEach(b => b.classList.toggle('active', b.dataset.value === state.detailTab));
  if (state.detailTab === 'overview') return renderOverviewTab(el);
  if (state.detailTab === 'matrix') return renderMatrixTab(el);
  return renderOchiaiTab(el);
}

// ---------------------------------------------------------- Overview tab
function renderOverviewTab(el) {
  const d = CURRENT_DETAIL;
  const c = colors();
  const rq1 = d.rq1, rq2 = d.rq2;
  el.innerHTML = `
    <div class="rq-cards" id="overview-metric-cards" style="margin-top:0"></div>
    <div class="rq-chart-panel" style="margin-top:24px"><div id="overview-pf-chart"></div></div>
  `;
  RQ.renderStatCards(document.getElementById('overview-metric-cards'), [
    { value: rq1 ? Number(rq1.Pass_TC) + Number(rq1.Fail_TC) : null, label: 'Total Test Cases' },
    { value: rq1 ? Number(rq1.Pass_TC) : null, label: 'Passing Test Cases' },
    { value: rq1 ? Number(rq1.Fail_TC) : null, label: 'Failing Test Cases' },
    { value: rq2 ? Number(rq2.full_execution_size) : null, label: 'Executed Statements' },
  ]);
  if (rq1) {
    RQ.renderComparisonBars(document.getElementById('overview-pf-chart'), [
      { label: 'Passing Tests', value: Number(rq1.Pass_TC), color: c.ok },
      { label: 'Failing Tests', value: Number(rq1.Fail_TC), color: c.fail },
    ]);
  } else {
    document.getElementById('overview-pf-chart').innerHTML = `<p class="muted" style="font-size:13px">Not available - this buggy version's pipeline run did not complete.</p>`;
  }
}

// ------------------------------------------------------------ Matrix tab
function renderMatrixTab(el) {
  const m = CURRENT_MATRIX;
  if (!m) {
    el.innerHTML = `<p class="skeleton">Matrix not available for this buggy version (pipeline did not reach this stage).</p>`;
    return;
  }
  el.innerHTML = `
    <div class="rq-controls" style="margin-top:0">
      <div class="seg-group"><span class="seg-label">Approach</span><div class="seg" id="matrix-approach-seg"></div></div>
    </div>
    <div class="kv-grid" id="matrix-dims" style="margin:18px 0"></div>
    <div id="heatmap-container"></div>
  `;
  RQ.renderSegmented(document.getElementById('matrix-approach-seg'), [
    { value: 'trace', label: 'Trace' }, { value: 'slice', label: 'Slice' },
  ], state.matrixApproach, v => { state.matrixApproach = v; renderMatrixTab(el); });

  const md = m[state.matrixApproach];
  if (!md) {
    document.getElementById('matrix-dims').innerHTML = `<div class="kv-item"><div class="k">Status</div><div class="v">Not available</div></div>`;
    document.getElementById('heatmap-container').innerHTML = '';
    return;
  }
  document.getElementById('matrix-dims').innerHTML = [
    ['Matrix Rows (tests)', RQ.fmt.format(md.total_rows)],
    ['Matrix Columns (statements)', RQ.fmt.format(md.total_cols)],
    ['Preview Density', RQ.pct(md.preview_density)],
  ].map(([k, v]) => `<div class="kv-item"><div class="k">${k}</div><div class="v">${v}</div></div>`).join('');
  renderHeatmap(document.getElementById('heatmap-container'), md);
}

function renderHeatmap(el, md) {
  const truncated = md.total_rows > md.preview_row_count || md.total_cols > md.preview_col_count;
  const header = `<tr><th></th>${md.stmt_labels.map(s => `<th>${s}</th>`).join('')}</tr>`;
  const body = md.rows.map(r => `<tr><th title="${r.test}">${r.test}</th>${r.cells.map(c => `<td class="heatmap-cell ${c ? 'on' : 'off'}" title="${r.test} = ${c}"></td>`).join('')}</tr>`).join('');
  el.innerHTML = `
    <div class="heatmap-toolbar">
      <span class="heatmap-note">${truncated
        ? `Showing ${md.preview_row_count}×${md.preview_col_count} of ${RQ.fmt.format(md.total_rows)}×${RQ.fmt.format(md.total_cols)} cells - too large to render fully in-browser.`
        : `Full matrix - ${md.total_rows}×${md.total_cols} cells.`}</span>
      <div class="seg" id="zoom-seg"></div>
    </div>
    <div class="heatmap-wrap"><table class="heatmap-table zoom-${state.matrixZoom}"><thead>${header}</thead><tbody>${body}</tbody></table></div>
  `;
  RQ.renderSegmented(document.getElementById('zoom-seg'), [
    { value: 'sm', label: '−' }, { value: 'md', label: '•' }, { value: 'lg', label: '+' },
  ], state.matrixZoom, v => { state.matrixZoom = v; document.querySelector('.heatmap-table').className = `heatmap-table zoom-${v}`; document.querySelectorAll('#zoom-seg button').forEach(b => b.classList.toggle('active', b.dataset.value === v)); });
}

// ------------------------------------------------------------ Ochiai tab
function parseRankingRows(top) {
  if (!top || top.length < 2) return [];
  const [header, ...body] = top;
  const idx = k => header.indexOf(k);
  return body.map(row => ({
    rank: parseInt(row[idx('rank')], 10),
    statement_id: row[idx('statement_id')],
    file: row[idx('file')],
    line: parseInt(row[idx('line')], 10),
    code: row[idx('code')],
    ochiai_score: parseFloat(row[idx('ochiai_score')]),
    tie_size: parseInt(row[idx('tie_size')], 10),
  }));
}

function renderOchiaiTab(el) {
  const d = CURRENT_DETAIL;
  el.innerHTML = `
    <div class="rq-controls" style="margin-top:0">
      <div class="seg-group"><span class="seg-label">Approach</span><div class="seg" id="ochiai-approach-seg"></div></div>
      <div class="seg-group"><span class="seg-label">Top</span><div class="seg" id="ochiai-topn-seg"></div></div>
    </div>
    <div class="section-head" style="margin-top:24px">
      <h2 style="font-size:18px">Ochiai Suspiciousness Ranking</h2>
    </div>
    <div class="rq-chart-panel"><div id="ochiai-chart"></div></div>
    <div class="rq-table-section"><div id="ochiai-table"></div></div>
  `;
  RQ.renderSegmented(document.getElementById('ochiai-approach-seg'), [
    { value: 'trace', label: 'Trace' }, { value: 'slice', label: 'Slice' },
  ], state.ochiaiApproach, v => { state.ochiaiApproach = v; renderOchiaiTab(el); });
  RQ.renderSegmented(document.getElementById('ochiai-topn-seg'), [
    { value: 10, label: 'Top 10' }, { value: 20, label: 'Top 20' }, { value: 50, label: 'Top 50' }, { value: 999, label: 'All' },
  ].map(o => ({ ...o, value: String(o.value) })), String(state.ochiaiTopN), v => { state.ochiaiTopN = parseInt(v, 10); renderOchiaiTab(el); });

  const raw = state.ochiaiApproach === 'trace' ? d.trace_ranking_top : d.slice_ranking_top;
  const allRows = parseRankingRows(raw);
  const faultySet = new Set((d.fault_lines || []).map(f => `${f.file_name}:${f.line_no}`));
  const rows = allRows.slice(0, Math.min(state.ochiaiTopN, allRows.length));

  if (!rows.length) {
    document.getElementById('ochiai-chart').innerHTML = `<p class="skeleton">Not available for this approach.</p>`;
    document.getElementById('ochiai-table').innerHTML = '';
    return;
  }
  if (allRows.length >= 50 && state.ochiaiTopN > allRows.length) {
    document.getElementById('ochiai-chart').insertAdjacentHTML('beforebegin', `<p class="muted" style="font-size:12px;margin-bottom:8px">Showing all ${allRows.length} statements available in this preview (the underlying ranking may contain more).</p>`);
  }
  renderOchiaiBars(document.getElementById('ochiai-chart'), rows, faultySet);

  RQ.createDataTable(document.getElementById('ochiai-table'), {
    columns: [
      { key: 'rank', label: 'Rank', numeric: true },
      { key: 'file', label: 'File' },
      { key: 'line', label: 'Line', numeric: true },
      { key: 'ochiai_score', label: 'Ochiai Score', numeric: true, format: v => v.toFixed(4) },
      { key: 'faulty', label: 'Faulty Line', format: v => v ? '★' : '' },
    ],
    rows: allRows.map(r => ({ ...r, faulty: faultySet.has(`${r.file}:${r.line}`) })),
    searchKeys: ['file'],
    pageSize: 20,
  });
}

function renderOchiaiBars(el, rows, faultySet) {
  const c = colors();
  const max = Math.max(...rows.map(r => r.ochiai_score), 0.0001);
  el.innerHTML = `<div class="bar-chart-scroll">` + rows.map(r => {
    const key = `${r.file}:${r.line}`;
    const isFaulty = faultySet.has(key);
    return `<div class="bar-row ${isFaulty ? 'faulty' : ''}">
      <div class="cat-label" title="${key}">${r.file}:${r.line}</div>
      <div class="bar-track">
        <div class="bar-seg" style="width:${(r.ochiai_score / max * 100).toFixed(1)}%;background:${c.accent};height:16px"></div>
        <span class="bar-value">${r.ochiai_score.toFixed(3)}</span>
        ${isFaulty ? '<span class="faulty-marker">← Faulty Line</span>' : ''}
      </div>
    </div>`;
  }).join('') + `</div>`;
}

// =============================================================== init
async function init() {
  try {
    [SUMMARY, PROJECT_ROWS] = await Promise.all([
      fetch('data/summary.json').then(r => r.json()),
      fetch('data/projects.json').then(r => r.json()),
    ]);
    renderBreadcrumb();
    renderOverviewSummary();
    renderProjectBarChart();
    renderProjectGrid();
    RQ.initNavHistory(navSnapshot, restoreNav);
  } catch (err) {
    console.error('Projects verisi yüklenemedi:', err);
    document.getElementById('project-grid').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
