# DPDP Remediation Tracker — Findings & Action Items

**Document:** Remediation Action Register  
**Version:** 1.0 | **Status:** Active  
**Last Updated:** April 15, 2026  
**Audit Report:** Template #49 — Comprehensive DPDP Audit  
**Audit Date:** April 2026  
**Overall Compliance Score:** 92/100

---

## Executive Summary

The comprehensive DPDP compliance audit identified **5 findings** across compliance domains:
- **CRITICAL:** 0 (₹50–100 Cr penalty exposure)
- **HIGH:** 2 (₹25–50 Cr penalty exposure each)
- **MEDIUM:** 2 (₹10–25 Cr penalty exposure each)
- **LOW:** 1 (<₹10 Cr, process improvement only)

**Total Remediation Budget:** ₹4,40,000 over 120 days  
**Target Completion:** December 31, 2026

---

## Detailed Findings Register

### **FINDING: H-001**

**Finding ID:** H-001  
**Title:** Automated Breach Detection & Alerting  
**Domain:** Breach Management (Section 8(6))  
**Severity:** 🟠 HIGH (₹25–50 Cr penalty exposure)  
**SLA:** 60 days | **Target Date:** June 30, 2026

**Problem Statement:**
Breach incidents are currently detected via manual log review and incident reporting. There is no automated real-time alerting system to detect unauthorized access attempts, bulk data exports, privilege escalation, or anomalous API activity. While the organization has a Breach Notification SOP documenting 72-hour notification requirement to DPB, the 72-hour clock only starts *after detection*. Risk: A breach could go undetected for days, causing the 72-hour SLA to be missed.

**Regulatory Reference:**
- **Section 8(6):** "Any failure of security safeguards or personal data breach shall be notified to the Board within 72 hours of discovery."
- **DPDP Rules 2025, Rule 8:** Breach notification must include "detection date" (implies timely detection expectation).

**Current State:**
- ✓ Breach Notification SOP exists (Section 8(6) procedure documented)
- ✓ Incident response team trained
- ✗ SIEM/DAM (Data Activity Monitoring) not deployed
- ✗ No automated alerting for data exfiltration
- ✗ No anomaly detection for privilege escalation
- ✗ Manual log review ad-hoc (daily, but human-dependent)

**Impact Assessment:**
| Risk Dimension | Impact |
|---|---|
| Regulatory | CRITICAL — DPB could assess ₹25–50 Cr penalty for late breach notification |
| Operational | HIGH — 72-hour detection SLA unmet if breach occurs on Friday/holiday |
| Reputational | HIGH — Delayed detection signals poor security posture |
| Customer | HIGH — Breach victims unaware of data exposure risk |

**Recommended Remediation:**
Deploy a **Security Information & Event Management (SIEM)** platform with real-time alerting for:
1. **Data Exfiltration:** Bulk access, uncommon file downloads, API token usage spike
2. **Privilege Escalation:** Multiple failed auth attempts (>5), admin account usage anomalies
3. **Unauthorized Access:** Access from new IP/geography, off-hours access, disabled user account usage
4. **System Events:** Database transaction logs, API rate limit violations, failed encryption integrity checks

**Implementation Roadmap (8 weeks):**

| Week | Phase | Tasks | Owner | Status |
|---|---|---|---|---|
| 1-2 | Vendor Selection | RFP to Splunk, ELK, Azure Sentinel, Wiz, Rapid7 | CISO | 🟡 IN PROGRESS |
| 2-3 | PoC & Testing | Demo with test data; performance baseline; cost comparison | CISO, IT | ⏳ PENDING |
| 3-4 | Proposal Evaluation | Feature gap analysis, reference calls, contract negotiation | CISO, Procurement | ⏳ PENDING |
| 4-5 | Production Setup | Deploy to prod; data pipeline from logs, APIs, databases | IT, Security Eng | ⏳ PENDING |
| 5-6 | Tuning & Integration | Alert rule tuning, false-positive reduction; IRP integration | Security Eng | ⏳ PENDING |
| 6-7 | Staff Training | Analyst training, on-call procedure, escalation playbook | Security Lead | ⏳ PENDING |
| 7-8 | Go-Live & Drill | Activate monitoring, run 72-hour breach simulation drill | CISO | ⏳ PENDING |

