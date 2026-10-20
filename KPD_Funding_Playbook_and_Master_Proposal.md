<!-- toc -->

<!-- pagebreak -->

# 1. How to use this document

This document brings together everything prepared so far for funding Kon Pop Detection (KPD): which grants fit, when they close, who should apply, what every proposal must contain, a **master proposal** you can adapt for any funder, and the supporting information reviewers expect (evidence, ethics, regulation, budget, registrations).

**Three rules for using it:**
1. **[FILL] means a fact only your team knows.** Nothing in this document invents data, results, names or amounts. Replace every [FILL] with real, checkable information.
2. **[CONFIRM] means a detail that changes between funding rounds** (deadline, budget cap, eligibility). Always check the official call document before submitting.
3. **Rewrite in your own voice.** MIT Solve advises against AI-written applications and asks you to certify that nothing is exaggerated. NIH does not consider applications "substantially developed by AI" to be original. Use this as raw material and structure, not final text.

**Companion files** (in `C:\Users\joyld\OralCancerGrantFinder\`):
| Folder / file | What it contains |
|---|---|
| `applications\` | Funder-specific draft applications (MIT Solve, Harvard PIC, NIH STTR/SBIR, NSF, HSRI, NRCT, PMU-C, ThaiHealth, cloud credits, NIH R21, concept note, your pandemic-preparedness draft) + Word copies |
| `templates\` | Generic fill-in templates for 21 funders + Common Information Pack |
| `find_grants.py` | Re-runs the live grant search (Grants.gov + NIH RePORTER) and produces an HTML report |
| `check_limits.py` | Checks your answers against word/character limits |

<!-- pagebreak -->

# 2. Executive summary

**The project.** Kon Pop Detection is an AI-assisted oral cancer screening tool for underserved communities. Village health volunteers (อสม.) use a smartphone app to record risk factors and take three standardised photos of the mouth. A fine-tuned Google MedGemma model and a YOLO lesion detector score the risk and mark suspicious areas, and hospital dentists triage patients from a ranked dashboard. The pilot is in **Health Region 10, northeast Thailand** (~300 volunteers, 3–4 partner hospitals), with planned expansion to Health Regions 7 and 9.

**The funding strategy in one sentence.** Use fast, non-dilutive startup awards and cloud credits now; fund **validation and implementation research through Thai funders with Mahidol University as the lead applicant**; fund **US-based technical R&D through NIH/NSF small-business grants**; then move to government contracts once the pilot proves accuracy and cost savings.

**Top 7 actions (October–December 2026):**
| # | Action | By |
|---|---|---|
| 1 | Finish, rewrite and submit **MIT Solve** (draft ready) + record a 2-minute video | **2 Nov 2026, 12:00 noon US Eastern** (= 00:00, 3 Nov, Thailand) |
| 2 | Apply for **startup cloud credits** (Google for Startups first, since you build on MedGemma) | This week |
| 3 | Decide **where KPD is incorporated and who owns it** (determines NIH/NSF and Thai startup eligibility) | This week |
| 4 | Start **SAM.gov/UEI, Grants.gov, eRA Commons** registrations and pick a US university partner for an **NIH STTR** | Now (takes 2–3 months); application ~5 Jan 2027 |
| 5 | Dr. Wareekul: register in **NRIIS**; ask Mahidol's research office about the **TSRI Fundamental Fund** internal call and the **NRCT/HSRI** FY2571 calls | October 2026 |
| 6 | Prepare **Harvard President's Innovation Challenge** application | ~early Dec 2026 [CONFIRM] |
| 7 | Collect the **facts list** (Section 16) and letters of support (Section 13) | Ongoing; needed by every funder |

<!-- pagebreak -->

# 3. Project at a glance

| Item | Current information |
|---|---|
| Organisation | Kon Pop Detection (KPD) [FILL: legal name, country/state of incorporation, date] |
| Origin | Team formed at MIT Hacking Medicine Grand Hack 2025; won [FILL: exact Google award name/amount]; company founded November 2025 [CONFIRM] |
| Support | Harvard Global Alliance for Medical Innovation (GAMI) incubator; collaborations with MIT, University of Michigan [FILL: roles], Mahidol University |
| Team | **Ernest Choi**, CEO (Harvard graduate student, three-time founder) · **Dr. Narawitchz Wareekul**, CMO (dentist, Mahidol University) · **Amir Fleurizard**, CTO (M.Sc. UNC Charlotte, full-stack engineer) |
| Product | Volunteer app (login, patient registration, digital risk survey for smoking/alcohol/betel, guided 3-photo capture) → AI (fine-tuned **MedGemma** + **YOLO**) → dentist dashboard ranking patients by risk; training game; picture-based manual |
| Pilot site | Health Region 10 (เขตสุขภาพที่ 10): Ubon Ratchathani, Sisaket, Yasothon, Amnat Charoen, Mukdahan |
| Partner hospitals | [FILL: names; deck says 3 regional hospitals; earlier "4 including Huathahan". Likely **Hua Taphan Hospital (โรงพยาบาลหัวตะพาน), Amnat Charoen**. CONFIRM] |
| Volunteers | ~300 to be trained; 20 lead trainers cascade training to the rest |
| Ethics | Approved [FILL: committee, number, date] |
| Status | MVP validated [FILL: metrics]; mini-pilots completed [FILL: numbers]; mass pilot launch planned 2026 Q3 [FILL: actual status] |
| Dataset | [FILL: number of images, sources, labels, biopsy-confirmed cases] |
| Model performance | [FILL: sensitivity, specificity, AUC, test-set size, reference standard] |
| Business model | B2G/B2B software-as-a-service: hospitals, Health Region offices, MOPH, NHSO, insurers; free for volunteers and patients |
| Market (deck) | TAM US$2.4B · SAM US$1.1B · SOM US$75M [FILL: show how these were calculated] |
| Funding raised | [FILL] |

<!-- pagebreak -->

# 4. Funding strategy

## 4.1 Who should apply for what
Different funders accept different applicants. Use three applicant "routes":

| Route | Lead applicant | Use for | Why |
|---|---|---|---|
| **A. Startup** | KPD (the company) | MIT Solve, Harvard PIC, cloud credits, NIH/NSF SBIR, Google programmes, investors | These fund companies and founders |
| **B. Thai academic** | **Mahidol University (PI: Dr. Wareekul)**, with KPD as technology partner and hospitals as sites | NRCT, HSRI, TSRI Fundamental Fund, PMU-C (KPD as co-funding industry partner), ThaiHealth, e-ASIA, ISPF, JST NEXUS, AI4PEP-style calls | Thai public funders fund Thai institutions; many international calls require a Global-South university PI |
| **C. US academic** | A US university (University of Michigan / Harvard / MIT) | NIH STTR (with KPD), NIH R21, Wellcome-type collaborations | NIH STTR requires a research institution partner; US universities can carry NIH R-grants |

## 4.2 Split the project so funders don't overlap
Funders check for double funding. Give each funder a distinct piece of the work and declare related applications honestly.

| Work package | Best-fit funders |
|---|---|
| **WP1 Technical R&D:** robustness to devices and lighting, image-quality gate, calibration, on-device model, reader study | NIH STTR/SBIR, NSF SBIR, cloud credits, NRCT (Thai validation) |
| **WP2 Multi-site clinical validation:** dataset, biopsy reference, external validation | NRCT, TSRI Fundamental Fund, NIH STTR (US-based analysis) |
| **WP3 Implementation pilot in Health Region 10:** volunteers, referral pathway, usability | HSRI, MIT Solve, Harvard PIC, ThaiHealth (community parts), Rotary |
| **WP4 Health economics & policy:** cost per screen, cost-effectiveness, budget impact, NHSO/MOPH engagement | HSRI, NIH R21 (academic) |
| **WP5 Productisation & regulation:** QMS, Thai FDA, commercial deployment | PMU-C, TCELS (later), investors |
| **WP6 Community prevention:** betel/tobacco/alcohol risk reduction, volunteer capacity | ThaiHealth, Rotary |
| **WP7 Training & capacity:** fellowships, exchange | UICC, IARC, e-ASIA |

## 4.3 Staged plan
| Stage | Period | Goal | Main funding |
|---|---|---|---|
| 1. Prove it works | Oct 2026 – mid 2027 | Pilot results, validation numbers, first publications | Solve, PIC, cloud credits, TSRI FF, NIH STTR Phase I |
| 2. Prove it's worth paying for | mid 2027 – 2028 | Cost-effectiveness, multi-region implementation, Thai FDA submission | HSRI, NRCT, PMU-C, NIH STTR Phase II |
| 3. Scale | 2028+ | Government contracts (MOPH/NHSO), regional expansion | Contracts, investment, TCELS, regional partners |

<!-- pagebreak -->

# 5. Funding calendar (October 2026 – June 2027)

| Date | Funder / event | Action | Status |
|---|---|---|---|
| Now (rolling) | Google for Startups / AWS Activate / Microsoft for Startups / NVIDIA Inception | Apply for credits | Draft ready (applications/10) |
| Now | SAM.gov / UEI / Grants.gov / eRA Commons; NRIIS | Start registrations | Start immediately |
| 26 Oct 2026 | MIT Solve online application clinic | Attend; ask questions | Register on Solve's events page |
| **2 Nov 2026, 12:00 ET** | **MIT Solve 2027 Global Health Challenge** | Submit | Draft ready (applications/01) |
| 4 Nov 2026 | NSF SBIR/STTR solicitation 26-511 (listed close date) | Check fit: this round emphasises scientific instrumentation | Draft pitch (applications/05) |
| Oct 2026 – Jan 2027 | TSRI Fundamental Fund (Mahidol internal call) | Ask Mahidol research office | [CONFIRM] |
| Nov 2026 – Apr 2027 | NRCT FY2571 calls | Submit via NRIIS | Draft (applications/07) |
| ~Early Dec 2026 | Harvard President's Innovation Challenge | Submit | Draft (applications/03) [CONFIRM date] |
| **~5 Jan 2027** | **NIH STTR PA-27-102 / SBIR PA-27-100** | Submit (needs completed registrations) | Draft (applications/04) [CONFIRM] |
| Feb 2027 | MIT Solve finalists notified; Zoom pitch | Prepare pitch | |
| 16 Feb 2027 | NIH R21 PA-25-253 (academic-led) | Submit if a university leads | Draft aims (applications/11) |
| Feb – Apr 2027 | HSRI FY2571 call | Submit via NRIIS | Draft (applications/06) [CONFIRM] |
| Annual | PMU-C / PMU-B calls | Submit with KPD co-funding | Draft (applications/08) [CONFIRM] |
| Open grant | ThaiHealth | Submit via Thai partner | Draft (applications/09) [CONFIRM] |
| 14–15 Apr 2027 | MIT Solve Solver Orientation (if selected) | Team lead attends in Cambridge, MA | |
| 11 Jun 2027 | NIH ITCR U01 (RFA-CA-27-019) | Only if reframed as an open research tool | Low fit |

<!-- pagebreak -->

# 6. Funder directory (ranked for KPD)

Fit ratings consider eligibility, topic match, competition and timing. Amounts and dates are from official pages or recent cycles; **[CONFIRM]** before applying.

## 6.1 Tier A: apply now (highest likelihood)

**MIT Solve 2027 Global Health Challenge** (route A)
- **What:** US$10,000 Solver grant + 9-month support programme + eligibility for sponsor prizes (AI for Humanity Prize up to US$150,000; Crescent Enterprises AI for Social Innovation Prize up to US$100,000). Average Solver funding ~US$40k.
- **Fit:** Strong. The "Expand quality primary care … by supporting frontline health workers" dimension matches the volunteer model. Must be at least Prototype stage (no concept-stage solutions).
- **Deadline:** 2 Nov 2026, 12:00 noon ET.
- **Submit:** online form (about 20 questions, 100–300 words each), optional 2-minute public video. File: applications/01.

**Startup cloud and compute programmes** (route A)
- **What:** cloud credits and technical support. Google for Startups Cloud Program (strongest story, since KPD uses MedGemma), AWS Activate, Microsoft for Startups, NVIDIA Inception (membership benefits, not cash). NVIDIA's academic GPU grant programme was closed as of Oct 2026.
- **Fit:** High likelihood, rolling. File: applications/10.

**Harvard President's Innovation Challenge** (route A)
- **What:** non-dilutive prizes (2025 pool ~US$517k), Health Care + Life Sciences track.
- **Eligibility:** team must include a current Harvard student (Ernest Choi).
- **Deadline:** 2026 cycle closed 8 Dec 2025, so expect early Dec 2026 [CONFIRM]. File: applications/03.

**NIH STTR (PA-27-102) / SBIR (PA-27-100) Phase I** (routes A + C)
- **What:** about US$300k Phase I [CONFIRM]. SBIR/STTR was reauthorised on 13 Apr 2026 through 2031.
- **Eligibility:** US small business, >50% owned by US citizens/permanent residents. R&D normally performed in the US. SBIR: PI primarily employed (>50%) by KPD. **STTR recommended:** partner with a US university; the PI can be university faculty.
- **New rules:** max 9 SBIR/STTR applications per company per fiscal year (HHS); expanded foreign-ties disclosure.
- **Next date:** ~5 Jan 2027. File: applications/04.

**HSRI (สวรส.)** (route B)
- **What:** Thai health-systems research funding.
- **Fit:** Excellent for the Health Region 10 implementation and cost-effectiveness work. Use the **health-systems** proposal form.
- **When:** annual call around Feb–Apr (the FY2569 call ran 17 Feb–30 Apr 2025) [CONFIRM FY2571]. File: applications/06.

**NRCT (วช.)** (route B)
- **What:** Thailand's main research funder.
- **Fit:** technical and clinical validation (dataset, external validation, reader study). Submit via NRIIS in Thai. File: applications/07.

**TSRI Fundamental Fund** (route B, via Mahidol)
- **What:** seed funding, usually one year at a time, competed internally at Mahidol.
- **Fit:** good for pilot data that strengthens every other application. Ask Mahidol's research office now. Template: templates/05.

## 6.2 Tier B: strong options with preparation

| Funder | Route | Why / conditions | File |
|---|---|---|---|
| **PMU-C (บพข.)** | B + KPD as co-funding partner | Product and regulatory path to market; usually needs private co-funding; may require a Thai-registered company [CONFIRM] | applications/08 |
| **ThaiHealth (สสส.)** | B (Thai organisation) | Community prevention (betel/tobacco/alcohol) + volunteer capacity; not AI R&D | applications/09 |
| **NSF SBIR/STTR** | A | Technical-risk R&D only; current solicitation 26-511 emphasises scientific instrumentation [CONFIRM fit] | applications/05 |
| **NIH R21 PA-25-253** | C | Up to US$275k direct over 2 years; foreign organisations eligible. **Must study screening delivery; developing diagnostic technology is non-responsive** | applications/11 |
| **Google.org / Google for Startups Accelerator** | A | MedGemma use-case in low-resource settings; occasional calls | applications/12 |
| **Rotary Foundation Global Grant** | Rotary clubs | Disease prevention; needs a Thai club + an international club as sponsors | applications/12 |
| **UICC fellowships** | Individual | Training/exchange for a team member | templates/08 |
| **IARC (WHO)** | Collaboration | Scientific credibility; oral cancer screening expertise in Asia | templates/16 |
| **National Cancer Institute of Thailand** | Partnership | Letter of support, registry data, policy route | templates/09 |

## 6.3 Tier C: later or conditional

| Funder | Condition |
|---|---|
| **TCELS** | Funds TRL 5–9 medical devices; after validation; likely needs a Thai entity |
| **depa / NIA** | Thai digital/innovation startup grants; likely need a Thai-registered company |
| **NHSO (สปสช.)** | A buyer and policy partner, not a grant; approach with cost-effectiveness results |
| **e-ASIA JRP** | Needs partners in 3+ member countries; each funded by its own agency |
| **UK ISPF (British Council + NRCT)** | No confirmed 2026 Thailand round; watch for calls |
| **JST ASPIRE / NEXUS (Japan–Thailand)** | 2026 Thailand guideline published; needs a Japanese partner; check whether health/AI topics qualify |
| **NRCT–NSFC (Thailand–China)** | Needs a Chinese partner |
| **Wellcome** | Discovery-research framing; host must be eligible; best after pilot data |
| **NIH IMAT R61/R33** | Only if you build a **new imaging device**; software/ML-focused projects are excluded |
| **NIH ITCR U01** | Only as an open tool for researchers; data collection ≤15% of budget |
| **NIH PAR-25-167 / PAR-25-081 (reissues)** | Later-stage clinical trials (pragmatic screening trial; Phase II diagnostic trial) |
| **NIH secondary-data PARs (reissue of PAR-25-095/096)** | If you have large archived image datasets with outcomes |
| **AMED / KHIDI** | Need a Japanese or Korean lead institution |
| **Temasek Foundation, Gates Grand Challenges, Cancer Grand Challenges, Pfizer** | Only when a call matches |

## 6.4 Not a good fit (skip)
- **NIH PRIMED-AI, SPOREs, Cancer Center Support Grants:** US cancer-centre or consortium programmes.
- **ASCO IDEA:** for early-career oncologists (probably not dentists) [CONFIRM].
- **AI4PEP / IDRC:** infectious-disease focus; last open call 2023. Your draft form matches this format; use it only if a current call accepts continuity-of-care framing.
- **CDC state cancer programmes:** US states and tribes only.

<!-- pagebreak -->

# 7. What every proposal must contain

## 7.1 Core anatomy (almost every funder)
| Section | What reviewers look for | Typical length |
|---|---|---|
| **Title** | Specific: who, what, where | ≤ 200 characters |
| **Summary / abstract / lay summary** | Problem, solution, aims, expected impact in plain language | 150–300 words |
| **Problem & significance** | Burden with cited numbers; the specific gap; why it matters to *this* funder | 0.5–2 pages |
| **Objectives / specific aims** | 2–4 measurable aims with success criteria | 1 page |
| **Innovation** | What is new compared with current practice and competitors | 0.5 page |
| **Preliminary work / track record** | Evidence you can deliver: data, prototype, results, ethics, partners | 0.5–1 page |
| **Methods / approach** | Design, setting, participants, sample size, procedures, analysis, rigour | 2–6 pages |
| **Implementation & management** | Roles, governance, timeline, milestones, risks and mitigation | 1 page |
| **Ethics & data protection** | Approvals, consent, privacy, AI safety, conflicts of interest | 0.5–1 page |
| **Gender, equity & inclusion** | Disaggregated analysis; who benefits; team diversity | 0.5 page |
| **Outputs, outcomes, impact** | Measurable products and changes; who uses results | 0.5 page |
| **Dissemination & uptake** | Publications, policy briefs, stakeholder engagement | 0.5 page |
| **Sustainability / scale / business model** | How it continues after the grant | 0.5 page |
| **Budget & justification** | Itemised; matches the work plan; follows funder rules | Form |
| **Team & CVs** | Right expertise for each aim; no gaps | Form |
| **Letters of support** | Commitment from hospitals, partners, users | Attachments |
| **References** | Recent, accurate, verifiable | As needed |

## 7.2 How sections differ by funder type
| | NIH (R21/STTR) | Thai (NRIIS: NRCT/HSRI/PMU) | Startup awards (Solve/PIC) | Foundations |
|---|---|---|---|---|
| Language | English | **Thai** (+ English title/abstract) | English | English |
| Core document | 1-page Specific Aims + Research Strategy (6 pages for R21/Phase I) | Online NRIIS fields + funder form | Short answers (100–300 words) + video | Concept note → full proposal |
| What wins | Rigour, feasibility, significance, team | National impact, outputs/outcomes/impact, TRL/SRL, alignment with national plans | Founder story, user engagement, traction, scalability | Fit with funder mission, impact per dollar |
| Special items | Foreign justification; Data Management & Sharing Plan; human-subjects forms; SciENcv biosketches | TRL/SRL; OKR alignment; institution certification; Thai budget categories | Stage of development; business model; theory of change | Theory of change; M&E plan |
| Budget rules | Foreign indirect costs ≤ 8%; detailed budget for foreign orgs | ค่าตอบแทน/ค่าจ้าง/ค่าวัสดุ/ค่าใช้สอย/ค่าครุภัณฑ์ + overhead | Use of funds | Often overhead caps |

## 7.3 Writing tips that raise scores
- **Lead with one number that matters** (e.g. late-stage % in Region 10) and one sentence on the gap.
- **Make every aim measurable:** "sensitivity ≥ 85% (95% CI lower bound ≥ 75%) for high-risk lesions vs biopsy" beats "high accuracy".
- **Show you listened to users:** e.g. picture-based manual because of language; cascade training through 20 lead volunteers.
- **Name the people who will use your results** (Health Region 10 office, NHSO) and include their letters.
- **Be honest about stage.** Solve and other judges penalise exaggeration; NIH reviewers check claims.
- **Address the obvious weaknesses yourself:** dataset size, reference standard, bias, regulation, who pays.
- **Mirror the funder's language** (their programme names, criteria and priorities).

<!-- pagebreak -->

# 8. Master proposal (adapt for any funder)

> This is a complete, funder-neutral proposal. Cut, reorder and translate it to fit each form. Section numbers match Section 7.1.

## 8.1 Title
**Kon Pop Detection: AI-Assisted Oral Cancer Screening by Village Health Volunteers in Health Region 10, Thailand: Validation, Implementation and Cost-Effectiveness**

## 8.2 Lay summary
Oral cancer is a serious and often deadly disease that disproportionately affects people in parts of Asia where betel quid (areca nut) chewing, smoking and alcohol use are common. It is usually curable when found early, but many patients are diagnosed late, when treatment is harder, costlier and less successful. In rural Thailand, screening is done by village health volunteers who receive about one day of training and record findings on paper.

Kon Pop Detection gives volunteers a smartphone app to take three standard photos of the mouth. An artificial-intelligence model highlights suspicious areas and estimates risk, and hospital dentists review the results remotely, seeing the highest-risk patients first. This project will test how accurate the tool is, whether volunteers and dentists can use it in everyday practice, and whether it saves money for patients and the health system compared with current screening.

## 8.3 Problem and significance
- **Global burden:** oral cancer causes about 177,000 deaths a year; Asia accounts for roughly two-thirds of cases [1, 2]. A large share in South and Southeast Asia is attributable to smokeless tobacco and areca nut [3].
- **Late diagnosis drives deaths and costs:** early-stage disease is highly curable. In Malaysian public hospitals, annual treatment cost per patient was about US$2,027 for late-stage vs US$394 for early-stage disease, nearly five-fold [5].
- **Screening by non-specialists works but varies:** a cluster-randomised trial in Kerala, India showed visual oral screening by trained health workers reduced oral cancer mortality among tobacco and/or alcohol users [7]. Accuracy of clinical visual examination nonetheless varies widely with examiner training [6].
- **Thailand's current model:** adults aged 40+ are screened by village health volunteers using a paper risk questionnaire (tobacco, alcohol, betel quid, ill-fitting dentures) and visual inspection, after about one day of training. Those with risk factors are referred to a doctor, dentist or dental nurse. Dentists are scarce in the northeast [FILL: dentist-to-population ratio], paper records are slow, and referrals are not prioritised.
- **Thailand and Health Region 10 data:** [FILL: GLOBOCAN 2022 Thailand incidence and mortality; % late-stage at partner hospitals; prevalence of betel chewing/smoking/drinking in Region 10].
- **Two costly failure modes:** missed high-risk lesions that progress, and unnecessary referrals that overload dentists and cost patients travel and lost wages.

## 8.4 Objectives
**General objective:** improve early detection of oral cancer and high-risk oral potentially malignant disorders (OPMDs) in underserved communities, using a low-cost AI-assisted screening tool operated by village health volunteers.

**Aim 1: Validate the AI model on community-acquired images.**
Build a multi-site dataset with reference-standard labels and validate the model internally and externally.
*Success criteria:* sensitivity ≥ [FILL]% and specificity ≥ [FILL]% for high-risk lesions vs dentist examination and biopsy; calibrated risk scores; performance reported by site, device, lighting, sex and age.

**Aim 2: Implement and evaluate the tool in Health Region 10.**
Train ~300 volunteers (20 lead trainers) and deploy for 6 months with [FILL] hospitals.
*Success criteria:* ≥ [FILL]% of photos meet quality standards; usability (SUS) ≥ [FILL]; referral completion ≥ [FILL]%; time from screen to dentist review ≤ [FILL] days.

**Aim 3: Quantify economic and health-system impact.**
Estimate cost per screen, cost per high-risk case appropriately referred, unnecessary referrals avoided, and cost-effectiveness against paper-based screening, from health-system and patient perspectives.

**Cross-cutting:** gender and equity analysis; continuity of screening during service disruptions (e.g. outbreaks).

**Hypothesis:** a low-cost, point-of-care AI tool integrated into existing volunteer screening will increase detection of high-risk lesions, reduce per-case screening, referral and treatment costs, and shorten time to diagnostic confirmation compared with visual inspection alone.

## 8.5 Innovation
1. **Designed for community conditions:** trained and validated on images from low-cost phones and variable lighting, not only hospital images.
2. **Upgrades the existing national volunteer programme** instead of creating a parallel one; the app replaces the paper form volunteers already use.
3. **Foundation-model approach** (fine-tuned MedGemma) to learn from limited local data, plus **lesion localisation** (YOLO) so users can see what the AI flagged.
4. **Point-of-capture image-quality checks** [CONFIRM built/planned] so dentists receive usable images.
5. **Triage dashboard** that ranks patients by risk for scarce dentists.
6. **Training game and picture-based manual** that make short training more effective.

## 8.6 Preliminary work
- App, dashboard and model built; MVP validated [FILL: how and with what results]
- Dataset: [FILL]
- Mini-pilots: [FILL: people screened; outcomes; the early-detection case described factually]
- Ethics approval: [FILL]
- Hospital approvals: [FILL]
- Recognition: MIT Grand Hack 2025 [FILL: Google award]; Harvard GAMI incubator

## 8.7 Methods
**Design.** Multi-site diagnostic accuracy study (Aim 1), embedded in a mixed-methods implementation study (Aim 2) with an economic evaluation (Aim 3).

**Setting.** Health Region 10: [FILL: provinces/districts], partner hospitals [FILL], their sub-district health promoting hospitals (รพ.สต.) and village volunteer networks.

**Participants.** Adults aged ≥ 40 attending community screening (inclusion: consent; exclusion: [FILL]); ~300 volunteers; dentists and dental nurses at partner hospitals.

**Screening procedure.**
1. Volunteer registers the participant and completes the digital risk survey.
2. Takes three standardised intraoral photos per protocol [FILL: views].
3. The app checks image quality.
4. AI generates a risk score and lesion box.
5. A dentist reviews on the dashboard.
6. High-risk participants are referred for examination and biopsy when indicated.
7. Referral completion is tracked.

**Reference standard.** Clinical examination by a dentist blinded to the AI result; histopathology for biopsied lesions; for screen-negatives, a random sample [FILL: %] examined by a dentist to estimate false negatives (avoids verification bias).

**AI development.** Fine-tune MedGemma for risk classification; YOLO detector for localisation; image-quality classifier. Patient-level train/validation/test splits; **external test on a hospital not used in training**; calibration; subgroup analysis; model card.

**Sample size (illustrative, using the Buderer formula).**
To estimate sensitivity of 85% ± 10% (95% CI) when [FILL: e.g. 5%] of screened people have a high-risk lesion:
n = 1.96² × 0.85 × 0.15 ÷ (0.10² × 0.05) ≈ 980 people screened (≈ 49 with high-risk lesions).
Replace the prevalence with local data; a tighter margin or lower prevalence needs more participants.
Your projection (150 volunteers × 15–20 people/day over 3–4 weeks ≈ 90,000 screens) is far above this, so the binding constraint is **reference-standard confirmation** of positives and a sample of negatives, not the number screened.

**Implementation outcomes (RE-AIM).** Reach, adoption by volunteers and hospitals, fidelity to protocol, image-quality pass rate, time added per screen, usability (System Usability Scale), provider confidence, referral completion, time to dentist review and to biopsy.

**Economic evaluation.** Micro-costing (training, devices, software, volunteer time, dentist time, referrals, biopsies, patient travel and lost wages); cost per screen; cost per high-risk case appropriately referred; decision model of lifetime costs and QALYs following Thai HTA methods [CONFIRM: Thailand has used a threshold of about 160,000 THB per QALY]; budget-impact analysis for Health Region 10.

**Qualitative work.** Focus groups with volunteers, dentists and patients; interviews with Provincial Health Office and Health Region managers.

**Reporting standards.** STARD 2015 (diagnostic accuracy), TRIPOD+AI (prediction-model development and validation), DECIDE-AI (early clinical evaluation of AI decision support), CHEERS 2022 (economic evaluation).

## 8.8 Gender, equity and inclusion
- **Risk factors differ by sex:** betel chewing is concentrated among older rural women; smoking and drinking are more common among men. Analyses and outreach are sex- and age-disaggregated.
- **Most village health volunteers are women:** measure added workload; fair compensation; leadership roles as lead trainers.
- **Access barriers to referral differ by sex:** record and address them (flexible appointments, transport support).
- **Algorithmic fairness:** report performance by sex, age, device and site; recalibrate if gaps appear.
- **Privacy and dignity:** mouth-only photos; same-sex volunteer where feasible; plain-language Thai consent (and local languages where needed).

## 8.9 Ethics, data protection and AI safety
- **Approvals:** [FILL: Mahidol ethics committee + site approvals]; amendments before changes.
- **Consent:** written informed consent in Thai (witnessed verbal consent for people who cannot read); covers screening, photos, storage and use of de-identified images to improve the AI; people can refuse image storage and still be screened.
- **Thailand PDPA (2019):** health data are sensitive personal data. Define controller (hospital/Mahidol) and processor (KPD); encryption; role-based access; de-identification; data-sharing agreement; data protection officer; storage location [FILL].
- **AI as decision support:** clinicians decide; a low AI score never blocks a referral if a volunteer or dentist is concerned; every high-risk result is followed up.
- **Conflict of interest:** KPD may profit from adoption. Accuracy and cost analyses are led by Mahidol/hospital investigators with an independent statistician.
- **Data ownership and benefit sharing:** Thai institutions own patient data; KPD uses de-identified data under agreement; joint authorship.

## 8.10 Regulatory pathway
- **Pilot:** research use under ethics approval.
- **Clinical use in Thailand:** likely regulated as Software as a Medical Device by the Thai FDA [CONFIRM classification and current AI/SaMD guidance]; start a pre-submission consultation early.
- **Quality system:** ISO 13485 (quality management), IEC 62304 (software lifecycle), ISO 14971 (risk management), cybersecurity documentation.
- **Model licence:** MedGemma is released under Google's Health AI Developer Foundations terms of use. Confirm the terms permit your commercial and clinical use, and document validation, since the base models are not intended for clinical use without it [CONFIRM].
- **Later markets:** each country's device regulator; US FDA strategy to be assessed if entering the US.

## 8.11 Team and partners
| Person / partner | Role |
|---|---|
| Dr. Narawitchz Wareekul (Mahidol University) | PI for Thai-led grants; clinical protocol, labelling standards, validation |
| Ernest Choi (KPD CEO) | Partnerships, operations, sustainability, business model |
| Amir Fleurizard (KPD CTO) | App, dashboard, AI pipeline, data security |
| Partner hospitals [FILL] | Site leads, dentist reviewers, volunteer supervision, referrals |
| Health Region 10 / Provincial Health Offices | Steering group, policy uptake |
| Harvard GAMI, MIT, University of Michigan [FILL: named people] | Mentorship; [FILL: e.g. biostatistics, health economics, STTR research partner] |
| **Gaps to fill** | Oral pathologist (reference standard) · biostatistician/epidemiologist · health economist · social/gender scientist · regulatory/QMS adviser |

## 8.12 Timeline and milestones (18 months; adjust to start date)
| Months | Activities | Milestone / deliverable |
|---|---|---|
| 1–3 | Agreements, ethics amendments, hiring; MVP finalisation (quality checks, offline mode); training manual | MVP v1.0; signed data-sharing agreement |
| 2–4 | Train 20 lead trainers → 300 volunteers | Training report; baseline survey |
| 4–9 | 6-month pilot; referral tracking; usability surveys | Monthly dashboards; interim report |
| 6–12 | Model refinement; external validation; biopsy follow-up | Validation report (STARD/TRIPOD+AI) |
| 9–14 | Economic evaluation; gender analysis; continuity-of-screening playbook | Cost-effectiveness report; policy brief |
| 12–18 | Dissemination workshop (Regions 7, 9, 10); scale-up plan; manuscripts | 2 manuscripts; scale-up proposal to MOPH/NHSO |

**Key performance indicators:** volunteers trained; people screened; % usable images; high-risk cases identified and confirmed; referral completion; time to diagnosis; cost per screen; cost per high-risk case referred; sensitivity/specificity; user satisfaction.

## 8.13 Risks and mitigation
| Risk | Mitigation |
|---|---|
| Too few confirmed high-risk cases | Enrich with archived hospital images; extend recruitment; add sites |
| Poor image quality in the field | In-app quality checks; refresher training; supervision by lead trainers |
| Model performs worse at new sites or devices | External validation; site recalibration; continuous monitoring |
| Low referral completion | Patient tracking via volunteers; reminders; transport support |
| Volunteer drop-out or workload | Compensation; recognition; peer support; time-per-screen monitoring |
| Data breach / privacy complaint | Encryption, access control, PDPA procedures, incident plan |
| Regulatory delay | Early Thai FDA consultation; research-use framing during pilot |
| Funding gaps | Staggered applications across funders; cloud credits; staged scope |

## 8.14 Dissemination and uptake
Steering group with Health Region 10 and Provincial Health Offices; policy briefs (Thai/English) for MOPH and NHSO; implementation guide for hospitals; picture-based training materials; open-access publications; published image-acquisition protocol and quality metrics; community feedback sessions; regional workshop with Regions 7 and 9.

## 8.15 Sustainability and business model
After the pilot, hospitals and Health Region offices contract for the software (per screen or per facility [FILL: pricing]). Evidence from Aim 3 supports financing by NHSO/MOPH. Training is embedded through lead volunteers. Regional expansion goes to other high-burden countries with community health-worker systems. Grants fund validation; contracts and investment fund scale.

## 8.16 Budget framework
See Section 9 for categories and rules. Typical cost drivers: volunteer training and compensation; devices; research staff at sites; biopsy/histopathology; dentist review time; cloud compute and secure storage; app maintenance; travel to districts; economic evaluation; publication fees; institutional overhead.

## 8.17 References
1. Su YF, et al. Current insights into oral cancer diagnostics. *Diagnostics*. 2021;11(7):1287.
2. Warnakulasuriya S, Filho AM. Oral cancer in the South and South-East Asia region, 2022: incidence and mortality. *Oral Dis*. 2025;31(5):1398–1405.
3. Rumgay H, et al. Global burden of oral cancer in 2022 attributable to smokeless tobacco and areca nut consumption. *Lancet Oncol*. 2024;25(11):1413–1423.
4. Francis DL, Pape Reddy SS. Oral cancer disparities in LMICs: a global health equity perspective. *Ann Glob Health*. 2025;91(1):81.
5. Raman S, et al. Provider cost of treating oral potentially malignant disorders and oral cancer in Malaysian public hospitals. *PLoS One*. 2021;16(5):e0251760.
6. Walsh T, et al. Clinical assessment for the detection of oral cavity cancer and potentially malignant disorders in apparently healthy adults. *Cochrane Database Syst Rev*. 2021;12:CD010173.
7. Sankaranarayanan R, et al. Effect of screening on oral cancer mortality in Kerala, India: a cluster-randomised controlled trial. *Lancet*. 2005;365(9475):1927–1933.

> Verify every reference (authors, year, pages, DOI) before submitting. Your draft's DOI for reference 1 appears truncated ("diagnostics1107128"); the article is in *Diagnostics* 11(7):1287 (2021).

<!-- pagebreak -->

# 9. Budget guide

## 9.1 Master budget (build once, then map to each funder's categories)
| Item | Unit cost | Quantity | Year 1 | Year 2 | Total | Site / owner |
|---|---|---|---|---|---|---|
| Project coordinator | | | | | | |
| AI/ML engineer | | | | | | KPD |
| Research assistants / dental assistants per site | | | | | | |
| Dentist review time / annotators | | | | | | |
| Pathology (biopsy + histology) | | | | | | |
| Volunteer training (venue, meals, materials) | | | | | | |
| Volunteer compensation (training and screening days) | | | | | | |
| Smartphones / intraoral cameras | | | | | | |
| Cloud compute, storage, security | | | | | | KPD |
| Software maintenance / app store / licences | | | | | | KPD |
| Travel to districts and between sites | | | | | | |
| Patient transport support for referrals | | | | | | |
| Economic evaluation / statistician | | | | | | |
| Regulatory / QMS consultant | | | | | | |
| Dissemination (workshop, open-access fees) | | | | | | |
| Ethics fees | | | | | | |
| Indirect costs / overhead (funder's rate) | | | | | | |
| **Total** | | | | | | |

State the exchange rate and date used (1 USD = [FILL] THB, [date]).

## 9.2 Funder budget rules (summary)
- **NIH:** foreign organisations: indirect costs ≤ 8% and detailed budget required. R21: ≤ US$275k direct over 2 years (≤ US$200k in any year). No new foreign subawards (see Section 11). SBIR/STTR: R&D normally in the US; STTR requires ≥ 40% small business and ≥ 30% research institution.
- **Thai (NRCT/HSRI/TSRI/PMU):** categories ค่าตอบแทน (compensation), ค่าจ้าง (wages), ค่าวัสดุ (materials), ค่าใช้สอย (operating), ค่าครุภัณฑ์ (equipment), and institutional overhead (often ~10% [CONFIRM]); budgets per year and per instalment (งวด); equipment needs strong justification.
- **PMU-C:** show private-partner co-funding (in-cash and in-kind) per category.
- **Startup awards:** a short "use of funds" table.

<!-- pagebreak -->

# 10. Evidence and context reviewers expect

## 10.1 Key numbers (with sources)
| Fact | Value | Source |
|---|---|---|
| Global oral cancer deaths per year | ~177,000 | Su et al. 2021 [1] (GLOBOCAN 2020) |
| Asia's share of global oral cancer | ~two-thirds of cases | [1, 2] |
| Burden attributable to smokeless tobacco and areca nut | Substantial share in South/Southeast Asia | Rumgay et al. 2024 [3] |
| Treatment cost late vs early stage (Malaysia) | US$2,027 vs US$394 per patient per year | Raman et al. 2021 [5] |
| Visual screening by trained health workers | Reduced oral cancer mortality in tobacco/alcohol users | Sankaranarayanan et al. 2005 [7] |
| Accuracy of clinical visual exam | Varies widely with examiner | Walsh et al. 2021 (Cochrane) [6] |
| Thailand incidence and mortality | [FILL] | GLOBOCAN 2022 (gco.iarc.fr) |
| Late-stage % in Region 10 hospitals | [FILL] | Hospital/registry data |
| Betel/tobacco/alcohol prevalence in Region 10 | [FILL] | Thai national surveys / provincial data |
| Dentists per population, Region 10 provinces | [FILL] | MOPH workforce data |

## 10.2 Thai health-system context (useful in every Thai and international proposal)
- **Village health volunteers (อสม.):** more than one million nationwide; the backbone of community health work, including outbreak response during COVID-19. Most are women.
- **Service tiers:** sub-district health promoting hospitals (รพ.สต.) → community (district) hospitals → general/provincial and regional hospitals. Referral flows upward.
- **Health Regions (เขตสุขภาพ):** 12 regions + Bangkok. **Region 10** = Ubon Ratchathani, Sisaket, Yasothon, Amnat Charoen, Mukdahan. **Region 7** = Khon Kaen, Roi Et, Maha Sarakham, Kalasin. **Region 9** = Nakhon Ratchasima, Chaiyaphum, Buriram, Surin.
- **Financing:** Universal Coverage Scheme managed by NHSO (สปสช.), which funds health promotion and prevention services; local health funds at sub-district level can co-finance community activities.
- **Current oral cancer screening:** paper risk questionnaire for adults aged 40+ (tobacco, alcohol, betel quid/tobacco chewing, ill-fitting dentures) → examination by doctor, dentist or dental nurse if risk factors are present.

## 10.3 Global policy alignment
- **WHO Global Strategy on Oral Health (2022)** and **Global Oral Health Action Plan 2023–2030:** emphasise integrating oral health into primary care and early detection of oral cancer.
- **UN Sustainable Development Goals:** SDG 3.4 (reduce premature NCD mortality), SDG 3.8 (universal health coverage), SDG 5 (gender equality; relevant to the volunteer workforce).
- **Thailand:** national NCD and cancer control plans; MOPH digital health strategy [FILL: cite current documents by name].

<!-- pagebreak -->

# 11. Compliance and rules that affect your applications

| Topic | Rule | Impact on KPD |
|---|---|---|
| **NIH foreign subawards** | Since 2025, NIH does not accept new applications with foreign subawards; due dates on or after 25 Jan 2026 use the new PF5/UF5 international structure | A US-led NIH grant cannot simply subcontract Thai hospitals; ask the programme officer |
| **SBIR/STTR place of performance** | R&D normally performed in the US; foreign work needs justification and approval | Fund US-based technical work with NIH/NSF; fund Thai fieldwork with Thai grants |
| **SBIR/STTR ownership** | > 50% owned/controlled by US citizens or permanent residents | Confirm KPD's cap table |
| **NIH Common Forms** | Biosketch and Current & Pending Support via SciENcv; ORCID linked (since 25 Jan 2026) | Every key person needs ORCID + SciENcv |
| **NIH AI policy** | Applications substantially developed by AI are not considered original; max 6 applications per PI per year | Write science sections yourselves |
| **MIT Solve AI policy** | Discourages AI-written applications; you certify no fabrication or exaggeration | Rewrite drafts; verify every claim |
| **Thailand PDPA (2019)** | Health data = sensitive personal data; explicit consent; security; cross-border transfer rules | Data-sharing agreement; storage location; DPO |
| **Ethics** | Approval at each site (or central approval accepted by all); FWA needed for US federal funding | Confirm each hospital's ethics route |
| **Thai FDA** | AI used for clinical decisions is likely a medical device | Plan the regulatory pathway before scale-up |
| **Conflict of interest** | Company founders evaluating their own product | Independent analysis by academic partners |
| **Thai startup funds (depa, NIA, TCELS, PMU-C partner)** | Often require a Thai-registered company | Consider a Thai subsidiary |

<!-- pagebreak -->

# 12. Registrations and administration checklist

| Registration | Who | Needed for | Lead time | Done |
|---|---|---|---|---|
| SAM.gov → UEI (foreign entities also need an NCAGE code) | KPD (and Mahidol if applying to NIH directly) | All US federal grants | 4–8 weeks | ☐ |
| SBA Company Registry (SBC Control ID) | KPD | SBIR/STTR | 1 day | ☐ |
| Grants.gov + eRA Commons (institution + PI) | KPD / US university | NIH | 2–4 weeks after SAM | ☐ |
| ORCID iD + SciENcv | Every key person | NIH | 1 day | ☐ |
| Research.gov / NSF registration | KPD | NSF SBIR | 1–2 weeks | ☐ |
| NRIIS (nriis.go.th) | Dr. Wareekul + Thai co-investigators | NRCT, HSRI, TSRI, PMU | 1–2 weeks | ☐ |
| Mahidol research office (internal deadlines) | Dr. Wareekul | All Thai grants | ongoing | ☐ |
| Ethics approvals / amendments (each site) | PI | All | 1–3 months | ☐ |
| Data-sharing agreement (hospitals + Mahidol + KPD) | All partners | All | 1–3 months | ☐ |
| Federalwide Assurance (FWA) for ethics committees | Hospitals | NIH (before award) | 2–6 weeks | ☐ |
| Company documents (registration certificate, bank letter, tax ID) | KPD | All startup awards | — | ☐ |

<!-- pagebreak -->

# 13. Letters of support

Collect signed letters on letterhead. Offer a draft to make it easy for partners to say yes.

| From | What the letter should say |
|---|---|
| Director of each partner hospital | Commitment of staff time, patient access, data access, space; named site lead |
| Head of pathology / oral pathology | Will provide histopathology confirmation for biopsied cases |
| Health Region 10 office / Provincial Health Offices | Interest in results; participation in the steering group; potential adoption |
| Mahidol University (faculty/research office) | Institutional support; PI time; ethics oversight |
| US research partner (for STTR) | Research role, PI/co-PI, share of work |
| Harvard GAMI / MIT / University of Michigan mentors | Mentorship and specific support |
| National Cancer Institute of Thailand | Alignment with national cancer control; data or advice |
| Volunteer network leader | Volunteers' interest and involvement in design |

**Draft wording (hospital director):**
> "[Hospital] is pleased to partner with Mahidol University and Kon Pop Detection on '[project title]'. Oral cancer is a significant problem in our catchment population, and most cases present late. We commit [staff/time], access to our oral and dental clinics, and support for village health volunteer training in [districts]. Dr./Mr./Ms. [name] will serve as site lead. We look forward to using the findings to improve early detection in our community. Signed, [Name], Director, [date]."

<!-- pagebreak -->

# 14. Pitch deck and draft fixes

| Where | Issue | Fix |
|---|---|---|
| Deck slide 4 | "Why so many in **South Asia**?" shows Thailand (Southeast Asia) | "South and Southeast Asia" |
| Deck slide 3 | "74% of oral cancer deaths occur in South Asia" | Check reference 1; it may refer to Asia overall |
| Deck slide 4 | "100% screening done without technology"; "57% die within 5 years" | Cite a source or rephrase |
| Deck slide 8 | "Terabytes of training data"; competitor ✓/✗ table | Give numbers; avoid unverifiable claims about competitors |
| Deck slide 10 | Meme on business model slide | For formal applications use a customer/pricing slide |
| Draft proposal | "Sector 10/7/9" | "Health Region 10/7/9 (เขตสุขภาพที่)" |
| Draft proposal | "one of the most expansive proprietary datasets globally" | Replace with the actual dataset size |
| Draft proposal | Pilot "Spring 2026", analysis "Summer 2026" | Update to actual status and the new timeline |
| Draft proposal | Stage survival "96% / 10%" | Use sourced survival figures |
| Draft proposal | Aim 1 bullet with internal notes; highlighted questions | Clean up (done in applications/02) |
| Draft proposal | Reference 1 DOI looks truncated | Verify |
| Draft proposal | Duplicate "scale" question | Answer once |

<!-- pagebreak -->

# 15. Decisions to make now

1. **Incorporation and ownership of KPD:** US company? Thai company? Both (US parent + Thai subsidiary)? This decides eligibility for NIH/NSF small-business grants and Thai startup funds.
2. **PI for each route:** Dr. Wareekul (Thai grants); a US university faculty member or a KPD employee who works more than 50% for KPD (NIH STTR/SBIR).
3. **US research partner for STTR:** University of Michigan, Harvard or MIT, with a named faculty member.
4. **Partner hospitals:** final list, names and site leads (3 or 4?).
5. **Which call your pandemic-preparedness draft is for,** and whether infectious-disease work can honestly be added.
6. **Data governance:** who owns the data, where it is stored, and what KPD may use it for (put this in a signed agreement).
7. **Pricing hypothesis** for business-model sections.

# 16. Facts to collect (fills most [FILL]s)

| Fact | Needed by |
|---|---|
| Legal name, incorporation country/state/date, HQ city, ownership | Solve, PIC, NIH/NSF, cloud credits |
| Dataset size, sources, labels, number of biopsy-confirmed cases | All |
| Model metrics (sensitivity, specificity, AUC, test-set size, reference standard) | All |
| Pilot status: start date, volunteers trained, people screened, referrals, active hospitals | All |
| The early-detection ("saved a life") case, described factually without identifying details | Solve, PIC |
| Ethics approval details | All |
| Hospital names, directors, site leads; letters | All |
| Google award name and amount; GAMI support; funds raised | Startup awards, NIH/NSF |
| Team details: titles, experience, publications; added co-investigators | All |
| Tech stack details: app framework, backend, cloud region, offline method, YOLO version | Solve, NSF, cloud credits |
| Thai and Region 10 statistics | All |
| Pricing hypothesis; customer letters of intent | Solve, PIC, PMU-C |

<!-- pagebreak -->

# 17. Glossary

| Term | Meaning |
|---|---|
| อสม. (VHV) | Village health volunteer (อาสาสมัครสาธารณสุขประจำหมู่บ้าน) |
| รพ.สต. | Sub-district health promoting hospital (primary-care unit) |
| เขตสุขภาพ | Health Region (Thailand has 12 + Bangkok) |
| MOPH | Ministry of Public Health, Thailand |
| NHSO (สปสช.) | National Health Security Office; manages the Universal Coverage Scheme |
| NRIIS | National Research and Innovation Information System; Thai grant submission platform |
| NRCT (วช.) / TSRI (สกสว.) / HSRI (สวรส.) | Thai research funders (national research council; research & innovation fund manager; health systems research institute) |
| PMU-C (บพข.) / PMU-B (บพค.) | Thai programme management units for competitiveness / human resources & institutional development |
| TRL / SRL | Technology / Societal Readiness Level (1–9 scales used by Thai funders) |
| OPMD | Oral potentially malignant disorder (e.g. leukoplakia, erythroplakia, oral submucous fibrosis) |
| SBIR / STTR | US Small Business Innovation Research / Small Business Technology Transfer grants |
| NOFO / RFA / PA / PAR | NIH funding announcement types |
| PI | Principal Investigator (lead researcher) |
| F&A / indirect costs | Institutional overhead |
| UEI / SAM / NCAGE | US federal entity ID / System for Award Management / foreign entity code |
| eRA Commons / SciENcv / ORCID | NIH systems / biosketch tool / researcher ID |
| PDPA | Thailand's Personal Data Protection Act (2019) |
| SaMD | Software as a Medical Device |
| QMS | Quality management system (ISO 13485) |
| MedGemma / HAI-DEF | Google's open medical AI models / Health AI Developer Foundations |
| YOLO | "You Only Look Once" object-detection model family |
| STARD / TRIPOD+AI / DECIDE-AI / CHEERS | Reporting guidelines for diagnostic accuracy / AI prediction models / early clinical AI evaluation / economic evaluations |
| QALY | Quality-adjusted life year (used in cost-effectiveness) |
| RE-AIM | Implementation framework: Reach, Effectiveness, Adoption, Implementation, Maintenance |
| TAM / SAM / SOM | Total / serviceable / obtainable market |

# 18. Key links

| Resource | Link |
|---|---|
| MIT Solve 2027 Global Health Challenge | solve.mit.edu/challenges/2027-global-health-challenge |
| Harvard President's Innovation Challenge | innovationlabs.harvard.edu/presidents-innovation-challenge |
| NIH SBIR/STTR | seed.nih.gov · grants.nih.gov (search PA-27-100, PA-27-102) |
| NSF SBIR/STTR | seedfund.nsf.gov |
| NIH PA-25-253 (R21) | grants.nih.gov/grants/guide/pa-files/PA-25-253.html |
| NRCT | nrct.go.th · NRIIS: nriis.go.th |
| HSRI | hsri.or.th |
| TSRI | tsri.or.th |
| PMU-C / PMU-B | pmuc.or.th · pmub.or.th |
| ThaiHealth | thaihealth.or.th |
| TCELS / depa / NIA | tcels.or.th · depa.or.th · nia.or.th |
| National Cancer Institute of Thailand | nci.go.th |
| UICC grants | uicc.org/what-we-do/capacity-building/grants |
| IARC | iarc.who.int |
| e-ASIA JRP | the-easia.org/jrp |
| GLOBOCAN (statistics) | gco.iarc.fr |
| Google for Startups Cloud | cloud.google.com/startup |
| AWS Activate | aws.amazon.com/activate |
