# DPDP Compliance Goal Tracking — OKR Framework & KPI Dashboard

A strategic goal-tracking system aligned to DPDP Act 2023 implementation. Covers phase-by-phase OKRs, weekly checkpoints, role accountability, and escalation triggers.

---

## DPDP Compliance Deadline

**Compliance Deadline:** 13 May 2027 (18 months from Phase 0 start, January 2026)

**Current Target Timeline:**
- **Phase 0:** Weeks -2 to 0 (January 2026) — Scoping & entity classification
- **Phase 1:** Weeks 1-8 (January-March 2026) — Data inventory & ROPA
- **Phase 2:** Weeks 3-8 (February-May 2026) — Gap analysis (overlapping Phase 1)
- **Phase 3:** Weeks 6-16 (March-June 2026) — Remediation across 5 streams
- **Phase 4:** Weeks 9-20 (May-September 2026) — Live monitoring dashboards
- **Phase 5:** Weeks 16-24 (July-October 2026) — Governance & board certification

**Buffer:** 6 months post-Phase 5 for final audits, remediation of late findings, board sign-off.

---

## Phase-by-Phase OKRs (Objectives + Key Results)

### Phase 0: Scoping (Weeks -2 to 0)

**Objective:** Determine DPDP applicability and entity classification before commencing compliance work.

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** DPDP applicability determined (DF vs SDF) | Board approves DF or SDF classification; documented | Legal, CTO | Week 0 |
| **KR2:** Entity type assigned (financial, healthcare, telecom, etc.) | Classification selected + regulatory overlay documented | Legal | Week 0 |
| **KR3:** Regulatory conflict matrix completed (RBI, SEBI, TRAI overlays) | Overlay requirements documented for each entity type | Legal, Compliance | Week 0 |
| **KR4:** DPO hiring plan (if SDF) | DPO job description + recruitment timeline | HR | Week 0 |
| **KR5:** Board approval obtained | Board resolution or CEO sign-off documented | CEO, Board | Week 0 |

---

### Phase 1: Assessment (Weeks 1-8)

**Objective:** Establish complete baseline of all data processing activities (Data Inventory, ROPA, Data Flows).

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** Data Inventory completed | All systems cataloged (T-03); >95% staff validation survey | Data Governance | Week 4 |
| **KR2:** Data Flow Diagram finalized | Visual map of all data flows (T-04); reviewed by IT | IT, Data Governance | Week 4 |
| **KR3:** ROPA finalized (all 50+ processing activities documented) | Complete ROPA (T-05) with all mandatory fields; DPO signed | DPO, Legal | Week 6 |
| **KR4:** Section 7 Legitimate Uses documented | Memo (T-06) covers all 9 Section 7 categories; Legal signed | Legal | Week 6 |
| **KR5:** Privacy Notice updated | Deployed on website (T-07); customers notified | Marketing, Legal | Week 7 |
| **KR6:** FSIUU Consent Form deployed | Live (T-08); ≥98% of new consents meet FSIUU (5/5 validity) | Product | Week 8 |
| **KR7:** Retrospective Consent Audit completed | Report (T-09) covers past 3 years; re-consent plan if needed | Compliance | Week 8 |

**Success Criteria:** Phase 1 complete ✓ = All 7 KRs met; Board sign-off obtained; <5% data inventory rework discovered in Phase 2.

---

### Phase 2: Gap Analysis (Weeks 3-8, overlapping Phase 1)

**Objective:** Assess compliance across 17 domains; create prioritized remediation roadmap.

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** 17-domain scorecard completed | All 17 domains scored (0-92 checkpoints); RAG assigned | DPO, Compliance | Week 5 |
| **KR2:** Gap severity analysis complete | All gaps classified Critical/High/Medium/Low per penalty exposure | Compliance, Legal | Week 6 |
| **KR3:** Gap register published | 44 identified gaps prioritized; Tiers 1/2/3 assigned; roadmap created | DPO | Week 7 |
| **KR4:** Remediation roadmap approved | Board approves phased remediation plan + resource allocation | Board | Week 8 |
| **KR5:** Compliance score baseline established | Starting score calculated (e.g., 35/92 = 38%); tracked weekly | DPO | Week 8 |

**Success Criteria:** Phase 2 complete ✓ = Clear remediation plan; no surprises in Phase 3; team aligned on Tier 1 priorities.

---

### Phase 3: Remediation (Weeks 6-16)

