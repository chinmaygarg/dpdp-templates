# DPDP Implementation Strategy — Master TODO
**Updated:** April 15, 2026 | **Source:** 92-Checkpoint Gap Analysis vs dataRakshaq competitor
**Compliance Deadline:** 13 May 2027

---

## PROGRESS SUMMARY (as of April 15, 2026)

### ✅ COMPLETED: 10 of 10 Tier 1 Critical Templates (100% DONE ✓✓✓)

| Template | Gap Closed | Status | Lines |
|----------|-----------|--------|-------|
| ✅ **A1: T-11 DSAR Response** | 30-day SLA, 48-hr ACK, 6 rights, identity verification, DPBI escalation | DONE | 350 |
| ✅ **A2: T-20 Incident Response** | CERT-In 6-hr + DPBI 72-hr dual-timer, 6 breach scenarios, SIEM, tabletop | DONE | 550 |
| ✅ **A3: T-21A CERT-In Breach (NEW)** | Complete CC-5 Form, 9 sections, 6-hour SLA, 10 incident types | DONE | 420 |
| ✅ **A4: T-12 Erasure & Correction** | Propagation SLA, Section 12(4) processor notification, legal exceptions | DONE | 420 |
| ✅ **A5: T-08 Consent Form** | FSIUU 5-attribute validity scoring, granular purposes, CPaaS/LSP, withdrawal | DONE | 380 |
| ✅ **A6: T-24 Security Hardening** | Aadhaar VID + PAN masking rules, encryption, pentest, DAM, SIEM, MFA, zero trust | DONE | 550 |
| ✅ **A7: T-33 Encryption Checklist** | India-specific rules: Aadhaar VID only (no 12-digit), PAN masking to last 4 | DONE | +240 |
| ✅ **A8: T-35 Audit Logging** | PII redaction, INSERT-only immutable logs, hash-chained, 7-year WORM archive | DONE | 520 |
| ✅ **A9: T-02A Data Retention** | RBI 10-year KYC (updated from 5yr), 8-year loans, 90-day CCTV standard | DONE | +80 |
| ✅ **A10: T-10 DSAR Form** | Identity verification (5 methods), 6 data rights, 48-hr ACK, portability, request tracking | DONE | 420 |

**Total Content Created:** ~4,620 lines of comprehensive compliance procedures + templates

---

## PART A — Template Updates (50 existing HTML files)

> **Key Finding:** 25 of 50 templates are 72-line skeletons (header + generic checklist only).
> They need full content written. The remaining 25 have substance but specific gaps to close.
>
> **Progress:** 5 of 10 Tier 1 critical templates complete. Estimated 1-2 more sessions to finish all 36 Part A updates.

---

### TIER 1 — Critical Updates (Legal / Penalty Exposure)

These gaps create direct ₹50–₹250 Cr penalty exposure. Fix first.

---

#### ✅ A1. `11_DSAR_Response_Letter.html` — Fix SLA Discrepancy [COMPLETED]
**Gap:** Template currently says "90-day SLA". DPDP/competitor says **30-day response + 48-hour ACK**.
**Also missing:** Data portability right, identity verification reference, DPBI escalation path.

Updates completed:
- [x] Changed all references from "90-day" to **30-day SLA** (pending Rules 2025 final publication)
- [x] Added **48-hour automated acknowledgement** section with Request ID, expected completion date, tracking link
- [x] Added **Data Portability** as Section 13 right alongside access, correction, erasure, nomination, grievance (6 rights total)
- [x] Added **Identity Verification** section with 5 methods: account login+OTP, Aadhaar VID, email callback, PAN+DOB, video KYC
- [x] Added **DPBI Escalation** section with 60-day DPO response SLA and DPBI complaint portal link
- [x] Created complete response letter template with: Request ID, verification confirmation, data formats (CSV/JSON/PDF), 6 rights section, portability explanation, DPBI escalation path
- [x] Added **27-item implementation checklist** including portal, automation, SLA monitoring
- [x] **Size: ~350 lines** (vs 72-line skeleton)

---

#### ✅ A2. `20_Incident_Response_Plan.html` — Add CERT-In + Dual-Timer [COMPLETED]
**Gap:** Template is a 72-line skeleton. Zero actual incident response content.
**Critical missing:** CERT-In 6-hour SLA, dual-timer breach command, SIEM, tabletop exercise.

Updates completed:
- [x] Created **Breach Classification Matrix** — 8 incident types × severity (data leak, ransomware, DDoS, malware, config error, insider, phishing, auth failure)
- [x] Created **Dual-Timer Breach Command Structure** — T+0 through T+30d with CERT-In (6-hr) and DPBI (72-hr) separated and mandatory
- [x] Added **CERT-In Notification Details** — Form CC-5, incident types, 6-hour SLA, CERT-In vs DPBI distinction
- [x] Created **Incident Commander Role & Authority** — responsibilities by phase, escalation authority, selection criteria
- [x] Created **6-Step Containment Playbook** — data exfiltration, ransomware, vendor breach, config error, insider threat, brute force with procedures
- [x] Added **Evidence Preservation & Chain of Custody** — forensics, disk imaging, log preservation, admissibility in court
- [x] Created **10 SIEM Alert Rules** — large data export, privilege escalation, ransomware pattern, unauthorized access, bulk deletion, etc.
- [x] Created **Annual Tabletop Exercise** — 2-3 hour drill structure with ransomware scenario walkthrough, lessons learned process
- [x] **33-item implementation checklist** — pre-incident preparation, during-incident execution, post-incident recovery
- [x] **Size: ~550 lines** (vs 72-line skeleton) — most comprehensive incident response template

