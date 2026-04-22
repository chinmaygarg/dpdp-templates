# Phase 5: Governance — Board Resolution, Certification & Ongoing Compliance

**Duration:** Weeks 16-24 (July-October 2026) | **Effort:** 8-10 weeks | **Owner:** DPO, Board, Legal | **Templates:** T-39 to T-48

---

## Overview

Phase 5 finalizes governance structures, obtains board certification, and establishes perpetual compliance maintenance cycles.

---

## 6 Governance Components

### 1. **Privacy Committee Charter (T-39)**
- **Charter Scope:** Board-level Privacy Committee established under Section 10(2)
- **Membership:** Board Chair, Independent Director (Data Privacy expert), CFO, CISO, DPO (non-voting)
- **Frequency:** Quarterly meetings (Q1-Q4); emergency session if CRITICAL breach/gap
- **Authority:** Approve DPIA findings, set compliance KPI targets, escalate to Board
- **First Meeting:** Before Phase 4 completion (by Week 12)
- **Owner:** Board Chair + DPO

### 2. **Board Resolution (T-40)**
- **Resolution Content:** Formal approval of DPDP compliance roadmap, appointment of DPO, designation of Privacy Committee
- **Sign-Off:** Board resolution passed (simple majority or unanimous per org bylaws)
- **Documented:** Board meeting minutes, resolution archived 7 years
- **Copy to:** DPO, Compliance Officer, DPBI (if SDF, as part of certification)
- **Owner:** Company Secretary/Board

### 3. **Compliance Certificate / Opinion Letter (T-41)**
- **Issuance Authority:** DPO (for DF); independent registered auditor (for SDF)
- **Content:** Certification that organization meets all 92 checkpoints; residual risks identified
- **Scope:** As of certification date (e.g., "15 May 2026")
- **Distribution:** Board, DPBI (if SDF), external auditors
- **Validity:** Renewed annually; updated if material changes post-certification
- **Owner:** DPO / External Auditor

### 4. **Consent Audit Worksheet (T-42)**
- **Purpose:** Quarterly verification that all active consents remain FSIUU-valid
- **Scope:** Random sample of 500+ consents per quarter
- **Checklist:** Re-verify all 5 FSIUU attributes (Free, Specific, Informed, Unconditional, Unambiguous)
- **Action:** If >2% invalid, trigger re-consent campaign
- **Frequency:** Q1, Q2, Q3, Q4 (4 audits per year)
- **Owner:** Compliance Officer

### 5. **Statutory Hold Register (T-43)**
- **Purpose:** Track data that CANNOT be deleted per regulatory/legal requirement
- **Categories:** KYC records (10-year RBI hold), loan files (8-year RBI hold), litigation hold, court order, tax records (6-year statutory hold)
- **Entry Format:** Record ID, hold reason, legal basis, hold end date, review frequency
- **Impact on DSAR Erasure:** When data principal requests erasure, check register; explain hold; offer alternative (anonymization, blocking)
- **Annual Review:** Verify each hold still justified; remove expired holds
- **Owner:** Legal Counsel + Compliance

### 6. **Cross-Border Transfer Register (T-44)**
- **Purpose:** Document all international data flows per Section 16
- **Entry Per Transfer:** Recipient country, data categories, legal basis (adequacy, binding contract, explicit consent), adequacy assessment, transfer agreement signed
- **Adequacy Verification:** India has adequacy findings for ONLY [to be verified with latest DPDP Rules], so most transfers require binding contract + Section 16 explicit consent
- **Annual Audit:** Re-verify each transfer remains justified; audit recipient security
- **Frequency:** Quarterly new transfer review; annual full audit
- **Owner:** Legal + DPO

### 7. **Ongoing Obligations Calendar (T-45)**
- **Annual Cadence:** 12-month rolling calendar of compliance tasks
- **Categories:** Regulatory change management (10-day triggers), quarterly checkpoint reviews, annual audit scheduling, board reporting
- **Key Dates:** Breach notification SLA (DPBI 72-hr, CERT-In 6-hr), DSAR response SLA (30 days), deletion SLA (30 days), consent audit (quarterly)
- **Renewal Tasks:** Privacy notice review (annual), employee training refresh (annual), DPA compliance audit (annual)
- **Escalation Triggers:** Regulatory change detected, DPA not signed, >5% invalid consents, breach SLA missed, audit finding >MEDIUM
- **Owner:** DPO

### 8. **DPIA Register (T-46, SDF only)**
- **Purpose:** Maintain immutable register of all Data Protection Impact Assessments (Section 10)
- **Entry Per DPIA:** Activity ID, processing description, DPIA completion date, risk level (HIGH/MEDIUM/LOW), DPO approval, safeguards implemented, re-assessment date
- **Mandatory DPIA Triggers:** Biometric, health, automated decision-making with legal effect, large-scale processing (10K+), children's data, cross-border, novel technology, systematic monitoring
- **Re-Assessment Frequency:** Every 24 months; immediately if processing materially changes
- **Archival:** 7-year retention post-completion
- **Report to DPBI:** Submit summary of all DPIA determinations with annual SDF audit
- **Owner:** DPO

