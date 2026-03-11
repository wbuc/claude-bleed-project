# Privacy Policy Requirements Checklist — Bleed (UK App Store, iOS)

Research date: 2026-02-26

This checklist covers three layers of compliance: Apple's App Store Review Guidelines, UK GDPR / Data Protection Act 2018, and health-data-specific rules for period tracking apps. Each item is marked as **MANDATORY** (legally or contractually required) or **RECOMMENDED** (best practice / risk reduction).

---

## 1. APPLE APP STORE REVIEW GUIDELINES

### 1.1 Privacy Policy Presence (Guideline 5.1.1(i)) — MANDATORY

- [ ] Privacy policy URL entered in App Store Connect metadata field
- [ ] Privacy policy accessible within the app itself (not just on a website)
- [ ] Privacy policy is publicly accessible (not behind a login)

### 1.2 Privacy Policy Content (Guideline 5.1.1(i)) — MANDATORY

The policy must "clearly and explicitly" state:

- [ ] What data the app collects (or that it collects none)
- [ ] How the app collects that data
- [ ] All uses of that data
- [ ] Data retention and deletion policies
- [ ] How users can revoke consent and request deletion of their data
- [ ] Confirmation that any third party with whom data is shared provides equal or greater protection (applies to auth providers like Google/Apple Sign-In)

### 1.3 Privacy Nutrition Label (App Store Connect) — MANDATORY

Must declare all data types collected. For Bleed specifically:

- [ ] **Health** data type: Declare as "Data Not Collected" (since cycle data stays on-device and is never transmitted)
- [ ] **Contact Info > Email Address**: Declare as "Data Linked to You" / "App Functionality" (account registration)
- [ ] **Purchases > Purchase History**: Declare if donation records are stored server-side
- [ ] **Identifiers**: Declare as "Data Not Collected" (no device IDs, no user tracking)
- [ ] Confirm no third-party SDKs collect data you haven't declared (audit all dependencies)
- [ ] Declare tracking status: "This app does not track you" (if no ATT prompt needed)

### 1.4 Health & Fitness Data Rules (Guideline 5.1.3) — MANDATORY

- [ ] Health data is not used for advertising or marketing
- [ ] Health data is not used for "use-based data mining" (except improving health management with permission)
- [ ] Health data is not shared with third parties
- [ ] Health data is not written to iCloud (Guideline 5.1.3(ii) explicitly prohibits storing personal health info in iCloud)
- [ ] Disclose the specific health data being collected from the device (even if stored locally only)
- [ ] No false or inaccurate data written to HealthKit (if integrated)

### 1.5 Consent & Permissions (Guideline 5.1.1(ii)) — MANDATORY

- [ ] Explicit user consent obtained before any data collection (even if anonymous)
- [ ] Purpose strings (NSUsageDescription keys in Info.plist) clearly and completely describe why each permission is needed
- [ ] App functionality is not gated behind granting unnecessary data access
- [ ] Users can withdraw consent easily

### 1.6 Data Use & Sharing (Guideline 5.1.2) — MANDATORY

- [ ] Data collected for one purpose is not repurposed without further consent (5.1.2(ii))
- [ ] No surreptitious user profiling (5.1.2(iii))
- [ ] If sharing data with third-party AI services: explicit disclosure before transmission (5.1.2(i), updated Nov 2025)

### 1.7 Account Deletion (Guideline 5.1.1(v)) — MANDATORY

- [ ] If account creation is supported, account deletion must be available within the app
- [ ] Deletion must include all associated personal data on your servers

---

## 2. UK GDPR (Articles 13 & 14) + DATA PROTECTION ACT 2018

### 2.1 Controller Identity — MANDATORY

- [ ] Full legal name of the data controller (company/individual)
- [ ] Contact details of the data controller (postal address, email)
- [ ] Contact details of a representative in the UK (if controller is based outside the UK)
- [ ] Contact details of Data Protection Officer (if one is appointed -- see 2.6 below for whether you need one)

### 2.2 What You Collect and Why — MANDATORY

- [ ] Categories of personal data collected (be specific: "email address," "donation amount and date," not "personal information")
- [ ] Purpose for each category of data processing (e.g., "email address for account authentication," "donation records for accounting")
- [ ] Lawful basis for each processing activity under Article 6 (for Bleed: contractual necessity for email/auth, legitimate interest for donation records)
- [ ] If relying on legitimate interest: state the specific legitimate interest
- [ ] If relying on consent: state this, explain how to withdraw, and confirm withdrawal is as easy as giving consent

### 2.3 Data Sharing & Transfers — MANDATORY

