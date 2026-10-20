# MIT Solve 2027 Global Health Challenge – Draft Application (Kon Pop Detection)

**Deadline: Monday 2 November 2026, 12:00 PM (noon) US Eastern, NOT end of day.** Submit early; you can keep editing after submitting.
**Prize:** US$10,000 Solver grant + eligibility for sponsor prizes (e.g. **AI for Humanity Prize, up to $150,000**; **Crescent Enterprises AI for Social Innovation Prize, up to $100,000**). Average Solver funding ~$40k.
**Challenge question:** "How can we use technology to make good health and quality care more equitable for all?"
**Apply:** https://solve.mit.edu/challenges/2027-global-health-challenge

> ⚠️ **Solve's rules on AI-written applications:** Solve "does not recommend using generative AI tools to write your application", and you must tick a box confirming nothing is fabricated or exaggerated. **Use this draft as raw material. Rewrite every answer in your own words and voice**, add your real stories, and replace every **[FILL]**. Solve reviewers want to hear the founders' passion and first-hand experience.
> ⚠️ Answers in "Page 1: Solution Profile" become **public** if you reach Semifinalist.
> Run `python check_limits.py applications\01_MIT_Solve_2027_Global_Health.md` to check word limits after editing.

---

## PAGE 1 – Solution Profile (public if Semifinalist)

### Name of your organization
Kon Pop Detection [FILL: exact legal name, e.g. "Kon Pop Detection, Inc."]

### Name of your solution {limit: 30 chars}
Kon Pop Detection

### One-line summary {limit: 150 chars}
AI-assisted smartphone screening that helps village health volunteers find oral cancer early and fast-track high-risk patients.

### City/town/region of headquarters
[FILL: e.g. Cambridge, MA, or the city where the company is registered and the senior team is based]

### Country of headquarters
[FILL: United States / Thailand – must match where the company is registered]

### Type of organization
For-profit [FILL: confirm]

### Elevator pitch video (≤ 2 minutes, public YouTube/Vimeo link)
[FILL: link] Strongly recommended. Suggested 2-minute script:
1. (0:00–0:20) Ernest: why this matters personally (both parents had cancer).
2. (0:20–0:50) Dr. Wareekul at a community screening: volunteers with one day of training and a paper form.
3. (0:50–1:30) **Live demo:** register a patient → take 3 photos → AI marks the lesion → dentist dashboard shows the prioritised case.
4. (1:30–2:00) Pilot in Health Region 10, what you need from Solve.

### What specific problem are you solving? {limit: 200 words}
Oral cancer kills about 177,000 people every year, and the burden falls hardest on South and Southeast Asia, where betel quid, tobacco and alcohol use are common. Caught early, oral cancer is usually curable with surgery. Caught late, survival drops sharply and treatment costs roughly five times more: about US$2,027 vs US$394 per patient per year in a Malaysian public-hospital study.

In rural Thailand, the first and often only screening contact is a village health volunteer. Volunteers receive about one day of training, record risk factors on a paper form, and must judge by eye which mouth lesions need a dentist. Paper results move slowly to hospitals. Dentists see both missed cancers and many unnecessary referrals. Patients referred unnecessarily lose wages and travel long distances, and genuinely high-risk patients can be lost to follow-up.

In Health Region 10 in northeast Thailand (Ubon Ratchathani, Sisaket, Yasothon, Amnat Charoen, Mukdahan), [FILL: number of adults aged 40+ eligible for oral cancer screening; number of dentists per population; % of oral cancers diagnosed at late stage, with source].

We are solving the gap between the first community contact and a fast, accurate referral.

### What is your solution? {limit: 200 words}
Kon Pop Detection turns a volunteer's smartphone into an oral cancer screening tool.

A trained volunteer registers the patient, records risk factors (tobacco, alcohol, betel quid) in the app instead of on paper, and takes three standardised photos of the mouth. Our AI checks image quality, marks suspicious areas and produces a risk score. It combines Google's MedGemma medical foundation model, fine-tuned on our oral-lesion images, with a YOLO lesion-detection model.

