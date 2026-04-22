# Critical Do's & Don'ts — By Compliance Domain

A reference guide of best practices and anti-patterns across all 17 DPDP domains. Each entry explains **Why** it matters for legal, operational, and risk mitigation.

---

## Domain 1: Consent & Privacy Notice (Section 6)

### Consent Validity (FSIUU)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| Require **all 5 FSIUU attributes** before marking consent valid | Accept consent missing *any* of the 5 (Free, Specific, Informed, Unconditional, Unambiguous) | DPDP Section 6(1) requires FSIUU as a sine qua non for valid consent; invalid consent = unauthorized processing = ₹50-100 Cr penalty + DPBI action |
| Provide **separate checkboxes per purpose** (Account Mgmt ≠ Marketing ≠ Analytics) | Bundle all purposes into single checkbox | Consent must be purpose-specific; bundling = invalid consent for any one purpose; withdrawal of one purpose must not affect others |
| **Prominently display** privacy notice *before* consent request | Bury privacy notice in Terms & Conditions footer | Informed consent requires data principal sees privacy notice BEFORE consenting; non-prominent placement = ambiguous consent = invalid |
| Show **unambiguous yes/no** (radio button, explicit toggle, clear text) | Use pre-ticked boxes, double negatives, or implicit opt-in | Unambiguous consent requires data principal actively chooses "yes"; pre-ticked = presumed consent (invalid under Section 6) |
| **Document consent grant** with timestamp, IP, device, consent form version hash | Store only consent ID without context | Audit trail proves valid consent if challenged; missing timestamp/version = can't prove FSIUU compliance; 7-year retention required for DPBI disputes |
| **Re-consent immediately** if consent audit finds >5% invalid consents | Ignore invalid consents; keep using data | Invalid consent = breach; using data = violation of Section 6(1); re-consent must be FSIUU-compliant; escalate to DPBI if >5% already granted invalid consent |

### Privacy Notice Compliance

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Publish updated privacy notice** within 5 days if data processing materially changes | Delay updating privacy notice while continuing new processing | Data principal has right to be informed (Section 5); continuing processing with outdated notice = deception; escalates to breach liability |
| Include **all 12 mandatory sections** (controller identity, categories, legal basis, rights, recipients, retention, security, breach procedure, DPO contact, etc.) | Omit sections (e.g., no security measures, no breach notification procedure) | Incomplete privacy notice = incomplete transparency; DPDP requires full disclosure; gaps = MEDIUM priority gap in 17-domain audit |
| Provide privacy notice in **org's registered language + data principal's preferred language** | English-only notice for multilingual market | DPDP does not mandate multilingual, but fair notice requires data principal can understand; legally defensible if principal explicitly chose English, but risky in India |
| Make privacy notice **easily accessible** (on homepage, before signup, in app settings, downloadable PDF) | Lock privacy notice behind login or deep navigation | Transparency requires easy access; inaccessible notice = circumventing transparency obligation |
| **Version and archive** all prior privacy notice versions (with effective dates) | Overwrite old notices without history | Audit trail proves what data principal saw when consenting; without versions, can't prove FSIUU compliance for historical consents |

---

## Domain 2: Data Subject Rights (Sections 11-14)

### DSAR (Data Access Subject Access)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Respond to DSAR within 30 days** (Section 11) with all personal data in portable format (CSV, JSON) | Miss 30-day SLA or delay response | DPDP Section 11 guarantees 30-day SLA; missing SLA = escalation to DPBI; ≥3 missed DSARs = complaint to DPBI; ₹50M+ penalty + reputation damage |
| **Provide portable format** (machine-readable, interoperable) with all data principal's personal data across all systems | Provide only snippets in PDF; omit linked data from other systems | Portability requires all related data (consent artifacts, DPIA findings, DPA clauses); incomplete DSAR = incomplete exercise of right = breach |
| **Verify data principal identity** before disclosing personal data (match email/phone/ID) | Send data to unverified requester | Security requirement; unverified DSAR = data leak liability; always authenticate |
| **Exclude third-party personal data** from DSAR export (e.g., employee names in transaction logs) | Include unrelated individuals' data in DSAR package | Third-party privacy violation; excludes only necessary to prevent harm to others (Section 11(4)) |
| **Document DSAR chain of custody:** received date, authentication method, response date, format delivered | No record of DSAR request/response | Audit trail proves SLA compliance; missing records = presumed violation; DSDP requires 7-year archive |
| **Auto-escalate to DPBI if DSAR outstanding >30 days** | Ignore missed SLA silently | DPDP Section 14(1) requires data principal notify DPBI if DFF refuses/delays DSAR; escalate proactively to avoid complaint |