---

#### ✅ A3. NEW: `21A_Breach_Notification_CERT-In.html` — Create New Template [COMPLETED]
**Gap:** We only have T-21 for DPBI (72-hr). CERT-In is a separate authority with a **6-hour SLA**.
**CERT-In is mandatory for ALL cybersecurity incidents** — regardless of personal data impact.

Template created:
- [x] Complete CERT-In incident reporting structure with 9 sections (9 sections covering organization, incident, systems, impact, attack, response, communication, vulnerability, contact)
- [x] 6-hour countdown timer prominently displayed with alarm trigger at T+5hr
- [x] Organization details, incident description, systems affected (table with IP, OS, services)
- [x] Attack vector classification (phishing, vulnerability, exposed RDP, misconfiguration, supply chain, physical, insider, unknown)
- [x] Data involved assessment (volume, categories, geographic distribution)
- [x] Containment steps checklist (isolation, revocation, patching, monitoring, restoration)
- [x] Multiple point of contact details (CISO, Incident Commander, follow-up contact)
- [x] Cross-reference to DPBI notification (T-21) with clear distinction: CERT-In for ALL incidents, DPBI for data breaches only
- [x] Added to `00_COMPLETE_TEMPLATE_MANIFEST.md` as **T-21A (NEW)**
- [x] Referenced in `20_Incident_Response_Plan.html` with CERT-In vs DPBI comparison table
- [x] **Size: ~420 lines** — entirely new template addressing critical gap

---

#### ✅ A4. `12_Erasure_and_Correction_SOP.html` — Add Propagation SLA [COMPLETED]
**Gap:** 72-line skeleton. Missing 24-hr withdrawal propagation, downstream erasure cascade.

Updates completed:
- [x] Created **Correction vs Erasure Comparison Table** — 2 distinct rights, both with 30-day SLA
- [x] Created **30-Day SLA Timeline** — T+0 through T+30 with 7 checkpoints (receive, verify, assess, search, execute, propagate, confirm)
- [x] Created **7-Step Correction Process** — receive → verify → assess → search → execute → **propagate to processors** → confirm
- [x] Created **8-Step Erasure Process** — same plus Step 3: identify legal exceptions (RBI, litigation, DPIA, tax)
- [x] **CRITICAL: Processor & Third-Party Propagation (Section 12(4))** — most-overlooked requirement
  - [x] Processor identification checklist (Data Processing Agreement T-24)
  - [x] Standardized notification templates for correction and erasure
  - [x] 5-business-day confirmation SLA from processors
  - [x] Sub-processor notification requirement
  - [x] Escalation if non-responsive
- [x] Created **Legal Exceptions Documentation** — RBI retention (8yr loans, 10yr KYC), tax records (8yr), litigation holds, DPIA findings
- [x] Created **Exception Notification Letter Template** — how to tell Data Principal why erasure is denied
- [x] Created **Correction & Erasure Tracker Schema** — 12 fields for DPBI audit proof (principal_id, received_date, processed_date, processors_confirmed_date, status, exception_reason, processors_list)
- [x] **27-item Implementation Checklist** — process, identity verification, tracker database, SOP documentation, processor register, notification templates, exception framework, legal hold process, 30-day monitoring
- [x] **Size: ~420 lines** (vs 72-line skeleton)

---

#### A5. `08_Consent_Form.html` — Add Technical Consent Spec 🔴
**Gap:** Has good FSIUU form content but missing the technical record requirements (CM-05/06/07/09).

Updates required:
- [ ] Add **Section: Technical Consent Record Requirements** after the form:
  ```
  Every consent capture must create one row in consent_records table with:
  - consent_id (UUID, primary key)
  - data_subject_id (customer/employee ID)
  - purpose_code (ONE per row — never multi-purpose)
  - consent_profile_id (CP-001 to CP-021)
  - ropa_activity_id (links to ROPA entry)
  - consent_timestamp (UTC, immutable)
  - channel (app / web / branch / AA / partner)
  - ip_address (IPv4 or IPv6)
  - notice_version (e.g. PN-v2.3)
  - consent_text_hash (SHA-256 of exact text shown)
  - is_active (BOOLEAN — FALSE on withdrawal or expiry)
  - withdrawal_timestamp (NULL until withdrawn, immutable once set)
  - is_minor (TRUE if data subject < 18)
  - s6_validity_score (0–100 computed score)
  ```
- [ ] Add **S.6 Validity Score Methodology** — 5-attribute scoring table:
  | Attribute | Score | Check |
  |-----------|-------|-------|
  | Free (no coercion) | 20 | Checkbox default = OFF |
  | Specific (one purpose) | 20 | Single purpose code per record |
  | Informed (notice shown) | 20 | notice_version populated |
  | Unconditional | 20 | Not bundled with service delivery |
  | Unambiguous (affirmative) | 20 | Explicit checkbox tick, not implied |
  | **Total** | **100** | **< 80 = non-compliant** |
