// home.js - Home / Overview page. Fetches web/data/*.json (generated from
// resQ_outputs_all by resQ_scripts/build_site_data.py) and renders every
// data-driven section. No experimental numbers are hard-coded here.

const fmt = new Intl.NumberFormat('en-US');

function secondsToMachineDays(s) {
  return (s / 86400).toFixed(1);
}
function secondsToHours(s) {
  return fmt.format(Math.round(s / 3600));
}

async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`${path}: HTTP ${res.status}`);
  return res.json();
}

function renderStats(summary) {
  const el = document.getElementById('stats-grid');
  const days = secondsToMachineDays(summary.total_elapsed_seconds);
  const cards = [
    { n: summary.total_projects, l: 'Defects4J Projects' },
    { n: fmt.format(summary.total_buggy_versions), l: 'Buggy Versions' },
    { n: fmt.format(summary.total_test_cases), l: 'Test Cases' },
    { n: fmt.format(summary.total_fail_tc), l: 'Failing Test Cases' },
    { n: `${days}`, l: 'Machine-Days Runtime', sub: `${fmt.format(summary.total_elapsed_seconds)}s · ~${secondsToHours(summary.total_elapsed_seconds)}h` },
  ];
  el.innerHTML = cards.map(c => `
    <div class="stat-card">
      <div class="n">${c.n}</div>
      <div class="l">${c.l}</div>
      ${c.sub ? `<div class="sub" title="raw elapsed_s sum across all runs">${c.sub}</div>` : ''}
    </div>`).join('');
}

function renderInfo(meta) {
  const el = document.getElementById('info-panel');
  const rows = [
    ['Institution', meta.institution],
    ['Dataset', meta.dataset],
    ['Research Topic', meta.research_topic],
    ['Research Start', meta.research_start],
    ['Status', meta.status],
  ].filter(([, v]) => v);
  el.innerHTML = rows.map(([k, v]) => `
    <div class="info-item"><div class="k">${k}</div><div class="v">${v}</div></div>`).join('');
}

function renderProjectsPanel(summary) {
  document.getElementById('proj-count').textContent = summary.total_projects;
  document.getElementById('bug-count').textContent = fmt.format(summary.total_buggy_versions);

  const sorted = [...summary.projects].sort((a, b) => b.buggy_versions - a.buggy_versions);
  const max = sorted[0].buggy_versions;
  const el = document.getElementById('dist-chart');
  el.innerHTML = sorted.map(p => `
    <div class="dist-row">
      <div class="name">${p.project}</div>
      <div class="bar-track"><div class="bar-fill" style="width:${(p.buggy_versions / max * 100).toFixed(0)}%"></div></div>
      <div class="count">${p.buggy_versions}</div>
    </div>`).join('');
}

function renderReferences(refData) {
  const el = document.getElementById('ref-grid');
  if (!refData.references || refData.references.length === 0) {
    el.innerHTML = `<div class="ref-empty">References will be added here.</div>`;
    return;
  }
  el.innerHTML = refData.references.map(r => `
    <div class="ref-card">
      <div class="cat">${r.category || ''}</div>
      <h4>${r.title}</h4>
      <div class="authors">${r.authors || ''}</div>
      <div class="venue">${[r.venue, r.year].filter(Boolean).join(' · ')}</div>
    </div>`).join('');
}

async function init() {
  try {
    const [summary, meta, refs] = await Promise.all([
      loadJSON('data/summary.json'),
      loadJSON('data/metadata.json'),
      loadJSON('data/references.json'),
    ]);
    renderStats(summary);
    renderInfo(meta);
    renderProjectsPanel(summary);
    renderReferences(refs);
    if (meta.github_url) {
      document.querySelectorAll('.js-gh-link').forEach(a => a.href = meta.github_url);
    }
  } catch (err) {
    console.error('Veri yüklenemedi:', err);
    document.getElementById('stats-grid').innerHTML =
      `<div class="skeleton" style="padding:20px">Veri yüklenirken bir sorun oluştu.</div>`;
  }
}

document.addEventListener('DOMContentLoaded', init);
