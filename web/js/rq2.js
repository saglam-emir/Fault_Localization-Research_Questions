// rq2.js - RQ2 (Search-Space Reduction) page logic.
// Data source: web/data/rq2.json (direct rq2.csv -> JSON, one row per
// successfully-run buggy version).

let ALL_ROWS = [];
const state = { metric: 'space', sliceType: 'all', scope: 'overall', project: null };

const SLICE_FIELD = { all: 'union_all_slice', pass: 'union_passing_slice', fail: 'union_failing_slice' };
const SLICE_LABEL = { all: 'All Slice', pass: 'Passing Slice', fail: 'Failing Slice' };

function sum(rows, key) { return rows.reduce((s, r) => s + r[key], 0); }
function bugNum(id) { return parseInt(id, 10) || 0; }
function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function rowsForProject(p) { return ALL_ROWS.filter(r => r.project === p).sort((a, b) => bugNum(a.bug_id) - bugNum(b.bug_id)); }
function median(nums) {
  const s = [...nums].sort((a, b) => a - b);
  const mid = Math.floor(s.length / 2);
  return s.length % 2 ? s[mid] : (s[mid - 1] + s[mid]) / 2;
}

function colors() {
  const cs = getComputedStyle(document.documentElement);
  return {
    full: cs.getPropertyValue('--ink-faint').trim(),
    slice: cs.getPropertyValue('--accent').trim(),
    ratio: cs.getPropertyValue('--ok').trim(),
  };
}

function renderSummaryCards() {
  const ratios = ALL_ROWS.map(r => r.all_reduction_ratio);
  const cards = [
    { value: ALL_ROWS.length, label: 'Buggy Versions Analyzed' },
    { value: ratios.reduce((a, b) => a + b, 0) / ratios.length, label: 'Average Reduction Ratio', format: RQ.pct },
    { value: median(ratios), label: 'Median Reduction Ratio', format: RQ.pct },
    { value: Math.max(...ratios), label: 'Maximum Reduction Ratio', format: RQ.pct },
  ];
  RQ.renderStatCards(document.getElementById('rq2-cards'), cards);
}

function renderControls() {
  RQ.renderSegmented(document.getElementById('metric-seg'), [
    { value: 'space', label: 'Search Space' },
    { value: 'ratio', label: 'Reduction Ratio' },
  ], state.metric, v => { state.metric = v; update(); });

  RQ.renderSegmented(document.getElementById('slicetype-seg'), [
    { value: 'all', label: 'All Tests' },
    { value: 'pass', label: 'Passing Tests' },
    { value: 'fail', label: 'Failing Tests' },
  ], state.sliceType, v => { state.sliceType = v; update(); });

  RQ.renderSegmented(document.getElementById('scope-seg'), [
    { value: 'overall', label: 'Overall' },
    { value: 'project', label: 'By Project' },
    { value: 'bug', label: 'By Bug' },
  ], state.scope, v => {
    state.scope = v;
    if (v !== 'bug') state.project = null;
    update();
  });
}

function renderProjectSelect() {
  const wrap = document.getElementById('project-select-wrap');
  const projects = projectList();
  if (!state.project) state.project = projects[0];
  wrap.querySelector('.seg-select').innerHTML = projects.map(p =>
    `<option value="${p}" ${p === state.project ? 'selected' : ''}>${p}</option>`).join('');
}

function goToBugScope(project) {
  state.scope = 'bug';
  state.project = project;
  update();
}

// Which bug's detail panel is open, if any - the one "place" this page has
// (Metric/Slice Type/Scope stay filters, not navigation - see navSnapshot).
let currentBugKey = null;

function navSnapshot() { return { bugKey: currentBugKey }; }
function restoreNav(s) {
  const key = s && s.bugKey;
  if (key) { showBugDetail(key, false); return; }
  currentBugKey = null;
  document.getElementById('bug-detail').hidden = true;
}