- [ ] Add **NBFC Consent Profile Reference** — table of 21 profiles (CP-001 to CP-021) with product type
- [ ] Add **5 Critical Implementation Rules** from 92-checkpoint doc (R1–R5)
- [ ] Add **Purpose Code Library** (PC-001 to PC-025) reference table

---

#### A6. `24_Security_Hardening_Plan.html` — Full Content 🔴
**Gap:** 72-line skeleton. Missing pentest, VA/PM, DAM, SIEM, Aadhaar VID, PAN masking.

Full content to write:
- [ ] **Aadhaar VID Compliance** rule: "12-digit Aadhaar number NEVER stored. VID only."
- [ ] **PAN Masking** rule: "PAN masked to XXXXXXX1234 in all logs, displays, API responses"
- [ ] **Encryption Standards** table: AES-256-GCM at rest, TLS 1.2+ in transit, key rotation schedule
- [ ] **Annual Penetration Testing** section:
  - OWASP Top 10 scope
  - Accredited third-party requirement
  - Remediation SLA: Critical 7d, High 30d, Medium 90d
  - Results to Board report
- [ ] **Vulnerability & Patch Management** — patch SLA table per severity
- [ ] **Database Activity Monitoring (DAM)** — alert rules: bulk export, schema changes, after-hours
- [ ] **SIEM Requirements** — systems to integrate, alert rules, breach trigger thresholds
- [ ] **MFA Requirements** — which roles require MFA, enforcement method
- [ ] **Zero Trust / Least Privilege** — access review cadence (quarterly)
- [ ] **Security Review Calendar** — annual pentest, quarterly access review, monthly vulnerability scan

---

#### A7. `33_Encryption_Implementation_Checklist.html` — Add Aadhaar VID + PAN 🔴
**Gap:** Has real content (241 lines) but missing specific Aadhaar VID and PAN masking requirements.

Updates required:
- [ ] Add new section **"India-Specific Regulatory Encryption Rules"**:
  - [ ] **Aadhaar:** Store only Virtual ID (VID). 12-digit Aadhaar number = NEVER persisted. Hash if needed for deduplication.
  - [ ] **PAN:** Mask to last 4 digits (XXXXXXX1234) in ALL displays, logs, API responses, exports
  - [ ] **Bank Account:** Mask to last 4 digits in displays; full number only in payment processing systems with restricted access
  - [ ] **Mobile Number:** Mask middle digits (XXXXX6789) in non-operational displays
- [ ] Add **Sensitive Data Field Registry** — table of PII fields and their masking/encryption rule

---

#### A8. `35_Audit_Logging_Configuration.html` — Add PII Redaction + Immutability 🔴
**Gap:** 72-line skeleton. Missing PII log redaction, INSERT-only enforcement, 7-year retention.

Full content to write:
- [ ] **PII Redaction Rules** — regex patterns to scrub before logging:
  - Aadhaar: replace 12-digit with [AADHAAR-REDACTED]
  - PAN: replace with [PAN-REDACTED]
  - Phone: mask middle digits
  - Email: mask to f***@domain.com
  - Bank account: mask to [ACCOUNT-REDACTED]
- [ ] **Immutable Audit Log Requirements**:
  - INSERT-only permissions (no UPDATE/DELETE on audit_log)
  - Hash-chained rows (each row includes SHA-256 of previous row)
  - Archive to write-once storage (S3 Object Lock / WORM) after 90 days
  - 7-year minimum retention (per SS-09 checkpoint)
- [ ] **Events to Log** — mandatory events list: login, logout, data access, data export, consent change, DSAR, deletion
- [ ] **Database Activity Monitoring (DAM)** integration — link to T-24
- [ ] **Log Retention Schedule** — operational (90 days hot), archive (7 years cold)
- [ ] **Alert Rules** — anomaly thresholds that trigger breach response

---

#### A9. `02A_Data_Retention_Schedule.html` — Fix RBI Period + Add CCTV 🔴
**Gap:** Has real content (504 lines) but:
1. RBI retention may be wrong (our guide says 8yr, 92-checkpoint says 10yr)
2. CCTV 90-day retention completely missing

Updates required:
- [ ] **Verify and correct RBI retention period** — check RBI Master Direction on KYC (expected: 10 years for KYC records, 8 years for loan records — these differ). Update the table rows accordingly with specific RBI circular reference
- [ ] **Add CCTV / Physical Surveillance row**:
  | Category | Retention | Legal Basis | Deletion Method |
  |----------|-----------|-------------|-----------------|
  | CCTV footage | 90 days | S.7(a) Observable data | Automated purge |
  | Branch access logs | 1 year | Security requirement | Secure deletion |
  | Physical visitor register | 1 year | Security requirement | Shredding |
- [ ] **Add Payroll clarification** — 7-year floor (tax law), not 10 years

---

#### A10. `10_Data_Subject_Access_Request_(DSAR)_Form.html` — Add ID Verify + Portability 🔴
**Gap:** 72-line skeleton. Missing identity verification step, portability right, 48-hr ACK.

Full content to write:
- [ ] **Identity Verification Gate** — before form is processed:
  - Verify via: OTP to registered mobile/email, OR Aadhaar VID match, OR registered account + DOB
  - Log verification method and timestamp
  - Reject and re-verify if identity cannot be confirmed
