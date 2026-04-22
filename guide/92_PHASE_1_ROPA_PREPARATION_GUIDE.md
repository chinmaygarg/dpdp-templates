# Phase 1: ROPA Preparation Guide
## How to Prepare ROPA During Phase 1: Assessment (Weeks 1-4)

**Document Version:** 1.0  
**Last Updated:** April 2026  
**Status:** DPDP Compliance Framework  
**Audience:** DPO, Compliance Officers, IT Leads, Project Managers

---

## Table of Contents

1. [Overview](#overview)
2. [Week-by-Week Execution Plan](#week-by-week-execution-plan)
3. [Data Discovery & Systems Mapping](#data-discovery--systems-mapping)
4. [Processing Activity Documentation](#processing-activity-documentation)
5. [Legal Basis Classification](#legal-basis-classification)
6. [ROPA Spreadsheet Creation](#ropa-spreadsheet-creation)
7. [Templates & Tools](#templates--tools)
8. [Common Mistakes & Solutions](#common-mistakes--solutions)
9. [DPO Review & Sign-Off](#dpo-review--sign-off)
10. [Success Criteria](#success-criteria)

---

## Overview

### Purpose of Phase 1

Phase 1 is the **Assessment phase** (Weeks 1-4) where you:
- **Discover** all systems holding personal data
- **Map** existing processing activities
- **Document** legal basis, retention, and data flows
- **Create** the ROPA Spreadsheet (Draft)
- **Identify** compliance gaps for Phases 2-5

### What is ROPA?

**ROPA (Record of Processing Activities)** is a comprehensive inventory of every data processing activity in your organization, required by **DPDP Act 2023, Section 8**.

Each ROPA entry documents:
- **What** data is processed and **Why**
- **Who** can access it and **Where** it goes
- **How long** it's kept and **How** it's deleted
- **What controls** protect it (encryption, access logs, DPIA)
- **Who approved** it and **When** it needs review

### Phase 1 Output

```
✅ ROPA Spreadsheet (Draft Status)
   ├── 15-40 processing activities documented
   ├── All mandatory fields populated
   ├── Risk levels assigned (High/Medium/Low)
   ├── Legal basis determined (Section 6 vs Section 7)
   └── DPO preliminary review completed

✅ Systems Inventory
   ├── All databases/applications cataloged
   ├── Data flow diagrams
   └── Access control summary

✅ Compliance Gap Register
   ├── High-risk activities requiring DPIA (Phase 4)
   ├── Missing consent mechanisms (Phase 3)
   ├── Retention policy gaps (Phase 2)
   └── Third-party DPA gaps (Phase 2)

✅ DPO Sign-Off
   └── "Baseline established. Data flows captured accurately."
```

---

## Week-by-Week Execution Plan

### Quick Reference Timeline

| Week | Focus | Key Activities | Deliverable |
|------|-------|-----------------|-------------|
| **Week 1** | Systems & Data Inventory | IT audit, database scan, systems catalog | Systems Registry (all apps cataloged) |
| **Week 2** | Processing Discovery | Stakeholder interviews, existing docs review | Processing Activities List (15-40 items) |
| **Week 3** | Compliance Mapping | Legal basis determination, risk assessment | ROPA with context (legal, risk, retention) |
| **Week 4** | ROPA Creation & Review | Spreadsheet compilation, DPO review, approval | **ROPA Spreadsheet (Draft)** + Sign-off |

---

## Data Discovery & Systems Mapping

### Week 1: Identify All Systems & Databases

**Goal:** Create a complete inventory of systems holding personal data

#### Step 1.1: Conduct IT Systems Audit

**Responsible:** IT/Tech Lead, DBA

**Actions:**
```
1. List all production databases
   └── CRM, HR, Finance, Customer, Logs, Analytics, etc.

2. Identify all applications
   └── Web apps, mobile apps, APIs, integrations

3. Document cloud services
   └── AWS, Azure, Google Cloud, Salesforce, HubSpot, etc.

4. Review file storage
   └── On-premise servers, cloud storage (S3, OneDrive, etc.)

5. Catalog backup & disaster recovery systems
   └── Archive locations, tape storage, replication systems
```

#### Step 1.2: Systems Registry Template

Create a spreadsheet with the following columns:

| Column | Example | Notes |
|--------|---------|-------|
| **System ID** | SYS-001 | Unique identifier |
| **System Name** | Salesforce CRM | Official name |
| **System Type** | Database / Cloud App / API | Category |
| **Data Owner** | Head of Sales | Who's responsible |
| **Data Custodian** | IT/Database Team | Technical owner |
| **Location** | AWS ap-south-1 | Where it's hosted |
| **Access Method** | Internal network, VPN, Public API | How accessed |
| **Data Sensitivity** | High / Medium / Low | Classification |
| **# of Records** | ~50,000 | Approximate scale |
| **# of Users** | 25 | Who accesses it |
| **Connected Systems** | ERP, Email, Analytics | Integrations |
| **Backup Location** | AWS S3 Glacier | DR details |
| **Notes** | Legacy system, plans to migrate 2027 | Context |

#### Step 1.3: Database Schema Review

**For each database:**

```sql
-- Query to discover tables and columns
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY table_name, ordinal_position;

-- Identify potential personal data fields
-- Pattern matching: name, email, phone, address, id_number, ssn, 
-- bank_account, health_data, biometric_data, ip_address, etc.
```

**Create Data Inventory Sheet:**

| Table Name | Column Name | Data Type | Sample Values | Sensitivity | Notes |
|-----------|------------|-----------|---------------|-------------|-------|
| customers | id | UUID | 550e8400-e29b | Low | Customer ID |
| customers | email | VARCHAR | user@example.com | High | Email address |
| customers | aadhaar_hash | VARCHAR | sha256(...) | Critical | Biometric ID |
| customers | annual_income | DECIMAL | 500000 | High | Financial |
| loans | loan_status | ENUM | active, closed | Low | Business data |

#### Step 1.4: Cloud Services Audit

**Check:**
```
☐ SaaS applications (Salesforce, HubSpot, Jira, Slack, etc.)
☐ Cloud infrastructure (AWS, Azure, GCP)
☐ Email service (Gmail, Office 365, etc.)
☐ Document storage (Google Drive, OneDrive, Dropbox)
☐ Analytics platforms (Google Analytics, Mixpanel, etc.)
☐ Payment processors (Stripe, Razorpay, etc.)
☐ Communication platforms (Twilio, SendGrid, etc.)
☐ Monitoring & logging (CloudWatch, DataDog, Splunk)
```

**For each, document:**
- Service name & vendor
- Data types processed
- Data location (region/country)
- Access credentials & authentication
- Backup/retention settings
- Data sharing with sub-processors

#### Week 1 Deliverable: Systems Registry

**Format:** Excel/Google Sheets with tabs:
- Tab 1: Systems Inventory (complete list)
- Tab 2: Database Schemas (tables & sensitive columns)
- Tab 3: Cloud Services (SaaS audit)
- Tab 4: Integration Map (how systems connect)

**Sign-off:** IT Lead confirms accuracy

---

## Processing Activity Documentation

### Week 2: Discover Processing Activities

**Goal:** For each system, document WHAT data is processed and WHY

#### Step 2.1: Stakeholder Interviews

**Schedule:** 1-hour meetings with department heads/data owners

**Participants by Role:**

| Role | Stakeholders | Questions Focus |
|------|--------------|-----------------|
| **Finance/CFO** | Finance Lead, RBI Compliance Officer | KYC, AML, loan processing, payment processing |
| **HR/People** | HR Manager, Payroll, Recruitment Lead | Employee data, payroll, benefits, training, background checks |
| **Sales/Marketing** | CMO, Sales Lead, Marketing Manager | Lead generation, customer data, campaigns, behavioral tracking |
| **Operations** | COO, Operations Manager | Supply chain, vendor management, logistics |
| **Tech/IT** | CTO, DBA, Security Lead | System logs, access controls, monitoring, backups |
| **Legal/Compliance** | General Counsel, Compliance Officer | Regulatory requirements, statutory holds, audit logs |

#### Step 2.2: Interview Questionnaire

**Use this template for each department:**

```markdown
## Department: ________________
## Interviewee: ________________
## Date: ________________

### 1. SYSTEMS & APPLICATIONS
- What systems/applications does your team use?
- What personal data does each system collect?
- Where is this data stored (on-premise/cloud)?
- How is it backed up?

### 2. DATA COLLECTION
- What personal data do you collect? (Aadhaar, email, phone, etc.)
- How is it collected? (Forms, API, import, manual entry)
- Is this data optional or mandatory?
- Do you have user consent forms?

### 3. PURPOSE & USE
- Why do you collect this data? (Business purpose)
- What do you use it for?
- How often is it used?
- Is it used for any of these?
  ☐ Regulatory compliance (RBI, SEBI, PMLA, GST)
  ☐ Fraud detection
  ☐ Marketing/sales
  ☐ Customer support
  ☐ Product improvement
  ☐ Analytics/reporting

### 4. DATA SHARING & RECIPIENTS
- Who in your organization accesses this data?
- Do you share this data with external parties? (vendors, partners, regulators)
- Do you have Data Processing Agreements (DPA) with them?
- Is data shared with government agencies?

### 5. RETENTION & DELETION
- How long do you keep this data?
- Why? (Business need / legal requirement / other)
- How is data deleted when no longer needed?
- Are there any statutory hold requirements?
  ☐ RBI: 8 years (banking)
  ☐ PMLA: 5 years (AML)
  ☐ GST: 6 years (tax)
  ☐ CERT-In: 180 days (security)
  ☐ Labor law: 2-3 years (employment)

### 6. DATA TRANSFERS
- Is data sent outside India?
- To which countries?
- Are those countries on the RBI whitelist?
- What's the legal basis for transfer?

### 7. RISK & SPECIAL DATA
- Does your team process sensitive data? (health, biometric, etc.)
- Do you make automated decisions with this data? (credit scoring, profiling)
- Is children's data involved?
- Any data breaches or incidents?

### 8. DOCUMENTATION
- Do you have consent forms? (can we see them?)
- Do you have retention policies? (can we see them?)
- Are there any privacy notices? (current/outdated?)
- Any vendor/processor contracts?

### 9. COMPLIANCE GAPS
- What compliance challenges do you see?
- What would you like to improve?
```

#### Step 2.3: Document Review

**Collect and review:**

1. **Existing Privacy Notices** (from website, forms)
   - What purposes are documented?
   - What data categories are listed?
   - Are retention periods mentioned?

2. **Consent Forms** (if any)
   - What data is being consented to?
   - How is consent recorded?
   - Is withdrawal mechanism available?

3. **Data Retention Policies**
   - What are current retention periods?
   - Are they documented?
   - Are they compliant with DPDP?

4. **Vendor/Processor Agreements**
   - Who are the third parties?
   - Are DPAs in place?
   - What data do they process?

5. **Regulatory Documentation**
   - RBI/SEBI/PMLA compliance docs
   - Statutory retention requirements
   - Regulatory reporting obligations

6. **Employee Handbooks**
   - Employee data collection practices
   - Data access policies
   - Privacy practices

#### Step 2.4: Processing Activities List Template

**Create spreadsheet with columns:**

| Activity ID | Activity Name | Department | System | Data Types | Primary Purpose | Secondary Purposes | Legal Basis Claim | High-Risk | Notes |
|-------------|---------------|-----------|--------|-----------|-----------------|-------------------|------------------|-----------|-------|
| PA-001 | Customer KYC | Finance | CRM | Aadhaar, PAN, Address | AML Compliance | Loan underwriting | Section 7 | Yes | Biometric data |
| PA-002 | Employee Payroll | HR | HR System | SSN, Bank Account | Salary processing | Tax compliance | Section 7 | No | Statutory requirement |
| PA-003 | Marketing Emails | Sales | Email Platform | Email, Behavior | Lead nurturing | Product recommendations | Section 6 | No | Requires consent |
| PA-004 | Website Analytics | IT | Google Analytics | IP, Device ID, Behavior | Performance metrics | Product improvement | Section 6? | No | Cookie consent needed |

#### Week 2 Deliverable: Processing Activities List

**Output:**
- List of 15-40 processing activities
- For each: department, system, data types, stated purpose
- Links to relevant documents (consent forms, policies, etc.)
- Notes on gaps or questions

**Sign-off:** Department heads confirm accuracy of their activities

---

## Legal Basis Classification

### Week 3: Determine Legal Basis & Risk Level

**Goal:** For each activity, determine if it's based on Section 6 (Consent) or Section 7 (Legitimate Use)

#### Step 3.1: Understand DPDP Legal Basis

**Section 6: Consent** (FSIUU Requirements)
```
When to use:
✓ Marketing & promotional activities
✓ Behavioral profiling & analytics (non-essential)
✓ Optional data collection (not required for core service)
✓ Automated decision-making (except for credit/employment)
✓ Cross-border transfers (to non-whitelisted countries)

Requirements:
✓ Specific consent form per purpose
✓ Easy withdrawal mechanism
✓ Granular & unbundled (separate checkboxes per purpose)
✓ Consent audit log
✓ Affirmative action (opt-in, not opt-out)

NOT Allowed Under Section 6:
✗ Pre-ticked boxes
✗ Bundled consent
✗ Misleading language
✗ Consent from intermediary (must be from data principal)
```

**Section 7: Legitimate Uses** (No Consent Required)
```
Allowed Uses (FinTech/NBFC relevant):
✓ KYC / AML compliance (regulatory requirement)
✓ Fraud detection & prevention (legitimate interest)
✓ Employee background verification (employment)
✓ Credit/loan assessment (legitimate business)
✓ RBI/regulatory reporting (statutory obligation)
✓ Court-ordered disclosure (legal requirement)
✓ Debt recovery (contractual obligation)
✓ Dispute resolution (legitimate interest)

Requirements:
✓ Must have legitimate purpose
✓ Must be proportionate to purpose
✓ Cannot override fundamental rights
✓ Must have appropriate safeguards
✓ Must be transparent (privacy notice required)

Note: Section 7 claims must be documented in "Section 7 
Legitimate Uses Memo" and reviewed by legal counsel.
```

#### Step 3.2: Legal Basis Assessment Matrix

**For each activity, document:**

| Activity | Purpose | Claimed Basis | Justification | Legal Review |
|----------|---------|---------------|---------------|--------------|
| Customer KYC | Regulatory compliance | Section 7 | RBI AML requirement, mandatory by law | Approved 2026-04-10 |
| Marketing Email | Lead nurturing | Section 6 | Non-essential, opt-in consent available | Pending review |
| Website Analytics | Performance metrics | Section 6? | Need to clarify if Section 6 applies to analytics | Review needed |
| Employee Payroll | Salary processing | Section 7 | Employment contract, statutory tax reporting | Approved 2026-04-08 |

**Decision Tree:**

```
Does the activity involve:
│
├─ Regulatory/statutory requirement? (RBI, SEBI, PMLA, GST, Labor law)
│  └─→ Section 7 (Legitimate Use)
│
├─ Marketing or promotional purpose?
│  └─→ Section 6 (Consent Required)
│
├─ Non-essential personalization/behavioral profiling?
│  └─→ Section 6 (Consent Required)
│
├─ Automated decision-making (credit, employment, insurance)?
│  └─→ May be Section 7 for credit (check Section 7(2))
│  └─→ Always Section 6 for other automated decisions
│
├─ Cross-border transfer to non-whitelisted country?
│  └─→ Section 6 (Consent Required)
│
├─ Core service delivery (required for service)?
│  └─→ Could be Section 7 if unavoidable for core service
│
└─ Fraud detection / security / debt recovery?
   └─→ Section 7 (Legitimate Use)
```

#### Step 3.3: Risk Level Classification

**Assign Risk Level for each activity:**

| Risk Level | Criteria | Examples | DPIA Required? |
|-----------|----------|----------|-----------------|
| **Critical** | Biometric data + automated decisions + cross-border | Aadhaar-based credit scoring + transfer to US | **YES** |
| **High** | Sensitive data OR large-scale processing OR high-impact decisions | KYC with Aadhaar, Health data, 50K+ principals | **YES** |
| **Medium** | Regular personal data + standard processing + limited sharing | Email marketing to 10K customers, standard loan processing | **Maybe** |
| **Low** | Non-sensitive data OR limited scope OR internal use only | Anonymous analytics, internal logs, non-identifiable data | **No** |

**Sensitivity Checklist:**

```
Data is SENSITIVE if it includes:
☐ Biometric data (Aadhaar, fingerprints, facial recognition)
☐ Health data (medical records, fitness data)
☐ Genetic data
☐ Racial/ethnic origin
☐ Religious beliefs or affiliations
☐ Sexual orientation or gender identity
☐ Precise location data
☐ Financial data (bank account, credit score, income)
☐ Criminal conviction records
☐ Children's data (under 18)

Processing is HIGH-RISK if:
☐ Automated decision-making (especially credit, employment, insurance)
☐ Systematic monitoring (surveillance, profiling)
☐ Large-scale processing (100K+ data principals)
☐ Processing of vulnerable groups (children, elderly, low-income)
☐ Involves cross-border transfer
☐ Data that could cause significant harm if breached
```

#### Step 3.4: Retention Period Justification

**For each activity, determine:**

```
Question 1: Is there a statutory/regulatory hold?
├─ YES → Apply the longer of statutory hold OR business need
│   ├─ RBI: 8 years (banking records, loans, AML)
│   ├─ PMLA: 5 years (suspicious transaction reports)
│   ├─ GST: 6 years (billing records)
│   ├─ Labor Law: 2-3 years (employment records)
│   └─ CERT-In: 180 days (cybersecurity logs)
│
└─ NO → Determine based on business need
    ├─ Lead nurturing: 2 years
    ├─ Customer support records: 3 years
    ├─ Analytics: 1 year
    ├─ Email/marketing: 2 years or until withdrawal
    ├─ System logs: 90 days
    └─ Backup/disaster recovery: Business continuity period

Question 2: What's the legitimate purpose for retention?
├─ Dispute resolution (how long until disputes resolved?)
├─ Legal claim defense (statute of limitations?)
├─ Regulatory compliance (which regulation + how long?)
├─ Operational necessity (backup, recovery?)
└─ Business continuity (system modernization plans?)

Question 3: How will data be deleted?
├─ Secure deletion (cryptographic erasure)
├─ Anonymization (irreversible)
├─ Pseudonymization (can be reversed)
└─ Archival (move to cold storage, then delete)
```

**Create Retention Schedule:**

| Activity | Data Category | Retention Period | Justification | Deletion Method | Responsible Owner |
|----------|---------------|------------------|----------------|-----------------|-------------------|
| Customer KYC | Aadhaar, PAN, Address | 8 years | RBI requirement for loan records | Secure overwrite + paper shred | Finance Lead |
| Marketing Email | Email, Behavior | 2 years or withdrawal | Lead nurturing window | Database delete + backup purge | Marketing Lead |
| Website Analytics | IP, Device ID | 90 days | Analytics processing window | Log rotation + aggregate | IT Lead |
| Employee Payroll | SSN, Bank Account | 7 years | Statutory hold + dispute resolution | Secure deletion + paper shred | HR Lead |

#### Week 3 Deliverable: Legal & Risk Assessment

**Output:**
- Legal basis matrix (all activities classified as Section 6 or 7)
- Risk levels assigned (Critical/High/Medium/Low)
- Retention periods justified with legal basis
- DPIA screening (which activities need DPIA in Phase 4)
- DPO preliminary notes on gaps

**Sign-off:** Legal counsel reviews Section 7 claims

---

## ROPA Spreadsheet Creation

### Week 4: Compile & Finalize ROPA Spreadsheet

**Goal:** Create the official ROPA Spreadsheet with all mandatory fields

#### Step 4.1: ROPA Mandatory Fields

**Create Excel/Google Sheets with these columns:**

| # | Field Name | Description | Example | Mandatory? |
|---|-----------|-------------|---------|-----------|
| A | Activity ID | Unique identifier | ROPA-001 | ✓ |
| B | Activity Name | Short name of processing activity | Customer KYC Processing | ✓ |
| C | Activity Description | Detailed description of what's processed | Collect and verify customer identity via Aadhaar matching for loan approval | ✓ |
| D | System Name | Which system holds/processes the data | Salesforce CRM + custom KYC service | ✓ |
| E | Department/Owner | Which department owns this activity | Finance | ✓ |
| F | Processing Purpose | Why is this data processed? | AML compliance and KYC regulatory requirement | ✓ |
| G | Legal Basis | Section 6 (Consent) or Section 7 (Legitimate Use) | Section 7 | ✓ |
| H | Legal Basis Justification | Explain why this legal basis applies | RBI mandatory requirement for loan origination | ✓ |
| I | Data Categories | Types of personal data processed | Aadhaar number, PAN, name, address, phone, DOB | ✓ |
| J | Data Principal Categories | Who is the data about? | Loan applicants, customers | ✓ |
| K | # of Data Principals | Approximate number of individuals | ~50,000 active customers | ✓ |
| L | Third-Party Recipients | External parties who receive the data | RBI (regulatory reporting), internal Finance team | ✓ |
| M | Cross-Border Transfers | Are transfers outside India? If yes, to where? | No | ✓ |
| N | Retention Period | How long is data kept? | 8 years | ✓ |
| O | Retention Days | Same as above, in numeric days | 2920 | ✓ |
| R | Retention Legal Basis | Why this retention period? | RBI requirement for loan records | ✓ |
| Q | Deletion Method | How is data deleted after retention expires? | Secure overwrite (AES-256), physical documents shredded | ✓ |
| R | Data Protection Measures | Security controls for this data | Encryption at rest (AES-256), TLS in transit, access logs, pseudonymization for analytics | ✓ |
| S | Risk Level | High / Medium / Low | High | ✓ |
| T | Involves Automated Decision-Making? | Yes/No (e.g., credit scoring) | Yes | ✓ |
| U | Involves Children's Data? | Yes/No | No | ✓ |
| V | Involves Sensitive Data? | Yes/No (biometric, health, etc.) | Yes (Aadhaar) | ✓ |
| W | Compliance Status | Draft / Pending DPIA / Approved | Pending DPIA | ✓ |
| X | DPIA Required? | Yes/No (determined from risk level) | Yes | ✓ |
| Y | Linked Purpose ID | Link to consent purpose (if applicable) | — (N/A - Section 7) | ✗ |
| Z | DPO Review Status | Pending / Reviewed / Approved | Reviewed | ✓ |
| AA | DPO Review Notes | Any gaps or concerns raised | Requires annual audit for RBI compliance | ✗ |
| AB | Approved By | Who approved this activity? | DPO + Legal Counsel | ✓ |
| AC | Approval Date | When was it approved? | 2026-04-20 | ✓ |
| AD | Last Updated | When was this ROPA entry last modified? | 2026-04-20 | ✓ |
| AE | Additional Notes | Any context or caveats | Legacy system, migration planned for 2027 | ✗ |

#### Step 4.2: ROPA Spreadsheet Template

**Download/Create file:** `ROPA_Phase1_Draft_[OrgName]_[Date].xlsx`

**Tabs:**
1. **ROPA Master List** — All activities with mandatory fields
2. **Data Categories Reference** — Legend of data types
3. **Legal Basis Guide** — Section 6 vs 7 decision matrix
4. **Risk Levels** — Classification criteria
5. **Summary Dashboard** — Statistics & compliance overview

#### Step 4.3: Sample ROPA Entries

**Example 1: Regulatory Activity (Section 7)**

```
Activity ID: ROPA-001
Activity Name: Customer KYC Processing
Activity Description: Collection and verification of customer 
  identity documents (Aadhaar, PAN) for loan application approval 
  and regulatory compliance

System Name: Salesforce CRM + Custom KYC Verification Service
Department/Owner: Finance (Head of Credit)
Processing Purpose: AML compliance and KYC regulatory requirement 
  for loan origination
Legal Basis: Section 7 (Legitimate Use)
Legal Basis Justification: RBI mandatory requirement for all 
  NBFC loan origination; statutory obligation under Prevention 
  of Money Laundering Act (PMLA)

Data Categories: 
  - Identity: Aadhaar number, PAN, Full name
  - Contact: Address, Phone number, Email
  - Financial: Monthly income, Bank account details
  - Document images: Aadhaar scan, PAN scan, address proof

Data Principal Categories: Loan applicants, customers
# of Data Principals: ~50,000 active customers

Third-Party Recipients: 
  - Internal: Finance team, Risk team, Admin staff
  - External: RBI (regulatory reports), Government agencies

Cross-Border Transfers: No

Retention Period: 8 years
Retention Days: 2920
Retention Legal Basis: RBI requirement for loan records; 
  PMLA requirement for AML documentation; potential legal 
  disputes/claims (7-year statute of limitations)

Deletion Method: Secure cryptographic erasure using AES-256; 
  physical documents shredded using certified shredding service

Data Protection Measures: 
  - Encryption at rest: AES-256-GCM
  - Encryption in transit: TLS 1.2+
  - Access control: Role-based access (RBAC), MFA
  - Audit logging: All access logged and monitored
  - Anonymization: PII redacted in analytics/reports
  - Physical security: Locked filing cabinets for documents

Risk Level: High
Involves Automated Decision-Making? Yes (credit scoring)
Involves Children's Data? No
Involves Sensitive Data? Yes (biometric - Aadhaar)

Compliance Status: Pending DPIA
DPIA Required? Yes (automated decision-making + biometric)
Linked Purpose ID: N/A (Section 7 - no consent needed)

DPO Review Status: Reviewed
DPO Review Notes: Requires annual compliance audit for RBI 
  alignment; DPIA to be completed by end of May 2026
Approved By: Chief Data Protection Officer
Approval Date: 2026-04-20
Last Updated: 2026-04-20

Additional Notes: Legacy system (Salesforce) scheduled for 
  migration to proprietary platform in 2027. Cross-border 
  expansion planned for Q4 2026 (will require transfer agreements).
```

**Example 2: Marketing Activity (Section 6)**

```
Activity ID: ROPA-002
Activity Name: Marketing Email Campaigns
Activity Description: Collection of email addresses and behavioral 
  data (website visits, product interests, purchase history) for 
  targeted promotional campaigns and product recommendations

System Name: Email Marketing Platform (Mailchimp) + Website Analytics
Department/Owner: Sales & Marketing (CMO)
Processing Purpose: Lead nurturing, promotional offers, product 
  recommendations, customer retention
Legal Basis: Section 6 (Consent - FSIUU compliant)
Legal Basis Justification: Non-essential processing; user can 
  opt-out without impacting core service; requires affirmative 
  consent via checkbox; withdrawal available at any time

Data Categories:
  - Contact: Email address
  - Behavioral: Website visits, product views, purchase history
  - Preferences: Category interests, communication frequency

Data Principal Categories: Website visitors, prospects, customers
# of Data Principals: ~200,000 contacts in email list

Third-Party Recipients: 
  - Internal: Marketing team, Sales team
  - External: Email service provider (Mailchimp - has DPA)

Cross-Border Transfers: Yes (Mailchimp servers in US)

Retention Period: 2 years or until withdrawal
Retention Days: 730 (or upon withdrawal)
Retention Legal Basis: Lead nurturing window (2 years typical 
  for sales cycle); FSIUU requirement to honor withdrawal immediately

Deletion Method: Immediate deletion from Mailchimp upon withdrawal 
  request; automatic deletion after 2 years of inactivity

Data Protection Measures:
  - Encryption in transit: TLS 1.2+
  - DPA with vendor: Signed on 2026-01-15
  - Anonymization: IP addresses anonymized after 90 days
  - Consent audit: All consent events logged with timestamp
  - Withdrawal mechanism: One-click unsubscribe link

Risk Level: Low
Involves Automated Decision-Making? No
Involves Children's Data? No
Involves Sensitive Data? No

Compliance Status: Approved
DPIA Required? No
Linked Purpose ID: PURPOSE-MARKETING-001

DPO Review Status: Approved
DPO Review Notes: Consent mechanism compliant with FSIUU; 
  withdrawal tested and working; consider implementing 
  preference center for better granularity
Approved By: Chief Data Protection Officer + Legal Counsel
Approval Date: 2026-04-15
Last Updated: 2026-04-20

Additional Notes: Cross-border transfer to Mailchimp (US) 
  requires formal transfer agreement; currently covered by 
  Mailchimp's standard DPA
```

**Example 3: Employee Data (Section 7)**

```
Activity ID: ROPA-003
Activity Name: Employee Payroll & Compensation Processing
Activity Description: Collection and processing of employee 
  personal data (SSN, bank account, tax information) for salary 
  processing, statutory tax compliance, and benefits administration

System Name: HR System (BambooHR) + Payroll Provider (ADP)
Department/Owner: HR & Payroll
Processing Purpose: Salary payment, tax compliance (IT, PF, ESI), 
  benefits administration, statutory reporting
Legal Basis: Section 7 (Legitimate Use)
Legal Basis Justification: Contractual obligation (employment 
  contract); statutory requirement (tax law, labor law); cannot 
  process payroll without this data

Data Categories:
  - Identity: Full name, SSN
  - Financial: Bank account number, salary, deductions
  - Tax: PAN, tax bracket, withholding information
  - Benefits: Health insurance elections, emergency contacts

Data Principal Categories: Current employees, contractors
# of Data Principals: ~500 employees

Third-Party Recipients:
  - Internal: Finance, HR, Department heads
  - External: Bank (salary disbursement), Government (tax filings), 
    Benefits providers, Payroll provider (ADP)

Cross-Border Transfers: No

Retention Period: 7 years
Retention Days: 2555
Retention Legal Basis: Statutory requirement (Indian tax law); 
  potential disputes (statute of limitations)

Deletion Method: Secure deletion from active systems after 7 years; 
  archived copies anonymized and retained for 3 additional years 
  (10 years total) for audit compliance

Data Protection Measures:
  - Encryption at rest: AES-256-GCM
  - Encryption in transit: TLS 1.2+
  - Access control: Only HR & Finance team (min. privilege)
  - Audit logging: All access logged
  - Physical security: Locked office access
  - Data minimization: Only required fields collected

Risk Level: Medium
Involves Automated Decision-Making? No
Involves Children's Data? No
Involves Sensitive Data? No (financial data only, not highly sensitive)

Compliance Status: Approved
DPIA Required? No
Linked Purpose ID: N/A (Section 7)

DPO Review Status: Approved
DPO Review Notes: Standard HR processing; ensure employees 
  informed via privacy notice at hiring
Approved By: Chief Data Protection Officer
Approval Date: 2026-04-15
Last Updated: 2026-04-20

Additional Notes: Current provider (ADP) has DPA in place; 
  consider annual review of payroll provider contracts
```

#### Step 4.4: ROPA Compilation Checklist

Before finalizing, verify:

```
□ All activities from Week 2 list are included
□ Every activity has a unique ID (ROPA-001, ROPA-002, etc.)
□ All mandatory fields are populated
□ Data categories are specific (not just "personal data")
□ Legal basis is clearly justified
□ Retention periods have documented justification
□ Risk levels are assigned correctly
□ DPIA screening completed
□ All third-party recipients identified
□ DPA status checked for external processors
□ Encryption/security measures documented
□ Deletion methods are clear and executable
□ DPO has reviewed all entries
□ No conflicting retention periods
□ Cross-border transfers are flagged
□ Automated decision-making is flagged
□ Children's data is flagged
□ Sensitive data is flagged
□ Approval dates are completed
□ Notes section explains any non-standard entries
```

#### Week 4 Deliverable: ROPA Spreadsheet (Draft)

**Final Output File:**
```
ROPA_Phase1_Draft_[OrgName]_[YYYY-MM-DD].xlsx
│
├── Tab 1: ROPA Master List
│   └── All activities with mandatory & optional fields
│
├── Tab 2: Summary Dashboard
│   ├── Total activities: XX
│   ├── By legal basis: Section 6 (XX), Section 7 (XX)
│   ├── By risk level: Critical (X), High (X), Medium (X), Low (X)
│   ├── Requiring DPIA: XX
│   ├── Cross-border transfers: XX
│   ├── Automated decision-making: XX
│   └── DPO approval status: XX approved, XX pending review
│
├── Tab 3: Data Categories Reference
│   ├── Identity data: Aadhaar, PAN, SSN, Passport, etc.
│   ├── Contact data: Email, phone, address
│   ├── Financial data: Income, bank account, credit score
│   ├── Health data: Medical records, fitness data
│   ├── Behavioral data: Purchase history, website visits
│   └── System data: IP address, device ID, logs
│
├── Tab 4: Legal Basis Guide
│   ├── Section 6 criteria
│   ├── Section 7 criteria
│   └── Decision matrix with examples
│
└── Tab 5: Risk Assessment Matrix
    ├── Risk level criteria
    ├── Examples by level
    └── DPIA screening criteria
```

---

## Templates & Tools

### Template 1: Stakeholder Interview Guide

**File:** `ROPA_Phase1_Interview_Template.docx`

Use for consistent interviews across departments.

```markdown
## Data Processing Interview Form

**Department:** _______________________
**Interviewee:** _______________________
**Date:** _______________________
**Duration:** _______________________

### Section A: Department Overview
1. What's your role and responsibilities?
2. What systems/applications does your team use daily?
3. How many team members access these systems?

### Section B: Data Inventory
1. What types of personal data does your team collect?
   ☐ Identity (name, ID numbers)
   ☐ Contact (email, phone, address)
   ☐ Financial (income, accounts, credit)
   ☐ Health data
   ☐ Behavioral (purchases, browsing)
   ☐ System logs (IP, device ID)
   ☐ Other: ________

2. Where is this data stored?
   ☐ On-premise database
   ☐ Cloud storage
   ☐ SaaS platform (which one? _________)
   ☐ Email/documents
   ☐ Excel spreadsheets
   ☐ Other: ________

3. How much data? (Approximate records/contacts)
   _______________________

### Section C: Processing Activities
1. What are the main processing activities in your department?
   Activity 1: ________________
   Activity 2: ________________
   Activity 3: ________________

2. For each activity, explain:
   - What data is processed?
   - Why is it processed?
   - Who accesses it?
   - How long is it kept?
   - Who receives it externally?

### Section D: Legal Basis
1. Do you have consent forms for this data?
   ☐ Yes (please share)
   ☐ No

2. Is this processing required by regulation?
   ☐ RBI / SEBI / PMLA / GST / Labor Law / Other
   ☐ No regulatory requirement

3. Do you process on behalf of another entity?
   ☐ Yes (we're a data processor)
   ☐ No

### Section E: Data Sharing & Recipients
1. Who in the organization accesses this data?
   _______________________

2. Who externally receives this data?
   - Third-party vendors? (which ones?)
   - Government agencies? (RBI, Tax, Police?)
   - Partners/affiliates?

3. Do you have DPAs (contracts) with external parties?
   ☐ Yes (please share)
   ☐ No (need to create)

### Section F: Retention & Deletion
1. How long do you keep this data?
   _______________________

2. Why this retention period?
   ☐ Business need (explain: _________)
   ☐ Regulatory requirement (which one? _________)
   ☐ Not sure

3. How is data deleted?
   ☐ Database deletion
   ☐ Secure overwrite
   ☐ Physical shredding (documents)
   ☐ Archive & then delete
   ☐ Not sure

4. Are there any legal holds (must keep beyond normal retention)?
   ☐ Yes (explain: _________)
   ☐ No

### Section G: Risk & Compliance
1. Does your team process sensitive data?
   ☐ Biometric (Aadhaar, fingerprints)
   ☐ Health information
   ☐ Financial (bank account, credit)
   ☐ Children's data
   ☐ No sensitive data

2. Do you make automated decisions?
   ☐ Credit scoring
   ☐ Employment decisions
   ☐ Insurance decisions
   ☐ Other: ________
   ☐ No automated decisions

3. Do you transfer data outside India?
   ☐ Yes (to which countries? _________)
   ☐ No

4. Have there been any data breaches or incidents?
   ☐ Yes (describe: _________)
   ☐ No

### Section H: Documentation
1. Do you have current privacy notices?
   ☐ Yes (please share)
   ☐ No (outdated / missing)

2. Do you have data retention policies?
   ☐ Yes (please share)
   ☐ No

3. Do you have vendor/processor agreements?
   ☐ Yes (please share)
   ☐ No

### Section I: Compliance Gaps & Suggestions
1. What compliance challenges do you see?
   _______________________

2. What would you improve if you could?
   _______________________

3. Do you have any questions about DPDP?
   _______________________

**Interviewer Notes:**
_______________________
_______________________

**Follow-up Actions:**
☐ Collect documents (consent forms, policies, contracts)
☐ Schedule technical audit (database schema)
☐ Schedule follow-up interview
☐ Escalate to legal counsel
☐ Other: ________

```

### Template 2: Systems Inventory Spreadsheet

**File:** `ROPA_Phase1_Systems_Inventory.xlsx`

| System ID | System Name | Type | Owner | Data Sensitivity | Key Data Types | Location | # Users | DPA Needed? | Notes |
|-----------|------------|------|-------|-----------------|----------------|----------|---------|-----------|-------|
| SYS-001 | Salesforce CRM | Cloud App | VP Sales | Medium | Email, phone, behavioral | US Cloud | 25 | Yes | Need vendor DPA |
| SYS-002 | HR Platform | Cloud App | HR Manager | High | SSN, bank account | US Cloud | 10 | Yes | Payroll data |
| SYS-003 | PostgreSQL Customer DB | Database | DBA | Medium | Email, phone, purchase history | AWS ap-south-1 | 5 | No | On-premise backup |

### Template 3: Processing Activities Matrix

**File:** `ROPA_Phase1_Processing_Activities.xlsx`

Use for Week 2 discovery.

| Activity ID | Activity Name | Department | System | Data Types | Purpose | Legal Basis (Preliminary) | High-Risk? | Requires DPIA? | Notes |
|-------------|--------------|-----------|--------|-----------|---------|------------------------|-----------|-----------------|-------|

### Template 4: Legal Basis Decision Tree

**File:** `ROPA_Phase1_Legal_Basis_Guide.docx`

Visual decision tree for classifying Section 6 vs Section 7.

### Template 5: Risk Assessment Checklist

**File:** `ROPA_Phase1_Risk_Assessment.docx`

Checklist for determining risk level and DPIA requirement.

---

## Common Mistakes & Solutions

### Mistake 1: Treating All Data as "Personal Data"

**Problem:** Over-documenting non-sensitive data (employee ID numbers, product SKUs)

**Solution:**
```
Personal Data = Any data that can identify an individual, directly or indirectly

Personal Data:
✓ Name + any identifier (email, phone, address)
✓ Aadhaar, PAN, SSN
✓ IP address + timestamp (links to individual)
✓ Device ID + cookie (can track individual)

NOT Personal Data:
✗ Anonymous aggregated data ("500 users visited page X")
✗ Truly anonymized data (irreversibly de-identified)
✗ Non-identifiable business data (product SKU, transaction amounts without customer link)
✗ Public data (published information)

Be Specific: Instead of "customer data", list actual data types:
✓ Customer email addresses (yes - personal data)
✓ Customer IDs (only if linked to personal info)
✓ Product purchase amounts (only if linked to customer identity)
```

### Mistake 2: Confusing "Data Types" with "Data Categories"

**Problem:** Listing fields instead of categorizing them

```
WRONG:
Data Types: email, phone, address, name, bank_account, aadhaar_number

CORRECT:
Data Categories:
- Identity: Full name, Aadhaar number, PAN
- Contact: Email address, Phone number, Physical address
- Financial: Bank account number, Monthly income
```

### Mistake 3: Defaulting All Activities to Section 6

**Problem:** Assuming everything needs consent when Section 7 applies

**Solution:**
```
Reality Check: Most FinTech/NBFC processing is Section 7
- KYC: Section 7 (regulatory)
- AML: Section 7 (regulatory)
- Credit scoring: Section 7 (legitimate business + contractual)
- Fraud detection: Section 7 (legitimate business)
- Loan servicing: Section 7 (contractual)

Only these typically need Section 6:
- Marketing emails
- Behavioral analytics (non-essential)
- Preference tracking
- Product recommendations (optional)

Escalate to legal counsel if unsure!
```

### Mistake 4: Retention Period Confusion

**Problem:** Setting retention periods without legal justification

```
WRONG:
"We keep customer data for 2 years"
(Why? No documented reason)

CORRECT:
"We keep KYC data for 8 years per RBI requirement;
customer contact data for 2 years for support history;
analytics data for 90 days for performance metrics"

Remember: Different data categories may have different retention periods!
```

### Mistake 5: Missing Cross-Border Transfers

**Problem:** Forgetting that SaaS = cross-border

```
Common Cross-Border Scenarios:
✓ Salesforce CRM (US servers) = cross-border
✓ Google Analytics (multiple countries) = cross-border
✓ AWS (configurable regions, often US) = cross-border
✓ Slack, Microsoft Teams, Google Workspace = cross-border
✓ Stripe, Razorpay (US/India but cloud) = cross-border

Each requires:
- Documentation that country is on RBI whitelist
- OR consent from data principal (Section 6)
- OR DPA with processor (Section 8(2))
```

### Mistake 6: Incomplete Risk Assessment

**Problem:** Marking everything as "Medium" risk

```
Actually HIGH-RISK if ANY of these are true:
✓ Biometric data (Aadhaar, fingerprints)
✓ Health data
✓ Automated decision-making (credit, employment)
✓ Processing of vulnerable groups (children)
✓ Large-scale processing (50K+ principals)
✓ Data that determines eligibility for benefits/services
✓ Systematic monitoring/profiling

Actually LOW-RISK if ALL of these are true:
✓ Non-sensitive data (name, email, phone)
✓ Limited processing (internal use only)
✓ No automated decisions
✓ Limited recipients (< 5 internal teams)
✓ Short retention (< 1 year)
✓ Standard security measures (encryption, access logs)
```

### Mistake 7: Forgetting DPA Requirements

**Problem:** Processing data with third parties but no contracts

```
Third-Party Data Processor = Anyone who processes data ON BEHALF of your org

Requires:
✓ Data Processing Agreement (DPA) - Section 8(2) mandatory
✓ Processor approved in writing (written mandate)
✓ Processor must follow instructions
✓ Processor responsible for security
✓ Sub-processor notification required

Examples of processors:
✓ Payroll provider (processes employee data)
✓ Email service (processes customer emails)
✓ Cloud storage (hosts your databases)
✓ Analytics service (processes behavioral data)
✓ Backup provider (stores your data)

Examples NOT processors (joint controllers):
✗ RBI (when you report regulatory data)
✗ Banks (when customer transfers money)
✗ Government agencies (when they request data)
```

### Mistake 8: Vague Security Descriptions

**Problem:** "Data is encrypted" without specifying what that means

```
WRONG:
"Security Measures: Encryption"

CORRECT:
"Security Measures: 
- Encryption at rest: AES-256-GCM
- Encryption in transit: TLS 1.2+
- Access control: Role-based (RBAC), MFA required
- Audit logging: All access logged, monitored for anomalies
- Anonymization: PII redacted in analytics/reports
- Physical security: Locked server rooms, biometric access
- Backup encryption: Separate encryption key
- Deletion method: Secure cryptographic erasure"
```

### Mistake 9: No Approval Trail

**Problem:** ROPA entries not formally approved by DPO

```
Each entry must have:
✓ DPO review completed (date)
✓ DPO approval or notes on gaps (comments)
✓ Legal counsel sign-off (if Section 7)
✓ Approval date documented
✓ Approver name recorded
✓ Version history tracked

Without this, ROPA is not compliance evidence!
```

### Mistake 10: Static ROPA (Never Updated)

**Problem:** ROPA created in Phase 1, never updated again

```
ROPA is a LIVING DOCUMENT

Update ROPA when:
✓ New system introduced
✓ Processing purpose changes
✓ Data retention policy changes
✓ Security measures updated
✓ Legal basis questioned
✓ DPIA completed
✓ New third-party added
✓ Regulatory requirements change

Frequency: At minimum, annual review by DPO
Review trigger: Any material change to processing
```

---

## DPO Review & Sign-Off

### Final DPO Review (Week 4, Day 5)

**DPO Checklist:**

```
COMPLETENESS
☐ All systems with personal data are documented?
☐ All processing activities are documented?
☐ No obvious gaps?
☐ Data types are accurately described?
☐ All mandatory fields populated?

LEGAL BASIS
☐ Section 6 activities have documented consent mechanisms?
☐ Section 7 activities have legitimate use justifications?
☐ Legal basis determinations are reasonable?
☐ Any questionable determinations flagged for legal review?

RISK ASSESSMENT
☐ High-risk activities identified (biometric, automated decisions)?
☐ DPIA screening accurately completed?
☐ Risk levels are defensible?
☐ Any critical-risk items noted for urgent Phase 4 action?

RETENTION & DELETION
☐ Retention periods are justified?
☐ Statutory holds are identified?
☐ Deletion methods are practical?
☐ No retention periods that violate DPDP?

THIRD PARTIES & SECURITY
☐ All third-party recipients documented?
☐ DPA status checked (gap identified for Phase 2)?
☐ Security measures described sufficiently?
☐ Cross-border transfers flagged?

COMPLIANCE GAPS
☐ Gap register created?
☐ Gaps prioritized for Phases 2-5?
☐ No critical gaps missed?

GOVERNANCE
☐ Approval dates recorded?
☐ Approver names documented?
☐ Version control established?
☐ Future review schedule set (annual minimum)?
```

**DPO Sign-Off Statement:**

```markdown
## PHASE 1 COMPLETION SIGN-OFF

I, [DPO Name], have reviewed the ROPA Spreadsheet dated [Date] 
for [Organization Name].

### Assessment:

✓ Baseline data processing inventory is complete and accurate
✓ Legal basis determinations are sound
✓ Risk assessments are reasonable
✓ Retention periods are justified
✓ Security measures are documented
✓ Third-party processing is identified
✓ Compliance gaps are identified and prioritized

### Identified Gaps for Remediation:

[List of gaps for Phases 2-5]

### Immediate Actions Required:

[Any critical issues requiring immediate attention]

### Conclusion:

The organization's data processing activities have been documented 
in the ROPA Spreadsheet (Draft). The baseline is established and 
data flows are accurately captured. The organization is ready to 
proceed to Phase 2 (Gap Analysis).

---
**Signed:** [DPO Signature]
**Date:** [Date]
**Title:** Chief Data Protection Officer
```

---

## Success Criteria

### Phase 1 Completion Checklist

```
ROPA SPREADSHEET
☑ All processing activities documented (15-40+ entries)
☑ Every activity has unique ID (ROPA-001, etc.)
☑ All mandatory fields populated
☑ Data categories are specific and accurate
☑ Legal basis determined for each activity
☑ Retention periods justified
☑ Risk levels assigned
☑ DPIA screening completed
☑ Third-party recipients identified
☑ Security measures described
☑ DPO has reviewed
☑ DPO has approved

SYSTEMS INVENTORY
☑ All databases cataloged
☑ All applications cataloged
☑ All cloud services documented
☑ Data flow diagrams created
☑ Access control summary prepared

COMPLIANCE GAPS
☑ High-risk activities requiring DPIA identified
☑ Missing consent mechanisms flagged
☑ Retention policy gaps identified
☑ Third-party DPA gaps identified
☑ Cross-border transfer issues flagged
☑ Automated decision-making flagged
☑ Children's data flagged
☑ Gaps prioritized for Phases 2-5

GOVERNANCE
☑ DPO sign-off obtained
☑ Approval dates documented
☑ Approver names recorded
☑ Version control established
☑ Future review schedule set

TEAM ALIGNMENT
☑ Stakeholders confirmed accuracy of their activities
☑ Legal counsel reviewed Section 7 claims
☑ IT confirmed system descriptions
☑ No stakeholder disagreements unresolved
```

### Expected Metrics

```
Typical Phase 1 Results:

Organizations: 15-40 processing activities documented
Data Categories: 5-15 different types across all activities
Legal Basis Split: ~60% Section 7, ~40% Section 6 (for fintech)
Risk Distribution: 10% Critical, 30% High, 40% Medium, 20% Low
DPIA Required: 20-30% of activities
Cross-Border: 5-10% of activities (SaaS, cloud services)
Third Parties: 10-20 vendor relationships identified
DPA Gap: 30-50% need DPA creation (Phase 2 action)
Retention Issues: 15-25% need policy refinement (Phase 2 action)
```

### Phase 1 Deliverables Summary

**Output Files:**

```
1. ROPA_Phase1_Draft_[OrgName]_[Date].xlsx
   ├── Master ROPA list with all activities
   ├── Summary dashboard with statistics
   ├── Data categories reference
   ├── Legal basis guide
   └── Risk assessment matrix

2. Systems_Inventory_Phase1_[OrgName]_[Date].xlsx
   ├── Complete systems catalog
   ├── Database schema summary
   ├── Cloud services audit
   └── Integration map

3. Compliance_Gaps_Register_Phase1_[OrgName]_[Date].xlsx
   ├── DPIA requirements (Phase 4)
   ├── Consent mechanism gaps (Phase 3)
   ├── Retention policy gaps (Phase 2)
   ├── DPA gaps (Phase 2)
   └── Priority matrix

4. DPO_Sign_Off_Phase1_[OrgName]_[Date].pdf
   └── Formal approval and gap summary

5. Meeting_Minutes_Phase1_Stakeholder_Interviews.docx
   └── Notes from all department interviews
```

### Next Steps: Transition to Phase 2

**At the end of Phase 1, you have:**
- ✅ Complete baseline of data processing
- ✅ Documented legal basis
- ✅ Risk assessment
- ✅ Identified compliance gaps
- ✅ DPO approval

**Phase 2 (Weeks 5-8) will:**
1. Score each gap across 17 compliance domains
2. Create remediation roadmap
3. Prioritize gaps (Critical → High → Medium → Low)
4. Estimate effort and timeline for Phases 3-5

---

## Appendix: Quick Reference Guides

### Appendix A: Data Categories Reference

```
IDENTITY DATA
- Full name, nickname
- ID numbers: Aadhaar, PAN, SSN, Passport, Voter ID, Driver's License
- Biometric data: Fingerprints, facial recognition, iris scan
- Signature

CONTACT DATA
- Email address
- Phone number (mobile, landline)
- Physical address (residential, business)
- Social media handles
- Contact person information

FINANCIAL DATA
- Bank account number and details
- Credit/debit card information
- Payment history and transaction records
- Income and salary information
- Loan and credit information
- Insurance information
- Investment portfolio
- Tax information (IT returns, GST)

EMPLOYMENT DATA
- Job title and employment history
- Skills and qualifications
- Performance reviews
- Salary and benefits
- Employment contract
- Background check results
- Work schedule and time tracking

HEALTH DATA
- Medical history and records
- Medication information
- Fitness and wellness data
- Health insurance information
- Mental health information
- Genetic data
- Biometric health measurements (heart rate, blood pressure)

BEHAVIORAL DATA
- Website browsing history
- Purchase history and preferences
- Search queries
- Product/service interactions
- Content preferences
- Location data (GPS, geolocation)
- Device usage patterns
- Social interactions and communications

FAMILY & RELATIONSHIP DATA
- Marital status
- Children information
- Family member details
- Guardian information
- Emergency contact information

EDUCATION DATA
- School/university attended
- Degree and qualifications
- Academic performance
- Certifications
- Training records

LEGAL & ADMINISTRATIVE DATA
- Court orders and legal proceedings
- Police records
- Regulatory compliance information
- Government benefits received
- Licenses and permits
- Citizenship and immigration status

SENSITIVE CATEGORIES (DPDP Definition)
- Biometric data (Aadhaar, fingerprints, etc.)
- Health data
- Genetic data
- Racial/ethnic origin
- Religious beliefs
- Sexual orientation
- Gender identity
- Caste information
```

### Appendix B: Section 6 vs Section 7 Quick Reference

| Aspect | Section 6 (Consent) | Section 7 (Legitimate Use) |
|--------|-------------------|--------------------------|
| **Requirement** | Affirmative consent REQUIRED | NO consent required |
| **Withdrawal** | Easy withdrawal mechanism MUST exist | No withdrawal right |
| **Granularity** | Separate consent per purpose | Can be bundled |
| **Pre-ticked** | NOT allowed | N/A |
| **Intermediary** | NOT allowed (must be from individual) | N/A |
| **What Qualifies** | Marketing, non-essential data, analytics | KYC, fraud detection, regulatory, employment |
| **Fintech Examples** | Email marketing, behavioral ads, preference tracking | AML/KYC, credit scoring, loan servicing, RBI reporting, fraud detection |
| **Documentation** | Consent form + audit log | Privacy notice + legitimate use justification |
| **Mechanism** | Checkbox, signature, digital record | Contractual obligation, regulatory requirement |
| **Evidence** | Consent records with timestamp | Regulation reference, contractual agreement |

### Appendix C: Risk Level Decision Tree

```
Question 1: Does this involve sensitive data?
├─ YES → Check Question 2
└─ NO → Check Question 3

Question 2: Sensitive Data Present
├─ Biometric (Aadhaar, fingerprints, facial)
├─ Health data
├─ Genetic data
├─ Precise location
└─ Combined with: Automated decision-making?
   ├─ YES → CRITICAL RISK
   └─ NO → HIGH RISK

Question 3: Automated Decision-Making?
├─ YES (Credit scoring, employment decisions, insurance)
│  ├─ Affects eligibility → HIGH/CRITICAL RISK
│  └─ Only informational → MEDIUM RISK
└─ NO → Continue

Question 4: Processing Scale
├─ Large-scale (50K+ data principals) → HIGH RISK
├─ Medium-scale (5K-50K) → MEDIUM RISK
└─ Small-scale (<5K) → MEDIUM/LOW RISK

Question 5: Data Sharing & Cross-Border
├─ Cross-border transfer → Add 1 level of risk
├─ Third-party processor → Add 1 level of risk
└─ Multiple recipients → Add 1 level of risk

Question 6: Retention Period
├─ Long-term (>2 years) → HIGH RISK
├─ Medium-term (1-2 years) → MEDIUM RISK
└─ Short-term (<1 year) → MEDIUM/LOW RISK

FINAL RISK LEVEL:
- Critical: Biometric + automated + cross-border
- High: Sensitive data OR automated decisions OR large-scale
- Medium: Standard personal data + moderate processing
- Low: Non-sensitive + limited scope + internal only
```

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-04-15 | Initial guide created | DPO |
| | | | |

---

## Contact & Questions

**DPO Contact:** [Name]  
**Email:** [Email]  
**Office Hours:** [Times]

For questions about ROPA preparation, please reach out to the Data Protection Office.

---

**Document Classification:** DPDP Compliance (Internal Use)  
**Retention Period:** 3 years or until superseded  
**Last Review Date:** 2026-04-15  
**Next Review Date:** 2026-12-15
