# DPDP Templates — Design System Guide

**Version:** 2.0 (Unified)  
**Last Updated:** April 9, 2026  
**Status:** ✅ All 50 templates compliant

---

## Overview

This guide documents the component library and design system used across all 50 DPDP compliance templates. All templates inherit styling from **UNIFIED_THEME.css**, which provides a centralized, consistent visual language.

### Key Principle
**Single source of truth:** Update colors, spacing, or components in `UNIFIED_THEME.css` and all 50 templates update automatically.

---

## Layout & Spacing

### Spacing System

UNIFIED_THEME.css defines CSS custom properties for all spacing:

```css
--spacing-xs:  6px    /* Extra small */
--spacing-sm:  12px   /* Small */
--spacing-md:  20px   /* Medium - default */
--spacing-lg:  28px   /* Large */
--spacing-xl:  40px   /* Extra large */
--spacing-xxl: 56px   /* 2X - major margins */
```

**Usage:** Always use CSS variables:

```css
/* ✅ CORRECT */
.box { padding: var(--spacing-lg); margin: var(--spacing-md) 0; }

/* ❌ INCORRECT */
.box { padding: 28px; margin: 20px 0; }
```

### Body Max-Width

All templates use **1200px** maximum width on desktop (via UNIFIED_THEME.css @media query).

---

## Color System

### Semantic Colors

#### Primary Brand
- `--primary-color:` #2563eb (main blue)
- `--primary-dark:` #1e40af (dark blue)
- `--primary-light:` #eff6ff (light blue)

#### Status Colors
- **Pass/Compliant:** `--status-pass` (#ecfdf5 bg), `--status-pass-border` (#10b981)
- **Warning/At Risk:** `--status-warn` (#fffbeb bg), `--status-warn-border` (#f59e0b)
- **Fail/Critical:** `--status-fail` (#fef2f2 bg), `--status-fail-border` (#ef4444)

#### Text & Background
- `--text-primary:` #334155 (dark text)
- `--text-secondary:` #64748b (gray text)
- `--text-light:` #94a3b8 (light gray)
- `--bg-container:` #ffffff (white)
- `--bg-light:` #f1f5f9 (light backgrounds)

### Usage

```html
<!-- ✅ CORRECT -->
<div style="color: var(--text-primary); background: var(--bg-light);">Content</div>

<!-- ❌ INCORRECT -->
<div style="color: #334155; background: #f1f5f9;">Content</div>
```

---

## Component Library

### Header (`.header`)

Standard document header for all templates.

```html
<div class="header">
  <div class="title">Document Title</div>
  <div class="subtitle">Optional description</div>
</div>
```

### Alert Boxes

```html
<div class="info-box">ℹ️ Informational</div>
<div class="warning-box">⚠️ Warning</div>
<div class="critical-box">⛔ Critical</div>
<div class="success-box">✓ Success</div>
```

### Text Utilities

```html
<p>Normal text (15px)</p>
<p class="text-sm">Small text (12px)</p>
<p class="text-xs">Extra small (11px)</p>
<p class="text-caption">Caption (10px)</p>
```

### Data Cards

Grid-based cards for structured data with hover effects.

```html
<div class="data-card">
  <div class="data-card-title">Title</div>
  <div class="data-card-desc">Description</div>
</div>
```

### KPI Boxes

Display key metrics and statistics.

```html
<div class="kpi-box">
  <div class="kpi-number">95</div>
  <div class="kpi-label">Compliance %</div>
</div>
```

### Signature Blocks

Multi-column signature area for approvals.

```html
<div class="signature-block">
  <div class="signature-item">
    <strong>Prepared By:</strong>
    <div class="signature-line"></div>
    <small>Name & Date</small>
  </div>
</div>
```

### Tables with Status Rows

```html
<table>
  <tr class="pass"><td>Compliant</td><td>100%</td></tr>
  <tr class="warn"><td>At Risk</td><td>78%</td></tr>
  <tr class="fail"><td>Failed</td><td>0%</td></tr>
</table>
```

### Forms

Standard input, textarea, select, checkbox styling from UNIFIED_THEME.

```html
<label>Username</label>
<input type="text" placeholder="...">
<textarea placeholder="..."></textarea>
<input type="checkbox"> I agree
```

**Features:**
- Proper border (1px solid)
- Focus state: blue border + light shadow
- 10px padding, 4px radius
- Full width in containers

---

## Typography

```html
<h1>Page Title (28px, blue, underlined)</h1>
<h2>Section (22px)</h2>
<h3>Subsection (18px)</h3>
<p>Body text (15px, line-height 1.7)</p>
<strong>Bold</strong>
<em>Italic</em>
```

---

## Icons

Use **Lucide React** icons:

```html
<i data-lucide="check"></i>
<i data-lucide="alert-circle"></i>
<i data-lucide="x-circle"></i>
<i data-lucide="clipboard-check"></i>

<script src="lucide.min.js"></script>
<script>lucide.createIcons();</script>
```

**Do NOT use emoji.** Use Lucide icons for consistency.

---

## Responsive Design

### Breakpoints

- **768px:** Desktop breakpoint (max-width 1200px body, rounded corners)
- **< 768px:** Mobile (single column, minimal padding)

### Testing
- [ ] Desktop (1920px): Full layout
- [ ] Tablet (768px): Centered 1200px container
- [ ] Mobile (375px): Single column, readable

---

## Print Styles

@media print rules handle:
- Margin/padding reset
- Background removal
- Link color inheritance
- Table borders

Test with Ctrl+P → Save as PDF.

---

## DO's ✅ and DON'Ts ❌

| DO | DON'T |
|----|-------|
| Use `var(--primary-color)` | Hardcode `#0066cc` |
| Use `var(--spacing-lg)` | Hardcode `padding: 28px` |
| Use `.text-sm` class | Use inline `style="font-size: 12px"` |
| Use `.pass`, `.warn`, `.fail` on rows | Hardcode row background colors |
| Link UNIFIED_THEME.css first | Create duplicate `<style>` blocks |
| Use Lucide icons | Use emoji directly |
| Test at 768px & 375px | Assume one breakpoint |
| Test print output (PDF) | Rely on browser print preview |

---

## Troubleshooting

**Colors wrong?** → Check CSS variables, clear cache, verify UNIFIED_THEME.css link

**Spacing off?** → Use var(--spacing-*), check responsive behavior

**Form inputs weird?** → Don't override input CSS, let UNIFIED_THEME handle it

**Print looks different?** → Test actual PDF output, avoid background images

---

## Reference

**File:** `UNIFIED_THEME.css` (single source of truth)  
**Audit:** PHASE_1_COMPLETE.md, PHASE_2_COMPLETE.md  
**All 50 templates:** ✅ 100% compliant

Last updated: April 9, 2026