**Objective:** Close all identified gaps via 5 operational streams (Consent, Rights, Vendor, Security, Data Lifecycle).

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** All Tier 1 Critical gaps remediated | 10 critical templates (T-07 to T-24) live; FSIUU validated | Product, IT, Legal | Week 12 |
| **KR2:** All Tier 2 High-Impact gaps remediated | 11 high-priority gaps closed; vendor DPA coverage ≥98% | Product, Procurement, IT | Week 14 |
| **KR3:** Compliance score ≥80% | 73+ of 92 checkpoints met; board dashboard shows progress | DPO | Week 15 |
| **KR4:** Data Subject Rights SLA ≥99%** (DSAR, correction, erasure, grievance, nomination) | 99%+ response ≤ SLA (DSAR ≤30d, correction ≤15d, etc.); tracked weekly | Legal, Product | Week 16 |
| **KR5:** Employee training ≥95% completion | 95%+ staff trained; role-specific modules deployed; annual refresher scheduled | HR, Compliance | Week 16 |
| **KR6:** Breach response & security controls live | Incident response plan tested (tabletop exercise); SIEM + DAM deployed; encryption audit passed | CISO, IT | Week 16 |

**Success Criteria:** Phase 3 complete ✓ = 80%+ compliance score; all critical SLAs met; Board confident in Phase 4 monitoring.

---

### Phase 4: Monitoring (Weeks 9-20)

**Objective:** Deploy real-time dashboards and continuous monitoring of compliance health.

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** Compliance Dashboard live (T-38) | Real-time 0-100% score + 17-domain RAG visible to Board; updated weekly | DPO, IT | Week 10 |
| **KR2:** Consent health metrics tracked | Consent registry (T-31) shows per-purpose %, withdrawal rate <10%, invalid <2%; dashboards live | Compliance, Product | Week 11 |
| **KR3:** Data Discovery scanning automated (T-32) | Weekly PII scans across all systems; unknown PII concentrations escalated | IT Security | Week 12 |
| **KR4:** Encryption audit completed (T-33) | AES-256 at rest verified; TLS 1.3+ in transit verified; Aadhaar/PAN masking rules validated | CISO | Week 13 |
| **KR5:** Access Control policy + quarterly review live (T-34) | RBAC enforced; MFA mandatory for admin; Q1 access review completed | IT Security | Week 14 |
| **KR6:** Audit logging with PII redaction operational (T-35) | Immutable logs (INSERT-only) + hash-chaining live; 7-year retention policy active | IT Security | Week 15 |
| **KR7:** Board Risk Committee reporting started (T-37) | Q1 report delivered (compliance score, domain RAG, breach summary); quarterly cadence confirmed | DPO, Board | Week 16 |
| **KR8:** Compliance score ≥90%** | 83+ of 92 checkpoints met; Phase 5 readiness confirmed | DPO | Week 18 |

**Success Criteria:** Phase 4 complete ✓ = 90%+ compliance; board visibility & confidence high; monitoring framework sustainable.

---

### Phase 5: Governance (Weeks 16-24)

**Objective:** Finalize governance structures, obtain board certification, establish perpetual compliance maintenance.

| Key Result | Success Metric | Owner | Target |
|---|---|---|---|
| **KR1:** Privacy Committee Charter approved & operational (T-39) | Board approves charter; Q1 meeting held with documented minutes | Board, DPO | Week 18 |
| **KR2:** Board Resolution passed (T-40) | Formal resolution approving DPDP compliance + DPO appointment + Privacy Committee | Board | Week 18 |
| **KR3:** Compliance Certificate issued (T-41) | DPO or independent auditor (if SDF) signs certification; compliance ≥92 checkpoints | DPO, Auditor | Week 20 |
| **KR4:** Statutory Hold Register populated & audited (T-43) | All regulatory holds documented (KYC 10yr, loan docs 8yr, etc.); Q1 audit complete | Legal, Compliance | Week 20 |
| **KR5:** Cross-Border Transfer Register completed (T-44) | All international transfers documented + adequacy assessed; annual audit scheduled | Legal, DPO | Week 20 |
| **KR6:** Ongoing Obligations Calendar live (T-45) | 12-month rolling calendar; regulatory change detection process live; escalation triggers active | Compliance | Week 21 |
| **KR7:** DPIA Register established (T-46, SDF only) | All high-risk DPIAs archived; register accessible; 24-month re-assessment schedule | DPO | Week 22 |
| **KR8:** Compliance score ≥97%** (92+ of 92 checkpoints) | All gaps closed; final board certification; public disclosure on website | DPO | Week 24 |