Results flow to a dashboard where hospital dentists review cases ranked by risk and bring high-risk patients in first for examination and biopsy. The app runs on low-cost phones and copes with patchy internet [FILL: describe how, e.g. "photos are stored on the phone and upload automatically when a signal returns"].

Volunteers learn with a picture-based training manual and a training game that teaches them to take usable photos and recognise warning signs.

The AI does not diagnose. It supports the volunteer's decision to refer and the dentist's decision on who to see first, and a clinician confirms every high-risk result.

[FILL: demo video link, if separate from the pitch video]

### Who does your solution serve, and in what ways will it impact their lives? {limit: 200 words}
We serve adults aged 40 and over in rural northeast Thailand, especially people who chew betel quid, smoke or drink alcohol. Many are farmers or older adults living far from a hospital dentist; in our region betel chewing remains common among older rural women, while smoking and drinking are more common among men. Today their only screening is a short visual check by a volunteer with one day of training, and if referred they may travel hours and lose a day's income.

With Kon Pop Detection:
- **Patients** are more likely to have a dangerous lesion noticed early, when treatment is simpler, cheaper and usually curative, and less likely to make an unnecessary trip.
- **Village health volunteers**, who are mostly women, get a tool that makes their screening more accurate and their work more valued, replacing paper forms with a simple app.
- **Hospital dentists** in short supply see the highest-risk patients first instead of a long, unsorted referral list.

In our pilot we aim to reach [FILL: number] adults through [FILL: number, e.g. 300] volunteers linked to [FILL: 3–4] hospitals [FILL: names, e.g. Hua Taphan Hospital, Amnat Charoen].

### Checkboxes (internal)
☐ Terms of Service / Media Release / Privacy Policy ☐ AI-tools processing notice ☐ **No fabricated or exaggerated information.** Check every number before ticking.

---

## PAGE 2 – Eligibility

### Is technology a core part of your solution?
Yes, tech is core to our solution.

### Does your solution address a health or healthcare access problem?
Yes

### What is your solution's stage of development?
> Choose honestly. **Pilot** = launched in at least one community, still iterating (often 10+ users). **Prototype** = working version still being tested, little or no investment raised. If the Health Region 10 pilot has started screening real patients with volunteers, choose **Pilot**. If only "mini pilots" have happened, consider **Prototype**.

[FILL: Pilot / Prototype]

### Why did you select this stage? What have you built and tested so far? {limit: 200 words}
We have a working app and AI model, and we are piloting them with real volunteers and patients in northeast Thailand.

Built so far:
- Volunteer mobile app: patient registration, digital risk-factor survey, guided three-photo capture
- Dentist dashboard that ranks screened patients by AI risk score
- AI model (fine-tuned MedGemma + YOLO detector) trained on [FILL: number] oral images from [FILL: sources]
- A training game for learning to recognise lesions and take good photos

Tested so far:
- Internal validation: [FILL: e.g. "sensitivity __% and specificity __% for high-risk lesions on __ held-out images, compared with specialist diagnosis/biopsy"]
- Mini-pilots: [FILL: number] people screened at [FILL: places/dates]; in one case [FILL: a short, factual description of the patient whose lesion was found early, without identifying details]
- Ethics approval from [FILL: committee name, approval number/date]
- Agreements with [FILL: number] hospitals in Health Region 10
- Pilot launch: [FILL: date; volunteers trained so far; people screened so far]

We call this a [FILL: Pilot/Prototype] because [FILL: e.g. "the tool is in use in one region but we are still refining the model and training approach based on volunteer feedback"].

---

## PAGE 3 – Solution & Team Details

### How many beneficiaries or customers does your solution currently serve?
[FILL: choose honestly: 0 / 1–10 / 11–100 / 101–1,000 / 1,001–10,000 …]