- [ ] Categories of recipients or specific recipients of personal data (e.g., Google and Apple as authentication providers)
- [ ] Whether data is transferred outside the UK, and if so: which countries, what safeguards are in place (e.g., adequacy decisions, standard contractual clauses)
- [ ] If using sub-processors: name them or describe the categories

### 2.4 Retention — MANDATORY

- [ ] Specific retention period for each data type, OR the criteria used to determine retention
- [ ] For Bleed: retention period for email (as long as account is active + X days after deletion request), retention period for donation records (state the accounting period, e.g., 7 years for UK tax purposes)

### 2.5 Individual Rights — MANDATORY

Must explicitly list these rights and explain how to exercise them:

- [ ] Right of access (Subject Access Request / SAR)
- [ ] Right to rectification
- [ ] Right to erasure ("right to be forgotten")
- [ ] Right to restrict processing
- [ ] Right to data portability
- [ ] Right to object to processing
- [ ] Rights related to automated decision-making and profiling (state whether you use these; if not, say so)
- [ ] Right to withdraw consent (if consent is a lawful basis)
- [ ] Right to lodge a complaint with the ICO (Information Commissioner's Office), with a link: https://ico.org.uk/make-a-complaint/

### 2.6 Data Protection Officer (DPO) — CONDITIONAL

A DPO is mandatory if your core activities involve large-scale processing of special category data. For Bleed:

- [ ] Assess whether DPO is required. Since Bleed stores health data on-device only and the controller never processes it, a DPO is likely NOT required. Document this decision.
- [ ] If DPO appointed: include their contact details in the privacy policy

### 2.7 Statutory/Contractual Requirement Disclosure — MANDATORY

- [ ] State whether providing personal data is a statutory or contractual requirement
- [ ] State consequences of not providing the data (e.g., "If you don't provide an email address, you cannot create an account")

### 2.8 Automated Decision-Making — MANDATORY

- [ ] State whether automated decision-making or profiling is used
- [ ] If yes: meaningful information about the logic involved, significance, and envisaged consequences
- [ ] If no: state this explicitly

### 2.9 Format & Accessibility — MANDATORY

- [ ] Policy written in clear, plain language (not legalese)
- [ ] Policy concise and easily accessible (UK GDPR Article 12 requires "concise, transparent, intelligible and easily accessible form, using clear and plain language")
- [ ] Information provided free of charge
- [ ] If policy changes: users notified before changes take effect

---

## 3. HEALTH / PERIOD TRACKING APP — SPECIAL CATEGORY DATA RULES

### 3.1 Special Category Data Classification — MANDATORY

Period/cycle data IS special category data under UK GDPR Article 9, even if stored locally. Key requirements:

- [ ] Identify in the privacy policy that the app handles health data (special category data)
- [ ] State the Article 9 condition for processing. For Bleed, the strongest option is **explicit consent** (Article 9(2)(a)), since the user actively chooses to enter their cycle data
- [ ] State the Article 6 lawful basis alongside the Article 9 condition (these are two separate legal requirements that both must be met)

### 3.2 On-Device Processing Nuance

Bleed's architecture (all health data on-device, never transmitted) significantly reduces regulatory burden, but does NOT eliminate it:

- [ ] Clarify in the policy that health data is processed on-device only
- [ ] Clarify that the controller (Bleed) never has access to, collects, or stores health data
- [ ] Note: since the app provides the means for data entry and processing, you are still the controller of that processing from a GDPR perspective. The policy should address this transparently.

### 3.3 Data Protection Impact Assessment (DPIA) — MANDATORY (to assess); RECOMMENDED (to complete)

- [ ] Conduct a screening assessment to determine whether a full DPIA is required. Processing health data is one of the ICO's criteria that may trigger a DPIA, but on-device-only processing with no data transmission likely falls below the "large scale" threshold.
- [ ] Document the screening decision (even if you decide a full DPIA is not needed)
- [ ] If DPIA is completed, retain it as an internal document (does not go in the privacy policy, but the ICO can request it)

### 3.4 Appropriate Policy Document (DPA 2018 Schedule 1) — CONDITIONAL

- [ ] If relying on a Schedule 1 condition (substantial public interest, employment, etc.) for processing special category data, you MUST have an Appropriate Policy Document. For Bleed using explicit consent (Article 9(2)(a)), an APD is NOT required but is still recommended as good practice.
- [ ] If created, the APD must explain: the condition relied on, how you comply with the data protection principles, and your retention/deletion policies

### 3.5 Security Measures for Health Data — MANDATORY

- [ ] Describe the security measures protecting on-device health data (device encryption, app-level passcode/biometric lock)
- [ ] Describe server-side security for account data (encryption in transit and at rest)
- [ ] State that health data is encrypted at rest on the device (confirm this is technically true in the app's implementation)

### 3.6 Data Breach Notification — MANDATORY (internal process); RECOMMENDED (mention in policy)

- [ ] Internal process: If a breach of server-side data (emails, donation records) occurs, notify the ICO within 72 hours if it poses a risk to individuals
- [ ] Internal process: Notify affected individuals without undue delay if breach poses a high risk
- [ ] Policy mention: State that you will notify users of breaches affecting their data in accordance with applicable law

---

## 4. GAPS IN THE CURRENT BLEED PRIVACY POLICY

Comparing the existing policy (`output/legal/privacy-policy-updated.md`) against this checklist:

### Must Fix (MANDATORY items missing or incomplete)

1. **No controller identity.** Policy says "Bleed" but does not provide the full legal name, registered address, or company number. UK GDPR Article 13(1)(a) requires this.
2. **No ICO complaint right.** Section 10 mentions "data protection laws" but never names the ICO or provides the complaint mechanism. UK GDPR Article 13(2)(d) requires this.
3. **No explicit list of individual rights.** The policy mentions deletion but does not list the full set of rights (access, rectification, restriction, portability, objection). UK GDPR Article 13(2)(b) requires this.
4. **No Article 9 condition stated.** The policy does not acknowledge that cycle data is special category data or state the legal condition for processing it.
5. **No mention of automated decision-making.** Even a "we do not use automated decision-making" statement is required under Article 13(2)(f).
6. **Retention period for donations is "indefinitely."** UK GDPR requires a specific period or criteria. Change to a defined period (e.g., "7 years from the date of the transaction, in accordance with UK accounting requirements").
7. **No statutory/contractual requirement statement.** Article 13(2)(e) requires this.
8. **International transfers.** Section 10 is vague. If auth providers (Google/Apple) process data outside the UK, you must state where and what safeguards apply.
9. **App Store Nutrition Label.** Not a policy issue, but ensure the App Store Connect declarations match the policy exactly.
10. **Section 8 age limit is 18.** This is fine as a business decision, but note that the UK age of data protection consent is 13 (not 18). If you mean "we don't market to children," that's different from "we refuse service to under-18s." Clarify the legal basis for the age restriction.

### Should Fix (RECOMMENDED)

1. Add a layered notice approach: short summary at the top (already done, good), full detail below.
2. Add a "last reviewed" date alongside the "last updated" date.
3. Document the DPIA screening decision internally.
4. Consider adding a "How this policy applies to on-device data" section to be explicit about the on-device vs. server-side distinction.

---

## REFERENCES

- [Apple App Store Review Guidelines (Section 5.1)](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Privacy Details (Nutrition Labels)](https://developer.apple.com/app-store/app-privacy-details/)
- [Apple Health & Fitness Apps Privacy Overview (Sept 2025)](https://www.apple.com/privacy/docs/Health_Fitness_Apps_Privacy_September_2025.pdf)
- [ICO: What privacy information should we provide? (Articles 13 & 14)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/)
- [ICO: What are the rules on special category data?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/)
- [ICO: What are the conditions for processing special category data?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-conditions-for-processing/)
- [ICO: Data protection impact assessments](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/guide-to-accountability-and-governance/data-protection-impact-assessments/)
- [ICO: Appropriate policy document (special category data)](https://ico.org.uk/about-the-ico/our-information/safeguards-policy/policy-document-our-processing-of-special-categories-of-personal-data-and-criminal-offence-data/)
- [UK Data Protection Act 2018](https://www.legislation.gov.uk/ukpga/2018/12/contents/enacted)
- [Waterfront Law: UK GDPR Privacy Policy Guide](https://waterfront.law/uk-gdpr-privacy-policy-guide-key-requirements-for-websites-and-apps/)
- [SecurePrivacy: GDPR Compliance for Mobile Apps (2026 Guide)](https://secureprivacy.ai/blog/gdpr-compliance-mobile-apps)
- [Apple updated App Review Guidelines (Nov 2025) — third-party AI data sharing rules](https://techcrunch.com/2025/11/13/apples-new-app-review-guidelines-clamp-down-on-apps-sharing-personal-data-with-third-party-ai/)
- [UK Data Use and Access Act 2025 changes](https://www.dataprotectionreport.com/2025/07/uk-data-protection-reform-what-you-need-to-know-and-do/)
