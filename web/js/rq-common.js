// rq-common.js - shared, reusable building blocks for every RQ page
// (RQ1 now, RQ2-RQ5 later). No RQ-specific data logic lives here.

const RQ = (() => {
  const fmt = new Intl.NumberFormat('en-US');

  // ---- segmented control (tabs) -------------------------------------
  // options: [{value, label}]. Re-renders on every call; caller re-invokes
  // after state changes rather than the control managing its own state.
  function renderSegmented(el, options, activeValue, onChange) {
    el.innerHTML = options.map(o => `
      <button type="button" class="${o.value === activeValue ? 'active' : ''}" data-value="${o.value}">${o.label}</button>
    `).join('');
    el.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', () => onChange(btn.dataset.value));
    });
  }

  // ---- simple side-by-side comparison bars (Overall scope) ----------
  // items: [{label, value, color}]
  function renderComparisonBars(el, items) {
    const max = Math.max(...items.map(i => i.value), 1);
    el.innerHTML = items.map(i => `
      <div class="bar-row">
        <div class="cat-label">${i.label}</div>
        <div class="bar-track">
          <div class="bar-seg" style="width:${(i.value / max * 100).toFixed(2)}%;background:${i.color};height:20px"></div>
          <span class="bar-value">${fmt.format(i.value)}</span>
        </div>
      </div>`).join('');
  }

  // ---- stacked horizontal bars (composition, e.g. Pass+Fail) --------
  // categories: string[]; series: [{name, color, values: number[]}]
  function renderStackedBarList(el, { categories, series, onCategoryClick, keys }) {
    const totals = categories.map((_, i) => series.reduce((s, ser) => s + ser.values[i], 0));
    const max = Math.max(...totals, 1);
    const legend = series.length > 1
      ? `<div class="bar-legend">${series.map(s => `<span class="item"><span class="swatch" style="background:${s.color}"></span>${s.name}</span>`).join('')}</div>`
      : '';
    const rows = categories.map((cat, i) => {
      const segs = series.map(s => {
        const w = (s.values[i] / max * 100).toFixed(2);
        return `<div class="bar-seg" style="width:${w}%;background:${s.color}"></div>`;
      }).join('');
      const clickable = onCategoryClick ? 'clickable' : '';
      return `
        <div class="bar-row ${clickable}" data-key="${keys ? keys[i] : cat}">
          <div class="cat-label" title="${cat}">${cat}</div>
          <div class="bar-track">${segs}<span class="bar-value">${fmt.format(totals[i])}</span></div>
        </div>`;
    }).join('');
    el.innerHTML = `${legend}<div class="bar-chart-scroll">${rows}</div>`;
    if (onCategoryClick) {
      el.querySelectorAll('.bar-row.clickable').forEach(row => {
        row.addEventListener('click', () => onCategoryClick(row.dataset.key));
      });
    }
  }

  // ---- grouped bars: one compact block per category, one thin bar ---
  // per series (used when series are NOT a composition/partition, e.g.
  // Failure Analysis's Fail_TC / Fail_Assert / Uncaught_Exception).
  function renderGroupedBarList(el, { categories, series, onCategoryClick, keys }) {
    const max = Math.max(...series.flatMap(s => s.values), 1);
    const legend = `<div class="bar-legend">${series.map(s => `<span class="item"><span class="swatch" style="background:${s.color}"></span>${s.name}</span>`).join('')}</div>`;
    const groups = categories.map((cat, i) => {
      const seriesRows = series.map(s => `
        <div class="bar-row">
          <div class="cat-label mono" style="font-size:10.5px">${s.name}</div>
          <div class="bar-track">
            <div class="bar-seg" style="width:${(s.values[i] / max * 100).toFixed(2)}%;background:${s.color};height:12px"></div>
            <span class="bar-value">${fmt.format(s.values[i])}</span>
          </div>
        </div>`).join('');
      const clickable = onCategoryClick ? 'clickable' : '';
      return `
        <div class="bar-group-block ${clickable}" data-key="${keys ? keys[i] : cat}" style="margin-bottom:16px">
          <div style="font-family:var(--font-mono);font-size:12.5px;color:var(--ink);margin-bottom:6px;${onCategoryClick ? 'cursor:pointer' : ''}">${cat}</div>
          ${seriesRows}
        </div>`;
    }).join('');
    el.innerHTML = `${legend}<div class="bar-chart-scroll">${groups}</div>`;
    if (onCategoryClick) {
      el.querySelectorAll('.bar-group-block.clickable').forEach(g => {
        g.addEventListener('click', () => onCategoryClick(g.dataset.key));
      });
    }
  }

  // ---- generic sortable / searchable / paginated data table ---------
  // columns: [{key, label, numeric}]. rows: array of plain objects.
  function createDataTable(root, { columns, rows, searchKeys, filterKey, pageSize = 25 }) {
    let sortKey = null, sortDir = 1, query = '', filterValue = '', page = 0;

    root.innerHTML = `
      <div class="table-toolbar">
        <input class="table-search" type="search" placeholder="Search…">
        ${filterKey ? `<select class="table-filter"><option value="">All ${filterKey}s</option></select>` : ''}
        <span class="table-count"></span>
      </div>
      <div class="table-scroll">
        <table class="data-table">
          <thead><tr>${columns.map(c => `<th data-key="${c.key}">${c.label}<span class="arrow"></span></th>`).join('')}</tr></thead>
          <tbody></tbody>
        </table>
      </div>
      <div class="table-pagination"></div>
    `;

    const tbody = root.querySelector('tbody');
    const countEl = root.querySelector('.table-count');
    const pagEl = root.querySelector('.table-pagination');
    const searchEl = root.querySelector('.table-search');
    const filterEl = root.querySelector('.table-filter');

    if (filterEl) {
      const values = [...new Set(rows.map(r => r[filterKey]))].sort();
      filterEl.innerHTML += values.map(v => `<option value="${v}">${v}</option>`).join('');
      filterEl.addEventListener('change', () => { filterValue = filterEl.value; page = 0; render(); });
    }
    searchEl.addEventListener('input', () => { query = searchEl.value.trim().toLowerCase(); page = 0; render(); });
    root.querySelectorAll('thead th').forEach(th => {
      th.addEventListener('click', () => {
        const key = th.dataset.key;
        if (sortKey === key) sortDir *= -1; else { sortKey = key; sortDir = 1; }
        render();
      });
    });

    function render() {
      let data = rows;
      if (filterValue) data = data.filter(r => r[filterKey] === filterValue);
      if (query) data = data.filter(r => searchKeys.some(k => String(r[k]).toLowerCase().includes(query)));
      if (sortKey) {
        data = [...data].sort((a, b) => {
          const av = a[sortKey], bv = b[sortKey];
          const cmp = typeof av === 'number' ? av - bv : String(av).localeCompare(String(bv));
          return cmp * sortDir;
        });
      }
      countEl.textContent = `${fmt.format(data.length)} row${data.length === 1 ? '' : 's'}`;
      root.querySelectorAll('thead th .arrow').forEach(a => a.textContent = '');
      if (sortKey) {
        const th = root.querySelector(`thead th[data-key="${sortKey}"] .arrow`);
        if (th) th.textContent = sortDir === 1 ? ' ↑' : ' ↓';
      }

      const totalPages = Math.max(1, Math.ceil(data.length / pageSize));
      page = Math.min(page, totalPages - 1);
      const pageRows = data.slice(page * pageSize, (page + 1) * pageSize);

      tbody.innerHTML = pageRows.map(r => `
        <tr>${columns.map(c => `<td class="${c.numeric ? 'num' : ''}">${c.numeric ? fmt.format(r[c.key]) : r[c.key]}</td>`).join('')}</tr>
      `).join('') || `<tr><td colspan="${columns.length}" style="text-align:center;color:var(--ink-faint);padding:24px">No matching rows.</td></tr>`;

      pagEl.innerHTML = totalPages > 1 ? `
        <button data-act="prev" ${page === 0 ? 'disabled' : ''}>← Prev</button>
        <span class="page-info">Page ${page + 1} of ${totalPages}</span>
        <button data-act="next" ${page >= totalPages - 1 ? 'disabled' : ''}>Next →</button>
      ` : '';
      pagEl.querySelectorAll('button').forEach(b => b.addEventListener('click', () => {
        page += b.dataset.act === 'next' ? 1 : -1;
        render();
      }));
    }

    render();
    return { refresh: render };
  }

  return { fmt, renderSegmented, renderComparisonBars, renderStackedBarList, renderGroupedBarList, createDataTable };
})();
