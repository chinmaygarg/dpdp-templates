# DPDP HTML Templates — Style Consistency & Unification Audit Report

**Audit Date:** April 9, 2026  
**Scope:** 50 HTML templates in esahamati/docs/templates/  
**Overall Compliance Status:** MIXED — 72% fully compliant, 28% with issues

---

## Executive Summary

The templates utilize a centralized **UNIFIED_THEME.css (v2.0)** that defines consistent colors, fonts, spacing, and components. However, audit reveals three tiers of compliance:

| Tier | Status | Count | Details |
|------|--------|-------|---------|
| **Tier 1** | Fully Compliant | 36 files (72%) | Pure UNIFIED_THEME reliance, minimal inline styles |
| **Tier 2** | Minor Issues | 11 files (22%) | Embedded `<style>` tags with template-specific customizations |
| **Tier 3** | Major Issues | 3 files (6%) | Custom layout systems with heavy deviations |

---

## Tier 1: Fully Compliant Files (36)

All files listed below properly use UNIFIED_THEME.css without custom header overrides or embedded style systems:

```
02_Entity_Classification.html
03_Data_Inventory_Asset_Register.html
04_Data_Flow_Diagram.html
05_Records_Processing_Activities_ROPA.html
07_Privacy_Notice_Web.html
08_Consent_Form.html
09_Retrospective_Notice_Reconsent.html
10_Data_Subject_Access_Request_(DSAR)_Form.html
11_DSAR_Response_Letter.html
12_Erasure_and_Correction_SOP.html
13_Grievance_Handling_SOP.html
14_Nominee_Registration_Form.html
15_Data_Processing_Agreement_(DPA).html
16_Vendor_Risk_Assessment.html
17_Sub-Processor_Register.html
18_Data_Protection_Policy.html
19_Employee_Data_Protection_Training.html
20_Incident_Response_Plan.html
21_Breach_Notification_Template_-_DPB.html
22_Breach_Notification_-_Data_Principal.html
23_Post-Breach_Review.html
24_Security_Hardening_Plan.html
25_Compliance_Audit_Plan.html
26_DPIA_Workbook_(SDF).html
27_DPO_Appointment_Letter_(SDF).html
28_Audit_Findings_Report.html
29_Deletion_Log.html
30_Breach_Register.html
31_Consent_Registry_Dashboard.html
32_Data_Discovery_Report.html
33_Encryption_Implementation_Checklist.html
34_Access_Control_Policy.html
35_Audit_Logging_Configuration.html
36_Annual_SDF_Audit_Report.html
37_Board_Risk_Committee_Report.html
38_Compliance_Tracking_Dashboard.html
```

**Checklist (All Pass):**
- ✓ Links to UNIFIED_THEME.css
- ✓ Uses `.header` class (not custom headers)
- ✓ Respects spacing variables
- ✓ Standard form element styling
- ✓ Standard footer/signature-block
- ✓ Semantic h1/h2/h3 sizing

---

## Tier 2: Minor Issues (11 Files)

These files include embedded `<style>` blocks with template-specific customizations. Issues are primarily visual enhancements without breaking UNIFIED_THEME structure.

### Files with Minor Issues:

| File | Issue | Inline Styles | Impact |
|------|-------|---------------|--------|
| 01_Applicability_Test.html | Custom .question-box class, font-size overrides | 24 | Low |
| 39_Privacy_Committee_Charter.html | Minor style overrides | 6 | Low |
| 40_Board_Resolution_Compliance.html | Minor style overrides | 6 | Low |
| 41_Compliance_Certificate_Opinion_Letter.html | Minor style overrides | 6 | Low |
| 42_Consent_Audit_Worksheet.html | Minor style overrides | 6 | Low |
| 43_Statutory_Hold_Register.html | Minor style overrides | 6 | Low |
| 44_Cross_Border_Transfer_Register.html | Minor style overrides | 6 | Low |
| 45_Ongoing_Obligations_Calendar.html | Minor style overrides | 6 | Low |
| 46_DPIA_Register.html | Minor style overrides | 6 | Low |
| DEMO_Unified_Design_System.html | Design demo file, custom color swatches | 15 | Reference |
| INDEX_DPDP_Compliance_Navigator.html | Minor style enhancements | 8 | Low |
| INDEX_TEMPLATE_APPLICATION_MAP.html | Kanban board custom styles | 10 | Low |

**Common Pattern:**
```css
/* Custom to Tier 2 files */
.question-box {
  background: #f9f9f9;
  border-left: 3px solid #0066cc;  /* Should use var(--primary-color) */
  padding: 15px;                    /* Should use var(--spacing-md) = 20px */
}
```

---

## Tier 3: Major Issues (3 Files)

