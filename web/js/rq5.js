// rq5.js - RQ5 (Fault Localization Ranking) page logic.
// Data source: web/data/rq5.json (one row per ground-truth fault LINE).
// Central interaction: DIFF (0-3) + Approach, driving a connected
// Overall -> Project -> Buggy Version drill-down.

let ALL_ROWS = [];
const state = { diff: 0, approach: 'slice', level: 'overall', project: null, bug: null };

const DIFF_EXPLAIN = {
  0: 'Exact line match only - the ranking\'s best hit must be the true fault line itself.',
  1: 'Exact match, or the nearest same-file ranked statement is within 1 line of the true fault line.',
  2: 'Exact match, or within 2 lines of the true fault line.',
  3: 'Exact match, or within 3 lines of the true fault line.',
};

function isUnanswerable(r) { return !!r.unanswerable_reason; }

// Single source of truth for "is this a hit at the selected diff" - follows
// the project's existing rq5.csv definitions, nothing new invented:
// diff=0 requires rank_best_* itself; diff=N>0 additionally accepts
// nearest_line_diff_* within N lines (0 there already means an exact hit).
function hitAt(row, kind, diff) {
  const rankKey = kind === 'trace' ? 'rank_best_trace' : 'rank_best_slice';
  if (row[rankKey] != null) return true;
  if (diff === 0) return false;
  const d = kind === 'trace' ? row.nearest_line_diff_trace : row.nearest_line_diff_slice;
  return d != null && Math.abs(d) <= diff;
}

// SUCCESS / PIPELINE GAP / PROJECT-CAUSED / OTHER MISS, from the row's own
// fields - not re-derived or newly invented. unanswerable_reason is checked
// directly (not via diff_reason_*'s "project_test_scenario") because
// diff_reason_* reports "succeed" whenever ANY line in that file has a
// nearby ranked candidate - true even for an unanswerable fault line, as
// long as something else nearby in the same file got ranked (see
// rq_writers._write_rq5's docstring: diff_reason_* only ever says
// project_test_scenario when the file is entirely absent from that
// ranking's universe, which is the less common case). unanswerable_reason
// is the one field that always reflects this specific fault line's own
// answerability, so it takes priority here.
function classify(row, kind, diff) {
  if (hitAt(row, kind, diff)) return 'SUCCESS';
  if (isUnanswerable(row)) return 'PROJECT-CAUSED';
  const reason = kind === 'trace' ? row.diff_reason_trace : row.diff_reason_slice;
  if (reason === 'pipeline_gap') return 'PIPELINE GAP';
  return 'OTHER MISS';
}

function rate(rows, kind, diff) { return rows.length ? rows.filter(r => hitAt(r, kind, diff)).length / rows.length : 0; }
function projectList() { return [...new Set(ALL_ROWS.map(r => r.project))].sort(); }
function rowsForProject(p) { return ALL_ROWS.filter(r => r.project === p); }
function bugNum(id) { return parseInt(id, 10) || 0; }
function bugsInProject(p) { return [...new Set(rowsForProject(p).map(r => r.bug_id))].sort((a, b) => bugNum(a) - bugNum(b)); }
function rowsForBug(p, b) { return ALL_ROWS.filter(r => r.project === p && r.bug_id === b); }

function currentRows() {
  if (state.level === 'bug') return rowsForBug(state.project, state.bug);
  if (state.level === 'project') return rowsForProject(state.project);
  return ALL_ROWS;
}

function colors() {
  const cs = getComputedStyle(document.documentElement);
  return { trace: cs.getPropertyValue('--ink-faint').trim(), slice: cs.getPropertyValue('--accent').trim(), ok: cs.getPropertyValue('--ok').trim() };
}

// ------------------------------------------------------------ DIFF hero --
function renderDiffControl() {
  const el = document.getElementById('diff-seg');
  el.innerHTML = [0, 1, 2, 3].map(d => `<button type="button" class="${d === state.diff ? 'active' : ''}" data-value="${d}">${d}</button>`).join('');
  el.querySelectorAll('button').forEach(btn => btn.addEventListener('click', () => { state.diff = parseInt(btn.dataset.value, 10); renderAll(); }));
  document.getElementById('diff-explain').textContent = DIFF_EXPLAIN[state.diff];
}

