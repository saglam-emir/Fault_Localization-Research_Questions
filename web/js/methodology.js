// methodology.js - Methodology page. Fetches web/data/*.json (generated
// from resQ_outputs_all by resQ_scripts/build_site_data.py) for the two
// data-driven bits of this otherwise-static page: the scope stat row and
// the data-provenance info panel. No experimental numbers are hard-coded.

const fmt = new Intl.NumberFormat('en-US');

async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`${path}: HTTP ${res.status}`);
  return res.json();
}

function renderScopeCards(summary) {
  const cards = [
    { value: summary.total_projects, label: 'Defects4J Projects' },
    { value: summary.total_buggy_versions, label: 'Buggy Versions' },
    { value: summary.total_test_cases, label: 'Test Cases' },
    { value: summary.total_ground_truth_fault_lines, label: 'Ground-Truth Fault Lines' },
  ];
  RQ.renderStatCards(document.getElementById('scope-cards'), cards);
}

function renderProvenance(summary, meta) {
  const rows = [
    ['Dataset', meta.dataset],
    ['Completed Buggy Versions', `${fmt.format(summary.total_ok)} / ${fmt.format(summary.total_buggy_versions)}`],
    ['Total Pipeline Runtime', `${fmt.format(summary.total_elapsed_seconds)}s (~${(summary.total_elapsed_seconds / 86400).toFixed(1)} machine-days)`],
    ['Status', meta.status],
  ].filter(([, v]) => v);
  document.getElementById('provenance-info').innerHTML = rows.map(([k, v]) => `
    <div class="info-item"><div class="k">${k}</div><div class="v">${v}</div></div>`).join('');
}

async function init() {
  try {
    const [summary, meta] = await Promise.all([
      loadJSON('data/summary.json'),
      loadJSON('data/metadata.json'),
    ]);
    renderScopeCards(summary);
    renderProvenance(summary, meta);
  } catch (err) {
    console.error('Veri yüklenemedi:', err);
    document.getElementById('scope-cards').innerHTML = `<p class="skeleton">Veri yüklenirken bir sorun oluştu.</p>`;
    document.getElementById('provenance-info').innerHTML = '';
  }
}

document.addEventListener('DOMContentLoaded', init);