**Success Criteria:** Phase 5 complete ✓ = Full compliance (97%+); board certified; perpetual compliance framework operational; deadline met (13 May 2027).

---

## Weekly Checkpoint Template

Run this checkpoint every Friday afternoon. Share with stakeholders by Monday morning.

```
## DPDP Compliance Checkpoint — Week [#] of [Phase Name]

**Date:** [YYYY-MM-DD] | **Reporter:** [Name] | **Phase:** [Phase] | **Week:** [#/Total]

### 1. Compliance Score Progress
- **Current Score:** [X/92] checkpoints = [Y]%
- **Target for Phase:** [Z]%
- **Status:** 🟢 On track / 🟡 At risk / 🔴 Off track
- **Change Since Last Week:** +[N] checkpoints ([+X]%)

### 2. Milestones — This Week
| Milestone | Target | Status | Notes |
|---|---|---|---|
| [Specific deliverable] | [Date] | 🟢 Done / 🟡 In Progress / 🔴 Blocked | [Brief note] |
| [Specific deliverable] | [Date] | 🟢 Done / 🟡 In Progress / 🔴 Blocked | [Brief note] |

### 3. Key Performance Indicators (KPIs)
| KPI | Target | Current | Status | Trend |
|---|---|---|---|---|
| Consent Health Score | ≥97% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| DSAR SLA Compliance | ≥99% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Withdrawal Rate | <10% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Invalid Consent Rate | <2% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Data Breach SLA (72-hr DPBI) | 100% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Deletion SLA (30-day) | ≥99% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Training Completion | ≥95% | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |
| Compliance Score | ≥90% (by Phase 4) | [X]% | 🟢/🟡/🔴 | ↑/→/↓ |

### 4. 17-Domain Compliance Scorecard (Snapshot)
| Domain | Checkpoints | Completed | % | RAG | Owner |
|---|---|---|---|---|---|
| 1. Consent & Notice | 8 | [#] | [#]% | 🟢/🟡/🔴 | [Name] |
| 2. Data Subject Rights | 8 | [#] | [#]% | 🟢/🟡/🔴 | [Name] |
| ... (all 17 domains) | | | | | |
| **TOTAL** | **92** | **[#]** | **[#]%** | | |

### 5. Top 3 Blockers/Risks
| Blocker | Impact | Owner | Mitigation | ETA |
|---|---|---|---|---|
| [Blocker description] | High/Medium/Low | [Name] | [Action] | [Date] |
| [Blocker description] | High/Medium/Low | [Name] | [Action] | [Date] |
| [Blocker description] | High/Medium/Low | [Name] | [Action] | [Date] |

### 6. Team Capacity & Staffing
| Role | Required FTE | Allocated | Utilization | Notes |
|---|---|---|---|---|
| DPO | 1.0 | [#] | [#]% | [Gaps?] |
| Legal | 0.5 | [#] | [#]% | [Gaps?] |
| Compliance Officer | 1.0 | [#] | [#]% | [Gaps?] |
| IT Security | 2.0 | [#] | [#]% | [Gaps?] |
| Product | 1.0 | [#] | [#]% | [Gaps?] |
| HR | 0.5 | [#] | [#]% | [Gaps?] |

### 7. Next Week's Priorities
- [ ] [Specific deliverable #1 due next week]
- [ ] [Specific deliverable #2 due next week]
- [ ] [Specific deliverable #3 due next week]

### 8. Escalations for Leadership
> **🚨 Critical Items Requiring Board/CEO Attention:**
- [Escalation #1]: [Issue] → [Required action] → [Deadline]
- [Escalation #2]: [Issue] → [Required action] → [Deadline]

### 9. Lessons Learned / Adjustments
- **What went well:** [Brief note]
- **What needs adjustment:** [Change recommendation]
- **Dependencies on other teams:** [List]

**Prepared by:** [Name] | **Distribution:** Board, Leadership, Compliance Team
```

---

## Monthly Board Report Template

Share this with Board Audit Committee / Leadership at month-end.

