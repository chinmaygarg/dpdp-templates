# Phase 1: Assessment — Data Inventory, ROPA, Data Flows

**Duration:** Weeks 1-8 (January-March 2026) | **Effort:** 6-8 weeks | **Owner:** DPO, Data Governance, Product | **Templates:** T-03 to T-09

---

## Overview

Phase 1 establishes the **baseline of all data processing activities** within your organization. This data inventory and ROPA (Records of Processing Activities) serve as the foundation for all subsequent compliance work.

---

## Step 1: System Audit & Data Inventory (T-03)

**Objective:** Catalog all systems, databases, and applications holding personal data.

### System Categories to Audit:
- **Operational DBs:** Core customer, transaction, employee databases
- **Cloud Storage:** AWS, Azure, GCP buckets; SaaS platforms
- **Analytics Platforms:** Data warehouses, BI tools, ML platforms
- **Third-Party APIs:** CRM, payment processors, communication platforms
- **Backup/Archive:** Backup systems, offline storage, disaster recovery

### For Each System, Document:
- System name & owner
- Data categories stored (identifiers, financial, health, etc.)
- Individuals affected (# of records)
- Retention period
- Security controls (encryption, access control)
- Sub-processors or third-party vendors

**Deliverable:** Data Inventory Asset Register (T-03)

---

## Step 2: Data Flow Diagram (T-04)

**Objective:** Map how personal data moves between systems, departments, and external parties.

### Create Visual Diagram Showing:
- Data entry points (customer registration, API, import)
- Storage locations
- Processing steps (analytics, fraud detection, decisioning)
- Sharing with processors/vendors
- Deletion/archival process
- Parallel flows for different data categories

**Template:** Use T-04 Data Flow Diagram template.

---

## Step 3: Records of Processing Activities — ROPA (T-05)

**Objective:** Document every processing activity per DPDP Section 5.

### ROPA Mandatory Fields:

| Field | Description | Example |
|---|---|---|
| **Processing Activity ID** | Unique ID per activity | PA-001-CUSTOMER-ONBOARDING |
| **Data Categories** | What personal data | Name, Email, Aadhaar, Income |
| **Legal Basis** | Section 6 (consent) or Section 7(i-ix) | S.6 (consent), S.7(ii) (statutory KYC) |
| **Purpose** | Why data is processed | Account creation, KYC verification |
| **Recipients** | Who the data is shared with | RBI (AML reporting), Credit bureau |
| **Retention Period** | How long stored | 10 years (RBI requirement) |
| **Security Measures** | Controls in place | AES-256 encryption, access logs |

**Deliverable:** Complete ROPA document (T-05) signed by DPO.

---

## Step 4: Legitimate Uses Documentation (T-06)

**Objective:** Justify Section 7 processing without consent.

For each Section 7 use case (employment, KYC/AML, fraud detection, etc.), prepare:
- Legal ground (which Section 7 sub-section)
- Necessity justification
- Data minimization statement
- Purpose limitation clause

**Deliverable:** Section 7 Legitimate Uses Memo (T-06) reviewed by Legal.

---

## Step 5: Privacy Notice Review & Update (T-07)

**Objective:** Deploy DPDP-compliant privacy notice.

### Required Sections:
- Data Controller identity
- Data categories collected
- Legal bases (S.6 consent, S.7 legitimate use)
- Data subject rights (Access, Correction, Erasure, Withdrawal)
- Recipient list (processors/third parties)
- Retention periods
- Security measures
- Breach notification procedure
- DPO contact

**Deliverable:** Updated Privacy Notice (T-07) published on website.

---

## Step 6: Consent Form Review & Redesign (T-08)

**Objective:** Implement FSIUU (Free, Specific, Informed, Unconditional, Unambiguous) consent.

### FSIUU Checklist (All 5 Must = Valid):
- [ ] **Free?** Not bundled with service access; can consent to service without marketing consent
- [ ] **Specific?** Per-purpose checkboxes (Account Mgmt ≠ Marketing ≠ Analytics)
- [ ] **Informed?** Privacy notice provided before consent request
- [ ] **Unconditional?** No penalty for declining (except mandatory uses)
- [ ] **Unambiguous?** Not pre-ticked; clear yes/no; no double negatives

**Deliverable:** FSIUU-compliant Consent Form (T-08) deployed in product.

---

## Step 7: Retrospective Consent Review (T-09)

**Objective:** Audit all existing consents for FSIUU validity.

### Review Process:
1. Pull all consents from past 3 years
2. Sample 100+ records per data category
3. Score each against FSIUU (0-5 points; all 5 required for valid)
4. If >5% invalid: Re-consent affected principals
5. Document findings in T-09 Retrospective Consent Review

**Deliverable:** T-09 Retrospective Review report; re-consent plan if needed.

---

## Phase 1 Deliverables Checklist

- [ ] T-03: Data Inventory Asset Register (all systems cataloged)
- [ ] T-04: Data Flow Diagram (visual map)
- [ ] T-05: ROPA document (all processing activities documented)
- [ ] T-06: Section 7 Legitimate Uses Memo (consent-free uses justified)
- [ ] T-07: Privacy Notice updated and deployed
- [ ] T-08: FSIUU Consent Form deployed
- [ ] T-09: Retrospective Consent Review (existing consents audited)
- [ ] **Board Sign-Off:** DPO certified Phase 1 complete

---

**Reference:** [PHASE_1_ROPA_PREPARATION_GUIDE.md](./PHASE_1_ROPA_PREPARATION_GUIDE.md) for detailed ROPA guidance.

→ [Next: Phase 2 Gap Analysis](./03_PHASE_2_GAP_ANALYSIS.md)

---

**Owner:** DPO | **Board Approval:** [Date/Signature]