- [ ] **6 Rights Selection** (checkboxes):
  - [ ] Access — receive summary of data processed
  - [ ] Correction — fix inaccurate data
  - [ ] Erasure — delete my data (subject to statutory holds)
  - [ ] Portability — receive data in machine-readable format (JSON/CSV)
  - [ ] Nomination — designate nominee for data rights
  - [ ] Grievance — raise a complaint
- [ ] **48-Hour Acknowledgement** commitment notice on form submission
- [ ] **Request tracking fields** — Request ID, submission date, expected completion date, status updates

---

### TIER 2 — Important Updates (Compliance Gaps)

---

#### A11. `13_Grievance_Handling_SOP.html` — Add DPBI Escalation 🟡
**Gap:** 72-line skeleton. DPBI escalation pathway completely missing.

Full content to write:
- [ ] **Grievance Intake** — acknowledgement within 48hr, reference number assigned
- [ ] **SLA Tiers**:
  - Simple query: 7 days
  - Complex investigation: 30 days  
  - DPBI escalation trigger: unresolved beyond 30 days
- [ ] **DPBI Escalation Workflow**:
  ```
  Day 1: Grievance received → ACK sent
  Day 7: Internal resolution attempt
  Day 30: Final response deadline
  Day 31+: If unresolved → inform complainant of DPBI escalation right
  DPBI: Data Protection Board of India — file at dpb.gov.in (when operational)
  ```
- [ ] **Escalation to Ombudsman** — RBI Ombudsman pathway for NBFC-specific grievances
- [ ] **Grievance Tracker** — status dashboard fields, SLA breach alerts

---

#### A12. `15_Data_Processing_Agreement_(DPA).html` — Add DSA/LSP + Deletion 🟡
**Gap:** 72-line skeleton. DSA/LSP consent verification, downstream deletion obligations missing.

Full content to write:
- [ ] **Standard DPA clauses** (DPDP S.8(2) compliant)
- [ ] **DSA/LSP Partner Channel clause**:
  - "Consent collected at DSA/LSP source. Partner must retain proof-of-consent (screenshot, API log, audit record) and provide to NBFC within 24 hours of request"
  - "NBFC cannot use leads from DSA/LSP without proof of valid S.6 consent at source"
- [ ] **Deletion on Termination** clause:
  - "Within 30 days of contract termination, processor must delete all personal data and provide written confirmation"
  - Cross-reference T-33A (Processor Deletion Confirmation)
- [ ] **Downstream propagation clause** — processor must cascade withdrawals within 24hr
- [ ] **Sub-processor notification** — processor must notify NBFC before engaging sub-processors

---

#### A13. `16_Vendor_Risk_Assessment.html` — Add CPaaS Controls 🟡
**Gap:** 72-line skeleton. CPaaS purpose-level consent controls completely missing.

Full content to write:
- [ ] **Vendor Classification Matrix** — table: High/Medium/Low risk criteria
- [ ] **DPDP Compliance Questionnaire** (20 questions)
- [ ] **CPaaS Vendor DPDP Configuration Checklist**:
  - [ ] Suppression list sync frequency ≤ 24 hours
  - [ ] Per-purpose opt-out (not just global unsubscribe)
  - [ ] Withdrawal propagation confirmation mechanism
  - [ ] No marketing communications to opted-out contacts
  - [ ] Separate consent for WhatsApp vs SMS vs email
  - [ ] DPA executed with CPaaS provider
- [ ] **Annual Review Process** — renewal criteria, risk score update
- [ ] **Vendor Risk Register** — columns: vendor, data categories, DPA status, last review, next review, risk score

---

#### A14. `39_Privacy_Committee_Charter.html` — Add Operational RACI 🟡
**Gap:** Has content (258 lines) but missing permanent operational RACI for data protection roles.

Updates required:
- [ ] Add **"Data Protection RACI Matrix"** section — permanent operational roles (not project RACI):
  | Activity | DPO | Legal | IT | HR | Finance | Board |
  |----------|-----|-------|----|----|---------|-------|
  | DSAR fulfilment | A | C | R | C | C | I |
  | Breach notification | A | C | R | I | I | I |
  | Consent management | C | A | R | I | I | I |
  | ROPA maintenance | A | C | R | C | C | I |
  | Vendor DPA execution | C | A | I | I | R | I |
  | Employee privacy training | C | I | I | R | I | I |
  | Annual audit | A | C | C | C | C | I |
  | Board reporting | R | C | C | I | I | A |
  *(R=Responsible, A=Accountable, C=Consulted, I=Informed)*

---

#### A15. `03A_Employee_Data_Protection_Policy.html` — Add Job Description Clause 🟡
**Gap:** Has substantial content (471 lines) but G-08 checkpoint (data protection in job descriptions) missing.

Updates required:
- [ ] Add section **"Data Protection in Job Descriptions"**:
  - List roles that MUST include data protection clause in JD: DBA, IT Admin, Customer Service, Marketing, Finance, HR, Legal
  - Sample clause text for JDs: *"This role involves access to personal data and requires strict adherence to [Org] Data Protection Policy and DPDP Act 2023. Violations may result in disciplinary action including termination."*
  - Acknowledgement requirement: all employees with personal data access must sign data protection acknowledgement annually

---

