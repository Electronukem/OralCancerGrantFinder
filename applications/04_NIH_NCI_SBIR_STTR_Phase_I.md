# NIH / NCI SBIR or STTR Phase I – Draft Application (Kon Pop Detection)

**Programme status:** SBIR/STTR authority lapsed 30 Sep 2025 and was **reauthorised through 30 Sep 2031** (Small Business Innovation and Economic Security Act of 2026, signed 13 Apr 2026). NIH is accepting applications again.
**Next standard due date:** **5 January 2027** (then 5 Apr and 5 Sep) **[CONFIRM in the NIH Guide]**
**Opportunity (found on Grants.gov, Oct 2026):**
- **PA-27-102**: NIH Small Business Technology Transfer Grant (Parent STTR [R41/R42], Clinical Trial Optional), listed close 5 Apr 2027 ← **recommended**
- **PA-27-100**: NIH, CDC and FDA Small Business Innovation Research Grant (Parent SBIR [R43/R44], Clinical Trial Optional), listed close 5 Apr 2027
- **PAR-27-039 / PAR-27-040**: Small Business Transition Grant for New Entrepreneurs (R43/R44 and R41/R42). Check whether an early-career founder qualifies **[CONFIRM eligibility]**
- Also check NCI-specific SBIR topics/contracts (seed.nih.gov, NCI SBIR Development Center)
**Phase I budget guideline:** about US$300k total costs **[CONFIRM the current SBA guideline amount and NCI's limits]**; ~6–12 months
**New 2026 rules:** each small business may submit **at most 9 SBIR/STTR applications per fiscal year** to HHS; expanded **foreign-ties disclosure** and due diligence (NOT-OD-26-073/-074/-075) **[CONFIRM]**

---

## ⚠️ Eligibility gate – answer these BEFORE writing
| Requirement | KPD status | OK? |
|---|---|---|
| For-profit small business, ≤ 500 employees, **place of business in the US** | [FILL: where is KPD incorporated?] | ☐ |
| **> 50% owned and controlled by US citizens or permanent residents** (or a permitted structure) | [FILL: ownership by citizenship] | ☐ |
| Registered in SAM.gov (UEI), SBA Company Registry (SBC Control ID), Grants.gov, eRA Commons | [FILL] | ☐ |
| **SBIR:** PI's **primary employment (> 50%)** is with KPD at the time of award. A full-time Harvard student may not qualify; consider **Amir Fleurizard (CTO)** as PI if employed > 50% | [FILL] | ☐ |
| **STTR alternative:** partner with a **US research institution** (Harvard, MIT, or the University of Michigan). KPD does ≥ 40% of the work and the institution ≥ 30%. The **PI may be employed by the research institution** | [FILL: which institution and PI] | ☐ |
| **Work performed in the US.** SBIR/STTR-funded R&D must normally be performed in the US; foreign performance requires strong justification and agency approval | Plan: fund **US-based** model development, software and analysis with NIH; fund **Thai field data collection and the pilot through Thai grants** (HSRI/NRCT/PMU) | ☐ |
| Disclose all foreign affiliations and support (e.g. Mahidol collaboration, Thai hospital data agreements) | | ☐ |

> **Recommendation:** apply as an **STTR (R41) with the University of Michigan, Harvard, or MIT** as the research institution, with a faculty PI or multi-PI. US-based technical aims are funded by NIH; Thai partners supply de-identified images under a data-use agreement, with their collection funded separately. Email the **NCI SBIR Development Center** programme director with a 1-page summary before writing.

> **NIH and AI-written applications:** NIH does not consider applications "substantially developed by AI" to be the applicants' original ideas (NOT-OD-25-132). Use this as a structure and rewrite the science yourselves.

---

## Project title
Robust AI triage of oral potentially malignant and malignant lesions from community-acquired smartphone images

## Project Summary/Abstract (≤ 30 lines) – draft
Oral cancer causes ~177,000 deaths annually, concentrated in South and Southeast Asia and in underserved populations with tobacco, alcohol and areca-nut exposure, including immigrant communities in the US. Survival depends on early detection, yet screening in low-resource and primary-care settings relies on unaided visual inspection by non-specialists, which has variable accuracy. Kon Pop Detection (KPD) has developed a mobile app and clinician dashboard that use a fine-tuned medical foundation model (MedGemma) and a lesion detector (YOLO) to triage intraoral photographs taken by non-specialists. Before clinical deployment, the key technical risk is **robustness**: performance must hold across low-cost devices, variable lighting, image quality and patient subgroups. In this Phase I project we will (Aim 1) build a quality-controlled, multi-site, biopsy-referenced image dataset and an automated image-quality assessment model; (Aim 2) develop and benchmark robust risk-stratification models with calibrated, explainable outputs; and (Aim 3) conduct a reader study comparing non-specialist accuracy with and without AI assistance. Success criteria: [FILL: e.g. AUC ≥ 0.__, sensitivity ≥ __% at specificity ≥ __% on external test data; ≤ __-point AUC drop across device/lighting strata; ≥ __% improvement in non-specialist sensitivity with AI]. Phase II will conduct prospective multi-site clinical validation and prepare a regulatory submission.

## Project Narrative (3 sentences)
Oral cancer is often found too late because primary-care and community screeners lack tools to recognise high-risk lesions. This project develops an AI tool that helps non-specialists photograph the mouth and identify which patients need urgent specialist review. It could make early detection of oral cancer cheaper and more accessible for underserved populations in the US and worldwide.

---

## Specific Aims (1 page) – draft
**Opening.** Oral cancer is highly curable when detected early, but most patients in high-burden, low-resource settings are diagnosed at late stage. Screening by non-specialists can reduce mortality, but its accuracy varies widely with training. AI image analysis could standardise screening, but current models are trained mostly on specialist-acquired hospital images and degrade on low-cost devices and variable field conditions.

**Long-term goal:** a validated, low-cost, regulatory-cleared AI triage tool for oral cancer screening in primary-care and community settings.
**Phase I objective:** demonstrate the technical feasibility of robust, calibrated AI triage on community-acquired smartphone images.

**Aim 1. Build a quality-controlled, biopsy-referenced dataset and an automated image-quality gate.**
Harmonise [FILL: N] de-identified intraoral images from [FILL: sources] with histopathology or expert-panel reference labels; develop an image-quality classifier that rejects unusable photos at capture.
*Milestone:* ≥ [FILL] labelled images; quality-gate AUC ≥ [FILL].

**Aim 2. Develop and benchmark robust risk-stratification models.**
Fine-tune MedGemma and train a YOLO lesion detector; compare against baseline CNNs; apply domain-robustness methods (augmentation for lighting and device; site-held-out validation); calibrate risk scores; generate lesion-localisation explanations.
*Milestone:* external (site-held-out) AUC ≥ [FILL]; sensitivity ≥ [FILL]% at specificity ≥ [FILL]%; calibration slope 0.9–1.1; performance reported by sex, age, device and lighting.

**Aim 3. Reader study of AI-assisted non-specialist triage.**
[FILL: N] non-specialist readers (e.g. community health workers, dental hygienists, general practitioners) classify [FILL: N] cases with and without AI assistance.
*Milestone:* AI assistance improves reader sensitivity by ≥ [FILL] percentage points without reducing specificity by more than [FILL].

**Expected outcome:** a technically de-risked model and software ready for prospective clinical validation in Phase II.

---

## Research Strategy (6 pages): outline with key content
**Significance (~1 page):** burden; failure of unaided visual screening; limitations of hospital-trained AI; relevance to US underserved populations (e.g. South/Southeast Asian immigrant communities who use areca nut; rural primary care) and to NCI global oncology priorities.
**Innovation (~½ page):** foundation-model fine-tuning for oral lesions; robustness to community acquisition; quality gate at point of capture; triage design for non-specialists.
**Approach (~4.5 pages):**
- Preliminary data: [FILL: dataset, current metrics, MVP screenshots, ethics, hospital agreements]
- Aim 1–3 methods, statistics (sample-size justification for AUC/sensitivity CIs; reader-study design and analysis, e.g. multi-reader multi-case analysis), go/no-go criteria
- Rigour: pre-registered analysis plan; site-held-out test set locked before final evaluation; TRIPOD+AI and STARD reporting
- Potential problems and alternatives
- Timeline (Gantt)
- Human subjects: de-identified secondary data → possibly exempt or "not human subjects research" **[CONFIRM with IRB]**; reader study needs consent from readers

## Other components
- **Biosketches** (SciENcv Common Form) for PI(s) and key personnel
- **Letters of support:** research institution (STTR); Thai data providers (data-use agreement); clinical advisors; potential customers (letters of interest)
- **Facilities & Other Resources:** KPD (US office, compute); research institution
- **Budget:** KPD and research-institution shares meeting STTR percentages; cloud compute; reader honoraria; **no foreign performance** unless approved
- **Data Management & Sharing Plan:** de-identified data under controlled access respecting Thai PDPA and data-use agreements; model card
- **SBIR/STTR Information form; SBA Company Registry certificate; foreign-disclosure items**
- **Phase II only:** Commercialisation Plan (12 pages)

## Commercialisation potential (short paragraph for the Significance section)
Initial market: public screening programmes in Thailand (Ministry of Public Health / NHSO) and other South and Southeast Asian health systems. US opportunity: dental and primary-care practices and federally qualified health centres serving high-risk populations; teledentistry platforms. Revenue: SaaS per screen or per site. Regulatory path: Thai FDA (Software as a Medical Device); US FDA strategy to be determined in Phase II (e.g. De Novo or 510(k), depending on predicates) **[FILL/CONFIRM]**.
