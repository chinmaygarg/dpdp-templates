# DPDP Compliance Template Library (41 Templates)

## Overview

This template library provides all 41 compliance templates required for end-to-end DPDP Act 2023 compliance. Templates are organized by phase and category, with status (Existing / New).

**Compliance Deadline:** May 13, 2027  
**Document Version:** 1.1  
**Last Updated:** 2026-04-15

---

## Template Status Summary

| Category | Existing | New | Total |
|----------|----------|-----|-------|
| Governance (6) | 6 | 0 | 6 |
| Data Inventory (3) | 3 | 0 | 3 |
| Notice & Consent (5) | 5 | 0 | 5 |
| Data Principal Rights (6) | 6 | 0 | 6 |
| Vendor Management (5) | 5 | 0 | 5 |
| Breach Management (5) | 5 | 0 | 5 |
| Retention & Deletion (3) | 3 | 0 | 3 |
| Audit & DPIA (4) | 0 | 4 | 4 |
| Audit Reports (1) | 0 | 1 | 1 |
| Compliance Output (3) | 0 | 3 | 3 |
| **TOTAL** | **28** | **13** | **41** |

---

## Phase 1: Governance (Weeks 9-12) — 6 Templates

### 1. Data Protection Policy
**Status:** ✓ Existing  
**File:** `01-Data_Protection_Policy.docx`  
**Description:** Master policy governing all DPDP principles, roles, and compliance obligations  
**Contents:**
- Scope and principles
- Roles and responsibilities
- Processing activities overview
- Rights and duties
- Breach response authority
- Regular review schedule

### 2. Data Retention Schedule
**Status:** ✓ Existing  
**File:** `02-Data_Retention_Schedule.xlsx`  
**Description:** Per-data-category retention periods, legal basis, and deletion triggers  
**Contents:**
- Data category
- Retention period (years/months)
- Legal basis (consent/legitimate/statutory)
- Deletion trigger (purpose completion / consent withdrawal / statutory expiry)
- Responsible owner
- Disposal method (secure delete / archive / etc.)

### 3. Employee Data Protection Policy
**Status:** ✓ Existing  
**File:** `03-Employee_Data_Protection_Policy.docx`  
**Description:** How employee personal data is processed (payroll, HR, training, access logs)  
**Contents:**
- Scope (which employee data collected)
- Purpose per data category
- Retention periods per statutory obligation
- Rights fulfillment procedures
- Employee consent requirements

### 4. DPO Appointment Letter (SDF only)
**Status:** ✓ Existing  
**File:** `04-DPO_Appointment_Letter.docx`  
**Description:** Formal appointment, terms, authority, and published contact  
**Contents:**
- Appointment effective date
- DPO name, qualifications, contact
- Terms of engagement (full-time / part-time)
- Authority scope (DPIA sign-off, audit review)
- Reporting line (Board / Audit Committee)
- Published contact details

### 5. Privacy Committee Charter
**Status:** ⭐ NEW  
**File:** `05-Privacy_Committee_Charter.docx`  
**Description:** Charter for Privacy/Data Protection Committee governance  
**Contents:**
- Committee composition (DPO, Legal, IT, Business, Risk, Audit)
- Meeting frequency (quarterly minimum)
- Decision authority (policy approval, incident escalation, DPIA sign-off)
- Agenda template
- Minutes template

### 6. Board Resolution on Compliance
**Status:** ⭐ NEW  
**File:** `06-Board_Resolution_Compliance.docx`  
**Description:** Formal board acknowledgement of DPDP compliance program and ongoing obligation  
**Contents:**
- Recital: DPDP Act 2023 requirements
- Resolution: Organization is committed to DPDP compliance
- Delegation: Board authorizes DPO/Privacy Committee to execute
- Review: Annual board reporting on compliance status
- Signature block: Board members

---

## Phase 2: Data Inventory (Weeks 5-8) — 3 Templates

### 7. Data Inventory / Asset Register
**Status:** ✓ Existing  
**File:** `07-Data_Inventory_Asset_Register.xlsx`  
**Description:** Master register of all systems holding personal data  
**Columns:**
- System name
- Data categories held (Identifiers / Financial / Health / Behavioral / etc.)
- Purpose
- Legal basis
- Retention period
- Storage location (on-prem / cloud / etc.)
- Third-party access (yes/no)
- Encryption (yes/no)
- Responsible owner
- Last reviewed