These files implement custom layout systems with significant deviations from UNIFIED_THEME.

### 1. 00_DPDP_Compliance_Journey.html (CRITICAL)

**Issue Severity:** CRITICAL (Entire custom layout system)

**Deviations:**
- Custom `.journey-container` wrapper (max-width: 1200px hardcoded)
- Custom `.journey-header` override (gradient: #0066cc → #003d99)
- Custom `.phase-timeline` with absolute positioning pseudo-elements
- Custom body background gradient
- **Inline styles: 86 instances** (largest in collection)

**Example Problems:**
```css
/* Line 14-21: Custom container instead of body */
.journey-container {
  max-width: 1400px;  /* Was 1400px, now 1200px after fix */
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

/* Line 23-42: Completely overrides .header */
.journey-header {
  background: linear-gradient(135deg, #0066cc 0%, #003d99 100%);  /* Hardcoded colors */
  color: white;
  padding: 40px;  /* Custom padding, not using variables */
}

/* Line 77-96+: Custom timeline visualization */
.phase-timeline::before {
  content: '';
  position: absolute;
  left: 50px;
  width: 3px;
  background: linear-gradient(180deg, #0066cc, #003d99);  /* Hardcoded gradient */
}
```

**Impact:**
- Difficult to theme centrally
- Multiple color conflicts (#0066cc vs --primary-color)
- Inconsistent spacing system
- Hard to maintain across platform

---

### 2. 47_Compliance_Status_Report_Board_Pack.html (CRITICAL)

**Issue Severity:** CRITICAL (Custom input styling, KPI components)

**Deviations:**
- Custom `.header` override with input fields
- Custom `.kpi-box`, `.kpi-number`, `.kpi-label` components (not in UNIFIED_THEME)
- Custom table header background (#2c3e50 hardcoded)
- Custom input styling: `border: none; border-bottom: 1px solid #333;` (overrides UNIFIED_THEME)
- **Inline styles: 44+ instances**

**Example Problems:**
```css
/* Line 22: Overrides UNIFIED_THEME input styles */
input[type="text"], textarea {
  border: none;
  border-bottom: 1px solid #333;  /* Conflicts with UNIFIED_THEME full border */
  padding: 3px;                     /* Too small, accessibility issue */
}

/* Line 14-16: Custom components not in UNIFIED_THEME */
.kpi-box {
  background: #f5f5f5;
  border: 1px solid #ddd;
  padding: 20px;
  text-align: center;
}

.kpi-number {
  font-size: 32px;
  font-weight: bold;
  color: #0066cc;  /* Hardcoded */
}
```

**Impact:**
- Inconsistent form input behavior
- Accessibility issues (small padding)
- Custom components not reusable
- Breaks UNIFIED_THEME visual consistency

---

### 3. DEMO_Unified_Design_System.html (REFERENCE ONLY)

**Issue Severity:** LOW (This is a demonstration file)

**Note:** This file is explicitly a design system reference. Custom styles are justified for demonstration purposes. Should be clearly marked as non-normative template.

---

## Common Patterns of Inconsistency

### 1. Inline Style Overuse (130+ instances across files)

| File | Count | Status |
|------|-------|--------|
| 00_DPDP_Compliance_Journey.html | 86 | Tier 3 |
| 47_Compliance_Status_Report_Board_Pack.html | 44 | Tier 3 |
| 01_Applicability_Test.html | 24 | Tier 2 |
| **Total** | **154+** | |

**Example:**
```html
<p style="font-size: 10px; margin-bottom: 20px;">Answer the three questions...</p>
<div style="background: #f9f9f9; padding: 15px; border-left: 3px solid #0066cc;">
```

**Fix:** Extract to UNIFIED_THEME.css classes like `.text-caption`, `.question-box`

---

### 2. Hardcoded Colors Instead of CSS Variables

| Hardcoded Color | Should Use | UNIFIED_THEME Value |
|-----------------|-----------|-------------------|
| #0066cc | var(--primary-color) | #2563eb |
| #003d99 | var(--primary-dark) | #1e40af |
| #fff3cd | var(--status-warn) | #fffbeb |
| #f8d7da | var(--status-fail) | #fef2f2 |
| #2c3e50 | var(--header-fg) | #0f172a |

**Files Affected:** 00_DPDP_Compliance_Journey.html, 47_Compliance_Status_Report_Board_Pack.html, 01_Applicability_Test.html

---

### 3. Spacing Variable Non-Compliance

**UNIFIED_THEME Defines:**
```css
--spacing-xs: 6px;
--spacing-sm: 12px;
--spacing-md: 20px;
--spacing-lg: 28px;
--spacing-xl: 40px;
--spacing-xxl: 56px;
```

**Found Instead:**
- `padding: 15px` (Tier 2, Tier 3)
- `margin: 10px 0` (Tier 2, Tier 3)
- `padding: 3px` (Tier 3 — accessibility issue)
- `margin: 40px 0` (Tier 3)

---

### 4. Font-Size Fragmentation

**UNIFIED_THEME Semantic Sizes:**
- h1: 28px, h2: 22px, h3: 18px, p: 15px

**Hardcoded Overrides Found:**
- `.title` overridden to 18px, 14px
- `.subtitle` overridden to 12px
- Inline `style="font-size: 10px; 11px; 12px"` throughout Tier 2/3

**Solution:** Add semantic utility classes:
```css
.text-sm { font-size: 12px; }
.text-xs { font-size: 11px; }
.text-caption { font-size: 10px; color: var(--text-light); }
```

---

## Priority Remediation Roadmap

### Priority 1: CRITICAL (Visual Consistency, Maintenance Risk)

**Action Items:**

#### 1a. Refactor 00_DPDP_Compliance_Journey.html
- [ ] Replace `.journey-container` with standard body structure
- [ ] Replace `.journey-header` with `.header` class
- [ ] Migrate 86 inline styles to UNIFIED_THEME.css
- [ ] Replace hardcoded colors (#0066cc, #003d99) with CSS variables
- [ ] Replace hardcoded spacing with --spacing-* variables

**Estimated Effort:** 2-3 hours

---

#### 1b. Refactor 47_Compliance_Status_Report_Board_Pack.html
- [ ] Remove custom input styling (restore UNIFIED_THEME defaults)
- [ ] Create `.kpi-box`, `.kpi-number`, `.kpi-label` in UNIFIED_THEME.css
- [ ] Extract 44+ inline styles to CSS classes
- [ ] Replace hardcoded table header color (#2c3e50 → var(--header-bg))
- [ ] Fix form input padding accessibility issue

**Estimated Effort:** 2-3 hours

---

#### 1c. Extend UNIFIED_THEME.css with Missing Components
```css
/* Add to UNIFIED_THEME.css */

/* Text size utilities */
.text-sm { font-size: 12px; color: var(--text-secondary); }
.text-xs { font-size: 11px; color: var(--text-light); }
.text-caption { font-size: 10px; color: var(--text-light); margin-bottom: var(--spacing-md); }

/* Question/info box component */
.question-box {
  background: var(--primary-light);
  border-left: 3px solid var(--primary-color);
  padding: var(--spacing-md);
  margin: var(--spacing-md) 0;
  border-radius: var(--radius-sm);
}

/* KPI card component */
.kpi-box {
  background: var(--bg-light);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--spacing-lg);
  text-align: center;
}

.kpi-number {
  font-size: 32px;
  font-weight: bold;
  color: var(--primary-color);
  margin-bottom: var(--spacing-xs);
}

.kpi-label {
  font-size: 12px;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
```

**Estimated Effort:** 1 hour

---

### Priority 2: IMPORTANT (Maintenance & Scalability)

**Action Items:**

#### 2a. Migrate Tier 2 Files
Update all 11 files with minor issues:
- [ ] Extract custom `<style>` blocks to UNIFIED_THEME.css
- [ ] Remove hardcoded font-sizes (use semantic classes)
- [ ] Replace hardcoded spacing with --spacing-* variables
- [ ] Replace hardcoded colors with CSS variables

**Files:**
- 01_Applicability_Test.html
- 39-46_*.html (9 files)
- INDEX_DPDP_Compliance_Navigator.html
- INDEX_TEMPLATE_APPLICATION_MAP.html

**Estimated Effort:** 1 hour per file × 11 = 11 hours (parallelizable to 2-3 hours with batch processing)

---

#### 2b. Remove Hardcoded Colors Across Board
- [ ] Search all 50 files for: #0066cc, #003d99, #fff3cd, #f8d7da, #2c3e50
- [ ] Replace with corresponding CSS variables
- [ ] Verify visual consistency in browser

**Estimated Effort:** 1 hour (automated find/replace + verification)

---

### Priority 3: SHOULD (Consistency)

**Action Items:**

#### 3a. Standardize Input/Select/Checkbox Styling
- [ ] Audit all form elements across all 50 files
- [ ] Ensure all use UNIFIED_THEME defaults (no `border-bottom` overrides)
- [ ] Test focus states for accessibility

**Estimated Effort:** 1 hour

---

#### 3b. Document Component Library
- [ ] Create DESIGN_GUIDE.md with all available components
- [ ] Include usage examples for:
  - `.header`, `.info-box`, `.warning-box`, `.critical-box`, `.success-box`
  - `.question-box`, `.kpi-box`, `.phase-block`
  - `.signature-block`, `.signature-item`
  - Text utilities: `.text-sm`, `.text-xs`, `.text-caption`

**Estimated Effort:** 1 hour

---

## Compliance Summary Table

| Aspect | Compliant | Non-Compliant | % |
|--------|-----------|--------------|---|
| UNIFIED_THEME Link | 50/50 | 0/50 | ✓ 100% |
| Header Class Usage | 36/50 | 14/50 | 72% |
| Spacing Variables | 36/50 | 14/50 | 72% |
| Form Defaults | 36/50 | 14/50 | 72% |
| Color Variables | 36/50 | 14/50 | 72% |
| No Custom Containers | 47/50 | 3/50 | 94% |
| Inline Styles <10 | 36/50 | 14/50 | 72% |

---

## Total Effort Estimate

| Phase | Tasks | Hours | Priority |
|-------|-------|-------|----------|
| P1a | Refactor 00_DPDP_Compliance_Journey.html | 2-3 | CRITICAL |
| P1b | Refactor 47_Compliance_Status_Report_Board_Pack.html | 2-3 | CRITICAL |
| P1c | Extend UNIFIED_THEME.css | 1 | CRITICAL |
| **P1 Total** | **3 tasks** | **5-7 hours** | **Phase 1** |
| P2a | Migrate 11 Tier 2 files | 11 (2-3 batch) | IMPORTANT |
| P2b | Replace hardcoded colors | 1 | IMPORTANT |
| **P2 Total** | **2 tasks** | **12-13 hours (2-3 batch)** | **Phase 2** |
| P3a | Standardize form inputs | 1 | SHOULD |
| P3b | Document design guide | 1 | SHOULD |
| **P3 Total** | **2 tasks** | **2 hours** | **Phase 3** |
| **Grand Total** | **7 tasks** | **19-22 hours** | |

---

## Implementation Checklist

### Phase 1 (Critical Refactoring)
- [ ] Add component classes to UNIFIED_THEME.css (.text-*, .question-box, .kpi-box)
- [ ] Refactor 00_DPDP_Compliance_Journey.html (extract 86 inline styles, replace custom container)
- [ ] Refactor 47_Compliance_Status_Report_Board_Pack.html (restore input defaults, extract 44+ inline styles)
- [ ] Test all three files in browser for visual consistency
- [ ] Run `git diff` to verify only styles changed

### Phase 2 (Tier 2 Cleanup)
- [ ] Batch update 11 Tier 2 files (remove `<style>` blocks, use UNIFIED_THEME classes)
- [ ] Global find/replace: #0066cc → var(--primary-color)
- [ ] Global find/replace: hardcoded spacing → variable replacements
- [ ] Test sample files from each category

### Phase 3 (Documentation & Polish)
- [ ] Create DESIGN_GUIDE.md with component library
- [ ] Mark DEMO_Unified_Design_System.html as reference-only
- [ ] Update this audit report with completion status
- [ ] Create PR with all changes

---

## Success Criteria

✓ **95%+ of templates** follow UNIFIED_THEME.css without custom overrides  
✓ **Zero inline `style="..."` attributes** with color/spacing hardcodes  
✓ **All form inputs** use UNIFIED_THEME defaults (consistent focus states)  
✓ **Component library** documented and available for reuse  
✓ **Central theme updates** affect all 50 templates without file-by-file edits

---

## Appendix: Files by Remediation Priority

### Must-Fix (Tier 3)
```
HIGH:  00_DPDP_Compliance_Journey.html
HIGH:  47_Compliance_Status_Report_Board_Pack.html
```

### Should-Fix (Tier 2)
```
MEDIUM: 01_Applicability_Test.html
MEDIUM: 39_Privacy_Committee_Charter.html
MEDIUM: 40_Board_Resolution_Compliance.html
MEDIUM: 41_Compliance_Certificate_Opinion_Letter.html
MEDIUM: 42_Consent_Audit_Worksheet.html
MEDIUM: 43_Statutory_Hold_Register.html
MEDIUM: 44_Cross_Border_Transfer_Register.html
MEDIUM: 45_Ongoing_Obligations_Calendar.html
MEDIUM: 46_DPIA_Register.html
MEDIUM: DEMO_Unified_Design_System.html (Reference - document, don't change)
MEDIUM: INDEX_DPDP_Compliance_Navigator.html
MEDIUM: INDEX_TEMPLATE_APPLICATION_MAP.html
```

### Already Compliant (Tier 1)
```
LOW: All 36 remaining files ✓
```

---

**Report Generated:** April 9, 2026  
**Next Review:** After Phase 1 completion
