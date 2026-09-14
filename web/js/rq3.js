// rq3.js - RQ3 (Computational Cost) page logic.
// Data source: web/data/rq3.json (direct rq3.csv -> JSON).

let ALL_ROWS = [];
const state = { metric: 'time', approach: 'hybrid', scope: 'overall', sortDir: 'desc', project: null };
const topState = { n: 10, sortBy: 'runtime' };

const APPROACH_FIELD = { baseline: 'baseline_time', sbfl: 'sbfl_time', hybrid: 'hybrid_time' };
const APPROACH_LABEL = { baseline: 'Baseline', sbfl: 'SBFL', hybrid: 'Hybrid' };

function formatSeconds(s) {
  if (s < 60) return `${s.toFixed(1)}s`;
  if (s < 3600) return `${(s / 60).toFixed(1)}m`;
  return `${(s / 3600).toFixed(1)}h`;
}
function formatKB(kb) {
  if (kb < 1024) return `${kb.toFixed(0)} KB`;
  if (kb < 1024 * 1024) return `${(kb / 1024).toFixed(1)} MB`;
  return `${(kb / 1024 / 1024).toFixed(2)} GB`;
}

function avg(rows, key) { return rows.length ? rows.reduce((s, r) => s + r[key], 0) / rows.length : 0; }
function bugNum(id) { return parseInt(id, 10) || 0; }
function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function rowsForProject(p) { return ALL_ROWS.filter(r => r.project === p).sort((a, b) => bugNum(a.bug_id) - bugNum(b.bug_id)); }
function keyOf(r) { return `${r.project}_${r.bug_id}`; }
function splitKey(key) { const i = key.lastIndexOf('_'); return [key.slice(0, i), key.slice(i + 1)]; }

function colors() {
  const cs = getComputedStyle(document.documentElement);
  return {
    baseline: cs.getPropertyValue('--ink-faint').trim(),
    sbfl: cs.getPropertyValue('--ok').trim(),
    hybrid: cs.getPropertyValue('--accent').trim(),
    slice: '#8a7fd1',
    memory: cs.getPropertyValue('--fail').trim(),
  };
}

function renderSummaryCards() {
  const slowest = [...ALL_ROWS].sort((a, b) => b.hybrid_time - a.hybrid_time)[0];
  const highestMem = [...ALL_ROWS].sort((a, b) => b.peak_memory_kb - a.peak_memory_kb)[0];
  const totalHybrid = ALL_ROWS.reduce((s, r) => s + r.hybrid_time, 0);
  const cards = [
    { n: RQ.fmt.format(ALL_ROWS.length), l: 'Analyzed Buggy Versions' },
    { n: formatSeconds(totalHybrid), l: 'Total Runtime (Hybrid)' },
    { n: formatSeconds(totalHybrid / ALL_ROWS.length), l: 'Average Runtime (Hybrid)' },
    { n: `${slowest.project}_${slowest.bug_id}`, l: `Slowest (${formatSeconds(slowest.hybrid_time)})` },
    { n: formatKB(highestMem.peak_memory_kb), l: `Peak Memory (${highestMem.project}_${highestMem.bug_id})` },
  ];
  document.getElementById('rq3-cards').innerHTML = cards.map(c => `
    <div class="rq-card-stat"><div class="n">${c.n}</div><div class="l">${c.l}</div></div>`).join('');
}