### Website, app, or social media
[FILL: website / app store / LinkedIn link. If none, upload proof such as company registration, a hospital MOU, or a 1-minute demo video]

### Which dimension of the Challenge does your solution most closely address?
**Expand quality primary care to vulnerable communities by supporting frontline health workers or reducing cost, distance, and administrative barriers.**
> This is the strongest fit: you equip village health volunteers, cut unnecessary travel, and replace paper forms. The alternative is "Improve prevention and management of noncommunicable diseases".

### How are you and your team well-positioned to deliver this solution? {limit: 300 words}
> Solve wants **lived experience and engagement with the community**, not credentials. Give real numbers and examples.

Our team brings together the clinic, the community and the code.

Dr. Narawitchz Wareekul, our Chief Medical Officer, is a dentist with Mahidol University [FILL: exact role] who has taken part in community oral cancer screening in rural Thailand alongside village health volunteers. [FILL: how many screening events/years; what he saw first-hand.] He saw that volunteers have about one day of training and a paper form, and that dentists receive referrals too late or for harmless lesions.

Ernest Choi, our CEO, is a Harvard graduate student and three-time founder. His drive is personal: both of his parents have had cancer.

Amir Fleurizard, our CTO, is a full-stack engineer (M.Sc., UNC Charlotte) who built our app, dashboard and AI pipeline.

We designed the tool with the people who will use it. [FILL: e.g. "We interviewed/observed __ volunteers and __ dentists at __ hospitals."] What we learned changed the product:
- Volunteers asked for instructions with pictures rather than text, because of language and literacy needs, so our training manual is picture-based.
- Training cascades through 20 fully trained lead volunteers who train their peers, matching how volunteer networks already work.
- [FILL: one more concrete design change from user feedback, e.g. the three-photo protocol, the risk survey, or offline use.]

We are supported by hospital partners in Health Region 10 [FILL: names], Mahidol University, and the Harvard Global Alliance for Medical Innovation (GAMI) incubator. We also collaborate with MIT and the University of Michigan [FILL: what each contributes]. We hold ethics approval [FILL: details] and began the pilot in [FILL: month/year].

### In which countries do you currently operate?
Thailand [FILL: plus United States, if the company is based there]

### Additional countries in the next year
[FILL: e.g. none, or Malaysia / Cambodia / Laos / India, only if there is a real plan]

### How many people work on your solution team? {limit: 100 words}
[FILL: e.g. "3 co-founders (part-time/full-time?), __ part-time contributors, __ volunteer trainers; plus partner-hospital staff who are not employees."]

### How long have you been working on your solution? {limit: 100 words}
Since early 2025. The team formed at MIT Hacking Medicine's Grand Hack in [FILL: month] 2025, where we won [FILL: exact name of Google award]. We incorporated Kon Pop Detection in November 2025 [FILL: confirm] and have worked on the solution for about [FILL: 1.5] years.

### Why are you applying to Solve? {limit: 200 words}
> Solve says: if your only goal is money, Solve is not the right fit. Name specific **non-financial** barriers.

We have a working tool and a pilot. To reach national scale, we need help with four barriers:

1. **Clinical validation and evidence.** We need advice on designing a rigorous multi-site validation, with biopsy-confirmed outcomes, that the Thai Ministry of Public Health and international funders will trust.
2. **Regulatory pathway.** Our AI is likely to be regulated as Software as a Medical Device in Thailand. We need guidance and partners to navigate approval efficiently.
3. **Government partnerships and business model.** Our long-term buyers are public health systems and insurers. We want introductions to and coaching on selling to governments, including Thailand's MOPH and NHSO, and later other South and Southeast Asian health ministries.
4. **Responsible AI and technical scale.** We want expert review of bias across sex, age and device type, privacy-preserving data handling, and access to compute to retrain our model as data grow.

Funding would let us train more volunteers and extend the pilot from Health Region 10 to Regions 7 and 9. Solve's network of health-system, AI and impact-investor partners is exactly what we lack.

