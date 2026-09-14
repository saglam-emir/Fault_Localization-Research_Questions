// rq5.js - RQ5 (Fault Localization Ranking) page logic.
// Data source: web/data/rq5.json (direct rq5.csv -> JSON, one row per
// ground-truth fault LINE, not per bug).

let ALL_ROWS = [];
const state = { tolerance: 0, faultSet: 'answerable', scope: 'overall' };

function isUnanswerable(r) { return !!r.unanswerable_reason; }
function faultSetRows() { return state.faultSet === 'answerable' ? ALL_ROWS.filter(r => !isUnanswerable(r)) : ALL_ROWS; }

// The single source of truth for "is this a hit at tolerance N" - diff=0 is
// an exact rank_best_* match; diff=N (N>0) relaxes to exact-match-OR-within-
// N-lines via nearest_line_diff_* (which is 0 exactly when rank_best_* is
// already found, per the data's own definition - see rq5-methodology).
function hitAt(row, kind, tol) {
  const rankKey = kind === 'trace' ? 'rank_best_trace' : 'rank_best_slice';
  if (row[rankKey] != null) return true;
  if (tol === 0) return false;
  const d = (kind === 'trace' ? row.nearest_line_diff_trace : row.nearest_line_diff_slice);
  return d != null && Math.abs(d) <= tol;
}
function rate(rows, kind, tol) {
  return rows.length ? rows.filter(r => hitAt(r, kind, tol)).length / rows.length : 0;
}

function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function colors() {
  const cs = getComputedStyle(document.documentElement);
  return { trace: cs.getPropertyValue('--ink-faint').trim(), slice: cs.getPropertyValue('--accent').trim() };
}

function renderSummaryCards() {
  const answerable = ALL_ROWS.filter(r => !isUnanswerable(r));
  const unanswerable = ALL_ROWS.length - answerable.length;
  const cards = [
    { n: RQ.fmt.format(ALL_ROWS.length), l: 'Total Fault Lines' },
    { n: RQ.fmt.format(answerable.length), l: 'Answerable Fault Lines' },
    { n: RQ.fmt.format(unanswerable), l: 'Unanswerable' },
    { n: RQ.pct(rate(answerable, 'trace', 0)), l: 'Exact Match Rate — Trace' },
    { n: RQ.pct(rate(answerable, 'slice', 0)), l: 'Exact Match Rate — Slice' },
  ];
  document.getElementById('rq5-cards').innerHTML = cards.map(c => `
    <div class="rq-card-stat"><div class="n">${c.n}</div><div class="l">${c.l}</div></div>`).join('');
}

function renderControls() {
  RQ.renderSegmented(document.getElementById('tolerance-seg'), [
    { value: 0, label: 'Exact (0)' }, { value: 1, label: '±1' }, { value: 2, label: '±2' }, { value: 3, label: '±3' },
  ].map(o => ({ ...o, value: String(o.value) })), String(state.tolerance), v => { state.tolerance = parseInt(v, 10); update(); });

  RQ.renderSegmented(document.getElementById('faultset-seg'), [
    { value: 'answerable', label: 'Answerable Only' }, { value: 'all', label: 'All Faults' },
  ], state.faultSet, v => { state.faultSet = v; update(); });

  RQ.renderSegmented(document.getElementById('scope-seg'), [
    { value: 'overall', label: 'Overall' }, { value: 'project', label: 'By Project' },
  ], state.scope, v => { state.scope = v; update(); });
}