**Budget Estimate:**
| Item | Cost |
|---|---|
| SIEM license (1-year, 10GB/day ingestion) | ₹1,50,000 |
| Integration/implementation services | ₹60,000 |
| Training & documentation | ₹20,000 |
| Contingency (10%) | ₹23,000 |
| **TOTAL** | **₹2,53,000** |

**Success Criteria:**
- [ ] SIEM actively monitoring all data sources (logs, APIs, databases)
- [ ] Alert rule set deployed (40+ use cases)
- [ ] <1 hour detection latency for data exfiltration events
- [ ] <5% false-positive rate (tuned within 2 weeks of go-live)
- [ ] 72-hour breach response drill passed (simulated breach detected & notified within 2 hours)
- [ ] Team trained and on-call schedule published

**Owner:** Chief Information Security Officer (CISO)  
**Status:** 🟡 IN PROGRESS (Vendor RFP issued, awaiting proposals)  
**Last Updated:** April 15, 2026

**Risk if Not Remediated:**
- 72-hour breach notification SLA missed → ₹25–50 Cr DPB penalty
- Regulatory inquiry if breach goes undetected for weeks
- Customer trust erosion

---

### **FINDING: H-002**

**Finding ID:** H-002  
**Title:** Retrospective Re-Consent Campaign (Legacy Pre-DPDP Data)  
**Domain:** Consent & Notice (Section 5(2), Section 6)  
**Severity:** 🟠 HIGH (₹25–50 Cr penalty exposure)  
**SLA:** 60 days | **Target Date:** June 30, 2026

**Problem Statement:**
Approximately 12,000 data principals have consents from the pre-DPDP era (before May 13, 2024). These consents lack version tracking and were collected under prior terms & conditions, not the FSIUU-compliant consent forms now in use. Section 5(2) of DPDP Act requires that organizations provide retrospective notice and reconsent opportunities for pre-existing data.

**Regulatory Reference:**
- **Section 5(2):** "If personal data has been collected before the commencement of this Act, the Data Fiduciary shall provide the notice and obtain explicit consent of the Data Principal in the manner as may be specified by rules."
- **DPDP Rules 2025, Rule 5(2):** Retrospective notice must be provided within 6 months of Act commencement (by November 13, 2024). **Deadline EXTENDED to May 13, 2027**, but proactive compliance required.

**Current State:**
- ✓ 12,000 legacy principals identified
- ✓ Current consent forms are FSIUU-compliant
- ✗ Legacy principals not re-consented under new forms
- ✗ No version tracking on pre-DPDP consents
- ✗ Regulatory risk exposure if challenged

**Impact Assessment:**
| Risk Dimension | Impact |
|---|---|
| Regulatory | HIGH — Could be construed as non-compliance with Section 5(2) |
| Legal | HIGH — If challenged, 12,000 principals could claim unauthorized processing |
| Operational | MEDIUM — Multi-channel campaign required (email, SMS, in-app) |
| Reputational | MEDIUM — "We need your consent again" messaging could confuse users |

**Recommended Remediation:**
Execute a **structured re-consent campaign** with:
1. **Multi-channel outreach:** Email (primary), SMS (secondary), in-app notification (tertiary)
2. **Consent form:** FSIUU-compliant, per-purpose, with clear explanation of new DPDP rights
3. **Audit verification:** Post-campaign sample audit (10% = 1,200 consents) for FSIUU compliance
4. **Escalation:** Non-respondents re-targeted at 30, 45, 60-day marks

**Implementation Roadmap (8 weeks):**

