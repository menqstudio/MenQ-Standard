/* @ds-bundle: {"format":4,"namespace":"MenQ","components":[{"name":"BrandMark"},{"name":"Button"},{"name":"Card"},{"name":"Panel"},{"name":"PageHeader"},{"name":"SectionHeading"},{"name":"Badge"},{"name":"StatusDot"},{"name":"Avatar"},{"name":"Field"},{"name":"Input"},{"name":"Tabs"},{"name":"LocaleSwitch"},{"name":"ThemeSwitch"},{"name":"EmptyState"},{"name":"Skeleton"},{"name":"Toast"},{"name":"Modal"},{"name":"ConfirmDialog"},{"name":"Drawer"},{"name":"KpiStat"},{"name":"MetricBar"},{"name":"Table"},{"name":"Timeline"},{"name":"ChatMessage"},{"name":"AgentCard"},{"name":"ApprovalCard"},{"name":"CommandComposer"},{"name":"ContrastSection"}]} */
(function () {
  var React = window.React;
  var h = React.createElement;
  var useState = React.useState, useEffect = React.useEffect, useRef = React.useRef;
  function cx() { return Array.prototype.filter.call(arguments, Boolean).join(' '); }
  function reducedMotion() { return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches); }

  /* ── From BroPS src/components/ui.tsx ── */
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
  function Avatar(p) { return h('span', { className: cx('avatar', p.kind && 'mq-avatar--' + p.kind), 'aria-label': p.name }, String(p.name || '?').slice(0, 1).toUpperCase()); }
  function Field(p) { return h('div', { className: 'field' }, h('span', { className: 'field-label' }, p.label), h('span', null, p.children)); }
  function Skeleton(p) {
    var rows = p.rows || 3, out = [];
    for (var i = 0; i < rows; i++) out.push(h('div', { key: i, className: 'skeleton', style: { height: 18, width: (90 - i * 8) + '%' } }));
    return h('div', { className: 'stack', 'aria-busy': 'true' }, out);
  }
  function FormRow(p) { return h('label', { className: 'form-row' }, h('span', { className: 'field-label' }, p.label), p.children, p.error ? h('span', { className: 'form-error', style: { margin: 0 } }, p.error) : null); }
  function Input(p) { return h('input', Object.assign({}, p, { className: cx('input', p.invalid && 'mq-invalid'), 'aria-invalid': p.invalid ? 'true' : undefined, invalid: undefined })); }
  function Textarea(p) { return h('textarea', Object.assign({}, p, { className: 'textarea' })); }
  function Select(p) { return h('select', Object.assign({}, p, { className: 'select input' })); }
  function Modal(p) {
    useEffect(function () {
      function onKey(e) { if (e.key === 'Escape' && p.onClose) p.onClose(); }
      document.addEventListener('keydown', onKey); return function () { document.removeEventListener('keydown', onKey); };
    }, [p.onClose]);
    var dialog = h('div', { className: 'modal', role: 'dialog', 'aria-modal': 'true', 'aria-label': p.title, onClick: function (e) { e.stopPropagation(); } }, h('div', { className: 'modal-title' }, p.title), p.children);
    return p.inline ? dialog : h('div', { className: 'modal-scrim', onClick: p.onClose }, dialog);
  }
  function ConfirmDialog(p) {
    return h(Modal, { title: p.title, onClose: p.onCancel, inline: p.inline },
      h('div', { className: 'muted', style: { marginBottom: 16 } }, p.message),
      h('div', { className: 'form-actions' }, h(Button, { variant: 'ghost', small: true, onClick: p.onCancel }, p.cancelLabel), h(Button, { variant: 'danger', small: true, onClick: p.onConfirm }, p.confirmLabel)));
  }
  function Toast(p) {
    return h('button', { type: 'button', className: 'toast toast--' + (p.tone || 'info'), onClick: p.onDismiss, role: 'status' }, p.children);
  }

  /* ── MenQ Studio additions ── */
  function StatusDot(p) {
    var s = p.status || 'offline';
    return h('span', { className: 'mq-status' }, h('span', { className: 'mq-status-dot mq-status-dot--' + s, 'aria-hidden': 'true' }), p.label || s);
  }
  function Tabs(p) {
    var st = useState(p.defaultValue || (p.items[0] && p.items[0].value)), cur = p.value !== undefined ? p.value : st[0];
    function pick(v) { st[1](v); if (p.onChange) p.onChange(v); }
    function onKey(e) {
      var i = p.items.findIndex(function (t) { return t.value === cur; });
      if (e.key === 'ArrowRight') pick(p.items[(i + 1) % p.items.length].value);
      if (e.key === 'ArrowLeft') pick(p.items[(i - 1 + p.items.length) % p.items.length].value);
    }
    return h('div', { className: 'mq-tabs', role: 'tablist', onKeyDown: onKey }, p.items.map(function (t) {
      var on = t.value === cur;
      return h('button', { key: t.value, type: 'button', role: 'tab', 'aria-selected': on ? 'true' : 'false', tabIndex: on ? 0 : -1, className: cx('mq-tab', on && 'mq-tab--active'), onClick: function () { pick(t.value); } },
        t.label, t.count != null ? h('span', { className: 'mq-tab-count' }, t.count) : null);
    }));
  }
  function Drawer(p) {
    var panel = h('aside', { className: 'mq-drawer', role: 'dialog', 'aria-label': p.title },
      h('div', { className: 'mq-drawer-head' }, h('div', { className: 'panel-title' }, p.title), h(Button, { variant: 'ghost', small: true, onClick: p.onClose, title: 'Close' }, '✕')),
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
    return h('div', { className: 'mq-table-wrap' }, h('table', { className: 'mq-table' },
      p.caption ? h('caption', null, p.caption) : null,
      h('thead', null, h('tr', null, p.columns.map(function (c) { return h('th', { key: c.key, scope: 'col', style: { textAlign: c.align || 'left' } }, c.label); }))),
      h('tbody', null, p.rows.map(function (r, i) {
        return h('tr', { key: r.id || i }, p.columns.map(function (c) { return h('td', { key: c.key, style: { textAlign: c.align || 'left' } }, c.render ? c.render(r) : r[c.key]); }));
      }))));
  }
  function Timeline(p) {
    return h('ol', { className: 'mq-timeline' }, p.items.map(function (it, i) {
      return h('li', { key: i, className: 'mq-tl-item mq-tl--' + (it.state || 'done') },
        h('span', { className: 'mq-tl-marker', 'aria-hidden': 'true' }),
        h('div', { className: 'mq-tl-body' }, h('div', { className: 'mq-tl-title' }, it.title), it.meta ? h('div', { className: 'mq-tl-meta' }, it.meta) : null, it.detail ? h('div', { className: 'run-step-result' }, it.detail) : null));
    }));
  }
  function ChatMessage(p) {
    var role = p.role || 'human';
    return h('div', { className: cx('chat-msg', 'mq-msg--' + role, p.mine && 'chat-msg--mine') },
      h(Avatar, { name: p.author, kind: role }),
      h('div', { className: 'mq-msg-col' },
        h('div', { className: 'chat-author' }, h('span', { className: 'mq-msg-name' }, p.author), p.scope ? h('span', { className: 'mq-msg-scope' }, p.scope) : null, p.time ? h('span', null, ' · ' + p.time) : null),
        h('div', { className: 'chat-bubble' }, p.children),
        p.state ? h('div', { className: 'mq-msg-state' }, h(StatusDot, { status: p.state === 'running' ? 'busy' : p.state === 'failed' ? 'error' : 'online', label: p.stateLabel || p.state })) : null));
  }
  function AgentCard(p) {
    return h(Card, { className: 'mq-agent', variant: 'elevated' },
      h('div', { className: 'row between' }, h('div', { className: 'row' }, h(Avatar, { name: p.name, kind: 'agent' }), h('div', null, h('div', { className: 'panel-title' }, p.name), h('div', { className: 'muted', style: { fontSize: 12 } }, p.role))), h(StatusDot, { status: p.status, label: p.statusLabel })),
      p.scope ? h('div', { className: 'mq-agent-scope' }, p.scope.map(function (s) { return h(Badge, { key: s, tone: 'accent' }, s); })) : null,
      p.task ? h('div', { className: 'mq-agent-task' }, h('span', { className: 'field-label' }, p.taskLabel || 'Current task'), h('div', null, p.task)) : null,
      p.progress != null ? h('div', { className: 'mq-progress', role: 'progressbar', 'aria-valuenow': p.progress, 'aria-valuemin': 0, 'aria-valuemax': 100 }, h('span', { style: { width: p.progress + '%' } })) : null);
  }
  function ApprovalCard(p) {
    var risk = p.risk || 'medium', tone = risk === 'high' ? 'danger' : risk === 'low' ? 'success' : 'warning';
    return h(Card, { className: 'mq-approval mq-approval--' + risk, variant: 'elevated' },
      h('div', { className: 'row between' }, h('div', { className: 'field-label' }, p.kicker || 'Approval required'), h(Badge, { tone: tone }, p.riskLabel || risk + ' risk')),
      h('div', { className: 'panel-title', style: { marginTop: 8 } }, p.title),
      p.description ? h('div', { className: 'muted', style: { marginTop: 4 } }, p.description) : null,
      p.requestedBy ? h('div', { className: 'row', style: { marginTop: 12, fontSize: 12 } }, h(Avatar, { name: p.requestedBy, kind: 'agent' }), h('span', { className: 'muted' }, p.requestedBy)) : null,
      h('div', { className: 'form-actions', style: { marginTop: 16 } }, h(Button, { variant: 'ghost', small: true, onClick: p.onReject }, p.rejectLabel || 'Reject'), h(Button, { variant: 'primary', small: true, onClick: p.onApprove }, p.approveLabel || 'Approve')));
  }
  function CommandComposer(p) {
    var st = useState(''), ref = useRef(null);
    function send() { var v = st[0].trim(); if (!v) return; if (p.onSubmit) p.onSubmit(v); st[1](''); }
    return h('div', { className: 'mq-composer' },
      h('span', { className: 'mq-composer-prompt', 'aria-hidden': 'true' }, '›'),
      h('textarea', { ref: ref, rows: 1, value: st[0], placeholder: p.placeholder || 'Ask Bro…', 'aria-label': p.label || p.placeholder || 'Command',
        onChange: function (e) { st[1](e.target.value); },
        onKeyDown: function (e) { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); } } }),
      p.hint ? h('kbd', { className: 'mq-kbd' }, p.hint) : null,
      h(Button, { variant: 'primary', small: true, onClick: send, disabled: !st[0].trim() }, p.sendLabel || 'Send'));
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
  function ThemeSwitch(p) {
    function apply(v) {
      var r = document.documentElement;
      if (v === 'system') r.setAttribute('data-theme', window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); else r.setAttribute('data-theme', v);
      if (p.onChange) p.onChange(v);
    }
    var L = p.labels || {};
    return h(Segmented, { label: p.label || 'Theme', value: p.value, defaultValue: p.defaultValue || 'system', onChange: apply,
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

  window.MenQ = { BrandMark: BrandMark, SectionHeading: SectionHeading, LocaleSwitch: LocaleSwitch, ThemeSwitch: ThemeSwitch, MetricBar: MetricBar, ContrastSection: ContrastSection,  Button: Button, Card: Card, Panel: Panel, PageHeader: PageHeader, Badge: Badge, StatusDot: StatusDot, Avatar: Avatar, Field: Field, Input: Input, Textarea: Textarea, Select: Select, FormRow: FormRow,
    Tabs: Tabs, EmptyState: EmptyState, Skeleton: Skeleton, Toast: Toast, Modal: Modal, ConfirmDialog: ConfirmDialog, Drawer: Drawer, KpiStat: KpiStat, Table: Table, Timeline: Timeline,
    ChatMessage: ChatMessage, AgentCard: AgentCard, ApprovalCard: ApprovalCard, CommandComposer: CommandComposer };
})();