function update() {
  renderControls();
  const c = colors();
  const rows = faultSetRows();
  const chartEl = document.getElementById('rq5-chart');

  if (state.scope === 'overall') {
    RQ.renderComparisonBars(chartEl, [
      { label: 'Trace', value: rate(rows, 'trace', state.tolerance), color: c.trace },
      { label: 'Slice', value: rate(rows, 'slice', state.tolerance), color: c.slice },
    ], { formatValue: RQ.pct });
  } else {
    const projects = projectList();
    const series = [
      { name: 'Trace', color: c.trace, values: projects.map(p => rate(rows.filter(r => r.project === p), 'trace', state.tolerance)) },
      { name: 'Slice', color: c.slice, values: projects.map(p => rate(rows.filter(r => r.project === p), 'slice', state.tolerance)) },
    ];
    const order = projects.map((_, i) => i).sort((a, b) => series[0].values[b] - series[0].values[a]);
    RQ.renderGroupedBarList(chartEl, {
      categories: order.map(i => projects[i]),
      series: series.map(s => ({ ...s, values: order.map(i => s.values[i]) })),
      formatValue: RQ.pct,
    });
  }

  const n = rows.length;
  const traceHits = rows.filter(r => hitAt(r, 'trace', state.tolerance)).length;
  const sliceHits = rows.filter(r => hitAt(r, 'slice', state.tolerance)).length;
  document.getElementById('rq5-tolerance-note-text').innerHTML = state.tolerance === 0
    ? `Exact match only: the ranked-best statement must be the true fault line itself. Trace: ${RQ.fmt.format(traceHits)}/${RQ.fmt.format(n)} · Slice: ${RQ.fmt.format(sliceHits)}/${RQ.fmt.format(n)} fault lines (${state.faultSet === 'answerable' ? 'answerable only' : 'all faults'}).`
    : `A hit counts if the ranking finds the exact line, <em>or</em> the nearest same-file ranked statement is within ${state.tolerance} line${state.tolerance > 1 ? 's' : ''} of it. Trace: ${RQ.fmt.format(traceHits)}/${RQ.fmt.format(n)} · Slice: ${RQ.fmt.format(sliceHits)}/${RQ.fmt.format(n)} fault lines (${state.faultSet === 'answerable' ? 'answerable only' : 'all faults'}). This is a diagnostic, near-miss view - it does not redefine the project's primary (exact-match) success metric.`;

  renderCurve();
}

function renderCurve() {
  const rows = faultSetRows();
  const c = colors();
  const tolerances = [0, 1, 2, 3];
  RQ.renderLineChart(document.getElementById('rq5-curve'), {
    xLabels: tolerances.map(t => t === 0 ? 'Exact' : `±${t}`),
    series: [
      { name: 'Trace', color: c.trace, values: tolerances.map(t => rate(rows, 'trace', t)) },
      { name: 'Slice', color: c.slice, values: tolerances.map(t => rate(rows, 'slice', t)) },
    ],
    formatY: RQ.pct,
  });
}

function renderUnanswerable() {
  const reasons = ALL_ROWS.filter(isUnanswerable).reduce((acc, r) => {
    acc[r.unanswerable_reason] = (acc[r.unanswerable_reason] || 0) + 1;
    return acc;
  }, {});
  const labels = { dead_code_never_executed: 'Dead Code (never existed in buggy build)', live_line_never_executed: 'Live Line, Never Executed (test-coverage gap)' };
  const items = Object.entries(reasons).map(([k, v]) => ({ label: labels[k] || k, value: v, color: getComputedStyle(document.documentElement).getPropertyValue('--fail').trim() }));
  RQ.renderComparisonBars(document.getElementById('rq5-unanswerable-chart'), items);
}

function fmtCell(v) { return v == null ? '—' : v; }

function renderTable() {
  RQ.createDataTable(document.getElementById('rq5-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'file_name', label: 'File' },
      { key: 'line_no', label: 'Line', numeric: true },
      { key: 'unanswerable_reason', label: 'Unanswerable', format: fmtCell },
      { key: 'rank_best_trace', label: 'Rank (Trace)', numeric: true, format: fmtCell },
      { key: 'nearest_line_diff_trace', label: 'Diff (Trace)', numeric: true, format: fmtCell },
      { key: 'rank_best_slice', label: 'Rank (Slice)', numeric: true, format: fmtCell },
      { key: 'nearest_line_diff_slice', label: 'Diff (Slice)', numeric: true, format: fmtCell },
    ],
    rows: ALL_ROWS,
    searchKeys: ['project', 'bug_id', 'file_name'],
    filterKey: 'project',
    pageSize: 25,
  });
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq5.json').then(r => r.json());
    renderSummaryCards();
    update();
    renderUnanswerable();
    renderTable();
  } catch (err) {
    console.error('RQ5 verisi yüklenemedi:', err);
    document.getElementById('rq5-chart').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