### Team Lead
Ernest Choi (CEO) [FILL: email, phone with country code; backup contact: e.g. Dr. Wareekul or Amir Fleurizard]
> The Team Lead must attend Solver Orientation at MIT on **14–15 April 2027** and Solve Challenge Finals in New York in September.

### Previously selected as a Solver?
No [FILL: confirm]

### Active or past participant in another entrepreneurship network?
Yes: MIT Hacking Medicine Grand Hack 2025; Harvard Global Alliance for Medical Innovation (GAMI) incubator [FILL: others, e.g. Harvard Innovation Labs]

---

## PAGE 4 – More About Your Solution and Business Model

### What makes your solution innovative? {limit: 300 words}
Most AI oral-cancer tools are built on images from well-equipped hospitals, taken by specialists under good lighting. They tend to perform worse in villages, on cheap phones, in poor light. Kon Pop Detection is designed the other way round: for the conditions of community screening.

What is new:
1. **Built into the existing volunteer system.** We do not create a new screening programme; we upgrade the one Thailand already runs. Volunteers keep their role, and the app replaces the paper risk form they already use, so adoption needs little change in behaviour.
2. **Foundation-model approach for small, diverse data.** We fine-tune Google's MedGemma, a medical foundation model, and pair it with a YOLO detector that localises lesions. This lets us learn from fewer images and produce visual explanations (a box on the suspicious area) that volunteers and dentists can check.
3. **Image-quality checks at the point of capture.** The app flags blurry or badly framed photos while the patient is still there, so dentists receive usable images. [FILL: confirm this is built or planned]
4. **Triage, not just detection.** The dentist dashboard ranks patients by risk, so scarce specialist time goes to those who need it most and unnecessary trips are avoided.
5. **Training game and picture-based manual** that make one day of training go further.

Broader impact: the volunteer-AI-dashboard workflow and our image-acquisition standards can be reused for other conditions that volunteers screen for. Our evaluation of cost per screen and per high-risk case referred will give health ministries evidence for buying AI-assisted primary-care screening. Other mobile oral screening efforts exist in the region, such as MeMoSA in Malaysia; we see them as potential partners in building shared standards and regional datasets.

### Theory of change: how and why will your solution have an impact? {limit: 300 words}
**Activities:** train volunteers (cascade from 20 lead trainers); volunteers screen adults aged 40+ with the app; AI scores images; dentists triage through the dashboard; high-risk patients are referred and tracked to biopsy.

**Outputs:** number of people screened; % of photos meeting quality standards; number of high-risk patients identified and referred; time from screening to dentist review.

**Short-term outcomes:** more accurate referrals (more true high-risk lesions found, fewer unnecessary referrals); shorter time to diagnosis; higher volunteer confidence.

**Long-term outcomes:** more oral cancers diagnosed at an early stage; lower mortality; lower costs for patients and the health system; AI-assisted screening adopted in national programmes.

**Evidence for the links:**
- A large cluster-randomised trial in Kerala, India showed that visual oral screening by trained health workers reduced oral cancer deaths among tobacco and alcohol users (Sankaranarayanan et al., *Lancet* 2005). Screening by non-specialists can work, but accuracy depends heavily on training (Cochrane review, Walsh et al. 2021). Our tool targets exactly that weakness.
- Early-stage treatment costs about one fifth of late-stage treatment (Raman et al., *PLoS One* 2021, Malaysia).
- Our own data: [FILL: model accuracy, pilot feedback, e.g. "volunteers rated usability __/100; __% of photos met quality standards"].

**Key assumptions we test in the pilot:** volunteers can take usable photos after training; the model performs well on community images; referred patients actually attend.

