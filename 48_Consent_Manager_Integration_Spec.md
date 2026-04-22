# Consent Manager Integration Specification

**Version:** 1.0  
**Last Updated:** November 14, 2025  
**Effective Date:** November 14, 2026 (government CM registration opens; mandatory integration by May 13, 2027)

---

## Executive Summary

This specification defines the technical and operational requirements for integrating with Government-Approved Consent Managers (CMs) as mandated by DPDP Rules 2025, Section 6(8-9). 

**Key Timeline:**
- **November 14, 2026** — Central Government publishes approved Consent Manager list
- **May 13, 2027** — Compliance deadline: Organizations must be capable of accepting CM-generated consent receipts
- **By May 13, 2027** — All new consent capture (where applicable) should flow through approved CM if organization chooses to use one

---

## 1. WHAT IS A GOVERNMENT-APPROVED CONSENT MANAGER?

### Definition
A Consent Manager (CM) is a third-party platform approved by the Central Government to:
- Capture and record consent from data principals on behalf of organizations (Data Fiduciaries)
- Generate cryptographically signed consent receipts
- Maintain an immutable consent audit trail
- Facilitate consent withdrawal at the principal's request
- Propagate consent decisions across multiple organizations (if principal consents to cross-org sharing)

### Why CMs Matter
- **DPDP Rules 2025** envision CMs as trusted intermediaries for consent capture
- **Benefits:** Standardized format, cross-organization interoperability, reduced DF liability for consent record integrity
- **Government Role:** Central Government maintains registry of approved CMs; DPB can audit CM practices

### Current Status (April 2026)
- Government has NOT yet published the approved CM list
- Expected publication: **November 14, 2026**
- Organizations should prepare integration pipelines now and activate by May 13, 2027

---

## 2. INTEGRATION ARCHITECTURE

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────┐
│  DATA PRINCIPAL (Consent Granter)                           │
│  • Visits organization website or mobile app                │
│  • Clicks "Grant Consent" button                            │
└───────────────────┬─────────────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────────┐
        │ Organization Landing Page │
        │ (Consent UI / Dashboard)  │
        └────────────┬──────────────┘
                     │
        ┌────────────▼─────────────────────────────┐
        │  CM Integration Decision                 │
        │  • Is this DF using an approved CM?      │
        │  • Should principal consent via CM?      │
        └────────────┬──────────────────────────────┘
                     │
        ┌────────────▼─────────────────────────────┐
        │  If YES: Redirect to CM                  │
        │  If NO:  Direct consent capture (legacy) │
        └──────────────────────────────────────────┘
                     │
                     ├─ PATH A: Via CM (NEW)
                     │  1. Org redirects to CM
                     │  2. CM hosts consent UI
                     │  3. CM captures choice
                     │  4. CM generates receipt
                     │  5. CM redirects back with receipt_id
                     │  6. Org stores receipt_id + verifies signature
                     │
                     └─ PATH B: Direct (LEGACY)
                        1. Org captures consent directly
                        2. Org stores consent record
                        3. Consent treated as "non-CM" origin
```

### Architecture Components

| Component | Role | Responsibility |
|-----------|------|-----------------|
| **Data Principal** | Consent Granter | Reviews notice, selects purposes, grants/denies consent |
| **Organization (DF)** | Consent Requester | Initiates consent flow, receives/stores receipts, fulfills rights requests |
| **Approved CM** | Consent Intermediary | Hosts UI, captures choice, generates receipt, maintains receipt archive, enables withdrawal |
| **Receipt Registry** | Audit Trail | Stores all CM-generated receipts (on-chain or centralized) |
| **DPB** | Regulator | Audits CM practices, enforces CM compliance, handles complaints |

---

## 3. API SPECIFICATION

### 3.1 Organization → CM: Initiate Consent Request

**Endpoint:** `POST https://cm.example.gov.in/v1/consent/initiate`

**Headers:**
```
Authorization: Bearer {org_jwt_token}
Content-Type: application/json
X-Org-ID: {org_id}
X-Request-ID: {unique_request_uuid}
X-Timestamp: {ISO_8601_timestamp}
```