| Week | Phase | Tasks | Owner | Status |
|---|---|---|---|---|
| 1-2 | Segmentation & Planning | Segment 12,000 by channel (email pref, SMS pref, app-only); draft messaging | Product, DPO | 🟡 IN PROGRESS (Messaging drafted) |
| 2-3 | Consent Form Design | Create 8 purpose-specific forms (Order Updates, Marketing, Analytics, etc.); legal review | Legal, Product | 📋 PLANNED |
| 3-4 | Localization | Translate notice + forms to Hindi, Tamil, Telugu, Marathi, Gujarati | Localization Vendor | 📋 PLANNED |
| 4-5 | Campaign Launch | Deploy email (Day 1), SMS (Day 2), in-app (Day 3); monitor opt-in rate | Marketing, Product | 📋 PLANNED |
| 5-6 | Response Tracking | Daily dashboard of opt-in rates per purpose; target >70% by Day 30 | Analytics | 📋 PLANNED |
| 6-7 | Audit Sample | Pull 10% sample (1,200); audit for FSIUU compliance (Free, Specific, Informed, Unconditional, Unambiguous) | DPO, Auditor | 📋 PLANNED |
| 7-8 | Escalation & Closure | Re-target non-respondents; final reporting to board | DPO, Product | 📋 PLANNED |

**Budget Estimate:**
| Item | Cost |
|---|---|
| SMS volume (12,000 principals × 2 sends) | ₹18,000 |
| Email platform costs (campaign automation) | ₹8,000 |
| Legal review & consent form drafting | ₹25,000 |
| Localization (5 languages) | ₹15,000 |
| Audit sample testing | ₹10,000 |
| Contingency (10%) | ₹8,400 |
| **TOTAL** | **₹84,400** |

**Success Criteria:**
- [ ] All 12,000 principals sent retrospective notice + consent request
- [ ] Re-consent rate ≥85% within 60 days
- [ ] Audit sample (1,200 consents) ≥98% FSIUU-compliant
- [ ] Consent records stored with version, timestamp, method
- [ ] Board presentation showing campaign completion

**Owner:** Data Protection Officer (DPO) + Product Lead  
**Status:** 🟡 PLANNED (Consent content drafted, segmentation in progress)  
**Last Updated:** April 15, 2026

**Risk if Not Remediated:**
- Regulatory risk if DPB challenges legacy consent validity
- Potential DSAR claims from 12,000 principals questioning processing basis
- ₹25–50 Cr penalty exposure if deemed non-compliant with Section 5(2)

---

### **FINDING: M-001**

**Finding ID:** M-001  
**Title:** Privacy Notice Enhancement — Automated Decision-Making Disclosure  
**Domain:** Consent & Notice (Section 6)  
**Severity:** 🟡 MEDIUM (₹10–25 Cr penalty exposure)  
**SLA:** 90 days | **Target Date:** September 30, 2026

**Problem Statement:**
Current privacy notices comply with core FSIUU requirements but lack explicit disclosure of automated decision-making activities. Section 7 guidance and Section 6 transparency requirement recommend that data principals be informed of:
- What automated decisions are made about them (credit scoring, pricing, risk assessment)
- How those decisions impact them
- Their right to human review and appeal

**Regulatory Reference:**
- **Section 6:** Notice must disclose purpose, scope, processing basis
- **Section 7 (Legitimate Use):** If relying on automated decision-making, transparency required
- **DPDP Rules 2025:** Expect future amendments requiring explicit automated decision disclosure

**Current State:**
- ✓ Privacy notice covers basic FSIUU (Free, Specific, Informed, Unconditional, Unambiguous)
- ✓ Rights disclosure included (access, correct, erase, nominate, grieve)
- ✗ No mention of automated decision-making
- ✗ No disclosure of scoring model factors
- ✗ No explicit appeal/override process documented

**Impact Assessment:**
| Risk Dimension | Impact |
|---|---|
| Regulatory | MEDIUM — Future compliance risk if DPDP Rules amended to mandate automated decision disclosure |
| Legal | MEDIUM — Data principals could challenge legitimacy of decisions without notice |
| Transparency | HIGH — Violates spirit of Section 7 guidance on automated decisions |
| Customer | MEDIUM — Users unaware of how profiling affects them |

