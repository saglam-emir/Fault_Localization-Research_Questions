// rq4.js - RQ4 (Fault Inclusion) page logic.
// Data source: web/data/rq4.json - rq4.trace.csv + rq4_slice.csv JOINED by
// (Project, BugID) at build time (see resQ_scripts/build_site_data.py).

let ALL_ROWS = [];
const state = { scope: 'overall', sortBy: 'best', sortDir: 'desc', project: null };
let compareMetric = 'rate';

function category(r) {
  if (r.trace_any_found && r.slice_any_found) return 'BEST CASE';
  if (r.trace_any_found) return 'TRACE ONLY';
  if (r.slice_any_found) return 'SLICE ONLY';
  return 'NEITHER';
}
function badgeClass(cat) {
  return { 'BEST CASE': 'best', 'TRACE ONLY': 'trace', 'SLICE ONLY': 'slice', 'NEITHER': 'neither' }[cat];
}
function badge(cat) { return `<span class="cat-badge ${badgeClass(cat)}">${cat}</span>`; }

function avg(rows, key) { return rows.length ? rows.reduce((s, r) => s + (r[key] || 0), 0) / rows.length : 0; }
function bugNum(id) { return parseInt(id, 10) || 0; }
function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function rowsForProject(p) { return ALL_ROWS.filter(r => r.project === p).sort((a, b) => bugNum(a.bug_id) - bugNum(b.bug_id)); }
function keyOf(r) { return `${r.project}_${r.bug_id}`; }
function splitKey(key) { const i = key.lastIndexOf('_'); return [key.slice(0, i), key.slice(i + 1)]; }

function colors() {
  const cs = getComputedStyle(document.documentElement);
  return { trace: cs.getPropertyValue('--ink-faint').trim(), slice: cs.getPropertyValue('--accent').trim(), best: cs.getPropertyValue('--ok').trim() };
}

function renderSummaryCards() {
  const n = ALL_ROWS.length;
  const traceIncl = ALL_ROWS.filter(r => r.trace_any_found).length;
  const sliceIncl = ALL_ROWS.filter(r => r.slice_any_found).length;
  const both = ALL_ROWS.filter(r => r.trace_any_found && r.slice_any_found).length;
  const neither = ALL_ROWS.filter(r => !r.trace_any_found && !r.slice_any_found).length;
  const cards = [
    { value: n, label: 'Buggy Versions Analyzed' },
    { value: traceIncl, label: 'Trace Included' },
    { value: sliceIncl, label: 'Slice Included' },
    { value: both, label: 'Both Included — Best Case', emph: true },
    { value: neither, label: 'Neither Included' },
  ];
  RQ.renderStatCards(document.getElementById('rq4-cards'), cards);
}

function renderControls() {
  RQ.renderSegmented(document.getElementById('scope-seg'), [
    { value: 'overall', label: 'Overall' }, { value: 'project', label: 'By Project' }, { value: 'bug', label: 'By Bug' },
  ], state.scope, v => { state.scope = v; if (v !== 'bug') state.project = null; update(); });

  RQ.renderSegmented(document.getElementById('sortby-seg'), [
    { value: 'best', label: 'Best Case Rate' }, { value: 'total', label: 'Total Faults' },
    { value: 'trace', label: 'Trace Inclusion Rate' }, { value: 'slice', label: 'Slice Inclusion Rate' },
  ], state.sortBy, v => { state.sortBy = v; update(); });

  RQ.renderSegmented(document.getElementById('sortdir-seg'), [
    { value: 'desc', label: 'Highest → Lowest' }, { value: 'asc', label: 'Lowest → Highest' },
  ], state.sortDir, v => { state.sortDir = v; update(); });
}

function renderProjectSelect() {
  const wrap = document.getElementById('project-select-wrap');
  const projects = projectList();
  if (!state.project) state.project = projects[0];
  wrap.querySelector('.seg-select').innerHTML = projects.map(p =>
    `<option value="${p}" ${p === state.project ? 'selected' : ''}>${p}</option>`).join('');
}

function goToBugScope(project) { state.scope = 'bug'; state.project = project; update(); }

function showBugDetail(key) {
  const [project, bugId] = splitKey(key);
  const row = ALL_ROWS.find(r => r.project === project && r.bug_id === bugId);
  const panel = document.getElementById('bug-detail');
  if (!row) { panel.hidden = true; return; }
  panel.hidden = false;
  panel.querySelector('h4').innerHTML = `${row.project} / ${row.bug_id} ${badge(category(row))}`;
  panel.querySelector('.bug-detail-grid').innerHTML = `
    <div><div class="k">Total Faults</div><div class="v">${row.total_faults}</div></div>
    <div><div class="k">Trace Included</div><div class="v">${row.trace_included ?? '—'}</div></div>
    <div><div class="k">Trace Inclusion Rate</div><div class="v">${row.trace_inclusion_rate != null ? RQ.pct(row.trace_inclusion_rate) : '—'}</div></div>
    <div><div class="k">Slice Included</div><div class="v">${row.slice_included ?? '—'}</div></div>
    <div><div class="k">Slice Inclusion Rate</div><div class="v">${row.slice_inclusion_rate != null ? RQ.pct(row.slice_inclusion_rate) : '—'}</div></div>
  `;
  panel.scrollIntoView?.({ behavior: 'smooth', block: 'nearest' });
}