**Request Body:**
```json
{
  "consent_request_id": "creq_org_20260411_001",
  "requesting_org_id": "org-quicklend-001",
  "requesting_org_name": "QuickLend Financial Services",
  "principal_email": "user@example.com",
  "principal_phone": "919876543210",
  "principal_external_id": "principal_ql_789",
  
  "notice_version": "v2.5",
  "notice_url": "https://org.example.com/notice?lang=en&v=2.5",
  
  "purposes": [
    {
      "purpose_id": "PUR-001",
      "purpose_name": "Loan Origination & KYC",
      "purpose_description": "Verify identity and assess credit risk for loan application",
      "legal_basis": "CONSENT",
      "sensitive_data_involved": true,
      "data_categories": ["Aadhaar", "PAN", "Income", "Credit Score"],
      "retention_period_days": 365,
      "third_party_recipients": ["Credit Bureau", "RBI"]
    },
    {
      "purpose_id": "PUR-002",
      "purpose_name": "Marketing Communications",
      "purpose_description": "Send product offers via email and SMS",
      "legal_basis": "CONSENT",
      "sensitive_data_involved": false,
      "data_categories": ["Email", "Phone"],
      "retention_period_days": 730,
      "third_party_recipients": []
    }
  ],
  
  "callback_url": "https://org.example.com/callback/cm-consent",
  "callback_signature_public_key": "-----BEGIN PUBLIC KEY-----\nMFwwDQYJKoZIhvc...\n-----END PUBLIC KEY-----",
  
  "expiry_seconds": 3600,
  "language_preference": "en"
}
```

**Response (201 Created):**
```json
{
  "status": "pending",
  "consent_request_id": "creq_org_20260411_001",
  "cm_consent_request_id": "creq_cm_abc123def456",
  "cm_redirect_url": "https://cm.example.gov.in/consent/creq_cm_abc123def456?return_to=https://org.example.com/callback/cm-consent",
  "expires_at": "2026-04-11T15:00:00Z",
  "created_at": "2026-04-11T14:00:00Z"
}
```

**Error Response (400):**
```json
{
  "error": "invalid_org_credentials",
  "message": "Organization JWT token expired or invalid signature",
  "code": "AUTH_001"
}
```

---

### 3.2 CM → Organization: Callback with Consent Receipt

After principal grants/denies consent on CM UI, CM redirects to organization callback URL with receipt.

**Callback URL (GET):**
```
https://org.example.com/callback/cm-consent?
  consent_request_id=creq_org_20260411_001&
  cm_consent_request_id=creq_cm_abc123def456&
  receipt_id=receipt_cm_xyz789&
  status=GRANTED&
  signature=<ECDSA_P256_signature>&
  timestamp=2026-04-11T14:05:30Z
```

**Org Validation Steps:**
1. Verify ECDSA signature using CM's public key (pre-shared or fetched from CM registry)
2. Verify timestamp freshness (< 1 minute old)
3. Verify receipt_id uniqueness (no replay)
4. Fetch full receipt details via receipt verification API

**Store in Database:**
```sql
INSERT INTO consent_receipts_cm (
  receipt_id,
  org_id,
  principal_id,
  consent_request_id,
  cm_origin,
  cm_consent_request_id,
  status,  -- GRANTED, DENIED, WITHDRAWN
  purposes_json,
  grant_timestamp,
  signature,
  cm_receipt_url
) VALUES (
  'receipt_cm_xyz789',
  'org-quicklend-001',
  'principal_ql_789',
  'creq_org_20260411_001',
  'cm.example.gov.in',
  'creq_cm_abc123def456',
  'GRANTED',
  '[{"purpose_id":"PUR-001","status":"GRANTED"},{"purpose_id":"PUR-002","status":"DENIED"}]',
  '2026-04-11T14:05:30Z',
  '<signature_from_cm>',
  'https://cm.example.gov.in/receipts/receipt_cm_xyz789'
);
```

---

### 3.3 Organization → CM: Verify Receipt (Optional but Recommended)

For added security, org can verify receipt details with CM.

**Endpoint:** `GET https://cm.example.gov.in/v1/receipts/{receipt_id}`

**Headers:**
```
Authorization: Bearer {org_jwt_token}
```

**Response (200 OK):**
```json
{
  "receipt_id": "receipt_cm_xyz789",
  "cm_consent_request_id": "creq_cm_abc123def456",
  "principal_email": "user@example.com",
  "principal_phone": "919876543210",
  "requesting_org_id": "org-quicklend-001",
  "status": "GRANTED",
  "purposes_granted": ["PUR-001"],
  "purposes_denied": ["PUR-002"],
  "timestamp": "2026-04-11T14:05:30Z",
  "signature": "<ECDSA_signature>",
  "signature_public_key_version": "1",
  "receipt_url": "https://cm.example.gov.in/receipts/receipt_cm_xyz789"
}
```

---

### 3.4 Principal → CM: Withdraw Consent

Principal logs into CM dashboard and withdraws consent. CM notifies org.

**CM → Org Withdrawal Notification Webhook:**

```json
POST /webhook/cm-withdrawal

{
  "event_type": "consent.withdrawn",
  "receipt_id": "receipt_cm_xyz789",
  "principal_email": "user@example.com",
  "withdrawn_at": "2026-04-15T10:30:00Z",
  "purposes_withdrawn": ["PUR-001"],
  "requesting_org_id": "org-quicklend-001",
  "cm_id": "cm.example.gov.in",
  "signature": "<ECDSA_signature>"
}
```