function renderControls() {
  RQ.renderSegmented(document.getElementById('metric-seg'), [
    { value: 'time', label: 'Execution Time' },
    { value: 'memory', label: 'Memory Usage' },
  ], state.metric, v => { state.metric = v; update(); });

  RQ.renderSegmented(document.getElementById('approach-seg'), [
    { value: 'baseline', label: 'Baseline' },
    { value: 'sbfl', label: 'SBFL' },
    { value: 'hybrid', label: 'Hybrid' },
    { value: 'all', label: 'All' },
  ], state.approach, v => { state.approach = v; update(); });

  RQ.renderSegmented(document.getElementById('scope-seg'), [
    { value: 'overall', label: 'Overall' },
    { value: 'project', label: 'By Project' },
    { value: 'bug', label: 'By Bug' },
  ], state.scope, v => {
    state.scope = v;
    if (v !== 'bug') state.project = null;
    update();
  });

  RQ.renderSegmented(document.getElementById('sortdir-seg'), [
    { value: 'desc', label: 'Highest → Lowest' },
    { value: 'asc', label: 'Lowest → Highest' },
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
  panel.querySelector('h4').textContent = `${row.project} / ${row.bug_id}`;
  panel.querySelector('.bug-detail-grid').innerHTML = `
    <div><div class="k">Baseline Time</div><div class="v">${formatSeconds(row.baseline_time)}</div></div>
    <div><div class="k">SBFL Time</div><div class="v">${formatSeconds(row.sbfl_time)}</div></div>
    <div><div class="k">Hybrid Time</div><div class="v">${formatSeconds(row.hybrid_time)}</div></div>
    <div><div class="k">Avg Slice Time</div><div class="v">${formatSeconds(row.avg_slice_time)}</div></div>
    <div><div class="k">Peak Memory</div><div class="v">${formatKB(row.peak_memory_kb)}</div></div>
  `;
  const diff = row.hybrid_time - row.baseline_time;
  const overheadPct = row.baseline_time ? (diff / row.baseline_time * 100) : null;
  document.getElementById('bug-detail-derived').innerHTML =
    `<span class="ic">ⓘ</span><span>Hybrid vs. Baseline: <strong>${diff >= 0 ? '+' : ''}${formatSeconds(Math.abs(diff))}</strong>` +
    (overheadPct !== null ? ` (<strong>${overheadPct >= 0 ? '+' : ''}${overheadPct.toFixed(0)}%</strong> overhead)` : '') +
    `</span>`;
  panel.scrollIntoView?.({ behavior: 'smooth', block: 'nearest' });
}

function update() {
  renderControls();
  document.getElementById('approach-wrap').hidden = state.metric !== 'time';
  document.getElementById('sort-dir-wrap').hidden = state.scope !== 'project';
  document.getElementById('project-select-wrap').hidden = state.scope !== 'bug';
  document.getElementById('bug-detail').hidden = true;
  document.getElementById('rq3-note').hidden = true;
  if (state.scope === 'bug') renderProjectSelect();

  const c = colors();
  const chartEl = document.getElementById('rq3-chart');
  const dir = state.sortDir === 'asc' ? 1 : -1;

  if (state.metric === 'memory') {
    renderMemoryView(chartEl, c, dir);
  } else if (state.approach === 'all') {
    renderAllApproachesView(chartEl, c, dir);
  } else {
    renderSingleApproachView(chartEl, c, dir);
  }
}

function renderMemoryView(chartEl, c, dir) {
  if (state.scope === 'overall') {
    RQ.renderComparisonBars(chartEl, [{ label: 'Peak Memory', value: avg(ALL_ROWS, 'peak_memory_kb'), color: c.memory }], { formatValue: formatKB });
    return;
  }
  if (state.scope === 'project') {
    const projects = projectList();
    const values = projects.map(p => avg(rowsForProject(p), 'peak_memory_kb'));
    const order = projects.map((_, i) => i).sort((a, b) => (values[a] - values[b]) * dir);
    RQ.renderStackedBarList(chartEl, {
      categories: order.map(i => projects[i]),
      series: [{ name: 'Peak Memory', color: c.memory, values: order.map(i => values[i]) }],
      formatValue: formatKB, onCategoryClick: goToBugScope,
    });
    return;
  }
  const rows = rowsForProject(state.project);
  RQ.renderStackedBarList(chartEl, {
    categories: rows.map(r => r.bug_id), keys: rows.map(keyOf),
    series: [{ name: 'Peak Memory', color: c.memory, values: rows.map(r => r.peak_memory_kb) }],
    formatValue: formatKB, onCategoryClick: showBugDetail,
  });
}

function renderSingleApproachView(chartEl, c, dir) {
  const field = APPROACH_FIELD[state.approach];
  const label = APPROACH_LABEL[state.approach];
  const color = c[state.approach];

  if (state.scope === 'overall') {
    RQ.renderComparisonBars(chartEl, [{ label, value: avg(ALL_ROWS, field), color }], { formatValue: formatSeconds });
    return;
  }
  if (state.scope === 'project') {
    const projects = projectList();
    const values = projects.map(p => avg(rowsForProject(p), field));
    const order = projects.map((_, i) => i).sort((a, b) => (values[a] - values[b]) * dir);
    RQ.renderStackedBarList(chartEl, {
      categories: order.map(i => projects[i]),
      series: [{ name: label, color, values: order.map(i => values[i]) }],
      formatValue: formatSeconds, onCategoryClick: goToBugScope,
    });
    return;
  }
  const rows = rowsForProject(state.project);
  RQ.renderStackedBarList(chartEl, {
    categories: rows.map(r => r.bug_id), keys: rows.map(keyOf),
    series: [{ name: label, color, values: rows.map(r => r[field]) }],
    formatValue: formatSeconds, onCategoryClick: showBugDetail,
  });
}

function renderAllApproachesView(chartEl, c, dir) {
  const seriesDef = [
    { key: 'baseline_time', name: 'Baseline', color: c.baseline },
    { key: 'sbfl_time', name: 'SBFL', color: c.sbfl },
    { key: 'hybrid_time', name: 'Hybrid', color: c.hybrid },
    { key: 'avg_slice_time', name: 'Avg Slice', color: c.slice },
  ];
  const note = document.getElementById('rq3-note');
  note.hidden = false;
  document.getElementById('rq3-note-text').innerHTML =
    'Grouped, not stacked - these are four separate timing measurements, not parts of one total. Compare bar lengths to see whether Hybrid meaningfully exceeds Baseline/SBFL.';

  if (state.scope === 'overall') {
    RQ.renderComparisonBars(chartEl, seriesDef.map(s => ({ label: s.name, value: avg(ALL_ROWS, s.key), color: s.color })), { formatValue: formatSeconds });
    return;
  }
  if (state.scope === 'project') {
    const projects = projectList();
    const series = seriesDef.map(s => ({ name: s.name, color: s.color, values: projects.map(p => avg(rowsForProject(p), s.key)) }));
    const hybridVals = series[2].values;
    const order = projects.map((_, i) => i).sort((a, b) => (hybridVals[a] - hybridVals[b]) * dir);
    RQ.renderGroupedBarList(chartEl, {
      categories: order.map(i => projects[i]),
      series: series.map(s => ({ ...s, values: order.map(i => s.values[i]) })),
      formatValue: formatSeconds, onCategoryClick: goToBugScope,
    });
    return;
  }
  const rows = rowsForProject(state.project);
  const series = seriesDef.map(s => ({ name: s.name, color: s.color, values: rows.map(r => r[s.key]) }));
  RQ.renderGroupedBarList(chartEl, {
    categories: rows.map(r => r.bug_id), keys: rows.map(keyOf),
    series, formatValue: formatSeconds, onCategoryClick: showBugDetail,
  });
}

// -------------------------------------------------------------- Top N --
function renderTopNControls() {
  RQ.renderSegmented(document.getElementById('topn-seg'), [
    { value: 5, label: 'Top 5' }, { value: 10, label: 'Top 10' }, { value: 20, label: 'Top 20' },
  ], topState.n, v => { topState.n = parseInt(v, 10); renderTopN(); });

  RQ.renderSegmented(document.getElementById('topn-sortby-seg'), [
    { value: 'runtime', label: 'Runtime' }, { value: 'memory', label: 'Memory' },
  ], topState.sortBy, v => { topState.sortBy = v; renderTopN(); });
}

function renderTopN() {
  document.querySelectorAll('#topn-seg button').forEach(b => b.classList.toggle('active', parseInt(b.dataset.value, 10) === topState.n));
  document.querySelectorAll('#topn-sortby-seg button').forEach(b => b.classList.toggle('active', b.dataset.value === topState.sortBy));

  const field = topState.sortBy === 'runtime' ? 'hybrid_time' : 'peak_memory_kb';
  const formatter = topState.sortBy === 'runtime' ? formatSeconds : formatKB;
  const c = colors();
  const top = [...ALL_ROWS].sort((a, b) => b[field] - a[field]).slice(0, topState.n);
  RQ.renderStackedBarList(document.getElementById('rq3-topn-chart'), {
    categories: top.map(r => `${r.project}-${r.bug_id}`),
    keys: top.map(keyOf),
    series: [{ name: topState.sortBy === 'runtime' ? 'Hybrid Time' : 'Peak Memory', color: topState.sortBy === 'runtime' ? c.hybrid : c.memory, values: top.map(r => r[field]) }],
    formatValue: formatter,
    onCategoryClick: showBugDetail,
  });
}

// ------------------------------------------------------------ Scatter --
function renderScatterSection() {
  const select = document.getElementById('scatter-project-select');
  select.innerHTML = `<option value="">All Projects</option>` + projectList().map(p => `<option value="${p}">${p}</option>`).join('');
  select.addEventListener('change', () => renderScatter());
  renderScatter();
}

function renderScatter() {
  const project = document.getElementById('scatter-project-select').value;
  const rows = project ? rowsForProject(project) : ALL_ROWS;
  const c = colors();
  RQ.renderScatter(document.getElementById('rq3-scatter'), {
    points: rows.map(r => ({ x: r.hybrid_time, y: r.peak_memory_kb, label: `${r.project}_${r.bug_id}`, key: keyOf(r) })),
    xLabel: 'Hybrid Time', yLabel: 'Peak Memory',
    formatX: formatSeconds, formatY: formatKB,
    color: c.hybrid,
    onPointClick: showBugDetail,
  });
}

function renderTable() {
  RQ.createDataTable(document.getElementById('rq3-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'baseline_time', label: 'Baseline Time', numeric: true, format: formatSeconds },
      { key: 'sbfl_time', label: 'SBFL Time', numeric: true, format: formatSeconds },
      { key: 'hybrid_time', label: 'Hybrid Time', numeric: true, format: formatSeconds },
      { key: 'avg_slice_time', label: 'Avg Slice Time', numeric: true, format: formatSeconds },
      { key: 'peak_memory_kb', label: 'Peak Memory', numeric: true, format: formatKB },
    ],
    rows: ALL_ROWS,
    searchKeys: ['project', 'bug_id'],
    filterKey: 'project',
    pageSize: 25,
  });
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq3.json').then(r => r.json());
    renderSummaryCards();
    document.getElementById('project-select-wrap').querySelector('.seg-select')
      .addEventListener('change', e => { state.project = e.target.value; update(); });
    update();
    renderTopNControls();
    renderTopN();
    renderScatterSection();
    renderTable();
  } catch (err) {
    console.error('RQ3 verisi yüklenemedi:', err);
    document.getElementById('rq3-chart').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