### 9. **Compliance Status Report / Board Pack (T-47)**
- **Content:** 5-section executive summary for Board Audit Committee
  - **Section 1:** Compliance score (0-100%), RAG status per 17 domain
  - **Section 2:** Key metrics dashboard (consent health, DSAR SLA, breach SLA, training completion, audit status)
  - **Section 3:** Top 5 risks/gaps and remediation roadmap
  - **Section 4:** Incident summary (if any breach/complaint in prior quarter)
  - **Section 5:** Upcoming obligations (next quarter's critical deadlines)
- **Frequency:** Quarterly (end of each Q1-Q4)
- **Audience:** Board Audit Committee, CEO, CFO
- **Owner:** DPO

### 10. **Consent Manager Integration Specification (T-48)**
- **Purpose:** Define consent platform requirements for operational consent tracking
- **Functional Specs:** Per-purpose consent tracking, withdrawal management, consent history, FSIUU audit trail, CPaaS sync API, DSAR fulfillment integration, deletion cascade
- **Data Elements:** Consent ID, data principal ID (email/phone), purpose(s), grant date, version, IP/device, consent form hash (for audit proof), withdrawal date/reason
- **Audit Trail:** Immutable consent history; every change (grant, withdrawal, re-consent, correction) timestamped + logged
- **Integration Points:** Email/SMS platform (CPaaS), CRM, analytics, website consent banner, mobile app
- **Frequency:** Real-time consent updates; weekly compliance audit
- **Owner:** Product + IT

---

## Post-Certification Maintenance Cycle

### **Month 1-3 (Post-Certification Honeymoon)**
- Execute Phase 5 checklist
- Obtain board certification
- Deploy ongoing obligations calendar
- Establish Privacy Committee meeting cadence
- Publish compliance certificate on website/Board disclosures

### **Month 4-12 (Ongoing Operations)**
- **Monthly:** KPI monitoring (consent health, DSAR SLA, deletion SLA)
- **Quarterly:** Privacy Committee meeting + Board Risk Report
- **Quarterly:** Consent audit (T-42) + statutory hold review (T-43) + cross-border audit (T-44)
- **Quarterly:** DPIA Register update (T-46, if SDF)
- **Quarterly:** Regulatory change scan (10-day response if critical)
- **Semi-Annual:** Data Discovery scan (T-32); encryption audit (T-33)
- **Annual:** Full compliance audit (T-36, if SDF); employee training refresh; DPA re-negotiation/renewal; Privacy Committee charter review; board re-certification

### **Escalation Triggers for Immediate Action**
| Condition | Action | SLA |
|---|---|---|
| **Data Breach Detected** | DPBI notification + Board notification | 72 hours (DPBI) + same day (Board) |
| **Regulatory Change (Critical)** | Legal review + Privacy Notice update + Board notification | 10 business days |
| **Compliance Score <90%** | DPO remediation plan + Board emergency session | Immediate |
| **DSAR >30 days** | Individual escalation + DPBI notification | Immediate |
| **Audit Finding CRITICAL** | Remediation plan + Board approval | 10 days |
| **DPA Unsigned** | Procurement re-negotiation or vendor termination | 30 days |
| **>5% Invalid Consents** | Pause processing + re-consent campaign | 15 days |

---

## Deliverables

- [ ] **T-39:** Privacy Committee Charter approved by Board
- [ ] **T-40:** Board Resolution signed (DPDP compliance mandate, DPO appointment, Privacy Committee established)
- [ ] **T-41:** Compliance Certificate issued by DPO/Auditor; signed + dated
- [ ] **T-42:** Consent Audit Worksheet Q1 completed; >98% FSIUU validity confirmed
- [ ] **T-43:** Statutory Hold Register populated (all RBI/legal holds documented)
- [ ] **T-44:** Cross-Border Transfer Register populated (all international flows documented + adequacy verified)
- [ ] **T-45:** Ongoing Obligations Calendar published (12-month rolling schedule live)
- [ ] **T-46:** DPIA Register established (SDF only); all mandatory DPIAs archived
- [ ] **T-47:** First Board Risk Committee Report delivered (Q1 2026 compliance snapshot)
- [ ] **T-48:** Consent Manager specification finalized + integration roadmap approved

→ [Next: Phase 5 Complete — Perpetual Compliance Maintenance](./08_GOAL_TRACKING.md)

---

**Owner:** DPO, Board | **Board Approval:** [Date/Signature]
