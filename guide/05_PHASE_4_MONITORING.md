# Phase 4: Monitoring — Live Dashboards & Audit Readiness

**Duration:** Weeks 9-20 (May-September 2026) | **Effort:** 8-10 weeks | **Owner:** IT, Analytics, Compliance | **Templates:** T-31 to T-38

---

## Overview

Deploy real-time monitoring dashboards to track DPDP compliance health and detect violations.

---

## 8 Monitoring Components

### 1. **Consent Registry Dashboard (T-31)**
- **Metrics:** Per-purpose consent %, withdrawal rate, invalid consent rate, FSIUU validity score
- **Alerts:** >15% withdrawal rate (red flag), >5% invalid consent (critical)
- **Frequency:** Updated daily; reviewed weekly by Compliance
- **Owner:** Compliance

### 2. **Data Discovery Report (T-32)**
- **Function:** Automated PII scanning across all systems
- **Scan Scope:** Databases, cloud storage, backups
- **Frequency:** Weekly; escalate unknown PII concentrations
- **Owner:** IT Security

### 3. **Encryption Verification (T-33)**
- **Audit:** Verify AES-256 at rest, TLS 1.3+ in transit
- **Checklist:** Aadhaar VID-only rule, PAN masking (XXXXXXX1234)
- **Frequency:** Quarterly; penetration test annually
- **Owner:** CISO

### 4. **Access Control Policy (T-34)**
- **Control:** Role-based access (RBAC), least privilege
- **MFA:** Mandatory for admin; required for sensitive data access
- **Quarterly Access Review:** Verify all accounts still active/justified
- **Owner:** IT Security

### 5. **Audit Logging Configuration (T-35)**
- **Immutable Logs:** INSERT-only database; no UPDATE/DELETE
- **PII Redaction:** Regex patterns remove sensitive data before logging
- **Hash-Chaining:** Detect log tampering
- **Retention:** 7 years per DPDP breach archive requirement
- **Owner:** IT Security

### 6. **Annual SDF Audit (T-36, if applicable)**
- **Independent Auditor:** Appoint registered auditor
- **Audit Scope:** Verify all 92 checkpoints implemented correctly
- **Report:** Due to DPBI; findings reported to Board
- **Frequency:** Annual (if SDF)
- **Owner:** DPO

### 7. **Board Risk Committee Report (T-37)**
- **Content:** Compliance score (0-100%), domain RAG status, breach summary, remediation roadmap
- **Frequency:** Quarterly (each Q1-Q4)
- **Audience:** Board Audit Committee
- **Owner:** DPO

### 8. **Compliance Tracking Dashboard (T-38)**
- **Score:** (Checkpoints Completed / 92) × 100
- **17-Domain Scorecard:** Current status per domain, weight, penalty exposure
- **DSAR SLA Tracker:** Response times for each DSAR request
- **Update Frequency:** Weekly; published to Board monthly
- **Owner:** DPO

---

## KPI Monitoring Schedule

| KPI | Target | Frequency | Owner | Alert Threshold |
|---|---|---|---|---|
| Consent Health Score | ≥97% | Daily | Compliance | <95% |
| DSAR SLA Compliance | ≥99% (30-day) | Weekly | Legal | <95% |
| Withdrawal Rate | <10% | Weekly | Product | >15% |
| Invalid Consent Rate | <2% | Weekly | Compliance | >5% |
| Data Breach SLA (72-hr DPBI) | 100% | Per incident | CISO | Any miss |
| Deletion SLA (30-day) | ≥99% | Weekly | IT | <95% |
| Security Audit Status | No CRITICAL findings | Quarterly | CISO | Any finding |
| Compliance Score | ≥97% (92 checkpoints) | Monthly | DPO | <90% |

---

## Escalation Triggers

| Condition | Action |
|---|---|
| **Consent Score <95%** | DPO review + form audit; potentially re-collect consents |
| **>5% Invalid Consents** | Critical incident; pause marketing; re-consent affected principals |
| **>15% Withdrawal Rate** | Data Principal trust issue; review messaging + suppression list sync |
| **DSAR >30 days** | Individual escalation path to DPBI; legal review |
| **Breach SLA Missed** | DPBI escalation risk; post-incident review mandatory |
| **Compliance Score <90%** | Board Privacy Committee emergency session |

---

## Deliverables

- [ ] **T-31:** Consent Registry Dashboard live
- [ ] **T-32:** Data Discovery Report (weekly scans automated)
- [ ] **T-33:** Encryption audit completed; India-specific rules verified
- [ ] **T-34:** Access control policy + quarterly review process live
- [ ] **T-35:** Audit logging with PII redaction + hash-chaining operational
- [ ] **T-36:** Independent auditor appointed; audit plan finalized (if SDF)
- [ ] **T-37:** First Board Risk Committee report delivered
- [ ] **T-38:** Compliance Dashboard live; compliance score ≥90%

→ [Next: Phase 5 Governance](./06_PHASE_5_GOVERNANCE.md)

---

**Owner:** IT, Compliance | **Board Approval:** [Date/Signature]