### Correction (Section 12)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Grant correction within 15 days** + notify all processors/third parties within 5 business days | Refuse correction or delay >15 days | Section 12(1) guarantees 15-day SLA; Section 12(4) requires processor propagation ≤5 days; violation = individual complaint to DPBI |
| **Verify correction request** (inaccuracy vs subjective complaint) before accepting | Blindly accept every "correction" request | Inaccuracy = factually wrong (e.g., wrong address); not opinion (e.g., "I'm not a credit risk"); verify scope to avoid corrupting valid data |
| **Propagate correction to all processors** with 5-day SLA (CC: vendors in email + confirmation required) | Correct own DB only; don't notify processors | Section 12(4) makes processor propagation mandatory; missed propagation = incomplete correction = breach; document confirmations in audit log |
| **Offer **alternative: add "contested" note** if correction cannot be verified | Reject correction requests outright | DPDP allows data principal to add dispute marker; better UX than rejection; escalation valve |

### Erasure (Section 12, "Right to Be Forgotten")

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Erase personal data within 30 days** (Section 12(2)) unless statutory hold applies | Delay >30 days; retain beyond statutory requirement | 30-day SLA is mandatory; violation = ₹10-50M penalty per ₹10,000 records deleted; document erasure in immutable log |
| **Check Statutory Hold Register** before erasing; explain hold if applicable (e.g., "KYC records retained 10 years per RBI mandate") | Ignore holds; erase data subject to legal retention | Illegal deletion = breach + regulatory non-compliance; RBI/tax audits fail if KYC erased; loss of audit trail |
| **Cascade erasure to all processors/vendors** (Section 12(4)) with 5-day SLA | Erase own DB only; don't notify processors | Incomplete erasure across vendors = DPDP violation; processor may still have copy = second breach |
| **Log erasure request + action in immutable audit log** (what was deleted, why, when, who authorized) with hash-chaining | Delete from audit log too | Audit trail proves erasure; cannot prove GDPR/DPDP compliance if logs missing; hash-chaining detects tampering |
| **Anonymize instead of erase** if full deletion impossible (e.g., analytics archives) | Keep personal data + PII in archives indefinitely | Anonymization is acceptable alternative (non-reversible de-identification); document anonymization method (k-anonymity, etc.) |
| **Offer bilateral deletion** if cross-border transfer: data principal can revoke sharing to country X | Force global deletion | Section 16(3) allows cross-border deletion; if data shared with US, RBI may allow EU-deletion-only; clarify in privacy notice |

### Nomination (Section 14)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Accept nominee registration** with ID proof of both nominee + data principal | Require complicated verification; make registration hard | Section 14 allows nominee to exercise rights on behalf of deceased; streamlined nomination = compliance advantage + customer goodwill |
| **Store nominee record with ID proof copies** (7-year retention) | Store only nominee name without identity verification | Audit trail: if nominee exercises rights, must prove they were validly registered; missing ID proof = liability |
| **Implement heir/estate flow:** Nominee can submit death cert + request data principal's consents/DSARs be exercised | Refuse nominee requests after death | Nomination creates inheritance of data rights; nominee can request DSAR, correction, erasure on behalf of deceased principal |

### Grievance (Section 14)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Respond to grievance within 30 days** (Section 14(2)) with written acknowledgment within 7 days | Ignore grievance; no acknowledgment | SLA breach = escalation to DPBI; unacknowledged grievance = presumed denial; ₹10-50M penalty |
| **Escalate to DPBI if unresolved after 30 days** (Section 14(2)) with evidence trail | Stall grievance beyond 30 days | DPBI must be notified of unresolved grievance; escalation is mandatory, not optional |
| **Document grievance + resolution** in immutable log (complaint date, issue, investigation, decision, remedy) | No record of grievance received/resolved | Audit trail proves due process; missing records = presumed negligence |
| **Offer appeal mechanism** if grievance denied | Final refusal with no appeal path | Fairness requires appeal; offer escalation to Board Privacy Committee or external mediator |

---

## Domain 3: Legitimate Uses (Section 7)