// ------------------------------------------------------------ breadcrumb --
function renderBreadcrumb() {
  const parts = [`<a data-level="overall">Overall</a>`];
  if (state.project) parts.push(`<span class="sep">›</span>` + (state.level === 'project' ? `<span class="current">${state.project}</span>` : `<a data-level="project">${state.project}</a>`));
  if (state.bug) parts.push(`<span class="sep">›</span><span class="current">${state.project}_${state.bug}</span>`);
  const el = document.getElementById('breadcrumb');
  el.innerHTML = parts.join('');
  el.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    if (a.dataset.level === 'overall') { state.level = 'overall'; state.project = null; state.bug = null; }
    else if (a.dataset.level === 'project') { state.level = 'project'; state.bug = null; }
    renderAll();
    RQ.pushNav(navSnapshot());
  }));
}

// The level/project/bug "place" - not the DIFF/approach filters, which
// stay out of history so Back undoes drill-down, not every control click.
function navSnapshot() { return { level: state.level, project: state.project, bug: state.bug }; }
function restoreNav(s) {
  const snap = s || { level: 'overall', project: null, bug: null };
  state.level = snap.level; state.project = snap.project; state.bug = snap.bug;
  renderAll();
}

// -------------------------------------------------------- summary cards --
function renderSummaryCards() {
  const rows = currentRows();
  const answerable = rows.filter(r => !isUnanswerable(r));
  const cards = [
    { value: rows.length, label: 'Fault Lines (current scope)' },
    { value: answerable.length, label: 'Answerable' },
    { value: rate(answerable, 'trace', state.diff), label: `Trace Success @ diff=${state.diff}`, format: RQ.pct },
    { value: rate(answerable, 'slice', state.diff), label: `Slice Success @ diff=${state.diff}`, format: RQ.pct },
  ];
  RQ.renderStatCards(document.getElementById('rq5-cards'), cards);
}

// ------------------------------------------------------------ main chart --
function renderApproachControl() {
  RQ.renderSegmented(document.getElementById('approach-seg'), [
    { value: 'slice', label: 'Slice' }, { value: 'trace', label: 'Trace' }, { value: 'compare', label: 'Compare' },
  ], state.approach, v => { state.approach = v; renderMainChart(); renderCurve(); });
}

// A category (project or bug) with zero answerable fault lines shows a
// flat 0.0% bar that is visually indistinguishable from "the technique
// found nothing" - the two mean very different things (see Methodology's
// Answerability section). This marks those bars so the difference is
// visible instead of silently looking like a missing/failed result.
function annotateNoAnswerable(chartEl, keys, countFn) {
  keys.forEach(key => {
    if (countFn(key) > 0) return;
    const row = chartEl.querySelector(`[data-key="${key}"]`);
    if (!row) return;
    row.classList.add('no-answerable');
    const valueEl = row.querySelector('.bar-value');
    if (valueEl && !row.querySelector('.no-data-note')) {
      valueEl.insertAdjacentHTML('afterend', '<span class="no-data-note">no answerable fault lines</span>');
    }
  });
}