**Org Action:**
1. Verify withdrawal signature
2. Cease processing for withdrawn purposes within 48 hours
3. Delete data per statutory hold logic
4. Update consent receipt status to "WITHDRAWN"

---

## 4. OPERATIONAL REQUIREMENTS

### 4.1 Consent Manager Selection

**By May 13, 2027, organizations must decide:**

- **Option A: Use Government-Approved CM**
  - Register with chosen CM (from approved list)
  - Pay CM fees (TBD by government)
  - Integrate using this spec
  - Forward all new consent requests through CM
  - Responsibility: Data Principal identifies itself, CM captures choice, org stores receipt

- **Option B: Maintain Direct Consent Capture (Legacy)**
  - Continue capturing consent directly
  - Maintain full responsibility for consent record integrity
  - Must still comply with FSIUU requirements
  - SDF organizations must ensure audit readiness

**Hybrid Approach (Recommended):**
- Offer BOTH options to data principal at consent page
- "Choose: Consent via Government CM [approved list] OR Consent via [OrgName]"
- Route based on principal choice
- Both receipt types stored in consent registry with origin tag

---

### 4.2 Receipt Storage & Longevity

**Org Must Store:**
- receipt_id
- CM origin (cm.example.gov.in)
- Principal email/phone
- Purposes granted/denied
- Timestamp
- Signature (for audit trail)
- Link to full receipt on CM (or local copy)

**Retention:**
- Minimum: As long as processing continues + 3 years after withdrawal
- Typical: Lifetime of relationship + 3 years

**Audit Trail:**
- Every receipt retrieval/verification logged
- Hash chain linkage (audit_log table with prev_hash)

---

### 4.3 Cross-Organization Consent Propagation (Future)

DPDP Rules 2025 Section 6(9) envisions principals granting consent once and having it propagate to multiple orgs. This is **Phase 2** (post-May 2027).

**Future Feature:**
```
Principal grants consent to DF-A via CM
  ↓
CM asks: "Allow DF-B to use this consent?"
  ↓
If YES → CM generates receipt for DF-B with principal's authorization
  ↓
DF-B can accept receipt without re-asking principal
```

**Status:** Not yet operationalized; prepare data model for future

---

## 5. COMPLIANCE CHECKLIST

- [ ] Organization has identified government-approved CM list (publish date: November 14, 2026)
- [ ] CM selection decision made (use CM vs. direct consent) by **May 1, 2027**
- [ ] API integration spec implemented and tested against CM sandbox by **May 1, 2027**
- [ ] Callback webhook implemented and tested by **May 1, 2027**
- [ ] Receipt storage schema designed and deployed by **May 13, 2027**
- [ ] Staff trained on CM receipt handling by **May 13, 2027**
- [ ] Consent UI updated with CM redirect option by **May 13, 2027**
- [ ] Data Principal Rights (withdrawal, access) updated to handle CM receipts by **May 13, 2027**
- [ ] Audit logging captures receipt origin (CM vs. Direct) by **May 13, 2027**
- [ ] DPO approval of CM integration strategy by **May 13, 2027**

---

## 6. FAQ & RISKS

**Q: What if government doesn't approve any CMs by November 2026?**  
A: Organizations may continue direct consent capture. No mandate to use CM if none approved.

**Q: Are we forced to use a CM?**  
A: No. DPDP Rules 2025 permit but do not mandate CM use. Organizations can continue direct capture.

**Q: What if a principal grants consent via CM but later disputes it?**  
A: CM maintains tamper-proof receipt. Organization can present receipt as evidence. CM liable for receipt integrity.

**Q: Multi-org consent propagation — what are my obligations?**  
A: For Phase 2 (post-May 2027): If principal consents to cross-org sharing via CM, be ready to receive and store CM-issued receipt for your org.

---

## 7. SIGN-OFF & APPROVAL

**DPO Sign-Off:**  
<input type="text" placeholder="Signature" style="border:none; border-bottom:1px solid #333; width:250px;"> Date: <input type="text" placeholder="DD/MM/YYYY" style="border:none; border-bottom:1px solid #333; width:150px;">

**General Counsel Approval:**  
<input type="text" placeholder="Signature" style="border:none; border-bottom:1px solid #333; width:250px;"> Date: <input type="text" placeholder="DD/MM/YYYY" style="border:none; border-bottom:1px solid #333; width:150px;">

**CTO / Technical Lead Approval:**  
<input type="text" placeholder="Signature" style="border:none; border-bottom:1px solid #333; width:250px;"> Date: <input type="text" placeholder="DD/MM/YYYY" style="border:none; border-bottom:1px solid #333; width:150px;">

---

**Next Review Date:** June 30, 2026 (after government CM list publication)
