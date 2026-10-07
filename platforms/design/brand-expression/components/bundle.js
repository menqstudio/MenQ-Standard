/* @ds-bundle: {"format":4,"namespace":"MenQ","components":[{"name":"BrandMark"},{"name":"Button"},{"name":"Card"},{"name":"Panel"},{"name":"PageHeader"},{"name":"SectionHeading"},{"name":"Badge"},{"name":"StatusDot"},{"name":"Avatar"},{"name":"Field"},{"name":"Input"},{"name":"Tabs"},{"name":"LocaleSwitch"},{"name":"ThemeSwitch"},{"name":"EmptyState"},{"name":"Skeleton"},{"name":"Toast"},{"name":"Modal"},{"name":"ConfirmDialog"},{"name":"Drawer"},{"name":"KpiStat"},{"name":"MetricBar"},{"name":"Table"},{"name":"ContrastSection"}]} */
/* MenQ brand expression components (D-027). Core layer: product-neutral. Product extensions (e.g. Bro) live under platforms/design/product-extensions/. */
(function () {
  var React = window.React;
  var h = React.createElement;
  var useState = React.useState, useEffect = React.useEffect, useRef = React.useRef;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(' '); }
  function reducedMotion() { return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches); }

  /* ── App components (adapted from BroPS src/components/ui.tsx) ── */
  function Button(p) {
    var v = p.variant || 'primary', size = p.small ? 'sm' : (p.size || 'md');
    var props = { title: p.title, onClick: p.onClick, 'aria-busy': p.loading ? 'true' : undefined,
      className: cx('btn', v !== 'secondary' && 'btn--' + v, size !== 'md' && 'btn--' + size, p.loading && 'btn--loading', p.className) };
    var kids = [p.loading ? h('span', { key: 's', className: 'mq-spinner', 'aria-hidden': 'true' }) : null, p.icon ? h('span', { key: 'i', 'aria-hidden': 'true', style: { display: 'inline-flex' } }, p.icon) : null, p.children];
    if (p.href) return h('a', Object.assign(props, { href: p.href }), kids);
    return h('button', Object.assign(props, { type: p.type || 'button', disabled: p.disabled || p.loading }), kids);
  }
  function Card(p) { var v = p.variant || 'solid'; return h('div', { className: cx('card', v !== 'solid' && 'card--' + v, p.className), style: p.style, 'data-interactive': p.interactive ? 'true' : undefined }, p.children); }
  function Panel(p) {
    return h(Card, null, h('div', { className: 'panel' },
      (p.title || p.actions) ? h('div', { className: 'panel-head' }, p.title ? h('div', { className: 'panel-title' }, p.title) : null, p.actions) : null,
      p.children));
  }
  function PageHeader(p) {
    return h('div', { className: 'page-header' }, h('div', null, h('div', { className: 'page-title' }, p.title), p.subtitle ? h('div', { className: 'page-subtitle' }, p.subtitle) : null), p.actions);
  }
  function Badge(p) { var t = p.tone || p.variant || 'neutral', status = ['info', 'success', 'warning', 'danger'].indexOf(t) >= 0; return h('span', { className: cx('badge', t !== 'neutral' && 'badge--' + t, (p.dot || status) && 'badge--dot') }, p.children); }
  function EmptyState(p) {
    return h('div', { className: 'empty' }, h('div', { className: 'empty-glyph', 'aria-hidden': 'true' }, p.glyph || '◍'), h('div', { className: 'empty-title' }, p.title),
      p.hint ? h('div', { className: 'muted', style: { marginTop: 4 } }, p.hint) : null, p.action ? h('div', { style: { marginTop: 12 } }, p.action) : null);
  }
  function Avatar(p) {
    var label = p.name || '?';
    if (p.src) return h('img', { className: cx('avatar', 'avatar--img', p.kind && 'mq-avatar--' + p.kind), src: p.src, alt: label, width: 28, height: 28 });
    return h('span', { className: cx('avatar', p.kind && 'mq-avatar--' + p.kind), role: 'img', 'aria-label': label }, String(label).slice(0, 1).toUpperCase());
  }
  function Field(p) { return h('div', { className: 'field' }, h('span', { className: 'field-label' }, p.label), h('span', null, p.children)); }
  function Skeleton(p) {
    var rows = p.rows || 3, out = [];
    for (var i = 0; i < rows; i++) out.push(h('div', { key: i, className: 'skeleton', style: { height: 18, width: (90 - i * 8) + '%' } }));
    return h('div', { className: 'stack', 'aria-busy': 'true' }, out);
  }
  function FormRow(p) { return h('label', { className: 'form-row' }, h('span', { className: 'field-label' }, p.label), p.children, p.error ? h('span', { className: 'form-error', style: { margin: 0 } }, p.error) : null); }
  function Input(p) { var rest = Object.assign({}, p); delete rest.invalid; return h('input', Object.assign(rest, { className: cx('input', p.invalid && 'mq-invalid'), 'aria-invalid': p.invalid ? 'true' : undefined })); }
  function Textarea(p) { return h('textarea', Object.assign({}, p, { className: 'textarea' })); }
  function Select(p) { return h('select', Object.assign({}, p, { className: 'select input' })); }
  function useDialog(ref, active, onClose) {
    useEffect(function () {
      if (!active) return undefined;
      var previous = document.activeElement, node = ref.current;
      var focusables = function () { return node ? Array.prototype.slice.call(node.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')).filter(function (el) { return !el.disabled; }) : []; };
      var first = focusables()[0]; if (first) first.focus();
      function onKey(e) {
        if (e.key === 'Escape' && onClose) { e.preventDefault(); onClose(); return; }
        if (e.key === 'Tab') {
          var list = focusables(); if (!list.length) return;
          var a = list[0], z = list[list.length - 1];
          if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
          else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
        }
      }
      document.addEventListener('keydown', onKey);
      return function () { document.removeEventListener('keydown', onKey); if (previous && previous.focus) previous.focus(); };
    }, [active, onClose]);
  }
  function Modal(p) {
    var ref = useRef(null);
    useDialog(ref, !p.inline, p.onClose);
    var dialog = h('div', { ref: ref, className: 'modal', role: 'dialog', 'aria-modal': p.inline ? undefined : 'true', 'aria-label': p.title, onClick: function (e) { e.stopPropagation(); } }, h('div', { className: 'modal-title' }, p.title), p.children);
    return p.inline ? dialog : h('div', { className: 'modal-scrim', onClick: p.onClose }, dialog);
  }
  function ConfirmDialog(p) {
    return h(Modal, { title: p.title, onClose: p.onCancel, inline: p.inline },
      h('div', { className: 'muted', style: { marginBottom: 16 } }, p.message),
      h('div', { className: 'form-actions' }, h(Button, { variant: 'ghost', small: true, onClick: p.onCancel }, p.cancelLabel), h(Button, { variant: 'danger', small: true, onClick: p.onConfirm }, p.confirmLabel)));
  }
  function Toast(p) {
    return h('div', { className: 'toast toast--' + (p.tone || 'info'), role: 'status' },
      h('span', { className: 'toast-text' }, p.children),
      p.onDismiss ? h('button', { type: 'button', className: 'toast-close', onClick: p.onDismiss, 'aria-label': p.dismissLabel || 'Dismiss' }, '✕') : null);
  }

  /* ── MenQ additions ── */
  function StatusDot(p) {
    var s = p.status || 'offline';
    return h('span', { className: 'mq-status' }, h('span', { className: 'mq-status-dot mq-status-dot--' + s, 'aria-hidden': 'true' }), p.label || s);
  }
  function Tabs(p) {
    var items = p.items || [], st = useState(p.defaultValue || (items[0] && items[0].value)), cur = p.value !== undefined ? p.value : st[0], list = useRef(null);
    function pick(v, focus) {
      st[1](v); if (p.onChange) p.onChange(v);
      if (focus && list.current) { var el = list.current.querySelector('[data-value="' + String(v).replace(/"/g, '') + '"]'); if (el) el.focus(); }
    }
    function onKey(e) {
      if (!items.length) return;
      var i = items.findIndex(function (t) { return t.value === cur; }), n = items.length, next = null;
      if (e.key === 'ArrowRight') next = (i + 1) % n;
      else if (e.key === 'ArrowLeft') next = (i - 1 + n) % n;
      else if (e.key === 'Home') next = 0;
      else if (e.key === 'End') next = n - 1;
      if (next !== null) { e.preventDefault(); pick(items[next].value, true); }
    }
    return h('div', { ref: list, className: 'mq-tabs', role: 'tablist', 'aria-label': p.label, onKeyDown: onKey }, items.map(function (t) {
      var on = t.value === cur;
      return h('button', { key: t.value, 'data-value': t.value, type: 'button', role: 'tab', id: t.id, 'aria-controls': t.controls, 'aria-selected': on ? 'true' : 'false', tabIndex: on ? 0 : -1, className: cx('mq-tab', on && 'mq-tab--active'), onClick: function () { pick(t.value); } },
        t.label, t.count != null ? h('span', { className: 'mq-tab-count' }, t.count) : null);
    }));
  }
  function Drawer(p) {
    var ref = useRef(null);
    useDialog(ref, !p.inline, p.onClose);
    var panel = h('aside', { ref: ref, className: 'mq-drawer', role: 'dialog', 'aria-modal': p.inline ? undefined : 'true', 'aria-label': p.title },
      h('div', { className: 'mq-drawer-head' }, h('div', { className: 'panel-title' }, p.title), h(Button, { variant: 'ghost', small: true, onClick: p.onClose, title: p.closeLabel || 'Close' }, '✕')),
      h('div', { className: 'mq-drawer-body' }, p.children));
    return p.inline ? panel : h('div', { className: 'mq-drawer-scrim', onClick: p.onClose }, h('div', { onClick: function (e) { e.stopPropagation(); } }, panel));
  }
  function KpiStat(p) {
    var target = Number(p.value) || 0, st = useState(reducedMotion() ? target : 0), raf = useRef(0);
    useEffect(function () {
      if (reducedMotion()) { st[1](target); return; }
      var t0 = performance.now(), dur = 800;
      function tick(now) { var k = Math.min(1, (now - t0) / dur); st[1](Math.round(target * (1 - Math.pow(1 - k, 3)))); if (k < 1) raf.current = requestAnimationFrame(tick); }
      raf.current = requestAnimationFrame(tick); return function () { cancelAnimationFrame(raf.current); };
    }, [target]);
    var fmt = new Intl.NumberFormat(p.locale || 'hy-AM').format(st[0]);
    return h(Card, { className: 'mq-kpi', variant: p.variant || 'elevated' }, h('div', { className: 'field-label' }, p.label), h('div', { className: 'stat' }, fmt, p.unit ? h('span', { className: 'mq-kpi-unit' }, p.unit) : null),
      p.delta != null ? h('div', { className: cx('mq-kpi-delta', p.delta >= 0 ? 'mq-up' : 'mq-down') }, (p.delta >= 0 ? '▲ ' : '▼ ') + Math.abs(p.delta) + '%', p.deltaLabel ? h('span', { className: 'muted' }, ' ' + p.deltaLabel) : null) : null);
  }
  function Table(p) {
    var columns = p.columns || [], rows = p.rows || [];
    return h('div', { className: 'mq-table-wrap' }, h('table', { className: 'mq-table' },
      p.caption ? h('caption', null, p.caption) : null,
      h('thead', null, h('tr', null, columns.map(function (c) { return h('th', { key: c.key, scope: 'col', style: { textAlign: c.align || 'left' } }, c.label); }))),
      h('tbody', null, rows.map(function (r, i) {
        return h('tr', { key: r.id || i }, columns.map(function (c) { return h('td', { key: c.key, style: { textAlign: c.align || 'left' } }, c.render ? c.render(r) : r[c.key]); }));
      }))));
  }
  /* ── Brand + marketing (Webpage) ── */
  function PowerIcon() {
    return h('svg', { viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: 2.2, strokeLinecap: 'round', strokeLinejoin: 'round', 'aria-hidden': 'true' },
      h('path', { d: 'M12 2v10' }), h('path', { d: 'M18.4 6.6a9 9 0 1 1-12.77.04' }));
  }
  function BrandMark(p) {
    return h('span', { className: cx('mq-brand', p.compact && 'mq-brand--compact', p.className), 'aria-label': p.admin ? 'MenQ Admin' : 'MenQ', role: 'img' },
      h('span', { className: 'mq-brand-word', 'aria-hidden': 'true' }, h('span', null, 'Men'), h('span', { className: 'mq-brand-q' }, h(PowerIcon))),
      p.admin ? h('span', { className: 'mq-brand-tag' }, p.tag || 'Admin') : null);
  }
  function SectionHeading(p) {
    var T = p.as || 'h2';
    return h('div', { className: cx('mq-sh', (p.align || 'center') === 'center' && 'mq-sh--center') },
      (p.index || p.eyebrow) ? h('div', { className: 'mq-sh-kicker' }, p.index ? h('span', { className: 'mq-sh-index' }, p.index) : null, p.eyebrow ? h('span', null, p.eyebrow) : null, h('span', { className: 'mq-sh-rule', 'aria-hidden': 'true' })) : null,
      h(T, { className: cx('mq-sh-title', T === 'h1' && 'mq-sh-title--h1') }, p.title),
      p.description ? h('p', { className: 'mq-sh-desc' }, p.description) : null, p.children);
  }
  function Segmented(p) {
    var st = useState(p.defaultValue || p.items[0].value), cur = p.value !== undefined ? p.value : st[0];
    return h('div', { className: 'mq-seg', role: 'group', 'aria-label': p.label }, p.items.map(function (it) {
      return h('button', { key: it.value, type: 'button', className: 'mq-seg-btn', 'aria-pressed': it.value === cur ? 'true' : 'false', title: it.title,
        onClick: function () { st[1](it.value); if (p.onChange) p.onChange(it.value); } }, it.label);
    }));
  }
  function LocaleSwitch(p) {
    return h(Segmented, { label: p.label || 'Language', value: p.value, defaultValue: p.defaultValue || 'hy', onChange: p.onChange,
      items: [{ value: 'hy', label: 'ՀԱՅ', title: 'Հայերեն' }, { value: 'en', label: 'EN', title: 'English' }, { value: 'ru', label: 'РУС', title: 'Русский' }] });
  }
  function applyTheme(v) {
    var r = document.documentElement, mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
    r.setAttribute('data-theme', v === 'system' ? (mq && mq.matches ? 'dark' : 'light') : v);
  }
  function ThemeSwitch(p) {
    var initial = p.value !== undefined ? p.value : (p.defaultValue || 'system'), pref = useState(initial);
    var current = p.value !== undefined ? p.value : pref[0];
    useEffect(function () {
      if (p.apply === false) return undefined;
      applyTheme(current);
      if (current !== 'system' || !window.matchMedia) return undefined;
      var mq = window.matchMedia('(prefers-color-scheme: dark)'), on = function () { applyTheme('system'); };
      if (mq.addEventListener) mq.addEventListener('change', on); else if (mq.addListener) mq.addListener(on);
      return function () { if (mq.removeEventListener) mq.removeEventListener('change', on); else if (mq.removeListener) mq.removeListener(on); };
    }, [current, p.apply]);
    function choose(v) { pref[1](v); if (p.onChange) p.onChange(v); }
    var L = p.labels || {};
    return h(Segmented, { label: p.label || 'Theme', value: current, onChange: choose,
      items: [{ value: 'system', label: L.system || 'System' }, { value: 'light', label: L.light || 'Light' }, { value: 'dark', label: L.dark || 'Dark' }] });
  }
  function MetricBar(p) {
    var pct = Math.max(0, Math.min(100, Number(p.value) || 0)), st = useState(reducedMotion() ? pct : 0);
    useEffect(function () { var t = setTimeout(function () { st[1](pct); }, 30); return function () { clearTimeout(t); }; }, [pct]);
    return h('div', { className: 'mq-metric' },
      h('div', { className: 'mq-metric-head' }, h('span', null, p.label), h('span', { className: 'muted' }, p.display || pct + '%')),
      h('div', { className: 'mq-metric-track', role: 'progressbar', 'aria-label': p.label, 'aria-valuenow': pct, 'aria-valuemin': 0, 'aria-valuemax': 100 }, h('div', { className: 'mq-metric-fill', style: { width: st[0] + '%' } })));
  }
  function ContrastSection(p) {
    return h('section', { className: cx('section-contrast', p.spotlight && 'section-spotlight', p.grid && 'mq-grid-bg', p.className), 'aria-labelledby': p.labelledBy }, p.children);
  }

  window.MenQ = { BrandMark: BrandMark, Button: Button, Card: Card, Panel: Panel, PageHeader: PageHeader, SectionHeading: SectionHeading, Badge: Badge, StatusDot: StatusDot, Avatar: Avatar,
    Field: Field, Input: Input, Textarea: Textarea, Select: Select, FormRow: FormRow, Tabs: Tabs, LocaleSwitch: LocaleSwitch, ThemeSwitch: ThemeSwitch, EmptyState: EmptyState, Skeleton: Skeleton,
    Toast: Toast, Modal: Modal, ConfirmDialog: ConfirmDialog, Drawer: Drawer, KpiStat: KpiStat, MetricBar: MetricBar, Table: Table, ContrastSection: ContrastSection, applyTheme: applyTheme };
})();