### 8. Data Flow Diagram (DFD)
**Status:** ✓ Existing  
**File:** `08-Data_Flow_Diagram.visio` or `.pdf`  
**Description:** Visual map of data movement across systems and boundaries  
**Contains:**
- Data sources (user input / third-party APIs / etc.)
- Processing systems (databases, batch jobs, APIs)
- Data stores (databases, file servers, cloud)
- Third-party recipients (processors, auditors)
- External transfers (cross-border)
- Data deletion points

### 9. Records of Processing Activities (ROPA)
**Status:** ✓ Existing  
**File:** `09-Records_of_Processing_Activities.xlsx` or `.docx`  
**Description:** Formal register per processing activity (Section 5 requirement)  
**Per-Activity Entries:**
- Processing activity name
- Purpose
- Data categories
- Legal basis
- Recipients
- Retention period
- Security measures
- Data subject rights
- DPO sign-off

---

## Phase 3: Notice & Consent (Weeks 10-16) — 5 Templates

### 10. Privacy Notice (per channel)
**Status:** ✓ Existing  
**File:** `10-Privacy_Notice_Web_v3.1.docx`, `10-Privacy_Notice_Mobile.docx`, etc.  
**Description:** Standalone notice per touchpoint (web, mobile, paper, call-centre)  
**Contents (FSIUU-compliant):**
- Standalone document (not buried in T&Cs)
- Data items collected (per-item listing)
- Purpose per item
- Consent form link
- Rights summary (access, correct, erase, nominate, grieve, withdraw)
- DPO contact
- How to withdraw consent
- Language: English + 22 scheduled Indian languages (Rule 3(2))

### 11. Consent Form (per purpose)
**Status:** ✓ Existing  
**File:** `11-Consent_Form_Marketing.docx`, `11-Consent_Form_Analytics.docx`, etc.  
**Description:** Per-purpose consent capture (single-purpose, FSIUU-compliant)  
**Contents:**
- Purpose clearly stated
- Data items for this purpose
- Affirmative action (checkbox / button with explicit consent language)
- No pre-ticked boxes
- Withdrawal instructions (as easy as consent)
- Timestamp capture (when, channel, IP)
- Consent version tracking

### 12. Consent Audit Worksheet
**Status:** ⭐ NEW  
**File:** `12-Consent_Audit_Worksheet.xlsx`  
**Description:** Audit worksheet to test existing consents against 5-element FSIUU test  
**Columns:**
- Consent ID
- Data Principal ID
- Purpose
- Free? (coerced / bundled / Y-N)
- Specific? (blanket / per-purpose / Y-N)
- Informed? (notice provided / Y-N)
- Unconditional? (pre-ticked / conditional / Y-N)
- Unambiguous? (affirmative action / Y-N)
- Overall FSIUU compliant? (Y-N)
- Remediation required? (Y-N)

### 13. Retrospective Notice & Re-consent Template
**Status:** ⭐ NEW  
**File:** `13-Retrospective_Notice_Campaign.docx`  
**Description:** Campaign for handling pre-DPDP data (Section 5(2) compliance)  
**Contents:**
- Letter to existing customers
- What data we hold (itemized)
- New rights under DPDP (access, correct, erase, nominate, grieve, withdraw)
- Re-consent request (per-purpose)
- Withdrawal option
- Campaign timeline
- Completion tracking

### 14. Consent Manager Integration Spec
**Status:** ⭐ NEW  
**File:** `14-Consent_Manager_Integration_Spec.md`  
**Description:** Technical specification for DPDP Rules 2025 Consent Manager integration  
**Covers (from Nov 14, 2026):**
- Government-approved Consent Manager list
- Integration API requirements
- Consent receipt generation
- Cross-organization consent propagation
- Withdrawal propagation
- Audit trail requirements
- Testing procedures

---

## Phase 4: Data Principal Rights (Weeks 12-20) — 6 Templates

### 15. Data Principal Rights Request Form
**Status:** ✓ Existing  
**File:** `15-DSAR_Request_Form.docx` or web form  
**Description:** Form for capturing rights requests (access, correct, erase, nominate, grieve)  
**Fields:**
- Request type (select from: access / correct / erase / nominate / grieve)
- Data principal details (name, email, contact)
- Specific data requested (if access / correct / erase)
- Reason for request
- Preferred response format (email, certified post, PDF, etc.)
- Submission method (web, email, paper)
- Timestamp