#### A16. `06_Section_7_Legitimate_Uses_Legal_Memo.html` — Add CPaaS + AA 🟡
**Gap:** Has real content (379 lines) but missing CPaaS channel classification and Account Aggregator guidance.

Updates required:
- [ ] Add **"Communication Channel Legal Basis Classification"** table:
  | Communication Type | Legal Basis | Consent Needed? | Notes |
  |-------------------|-------------|-----------------|-------|
  | OTP / 2FA | S.7(a) — service delivery | No | Core service |
  | EMI payment reminders | S.7(a) — loan relationship | No | Core service |
  | Loan statements / NOC | S.7(a) — loan relationship | No | Core service |
  | Debt collection calls | S.7(a) — lending rights | No | Core service |
  | Marketing SMS | S.6 — Consent | Yes | Optional |
  | Cross-sell campaigns | S.6 — Consent | Yes | Optional |
  | WhatsApp communications | S.6 — Consent | Yes | Separate opt-in |
  | Promotional push notifications | S.6 — Consent | Yes | Optional |
- [ ] Add **"Account Aggregator (AA) Framework"** section:
  - AA financial data: linked via RBI AA Reference ID only
  - Never store raw financial data from AA fetch
  - Processing scope limited to original consent purpose
  - AA fetch = separate consent event (CP-004 in consent profile library)

---

#### A17. `07_Privacy_Notice_Web.html` — Add Version Control + Update SLA 🟡
**Gap:** Has real content (216 lines) but missing version control log and 10-day regulatory update SLA.

Updates required:
- [ ] Add **Notice Version Control Log** table at end of template:
  | Version | Effective Date | Changes Made | Approved By | Published Date |
  |---------|---------------|--------------|-------------|----------------|
  | 1.0 | [Date] | Initial publication | DPO | [Date] |
- [ ] Add **"When to Update This Notice"** section:
  - New processing purpose added → update within 5 working days
  - Regulatory change (DPDP/RBI/PMLA) → update within 10 working days
  - New third-party processor added → update within 5 working days
  - Any change to retention periods → update within 5 working days
- [ ] Add **Point-of-Collection Delivery** note: "This notice must be presented at the point of data collection, before any data is captured"

---

#### A18. `26_DPIA_Workbook_(SDF).html` — Add Trigger Checklist + Go-Live Gate 🟡
**Gap:** 72-line skeleton. DPIA trigger checklist, go-live gate, high-risk indicators missing.

Full content to write:
- [ ] **DPIA Trigger Checklist** — mandatory gate, tick any YES = DPIA required:
  - [ ] Biometric data? (Aadhaar, fingerprints, facial recognition)
  - [ ] Health data?
  - [ ] Automated decision-making affecting individual rights?
  - [ ] 10,000+ data principals?
  - [ ] Children's data?
  - [ ] Cross-border transfer?
  - [ ] New technology not previously assessed?
  - [ ] Systematic monitoring or profiling?
- [ ] **DPIA Process** — 6-step workbook: identify → assess necessity → assess risk → mitigation → DPO review → Board notification
- [ ] **Risk Scoring Matrix** — likelihood × impact = risk level
- [ ] **"Before Go-Live" Gate** — explicit sign-off: *"This DPIA must be completed and DPO must sign off BEFORE this processing activity goes live. No exceptions."*
- [ ] **DPIA Register link** — cross-reference to T-46

---

#### A19. `31_Consent_Registry_Dashboard.html` — Add Health Scoring 🟡
**Gap:** 72-line skeleton. Consent profile health monitoring, withdrawal rate alerts missing.

Full content to write:
- [ ] **Per-Purpose Health Score** dashboard fields:
  - Total active consents
  - Withdrawal rate (%) — alert if > 15%
  - Capture success rate (%) — alert if < 70%
  - Invalid consent rate (%) — alert if > 5%
  - S.6 validity score average
- [ ] **Purpose Health Status** — RAG per consent profile (CP-001 to CP-021)
- [ ] **Withdrawal Propagation Monitoring** — confirm downstream suppression within 24hr
- [ ] **Anomaly Alerts** — sudden spike in withdrawals, bulk consent capture

---

#### A20. `38_Compliance_Tracking_Dashboard.html` — Add 0-100% Scoring 🟡
**Gap:** 72-line skeleton. Scoring methodology, 92-checkpoint tracking not defined.

Full content to write:
- [ ] **Compliance Score Methodology** — how 0-100% is calculated:
  ```
  Score = (Checkpoints passed / 92) × 100
  Weighted by domain:
  - Domain 02 (Consent): 15% weight
  - Domain 08 (Security): 15% weight
  - Domain 05 (DSAR): 12% weight
  - Domain 10 (Breach): 12% weight
  - All others: ~6-7% each
  ```
- [ ] **92-Checkpoint Status Table** — all 12 domains with auto-populated vs DPO-reviewed split
- [ ] **DSAR SLA Tracker** — requests open, overdue, completed this month
- [ ] **Domain RAG Status** — Red/Amber/Green per domain with trend arrow
- [ ] **Alert Thresholds** — what triggers escalation to DPO/Board

---

#### A21. `45_Ongoing_Obligations_Calendar.html` — Add Regulatory Change + DPO Quarterly Review 🟡
**Gap:** Has real content (271 lines) but missing regulatory change management and DPO quarterly checkpoint review.

