# Phase 0: Scoping — DPDP Applicability & Entity Classification

**Duration:** Weeks -2 to 0 (January 2026) | **Effort:** 1-2 weeks | **Owner:** Legal, CTO | **Templates:** T-01, T-02

---

## Objective

Determine your organization's **DPDP classification** (Data Fiduciary vs Significant Data Fiduciary) and **entity types** before commencing compliance work.

---

## Step 1: DPDP Applicability Test (T-01)

**Question 1:** Does your organization collect, use, store, share, or process any personal data?
- [ ] YES → Continue to Step 2
- [ ] NO → DPDP may not apply (rare for digital businesses)

**Question 2:** Is personal data processed within India or for Indian residents?
- [ ] YES → DPDP applies
- [ ] NO → DPDP may not apply

**Question 3:** Does your organization have a significant presence in India?
- [ ] YES (office, employees, servers, customer base) → DPDP applies
- [ ] NO → DPDP may not apply

---

## Step 2: Data Fiduciary (DF) vs Significant Data Fiduciary (SDF) Classification

### **You are a Data Fiduciary (DF) if:**
- You decide the purpose and means of processing personal data
- You collect consent (Section 6) or rely on legitimate use (Section 7)
- You implement security and breach notification procedures

### **You are a Significant Data Fiduciary (SDF) if you are a DF AND meet ANY:**

| SDF Criterion | Your Organization? |
|---|---|
| **Processing Scale:** Processing personal data of >50 lakh individuals (50 million+) | [ ] YES [ ] NO |
| **Sensitive Data:** Processing special category data at scale (health, biometrics, financial, children) | [ ] YES [ ] NO |
| **High-Risk Processing:** Large-scale automated decision-making, systematic monitoring, cross-border transfers | [ ] YES [ ] NO |
| **Regulatory Dominance:** Financial services (bank, NBFC, insurance), healthcare, telecom, government agency | [ ] YES [ ] NO |
| **Fiduciary Designation:** Government notifies you as SDF in official gazette | [ ] YES [ ] NO |

**If ANY checkbox is YES → You are an SDF**

---

### **SDF Obligations (Additional to DF):**

| Obligation | What's Required |
|---|---|
| **DPO Appointment (Section 10)** | Appoint dedicated Data Protection Officer before Phase 1 |
| **DPIA (Section 10)** | Conduct Data Protection Impact Assessment for high-risk activities |
| **Independent Audit (Section 10)** | Annual independent audit by registered auditor; report to DPBI |
| **Privacy Committee** | Board-level Privacy Committee + quarterly reviews |
| **DPIA Register** | Maintain register of all DPIAs; report to DPBI |

---

## Step 3: Entity Type Classification

Assign your organization to ONE or MORE entity types:

- [ ] **Financial Services** (Bank, NBFC, Fintech, Payment, Insurance) → RBI/SEBI overlay
- [ ] **Healthcare** (Hospital, Clinic, Health Insurance) → Medical Council overlay
- [ ] **Telecom** → TRAI overlay
- [ ] **E-Commerce** → Consumer Protection overlay
- [ ] **Employment/HR** → Labor law overlay
- [ ] **Government/Public** → RTI/IT Act overlay
- [ ] **Other** → General DPDP only

**Why This Matters:** Each sector has regulatory overlays affecting data retention, security standards, and breach notification.

---

## Step 4: Regulatory Conflict Matrix

### **RBI Data Retention Overlay (if Financial Services)**

| Data Type | DPDP Default | RBI Requirement | Applies |
|---|---|---|---|
| KYC records | 6 months (no justification) | 10 years | ✅ RBI wins (10yr mandatory) |
| Transaction logs | 6 months | 8 years | ✅ RBI wins (8yr minimum) |
| Loan documents | 6 months | 8 years post-closure | ✅ RBI wins |
| CCTV/Physical logs | 90 days | 1 year (if investigation) | ⚠️ RBI wins |

**Action:** Use longer retention period per Table above.

---

## Step 5: Deliverables Checklist

- [ ] **Applicability Determination:** DF or SDF classification documented
- [ ] **Entity Type Assignment:** One or more types selected
- [ ] **Regulatory Overlay Matrix:** Identified applicable regulations (RBI, SEBI, etc.)
- [ ] **SDF Obligations List:** If SDF, list all 4 mandatory obligations above
- [ ] **DPO Hiring Plan** (if SDF): Timeline for DPO appointment before Phase 1
- [ ] **Board Sign-Off:** Compliance roadmap approved by Board/CEO

---

## Next Phase: Phase 1 Assessment (Weeks 1-8)

→ [Phase 1: Assessment](./02_PHASE_1_ASSESSMENT.md)

---

**Owner:** Legal | **Board Approval:** [Date/Signature]
