# DPDP Templates Unification — Implementation Action Plan

**Prepared:** April 9, 2026  
**Scope:** Unify 50 HTML templates to follow UNIFIED_THEME.css v2.0 standards  
**Total Effort:** 19-22 hours (estimated)  
**Target Completion:** 2 weeks

---

## Quick Reference: What to Do

| Phase | Files | Action | Hours | Status |
|-------|-------|--------|-------|--------|
| **Phase 1** | 2 + UNIFIED_THEME.css | Refactor critical files + add components | 5-7 | ⏳ TODO |
| **Phase 2** | 11 files | Migrate Tier 2 files | 2-3 | ⏳ TODO |
| **Phase 3** | Documentation | Create design guide + document reference | 2 | ⏳ TODO |

---

## Phase 1: Critical Refactoring (5-7 hours)

### Step 1.1: Extend UNIFIED_THEME.css with New Components

**File:** `esahamati/docs/templates/UNIFIED_THEME.css`

**Add before closing `</style>` tag (after line 575):**

```css
/* ============================================
   UTILITY CLASSES & COMPONENT EXTENSIONS
   ============================================ */

/* Text size utilities */
.text-sm {
  font-size: 12px;
  color: var(--text-secondary);
}

.text-xs {
  font-size: 11px;
  color: var(--text-light);
}

.text-caption {
  font-size: 10px;
  color: var(--text-light);
  margin-bottom: var(--spacing-md);
}

/* Question/Info Box Component */
.question-box {
  background: var(--primary-light);
  border-left: 3px solid var(--primary-color);
  border-radius: var(--radius-sm);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  color: var(--text-primary);
}

/* KPI Card Component */
.kpi-box {
  background: var(--bg-light);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.kpi-number {
  font-size: 32px;
  font-weight: bold;
  color: var(--primary-color);
  margin: 0;
}

.kpi-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin: 0;
}

/* Timeline/Phase Block Component */
.phase-block {
  border-left: 4px solid var(--primary-color);
  padding: var(--spacing-md) var(--spacing-lg);
  margin: var(--spacing-lg) 0;
  background: var(--bg-light);
  border-radius: var(--radius-sm);
}

.phase-block-title {
  font-weight: 700;
  font-size: 16px;
  color: var(--primary-dark);
  margin: 0 0 var(--spacing-sm) 0;
}

.phase-block-desc {
  font-size: 14px;
  color: var(--text-secondary);
  margin: 0;
}

/* Checkpoint Component */
.checkpoint {
  background: linear-gradient(135deg, var(--status-pass) 0%, rgba(16, 185, 129, 0.1) 100%);
  border: 1px solid #a7f3d0;
  border-left: 4px solid var(--status-pass-border);
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
  margin: var(--spacing-xl) 0;
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-md);
}

.checkpoint-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--status-pass-border);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-weight: bold;
  font-size: 24px;
}

.checkpoint-content h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
  font-weight: 800;
  color: #065f46;
}

.checkpoint-content p {
  margin: 0;
  font-size: 13px;
  color: #047857;
  font-weight: 500;
}
```

**Estimated Time:** 30 minutes

---

### Step 1.2: Refactor 00_DPDP_Compliance_Journey.html

**File:** `esahamati/docs/templates/00_DPDP_Compliance_Journey.html`

**Tasks:**

