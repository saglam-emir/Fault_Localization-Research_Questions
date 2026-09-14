// rq-common.js - shared, reusable building blocks for every RQ page
// (RQ1 now, RQ2-RQ5 later). No RQ-specific data logic lives here.

const RQ = (() => {
  const fmt = new Intl.NumberFormat('en-US');
  const pct = v => `${(v * 100).toFixed(1)}%`;

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
  function renderComparisonBars(el, items, { formatValue = fmt.format } = {}) {
    const max = Math.max(...items.map(i => i.value), 1);
    el.innerHTML = items.map(i => `
      <div class="bar-row">
        <div class="cat-label">${i.label}</div>
        <div class="bar-track">
          <div class="bar-seg" style="width:${(i.value / max * 100).toFixed(2)}%;background:${i.color};height:20px"></div>
          <span class="bar-value">${formatValue(i.value)}</span>
        </div>
      </div>`).join('');
  }

  // ---- stacked horizontal bars (composition, e.g. Pass+Fail) --------
  // categories: string[]; series: [{name, color, values: number[]}].
  // With a single series this is just a plain (non-stacked) bar list -
  // used for single-value comparisons like per-project reduction ratio.
  function renderStackedBarList(el, { categories, series, onCategoryClick, keys, formatValue = fmt.format, extra }) {
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
      const extraLabel = extra ? ` · ${extra(cat, i)}` : '';
      return `
        <div class="bar-row ${clickable}" data-key="${keys ? keys[i] : cat}">
          <div class="cat-label" title="${cat}">${cat}</div>
          <div class="bar-track">${segs}<span class="bar-value">${formatValue(totals[i])}${extraLabel}</span></div>
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
  // Failure Analysis's Fail_TC / Fail_Assert / Uncaught_Exception, or
  // RQ2's Full Execution vs. Slice Size which are a before/after pair,
  // not parts of one whole).
  // extra(cat, i): optional function returning a short label appended
  // next to the category heading (e.g. a computed reduction %).
  function renderGroupedBarList(el, { categories, series, onCategoryClick, keys, formatValue = fmt.format, extra }) {
    const max = Math.max(...series.flatMap(s => s.values), 1);
    const legend = `<div class="bar-legend">${series.map(s => `<span class="item"><span class="swatch" style="background:${s.color}"></span>${s.name}</span>`).join('')}</div>`;
    const groups = categories.map((cat, i) => {
      const seriesRows = series.map(s => `
        <div class="bar-row">
          <div class="cat-label mono" style="font-size:10.5px">${s.name}</div>
          <div class="bar-track">
            <div class="bar-seg" style="width:${(s.values[i] / max * 100).toFixed(2)}%;background:${s.color};height:12px"></div>
            <span class="bar-value">${formatValue(s.values[i])}</span>
          </div>
        </div>`).join('');
      const clickable = onCategoryClick ? 'clickable' : '';
      const extraLabel = extra ? `<span style="color:var(--ink-faint);font-family:var(--font-mono);font-size:11px"> · ${extra(cat, i)}</span>` : '';
      return `
        <div class="bar-group-block ${clickable}" data-key="${keys ? keys[i] : cat}" style="margin-bottom:16px">
          <div style="font-family:var(--font-mono);font-size:12.5px;color:var(--ink);margin-bottom:6px;${onCategoryClick ? 'cursor:pointer' : ''}">${cat}${extraLabel}</div>
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

  // ---- scatter plot (SVG, no library) --------------------------------
  // points: [{x, y, label, key}]. formatX/formatY format axis ticks and
  // tooltip values. onPointClick(key) is optional.
  function renderScatter(el, { points, xLabel, yLabel, formatX = fmt.format, formatY = fmt.format, color, onPointClick }) {
    const width = 720, height = 380, pad = { l: 64, r: 20, t: 16, b: 44 };
    const xMax = Math.max(...points.map(p => p.x), 1);
    const yMax = Math.max(...points.map(p => p.y), 1);
    const xScale = x => pad.l + (x / xMax) * (width - pad.l - pad.r);
    const yScale = y => height - pad.b - (y / yMax) * (height - pad.t - pad.b);
    const tickFracs = [0, 0.25, 0.5, 0.75, 1];

    const gridlines = tickFracs.map(f => `<line x1="${pad.l}" x2="${width - pad.r}" y1="${yScale(f * yMax).toFixed(1)}" y2="${yScale(f * yMax).toFixed(1)}" stroke="var(--border)" stroke-width="1"/>`).join('');
    const yTickLabels = tickFracs.map(f => `<text x="${pad.l - 8}" y="${(yScale(f * yMax) + 3).toFixed(1)}" text-anchor="end" font-size="10" fill="var(--ink-faint)" font-family="var(--font-mono)">${formatY(f * yMax)}</text>`).join('');
    const xTickLabels = tickFracs.map(f => `<text x="${xScale(f * xMax).toFixed(1)}" y="${height - pad.b + 18}" text-anchor="middle" font-size="10" fill="var(--ink-faint)" font-family="var(--font-mono)">${formatX(f * xMax)}</text>`).join('');
    const dots = points.map(p => `
      <circle class="${onPointClick ? 'scatter-pt-clickable' : ''}" data-key="${p.key ?? ''}"
        cx="${xScale(p.x).toFixed(1)}" cy="${yScale(p.y).toFixed(1)}" r="4.5"
        fill="${color}" fill-opacity="0.62" stroke="${color}" stroke-width="1.2">
        <title>${p.label}\n${xLabel}: ${formatX(p.x)}\n${yLabel}: ${formatY(p.y)}</title>
      </circle>`).join('');

    el.innerHTML = `<svg viewBox="0 0 ${width} ${height}" style="width:100%;height:auto;display:block">
      ${gridlines}
      <line x1="${pad.l}" x2="${pad.l}" y1="${pad.t}" y2="${height - pad.b}" stroke="var(--border)"/>
      <line x1="${pad.l}" x2="${width - pad.r}" y1="${height - pad.b}" y2="${height - pad.b}" stroke="var(--border)"/>
      ${yTickLabels}${xTickLabels}
      ${dots}
      <text x="${(pad.l + width - pad.r) / 2}" y="${height - 4}" text-anchor="middle" font-size="11" fill="var(--ink-muted)" font-family="var(--font-mono)">${xLabel}</text>
      <text x="14" y="${(pad.t + height - pad.b) / 2}" text-anchor="middle" font-size="11" fill="var(--ink-muted)" font-family="var(--font-mono)" transform="rotate(-90 14 ${(pad.t + height - pad.b) / 2})">${yLabel}</text>
    </svg>`;
    if (onPointClick) {
      el.querySelectorAll('.scatter-pt-clickable').forEach(pt => {
        pt.style.cursor = 'pointer';
        pt.addEventListener('click', () => onPointClick(pt.dataset.key));
      });
    }
  }

  // ---- 2x2 matrix / heatmap (e.g. Trace inclusion x Slice inclusion) --
  // cells: [{row, col, count, total, emphasize}] in reading order
  // (row-major: [rowA-colA, rowA-colB, rowB-colA, rowB-colB]).
  // rowLabels/colLabels: [labelA, labelB].
  function renderMatrix2x2(el, { rowLabels, colLabels, cells, rowAxis = '', colAxis = '' }) {
    const max = Math.max(...cells.map(c => c.count), 1);
    const cellHtml = c => {
      const pct = c.total ? (c.count / c.total * 100) : 0;
      const intensity = 0.12 + (c.count / max) * 0.5;
      return `
        <div class="matrix-cell ${c.emphasize ? 'emphasize' : ''}" style="--fill-alpha:${intensity.toFixed(2)}">
          ${c.emphasize ? '<div class="matrix-cell-tag">BEST CASE</div>' : ''}
          <div class="matrix-cell-n">${fmt.format(c.count)}</div>
          <div class="matrix-cell-pct">${pct.toFixed(1)}%</div>
        </div>`;
    };
    el.innerHTML = `
      <div class="matrix-2x2">
        <div class="matrix-corner"></div>
        <div class="matrix-col-label">${colLabels[0]}</div>
        <div class="matrix-col-label">${colLabels[1]}</div>
        <div class="matrix-row-label">${rowLabels[0]}</div>
        ${cellHtml(cells[0])}${cellHtml(cells[1])}
        <div class="matrix-row-label">${rowLabels[1]}</div>
        ${cellHtml(cells[2])}${cellHtml(cells[3])}
      </div>
      ${(rowAxis || colAxis) ? `<div class="matrix-axis-labels"><span>↓ ${rowAxis}</span><span>${colAxis} →</span></div>` : ''}
    `;
  }

  // ---- generic sortable / searchable / paginated data table ---------
  // columns: [{key, label, numeric}]. rows: array of plain objects.
  function createDataTable(root, { columns, rows, searchKeys, filterKey, pageSize = 25, onRowClick, rowKey }) {
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
        <tr ${onRowClick ? `class="clickable-row" data-key="${rowKey ? rowKey(r) : ''}"` : ''}>${columns.map(c => {
          const raw = r[c.key];
          const text = c.format ? c.format(raw) : (c.numeric ? fmt.format(raw) : raw);
          return `<td class="${c.numeric ? 'num' : ''}">${text}</td>`;
        }).join('')}</tr>
      `).join('') || `<tr><td colspan="${columns.length}" style="text-align:center;color:var(--ink-faint);padding:24px">No matching rows.</td></tr>`;
      if (onRowClick) {
        tbody.querySelectorAll('tr.clickable-row').forEach(tr => tr.addEventListener('click', () => onRowClick(tr.dataset.key)));
      }

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

  return { fmt, pct, renderSegmented, renderComparisonBars, renderStackedBarList, renderGroupedBarList, renderScatter, renderMatrix2x2, createDataTable };
})();
