# NSF SBIR/STTR Phase I – Project Pitch Draft (Kon Pop Detection)

**What it is:** NSF's "America's Seed Fund". You first submit a short **Project Pitch**. If NSF invites you, you then submit a full Phase I proposal (historically up to ~$305k **[CONFIRM current amount]**).
**Status:** SBIR/STTR reauthorised in April 2026. Grants.gov lists **NSF 26-511** (SBIR/STTR Phase I, Phase II, Fast-Track, "a pilot emphasis on scientific instrumentation") with a close date of **4 Nov 2026**. Read the solicitation: if the current round emphasises scientific instrumentation, a digital-health AI pitch may not fit this cycle **[CONFIRM at seedfund.nsf.gov, along with whether Project Pitches are open and which topics]**
**Topic to select:** Digital Health, or Artificial Intelligence **[CONFIRM current topic names]**
**Eligibility:** same as SBIR generally: US small business, > 50% US-owned, PI primarily employed by the company at award, and **R&D performed in the US**. NSF funds **technical innovation with high technical risk**, not clinical trials or pilots.

> NSF reviewers want **technical risk**: what is hard, unproven, and worth funding? Focus on the robustness, on-device AI, and quality-gating research, not on the Thai pilot logistics.

> Character limits below are from past NSF Project Pitch forms **[CONFIRM]**.

---

### 1. The Technology Innovation {limit: 3500 chars}
Kon Pop Detection is developing an AI triage system that lets non-specialist health workers detect high-risk oral lesions from smartphone photographs taken in community settings. The core innovation is making medical-image AI reliable outside the clinic: on low-cost phones, under uncontrolled lighting, operated by minimally trained users, with intermittent connectivity.

Our approach combines (1) a medical foundation model (Google's MedGemma) fine-tuned for oral-lesion risk classification, which allows strong performance from limited labelled data; (2) a YOLO-based detector that localises suspicious areas, giving an interpretable output that users can verify; (3) an image-quality gate that evaluates each photo at capture and prompts the user to retake unusable images; and (4) calibrated risk scores that drive a triage queue for clinicians.

This differs from existing oral-cancer AI research, which mostly trains and tests on specialist-acquired hospital images and reports accuracy that does not transfer to field conditions. Our system is designed for the conditions where most oral cancers are missed: community screening in high-burden, low-resource regions and underserved primary-care settings. Success would enable scalable, low-cost screening programmes and create a reusable framework for robust point-of-care image AI.

[FILL: 1–2 sentences on current prototype status and preliminary results]

### 2. The Technical Objectives and Challenges {limit: 3500 chars}
**Objective 1: robustness to acquisition variability.** *Challenge:* model accuracy drops with device, lighting, angle and blur. *R&D:* device- and lighting-stratified evaluation; physics-informed augmentation; test-time quality gating; site-held-out validation. *Target:* AUC drop ≤ [FILL] between best and worst strata.

**Objective 2: reliable, calibrated triage with explainability.** *Challenge:* foundation-model outputs can be over-confident; users need to understand where the lesion is. *R&D:* calibration methods (e.g. temperature scaling, conformal prediction to produce "refer / do not refer / retake" sets with guaranteed error rates); detector-based localisation. *Target:* calibration error ≤ [FILL]; sensitivity ≥ [FILL]% for high-risk lesions at specificity ≥ [FILL]%.

**Objective 3: efficient on-device or low-bandwidth inference.** *Challenge:* the large foundation model is too heavy for low-cost phones and weak networks. *R&D:* knowledge distillation into a compact model; quantisation; hybrid on-device quality check with deferred cloud scoring. *Target:* on-device quality check < [FILL] s on a US$[FILL] phone; full result within [FILL] minutes after connectivity resumes.

**Objective 4: subgroup fairness.** *Challenge:* performance may vary by sex, age and mucosal pigmentation. *R&D:* stratified evaluation and mitigation. *Target:* no subgroup sensitivity more than [FILL] points below overall.

### 3. The Market Opportunity {limit: 1750 chars}
Oral cancer causes ~177,000 deaths per year. Most occur in South and Southeast Asia, where public health systems already run community screening using non-specialist workers; Thailand alone has more than a million village health volunteers. Late-stage treatment costs about five times more than early-stage treatment, so payers have a direct economic incentive to improve early detection. Customers are public health systems, hospitals and insurers (B2G/B2B software-as-a-service, priced per screen or per site). In the US, dental and primary-care practices and community health centres serving high-risk populations, plus teledentistry platforms, are a secondary market. [FILL: pricing hypothesis; market size with sources; customer discovery done, e.g. "__ interviews with hospital directors and dentists"]

### 4. The Company and Team {limit: 1750 chars}
Kon Pop Detection was founded in [FILL: month] 2025 after the team won [FILL: Google award] at MIT Hacking Medicine's Grand Hack, and it is part of the Harvard GAMI incubator.
- **CTO Amir Fleurizard** (M.Sc., UNC Charlotte) built the app, dashboard and AI pipeline [FILL: AI/ML experience].
- **CEO Ernest Choi** is a Harvard graduate student and three-time founder.
- **CMO Dr. Narawitchz Wareekul** is a dentist at Mahidol University with community screening experience.

Collaborators include MIT, the University of Michigan, and partner hospitals in Thailand. [FILL: incorporation state; which founder would be the PI and their employment status with KPD]