**Recommended Remediation:**
Enhance privacy notice to include:
1. **Automated Decisions Section:** List all automated decision-making activities (credit scoring, behavior profiling, fraud detection)
2. **Decision Impacts:** Clearly state consequences of each automated decision
3. **Human Review:** Explicitly offer right to human review/appeal of automated decisions
4. **Opt-Out Options:** Where feasible, allow opt-out from automated decision-making

**Implementation Roadmap (7 weeks):**

| Week | Phase | Tasks | Owner |
|---|---|---|---|
| 1-2 | Audit & Documentation | Identify all 17 automated decision activities; document decision logic | ML Engineering, DPO |
| 2-3 | Notice Drafting | Draft disclosure language per activity; legal review | Legal |
| 4 | Localization | Translate to 5 regional languages | Localization |
| 5 | UX Design | Integrate into web, mobile, email templates | Product, UX |
| 5-6 | A/B Testing | Test with 100-user sample for clarity (comprehension score target: >80) | Analytics |
| 6-7 | Deployment | Deploy to all platforms; monitor comprehension metrics | Product |

**Budget Estimate:**
| Item | Cost |
|---|---|
| Legal review & drafting | ₹12,000 |
| Localization (5 languages) | ₹10,000 |
| UX/design integration | ₹5,000 |
| A/B testing & analytics | ₹3,000 |
| **TOTAL** | **₹30,000** |

**Success Criteria:**
- [ ] Privacy notice updated with automated decision section
- [ ] All 17 automated activities disclosed
- [ ] Comprehension test score ≥80% (user survey)
- [ ] Deployed to web, mobile, email, documents
- [ ] Board approval

**Owner:** Legal / Product  
**Status:** 📋 PLANNED (Audit of automated activities in progress)  
**Target Date:** September 30, 2026

---

### **FINDING: M-002**

**Finding ID:** M-002  
**Title:** DPIA Documentation — Credit Scoring & Behavioral Profiling  
**Domain:** DPIA & Legitimate Uses (Section 7, Rule 6)  
**Severity:** 🟡 MEDIUM (₹10–25 Cr penalty exposure)  
**SLA:** 90 days | **Target Date:** September 30, 2026

**Problem Statement:**
Credit scoring and behavioral profiling are high-risk processing activities (risk of discriminatory decisions, bias, legal liability). DPIA process exists, but activity-specific documentation for credit scoring and behavioral profiling is incomplete. Rule 6 requires DPIA for high-risk activities.

**Regulatory Reference:**
- **Rule 6(1):** SDF must conduct DPIA for high-risk processing
- **Rule 6(2) Mandatory DPIA triggers:** Automated decision-making with legal effect, large-scale processing, systematic monitoring, novel technology

**Current State:**
- ✓ DPIA process framework exists
- ✗ Credit scoring DPIA incomplete
- ✗ Behavioral profiling DPIA incomplete
- ✗ Bias testing not documented
- ✗ Board approval not obtained

**Impact Assessment:**
| Risk Dimension | Impact |
|---|---|
| Regulatory | MEDIUM — Non-compliance with Rule 6 DPIA requirement for high-risk activities |
| Legal | HIGH — Discriminatory decision risk if profiling not properly assessed |
| Reputational | HIGH — If bias detected post-deployment, regulatory & PR crisis |

**Recommended Remediation:**
Complete DPIA workbooks for credit scoring and behavioral profiling, including:
1. **Model Documentation:** Risk factors, training data sources, decision rules
2. **Bias Audit:** Demographic parity testing, disparate impact analysis
3. **Mitigation Controls:** Human override capability, appeals process, monitoring
4. **Board Approval:** DPIA sign-off by DPO + board review

**Implementation Roadmap (8 weeks):**