function renderMainChart() {
  const c = colors();
  const eyebrow = document.getElementById('main-chart-eyebrow');
  const title = document.getElementById('main-chart-title');
  const desc = document.getElementById('main-chart-desc');
  const chartEl = document.getElementById('rq5-main-chart');

  if (state.level === 'overall') {
    eyebrow.textContent = 'Overall + Project'; title.textContent = 'Success Rate';
    desc.textContent = 'The first bar is the overall rate across every project; click any project bar to drill down.';
    const projects = projectList();
    const cats = ['Overall', ...projects];
    const answerableRows = p => (p === 'Overall' ? ALL_ROWS : rowsForProject(p)).filter(r => !isUnanswerable(r));
    if (state.approach === 'compare') {
      const series = [
        { name: 'Trace', color: c.trace, values: cats.map(p => rate(answerableRows(p), 'trace', state.diff)) },
        { name: 'Slice', color: c.slice, values: cats.map(p => rate(answerableRows(p), 'slice', state.diff)) },
      ];
      RQ.renderGroupedBarList(chartEl, { categories: cats, series, formatValue: RQ.pct, onCategoryClick: goToProject });
    } else {
      const values = cats.map(p => rate(answerableRows(p), state.approach, state.diff));
      RQ.renderStackedBarList(chartEl, {
        categories: cats,
        series: [{ name: state.approach === 'trace' ? 'Trace' : 'Slice', color: state.approach === 'trace' ? c.trace : c.slice, values }],
        formatValue: RQ.pct, onCategoryClick: goToProject,
      });
    }
    annotateNoAnswerable(chartEl, cats, p => answerableRows(p).length);
  } else if (state.level === 'project') {
    eyebrow.textContent = state.project; title.textContent = 'Buggy-Version Success Rate';
    desc.textContent = 'Click a buggy version for its fault-line-level detail.';
    const bugs = bugsInProject(state.project);
    const answerableFor = b => rowsForBug(state.project, b).filter(r => !isUnanswerable(r));
    if (state.approach === 'compare') {
      const series = [
        { name: 'Trace', color: c.trace, values: bugs.map(b => rate(answerableFor(b), 'trace', state.diff)) },
        { name: 'Slice', color: c.slice, values: bugs.map(b => rate(answerableFor(b), 'slice', state.diff)) },
      ];
      RQ.renderGroupedBarList(chartEl, { categories: bugs, series, formatValue: RQ.pct, onCategoryClick: b => goToBug(state.project, b) });
    } else {
      const values = bugs.map(b => rate(answerableFor(b), state.approach, state.diff));
      RQ.renderStackedBarList(chartEl, {
        categories: bugs,
        series: [{ name: state.approach === 'trace' ? 'Trace' : 'Slice', color: state.approach === 'trace' ? c.trace : c.slice, values }],
        formatValue: RQ.pct, onCategoryClick: b => goToBug(state.project, b),
      });
    }
    annotateNoAnswerable(chartEl, bugs, b => answerableFor(b).length);
  } else {
    eyebrow.textContent = `${state.project} / ${state.bug}`; title.textContent = 'Fault Lines in This Buggy Version';
    desc.textContent = 'See the full detail panel below for a per-line Trace/Slice comparison.';
    chartEl.innerHTML = `<p class="muted" style="font-size:13.5px">${currentRows().length} fault line(s) in this buggy version - see the detail panel below.</p>`;
  }
}

// Scope-level banner: when every ground-truth fault line in the CURRENT
// drill scope is unanswerable, every rate on this page reads 0.0% for a
// reason that has nothing to do with ranking quality - say so plainly
// instead of leaving a bare 0.0% to be misread as "no result"/"failure".
function renderUnanswerableNote() {
  const el = document.getElementById('rq5-unanswerable-note');
  const rows = currentRows();
  const answerable = rows.filter(r => !isUnanswerable(r));
  if (rows.length === 0 || answerable.length > 0) { el.hidden = true; return; }
  el.hidden = false;
  const scopeLabel = state.level === 'bug' ? `${state.project}/${state.bug}` : state.level === 'project' ? state.project : 'this scope';
  el.innerHTML = `
    <p class="rq-note" style="max-width:none;margin-top:16px">
      <span class="ic">ⓘ</span>
      <span><strong>None of the ${rows.length} ground-truth fault line(s) in ${scopeLabel} are answerable</strong> - every
        one is flagged in <code>answerability_bySlicers.csv</code> (dead code, or a live line no test in this run's
        suite ever executed). The 0.0% success rate shown below reflects an empty answerable set, not a ranking
        failure - see <a href="methodology.html#tolerance" style="color:var(--accent)">Methodology → Answerability</a>.</span>
    </p>`;
}

function goToProject(p) { if (p === 'Overall') return; state.level = 'project'; state.project = p; state.bug = null; renderAll(); RQ.pushNav(navSnapshot()); }
function goToBug(p, b) { state.level = 'bug'; state.project = p; state.bug = b; renderAll(); RQ.pushNav(navSnapshot()); }

