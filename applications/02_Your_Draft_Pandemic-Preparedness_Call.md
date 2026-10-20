# Completed Draft – Your Existing Proposal Form (AI4PEP / IDRC-style call)

> **Which grant is this?** The questions in your draft (pandemic and epidemic preparedness; gender; "use and mobilization"; IRB; "Excellence of Research Team (500 words)") match the format of the **AI4PEP network** (Global South AI for Pandemic & Epidemic Preparedness & Response, funded by Canada's IDRC and run from York University). AI4PEP's last open call (2023) required:
> - a **recognised public university in Asia/Africa/LAC/MENA** in the team, with the **PI from the region** (students cannot be PI). **Dr. Wareekul / Mahidol University should be the PI and lead institution, not the company**
> - AI as the "entry point" for **early detection, warning and response to infectious diseases**
> - a gender-sensitive approach (SDG 3 + SDG 5)
>
> **Fit warning:** oral cancer is not an infectious disease. The draft below frames the project honestly around **continuity of essential care during outbreaks** and **strengthening the volunteer/digital infrastructure used in outbreak response**. If the call strictly requires infectious-disease detection, this proposal will likely score low; consider adding a genuine infectious-disease module (see Q2 option B) or choosing another funder. **Confirm the call name, eligibility and deadline: [FILL].**

> **Corrections made to your draft:**
> 1. The timeline said "Pilot Launch Spring 2026" and "Analysis Summer 2026", which are now in the past. The plan below is updated from Nov 2026 onward. **[FILL]** what actually happened.
> 2. "Sector 10" → **Health Region 10** (เขตสุขภาพที่ 10: Ubon Ratchathani, Sisaket, Yasothon, Amnat Charoen, Mukdahan). Use the official term.
> 3. Your draft says "three regional hospitals"; earlier you mentioned four, including "Huathahan". **I think this is Hua Taphan Hospital (โรงพยาบาลหัวตะพาน), Amnat Charoen, which is in Health Region 10.** Confirm names and number.
> 4. Unsupported claims to remove or back up with numbers: "one of the most expansive proprietary oral cancer imaging datasets globally"; "high-performance model"; "Stage 1 – 96%, Stage 4 – 10%" (cite a source or replace with a sourced survival figure).
> 5. The question "What are the potential opportunities to scale…" appears **twice** in your copy of the form. Answer it once.
> 6. Your Aim 1 bullet "1 year annual outlook validation tool – number detected, full number comes out in 10 years…" and the highlighted notes are internal notes. They are cleaned up below.

---

## Title
Kon Pop Detection (KPD): AI-Enabled Oral Cancer Screening by Village Health Volunteers in Northeast Thailand, Building Resilient Community Screening for Health Emergencies

## Lay summary
*(Your existing lay summary is good. Keep it, but update the pilot dates.)*

---

## Research Problems and Justification {limit: 1500 words}

### a) General objective
To improve early detection of oral cancer and high-risk oral potentially malignant disorders (OPMDs) in underserved communities of northeast Thailand, by developing, validating and implementing a low-cost AI-assisted screening tool used by village health volunteers. The tool must keep working when health systems are under strain, such as during epidemics.

### b) Specific objectives
1. **Develop and validate** an AI model (fine-tuned MedGemma with a YOLO lesion detector) that classifies intraoral smartphone images into low/high risk, with target sensitivity ≥ [FILL]% and specificity ≥ [FILL]% against specialist diagnosis and biopsy, including external validation at a hospital not used in training.
2. **Implement** the tool with ~300 trained village health volunteers linked to [FILL: 3–4] hospitals in Health Region 10, and measure feasibility, usability, image quality, adoption and referral completion over 6 months.
3. **Quantify** the economic and health-system impact (cost per screen, cost per high-risk case appropriately referred, unnecessary referrals avoided, time to diagnostic confirmation) compared with standard paper-based visual screening.
4. **Test resilience:** document how decentralised, app-based screening and remote dentist triage can maintain oral cancer screening during disruptions (outbreaks, staff shortages), and produce a playbook for health authorities.
5. **Analyse gender and equity:** examine differences in risk factors, screening uptake, model performance and volunteer workload by sex and age.

### Problem
Oral cancer causes about 177,000 deaths globally each year, and Asia carries roughly two-thirds of the global burden (Su et al. 2021; Warnakulasuriya & Filho 2025). In South and Southeast Asia, a large share of cases is attributable to smokeless tobacco and areca nut (betel quid) (Rumgay et al. 2024). Outcomes are driven less by a lack of treatment than by late presentation: early-stage disease is highly curable, while late-stage disease carries poor survival and roughly five-fold higher treatment costs (US$2,027 vs US$394 per patient per year in Malaysian public hospitals; Raman et al. 2021).

In Thailand, community screening for adults aged 40+ is delivered largely by village health volunteers (อสม.) using a paper risk-factor questionnaire and a visual mouth examination after about one day of training. Those with risk factors are referred to a doctor, dentist or dental nurse. This system has two failure modes (Walsh et al. 2021, Cochrane):
1. **Missed lesions:** visual inspection accuracy varies widely with examiner training.
2. **Excess referrals:** low-risk referrals overload scarce dentists and cost patients travel and lost wages, while high-risk patients may be lost to follow-up.

Paper records are slow to reach hospitals and cannot be prioritised.

### Why AI, why now
Smartphones are now common among volunteers. Medical foundation models such as Google's MedGemma allow accurate image models to be built from smaller, locally collected datasets. Most published oral-image AI models were trained on hospital images and may not generalise to community conditions: variable lighting, low-cost phones, and diverse presentations. KPD trains and validates directly on images collected in the intended setting.

### Justification and preliminary work
- Working volunteer app (digital risk survey, guided three-photo capture), dentist triage dashboard, fine-tuned model, training game, and picture-based training manual
- Dataset: [FILL: number of images, how labelled]
- Ethics approval: [FILL: committee, number]
- Hospital agreements: [FILL]
- Mini-pilot results: [FILL]
- Team recognition: MIT Grand Hack 2025 [FILL: Google award name]; Harvard GAMI incubator

### Significance
If successful, the project will provide (1) a validated, low-cost tool; (2) evidence on cost-effectiveness for Thai health authorities; (3) implementation standards (image acquisition, quality assurance, governance) for AI in community screening in low-resource settings; and (4) a model of resilient, decentralised screening that can continue during health emergencies.

> [FILL: add 1–2 Thailand-specific statistics: oral cancer incidence and mortality in Thailand (GLOBOCAN 2022), and % late-stage at diagnosis from Thai sources.]

---

## How does your proposal connect to preparedness and response to emerging and re-emerging infectious diseases? {limit: 1000 words}

**Option A (recommended, honest framing): continuity of essential care and resilient community health infrastructure.**

During COVID-19, routine cancer screening fell sharply worldwide, and delayed diagnoses followed. Specialist services, hospital outpatient clinics and travel were all restricted, while Thailand's village health volunteers became the backbone of community outbreak response: house-to-house screening, contact follow-up and home monitoring. Any future epidemic will put the same pressure on oral cancer screening, which depends on in-person visits to scarce dentists.

KPD strengthens preparedness in three ways:

1. **Maintaining NCD screening during outbreaks.** Volunteers can screen in the community and send images to dentists for remote triage, without patients travelling to hospital. Only high-risk patients need a hospital visit. This keeps an essential cancer-prevention service running with fewer contacts and less crowding in facilities during an epidemic.
2. **Strengthening the volunteer digital backbone used in outbreak response.** The project trains ~300 volunteers in structured digital data collection, image capture, data protection and referral workflows. It also builds the supporting infrastructure: devices, secure data pipelines, dashboards, and supervision links between volunteers and hospitals. The same capabilities are used in outbreak response, such as symptom reporting and follow-up of cases or contacts. The KPD platform is modular: the data-collection and triage workflow can carry additional forms or screening modules when health authorities need them.
3. **Reducing system load.** By lowering unnecessary referrals, KPD frees specialist and outpatient capacity, which is critical when health systems are stretched by an outbreak.

**Research question added for this call:** *Can AI-assisted community screening with remote triage maintain oral cancer screening coverage and referral completion under simulated or real service disruption?* We will document service continuity: the share of screens completed and triaged remotely, and the time to triage. With Health Region 10 and Provincial Health Office partners, we will co-develop a **continuity-of-screening playbook** for use during outbreaks.

**Alignment with national and sub-national plans:** [FILL: cite Thailand's national NCD/cancer control plan, MOPH digital health strategy, Health Region 10 service plan, and the national emergency preparedness framework, if you can name the actual documents.]

**Option B (only if the call requires an infectious-disease AI use-case):** add a work package with an infectious-disease partner, e.g. using the volunteer app to capture images of oral lesions linked to infections (oral candidiasis as an HIV marker, hand-foot-and-mouth disease, mpox oral lesions) for early-warning reporting to district health officers. This needs an infectious-disease co-investigator and ethics amendment. **Do not claim it unless you will do it.**

---

## Engagement with national and sub-national governing institutions
> Describe **actual** engagement (meetings, letters, MOUs) separately from **planned** engagement.

**Done so far:** [FILL: e.g. approval from the directors of [hospitals]; meetings with the Health Region 10 office / Provincial Health Office of Amnat Charoen / Ubon Ratchathani; Mahidol University ethics committee; district health offices supervising volunteers]

**Planned:**
- **Health Region 10 office and Provincial Health Offices:** steering committee membership; quarterly results reviews; co-design of referral pathways
- **Ministry of Public Health, Department of Health (Bureau of Dental Health) [FILL: confirm unit]:** alignment with the national oral cancer screening programme and volunteer training curricula
- **National Health Security Office (NHSO):** cost-effectiveness evidence for possible inclusion of AI-assisted screening in preventive benefits
- **Thai Food and Drug Administration:** early consultation on regulatory classification of the AI as Software as a Medical Device
- **National Cancer Institute of Thailand:** data alignment with the cancer registry and national cancer control planning

---

## How will you manage use and mobilization of the research? {limit: 1000 words}
Our strategy is to involve the people who will use the results from the start, and to produce outputs in forms they can act on.

1. **Co-production with knowledge users.** A project steering group includes Health Region 10 and provincial health office representatives, hospital dentists, volunteer leaders and the Mahidol team. It meets quarterly to review results and decide on changes.
2. **Tailored products for each audience:**
   - **Health authorities:** policy briefs (Thai and English) on cost per screen, cost per high-risk case referred, and referral efficiency; the continuity-of-screening playbook
   - **Hospitals:** implementation guide covering staffing, workflow, and the dashboard triage protocol
   - **Volunteers:** picture-based training manual, training game, and refresher videos in Thai and local languages [FILL: e.g. Isan/Lao, Khmer, Kui, if relevant]
   - **Researchers:** open-access papers (validation per STARD and TRIPOD+AI; implementation outcomes), and a model card describing performance and limits
   - **Communities:** feedback sessions in pilot villages about results and oral cancer risk factors
3. **Training of trainers:** 20 lead volunteers become certified trainers, so capacity stays in the community.
4. **Open standards:** we will publish our image-acquisition protocol and quality-assurance metrics so other programmes can adopt them.
5. **Events:** a regional dissemination workshop with Regions 7, 9 and 10 at month [FILL]; presentations to MOPH.
6. **Monitoring use:** we track uptake indicators such as hospitals adopting the protocol, volunteers trained beyond the project, and policy references.

Example: if the pilot shows that AI triage cuts unnecessary referrals by [FILL target]% with no loss of sensitivity, we will bring a costed proposal to the Health Region 10 service-plan committee for expansion to Regions 7 and 9.

---

## Who are the end users? Did they participate in design, and how will they be engaged?
**End users:**
1. Village health volunteers, who screen
2. Dentists, dental nurses and doctors at district/provincial hospitals, who triage and diagnose
3. Programme managers at the Provincial Health Office and Health Region office
4. Ultimately, adults aged 40+ at risk of oral cancer

**Participation in design so far:** [FILL: e.g. number of volunteers and dentists consulted; how]. Concrete design changes that came from users: the picture-based manual (language and literacy needs) and the cascade training model (20 lead trainers) [FILL: others].

**During the project:** usability testing rounds (months [FILL]); structured surveys and focus groups with volunteers and dentists; volunteer representatives on the steering group; patient feedback on acceptability.

**After the project:** volunteer trainers and hospital dentists will lead roll-out in new districts.

---

## What are the potential opportunities to scale the research innovations, or potential for uptake and policy adoption? {limit: 1000 words}
- **Within Thailand:** Thailand already runs community oral cancer screening through more than a million village health volunteers nationwide. KPD upgrades an existing national programme rather than creating a new one, which lowers the barrier to adoption. The scale-up path runs from Health Region 10 → Regions 7 and 9 → the national programme, through MOPH and NHSO.
- **Regionally:** high-burden countries in South and Southeast Asia, including Cambodia, Laos, Myanmar, India, Bangladesh, Sri Lanka and Malaysia, have similar risk factors and community health worker systems.
- **Policy adoption:** cost-effectiveness evidence (Objective 3) is what decision-makers need. We will present it in the formats used for Thai health-technology decisions [FILL: e.g. HITAP-style economic evaluation].
- **Business sustainability:** KPD is structured as a social-impact company. After the pilot, hospitals and health authorities can contract for the software, and volunteer training is embedded in existing structures.
- **Platform effect:** the same volunteer-to-dashboard workflow can support other screening programmes.

## How does your proposal work, why, for whom, to what extent, and in what contexts? What technical, social and institutional factors must be addressed to scale?
We will use a **realist evaluation** lens, asking what works, for whom, and in what circumstances.
- **Technical:** model robustness across phone models, lighting and skin and mucosal tones; connectivity; device supply and maintenance; data security. *Design response:* external validation by site and device; image-quality checks; offline mode; performance monitoring after deployment.
- **Social:** volunteer workload, confidence and literacy; patient trust in AI and willingness to travel for referral; stigma; gender roles (see gender section). *Design response:* picture-based training; peer trainers; community feedback sessions; tracking referral completion and the reasons for non-attendance.
- **Institutional:** dentist capacity to review cases; integration with hospital information systems; financing (who pays); regulation. *Design response:* steering group with health authorities; dashboard designed around dentists' existing triage; NHSO and Thai FDA engagement; cost-effectiveness analysis.

We will compare implementation outcomes across hospitals and districts with different resources to identify the conditions needed for success at scale.

---

## How will your project address and integrate gender considerations? {limit: 1000 words}
Gender shapes who is at risk, who screens and who benefits.

1. **Risk factors differ by sex.** In rural Thailand, betel quid chewing is concentrated among older women, while smoking and heavy drinking are more common among men. Our recruitment, risk survey and analyses will be **sex- and age-disaggregated**, and outreach messages will be tailored, e.g. betel-cessation messages for older women and tobacco and alcohol messages for men.
2. **Most village health volunteers are women.** The project relies on their unpaid or low-paid labour. We will measure the added **time burden** per screen, provide fair compensation for training days and travel [FILL: amount], and create recognised roles: certified lead trainers, with leadership opportunities for women volunteers.
3. **Access barriers.** Women may face caregiving duties and men may face work-related constraints that prevent attending referrals. We will record reasons for non-attendance by sex and test solutions such as flexible appointment times and transport support.
4. **Algorithmic fairness.** We will report model sensitivity and specificity separately for women and men and by age group. If performance differs, we will collect more data and recalibrate.
5. **Privacy and dignity.** Intraoral photos can be sensitive. Participants can choose a same-sex volunteer where feasible; photos are cropped to the mouth; consent is explained in plain Thai.
6. **Team.** [FILL: gender composition of the team and leadership; plan to include women researchers and volunteer leaders in decision-making.]

**Indicators:** screening uptake by sex; referral completion by sex; volunteer time burden; model performance by sex; % women in trainer and leadership roles.

---

## Ethical challenges and review {limit: 1000 words}
**Ethical oversight:** approved by [FILL: name of ethics committee, e.g. Mahidol University Faculty of Dentistry / Faculty of Medicine IRB, approval number and date]; site approvals at [FILL: each hospital]. Any amendments will be submitted before changes are made. [FILL: up to 5 links]

**Key challenges and how we manage them:**
1. **Informed consent:** written consent in Thai (verbal and witnessed for participants who cannot read), covering screening, photographs, and use of de-identified images to improve the AI. Participants can refuse image storage and still be screened.
2. **Identifiable images:** photos are framed on the oral cavity, with no full face. Metadata are stripped; images are linked to a coded ID; the key is held separately by the hospital.
3. **Data protection (Thailand PDPA 2019):** health data are "sensitive personal data". We define the data controller ([FILL: hospital/Mahidol]) and processor (KPD); data are encrypted in transit and at rest and stored in [FILL: location/cloud region]; access is role-based; there is a data-sharing agreement among partners; a data protection officer is named [FILL].
4. **AI is decision support, not diagnosis:** volunteers refer per protocol, dentists make clinical decisions, and biopsy confirms. No patient is denied referral because of a low AI score if the volunteer or dentist is concerned.
5. **Duty of care:** every high-risk result is referred and tracked; we follow up patients who do not attend. Incidental findings are referred.
6. **Bias and fairness:** subgroup performance monitoring (see gender section).
7. **Data ownership and benefit-sharing:** Thai partner institutions retain ownership of patient data. KPD licences the use of de-identified data for model development under the data-sharing agreement [FILL: confirm terms], and partners share in publications.
8. **Conflict of interest:** KPD is a company. Team members disclose financial interests, and independent hospital dentists and Mahidol co-investigators conduct the validation analyses.
9. **Regulation:** consultation with the Thai FDA before clinical use outside the research protocol.

---

## Project Management and Collaboration {limit: 1000 words}
**Structure:**
- **Principal Investigator / lead institution:** Dr. Narawitchz Wareekul, Mahidol University [FILL: faculty, title]. Responsible for scientific direction, ethics and clinical validation.
- **Technology partner:** Kon Pop Detection (CEO Ernest Choi; CTO Amir Fleurizard). Responsible for the app, AI model, dashboard, data infrastructure and technical support.
- **Implementation partners:** [FILL: hospital names] in Health Region 10. They provide site leads, dentist reviewers, volunteer supervision and referral management.
- **Academic collaborators:** Harvard GAMI [FILL: role], MIT [FILL: role], University of Michigan [FILL: role, e.g. biostatistics, health economics].
- **Steering group:** PI, KPD, a hospital site lead from each hospital, a Health Region 10 / Provincial Health Office representative, and a volunteer representative. Meets quarterly.
- **Day-to-day:** project coordinator [FILL]; monthly team meetings; shared task tracker; risk register.

**History of collaboration:** [FILL: e.g. "The team formed at MIT Grand Hack 2025; Dr. Wareekul has worked with [hospitals] on community screening since [year]; mini-pilots in [month/year]."]

**Shared ownership:** joint authorship policy agreed at the start; Thai institutions own patient data; results are presented jointly to health authorities; IP arrangements are set out in a collaboration agreement [FILL].

**Risk management:**
| Risk | Mitigation |
|---|---|
| Too few cancer/high-risk cases for validation | Enrich with archived hospital images; extend recruitment; add sites |
| Poor image quality in the field | In-app quality checks; refresher training; lead-trainer supervision |
| Volunteer drop-out | Compensation; recognition; peer support |
| Low referral completion | Patient tracking; reminders through volunteers; transport support |
| Model performs worse at new sites | External validation; site recalibration; continuous monitoring |
| Regulatory delay | Early Thai FDA consultation; research-use framing during the pilot |

---

## Relevant Experience and Related Work {limit: 1000 words}
- **Dr. Narawitchz Wareekul:** [FILL: clinical experience; community screening experience; publications. Your draft says "[CV of Dentist]"; insert a summary here.]
- **Ernest Choi:** Harvard graduate student [FILL: programme]; three-time founder [FILL: companies, outcomes].
- **Amir Fleurizard:** M.Sc., UNC Charlotte; full-stack engineer [FILL: relevant AI/health software experience].
- **KPD work to date:** MIT Grand Hack 2025 [FILL: Google award]; Harvard GAMI incubator; app, dashboard, model and training game built; ethics approval; mini-pilots.

**Related work by others (keep, from your draft):** community-based oral screening programmes identify OPMDs and early cancers, but their effectiveness is limited by examiner variability, specialist shortages and weak referral systems. Computer-vision models for oral lesions have shown promise but are mostly developed in high-resource settings and may not generalise to low-income screening contexts. KPD addresses this gap by training and validating in the intended deployment setting.

**Links (up to 5):** [FILL: website; Grand Hack/Google award page; any preprint or poster; GAMI profile; Mahidol profile]

---

## Excellence of Research Team {limit: 500 words}
Our team combines clinical, technical and entrepreneurial expertise with deep links to the communities we serve.

- **Clinical leadership:** Dr. Narawitchz Wareekul (Mahidol University) brings dental expertise and first-hand experience of community oral screening with volunteers in Thailand. He leads clinical protocol design, labelling standards and validation.
- **Technology:** Amir Fleurizard (CTO) designs and builds the app, dashboard and AI pipeline, with experience in full-stack and machine-learning deployment.
- **Implementation and strategy:** Ernest Choi (CEO), a Harvard graduate student and three-time founder, leads partnerships, operations and the path to sustainability.
- **Partners:** hospital dentists and site leads in Health Region 10 [FILL]; academic collaborators at Harvard GAMI, MIT and the University of Michigan [FILL: named people and expertise, e.g. biostatistics, health economics, implementation science].

> **Gaps reviewers will notice; fill them with named people:** an **oral pathologist** (biopsy reference standard), a **biostatistician/epidemiologist**, a **health economist** (Aim 3), and a **gender/social scientist** (required by this call). Add them as co-investigators.

**Interdisciplinarity:** clinical dentistry, pathology, AI engineering, public health, health economics and social science, working with volunteers and health authorities as knowledge users.

**Inclusivity plan:** women in leadership roles among investigators and volunteer trainers [FILL: numbers]; Thai-based team members lead community work; training opportunities for Thai students and early-career researchers [FILL: e.g. 2 graduate students]; materials in local languages.

---

## Timeline and deliverables
> Updated from your draft, which had dates in the past. Adjust to the call's start date.

| Period | Activities | Deliverables |
|---|---|---|
| Months 1–3 | Ethics amendments; data-sharing agreement; recruit staff; finalise MVP (image-quality checks, offline mode); training manual | Signed agreements; MVP v1.0; Thai training manual |
| Months 2–4 | Train 20 lead trainers → 300 volunteers | Training completion report; baseline survey |
| Months 4–9 | 6-month pilot in Health Region 10 [FILL: districts]; continuous data collection; usability surveys | Monthly dashboards; interim report |
| Months 6–12 | Model refinement; external validation at hold-out hospital; biopsy follow-up | Validation report (STARD/TRIPOD+AI) |
| Months 9–14 | Economic evaluation; gender analysis; continuity-of-screening playbook | Cost-effectiveness report; policy brief; playbook |
| Months 12–18 | Dissemination workshop (Regions 7, 9, 10); scale-up plan; papers | Workshop report; 2 manuscripts; scale-up proposal to MOPH |

## Budget
[FILL: use the call's budget template. AI4PEP's last call allowed ~CAD 362,500 per team over 3 years incl. 13% indirect costs. Confirm the current call's limits.]
