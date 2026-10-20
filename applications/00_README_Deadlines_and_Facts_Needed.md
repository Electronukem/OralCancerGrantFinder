# Kon Pop Detection – Grant Applications: Priorities, Deadlines, and Facts Needed

Drafted 13 Oct 2026 from the KPD pitch deck and draft proposal.

> **Read first:** these are **drafts to rewrite in your own words**, not final submissions. MIT Solve advises against AI-written applications, and NIH does not treat applications "substantially developed by AI" as original. Every **[FILL]** is a fact only your team knows. Nothing has been invented to fill the gaps; please don't let numbers be guessed either.

## Priority order (by deadline and fit)

| # | Grant | Applicant | Deadline | Amount | File |
|---|---|---|---|---|---|
| 1 | **MIT Solve 2027 Global Health Challenge** | KPD | **2 Nov 2026, 12:00 noon US Eastern** (= 00:00, 3 Nov, Thailand) | $10k + prizes up to $150k (AI for Humanity) | 01 |
| 2 | **Startup cloud credits** (Google for Startups, AWS Activate, Microsoft, NVIDIA Inception) | KPD | Rolling: apply this week | Credits | 10 |
| 3 | **Harvard President's Innovation Challenge 2027** | KPD (Harvard student on team) | ~early Dec 2026 **[CONFIRM]** | Share of ~$500k pool | 03 |
| 4 | **NIH STTR PA-27-102 (or SBIR PA-27-100) Phase I** | KPD + US university | **5 Jan 2027** **[CONFIRM]**; registrations take ~2–3 months, so start now | ~$300k **[CONFIRM]** | 04 |
| 5 | **NSF SBIR (solicitation 26-511) Project Pitch** | KPD | listed close **4 Nov 2026**; check whether its "scientific instrumentation" emphasis excludes you | Phase I ~$305k **[CONFIRM]** | 05 |
| 6 | **TSRI Fundamental Fund via Mahidol** | Mahidol (Dr. Wareekul) | Internal Mahidol call, often Oct–Jan: ask the research office now | Seed (1 yr) | templates/05 |
| 7 | **NRCT** | Mahidol | FY2571 calls ~Nov 2026–Apr 2027 **[CONFIRM]** | varies | 07 |
| 8 | **HSRI** | Mahidol | ~Feb–Apr 2027 **[CONFIRM]** | varies | 06 |
| 9 | **PMU-C** | Mahidol + KPD (co-funding) | annual call **[CONFIRM]** | varies | 08 |
| 10 | **ThaiHealth** | Thai hospital / Mahidol / community organisation | open grant **[CONFIRM]** | varies | 09 |
| 11 | **NIH R21 PA-25-253** (academic-led) | University | 16 Feb 2027 **[CONFIRM]** | ≤ $275k direct | 11 |
| 12 | **Your draft (AI4PEP/IDRC-style call)** | Mahidol as lead (PI from region) | **[FILL: which call? deadline?]** | AI4PEP last call: ≤ CAD 362,500 | 02 |
| 13 | Others: Google.org, Rotary, Temasek, IARC, UICC, TCELS/depa/NIA, e-ASIA, JST NEXUS, Wellcome | various | various | various | 12 (concept note) |

## Decisions you need to make (they change several applications)
1. **Where is KPD incorporated, and who owns it?** US small business, > 50% US-owned → SBIR/STTR and NSF possible. Thai company → TCELS/depa/NIA/PMU-C possible. You may need both (a US parent and a Thai subsidiary).
2. **Who is PI for each grant?** Thai grants and the AI4PEP-style call: Dr. Wareekul via Mahidol. NIH STTR: a US university faculty member or a KPD employee who is > 50% employed by KPD.
3. **How many partner hospitals, and their exact names?** The deck/draft says 3 regional hospitals in Health Region 10; you told me 4 including "Huathahan". **I think "Huathahan" is Hua Taphan Hospital (โรงพยาบาลหัวตะพาน), Amnat Charoen, which is in Health Region 10. Please confirm.**
4. **Keep aims distinct across funders:** NRCT = technical validation; HSRI = health-system implementation and costs; PMU-C = product and regulation; ThaiHealth = community prevention; NIH/NSF = US-based technical R&D. Declare overlapping applications honestly.

## Master list of facts to collect (fills most [FILL]s)
| Fact | Used in |
|---|---|
| Legal name, incorporation country/state/date, HQ city, ownership | 01, 03, 04, 05, 10 |
| Dataset: number of images, sources, how labelled (dentist? biopsy?), number of high-risk/cancer cases | all |
| Model results: sensitivity, specificity, AUC, test-set size, comparison standard | all |
| Pilot status: start date, volunteers trained, people screened, referrals, hospitals active | all |
| The "saved 1 life" case: factual, de-identified description | 01, 03 |
| Ethics approval: committee name, number, date | 01, 02, 06, 07 |
| Hospital names and directors; letters of support | all |
| Google award exact name and amount; GAMI support; money raised | 01, 03, 05, 10, 12 |
| Team: Dr. Wareekul's exact title and experience; Ernest's Harvard programme; Amir's AI experience; others (pathologist, statistician, health economist) | all |
| Tech stack: app framework, backend, cloud, offline method, YOLO version | 01, 05, 10 |
| Pricing hypothesis and any customer letters of intent | 01, 03, 08 |
| Thai statistics: oral cancer incidence/mortality (GLOBOCAN 2022 Thailand), late-stage %, dentists per population in Region 10 | 01, 02, 06, 07 |

## Fix in your pitch deck / draft before reusing text
- "South Asia" → **"South and Southeast Asia"** (Thailand is Southeast Asia)
- "74% of oral cancer deaths occur in South Asia": verify against Su et al. 2021; it may refer to Asia
- "100% screening done without technology" and "57% die within 5 years": cite a source or rephrase
- "Terabytes of training data"; "one of the most expansive proprietary datasets globally"; the competitor ✓/✗ table: back them up with numbers or soften them. Solve requires you to confirm there is no exaggeration.
- "Sector 10/7/9" → **Health Region 10/7/9 (เขตสุขภาพที่)**
- Timeline: Spring/Summer 2026 pilot dates are now past; update with what actually happened
- Stage survival "96% / 10%": replace with a sourced figure

## Tools
- `python check_limits.py applications\<file>.md`: checks answers against word and character limits
- `python make_word_templates.py applications`: makes Word copies in `applications\word\`
- `python find_grants.py`: reruns the grant search (now includes SBIR/STTR and the new funders)