Updates required:
- [ ] Add **"Regulatory Change Management"** trigger:
  - *"Within 10 working days of any DPDP/RBI/PMLA/SEBI/CERT-In regulatory update: DPO reviews impact on all templates, policies, and ROPA. Updates affected documents. Notifies Board. Logs change in version control."*
- [ ] Add **"DPO Quarterly 92-Checkpoint Review"** schedule:
  - Q1 (Jan): Full 92-checkpoint audit, compliance score updated
  - Q2 (Apr): Consent profile health review + DSAR SLA audit
  - Q3 (Jul): Vendor DPA review + security controls check
  - Q4 (Oct): Annual Board Report preparation + ROPA review
- [ ] Add **"CCTV Retention Automated Purge"** monthly task

---

### TIER 3 — Full Content for Remaining Skeleton Templates

These 14 templates are 72-line skeletons that need complete content written.
Each follows the same structure: Header → Scope → Process → Workflow → Templates/Forms → Checklist → Sign-Off

| Template | Content to Write | Checkpoint IDs |
|----------|-----------------|----------------|
| **A22** `18_Data_Protection_Policy.html` | Master policy: scope, roles, 8 principles, processing obligations, rights, breach authority, review schedule | G-01 |
| **A23** `21_Breach_Notification_Template_-_DPB.html` | DPBI notification form: incident details, principals affected, data categories, mitigation steps, DPO contact | BN-03 |
| **A24** `22_Breach_Notification_-_Data_Principal.html` | Principal notification letter: what happened, data affected, steps taken, rights available | BN-07 |
| **A25** `23_Post-Breach_Review.html` | PIR template: incident timeline, root cause, systems affected, response quality, lessons learned, remediation plan | BN-08 |
| **A26** `25_Compliance_Audit_Plan.html` | Annual audit plan: scope, methodology, domains, evidence collection, findings report, DPO sign-off | AC-08 |
| **A27** `27_DPO_Appointment_Letter_(SDF).html` | Appointment letter: name, qualifications, mandate, authority scope, reporting line, published contact, remuneration | G-02 |
| **A28** `28_Audit_Findings_Report.html` | Audit findings: domain scores, critical/high/medium findings, remediation actions, owner, deadline, status | AC-08 |
| **A29** `29_Deletion_Log.html` | Deletion record: request ID, data subject, categories deleted, systems deleted from, deletion method, certificate issued | RD-06 |
| **A30** `30_Breach_Register.html` | Breach register: date, nature, scope, principals affected, notification dates (DPB, CERT-In), remediation status | BN-07 |
| **A31** `32_Data_Discovery_Report.html` | Discovery scan results: systems scanned, PII found, classification, risk level, remediation needed | DD-06 |
| **A32** `34_Access_Control_Policy.html` | RBAC policy: role definitions, permission matrix, least-privilege, MFA requirement, access review schedule | SS-06, SS-07 |
| **A33** `36_Annual_SDF_Audit_Report.html` | Annual SDF audit: auditor details, scope, methodology, 12-domain assessment, findings, board sign-off | AC-08 |
| **A34** `37_Board_Risk_Committee_Report.html` | Executive dashboard: compliance score, key risks, DSAR stats, breach summary, consent health, quarter actions | G-07 |
| **A35** `19_Employee_Data_Protection_Training.html` | Training programme: modules, certification, completion tracking, annual renewal, role-specific variants | G-06 |

---

### TIER 4 — New Template to Create

#### A36. NEW: `21A_Breach_Notification_CERT-In.html` 🔴
**Reason:** CERT-In 6-hour SLA is completely separate from DPBI 72-hour. Critical gap.
- Create from scratch in the same UNIFIED_THEME.css style as other templates
- Add to template manifest, navigator, and application map
- Link bidirectionally with T-20 (Incident Response Plan) and T-21 (DPBI notification)

---

## PART B — Guide Document Updates (9 files in `/guide/`)

Updates needed to the guide documents planned in TODO.md (original 9-document plan).

---

### B1. Update `TODO.md` (this file) ← DONE (you're reading it)

---

### B2. `00_MASTER_STRATEGY.md` — Additional Sections Needed

- [ ] Add **"92-Checkpoint Coverage Status"** table — which of the 92 checkpoints each phase covers
- [ ] Add **"Template Health Status"** — mark which templates are skeletons vs substantial
- [ ] Add **"CERT-In vs DPBI"** distinction box — two separate obligations, two separate timers
- [ ] Update template count: 50 → 51 (after adding T-21A CERT-In)
- [ ] Correct the DSAR SLA to the verified correct period

---

### B3. `02_PHASE_1_ASSESSMENT.md` — Add 45 Pre-Mapped ROPA Activities

- [ ] Add **"45 Pre-Mapped NBFC ROPA Activities"** reference table — the full list from dataRakshaq/CERF:
  - 22 consent-based activities (personal loan, BNPL, marketing, AA, microfinance, etc.)
  - 23 legitimate use activities (KYC, fraud detection, credit bureau, debt recovery, etc.)
- [ ] Add **"Notice Version Control"** guidance (PN-06 gap)
- [ ] Add **sensitive data tagging** methodology (DD-05 gap)
- [ ] Correct any references to DSAR SLA from 90 days to verified correct period

---