### 16. DSAR Response Letter
**Status:** ✓ Existing  
**File:** `16-DSAR_Response_Letter_Templates.docx`  
**Variations:**
- Acknowledgement letter (within 7 days of receipt)
- Access response letter (data exported)
- Correction letter (data corrected, confirmation sent)
- Erasure letter (data deleted, processor confirmations attached)
- Rejection letter (with legal grounds, appeal instructions)

### 17. Erasure / Correction SOP
**Status:** ✓ Existing  
**File:** `17-Erasure_Correction_SOP.docx`  
**Procedure:**
1. Request intake → verify (7 days)
2. Identity verification → authenticate (7 days)
3. Locate data → across systems (30 days)
4. Statutory hold check → PMLA / RBI / IRDAI (5 days)
5. Execute deletion → processor notification (15 days)
6. Confirm deletion → collect processor receipts (15 days)
7. Notify requester → response letter + evidence (by day 90)
8. Log deletion → audit trail hash-chain (ongoing)

### 18. Grievance Handling SOP
**Status:** ✓ Existing  
**File:** `18-Grievance_Handling_SOP.docx`  
**3-Tier Escalation:**
- **Tier 1:** DPO handles (30-day response target)
- **Tier 2:** Internal committee review (30-day response target if appeal)
- **Tier 3:** Data Protection Board complaint (if Tier 2 unresolved after 90 days)

### 19. Nominee Registration Form
**Status:** ✓ Existing  
**File:** `19-Nominee_Registration_Form.docx` or web form  
**Contents:**
- Nominee name, relationship, contact
- Nominee verification (ID proof)
- Scope of rights (full / limited to specific data)
- Registration date
- Revocation instructions

### 20. Statutory Hold Register
**Status:** ⭐ NEW  
**File:** `20-Statutory_Hold_Register.xlsx`  
**Description:** Data that cannot be erased due to legal obligation  
**Columns:**
- Data type (e.g., "KYC documents")
- Applicable law (PMLA / RBI / IRDAI / SEBI)
- Mandatory hold period (5 years / 8 years / etc.)
- Hold expiry date
- Responsible owner
- Review frequency

---

## Phase 4: Vendor Management (Weeks 14-20) — 5 Templates

### 21. Data Processing Agreement (DPA)
**Status:** ✓ Existing  
**File:** `21-Data_Processing_Agreement_Template.docx`  
**Requirements (Section 8(2)):**
- Processor must process only per controller's written instructions
- Processor must ensure sub-processor compliance
- Processor must delete/return data on contract termination
- Processor must provide security safeguards (Section 8(5))
- Processor must notify controller of breaches
- Processor must cooperate with breach investigations
- Processor must facilitate audits

### 22. Vendor Risk Assessment Questionnaire
**Status:** ✓ Existing  
**File:** `22-Vendor_Risk_Assessment_Questionnaire.docx`  
**Sections:**
- Organization details (name, location, jurisdiction)
- Data processing scope (what data, what systems)
- Security posture (encryption, access controls, pen-testing)
- Certifications (ISO 27001, SOC 2, etc.)
- Breach history (past incidents, resolution)
- Subcontractors (list of data recipients)
- References

### 23. Sub-Processor Register
**Status:** ✓ Existing  
**File:** `23-Sub_Processor_Register.xlsx`  
**Columns:**
- Sub-processor name
- Data categories shared
- Processing location
- Approval date
- Contract reference
- Contact for escalations

### 24. Cross-Border Transfer Register
**Status:** ⭐ NEW  
**File:** `24-Cross_Border_Transfer_Register.xlsx`  
**Columns:**
- Destination country
- Data categories transferred
- Legal basis (adequacy / contractual safeguards / etc.)
- Contractual safeguards (yes/no) + reference
- Government notification status (restricted country list monitoring)
- Transfer date
- Responsible owner

### 25. Third-Party Inventory
**Status:** ✓ Existing  
**File:** `25-Third_Party_Inventory.xlsx`  
**Columns:**
- Vendor name
- Data categories shared
- Purpose of sharing
- Processing location
- DPA status (signed / pending)
- Risk rating (low / medium / high)
- Last security assessment date

---

## Phase 5: Breach Management (Weeks 16-22) — 5 Templates