// --------------------------------------------------------- diff progression
function renderCurve() {
  const rows = currentRows().filter(r => !isUnanswerable(r));
  const c = colors();
  const tolerances = [0, 1, 2, 3];
  document.getElementById('progression-title').textContent =
    state.level === 'overall' ? 'Success Rate: 0 → 1 → 2 → 3 (Overall)'
      : state.level === 'project' ? `Success Rate: 0 → 1 → 2 → 3 (${state.project})`
        : `Success Rate: 0 → 1 → 2 → 3 (${state.project}/${state.bug})`;
  const series = [];
  if (state.approach !== 'slice') series.push({ name: 'Trace', color: c.trace, values: tolerances.map(t => rate(rows, 'trace', t)) });
  if (state.approach !== 'trace') series.push({ name: 'Slice', color: c.slice, values: tolerances.map(t => rate(rows, 'slice', t)) });
  RQ.renderLineChart(document.getElementById('rq5-curve'), { xLabels: tolerances.map(String), series, formatY: RQ.pct });
}

// -------------------------------------------------------------- status ----
function renderStatusBoxes() {
  const rows = currentRows();
  ['trace', 'slice'].forEach(kind => {
    const counts = { 'SUCCESS': 0, 'PIPELINE GAP': 0, 'PROJECT-CAUSED': 0, 'OTHER MISS': 0 };
    rows.forEach(r => { counts[classify(r, kind, state.diff)]++; });
    const boxes = [
      { cls: 'success', lbl: 'SUCCESS', n: counts['SUCCESS'] },
      { cls: 'gap', lbl: 'PIPELINE GAP', n: counts['PIPELINE GAP'] },
      { cls: 'project', lbl: 'PROJECT-CAUSED', n: counts['PROJECT-CAUSED'] },
      { cls: 'other', lbl: 'OTHER MISS', n: counts['OTHER MISS'] },
    ];
    document.getElementById(`status-boxes-${kind}`).innerHTML = boxes.map(b => `
      <div class="status-box ${b.cls}"><div class="lbl">${b.lbl}</div><div class="n">${RQ.fmt.format(b.n)}</div></div>`).join('');
  });
}

// --------------------------------------------------------- tolerance vis --
function renderToleranceVis() {
  const d = state.diff;
  const positions = [-3, -2, -1, 0, 1, 2, 3];
  const inRange = p => Math.abs(p) <= d;
  const ticks = positions.map(p => `
    <div class="tol-tick ${inRange(p) ? 'in-range' : ''} ${p === 0 ? 'zero' : ''}" style="left:${((p + 3) / 6 * 100).toFixed(1)}%">
      <div class="tol-dot"></div>
      <div class="tol-tick-label">${p === 0 ? 'Fault Line' : (p > 0 ? '+' + p : p)}</div>
    </div>`).join('');
  document.getElementById('rq5-tolerance-vis').innerHTML = `
    <div class="tol-vis">
      <div class="tol-range" style="left:${((3 - d) / 6 * 100).toFixed(1)}%;width:${(d / 3 * 50).toFixed(1)}%"></div>
      <div class="tol-range" style="left:50%;width:${(d / 3 * 50).toFixed(1)}%"></div>
      <div class="tol-line"></div>
      ${ticks}
    </div>
    <p class="muted" style="font-size:12.5px;margin-top:34px;text-align:center">
      DIFF only widens the accepted tolerance band around the true fault line - it never moves the prediction itself.</p>`;
}