```
## DPDP Compliance Status Report — Month [Month Year]

**Reporting Period:** [Start Date] to [End Date]
**Prepared by:** [DPO Name]
**Distribution:** Board Audit Committee, CEO, CFO

### 1. Executive Summary
- **Compliance Score:** [X/92] = [Y]% (target: [Z]% for this phase)
- **Phase:** [Phase Name] (Weeks [#] of [Total])
- **Status:** On Track / At Risk / Off Track
- **Key Achievement This Month:** [1-2 sentence highlight]
- **Key Risk This Month:** [1-2 sentence concern]

### 2. 17-Domain RAG Status (Heat Map)
| Domain | Status | Checkpoints | % Complete | Trend | Owner |
|---|---|---|---|---|---|
| 1. Consent & Notice | 🟢/🟡/🔴 | [X/8] | [#]% | ↑/→/↓ | [Name] |
| ... (all 17 domains) | | | | | |
| **OVERALL** | **🟢/🟡/🔴** | **[X/92]** | **[#]%** | **↑/→/↓** | |

### 3. Key Metrics Dashboard
| Metric | Target | Current | Status |
|---|---|---|---|
| **Consent Health Score** | ≥97% | [X]% | 🟢/🟡/🔴 |
| **DSAR SLA Compliance** | ≥99% | [X]% | 🟢/🟡/🔴 |
| **Withdrawal Rate** | <10% | [X]% | 🟢/🟡/🔴 |
| **Invalid Consent Rate** | <2% | [X]% | 🟢/🟡/🔴 |
| **Data Breach SLA** | 100% | [X]% | 🟢/🟡/🔴 |
| **Employee Training** | ≥95% | [X]% | 🟢/🟡/🔴 |

### 4. Completed Deliverables This Month
- ✓ [Template T-XX] completed
- ✓ [Domain gap] closed
- ✓ [Milestone] achieved

### 5. In-Progress Work (Next 30 Days)
- 🔄 [Deliverable] — Due [Date] (Owner: [Name])
- 🔄 [Deliverable] — Due [Date] (Owner: [Name])

### 6. Critical Risks & Mitigations
| Risk | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk description] | High/Med/Low | High/Med/Low | [Action] | [Name] |

### 7. Remediation Roadmap (Remaining Gaps)
- **Tier 1 Critical (0 remaining):** [List any open critical gaps]
- **Tier 2 High (X remaining):** [Scheduled completion date per gap]
- **Tier 3 Medium (X remaining):** [Scheduled completion date per gap]

### 8. Incidents & Breaches (This Month)
| Incident | Date | DPBI Notified? | Status |
|---|---|---|---|
| [Incident description] | [Date] | Yes/No | Closed/Open |

### 9. Regulatory Updates
- [New DPDP Rule or court judgment] — Impact: [Assessment]

### 10. Recommendations for Board
1. [Action item #1] — Recommended by [DPO]
2. [Action item #2] — Recommended by [DPO]

**Prepared by:** [DPO] | **Date:** [YYYY-MM-DD] | **Next Report:** [Date]
```

---

## Role Accountability Matrix (RACI)

Who is **R**esponsible, **A**ccountable, **C**onsulted, **I**nformed for each compliance task.

| Compliance Task | DPO | Legal | Compliance | IT Security | Product | HR | Finance | Board |
|---|---|---|---|---|---|---|---|---|
| **Phase 0: Scoping** |
| Entity classification (DF vs SDF) | I | A/R | C | C | I | I | I | A |
| Regulatory overlay assessment | I | A/R | C | I | I | I | I | I |
| **Phase 1: Assessment** |
| Data Inventory (T-03) | C | I | A/R | R | R | R | I | I |
| Data Flow Diagram (T-04) | C | I | I | A/R | C | I | I | I |
| ROPA (T-05) | A/R | C | C | C | C | I | I | I |
| Section 7 Memo (T-06) | C | A/R | C | I | C | I | I | I |
| **Phase 2: Gap Analysis** |
| 17-Domain Scorecard | A/R | C | R | C | C | I | I | I |
| Gap Register (prioritization) | A/R | C | R | C | C | I | I | C |
| **Phase 3: Remediation** |
| Consent form FSIUU compliance | C | C | A | I | A/R | I | I | I |
| DSAR/Rights workflow implementation | C | C | C | A | A/R | C | I | I |
| Vendor DPA negotiation | C | A/R | C | C | I | I | C | I |
| Security controls (encryption, MFA) | C | I | C | A/R | I | I | I | I |
| Employee training | C | C | A | I | I | A/R | I | I |
| **Phase 4: Monitoring** |
| Compliance Dashboard live | A/R | I | R | R | C | I | I | C |
| Consent Registry health metrics | C | I | A/R | I | R | I | I | C |
| Data Discovery scanning | C | I | C | A/R | I | I | I | I |
| Encryption audit | C | I | C | A/R | I | I | I | I |
| **Phase 5: Governance** |
| Privacy Committee Charter | A/R | C | C | I | I | I | I | A |
| Board Resolution | I | C | I | I | I | I | I | A/R |
| Compliance Certificate | A/R | C | C | I | I | I | I | C |
| **Ongoing** |
| Weekly compliance checkpoint | A/R | I | R | I | I | I | I | I |
| Monthly board report | A/R | I | C | I | I | I | I | C |
| Quarterly access review | C | I | C | A/R | I | C | I | I |
| Regulatory change monitoring | A/R | A | R | I | I | I | I | C |
| Breach incident response | A | A | R | A | C | I | I | A |