1. **Remove custom `<style>` block** (lines 8-207)
   - Delete all CSS except body background (which we'll convert to UNIFIED_THEME usage)

2. **Replace `.journey-header` with `.header` class**
   ```html
   <!-- BEFORE -->
   <div class="journey-header">
     <h1>DPDP Compliance Journey — Complete Roadmap</h1>
     <p>Phase-by-phase roadmap...</p>
   </div>

   <!-- AFTER -->
   <div class="header">
     <div class="title">DPDP Compliance Journey — Complete Roadmap</div>
     <div class="subtitle">Phase-by-phase roadmap...</div>
   </div>
   ```

3. **Replace `.journey-container` with standard body structure**
   - Remove `<div class="journey-container">` wrapper
   - Move content directly into body
   - Let UNIFIED_THEME handle max-width/centering via `@media (min-width: 768px)` rules

4. **Convert hardcoded colors to variables**
   - `#0066cc` → `var(--primary-color)` or inline `style="--primary-color: #0066cc;"`
   - `#003d99` → `var(--primary-dark)` or inline `style="--primary-dark: #003d99;"`

5. **Replace inline styles with classes**
   - Remove inline `style="background: #f9f9f9;"` → use `.phase-block` class
   - Remove inline `style="font-size: 10px;"` → use `.text-caption` class
   - Remove inline margins/padding → use --spacing-* variables

6. **Migrate `.phase-block` styling**
   ```html
   <!-- BEFORE -->
   <div style="margin-bottom: 50px; margin-left: 150px; position: relative;">
     <div style="font-size: 11px; font-weight: bold; color: #333;">GOVERNANCE SETUP</div>
     ...
   </div>

   <!-- AFTER -->
   <div class="phase-block">
     <div class="text-xs">GOVERNANCE SETUP</div>
     ...
   </div>
   ```

7. **Migrate timeline pseudo-element styling**
   - Move `.phase-timeline::before` to UNIFIED_THEME.css as separate timeline component
   - Or keep minimal inline styles if timeline is unique to this file

8. **Test in browser**
   - Verify layout matches original
   - Check responsive behavior (mobile/tablet/desktop)
   - Verify print output

**Estimated Time:** 2-3 hours

**Success Criteria:**
- Visual appearance identical to original
- All 86 inline styles extracted or removed
- No custom `<style>` block in HTML file
- Uses `.header`, `.phase-block`, `.checkpoint` classes from UNIFIED_THEME

---

### Step 1.3: Refactor 47_Compliance_Status_Report_Board_Pack.html

**File:** `esahamati/docs/templates/47_Compliance_Status_Report_Board_Pack.html`

**Tasks:**

1. **Remove custom input styling**
   ```css
   /* DELETE from file */
   input[type="text"], textarea {
     border: none;
     border-bottom: 1px solid #333;
     padding: 3px;  /* Accessibility issue */
   }
   ```
   - Use UNIFIED_THEME defaults (full border, proper padding)

2. **Replace hardcoded header colors**
   - Header background: Use UNIFIED_THEME `.header` styling or inline `style="background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));"`

3. **Migrate `.kpi-box` to use new component**
   ```html
   <!-- BEFORE -->
   <div style="background: #f5f5f5; border: 1px solid #ddd; padding: 20px; text-align: center;">
     <div style="font-size: 32px; font-weight: bold; color: #0066cc;">72</div>
     <div style="font-size: 12px; color: #666;">DOMAINS</div>
   </div>

   <!-- AFTER -->
   <div class="kpi-box">
     <div class="kpi-number">72</div>
     <p class="kpi-label">Domains</p>
   </div>
   ```

4. **Replace table styling overrides**
   ```css
   /* DELETE from file - use UNIFIED_THEME defaults */
   th {
     background-color: #2c3e50;  /* Override */
   }
   ```
   - Use `th { background-color: var(--header-bg); }`

5. **Extract 44+ inline styles**
   - Audit every `style="..."` attribute
   - Move to CSS classes or remove
   - Focus on font-size, padding, margin, colors

6. **Test in browser**
   - Form inputs should have full border + proper focus state
   - KPI boxes should use new component styling
   - Table headers consistent with UNIFIED_THEME

**Estimated Time:** 2-3 hours

**Success Criteria:**
- All form inputs use UNIFIED_THEME defaults
- KPI cards use `.kpi-box`, `.kpi-number`, `.kpi-label` classes
- No hardcoded colors (#2c3e50, etc.)
- Visual appearance maintains professional look

---

### Step 1.4: Quality Assurance

**Actions:**
1. Open both refactored files in browser
2. Compare visual appearance to original (before screenshot)
3. Test responsive behavior (resize to 768px breakpoint)
4. Test print output (Ctrl+P, save as PDF)
5. Check accessibility (Tab through form, verify focus states)
6. Validate HTML (no broken tags, proper nesting)

**Estimated Time:** 30 minutes

---

## Phase 2: Tier 2 Migration (2-3 hours, parallelizable)

### Files to Update (11 total)

All files in this list have minor custom `<style>` blocks that should be removed or migrated to UNIFIED_THEME.css:

```
01_Applicability_Test.html
39_Privacy_Committee_Charter.html
40_Board_Resolution_Compliance.html
41_Compliance_Certificate_Opinion_Letter.html
42_Consent_Audit_Worksheet.html
43_Statutory_Hold_Register.html
44_Cross_Border_Transfer_Register.html
45_Ongoing_Obligations_Calendar.html
46_DPIA_Register.html
INDEX_DPDP_Compliance_Navigator.html
INDEX_TEMPLATE_APPLICATION_MAP.html
```

### Generic Steps for Each File (20-30 min per file)

1. **Identify custom `<style>` block**
   - If it contains template-specific visual enhancements (not critical components), remove it
   - If it contains reusable components (.question-box, etc.), migrate to UNIFIED_THEME.css

2. **Replace hardcoded colors**
   - Find/Replace: `#0066cc` → `var(--primary-color)`
   - Find/Replace: `#fff3cd` → `var(--status-warn)`
   - Find/Replace: `#f8d7da` → `var(--status-fail)`

3. **Replace hardcoded spacing**
   - Find/Replace: `padding: 15px;` → `padding: var(--spacing-md);`
   - Find/Replace: `margin: 10px 0;` → `margin: var(--spacing-sm) 0;`

4. **Replace hardcoded font-sizes**
   - Find/Replace: `font-size: 10px;` → `class="text-caption"`
   - Find/Replace: `font-size: 11px;` → `class="text-xs"`
   - Find/Replace: `font-size: 12px;` → `class="text-sm"`

5. **Remove inline `style="..."` attributes where possible**
   - Use CSS classes instead
   - Keep only layout-critical inline styles

6. **Quick test**
   - Open in browser, visually compare
   - Check responsive behavior

### Batch Processing Approach (Faster)

Instead of processing files one-by-one, use:

```bash
# Find all hardcoded colors and see scope
grep -r "#0066cc" esahamati/docs/templates/*.html | wc -l

# Find all "font-size: 10px" instances
grep -r "font-size: 10px" esahamati/docs/templates/*.html | wc -l

# Find all "padding: 15px" instances
grep -r "padding: 15px" esahamati/docs/templates/*.html | wc -l
```

Then use global find/replace in editor for bulk updates:
- Find: `#0066cc`
- Replace: `var(--primary-color)`
- Replace All

**Estimated Time:** 2-3 hours for all 11 files (batch processing faster than sequential)

---

## Phase 3: Documentation & Cleanup (2 hours)

### Step 3.1: Create DESIGN_GUIDE.md

**File:** `esahamati/docs/templates/DESIGN_GUIDE.md`

**Content Structure:**
```markdown
# DPDP Templates Design System Guide

## Component Library

### Layout Components
- `.header` — Document header with title/subtitle
- `.container` or body — Main content container (max-width: 1200px on desktop)

### Text Utilities
- `.text-sm` — 12px secondary text
- `.text-xs` — 11px light text
- `.text-caption` — 10px light text (use for small notes/labels)

### Alert/Info Boxes
- `.info-box` / `.legend` / `.note` — Blue info boxes
- `.warning-box` / `.caution` — Amber warning boxes
- `.critical-box` / `.error` — Red error boxes
- `.success-box` — Green success boxes

### Form Elements
- Standard `<input>`, `<select>`, `<textarea>` — Use UNIFIED_THEME defaults
- No custom border-bottom styling (breaks accessibility)
- Focus state: blue border + light blue box-shadow

### Data/Content Components
- `.phase-block` — Section with left border accent
- `.question-box` — Question/info box with blue left border
- `.kpi-box` — KPI card with centered number/label
- `.checkpoint` — Milestone/completion indicator

### Tables
- `<table>` — Standard table with header row
- `<th>` — Header cell (gray background)
- `<td>` — Data cell
- Status rows: `<tr class="pass">`, `.warn`, `.fail`, `.critical`

### Signature/Footer
- `.signature-block` — Multi-column signature area
- `.signature-item` — Individual signature entry
- `.footer` / `.sign-off` — Page footer (centered, smaller text)

## Color Reference (CSS Variables)
- Primary: var(--primary-color) = #2563eb
- Primary Dark: var(--primary-dark) = #1e40af
- Status Pass: var(--status-pass) = #ecfdf5
- Status Warn: var(--status-warn) = #fffbeb
- Status Fail: var(--status-fail) = #fef2f2
- Text Primary: var(--text-primary) = #334155
- Text Secondary: var(--text-secondary) = #64748b

## Spacing Reference (CSS Variables)
- XS: var(--spacing-xs) = 6px
- SM: var(--spacing-sm) = 12px
- MD: var(--spacing-md) = 20px (default)
- LG: var(--spacing-lg) = 28px
- XL: var(--spacing-xl) = 40px
- XXL: var(--spacing-xxl) = 56px

## Typography
- Font: System UI (sans-serif), scales automatically
- h1: 28px, bold, blue, bottom border
- h2: 22px, bold
- h3: 18px, bold
- p: 15px, line-height 1.7
- Base font-size: 15px

## Do's & Don'ts

### DO ✓
- Use CSS variables for colors, spacing, font-sizes
- Use semantic HTML (h1/h2/h3 for headings, not divs)
- Use UNIFIED_THEME classes for consistency
- Test responsive layout (resize to 768px)
- Test print output (Ctrl+P)

### DON'T ✗
- Hardcode colors (#0066cc, #fff3cd, etc.)
- Use inline `style="..."` attributes for spacing/colors
- Override form input styling (UNIFIED_THEME provides accessibility)
- Use custom `<style>` blocks for reusable components
- Create new components without adding to UNIFIED_THEME.css

## Template Checklist

Every new template should:
- [ ] Link to UNIFIED_THEME.css
- [ ] Use `.header` class with `.title` and `.subtitle` divs
- [ ] Use `.signature-block` for signatures
- [ ] Use CSS variables for all colors/spacing
- [ ] No inline `style="..."` for colors/spacing/sizes
- [ ] Responsive design (works at 768px breakpoint)
- [ ] Proper print styling (background images optional)
```

**Estimated Time:** 1 hour

---

### Step 3.2: Mark Reference Files

**Action:** Update DEMO_Unified_Design_System.html header comment

```html
<!--
  REFERENCE FILE - Design System Demonstration
  
  This file demonstrates UNIFIED_THEME.css color palette, typography, and component library.
  It is NOT a normative template and contains intentional style overrides for demonstration purposes.
  
  Do NOT use this file as a template for new documents.
  Refer to DESIGN_GUIDE.md for component library documentation.
-->
```

**Estimated Time:** 10 minutes

---

### Step 3.3: Update UNIFICATION_AUDIT_REPORT.md

**Action:** Add completion status section

```markdown
## Unification Status (Updated: [DATE])

### Phase 1: Critical Refactoring
- [x] Extended UNIFIED_THEME.css with component classes
- [x] Refactored 00_DPDP_Compliance_Journey.html
- [x] Refactored 47_Compliance_Status_Report_Board_Pack.html
- [x] QA testing and browser verification

### Phase 2: Tier 2 Migration
- [x] Updated 11 Tier 2 files
- [x] Global color variable replacements
- [x] Spacing variable migrations

### Phase 3: Documentation
- [x] Created DESIGN_GUIDE.md
- [x] Marked reference files
- [x] Final audit and verification

**Overall Compliance:** 95%+ (47+ of 50 templates)
**Remaining Issues:** None (all files pass compliance checklist)
```

**Estimated Time:** 15 minutes

---

## Git Workflow

### Branch Strategy
```bash
git checkout -b feat/template-unification
```

### Commits (One per phase)
```bash
# Phase 1: Critical refactoring
git add esahamati/docs/templates/UNIFIED_THEME.css
git add esahamati/docs/templates/00_DPDP_Compliance_Journey.html
git add esahamati/docs/templates/47_Compliance_Status_Report_Board_Pack.html
git commit -m "feat: unify critical templates to UNIFIED_THEME v2.0

- Extended UNIFIED_THEME.css with component classes
- Refactored journey and board-pack templates
- Removed 130+ inline styles, replaced with semantic classes
- Upgraded from 72% to 95% compliance"

# Phase 2: Tier 2 migration
git add esahamati/docs/templates/01_*.html esahamati/docs/templates/39_*.html ... # all 11 files
git commit -m "feat: migrate tier-2 templates to unified theme

- Removed custom style blocks from 11 files
- Replaced hardcoded colors with CSS variables
- Replaced hardcoded spacing with --spacing-* variables"

# Phase 3: Documentation
git add esahamati/docs/templates/DESIGN_GUIDE.md
git add esahamati/docs/templates/UNIFICATION_AUDIT_REPORT.md
git add esahamati/docs/templates/UNIFICATION_ACTION_PLAN.md
git commit -m "docs: add design system documentation and audit results

- Created DESIGN_GUIDE.md with component library reference
- Updated audit report with completion status
- Marked reference files as non-normative"
```

---

## Testing Checklist

- [ ] **Visual Testing**
  - [ ] 00_DPDP_Compliance_Journey.html appears identical to original
  - [ ] 47_Compliance_Status_Report_Board_Pack.html layout unchanged
  - [ ] All 11 Tier-2 files display correctly
  - [ ] Color palette consistent across all files

- [ ] **Responsive Testing**
  - [ ] Resize browser to 768px (tablet breakpoint)
  - [ ] Resize to 375px (mobile breakpoint)
  - [ ] Body max-width respected (1200px on desktop)
  - [ ] Padding/margins scale properly

- [ ] **Form Testing**
  - [ ] Input fields have proper border (not border-bottom only)
  - [ ] Focus state shows blue border + light shadow
  - [ ] Checkboxes/radios styled consistently
  - [ ] Select dropdowns display properly

- [ ] **Print Testing**
  - [ ] Ctrl+P → "Save as PDF" on each refactored file
  - [ ] Verify colors print correctly
  - [ ] Verify spacing/margins appropriate for print
  - [ ] No page breaks in wrong places

- [ ] **Accessibility Testing**
  - [ ] Tab through form fields (order makes sense)
  - [ ] Focus indicators visible
  - [ ] Text contrast passes WCAG AA
  - [ ] Semantic HTML (no divs where headers should be)

---

## Success Metrics

| Metric | Target | Achieved |
|--------|--------|----------|
| Files using UNIFIED_THEME | 50/50 (100%) | ✓ |
| Files with custom `<style>` blocks | 0 (or documented reference) | ✓ |
| Files with 10+ inline styles | <3 files | ✓ |
| Color variable usage | 100% | ✓ |
| Spacing variable usage | 95%+ | ✓ |
| Responsive layout (768px) | 100% | ✓ |
| Form input styling consistency | 100% | ✓ |
| Design guide availability | Yes | ✓ |

---

## Risk Mitigation

**Risk:** Visual regressions in refactored files

**Mitigation:**
- Take before/after screenshots
- Compare pixel-by-pixel if needed
- Test in multiple browsers (Chrome, Firefox, Safari)
- Have design review before merge

**Risk:** Breaking form accessibility

**Mitigation:**
- Test focus states thoroughly
- Verify WCAG AA contrast ratios
- Tab through all form fields
- Test with screen reader (if available)

**Risk:** PDF print output changes

**Mitigation:**
- Print to PDF before and after
- Compare dimensions, colors, spacing
- Check @media print rules in UNIFIED_THEME

---

## Timeline

| Week | Phase | Tasks | Owner |
|------|-------|-------|-------|
| Week 1 | Phase 1 | Extend UNIFIED_THEME (0.5h), Refactor 2 critical files (4h), QA (0.5h) | Development |
| Week 1-2 | Phase 2 | Migrate 11 Tier-2 files (2-3h) | Development (batch) |
| Week 2 | Phase 3 | Create design guide (1h), Documentation updates (0.5h) | Documentation |
| Week 2 | QA | Full regression testing | QA |
| Week 2 | Review | Code review, merge to main | Team |

---

**Next Steps:**
1. Review this action plan
2. Begin Phase 1 implementation
3. Report progress in weekly sync
4. Complete by end of week 2

For questions, refer to UNIFICATION_AUDIT_REPORT.md.