### 26. Incident Response Plan (IRP)
**Status:** ✓ Existing  
**File:** `26-Incident_Response_Plan.docx`  
**Procedures:**
- Detection (automated alerting, manual reporting)
- Triage (severity classification: Critical / High / Medium / Low)
- Containment (isolation, evidence preservation)
- Notification (DPB ≤72 hrs, CERT-In ≤6 hrs if applicable, principals ASAP)
- Post-incident (root cause analysis, remediation, lessons learned)
- Roles & responsibilities (incident commander, DPO, legal, comms, tech)
- Contact list (DPB email, CERT-In hotline, media, insurance)

### 27. Breach Notification Template — DPB (72-hour)
**Status:** ✓ Existing  
**File:** `27-Breach_Notification_DPB.docx`  
**Contents:**
- Breach date and detection date
- Nature of breach
- Data categories affected (Identifiers / Financial / Health / etc.)
- Approximate number of Data Principals affected
- Likely consequences (identity theft / financial / etc.)
- Measures taken so far (containment, investigation)
- DPO contact for follow-up

### 28. Breach Notification Template — Data Principal
**Status:** ✓ Existing  
**File:** `28-Breach_Notification_Principal.docx`  
**Contents (plain language):**
- What happened (description in non-technical language)
- What data was affected
- When it was detected
- What risk does it pose to the individual
- What steps the individual should take (change passwords, monitor credit, etc.)
- How to contact the Organization (DPO)
- How to file a grievance

### 29. Breach Register
**Status:** ✓ Existing  
**File:** `29-Breach_Register.xlsx`  
**Columns:**
- Incident ID
- Detection date & time
- Nature of breach
- Data categories affected
- Approximate principals affected
- DPB notification timestamp (must be ≤72 hrs)
- CERT-In notification timestamp (if applicable, ≤6 hrs)
- Principal notification timestamp
- Root cause
- Remediation status
- Resolution date

### 30. Post-Breach Review Template
**Status:** ✓ Existing  
**File:** `30-Post_Breach_Review.docx`  
**Contents:**
- Timeline (detection → notification → resolution)
- Root cause analysis
- Systemic weaknesses identified
- Corrective actions (preventive, technical, process)
- Owner & completion date per action
- Board/Committee presentation summary
- Insurance/legal implications

---

## Phase 6: Retention & Deletion (Weeks 18-22) — 3 Templates

### 31. Retention Schedule
**Status:** ✓ Existing  
**File:** `31-Retention_Schedule.xlsx`  
**See Template #2 (Data Retention Schedule)** — same document covers both governance and operational retention planning.

### 32. Deletion Log
**Status:** ✓ Existing  
**File:** `32-Deletion_Log.xlsx`  
**Columns:**
- Deletion event ID
- Data categories deleted
- Number of records deleted
- Trigger (purpose completion / consent withdrawal / retention expiry / erasure request)
- Systems affected
- Deletion timestamp
- Verification method (secure delete / archive)
- Responsible owner
- Audit hash

### 33. Processor Deletion Confirmation Template
**Status:** ✓ Existing  
**File:** `33-Processor_Deletion_Confirmation.docx`  
**Instruction Format:**
- Issued to: [Processor name]
- Data subject IDs: [list or batch]
- Data categories: [specify]
- Deletion deadline: [within X days]
- Confirmation required: [signed receipt + timestamp]
- Sub-processor notification: [yes/no]

---

## Phase 6: Validation & Certification (Weeks 25-40) — 7 Templates

### 34. Compliance Audit Plan & Checklist
**Status:** ✓ Existing  
**File:** `34-Compliance_Audit_Plan_Checklist.docx` or `.xlsx`  
**Covers:**
- ROPA completeness
- Notice compliance (standalone, multilingual, per-purpose)
- Consent quality (FSIUU test on sample)
- Rights fulfillment (SLA on sample requests)
- DPA execution (100% coverage)
- Breach process (tabletop test)
- Security controls (evidence review + spot checks)
- Training records (coverage and recency)

### 35. Audit Findings Report
**Status:** ✓ Existing  
**File:** `35-Audit_Findings_Report.docx`  
**Per Finding:**
- Finding ID
- Domain (Governance / Data Inventory / Notice / etc.)
- Description
- Severity (Critical / High / Medium / Low)
- Root cause
- Remediation recommendation
- Owner & due date
- Evidence references

### 36. DPIA Workbook (SDF only)
**Status:** ⭐ NEW  
**File:** `36-DPIA_Workbook_Template.docx` or `.xlsx`  
**Sections:**
- Processing activity description
- Purpose & necessity assessment
- Proportionality analysis
- Risk identification (likelihood × impact per DPDP section)
- Risk mitigation measures
- Residual risk statement
- DPO sign-off
- Board approval & submission date