| Week | Phase | Tasks | Owner |
|---|---|---|---|
| 1-2 | Model Documentation | Collect credit score model params, training data, validation metrics | ML Eng |
| 2-3 | Bias Testing | Engage external ML auditor; conduct demographic parity & disparate impact tests | DPO, External Auditor |
| 3-4 | DPIA Completion | Draft DPIA workbook; document risks, mitigations, residual risks | DPO |
| 5-6 | DPO Review | DPO sign-off on DPIA findings; board presentation prep | DPO |
| 6-7 | Board Approval | Present to board/audit committee; obtain approval | Board |
| 7-8 | Remediation (if needed) | If bias detected, implement fairness controls; re-test | ML Eng |

**Budget Estimate:**
| Item | Cost |
|---|---|
| External ML bias audit | ₹25,000 |
| DPIA workbook development | ₹10,000 |
| Board presentation & approval | ₹3,000 |
| **TOTAL** | **₹38,000** |

**Success Criteria:**
- [ ] Credit scoring DPIA completed & signed by DPO
- [ ] Behavioral profiling DPIA completed & signed by DPO
- [ ] Bias audit score <5% disparate impact
- [ ] Board approval obtained
- [ ] Mitigation controls documented & implemented

**Owner:** DPO / ML Engineering  
**Status:** 📋 PLANNED (Model audit scheduled)  
**Target Date:** September 30, 2026

---

### **FINDING: L-001**

**Finding ID:** L-001  
**Title:** Response SOP Documentation Enhancement  
**Domain:** Data Principal Rights (Sections 11-14)  
**Severity:** 🟢 LOW (<₹10 Cr, process improvement only)  
**SLA:** No deadline | **Target Date:** December 31, 2026

**Problem Statement:**
Current DSAR/rights response workflows perform excellently (avg 4.2d response, 100% <30d SLA compliance). Documentation could be enhanced for edge cases: deceased principals, guardianship, international requests, conflicts.

**Current State:**
- ✓ Workflows exist and perform well
- ✗ SOP lacks edge case procedures
- ✗ Ambiguity resolution process not documented

**Recommended Remediation:**
Enhance SOP documentation with:
1. Deceased principal escalation (estate context)
2. Guardianship verification procedures
3. International DSAR handling
4. Conflict resolution (identity ambiguity, competing claims)

**Owner:** Operations Lead / DPO  
**Status:** 💬 BACKLOG (Post-remediation phase)  
**Target Date:** December 31, 2026 (No urgency)

---

## Remediation Summary Dashboard

```
CRITICAL (30-day SLA)
├─ None identified ✓

HIGH (60-day SLA) — Target: June 30, 2026
├─ H-001: SIEM Deployment — 🟡 IN PROGRESS (Week 2/8)
└─ H-002: Retrospective Campaign — 🟡 PLANNED (Week 2/8)

MEDIUM (90-day SLA) — Target: September 30, 2026
├─ M-001: Privacy Notice Enhancement — 📋 PLANNED (Week 1/7)
└─ M-002: DPIA Profiling — 📋 PLANNED (Week 1/8)

LOW (No deadline) — Target: December 31, 2026
└─ L-001: SOP Documentation — 💬 BACKLOG
```

**Total Budget:** ₹4,40,000  
**Total Effort:** 25-32 weeks (sequential Q2-Q4 2026)  
**Success Rate Target:** 100% of HIGH/MEDIUM findings closed by SLA

---

## Ongoing Obligations (Post-Remediation)

Once remediation completes, maintain ongoing compliance:

| Obligation | Frequency | Owner | Next Due |
|---|---|---|---|
| Consent audit (FSIUU sample) | Quarterly | DPO | Jul 2026 |
| SIEM monitoring & tuning | Continuous | CISO | Ongoing |
| Privacy notice review | Annually | Legal | May 2027 |
| DPIA refresh (credit scoring) | Every 24 months | DPO | Sep 2028 |
| Breach response drill | Annually | CISO | Sep 2027 |

---

*Document End — Remediation Tracker v1.0 — April 15, 2026*