### Legal Basis Classification

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Document every Section 7 use case** with legal reference + necessity justification | Use Section 7 without documented legal basis | DPDP Section 7 allows processing *without* consent if grounds clearly established; no documentation = presumed consent-free processing without legal basis = breach |
| **Classify correctly:** KYC = Section 7(ii) statutory, Fraud = Section 7(iii) legitimate interest, AML = Section 7(ii) statutory, Collections = Section 7(iii) with contract + consent for certain channels | Misclassify uses (e.g., call fraud detection as "analytics consent") | Misclassification = wrong legal basis = breach; DPBI audits classification; penalties up to ₹50M if wrong |
| **For Section 7(iii) legitimate interest:** Document balancing test (interest vs data principal's rights), data minimization | Assume legitimate interest covers all processing | Section 7(iii) requires explicit balancing; over-reliance on legitimate interest = overreach; DPBI scrutinizes |
| **Provide opt-out path** for Section 7 processing where possible (except statutory) | Force processing without opt-out | Fairness requires opt-out if not legally mandatory; no opt-out = customer distrust |
| **Re-classify if processing changes** (e.g., analytics purpose changes) | Lock classification; process under old legal basis | Scope creep = reclassification required; failure to re-classify = unauthorized processing |

### Cross-Channel Consent Rules

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **SMS/WhatsApp OTP (authentication):** Use Section 7(viii) lawful contract; no consent needed | Require consent for OTP | OTP is service delivery; consent unnecessary; requiring consent = poor UX + compliance confusion |
| **Transactional SMS/Email (statements, EMI reminders):** Use Section 7(viii) lawful contract; no consent needed | Request consent for transactional messages | Service-related communication; consent not required if related to established contract |
| **Marketing SMS/WhatsApp (promotions):** Require Section 6 consent; whitelist all; track withdrawal SLA ≤24hr | Send promotional SMS without prior consent | TRAI rules + DPDP Section 6 both require opt-in consent for marketing; violation = ₹100K/message penalty from TRAI + DPBI |
| **Service notification (policy updates, new fees, security alerts):** Use Section 7(ii) statutory or Section 7(viii) contract; no consent needed | Require consent for service notifications | Service updates are operational; suppress consent dialog = worse UX |
| **Account Aggregator (AA) data sharing:** Use Section 6 AA Consent Artefact; immutable 7-year storage | Use transactional SMS for AA permission | AA requires formal consent artefact (RBI mandate); SMS is insufficient proof; artefact must be immutable + archival-grade |
| **Recorded voice calls (support, collections):** Require Section 6 consent for recording; pre-recorded consent in call start | Record calls without consent | Telecom regulations + DPDP Section 6 both require consent; non-consensual recording = ₹50K/call penalty from TRAI |

---

## Domain 4: Information Security (Section 8)

### Encryption

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Encrypt all personal data at rest** using AES-256-GCM or stronger (Section 8(2)) | Store personal data in plaintext | Breach of Section 8(2); unencrypted breach = ₹50-100M penalty; plaintext is indefensible |
| **Use TLS 1.3+ for all in-transit encryption** (HTTPS for web, TLS for APIs) | Use TLS 1.0 or HTTP for personal data transmission | TLS 1.0 is broken; unencrypted transit = man-in-the-middle exposure; breach of Section 8(2) |
| **India-specific rules:** Aadhaar = VID (Virtual ID) or hash ONLY, never plaintext 12-digit; PAN = masked XXXXXXX1234 in logs/APIs/dashboards | Store Aadhaar/PAN plaintext | DPDP + RBI + PMLA all prohibit plaintext biometric/PAN storage; violation = ₹100M+ penalty + law enforcement referral |
| **Key management:** Rotate encryption keys annually; store master key in HSM or AWS KMS (never plaintext config) | Store encryption keys in plaintext config files | Key compromise = all data exposed; plaintext keys = elementary violation; use HSM/KMS |
| **Hash sensitive data** (Aadhaar, PAN, SSN) using SHA-256; compare hashes, never decrypt for comparison | Hash with MD5; store hashes in code | MD5 is broken; hashes in code = key leakage vulnerability; SHA-256 only |

### Access Control (RBAC)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Implement role-based access control (RBAC)** per Section 8: DPO, Legal, Compliance, IT, Finance, Customer Service roles with *least privilege* | Open all data to all staff | Least privilege minimizes breach blast radius; open access = ₹25-50M penalty per role |
| **Mandate MFA** for all admin/DPO/Legal/Compliance accounts; JIT (just-in-time) elevated access auto-revoke after 2 hours | Single-factor password auth for sensitive roles | Breach of Section 8(3) (security measures); password compromise = full takeover; MFA = baseline |
| **Quarterly access review:** Verify all active accounts, remove unused access, revalidate role assignments | No access review; accounts accumulate | Stale access = breach vector; quarterly review = compliance requirement; document reviews |
| **Implement zero trust:** Never trust, always verify; every request requires authentication + re-authorization | Assume trust after first login | Zero trust prevents lateral movement if one account compromised; essential for multi-tenant safety |

### Audit Logging (Section 8)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Log all data access:** Who accessed what, when, from where (IP), why (purpose), successful or failed | No audit trail of data access | Audit log proves compliance; missing logs = presumed violation; can't prove data wasn't stolen |
| **Make audit logs immutable:** INSERT-only database; no UPDATE/DELETE of past entries (prevents log tampering) | Update/delete audit logs after incidents | Immutability proves logs weren't forged; mutable logs = worthless in litigation |
| **Implement hash-chaining:** Each log entry includes SHA-256 hash of previous entry (Merkle chain); detect any tampering | No hash-chaining; linear logs only | Hash-chain detects if logs altered; linear logs can be inserted/deleted undetectably |
| **Redact PII before logging:** Remove Aadhaar/PAN/Email/Phone from audit entries; log only hashes + masked tokens | Log full PII in audit entries | PII in logs = log file becomes a PII database; if log breached, PII exposed; always redact |
| **Retain logs 7 years** (DPDP Section 5 accountability) per WORM (write-once, read-many) archive | Purge logs after 1 year | 7-year retention proves historical compliance; shorter retention = presumed destruction of evidence |
| **Configure SIEM (Security Information & Event Management)** with 8 alert rules: bulk export >10K records, privilege escalation, ransomware pattern, brute force, API key exposure, schema changes, unauthorized access, malware | Manual log review only | SIEM detects anomalies humans miss; real-time alerts catch active breaches; manual review is reactive |

### Incident Response

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Have written incident response plan** (6 steps: detect, assess, contain, eradicate, recover, post-incident review) | No incident plan; ad-hoc response during breach | Breach response chaos = delayed notification = ₹50-100M penalty; written plan = coordinated response |
| **Conduct tabletop exercise annually** (simulate breach scenario; walk through playbook) | No testing; only execute plan under real breach | Untested plan fails when needed; tabletop = low-risk rehearsal |
| **Dual-timer breach notification:** DPBI (72 hours for data breach) + CERT-In (6 hours for cybersecurity incident); both run in parallel, not sequential | Sequential notification (CERT-In then DPBI) | Parallel timing = faster public alert; sequential = delayed response; both are independent obligations |

---

## Domain 5: Children's Data (Section 9)

### Age Verification

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Implement age verification** (OAuth parent consent, ID proof, parental email verification) before collecting child's data | No age check; process children same as adults | DPDP Section 9 requires verifiable parental consent for <18; no verification = invalid consent = ₹10-50M penalty per child |
| **Obtain verifiable parental consent** for children <18; consent from parent's verified email/phone + signature | Collect child's assent only (not parent consent) | Section 9(1) requires **parent** consent, not child; assent alone is insufficient |
| **Store consent proof with parent ID/email verification record** (7-year retention) | No proof of parental consent verification | Audit trail proves compliance; missing proof = presumed violation |

### Data Minimization for Children

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Collect only data necessary for stated purpose** for children (minimize profiling, behavioral tracking) | Over-collect children's data for "future use" | Scope creep = unauthorized processing; children's data = extra sensitivity; minimize = DPDP mandate |
| **Restrict behavioral tracking/profiling** of children (no algorithmic decisioning for educational impact) | Use child's data for ad-targeting, recommendation algorithms | Automated decision-making on children = DPIA trigger + Section 8(4) scrutiny; harm potential high; restrict |
| **Offer easy data deletion** for children (no friction; no "reasons for deletion" survey) | Require children submit deletion request + justify reason | Deletion must be friction-free for minors; extra steps = de-facto denial of right |

---

## Domain 6: DPIA & DPO (Section 10)

### DPIA (Data Protection Impact Assessment)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Conduct DPIA before high-risk processing:** biometric, health, automated decision-making, large-scale, children, cross-border, novel tech, systematic monitoring | Skip DPIA for "normal" processing | DPDP Section 10(2) mandates DPIA for high-risk; risk assessment = proactive compliance |
| **Document DPIA process:** trigger analysis, risk assessment (Likelihood × Impact matrix), safeguards, DPO approval, sign-off | No DPIA documentation | Audit proves process followed; no docs = presumed negligence; DPBI penalizes missing DPIAs |
| **Include mitigation controls:** encryption, access control, audit logging, consent management, DSAR/deletion SLA, vendor DPA, bias testing | Risk assessment only; no safeguards | Risk alone insufficient; safeguards reduce risk; document how each control mitigates risk |
| **Re-assess DPIA if processing materially changes** (new data category, new recipient, new retention period) | Lock DPIA after approval; no re-assessment | Processing evolves; DPIA becomes stale; re-assess every 24 months minimum |

### DPO (Data Protection Officer)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Appoint DPO if SDF** (Section 10(1)); role = independent review of DPIA, audit, DPBI escalation, privacy committee chair | Appoint DPO with heavy IT operational load | DPO independence = credibility; operational tasks = conflict of interest; DPO cannot be IT ops manager |
| **DPO reports to Board Privacy Committee,** not CEO/CTO (independence requirement) | DPO reports to CTO; CEO/CTO override DPO recommendations | DPO independence is structural; reporting to operational leadership = lack of independence = violation |
| **Provide DPO resources:** training budget, tools (DPIA template, audit toolkit), legal support, autonomy | Appoint DPO with no budget/tools/autonomy | Underfunded DPO = nominal compliance; invest in DPO = real compliance; document resources allocated |
| **DPO conducts annual audit** across all 92 checkpoints; documents findings in audit report signed by DPO | Self-assessment without DPO | DPO's independent audit = credibility; DPO signature = accountability |

---

## Domain 7: Breach Notification (Section 20)

### 72-Hour DPBI Notification

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Notify DPBI within 72 hours** of identifying breach; if impossible to assess in 72 hours, notify with preliminary info + timeline for full report | Delay notification hoping breach resolves | DPDP Section 20(1) is hard 72-hour SLA; violation = ₹50-100M penalty + DPBI investigation |
| **Notification content:** incident summary, data categories affected, # of principals affected, likely impact, remedial measures, DPBI contact (DPO) | Minimal notification; hide scope/impact | DPBI needs detail to assess systemic risk; sparse notification = presumed cover-up |
| **Simultaneously notify CERT-In (6-hour SLA)** if breach involves cybersecurity incident (malware, ransomware, unauthorized access via hacking) | Sequential notification (DPBI then CERT-In) or only DPBI | Both agencies have independent SLA; parallel = compliance |
| **Maintain breach log (T-30)** with incident ID, date, categories, # principals, DPBI notification date, investigation findings, remediation | No centralized breach register | Breach register = audit trail; demonstrates pattern of incidents (or lack); required for annual certification |

### Customer Notification

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Notify affected data principals without undue delay** if breach likely causes harm (Section 20(3)) | Delay customer notification beyond DPBI notification | DPBI notified ≠ customers informed; customers have right to timely notice; delayed notice = separate breach |
| **Notification includes:** breach summary, data affected, likely consequences, remedial measures, DPO contact | Obscure notification language; no actionable steps | Transparency requires clear language; customers need to know impact + what to do (monitor accounts, etc.) |
| **Offer remedies:** credit monitoring, password reset assistance, identity theft insurance (if financial data) | Notification only; no remedial support | Offers demonstrate good faith; cost is fraction of breach liability |

---

## Domain 8: Data Retention & Deletion (Section 17)

### Retention Schedule

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Publish Data Retention Schedule (T-02A)** specifying how long each data category retained (per-purpose + per-legal-basis) | No published retention schedule; vague "as long as needed" | Transparency requires explicit retention; DPDP Section 17(1) mandates retention only "as long as necessary" |
| **Apply stricter requirement if applicable:** e.g., RBI KYC 10-year hold overrides DPDP default 6 months | Default to DPDP 6-month retention for KYC | Regulatory overlay (RBI, tax, PMLA) often mandates longer; apply stricter standard; document in Statutory Hold Register |
| **Document erasure schedule:** Auto-delete old records after retention expires; track deletes in immutable log | Manual deletion only; some data kept indefinitely | Automated deletion = consistent compliance; manual = prone to gaps; document schedule (weekly cron job, etc.) |
| **Re-assess retention if processing purpose changes** (e.g., analytics retention may differ from transactional) | Lock retention decision after first classification | Scope change = re-assess retention; document re-assessment |

### Deletion

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Cascade deletion to all processors/vendors** within 5 days (Section 17(2)); document confirmations | Delete own database only; don't notify processors | Incomplete deletion = DPDP violation; processor may still have copy = residual exposure |
| **Immutable deletion log (T-29):** Track every erasure request (who, when, what data, reason, confirmation), cannot tamper | No deletion record; data silently purged | Deletion audit trail proves compliance; missing logs = presumed unauthorized retention |
| **PII still in analytics/archives?** Anonymize instead of delete (irreversible de-identification, k-anonymity ≥5, aggregate counts) | Keep personal data + PII in analytics indefinitely | Anonymization satisfies deletion requirement if irreversible; document anonymization method |

---

## Domain 9: Vendor & Processor Management (Section 12(4), Section 16)

### DPA (Data Processing Agreement)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Sign DPA with 100% of processors** before sharing personal data (Section 12(4) mandate) | Process data via vendors without DPA | No DPA = uncontrolled processing; vendor has no contractual obligation to comply = breach |
| **Include Section 12(4) propagation clause:** Vendor must propagate correction/erasure requests to sub-processors ≤5 days | No propagation clause; vendor independent of requirements | Correction/erasure SLA breaks if vendor doesn't propagate; vendor must contractually propagate |
| **Include audit rights** (right to audit vendor's security controls, receive SOC2 reports annually) | No audit rights; blind trust | Audit rights = visibility into vendor's practices; required by DPDP Section 8(4) processor accountability |
| **Include sub-processor clause:** Vendor cannot engage sub-processors without 30-day advance notice + data principal opt-out right | Vendor can freely add sub-processors | Sub-processor transparency = data principal knows full chain; unauthorized sub-processor = breach |
| **Include data location clause:** Specify where personal data processed (India-only, or specific countries, cross-border transfer rules per Section 16) | No data location clause; vendor can move data anywhere | Data location matters for regulatory compliance; specify permitted countries in DPA |
| **Include deletion/termination clause:** Upon contract termination, vendor must delete or return all personal data within 30 days | Vendor retains data after termination | Deletion on termination = standard practice; missing clause = residual exposure |

### Vendor Risk Assessment

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Conduct Vendor Risk Assessment (T-16)** for all processors: security score (encryption, MFA, audit logs), compliance score (GDPR, DPDP, ISO27001), geopolitical risk (country, regulatory environment) | No vendor risk assessment; assume all vendors secure | Risk assessment = due diligence; missing assessment = negligent delegation = breach liability |
| **Risk score >70 = HIGH risk:** Require SOC2 Type II audit, insurance, executive commitment; consider alternative vendor | Engage high-risk vendor without mitigation | >70 risk = unacceptable without strong controls; SOC2 audit + insurance = risk reduction |
| **Annual re-assessment:** Vendor landscape changes (breach history, regulation changes); re-assess annually | One-time assessment; no updates | Vendor risk evolves; re-assess to catch new issues |

### Sub-Processor Management

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Maintain Sub-Processor Register (T-44A):** Track all sub-processors engaged by primary vendor; request 30-day advance notice | No sub-processor visibility; primary vendor responsible | DPDP requires full chain transparency; register = audit proof |
| **Offer sub-processor opt-out right** (if data principal objects to specific sub-processor, deny/suppress processing that data) | Force data principal accept all sub-processors | Fair notice requires opt-out right; mandatory sub-processor = unfair |

---

## Domain 10: Cross-Border Transfers (Section 16)

### Adequacy & Binding Contracts

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Check if recipient country has adequacy finding** from India (currently: [verify with latest DPDP Rules]; most countries require binding contract) | Assume all countries safe; no legal basis check | Most countries lack adequacy; transfer without contract = unauthorized international disclosure = breach |
| **For non-adequate countries,** execute Binding Corporate Rules (BCR) or Standard Contractual Clauses (SCC) + Section 16(3) explicit consent | Transfer to non-adequate country with no contract | Binding contract required by Section 16(2); transfer without = breach; explicit consent + contract = dual safeguard |
| **Include Section 16(3) explicit consent** for each cross-border transfer; show data principal *which* country, *which* vendor, *which* data categories | Implicit consent via privacy notice + blanket transfer | Cross-border requires *explicit, specific* consent per Section 16(3); blanket consent invalid |
| **Document all cross-border transfers in Cross-Border Transfer Register (T-44):** Recipient country, legal basis, data categories, consent status, contract signed date | No centralized transfer register | Register = audit trail; missing docs = presumed unauthorized transfer |

### Schrems II Implications (if EU personal data involved)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **If transferring EU personal data to India:** Assess data protection equivalent (GDPR vs DPDP parity); document adequacy analysis | Assume Europe → India transfer is automatic | EU data protection is stricter than DPDP in many areas (consent, DPO, DPIA, processor oversight); document parity analysis |
| **If transferring India personal data to US/UK:** Assess surveillance law risk (US FISA, UK IPB); document GDPR-equivalent safeguards | Assume US/UK = safe havens; no risk assessment | US/UK surveillance laws (FISA, IPB) override GDPR/DPDP privacy; document mitigation (encryption, data minimization) |

---

## Domain 11: Audit & Monitoring (Section 5)

### Compliance Dashboard

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Deploy live compliance dashboard (T-38)** showing 0-100% score (checkpoints completed / 92 total) + RAG per 17 domain | Offline compliance tracking; no visibility | Live dashboard = board visibility; transparency drives accountability; compliance becomes operational KPI |
| **Track 8 KPIs:** consent health, DSAR SLA, withdrawal rate, invalid consent rate, deletion SLA, breach SLA, audit status, training completion | Track only "compliance %" without metrics | KPIs reveal operational gaps; consent health declining = systemic issue (data principal distrust); catch early |
| **Weekly dashboard update; monthly board report** | Quarterly compliance review | Weekly = timely detection of drift; monthly board report = accountability; escalation if score drops |

### Monitoring & Alerting

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Configure data discovery scanning (T-32):** Weekly scan of all databases/cloud storage for PII concentrations; escalate unknown PII | Manual data inventory only; no scanning | Automated discovery = find PII you didn't know existed (e.g., SSNs in test data); manual = gaps |
| **Encryption audit (T-33):** Quarterly verify AES-256 at rest, TLS 1.3+ in transit, Aadhaar/PAN masking rules followed | No encryption audit; assume encryption is set | Encryption configurations drift; quarterly audit = catch weak configs before breach |
| **Access control audit (T-34):** Quarterly RBAC review, MFA enforcement, privilege escalation detection | No access review; roles accumulate | Stale access = breach vector; quarterly cleanup |
| **SIEM alerting (T-35):** Configure 8 alerts (bulk export, privilege escalation, ransomware, brute force, API key exposure, schema changes, unauthorized access, anomalous slow query) | No SIEM; manual log review only | Real-time alerts catch active breaches; manual = reactive |

---

## Domain 12: Grievance Handling (Section 14)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Accept grievances via multiple channels:** email, portal, phone, in-person; no gatekeeping | Only email; require formal procedure | Multiple channels = accessibility; gatekeeping = de-facto denial |
| **Respond within 30 days with written decision** (Section 14(2)) | "No decision within 30 days" or evasive response | 30-day SLA is hard requirement; violation = DPBI escalation |
| **Escalate to DPBI if unresolved after 30 days** | Stall beyond 30 days without escalation | Automatic DPBI escalation = compliance; no escalation = DPBI complaint incoming |
| **Appeal mechanism:** If grievance denied, offer appeal to Board Privacy Committee or external ombudsman | No appeal; final refusal | Fairness requires appeal; demonstrates good faith |

---

## Domain 13: Consent Withdrawal (Section 11(2))

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Enable withdrawal in real-time:** In-app toggle, email link, SMS reply "STOP" | Require phone call + identity verification for withdrawal | Section 11(2) requires frictionless withdrawal; extra steps = de-facto denial; withdrawal SLA = immediate |
| **Propagate withdrawal to all processors** (CPaaS, analytics, email platform) within 24 hours; document confirmations | Withdraw consent in own DB; don't notify downstream systems | Incomplete withdrawal = continued processing = breach; downstream vendors must stop immediately |
| **Track withdrawal rate weekly;** alert if rate >15% (indicates consent quality or data principal distrust issues) | No withdrawal tracking | High withdrawal rate = system issue; low consent trust = investigate privacy notice clarity, data minimization |
| **Respect withdrawal before response:** If DSAR requested + withdrawal pending, honor withdrawal first (don't process data) | Process DSAR after withdrawal | Withdrawal = stop processing; DSAR contradicts if processing ceased; withdrawal takes precedence |

---

## Domain 14: Legitimate Use Documentation (Section 7)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Document all Section 7 use cases:** Each use case has written legal memo justifying necessity, data minimization, balancing test (if Section 7(iii) legitimate interest) | Assume Section 7 covers all processing without documentation | Documentation = proof of due diligence; DPBI audits classification; missing docs = presumed unauthorized processing |
| **Obtain Legal sign-off** on all Section 7 memos before processing starts | Product team self-certifies Section 7 | Legal review = credibility; self-certification = liability; DPBI expects legal counsel sign-off |

---

## Domain 15: Privacy by Design (Section 8)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Include privacy requirements in product requirements document** before development starts | Add privacy controls post-launch as patch | Privacy by design = embedding privacy from concept; post-hoc patches = security theater + gaps |
| **Default to data minimization:** Only collect data strictly necessary for purpose; test with fewer data categories | Collect "everything might be useful" | Data minimization = risk reduction; less data = smaller breach impact; fewer retention obligations |
| **Privacy impact analysis for each feature:** Before launch, assess data categories, recipients, retention, security, consent | Ship features without privacy review | Privacy review = catch issues early; post-launch = customer impact |
| **Implement DSAR/deletion APIs early** (not bolted on) | Realize after launch DSAR implementation is hard | APIs designed into architecture = scalable; retrofitted = fragile |

---

## Domain 16: Employee Training (Section 5)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Mandatory DPDP training for 100% of staff** (2-hour course covering FSIUU, data subject rights, breach response) | Training optional or low completion rate | Training = awareness; untrained staff = breach vectors; mandatory + tracked = compliance |
| **Role-specific modules:** IT (encryption, access control), HR (employee data handling), Customer Service (DSAR response), Finance (data retention), Marketing (consent compliance) | Generic training for all roles | Role-specific = relevant; generic = low engagement; different roles have different risks |
| **Annual refresher training;** re-train new hires within 30 days | One-time training; no refresher | Compliance knowledge decays; annual refresh = currency; new hires need baseline |
| **Track completion + quiz scores;** target ≥95% completion | Training assigned; no tracking | Tracking = accountability; low completion = compliance risk; target 95%+ |

---

## Domain 17: Governance & Board Oversight (Section 10, Section 5)

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Establish Board Privacy Committee** (Section 10(2) SDF requirement); quarterly meetings | No board-level privacy oversight | Board accountability = compliance seriousness; no board oversight = reactive governance |
| **Board resolution** approving compliance roadmap + DPO appointment + Privacy Committee charter | Verbal approval only; no formal resolution | Resolution = documented authority; DPBI expects board minutes |
| **DPO appointed before Phase 1 starts;** independent role (not CTO/COO) | DPO hired mid-compliance project | Early appointment = DPO shapes Phase 1 ROPA; late appointment = DPO inherits poor choices |
| **Quarterly Board Risk Report (T-37):** Compliance score, domain RAG, breach summary, remediation roadmap | Annual compliance report only | Quarterly = timely visibility into risks; breaches = immediate notification (not deferred to annual) |
| **Annual compliance certification** by DPO/Auditor; published publicly (website transparency) | No certification; internal compliance claim | Public certification = credibility; website publication = data principal confidence |

---

## FinTech-Specific Do's & Don'ts

| ✅ DO | ❌ DON'T | Why It Matters |
|---|---|---|
| **Maintain RBI-compliant KYC records:** 10-year retention minimum; add to Statutory Hold Register | DPDP default 6-month retention for KYC | RBI Master Direction overrides DPDP; 10-year mandatory for KYC |
| **Account Aggregator (AA) consent:** Use AA Consent Artefact (immutable, signed, RBI-compliant); never use SMS/WhatsApp for AA permission | SMS-based AA consent | SMS is transactional; AA requires formal artefact per RBI AA framework; artefact = 7-year retention |
| **Masked PAN in all outputs:** XXXXXXX1234 in logs, APIs, dashboards, exports; never FULL PAN visible | PAN visible in customer-facing outputs | RBI + DPDP both require masking; visible PAN = ₹100K per PAN penalty; masking = standard practice |
| **Loan document deletion:** Respect 8-year RBI hold *after* loan closure; erasure request acknowledged but hold explained | Erase loan docs on deletion request | RBI 8-year hold is regulatory; cannot erase despite DPDP request; explain hold + offer alternative (anonymization) |
| **EMI/transaction SMS:** Use Section 7(viii) lawful contract; no consent needed | Require consent for transactional SMS | Transactional SMS = service delivery; consent unnecessary; requiring it = UX friction + compliance confusion |
| **Collections calls (recorded):** Obtain Section 6 consent for recording before call; pre-recorded announcement at call start | Call recording without consent | TRAI + DPDP require consent; non-consensual recording = ₹50K/call TRAI penalty |

---

## Summary: The Compliance Mindset

✅ **Core Principle:** If a person's data is involved, transparency + consent + control is mandatory (Section 6). If Section 7 legitimate use applied, document it (Section 7). Encrypt everything (Section 8). Respond to rights requests fast + completely (Sections 11-14). Audit + monitor continuously (Section 5).

❌ **Anti-Pattern:** "Privacy is a compliance checkbox; we'll add it post-launch; DPDP is scary so we'll go minimal." → Compliance becomes a crisis management exercise, not operational.

---

**Owner:** Legal, DPO | **Version:** 1.0 | **Last Updated:** April 2026
