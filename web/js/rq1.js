// rq1.js - RQ1 (Test Suite Characteristics) page logic.
// Data source: web/data/rq1.json (one row per successfully-run buggy
// version, generated from rq1.csv - see resQ_scripts/build_site_data.py).

let ALL_ROWS = [];
const state = { metric: 'tc', scope: 'overall', project: null };

function sum(rows, key) { return rows.reduce((s, r) => s + r[key], 0); }
function bugNum(id) { return parseInt(id, 10) || 0; }
function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function rowsForProject(p) { return ALL_ROWS.filter(r => r.project === p).sort((a, b) => bugNum(a.bug_id) - bugNum(b.bug_id)); }

function colors() {
  const cs = getComputedStyle(document.documentElement);
  return {
    ok: cs.getPropertyValue('--ok').trim(),
    fail: cs.getPropertyValue('--fail').trim(),
    accent: cs.getPropertyValue('--accent').trim(),
    neutral: '#7c8a9a',
  };
}

function metricSeriesDef(c) {
  if (state.metric === 'tc') {
    return [{ key: 'pass_tc', name: 'Passing', color: c.ok }, { key: 'fail_tc', name: 'Failing', color: c.fail }];
  }
  if (state.metric === 'assert') {
    return [{ key: 'pass_assert', name: 'Passing', color: c.ok }, { key: 'fail_assert', name: 'Failing', color: c.fail }];
  }
  return [
    { key: 'fail_tc', name: 'Fail_TC', color: c.fail },
    { key: 'fail_assert', name: 'Fail_Assert', color: c.accent },
    { key: 'uncaught_exception', name: 'Uncaught_Exception', color: c.neutral },
  ];
}

function renderSummaryCards() {
  const withUncaught = ALL_ROWS.filter(r => r.uncaught_exception > 0).length;
  const cards = [
    { value: ALL_ROWS.length, label: 'Buggy Versions Analyzed' },
    { value: sum(ALL_ROWS, 'pass_tc') + sum(ALL_ROWS, 'fail_tc'), label: 'Total Test Cases' },
    { value: sum(ALL_ROWS, 'pass_tc'), label: 'Passing Test Cases' },
    { value: sum(ALL_ROWS, 'fail_tc'), label: 'Failing Test Cases' },
    { value: withUncaught, label: 'With Uncaught Exceptions' },
  ];
  RQ.renderStatCards(document.getElementById('rq1-cards'), cards);
}

function renderControls() {
  RQ.renderSegmented(document.getElementById('metric-seg'), [
    { value: 'tc', label: 'Test Cases' },
    { value: 'assert', label: 'Assertions' },
    { value: 'failure', label: 'Failure Analysis' },
  ], state.metric, v => { state.metric = v; update(); });

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
// (Metric/Scope stay filters, not navigation - see navSnapshot below).
let currentBugKey = null;

function navSnapshot() { return { bugKey: currentBugKey }; }
function restoreNav(s) {
  const key = s && s.bugKey;
  if (key) { showBugDetail(key, false); return; }
  currentBugKey = null;
  document.getElementById('bug-detail').hidden = true;
}

function showBugDetail(name, push = true) {
  const row = ALL_ROWS.find(r => `${r.project}_${r.bug_id}` === name);
  const panel = document.getElementById('bug-detail');
  if (!row) { panel.hidden = true; currentBugKey = null; return; }
  panel.hidden = false;
  currentBugKey = name;
  panel.querySelector('h4').textContent = `${row.project} / ${row.bug_id}`;
  panel.querySelector('.bug-detail-grid').innerHTML = `
    <div><div class="k">Passing Tests</div><div class="v">${row.pass_tc}</div></div>
    <div><div class="k">Failing Tests</div><div class="v">${row.fail_tc}</div></div>
    <div><div class="k">Passing Assertions</div><div class="v">${row.pass_assert}</div></div>
    <div><div class="k">Failing Assertions</div><div class="v">${row.fail_assert}</div></div>
    <div><div class="k">Uncaught Exceptions</div><div class="v">${row.uncaught_exception}</div></div>
  `;
  if (push) RQ.pushNav(navSnapshot());
}

function update() {
  renderControls(); // re-render so segmented "active" state reflects programmatic changes (e.g. drill-down clicks)
  document.getElementById('project-select-wrap').hidden = state.scope !== 'bug';
  document.getElementById('bug-detail').hidden = true;
  currentBugKey = null;
  document.getElementById('rq1-note').hidden = state.metric !== 'failure';

  if (state.scope === 'bug') renderProjectSelect();

  const c = colors();
  const defs = metricSeriesDef(c);
  const chartEl = document.getElementById('rq1-chart');

  if (state.scope === 'overall') {
    const items = defs.map(d => ({ label: d.name, value: sum(ALL_ROWS, d.key), color: d.color }));
    RQ.renderComparisonBars(chartEl, items);
    return;
  }

  if (state.scope === 'project') {
    const projects = projectList();
    const series = defs.map(d => ({ name: d.name, color: d.color, values: projects.map(p => sum(rowsForProject(p), d.key)) }));
    const totals = projects.map((_, i) => series.reduce((s, ser) => s + ser.values[i], 0));
    const order = projects.map((_, i) => i).sort((a, b) => totals[b] - totals[a]);
    const sortedProjects = order.map(i => projects[i]);
    const sortedSeries = series.map(s => ({ ...s, values: order.map(i => s.values[i]) }));
    const onClick = p => goToBugScope(p);
    if (state.metric === 'failure') {
      RQ.renderGroupedBarList(chartEl, { categories: sortedProjects, series: sortedSeries, onCategoryClick: onClick });
    } else {
      RQ.renderStackedBarList(chartEl, { categories: sortedProjects, series: sortedSeries, onCategoryClick: onClick });
    }
    return;
  }

  // scope === 'bug'
  const rows = rowsForProject(state.project);
  const cats = rows.map(r => r.bug_id);
  const keys = rows.map(r => `${r.project}_${r.bug_id}`);
  const series = defs.map(d => ({ name: d.name, color: d.color, values: rows.map(r => r[d.key]) }));
  if (state.metric === 'failure') {
    RQ.renderGroupedBarList(chartEl, { categories: cats, series, keys, onCategoryClick: showBugDetail });
  } else {
    RQ.renderStackedBarList(chartEl, { categories: cats, series, keys, onCategoryClick: showBugDetail });
  }
}

function renderTable() {
  RQ.createDataTable(document.getElementById('rq1-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'pass_tc', label: 'Pass TC', numeric: true },
      { key: 'fail_tc', label: 'Fail TC', numeric: true },
      { key: 'pass_assert', label: 'Pass Assert', numeric: true },
      { key: 'fail_assert', label: 'Fail Assert', numeric: true },
      { key: 'uncaught_exception', label: 'Uncaught Exception', numeric: true },
    ],
    rows: ALL_ROWS,
    searchKeys: ['project', 'bug_id'],
    filterKey: 'project',
    pageSize: 25,
  });
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq1.json').then(r => r.json());
    renderSummaryCards();
    document.getElementById('project-select-wrap').querySelector('.seg-select')
      .addEventListener('change', e => { state.project = e.target.value; update(); });
    update();
    renderTable();
    RQ.initNavHistory(navSnapshot, restoreNav);
  } catch (err) {
    console.error('RQ1 verisi yüklenemedi:', err);
    document.getElementById('rq1-chart').innerHTML =
      `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