function showBugDetail(key, push = true) {
  const [project, bugId] = splitKey(key);
  const row = ALL_ROWS.find(r => r.project === project && r.bug_id === bugId);
  const panel = document.getElementById('bug-detail');
  if (!row) { panel.hidden = true; currentBugKey = null; return; }
  panel.hidden = false;
  currentBugKey = key;
  panel.querySelector('h4').textContent = `${row.project} / ${row.bug_id}`;
  panel.querySelector('.bug-detail-grid').innerHTML = `
    <div><div class="k">Full Execution Size</div><div class="v">${RQ.fmt.format(row.full_execution_size)}</div></div>
    <div><div class="k">Passing Slice</div><div class="v">${RQ.fmt.format(row.union_passing_slice)}</div></div>
    <div><div class="k">Failing Slice</div><div class="v">${RQ.fmt.format(row.union_failing_slice)}</div></div>
    <div><div class="k">All Slice</div><div class="v">${RQ.fmt.format(row.union_all_slice)}</div></div>
    <div><div class="k">Reduction Ratio</div><div class="v">${RQ.pct(row.all_reduction_ratio)}</div></div>
  `;
  if (push) RQ.pushNav(navSnapshot());
}
function splitKey(key) {
  const idx = key.lastIndexOf('_');
  return [key.slice(0, idx), key.slice(idx + 1)];
}

function setNote(html) {
  const note = document.getElementById('rq2-note');
  if (!html) { note.hidden = true; return; }
  note.hidden = false;
  document.getElementById('rq2-note-text').innerHTML = html;
}

function update() {
  renderControls();
  document.getElementById('slice-type-wrap').hidden = state.metric !== 'space';
  document.getElementById('project-select-wrap').hidden = state.scope !== 'bug';
  document.getElementById('bug-detail').hidden = true;
  currentBugKey = null;
  if (state.scope === 'bug') renderProjectSelect();

  const c = colors();
  const chartEl = document.getElementById('rq2-chart');

  if (state.metric === 'space') {
    renderSearchSpace(chartEl, c);
  } else {
    renderReductionRatio(chartEl, c);
  }
}

function renderSearchSpace(chartEl, c) {
  const sliceKey = SLICE_FIELD[state.sliceType];
  const sliceLabel = SLICE_LABEL[state.sliceType];
  setNote(null);

  if (state.scope === 'overall') {
    RQ.renderComparisonBars(chartEl, [
      { label: 'Full Execution Space', value: sum(ALL_ROWS, 'full_execution_size'), color: c.full },
      { label: sliceLabel, value: sum(ALL_ROWS, sliceKey), color: c.slice },
    ]);
    return;
  }

  if (state.scope === 'project') {
    const projects = projectList();
    const series = [
      { name: 'Full Execution', color: c.full, values: projects.map(p => sum(rowsForProject(p), 'full_execution_size')) },
      { name: sliceLabel, color: c.slice, values: projects.map(p => sum(rowsForProject(p), sliceKey)) },
    ];
    const order = projects.map((_, i) => i).sort((a, b) => series[0].values[b] - series[0].values[a]);
    const sortedProjects = order.map(i => projects[i]);
    const sortedSeries = series.map(s => ({ ...s, values: order.map(i => s.values[i]) }));
    RQ.renderGroupedBarList(chartEl, {
      categories: sortedProjects, series: sortedSeries, onCategoryClick: goToBugScope,
      extra: (_, i) => {
        const full = sortedSeries[0].values[i], sliced = sortedSeries[1].values[i];
        return `${RQ.pct(full ? 1 - sliced / full : 0)} reduction`;
      },
    });
    return;
  }

  // scope === 'bug'
  const rows = rowsForProject(state.project);
  const keys = rows.map(r => `${r.project}_${r.bug_id}`);
  const series = [
    { name: 'Full Execution', color: c.full, values: rows.map(r => r.full_execution_size) },
    { name: sliceLabel, color: c.slice, values: rows.map(r => r[sliceKey]) },
  ];
  RQ.renderGroupedBarList(chartEl, {
    categories: rows.map(r => r.bug_id), keys, series, onCategoryClick: showBugDetail,
    extra: (_, i) => {
      const full = series[0].values[i], sliced = series[1].values[i];
      return `${RQ.pct(full ? 1 - sliced / full : 0)} reduction`;
    },
  });
}