**Legend:**
- **A** = Accountable (ultimate owner; makes final decision)
- **R** = Responsible (does the work)
- **C** = Consulted (provides input; must be asked)
- **I** = Informed (kept in loop; no input required)

---

## Escalation Triggers & Response Process

### Escalation Matrix

| Condition | Threshold | Action | Owner | SLA | Escalation Path |
|---|---|---|---|---|---|
| **Compliance Score Decline** | Score drops >5% week-over-week | Root cause analysis + remediation plan | DPO | 3 days | DPO → Board Privacy Committee |
| **Consent Health Critical** | Consent health <95% OR Invalid consent >5% | Immediate re-consent campaign + DPBI notification | Compliance | Immediate | Compliance → DPO → Board → DPBI |
| **DSAR/Rights SLA Miss** | >5 DSARs outstanding >30 days | Individual escalation to DPBI; legal review | Legal | 1 day | Legal → DPO → DPBI |
| **Data Breach Detected** | Any confirmed data breach | DPBI notification (72hr) + CERT-In (6hr); Customer notification; Board notification | CISO | Immediate | CISO → DPO → Board → DPBI/CERT-In |
| **Audit Finding CRITICAL** | Critical finding in annual audit | Remediation plan; board emergency session; DPBI notification if SDF | DPO | 10 days | DPO → Board Privacy Committee → Board → DPBI |
| **DPA Not Signed** | Vendor engaged without DPA | Pause data sharing; immediate DPA negotiation or vendor termination | Procurement | 30 days | Procurement → Legal → DPO → Board |
| **Encryption Audit Fail** | Failed encryption audit / weak config | Immediate remediation; security patch release | CISO | 7 days | CISO → IT Security → DPO → Board |
| **Regulatory Change (Critical)** | New DPDP Rule / RBI directive / court order | Legal review; Privacy Notice + template updates; Board notification | Legal | 10 days | Legal → DPO → Board → DPBI (if material) |
| **Inadequate Staffing** | DPO/Compliance understaffed >30% planned | Hire temporary DPO/Compliance consultant OR request budget for hiring | HR | 30 days | HR → CFO → Board |

### Escalation Workflow

```
1. DETECTION
   ↓
2. ASSESSMENT (by Responsible owner)
   "Is this above threshold?"
   ↓
3. IF YES → ESCALATION
   - Owner creates escalation ticket (date, condition, threshold exceeded, evidence)
   - Escalates to Accountable owner
   ↓
4. ACCOUNTABLE DECISION
   - Accepts/rejects escalation
   - If accepted: assigns remediation owner + SLA
   ↓
5. BOARD NOTIFICATION (if critical)
   - DPO sends Board summary
   - Board discusses in Privacy Committee or emergency session
   ↓
6. EXTERNAL ESCALATION (if regulatory)
   - Legal sends notification to DPBI/CERT-In (if required)
   - DPO coordinates external communication
   ↓
7. CLOSURE
   - Remediation complete
   - Escalation ticket closed
   - Root cause analysis documented
```

---

## Resource Allocation by Phase

### Staffing Plan (Full-Time Equivalents)

| Role | Phase 0 | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Ongoing |
|---|---|---|---|---|---|---|---|
| **DPO** | 0.5 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| **Legal** | 0.5 | 0.5 | 0.5 | 1.0 | 0.5 | 0.5 | 0.25 |
| **Compliance Officer** | 0.5 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.5 |
| **IT Security / CISO** | 0.25 | 0.5 | 0.5 | 2.0 | 2.0 | 1.0 | 0.5 |
| **Product Manager (Privacy)** | 0.25 | 0.5 | 0.5 | 1.5 | 1.0 | 0.5 | 0.25 |
| **Data Governance / Analytics** | 0.5 | 1.0 | 0.5 | 0.5 | 0.5 | 0.25 | 0.1 |
| **HR / L&D** | 0.1 | 0.25 | 0.25 | 1.0 | 0.25 | 0.1 | 0.1 |
| **Procurement / Vendor Mgmt** | 0 | 0.25 | 0.25 | 1.0 | 0.5 | 0.25 | 0.1 |
| **Finance** | 0 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.05 |
| **IT Operations (Database)** | 0.1 | 0.25 | 0.25 | 1.0 | 1.0 | 0.5 | 0.25 |
| **QA / Testing** | 0 | 0.25 | 0.25 | 0.5 | 0.5 | 0.25 | 0.1 |
| **Total Team FTE** | **3.65** | **6.4** | **6.1** | **10.6** | **8.25** | **5.5** | **3.2** |

