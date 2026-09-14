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

// Sayı sayaç animasyonu - 0'dan hedef degere ~1.1s'de, ease-out ile sayar.
function animateCount(el, target, { decimals = 0, duration = 1100 } = {}) {
  const start = performance.now();
  const easeOut = t => 1 - Math.pow(1 - t, 3);
  function tick(now) {
    const p = Math.min(1, (now - start) / duration);
    const value = target * easeOut(p);
    el.textContent = decimals > 0 ? value.toFixed(decimals) : fmt.format(Math.round(value));
    if (p < 1) requestAnimationFrame(tick);
    else el.textContent = decimals > 0 ? target.toFixed(decimals) : fmt.format(target);
  }
  requestAnimationFrame(tick);
}

function renderStats(summary) {
  const days = parseFloat(secondsToMachineDays(summary.total_elapsed_seconds));
  const values = {
    total_projects: summary.total_projects,
    total_buggy_versions: summary.total_buggy_versions,
    total_test_cases: summary.total_test_cases,
    machine_days: days,
  };
  document.querySelectorAll('[data-stat]').forEach(el => {
    const key = el.dataset.stat;
    const decimals = parseInt(el.dataset.decimals || '0', 10);
    animateCount(el, values[key], { decimals });
  });
  const sub = document.getElementById('stat-runtime-sub');
  if (sub) sub.textContent = `${fmt.format(summary.total_elapsed_seconds)}s · ~${secondsToHours(summary.total_elapsed_seconds)}h`;
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
    const sub = document.getElementById('stat-runtime-sub');
    if (sub) sub.textContent = 'Veri yüklenirken bir sorun oluştu.';
  }
}

document.addEventListener('DOMContentLoaded', init);