function update() {
  renderControls();
  const isProject = state.scope === 'project';
  document.getElementById('sort-wrap').hidden = !isProject;
  document.getElementById('sort-dir-wrap').hidden = !isProject;
  document.getElementById('project-select-wrap').hidden = state.scope !== 'bug';
  document.getElementById('bug-detail').hidden = true;
  document.getElementById('rq4-matrix').innerHTML = '';
  document.getElementById('rq4-chart').innerHTML = '';
  if (state.scope === 'bug') renderProjectSelect();

  if (state.scope === 'overall') { renderOverallMatrix(); return; }
  if (state.scope === 'project') { renderProjectRanking(); return; }
  renderBugTable();
}

function renderOverallMatrix() {
  const c = colors();
  const cellCount = (traceVal, sliceVal) => ALL_ROWS.filter(r => !!r.trace_any_found === traceVal && !!r.slice_any_found === sliceVal).length;
  const n = ALL_ROWS.length;
  RQ.renderMatrix2x2(document.getElementById('rq4-matrix'), {
    rowLabels: ['Trace: False', 'Trace: True'],
    colLabels: ['Slice: False', 'Slice: True'],
    rowAxis: 'Trace', colAxis: 'Slice',
    cells: [
      { row: 0, col: 0, count: cellCount(false, false), total: n },
      { row: 0, col: 1, count: cellCount(false, true), total: n },
      { row: 1, col: 0, count: cellCount(true, false), total: n },
      { row: 1, col: 1, count: cellCount(true, true), total: n, emphasize: true },
    ],
  });
}

function renderProjectRanking() {
  const c = colors();
  const projects = projectList();
  const metricFor = p => {
    const rs = rowsForProject(p);
    if (state.sortBy === 'total') return rs.reduce((s, r) => s + r.total_faults, 0);
    if (state.sortBy === 'trace') return avg(rs, 'trace_inclusion_rate');
    if (state.sortBy === 'slice') return avg(rs, 'slice_inclusion_rate');
    return rs.filter(r => r.trace_any_found && r.slice_any_found).length / rs.length; // best case rate
  };
  const values = projects.map(metricFor);
  const dir = state.sortDir === 'asc' ? 1 : -1;
  const order = projects.map((_, i) => i).sort((a, b) => (values[a] - values[b]) * dir);
  const isRate = state.sortBy !== 'total';
  RQ.renderStackedBarList(document.getElementById('rq4-chart'), {
    categories: order.map(i => projects[i]),
    series: [{ name: state.sortBy, color: c.best, values: order.map(i => values[i]) }],
    formatValue: isRate ? RQ.pct : RQ.fmt.format,
    onCategoryClick: goToBugScope,
  });
}

function renderBugTable() {
  const rows = rowsForProject(state.project);
  RQ.createDataTable(document.getElementById('rq4-chart'), {
    columns: [
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'total_faults', label: 'Total Faults', numeric: true },
      { key: 'trace_included', label: 'Trace Included', numeric: true },
      { key: 'slice_included', label: 'Slice Included', numeric: true },
      { key: 'category', label: 'Category', format: v => badge(v) },
    ],
    rows: rows.map(r => ({ ...r, category: category(r) })),
    searchKeys: ['bug_id'],
    pageSize: 25,
    onRowClick: showBugDetail,
    rowKey: r => keyOf(r),
  });
}

function renderCompareControls() {
  RQ.renderSegmented(document.getElementById('compare-metric-seg'), [
    { value: 'rate', label: 'Inclusion Rate' }, { value: 'count', label: 'Faulty Statements' },
  ], compareMetric, v => { compareMetric = v; renderCompare(); });
}

function renderCompare() {
  const c = colors();
  const projects = projectList();
  const traceKey = compareMetric === 'rate' ? 'trace_inclusion_rate' : 'trace_included';
  const sliceKey = compareMetric === 'rate' ? 'slice_inclusion_rate' : 'slice_included';
  const series = [
    { name: 'Trace', color: c.trace, values: projects.map(p => avg(rowsForProject(p), traceKey)) },
    { name: 'Slice', color: c.slice, values: projects.map(p => avg(rowsForProject(p), sliceKey)) },
  ];
  const order = projects.map((_, i) => i).sort((a, b) => series[0].values[b] - series[0].values[a]);
  RQ.renderGroupedBarList(document.getElementById('rq4-compare-chart'), {
    categories: order.map(i => projects[i]),
    series: series.map(s => ({ ...s, values: order.map(i => s.values[i]) })),
    formatValue: compareMetric === 'rate' ? RQ.pct : RQ.fmt.format,
  });
}

function renderTable() {
  RQ.createDataTable(document.getElementById('rq4-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'total_faults', label: 'Total Faults', numeric: true },
      { key: 'trace_included', label: 'Trace Included', numeric: true },
      { key: 'trace_inclusion_rate', label: 'Trace Rate', numeric: true, format: v => v != null ? RQ.pct(v) : '—' },
      { key: 'slice_included', label: 'Slice Included', numeric: true },
      { key: 'slice_inclusion_rate', label: 'Slice Rate', numeric: true, format: v => v != null ? RQ.pct(v) : '—' },
      { key: 'category', label: 'Category', format: v => badge(v) },
    ],
    rows: ALL_ROWS.map(r => ({ ...r, category: category(r) })),
    searchKeys: ['project', 'bug_id'],
    filterKey: 'project',
    pageSize: 25,
  });
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq4.json').then(r => r.json());
    renderSummaryCards();
    document.getElementById('project-select-wrap').querySelector('.seg-select')
      .addEventListener('change', e => { state.project = e.target.value; update(); });
    update();
    renderCompareControls();
    renderCompare();
    renderTable();
  } catch (err) {
    console.error('RQ4 verisi yüklenemedi:', err);
    document.getElementById('rq4-matrix').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