### Budget Estimate by Phase

| Phase | Item | Cost | Notes |
|---|---|---|---|
| **0** | DPO recruitment/onboarding | ₹5-10L | If external hire |
| **1-5** | Tools (DPIA template, audit toolkit, SIEM, DAM) | ₹15-25L | One-time + annual support |
| **1-5** | Training & certification (staff + DPO) | ₹5-10L | External trainers + certifications |
| **3** | Vendor DPA negotiation (legal fees) | ₹10-15L | External counsel if needed |
| **4** | Dashboard/monitoring infrastructure | ₹10-20L | Cloud dashboards, analytics |
| **5** | Independent audit (if SDF) | ₹15-30L | Registered auditor fees |
| **1-5** | Contingency (10% buffer) | ₹10-15L | Unforeseen costs |
| **Total** | | **₹75-145L** | Typical for DF; SDF may be ₹200L+ |

---

## Success Metrics & Definition of Done

### Phase Completion Checklist

**Phase is DONE when:**
- [ ] All KRs for phase met (≥80% threshold)
- [ ] Compliance score meets phase target (Phase 0: ≥50%, Phase 1: ≥60%, Phase 2: ≥70%, Phase 3: ≥80%, Phase 4: ≥90%, Phase 5: ≥97%)
- [ ] All deliverables signed off (DPO or Board depending on phase)
- [ ] No escalated CRITICAL findings outstanding
- [ ] All SLAs (DSAR, deletion, training completion) met ≥95%
- [ ] Team capacity at planned FTE levels (no >20% understaffing)
- [ ] Board approval obtained
- [ ] Documentation archived (templates, ROPA, gap register, audit reports)

---

## Compliance Deadline Countdown

**13 May 2027 Deadline**

| Date | Milestone | Weeks Remaining |
|---|---|---|
| 15 Jan 2026 | Phase 0 starts | 17 weeks |
| 15 Feb 2026 | Phase 1 mid-point | 15 weeks |
| 15 Mar 2026 | Phase 1 complete | 13 weeks |
| 15 Apr 2026 | Phase 2 complete | 11 weeks |
| 15 May 2026 | Phase 3 mid-point | 9 weeks |
| 15 Jun 2026 | Phase 3 complete | 7 weeks |
| 15 Jul 2026 | Phase 4 mid-point | 5 weeks |
| 15 Sep 2026 | Phase 4 complete | 2 weeks |
| 15 Oct 2026 | Phase 5 complete | 27 weeks prior to deadline |
| 15 Nov 2026 - 13 May 2027 | Final audit & buffer | 27 weeks for remediation of late findings |
| **13 May 2027** | **DPDP Compliance Deadline** | **0 weeks** |

---

## References

- [00_MASTER_STRATEGY.md](./00_MASTER_STRATEGY.md) — Overview & timeline
- [01_PHASE_0_SCOPING.md](./01_PHASE_0_SCOPING.md) — Entity classification
- [02_PHASE_1_ASSESSMENT.md](./02_PHASE_1_ASSESSMENT.md) — Data inventory & ROPA
- [03_PHASE_2_GAP_ANALYSIS.md](./03_PHASE_2_GAP_ANALYSIS.md) — 17-domain scorecard
- [04_PHASE_3_REMEDIATION.md](./04_PHASE_3_REMEDIATION.md) — Remediation roadmap
- [05_PHASE_4_MONITORING.md](./05_PHASE_4_MONITORING.md) — Live dashboards
- [06_PHASE_5_GOVERNANCE.md](./06_PHASE_5_GOVERNANCE.md) — Board certification
- [07_DOS_AND_DONTS.md](./07_DOS_AND_DONTS.md) — Critical best practices

---

**Owner:** DPO | **Version:** 1.0 | **Last Updated:** April 2026