### Tech stack and how you know it works {limit: 300 words}
- **Mobile app** (volunteers): [FILL: e.g. Flutter/React Native/Kotlin], Thai-language interface, guided three-photo capture, digital risk survey, [FILL: offline storage and sync]
- **Clinician dashboard** (web/tablet): [FILL: framework]; secure login; patient list ranked by risk; image viewer with AI annotations
- **AI:** Google **MedGemma** (Health AI Developer Foundations) fine-tuned for oral-lesion risk classification, plus a **YOLO** [FILL: version] object detector for lesion localisation; image-quality check model [FILL]
- **Data & infrastructure:** [FILL: cloud provider and region; encryption; de-identification; where data are stored and who owns them]
- **Training data:** [FILL: number of images, sources, how labelled (dentists? biopsy?)]

**How we know it works:**
- [FILL: validation results with numbers: sensitivity, specificity, AUC, test-set size, comparison standard]
- [FILL: pilot usability results]
- [FILL: link to any public evidence: preprint, poster, hackathon page, Google award announcement]

> Solve asks for "proof that it works in the form of an academic paper or some other form of publicly available evidence." If you have none yet, consider posting a short validation report or preprint (e.g. on medRxiv) before the deadline, or link the Grand Hack/Google award page.

**Technologies used (tick):** Machine Learning; Generative AI (MedGemma is a generative model; tick only if you use its text or vision-language capabilities); Imaging and Sensor Technology; Software and Mobile Applications; Big Data [FILL: only if accurate]

### What is your business model? {limit: 300 words}
**Customers (who pays):** hospitals and public health systems. In Thailand these are provincial and district hospitals, Health Region offices and the Ministry of Public Health, and potentially the National Health Security Office (NHSO), which funds preventive services. Later customers include health ministries and insurers elsewhere in South and Southeast Asia, and private dental networks.

**Beneficiaries (who uses it, free of charge):** village health volunteers and the patients they screen.

**What we provide:** a software-as-a-service package: the volunteer app, the AI risk scoring, the dentist dashboard, training materials and the training game, and reporting for programme managers.

**Why they want it:** public systems already pay for volunteer screening and for treating late-stage cancer. Our tool makes the screening they already fund more accurate and reduces costly late-stage treatment and wasted referrals.

**How we deliver:** we pilot with partner hospitals, show results, then sign per-region contracts priced [FILL: e.g. per screen / per facility per year / per region], with training delivered through lead volunteers.

**Primary customer type:** Government (B2G) [or B2B if hospitals contract directly; FILL: choose one]

### What is your plan for becoming financially sustainable, and what evidence do you have? {limit: 300 words}
**Phase 1 (now to 2027): grants and non-dilutive funding** to complete validation and the pilot. Received so far: [FILL: Google award amount; GAMI support; any grants]. Applications in progress: [FILL: e.g. NIH SBIR, HSRI, Harvard President's Innovation Challenge].

**Phase 2 (2027–2028): first paid contracts** with hospitals and Health Region offices in Thailand once the pilot shows accuracy and cost savings. [FILL: any letters of intent or pricing discussions.]

**Phase 3: national and regional scale** through government contracts (MOPH/NHSO) and expansion to other high-burden countries.

**Investment:** we are raising [FILL: amount and type, e.g. pre-seed; Regulation Crowdfunding] to support the team between grants and contracts. Raised to date: [FILL].

**Why the economics work:** treating late-stage oral cancer costs about five times more than early-stage treatment, so a modest price per screen can be repaid by a small number of cancers caught earlier. Our Aim 3 cost-effectiveness analysis will measure this directly and support procurement decisions.

[FILL: evidence of success so far: awards with amounts, in-kind support (compute credits, hospital staff time), revenue if any.]

---

## Before you submit – checklist
- ☐ Every **[FILL]** replaced; every number checked against a source
- ☐ Answers rewritten in your own voice (Solve penalises generic AI-sounding text)
- ☐ Word/character limits checked (`python check_limits.py ...`)
- ☐ 2-minute video uploaded and set to **public**
- ☐ Team Lead available 14–15 April 2027 (Cambridge, MA)
- ☐ Submitted before **12:00 noon ET, 2 Nov 2026** (= **midnight 00:00, 3 Nov, Thailand time**)