### 37. DPIA Register (SDF only)
**Status:** ⭐ NEW  
**File:** `37-DPIA_Register.xlsx`  
**Columns:**
- DPIA ID
- Processing activity
- Risk level (High / Medium / Low)
- Completion date
- DPO sign-off date
- Board approval date
- Next review date
- Status (current / pending renewal)

### 38. Compliance Status Report (Board Pack)
**Status:** ⭐ NEW  
**File:** `38-Compliance_Status_Report_Board_Pack.docx` or `.pptx`  
**Contents:**
- Executive summary (overall compliance status: Compliant / Conditional / Non-Compliant)
- Domain scores (17 domains on radar chart)
- Critical findings (if any)
- Open risks
- Certifications/opinions issued
- Ongoing obligations timeline
- Recommendations for next 12 months

### 39. Compliance Certificate / Opinion Letter
**Status:** ⭐ NEW  
**File:** `39-Compliance_Certificate_Opinion_Letter.html` (created above)  
**See above**

### 40. Ongoing Obligations Calendar
**Status:** ⭐ NEW  
**File:** `40-Ongoing_Obligations_Calendar.xlsx` or `.ics`  
**Entries:**
- Annual compliance review (Q2 or specified month)
- Consent audit (sample verification)
- DPIA review (for new high-risk processing)
- Independent audit (SDF only)
- Staff training refresher
- Regulatory monitoring & policy updates
- Retrospective re-consent campaign (if pre-DPDP data exists)

---

## Phase 7: Comprehensive Audit Reporting (Weeks 24-40) — 1 Template

### 49. DPDP Compliance Audit Report (Regulator-Grade)
**Status:** ⭐ NEW  
**File:** `49_DPDP_Compliance_Audit_Report.html`  
**Description:** Comprehensive regulator-grade compliance audit report covering all 17 DPDP domains with 92-checkpoint assessment methodology  
**Contains:**
- **Cover Page:** Organization details, audit period, report date, confidentiality notice
- **Executive Summary:** Overall compliance score (0–100), domain compliance status (compliant/partial/non-compliant), findings summary, audit findings highlights
- **Section 1–17 Domain Assessment:** Individual sections for each DPDP compliance domain:
  1. Consent & Notice (FSIUU) — Section 6
  2. Data Inventory & ROPA — Section 5
  3. Information Security (AES-256, TLS 1.2+) — Section 8(5)
  4. Breach Notification (72h to DPB) — Section 8(6)
  5. Data Principal Rights (DSAR, correction, erasure, etc.) — Section 11–14
  6. Third-Party & DPA — Section 8(2)
  7. Retention & Deletion — Section 8(7)
  8. DPO & Governance — Section 8, Rule 5
  9. DPIA & Legitimate Uses — Section 7, Rule 6
  10. Children's Data Protection — Section 9
  11. Cross-Border Transfers — Section 17
  12. Grievance Redressal (3-tier escalation) — Section 15
  13. Data Processing Activities — Section 5, 8
  14. Training & Awareness — Section 8
  15. Audit Trail & Logging (hash-chained) — Section 8
  16. Data Quality & Accuracy — Section 8
  17. Incident Response & Continuity — Section 8
- **Key Metrics Dashboard:**
  - Consent metrics (total principals, active/withdrawn consents, compliance %)
  - Data principal rights metrics (DSAR, correction, erasure, grievance response times)
  - Security metrics (encryption, breach incidents, vulnerability assessments)
  - Retention & deletion metrics (data deleted, audit trail integrity, statutory holds)
- **Findings & Remediation Roadmap:**
  - CRITICAL findings (30-day SLA, ₹50–100 Cr penalty exposure)
  - HIGH findings (60-day SLA, ₹25–50 Cr penalty exposure)
  - MEDIUM findings (90-day SLA, ₹10–25 Cr penalty exposure)
  - LOW findings (no deadline, process improvement)
- **DPDP Act 2023 Compliance Checklist:** Section-by-section verification checklist for Sections 5–17, Rule 5–6
- **Audit Methodology & Scope:** Framework, audit approach per domain, sample sizes, audit timeline, team roles
- **Risk Assessment Matrix:** Current risk levels, mitigation status, residual risk per area
- **Board Recommendations & Next Steps:** Approval decisions, resource allocation, quarterly review schedule, ongoing obligations
- **Auditor Declaration & Sign-Off:** Auditor signatures, management confirmation
- **Appendix A:** Cross-reference to related templates in the library

