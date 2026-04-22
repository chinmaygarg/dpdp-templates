# DPDP Compliance Implementation Strategy for NBFC/Fintech Organizations

**Document Type:** Implementation Strategy  
**Target Audience:** NBFC, Fintech, Small & Mid-Size Financial Services Organizations  
**Version:** 1.0  
**Last Updated:** April 2026  
**Deadline:** 13 May 2027 (DPDP Compliance Deadline)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Applicability Determination](#2-applicability-determination)
3. [Phase-by-Phase Implementation](#3-phase-by-phase-implementation)
4. [Personnel Requirements](#4-personnel-requirements)
5. [Manual vs Software Tasks](#5-manual-vs-software-tasks)
6. [Information Mapping](#6-information-mapping)
7. [e-Sahamati Utilization](#7-e-sahamati-utilization)
8. [Data Discovery Software](#8-data-discovery-software)
9. [Mandatory vs Deferrable Items](#9-mandatory-vs-deferrable-items)
10. [Implementation Timeline](#10-implementation-timeline)
11. [Ongoing Compliance Cycle](#11-ongoing-compliance-cycle)

---

## 1. Executive Summary

### Purpose
This document provides a practical implementation roadmap for achieving DPDP (Digital Personal Data Protection) Act 2023 compliance specifically for:
- **Non-Banking Financial Companies (NBFC)**
- **Fintech Organizations**
- **Small to Mid-Size Financial Services Providers**

### Why NBFC/Fintech Must Prioritize
| Factor | Impact on NBFC/Fintech |
|--------|------------------------|
| **RBI Overlay** | 10-year KYC retention (vs DPDP default 6 months) |
| **Sensitive Data** | Financial data, Aadhaar, credit scores = special category |
| **SDF Trigger** | Cross-border processing + automated decisions = likely SDF |
| **Penalty Exposure** | ₹50-100 Crore per violation, up to ₹250 Crore for breach |
| **Trust Impact** | Customer loss after breach/high-profile non-compliance |

### Key Success Metrics
- **Compliance Score:** Target 97%+ (88+ of 92 checkpoints)
- **DSAR SLA:** 99%+ within 30 days
- **Consent Validity:** 98%+ FSIUU-compliant
- **Breach Notification:** 100% within 72 hours to DPBI

---

## 2. Applicability Determination

### Step 1: Are You a Data Fiduciary (DF)?
Answer these questions first:

| Question | Answer | Implication |
|----------|--------|-------------|
| Do you collect personal data (name, phone, email, Aadhaar, PAN, financial info)? | YES/NO | If YES → DF applies |
| Is data processed for Indian residents? | YES/NO | If YES → DPDP applies |
| Do you have Indian customers/users? | YES/NO | If YES → DPDP applies |

**If ALL YES → You are a Data Fiduciary (DF)**

### Step 2: Are You a Significant Data Fiduciary (SDF)?
NBFC/Fintech organizations typically meet SDF criteria due to:

| SDF Criterion | Most NBFC/Fintech? | Notes |
|---------------|-------------------|-------|
| Processing >50 lakh individuals | YES → If 50K+ customers | |
| Processing sensitive personal data | YES → Always (financial, Aadhaar) | |
| Systematic monitoring/automated decisions | YES → Credit scoring, fraud detection | |
| Financial services sector | YES → RBI-regulated | **Strong trigger** |
| Cross-border data transfers | LIKELY → Cloud (AWS AP-South), analytics | |

**If YOU ANSWER "YES" TO ANY → You are an SDF**

### Step 3: Entity Type Classification (NBFC/Fintech)

Select ALL that apply:
- [x] **Financial Services (NBFC)** → RBI overlay applies
- [x] **Fintech/Payment Services** → RBI/SEBI overlay
- [x] **Credit/Loan Services** → Credit Information Act overlay
- [ ] **Insurance** → IRDAI overlay
- [ ] **Wealth Management** → SEBI overlay
- [ ] **Other**

### Step 4: Regulatory Conflict Matrix (RBI + DPDP)

This is CRITICAL for NBFC/Fintech. DPDP default retention periods CONFLICT with RBI requirements:

| Data Category | DPDP Default | RBI Requirement | Resolution |
|--------------|--------------|----------------|-------------|
| KYC Records | 6 months (if no justification) | **10 years** | Use RBI period (mandatory) |
| Transaction Records | 6 months | **8 years** | Use RBI period |
| Loan Documents | 6 months | **8 years post-closure** | Use RBI period |
| Credit Bureau Reports | 6 months | 5 years (CIF) | Use longer |
| CCTV/Security Logs | 90 days | 1 year (if investigation) | Use RBI period |

**ACTION:** Your Data Retention Schedule (T-02A) MUST use the LONGER of DPDP or RBI periods.

---

## 3. Phase-by-Phase Implementation

### Phase 0: Scoping (Weeks 1-2) — START HERE

**Objective:** Determine your DPDP classification and regulatory overlays

| Task | Manual Action | Owner | Deliverable |
|-----|---------------|------|------------|
| 1.1 Complete DPDP Applicability Test | Answer T-01 questions; document classification | Legal/Compliance | Applicability certificate |
| 1.2 Complete Entity Classification | Select entity types (T-02); document overlay regulations | Legal | Entity type matrix |
| 1.3 Identify RBI/SEBI overlay requirements | Cross-reference with RBI master circulars | Legal/Compliance | Regulatory overlay list |
| 1.4 Determine SDF obligations | If SDF, list: DPO, DPIA, Annual Audit, Privacy Committee | DPO Designate | SDF obligations list |
| 1.5 Board presentation | Present roadmap, resource requirements | CTO/CFO | Board sign-off |

**Checklist:**
- [ ] DF or SDF classification documented
- [ ] Entity types assigned
- [ ] RBI/SEBI overlay requirements identified
- [ ] SDF obligations listed (if applicable)
- [ ] Board approved roadmap

---

### Phase 1: Assessment (Weeks 3-10)

**Objective:** Create baseline inventory of all data processing activities

| Task | Manual Action | Owner | Deliverable |
|-----|---------------|------|------------|
| 1.6 System Audit | Catalog all databases, cloud storage, SaaS platforms holding personal data | IT/DPO | Data Inventory (T-03) |
| 1.7 Data Flow Mapping | Document how data moves: entry → storage → processing → sharing → deletion | IT/Product | Data Flow Diagram (T-04) |
| 1.8 ROPA Documentation | Document ALL processing activities per T-05 | DPO | ROPA (T-05) |
| 1.9 Section 7 Legitimate Uses | For non-consent processing (KYC, fraud), document legal basis | Legal | Legitimate Uses Memo (T-06) |
| 1.10 Privacy Notice Review | Audit current privacy notice against T-07 requirements | Legal | Current notice gaps |
| 1.11 Consent Form Audit | Audit existing consent forms against FSIUU requirements | Product/Legal | FSIUU gap analysis |
| 1.12 Historical Consent Review | Sample 100+ historical consents; score FSIUU validity | Compliance | Retrospective Review (T-09) |

**Checklist:**
- [ ] All systems cataloged (T-03)
- [ ] Data flows documented (T-04)
- [ ] Complete ROPA (T-05)
- [ ] Section 7 uses documented (T-06)
- [ ] Privacy notice gaps identified
- [ ] Consent form gaps identified
- [ ] Historical consent review completed

---

### Phase 2: Gap Analysis (Weeks 8-14)

**Objective:** Score compliance across 17 domains; create prioritized remediation roadmap

| Task | Manual Action | Owner | Deliverable |
|-----|---------------|------|------------|
| 1.13 17-Domain Scoring | Score each domain; assign RAG status | DPO/Compliance | Scoring matrix |
| 1.14 Gap Register | Document all gaps with severity | Compliance | Gap register |
| 1.15 Penalty Exposure Calculation | Calculate ₹ exposure per gap by violation type | Legal/Compliance | Risk report |
| 1.16 Remediation Roadmap | Prioritize by penalty exposure | DPO | Remediation plan |

**17-Domain Scorecard:**

| Domain | Weight | Priority | NBFC-Specific Focus |
|--------|--------|----------|---------------------|
| Consent & Notice | 9% | CRITICAL — FSIUU compliance |
| Data Subject Rights | 9% | CRITICAL — DSAR handling |
| Legitimate Uses (S.7) | 7% | CRITICAL — KYC statutory basis |
| Information Security | 13% | CRITICAL — AES-256, RBI cyber controls |
| Children's Data | 4% | MEDIUM — Age verification |
| DPIA & DPO | 5% | HIGH (SDF) — Credit decisions |
| Breach Notification | 7% | CRITICAL — DPBI + CERT-In dual |
| Data Retention & Deletion | 7% | CRITICAL — RBI 10-year conflicts |
| Vendor Management | 8% | HIGH — Cloud, payment processors |
| Cross-Border Transfers | 5% | HIGH — AWS Mumbai, analytics |
| Audit & Monitoring | 5% | HIGH — SIEM, DAM |
| Grievance Handling | 4% | MEDIUM — DPBI escalation |
| Consent Withdrawal | 4% | CRITICAL — Suppression lists |
| Privacy by Design | 3% | MEDIUM — New products |
| Employee Training | 3% | CRITICAL — 95% completion |
| Governance | 4% | HIGH (SDF) — Board committee |

**Checklist:**
- [ ] 17 domains scored
- [ ] All gaps documented
- [ ] Penalty exposure calculated
- [ ] Remediation roadmap approved

---

### Phase 3: Remediation (Weeks 12-24)

**Objective:** Implement all required controls

#### Stream 1: Consent & Privacy Notice

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.17 Privacy Notice Update | Manual content + e-Sahamati template | Legal | Published T-07 |
| 1.18 FSIUU Consent Form | Software: e-Sahamati Consent Manager | Product | Live T-08 |
| 1.19 Retrospective Consent | Manual: re-consent campaign if >5% invalid | Compliance | Re-consent complete |

#### Stream 2: Data Subject Rights

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.20 DSAR Portal | Software: e-Sahamati DSAR module | IT | Live T-10 |
| 1.21 DSAR Response Letter | Manual: template + process | Legal | T-11 |
| 1.22 Correction/Erasure SOP | Manual + software | IT/Legal | T-12 SOP |
| 1.23 Grievance SOP | Manual: escalation process | Legal | T-13 SOP |
| 1.24 Nomination Form | Software + manual | Product | T-14 live |

#### Stream 3: Vendor & Processor Management

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.25 DPA Negotiation | Manual: legal review + signing | Legal/Procurement | 100% DPAs signed |
| 1.26 Vendor Risk Assessment | Manual: questionnaire + scoring | Procurement | T-16 complete |
| 1.27 Sub-processor Register | Software: monitor notifications | Compliance | T-17 register |

#### Stream 4: Security & Breach Response

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.28 Incident Response Plan | Manual: 6-step playbook | CISO | T-20 |
| 1.29 DPBI Notification | Manual: procedure + template | DPO | T-21 |
| 1.30 CERT-In Notification | Manual: 6-hour procedure | CISO | T-21A |
| 1.31 Customer Notification | Manual: breach letter template | Legal | T-22 |
| 1.32 Security Hardening | Software: SIEM, MFA, encryption | IT Security | T-24 |
| 1.33 Audit Logging | Software: enable PII redaction | IT | T-35 |

#### Stream 5: Governance & Policies

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.34 Data Protection Policy | Manual: master policy document | Legal | T-18 |
| 1.35 Employee Training | Manual + software: LMS | HR | 95% completion |
| 1.36 Privacy Committee | Manual: charter + first meeting | Board/DPO | T-39 |
| 1.37 Board Resolution | Manual: formal mandate | Board | T-40 |

**Checklist:**
- [ ] Privacy notice published
- [ ] Consent form FSIUU-compliant
- [ ] DSAR portal live
- [ ] All DPAs signed
- [ ] Breach response plan tested
- [ ] Security controls implemented
- [ ] Board resolution signed

---

### Phase 4: Monitoring (Weeks 20-32)

**Objective:** Deploy live dashboards and ongoing monitoring

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.38 Consent Registry | Software: e-Sahamati dashboard | Compliance | T-31 |
| 1.39 Data Discovery | Software: automated PII scanner | IT Security | Weekly scans |
| 1.40 Encryption Audit | Manual: quarterly verification | CISO | T-33 |
| 1.41 Access Control Review | Manual: quarterly access review | IT | T-34 |
| 1.42 Compliance Dashboard | Software: e-Sahamati | DPO | T-38 live |
| 1.43 Board Risk Report | Manual: quarterly report | DPO | T-37 |

---

### Phase 5: Governance & Certification (Weeks 28-40)

**Objective:** Board certification and perpetual compliance

| Task | Manual/Software | Owner | Deliverable |
|------|---------------|-------|------------|
| 1.44 Privacy Committee | Manual: quarterly meetings | Board | Active |
| 1.45 Board Certification | Manual: compliance certificate | DPO | T-41 |
| 1.46 Annual Audit (SDF) | Manual: independent auditor | External | T-36 |
| 1.47 Ongoing Calendar | Manual + software | DPO | T-45 |
| 1.48 Consent Audit | Manual: quarterly sample | Compliance | T-42 |
| 1.49 Statutory Holds | Manual: RBI hold register | Legal | T-43 |
| 1.50 Cross-Border Register | Manual: transfer documentation | Legal | T-44 |

---

## 4. Personnel Requirements

### Minimum Team for Small NBFC/Fintech (<100 employees, <1L customers)

| Role | Phase 0-1 | Phase 2-3 | Phase 4-5 | Key Responsibilities |
|------|----------|-----------|----------|---------------------|
| **Compliance Lead** | 1.0 | 1.0 | 0.5 | Overall coordination, gap tracking |
| **Legal Counsel** | 0.5 | 0.5 | 1.0 | DPA negotiation, notices, legal memo |
| **IT Security** | 0.3 | 1.0 | 0.5 | SIEM, encryption, access controls |
| **Product/PM** | 0.2 | 0.5 | 0.3 | Consent UI, DSAR workflow |
| **Data Governance** | 0.5 | 0.5 | 0.3 | ROPA, data inventory |

### Mid-Size Team (100-500 employees, 1L-10L customers)

| Role | Phase 0-1 | Phase 2-3 | Phase 4-5 | Key Responsibilities |
|------|----------|-----------|----------|---------------------|
| **DPO** | 1.0 | 1.0 | 1.0 | Board reporting, DPIA, certification |
| **Compliance Manager** | 1.0 | 1.0 | 0.8 | Audit, gap tracking |
| **Legal Counsel** | 0.5 | 1.0 | 1.0 | DPA, notices, legal |
| **CISO** | 0.3 | 1.0 | 0.5 | Security, breach response |
| **IT Manager** | 0.3 | 1.0 | 0.5 | Technical implementation |
| **Product Manager** | 0.2 | 1.0 | 0.3 | Consent UI, DSAR workflow |
| **Data Governance Lead** | 1.0 | 0.5 | 0.3 | ROPA, data inventory |
| **HR/Training** | 0.2 | 0.3 | 0.3 | Employee training |
| **Procurement** | 0.2 | 0.5 | 0.2 | Vendor assessments |

### Large/Enterprise Team (500+ employees, 10L+ customers)

| Additional Roles | Count | Responsibilities |
|----------------|-------|----------------|
| **Deputy DPO** | 1 | Day-to-day operations |
| **Privacy Attorneys** | 2 | DPA negotiation, legal review |
| **Security Analysts** | 2-3 | SIEM, threat monitoring |
| **Data Engineers** | 2 | Data discovery, retention |
| **Consent Operations** | 2 | Consent management, DSAR processing |

---

## 5. Manual vs Software Tasks

### Manual Tasks (Required Human Effort)

| Task | When | Personnel | Justification |
|------|------|-----------|---------------|
| Applicability test completion | Phase 0 | Legal | Legal judgment required |
| Entity classification | Phase 0 | Legal | Regulatory interpretation |
| ROPA documentation | Phase 1 | DPO/Data Governance | Context understanding |
| Section 7 legal memo | Phase 1 | Legal | Legal opinion |
| Privacy notice content | Phase 3 | Legal | Legal language |
| DPA negotiation | Phase 3 | Legal | Contract review |
| Board presentation | All phases | DPO/Executive | Governance |
| Breach investigation | On-incident | CISO | Root cause analysis |
| DPIA (if SDF) | Phase 3 | DPO | Expert judgment |
| Annual audit (SDF) | Phase 5 | External auditor | Independence |

### Software Tasks (Automation/Platform)

| Task | Software | e-Sahamati? | Alternative |
|------|----------|-------------|--------------|
| Consent collection | Consent Manager | **Yes** | OneTrust, Cookiebot |
| Consent registry | Dashboard | **Yes** | RAdyne, BigID |
| DSAR workflow | DSAR Portal | **Yes** | OneTrust, Jira |
| Privacy notice hosting | CMS | Template only | WordPress, Webflow |
| Data discovery | PII Scanner | Build/Integrate | BigID, Spirion, Microsoft Purview |
| Access control | IAM | Build/Integrate | Okta, Azure AD |
| Audit logging | SIEM/DAM | Build/Integrate | Splunk, QRadar |
| Encryption key management | KMS | Build/Integrate | AWS KMS, HashiCorp Vault |
| Data retention automation | Retention engine | Build/Integrate | custom scripts |
| Compliance dashboard | BI Dashboard | **Yes** | PowerBI, Tableau |

### Manual-to-Software Transition Guide

| Phase | Manual Start → Software Goal |
|-------|------------------------------|
| Phase 0-1 | Manual ROPA → Automated ROPA import via data discovery |
| Phase 1 | Manual consent audit → Software consent scoring |
| Phase 2 | Manual DSAR tracking → Software DSAR workflow |
| Phase 3 | Manual breach notification → Automated breach pipeline |
| Phase 4 | Manual weekly scans → Automated data discovery |

---

## 6. Information Mapping

### What Information is Required and Where

| Information | Source | Maps To | Used In |
|-------------|--------|---------|---------|
| **Customer Identifiers** (name, email, phone, Aadhaar, PAN) | Onboarding | Data Inventory (T-03) → ROPA | Consent, DSAR |
| **Financial Data** (income, credit score, loan amount) | Product systems | Data Inventory → ROPA | Processing, retention |
| **KYC Documents** | CRM/Loan system | Data Inventory → Statutory Hold (T-43) | RBI 10-year hold |
| **Transaction History** | Core banking | Data Inventory → ROPA | Processing, audit |
| **Consent Records** | Consent Manager | Consent Registry (T-31) | Withdrawal, DSAR |
| **Third-Party Data** | Vendor systems | Third-Party Inventory (T-25A) | DPA management |
| **Cross-Border Transfers** | IT systems | Transfer Register (T-44) | Section 16 compliance |
| **Employee Data** | HR systems | Employee Policy (T-03A) | Training, DSAR |
| **Processed Personal Data** | All systems | ROPA (T-05) | DPIA, audit |

### Data Flow Mapping (T-04)

```
Customer Onboarding
    ↓
[CRM System] → [KYC Verification] → [Credit Bureau]
    ↓                              ↓
[Loan Origination] → [ disbursement] → [Collections]
    ↓              ↓              ↓
[Cloud Storage]  → [Analytics]    → [Reporting]
    ↓              ↓              ↓
[Cloud (AWS Mumbai/GCP Mumbai) — Cross-Border — Check T-44]
```

### Information-to-Template Mapping

| Template | Information Required | Owner | Usage |
|----------|---------------------|-------|-------|
| T-01 | DF/SDF classification | Legal | Applicability |
| T-02 | Entity types, RBI regulations | Legal | Overlay |
| T-03 | All PII locations | IT/DPO | Inventory |
| T-04 | Data flows | IT | Mapping |
| T-05 | Processing activities | DPO | ROPA |
| T-06 | Legal bases for processing | Legal | Legitimate uses |
| T-07 | Notice content | Legal | Publication |
| T-08 | Consent fields | Product | FSIUU form |
| T-09 | Historical consent | Compliance | Audit |
| T-10 to T-14 | DSAR, correction, erasure, grievance, nominee | Legal | Rights fulfillment |
| T-15 to T-17 | DPA, vendor, sub-processor | Procurement | Vendor management |
| T-18 | Policy content | Legal | Internal policy |
| T-19 | Training content | HR | Employee training |
| T-20 to T-23 | Breach response | CISO | Security |
| T-24 to T-30 | Security, retention, deletion, breach register | IT | Operations |
| T-31 to T-38 | All metrics | Compliance | Monitoring |
| T-39 to T-50 | Governance | Board/DPO | Certification |

---

## 7. e-Sahamati Utilization

### Where e-Sahamati Can Help

| e-Sahamati Module | Phase | How It Helps | Templates |
|------------------|-------|--------------|-----------|
| **Consent UI** | Phase 3 | FSIUU-compliant consent collection | T-08, T-31 |
| **Consent Manager** | Phase 3-4 | Per-purpose tracking, withdrawal, history | T-31, T-42 |
| **DSAR Portal** | Phase 3-4 | Access, correction, erasure requests | T-10 to T-12 |
| **Grievance Handling** | Phase 3-4 | Complaint submission, escalation | T-13 |
| **Nominee Registration** | Phase 3-4 | Nominee form and management | T-14 |
| **Admin Console** | Phase 3-5 | Templates, processors, ROPA, notices | All T-templates |
| **Retention Schedule** | Phase 3 | Data retention configuration | T-02A |
| **Breach Register** | Phase 3 | Incident tracking | T-30 |
| **Compliance Dashboard** | Phase 4-5 | Score tracking | T-38 |
| **Board Reports** | Phase 5 | Pack generation | T-37, T-47 |
| **DPIA Workbooks** | Phase 3 | Impact assessments | T-26 (SDF) |
| **Sub-Processor Register** | Phase 3 | Vendor tracking | T-17 |
| **Encryption Config** | Phase 4 | Security policies | T-24 |
| **Access Control** | Phase 4 | RBAC management | T-34 |
| **Audit Logging** | Phase 4 | Immutable audit trail | T-35 |
| **Privacy Notice** | Phase 1-3 | Web publication | T-07 |
| **ROPA Management** | Phase 1-5 | Processing activities | T-05 |
| **Data Discovery** | Phase 4 | Inventory reporting | T-32 |
| **Statutory Holds** | Phase 5 | Hold register | T-43 |
| **Cross-Border Register** | Phase 5 | Transfer tracking | T-44 |

### e-Sahamati Workflow Integration

```
e-Sahamati Consent Flow:
    e-Sahamati Consent Form (T-08)
        ↓
    Consent Recorded in e-Sahamati DB
        ↓
    e-Sahamati Consent Registry (T-31) ← Dashboard tracks
        ↓
    Withdrawal → e-Sahamati Suppression List
        ↓
    Grievance → e-Sahamati Grievance Workflow (T-13)
        ↓
    DSAR → e-Sahamati DSAR Portal (T-10)


e-Sahamati DSAR Flow:
    Data Principal submits DSAR (T-10 form)
        ↓
    e-Sahamati validates identity
        ↓
    Request enters e-Sahamati workflow
        ↓
    Processing team receives task
        ↓
    Response prepared with e-Sahamati (T-11 template)
        ↓
    30-day SLA tracked in e-Sahamati
        ↓
    Completion logged (T-29 deletion log if erasure)
```

### Where You Need Additional Tools

| Gap | Recommended Additional Tool | Phase |
|-----|--------------------------|-------|
| Data Discovery/PII Scanning | Microsoft Purview, BigID, Spirion | Phase 1-4 |
| SIEM/Security Monitoring | Splunk, QRadar, Microsoft Sentinel | Phase 3-4 |
| DAM/Database Audit | Imperva, Oracle Audit Vault | Phase 3-4 |
| Cloud Security Posture | Prisma Cloud, Wiz | Phase 3-4 |
| Identity Access Management | Okta, Azure AD | Phase 3-4 |
| Encryption Key Management | AWS KMS, HashiCorp Vault | Phase 3-4 |
| LMS/Employee Training | TalentLMS, Docebo | Phase 3 |
| Compliance GRC | ServiceNow GRC, RSA Archer | Phase 2-5 |
| Annual Audit (SDF) | Big4 firm or registered auditor | Phase 5 |

---

## 8. Data Discovery Software

### When Is Data Discovery Software Required?

| Scenario | Data Discovery Needed? | Why |
|----------|-------------------------|-----|
| **Phase 1: System Audit** | YES (Manual + Software) | Cannot manually catalog all data |
| **30+ Systems with personal data** | YES | Scale makes manual impossible |
| **Cloud multi-environment** | YES | AWS/Azure/GCP = distributed |
| **Multiple databases** | YES | Each DB needs scanning |
| **Historical data migration** | YES | Find all PII before moving |
| **Weekly monitoring (Phase 4)** | YES | Ongoing automated scanning |
| **Acquisition/M&A** | YES | Due diligence, data inventory |

### Manual Alternative (For Budget-Constrained Orgs)

**Manual Data Discovery Process (Phases 0-1):**
1. Interview IT owners of each system (2-3 people per system)
2. Request database schemas from DBAs
3. Search sample data using SQL queries:
   ```sql
   SELECT column_name FROM information_schema.columns 
   WHERE table_name = 'customers' AND column_name LIKE '%name%';
   ```
4. Document findings in T-03 Data Inventory
5. Validate with system owners
6. Update ROPA

**Manual Works For:** <20 systems, small databases, simple architecture
**Manual Does NOT Work For:** Cloud-first, 20+ systems, complex data flows

### Recommended Data Discovery Tools

| Tool | Best For | Approximate Cost (₹) | Deployment |
|------|----------|---------------------|------------|
| **Microsoft Purview** | Enterprise, MS-heavy | 15-30 L/year | 4-6 weeks |
| **BigID** | Enterprise, cross-platform | 25-50 L/year | 4-8 weeks |
| **Spirion** | Mid-market | 10-20 L/year | 2-4 weeks |
| **Open-source (tagpipe)** | Budget-conscious | Free | 8-12 weeks |

---

## 9. Mandatory vs Deferrable Items

### MANDATORY (Do First)

| Item | Phase | Deadline | Owner | Penalty if Ignored |
|------|-------|----------|-------|---------------------|
| **DF/SDF Classification** | 0 | Week 2 | Legal | Wrong obligations |
| **DPO Appointment (SDF)** | 0 | Before Phase 1 | Board | ₹50-100 Cr |
| **Privacy Notice (T-07)** | 1 | Week 8 | Legal | ₹50-100 Cr |
| **ROPA (T-05)** | 1 | Week 10 | DPO | ₹25-50 Cr |
| **Section 7 Memo (T-06)** | 1 | Week 10 | Legal | ₹25-50 Cr |
| **FSIUU Consent (T-08)** | 3 | Week 20 | Product | ₹50-100 Cr |
| **DSAR Workflow (T-10-14)** | 3 | Week 20 | Legal/IT | ₹50-100 Cr |
| **DPA Signing (T-15)** | 3 | Week 24 | Procurement | ₹50-100 Cr |
| **Security Controls (T-24)** | 3 | Week 24 | CISO | ₹50-100 Cr |
| **Breach Response (T-20-23)** | 3 | Week 24 | CISO | ₹50-100 Cr |
| **Data Retention (T-02A)** | 3 | Week 24 | IT | ₹25-50 Cr |
| **Employee Training (T-19)** | 3 | Week 24 | HR | ₹10-25 Cr |
| **Board Resolution (T-40)** | 3 | Week 24 | Board | Governance gap |
| **Privacy Committee (SDF)** | 5 | Week 36 | Board | Governance gap |
| **Compliance Certificate (T-41)** | 5 | Week 40 | DPO | No certification |
| **Annual Audit (SDF)** | 5 | Week 40 | External | Regulatory risk |

### DEFER/IGNORE (Do Later or If Applicable)

| Item | Defer Until | Why deferrable |
|------|-------------|----------------|
| **Multi-language privacy notice** | Phase 4 | English compliant; expand later |
| **Cross-Border Transfer Register** | If no active transfers | T-44 only needed if transfers exist |
| **DPIA Register (SDF)** | If planning new high-risk processing | T-46 only needed for specific activities |
| **Sub-processor approval workflow** | Phase 4 | Only needed if vendors engage sub-processors |
| **Video analytics consent** | If implementing video | Only needed if using video data |
| **Children's specific controls** | If serving minors | Only needed if product serves <18 |
| **Biometric authentication** | If implementing | Only needed if using biometrics |
| **Automated decision-making DPIA** | If implementing new ML | Only needed for new high-risk processing |

### NBFC-Specific Mandatory Items (RBI Overlay)

| Item | Why Mandatory | Template |
|------|---------------|----------|
| **KYC 10-year retention** | RBI Master Circular | T-02A |
| **Transaction 8-year retention** | RBI requirement | T-02A |
| **Loan document 8-year hold** | RBI requirement | T-02A |
| **Credit bureau reporting合规** | Credit Information Act | T-06 |
| **AML/KYC processing** | PMLA requirements | T-06 (S.7) |
| **CERT-In breach notification** | cybersecurity rules | T-21A |

---

## 10. Implementation Timeline

### Quick Start Timeline (DF Only, <6 months)

| Week | Task | Owner |
|-----|-----|-------|
| 1-2 | Phase 0: Classification | Legal |
| 3-6 | Phase 1: Assessment (T-03 to T-09) | DPO |
| 7-10 | Consent + Privacy Notice (T-07, T-08) | Legal/Product |
| 11-14 | DSAR workflows (T-10 to T-14) | IT/Legal |
| 15-18 | Breach response (T-20 to T-23) | CISO |
| 19-24 | Monitoring + Governance | DPO/Board |

### Standard Timeline (DF + SDF, 9-12 months)

| Week | Task | Owner |
|-----|-----|-------|
| 1-2 | Phase 0: Classification | Legal |
| 3-10 | Phase 1: Full Assessment | DPO |
| 8-14 | Phase 2: Gap Analysis | Compliance |
| 12-24 | Phase 3: Full Remediation | All streams |
| 20-32 | Phase 4: Monitoring | IT/Compliance |
| 28-40 | Phase 5: Governance | Board/DPO |

### FinTech-Specific Timeline (NBFC SDF, 12-18 months)

| Week | Task | Additional NBFC Focus |
|-----|-----|----------------------|
| 1-2 | Phase 0: Classification + RBI overlay | RBI compliance review |
| 3-10 | Phase 1: Assessment + KYC retention | 10-year retention mapping |
| 8-14 | Phase 2: Gap Analysis + RBI conflicts | RBI/DPDP conflict resolution |
| 12-24 | Phase 3: Full Remediation + AML | PMLA compliance |
| 20-32 | Phase 4: Monitoring + Credit Bureau | Credit Information Act |
| 28-40 | Phase 5: Governance + RBI audit | Annual RBI inspection ready |

---

## 11. Ongoing Compliance Cycle

### Monthly Tasks

| Task | Owner | Frequency |
|------|-------|----------|
| Consent health score review | Compliance | Weekly |
| DSAR SLA tracking | Legal | Weekly |
| Deletion SLA tracking | IT | Weekly |
| KPI dashboard review | DPO | Weekly |
| Breach indicators | CISO | Real-time |

### Quarterly Tasks

| Task | Owner | When |
|------|-------|------|
| Privacy Committee meeting | Board | Q1, Q2, Q3, Q4 |
| Board Risk Report (T-37) | DPO | End of each quarter |
| Consent audit sample (T-42) | Compliance | Each quarter |
| Statutory hold review (T-43) | Legal | Each quarter |
| Cross-border transfer audit (T-44) | Legal | Each quarter |
| Access control review (T-34) | IT Security | Each quarter |
| Data Discovery scan | IT Security | Semi-annual |

### Annual Tasks

| Task | Owner | When |
|------|-------|------|
| Independent audit (SDF) | External auditor | Before May 13 |
| Privacy notice review | Legal | Annual |
| Employee training refresh | HR | Annual |
| DPA re-validation | Procurement | Annual |
| Board re-certification | DPO | Annual |
| Compliance score report | DPO | Annual |

---

## Appendix: Key Templates Quick Reference

| Template ID | Name | Phase | Mandatory for DF | Mandatory for SDF |
|------------|------|-------|---------------|----------------|
| T-01 | Applicability Test | 0 | YES | YES |
| T-02 | Entity Classification | 0 | YES | YES |
| T-03 | Data Inventory | 1 | YES | YES |
| T-04 | Data Flow Diagram | 1 | YES | YES |
| T-05 | ROPA | 1 | YES | YES |
| T-06 | Section 7 Memo | 1 | YES | YES |
| T-07 | Privacy Notice | 1 | YES | YES |
| T-08 | Consent Form | 1 | YES | YES |
| T-09 | Retrospective Consent | 1 | YES | YES |
| T-10 to T-14 | DSAR, Rights | 3 | YES | YES |
| T-15, T-16 | DPA, Vendor | 3 | YES | YES |
| T-18 | Data Protection Policy | 3 | YES | YES |
| T-19 | Employee Training | 3 | YES | YES |
| T-20 to T-23 | Breach | 3 | YES | YES |
| T-24 | Security Hardening | 3 | YES | YES |
| T-25, T-28 | Audit Plan | 2 | - | YES |
| T-26 | DPIA | 3 | - | YES |
| T-30 | Breach Register | 3 | YES | YES |
| T-31 to T-38 | Monitoring | 4 | YES | YES |
| T-39 | Privacy Committee | 5 | - | YES |
| T-40 | Board Resolution | 5 | YES | YES |
| T-41 | Compliance Certificate | 5 | YES | YES |
| T-42 | Consent Audit | 5 | YES | YES |
| T-43 | Statutory Holds | 5 | YES | YES |
| T-44 | Cross-Border | 5 | If applicable | If applicable |
| T-45 | Ongoing Calendar | 5 | YES | YES |
| T-46 | DPIA Register | 5 | - | YES |
| T-47 | Board Pack | 5 | YES | YES |

---

## Summary: Critical Success Factors

1. **DPO Appointment:** If SDF, appoint before Phase 1
2. **RBI Conflict Resolution:** Use longer retention (10yr for KYC)
3. **FSIUU Consent:** Ensure 5/5 validity score
4. **Breach Notification:** 72-hour DPBI + 6-hour CERT-In
5. **Data Discovery:** Automated scanning for 30+ systems
6. **Board Sponsorship:** Executive buy-in critical
7. **Vendor DPA Coverage:** 100% signed before Phase 5
8. **Training Completion:** Target 95%+ staff trained
9. **Ongoing Monitoring:** Live dashboards by Phase 4
10. **Annual Audit (SDF):** Independent auditor by May 2027

---

**Document Navigation:**
← [Back to DPDP Compliance Navigator](../INDEX_DPDP_Compliance_Navigator.html)

---

**Last Updated:** April 2026  
**Next Review:** Quarterly (Q1-Q4)  
**Owner:** DPO  
**Board Approval:** [Date/Signature]

---

**End of Document**