// -------------------------------------------------------------- detail ----
function showBugDetailFromMain() {
  const panel = document.getElementById('bug-detail');
  if (state.level !== 'bug') { panel.hidden = true; return; }
  const rows = currentRows();
  panel.hidden = false;
  panel.querySelector('h4').textContent = `${state.project} / ${state.bug} — ${rows.length} fault line(s), DIFF = ${state.diff}`;
  panel.querySelector('#bug-detail-fault-lines').innerHTML = rows.map(r => {
    const tCls = classify(r, 'trace', state.diff), sCls = classify(r, 'slice', state.diff);
    return `
      <div class="fault-line-block">
        <div class="fault-line-heading">${r.file_name}:${r.line_no}</div>
        <div class="trace-slice-compare">
          <div class="ts-col">
            <div class="ts-col-label">TRACE</div>
            <div class="ts-row"><span>Rank</span><strong>${r.rank_best_trace ?? '—'}</strong></div>
            <div class="ts-row"><span>Line Diff</span><strong>${r.nearest_line_diff_trace ?? '—'}</strong></div>
            <div class="ts-row"><span>Status</span><span class="cat-badge ${tCls === 'SUCCESS' ? 'best' : tCls === 'PIPELINE GAP' ? 'neither' : 'trace'}">${tCls}</span></div>
          </div>
          <div class="ts-col">
            <div class="ts-col-label">SLICE</div>
            <div class="ts-row"><span>Rank</span><strong>${r.rank_best_slice ?? '—'}</strong></div>
            <div class="ts-row"><span>Line Diff</span><strong>${r.nearest_line_diff_slice ?? '—'}</strong></div>
            <div class="ts-row"><span>Status</span><span class="cat-badge ${sCls === 'SUCCESS' ? 'best' : sCls === 'PIPELINE GAP' ? 'neither' : 'trace'}">${sCls}</span></div>
          </div>
        </div>
      </div>`;
  }).join('');
  panel.scrollIntoView?.({ behavior: 'smooth', block: 'nearest' });
}

// -------------------------------------------------------------- table -----
function fmtCell(v) { return v == null ? '—' : v; }
function renderTable() {
  RQ.createDataTable(document.getElementById('rq5-table'), {
    columns: [
      { key: 'project', label: 'Project' },
      { key: 'bug_id', label: 'Bug ID' },
      { key: 'file_name', label: 'File' },
      { key: 'line_no', label: 'Actual Line', numeric: true },
      { key: 'rank_best_trace', label: 'Trace Rank', numeric: true, format: fmtCell },
      { key: 'nearest_line_diff_trace', label: 'Trace Line Diff', numeric: true, format: fmtCell },
      { key: 'trace_status', label: 'Trace Status', format: v => `<span class="cat-badge ${v === 'SUCCESS' ? 'best' : v === 'PIPELINE GAP' ? 'neither' : 'trace'}">${v}</span>` },
      { key: 'rank_best_slice', label: 'Slice Rank', numeric: true, format: fmtCell },
      { key: 'nearest_line_diff_slice', label: 'Slice Line Diff', numeric: true, format: fmtCell },
      { key: 'slice_status', label: 'Slice Status', format: v => `<span class="cat-badge ${v === 'SUCCESS' ? 'best' : v === 'PIPELINE GAP' ? 'neither' : 'trace'}">${v}</span>` },
    ],
    rows: tableRows(),
    searchKeys: ['project', 'bug_id', 'file_name'],
    filterKey: 'project',
    pageSize: 25,
  });
}
function tableRows() {
  return ALL_ROWS.map(r => ({ ...r, trace_status: classify(r, 'trace', state.diff), slice_status: classify(r, 'slice', state.diff) }));
}
function refreshTable() {
  // rebuild in place (columns/filter unchanged, only row content - simplest correct approach: re-run createDataTable)
  renderTable();
}

// --------------------------------------------------------------- root -----
function renderAll() {
  renderDiffControl();
  renderBreadcrumb();
  renderSummaryCards();
  renderUnanswerableNote();
  renderMainChart();
  renderCurve();
  renderStatusBoxes();
  renderToleranceVis();
  showBugDetailFromMain();
  refreshTable();
}

async function init() {
  try {
    ALL_ROWS = await fetch('data/rq5.json').then(r => r.json());
    renderApproachControl();
    renderAll();
    RQ.initNavHistory(navSnapshot, restoreNav);
  } catch (err) {
    console.error('RQ5 verisi yüklenemedi:', err);
    document.getElementById('rq5-main-chart').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