**Integration:**
- Backend API: `POST /api/v1/compliance-audits/:orgId/comprehensive-report` — Generates report from live database
- Admin UI page: `/admin/dashboard/audit-reports` — View, download, export reports
- Backend service: `AuditReportGenerator` (audit-report-generator.ts) — Queries all compliance domains and metrics
- Shared types: `AuditReport`, `ComplianceDomain`, `AuditFinding`, `ComplianceMetrics` (audit-report.ts)
- Validators: `auditReportSchema`, `auditReportInputSchema` (audit-report.ts)

**Usage:**
- Quarterly/annual compliance verification for internal board reporting
- External auditor/compliance consultant deliverable
- Data Protection Board (DPB) submission upon inspection/complaint
- Regulatory confidence demonstration
- Remediation roadmap tracking and execution
- Ongoing obligations calendar alignment

**Regulatory References:**
- DPDP Act, 2023 Sections 5–17, Rules 2025
- Data Protection Board guidelines
- Industry standard: CERF (Compliance Enablement Reference Framework)

---

## How to Use This Library

### For Consultants:

1. **Download existing templates** from `docs/cerf-templates/template/` (files 1-37, excluding new ones)
2. **Review new templates** (files 38-40, 49) — ready to use, customize with org data
3. **Customize per client:**
   - Replace `[Organization Name]` placeholders
   - Populate checklists with org-specific data
   - Collect evidence per domain
4. **Populate systematically:**
   - Phase 1: Governance (weeks 1-3)
   - Phase 2: Data Inventory (weeks 3-6)
   - Phase 3: Notice & Consent (weeks 6-10)
   - Phase 4: Rights & Vendor (weeks 10-16)
   - Phase 5: Breach & Retention (weeks 12-18)
   - Phase 6: Validation (weeks 18-24)
   - Phase 7: Audit Reporting (weeks 24-40) — Generate Template #49 upon completion
5. **Issue compliance opinion** using Template #39 once all 13 mandatory criteria met
6. **Generate comprehensive audit report** using Template #49 (backend-driven, auto-populated from database)
7. **Schedule ongoing obligations** using Template #40

### For Organizations:

1. **Receive templates** from consultant in fillable formats (DOCX / XLSX / HTML)
2. **Assign owners** per category:
   - Governance → DPO / Legal
   - Data Inventory → IT / Business
   - Notice & Consent → Product / Marketing
   - Rights → Operations
   - Vendor → Procurement / Legal
   - Breach → Security / DPO
   - Validation → Audit / DPO
   - Audit Reporting → DPO / Auditor
3. **Complete templates** per timeline
4. **Collect evidence** and store in indexed folder (per domain)
5. **Prepare for audit** using Audit Checklist (Template #34)
6. **Generate comprehensive audit reports** quarterly/annually via API (`POST /api/v1/compliance-audits/:orgId/comprehensive-report`)
7. **Track remediation** progress from Template #49 findings against Ongoing Obligations (Template #40)
8. **Maintain ongoing** per Obligations Calendar (Template #40)

---

## Regulations Covered

| Template | Section | Reg | Category |
|----------|---------|-----|----------|
| 1-6 | S.8 | Data Protection Policy | Governance |
| 7-9 | S.5 | Data Inventory & Mapping | ROPA |
| 10-14 | S.5, S.6 | Notice & Consent | Transparency |
| 15-20 | S.11-14 | Data Principal Rights | DSAR |
| 21-25 | S.8(2), S.16 | Vendor Management | Third-Party |
| 26-30 | S.8(6) | Breach Management | Incident Response |
| 31-33 | S.8(7) | Retention & Deletion | Data Governance |
| 34-37 | S.10 | Audit & DPIA | SDF Obligations |
| 38-40 | All | Compliance Output | Certification |
| 49 | S.5-17, R.5-6 | Comprehensive Audit Report | Audit Reporting |

---

## Support & Questions

For template customization questions, contact:
- **Consultant:** [contact]
- **Organization DPO:** [contact]
- **Data Protection Board (queries):** [email / portal]
- **Regulatory references:** [DPDP Act 2023 URL], [Rules 2025 URL]

---

**Document end. Print-friendly version available on request.**