function reductionBuckets(rows) {
  const buckets = Array.from({ length: 10 }, (_, i) => ({ label: `${i * 10}–${i * 10 + 10}%`, count: 0 }));
  rows.forEach(r => {
    let idx = Math.floor(r.all_reduction_ratio * 10);
    if (idx > 9) idx = 9;
    if (idx < 0) idx = 0;
    buckets[idx].count++;
  });
  return buckets;
}

function renderReductionRatio(chartEl, c) {
  if (state.scope === 'overall') {
    const buckets = reductionBuckets(ALL_ROWS);
    RQ.renderStackedBarList(chartEl, {
      categories: buckets.map(b => b.label),
      series: [{ name: 'Buggy Versions', color: c.ratio, values: buckets.map(b => b.count) }],
    });
    setNote('Distribution of <code>all_reduction_ratio</code> across all analyzed buggy versions, bucketed in 10-point-percentage bins. ' +
      'A ratio of 100% means the slice was empty (0 statements) for that bug - slicing found nothing to rank, which is a distinct outcome from a small-but-nonempty slice and is worth distinguishing when reading this distribution.');
    return;
  }

  if (state.scope === 'project') {
    const projects = projectList();
    const values = projects.map(p => {
      const rs = rowsForProject(p);
      return sum(rs, 'all_reduction_ratio') / rs.length;
    });
    const order = projects.map((_, i) => i).sort((a, b) => values[b] - values[a]);
    RQ.renderStackedBarList(chartEl, {
      categories: order.map(i => projects[i]),
      series: [{ name: 'Avg Reduction Ratio', color: c.ratio, values: order.map(i => values[i]) }],
      formatValue: RQ.pct,
      onCategoryClick: goToBugScope,
    });
    setNote(null);
    return;
  }

  // scope === 'bug'
  const rows = rowsForProject(state.project);
  const keys = rows.map(r => `${r.project}_${r.bug_id}`);
  RQ.renderStackedBarList(chartEl, {
    categories: rows.map(r => r.bug_id),
    keys,
    series: [{ name: 'Reduction Ratio', color: c.ratio, values: rows.map(r => r.all_reduction_ratio) }],
    formatValue: RQ.pct,
    onCategoryClick: showBugDetail,
  });
  setNote(null);
}

function renderTable() {
  RQ.createDataTable(document.getElementById('rq2-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'full_execution_size', label: 'Full Execution', numeric: true },
      { key: 'passing_TC_size', label: 'Passing TC Size', numeric: true },
      { key: 'failing_TC_size', label: 'Failing TC Size', numeric: true },
      { key: 'union_passing_slice', label: 'Passing Slice', numeric: true },
      { key: 'union_failing_slice', label: 'Failing Slice', numeric: true },
      { key: 'union_all_slice', label: 'All Slice', numeric: true },
      { key: 'all_reduction_ratio', label: 'Reduction Ratio', numeric: true, format: RQ.pct },
    ],
    rows: ALL_ROWS,
    searchKeys: ['project', 'bug_id'],
    filterKey: 'project',
    pageSize: 25,
  });
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq2.json').then(r => r.json());
    renderSummaryCards();
    document.getElementById('project-select-wrap').querySelector('.seg-select')
      .addEventListener('change', e => { state.project = e.target.value; update(); });
    update();
    renderTable();
    RQ.initNavHistory(navSnapshot, restoreNav);
  } catch (err) {
    console.error('RQ2 verisi yüklenemedi:', err);
    document.getElementById('rq2-chart').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