### B4. `03_PHASE_2_GAP_ANALYSIS.md` — Add 92-Checkpoint Scoring

- [ ] Add the full **92-checkpoint domain matrix** as the scoring framework
- [ ] Add **S.6 Validity Score** methodology as a gap metric
- [ ] Add **Penalty exposure table** — per section, per violation type
- [ ] Add domain weighting for the 0–100% compliance score

---

### B5. `04_PHASE_3_REMEDIATION.md` — Add Major Missing Tracks

Track 3A (Consent):
- [ ] Add **21 Consent Profiles** (CP-001 to CP-021) — NBFC product-specific consent profiles
- [ ] Add **25 Purpose Codes** (PC-001 to PC-025) — granular purpose-level consent
- [ ] Add **26-field consent_records schema** — technical implementation spec
- [ ] Add **Account Aggregator (AA) compliance** — RBI AA framework interop
- [ ] Add **DSA/LSP channel consent verification** — proof-of-consent at partner source

Track 3F (Breach):
- [ ] Add **CERT-In 6-hour SLA** workflow — separate from DPBI 72-hour
- [ ] Add **Dual-timer breach command centre** — T+0 to T+30d timeline
- [ ] Add **SIEM requirements** — what to monitor, alert thresholds
- [ ] Add **Annual tabletop exercise** — how to run, who participates

Track 3A (Communication):
- [ ] Add **CPaaS channel classification** — which comms = S.7, which = S.6

---

### B6. `05_PHASE_4_MONITORING.md` — Add 92-Checkpoint Tracking

- [ ] Add **92-checkpoint quarterly review schedule** — how DPO signs off on 45 DPO-reviewed checkpoints
- [ ] Add **Consent profile health monitoring** (AC-06 gap)
- [ ] Add **DAM (Database Activity Monitoring)** as a monitoring requirement
- [ ] Add **SIEM alert monitoring** — ongoing surveillance

---

### B7. `06_PHASE_5_GOVERNANCE.md` — Add Operational RACI + Regulatory Change Management

- [ ] Add **Permanent operational RACI** for data protection roles (G-03 gap)
- [ ] Add **Regulatory change management process** (AC-07 gap) — 10-day update SLA
- [ ] Add **Annual obligations calendar** with CERT-In and DPO quarterly review

---

### B8. `07_DOS_AND_DONTS.md` — Verified and Expanded

Update based on gap analysis findings:

- [ ] **Consent section:** Add DO: "Compute S.6 validity score at every capture" + DON'T: "Never store 12-digit Aadhaar"
- [ ] **Security section:** Add DO: "Run OWASP Top 10 pentest annually" + DO: "Enable DAM on all PII databases"
- [ ] **Breach section:** Add DO: "Notify CERT-In within 6 hours" (separate from DPBI 72-hour) — this is the most commonly missed rule
- [ ] **DSAR section:** Add DO: "Acknowledge within 48 hours" + DO: "Verify identity before processing" + DO: "Propagate erasure to all processors"
- [ ] **Retention section:** Add DO: "CCTV footage purged after 90 days" + DO: "Verify RBI retention period (8yr loan / 10yr KYC)"
- [ ] **CPaaS section (new):** Add DO/DON'T table for communication channels classification

---

### B9. `08_GOAL_TRACKING.md` — Add 92-Checkpoint OKRs

- [ ] Add OKR: **"Achieve 92/92 checkpoint green by Q4 2026"**
- [ ] Add **DPO Quarterly 92-Checkpoint Review** as a recurring OKR
- [ ] Add **Consent profile health score ≥ 80%** as a Key Result
- [ ] Add **DSAR SLA compliance rate ≥ 98%** as a Key Result
- [ ] Add **Zero CERT-In SLA breaches** as a Key Result
- [ ] Add **Compliance score improvement trajectory** — monthly tracking chart template

---

## Execution Order

```
PHASE A — Critical Fixes (Do First)
Week 1:
  ├── A1: Fix T-11 DSAR SLA (90-day → verify correct period)
  ├── A2: Build out T-20 Incident Response Plan (full content)
  ├── A3: Create T-21A CERT-In notification template (NEW)
  └── A9: Fix T-02A retention schedule (RBI period + CCTV)

Week 2:
  ├── A4: T-12 Erasure SOP (downstream propagation)
  ├── A5: T-08 Consent Form (26-field schema + S.6 scoring)
  ├── A7: T-33 Encryption Checklist (Aadhaar VID + PAN)
  └── A8: T-35 Audit Logging (PII redaction + immutability)

Week 3:
  ├── A6: T-24 Security Hardening Plan (full content)
  ├── A10: T-10 DSAR Form (ID verify + portability)
  └── A11-A16: Tier 2 updates (6 templates)

PHASE B — Full Content for Skeletons (Parallel with A)
Week 2-4:
  ├── A22-A35: 14 skeleton templates (full content)
  └── A36: Create T-21A CERT-In template

PHASE C — Guide Documents
Week 3-5:
  ├── B2: 00_MASTER_STRATEGY.md
  ├── B3: 02_PHASE_1_ASSESSMENT.md (45 ROPA activities)
  ├── B4: 03_PHASE_2_GAP_ANALYSIS.md (92-checkpoint scoring)
  ├── B5: 04_PHASE_3_REMEDIATION.md (21 CPs + 25 PCs + CERT-In)
  ├── B6: 05_PHASE_4_MONITORING.md
  ├── B7: 06_PHASE_5_GOVERNANCE.md
  ├── B8: 07_DOS_AND_DONTS.md
  └── B9: 08_GOAL_TRACKING.md
```

---

## Master Gap Closure Tracker

| # | Gap ID | Gap Description | Template | Guide | Status |
|---|--------|----------------|---------|-------|--------|
| 1 | DP-03 | DSAR SLA discrepancy (90d vs correct period) | T-11 | All guides | [ ] |
| 2 | BN-04 | CERT-In 6-hr SLA missing | T-20, T-21A (new) | B5 | [ ] |
| 3 | CM-05/06/07 | 26-field consent schema missing | T-08 | B5 | [ ] |
| 4 | CM-08/10 | 24-hr withdrawal propagation SLA | T-12 | B5 | [ ] |
| 5 | DD-07 | Aadhaar VID only rule | T-24, T-33 | B8 | [ ] |
| 6 | DD-08 | PAN masking rule | T-33, T-35 | B8 | [ ] |
| 7 | DP-07 | Erasure downstream propagation | T-12 | B5 | [ ] |
| 8 | RD-03 | RBI retention period discrepancy | T-02A, T-43 | B3 | [ ] |
| 9 | SS-05 | Penetration testing missing | T-24 | B8 | [ ] |
| 10 | SS-10 | Vulnerability/patch management missing | T-24 | B5 | [ ] |
| 11 | LU-05 | DSA/LSP consent verification | T-15 | B5 | [ ] |
| 12 | LU-03 | CPaaS channel classification | T-06 | B5, B8 | [ ] |
| 13 | G-08 | Data protection in job descriptions | T-03A | B7 | [ ] |
| 14 | DP-02 | 48-hr DSAR acknowledgement | T-10, T-11 | B5 | [ ] |
| 15 | DP-04 | Identity verification before DSAR | T-10, T-12 | B5 | [ ] |
| 16 | SS-03 | PII log redaction not specified | T-35 | B5 | [ ] |
| 17 | SS-08 | DAM not covered | T-35, T-24 | B6 | [ ] |
| 18 | BN-01 | SIEM not covered | T-24 | B5 | [ ] |
| 19 | AC-07 | No regulatory change management | T-45 | B7 | [ ] |
| 20 | RD-05 | CCTV 90-day retention | T-02A, T-43 | B3 | [ ] |
| 21 | Comp-1 | 45 pre-mapped ROPA activities | ROPA Guide | B3 | [ ] |
| 22 | Comp-2 | 21 Consent Profiles (CP-001 to CP-021) | T-08 | B5 | [ ] |
| 23 | Comp-3 | 25 Purpose Codes (PC-001 to PC-025) | T-08 | B5 | [ ] |
| 24 | Comp-5 | DSA/LSP consent workflow | T-15 | B5 | [ ] |
| 25 | Comp-6 | Account Aggregator compliance | T-06 | B5 | [ ] |
| 26 | G-03 | Operational RACI missing | T-39 | B7 | [ ] |
| 27 | AC-03 | DPO quarterly review schedule | T-45 | B9 | [ ] |
| 28 | AC-06 | Consent profile health score | T-31 | B6 | [ ] |
| 29 | AC-01 | 0-100% compliance score methodology | T-38 | B9 | [ ] |
| 30 | PN-03 | Notice 10-day update SLA | T-07, T-45 | B3 | [ ] |
| 31 | PN-06 | Notice version control log | T-07 | B3 | [ ] |
| 32 | LU-04 | Account Aggregator DPDP guidance | T-06 | B5 | [ ] |
| 33 | TV-08 | CPaaS vendor consent controls | T-16 | B5 | [ ] |
| 34 | SS-09 | INSERT-only + 7-yr + S3 Object Lock | T-35 | B5 | [ ] |
| 35 | DP-01 | Data portability right missing | T-10, T-11 | B5 | [ ] |
| 36 | DP-05 | DPBI grievance escalation | T-13 | B5 | [ ] |
| 37 | CM-09 | S.6 validity scoring | T-08, T-42 | B4 | [ ] |
| 38 | BN-05 | Dual-timer breach command | T-20 | B5 | [ ] |
| 39 | BN-02 | Tabletop exercise not required | T-20 | B5 | [ ] |
| 40 | DPIA-02 | DPIA before go-live gate | T-26 | B7 | [ ] |
| 41 | DPIA-03 | High-risk indicator checklist | T-26 | B7 | [ ] |
| 42 | DD-05 | Sensitive data tagging methodology | T-03 | B3 | [ ] |
| 43 | SS-09 | Immutable audit log enforcement | T-35 | B5 | [ ] |
| 44 | G-08 | 25 skeletons need full content | A22-A35 | — | [ ] |

---

## Summary Counts

| Category | Count | Estimated Effort |
|----------|-------|-----------------|
| Tier 1 critical template updates | 10 | High |
| Tier 2 important template updates | 11 | Medium |
| Tier 3 skeleton → full content | 14 | High |
| New template (T-21A CERT-In) | 1 | Medium |
| Guide document creates (9) | 9 | Medium |
| Guide document updates (8) | 8 | Low-Medium |
| **Total tasks** | **53** | — |
