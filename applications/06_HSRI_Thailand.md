# HSRI (สวรส.) – Draft Proposal: AI-Assisted Oral Cancer Screening by Village Health Volunteers in Health Region 10

**Applicant (PI):** Dr. Narawitchz Wareekul, Mahidol University [FILL: faculty/position]. HSRI funds Thai institutions, not foreign companies. **KPD participates as technology partner/collaborator.**
**Submission:** NRIIS + Mahidol's research-management system, **in Thai**. HSRI's annual call has opened around **Feb–Apr**; the FY2571 call is expected ~Feb–Apr 2027 **[CONFIRM]**. Contact the HSRI programme officer early.
**Form:** HSRI provides separate forms for **health-systems research (งานวิจัยเชิงระบบ)** and **clinical research (งานวิจัยทางคลินิก)**. **Use the health-systems form.** This proposal is about the screening *service model*, referral efficiency and cost.
**Why HSRI fits best among Thai funders:** HSRI funds research that changes how the Thai health system delivers services, and Objective 3 (cost-effectiveness) and the Health Region 10 implementation are exactly that.

> Below: Thai title and abstract (draft, **please have a native-speaking team member check the wording**) + English section drafts to translate into the HSRI form.

---

## ชื่อโครงการ (Title)
**TH:** การพัฒนาและประเมินระบบคัดกรองมะเร็งช่องปากด้วยปัญญาประดิษฐ์โดยอาสาสมัครสาธารณสุขประจำหมู่บ้าน (อสม.) ในเขตสุขภาพที่ 10: การศึกษาความเป็นไปได้ ความแม่นยำ และความคุ้มค่า
**EN:** Development and evaluation of AI-assisted oral cancer screening by village health volunteers in Health Region 10: feasibility, accuracy and cost-effectiveness

## บทคัดย่อ (Thai abstract, draft)
มะเร็งช่องปากเป็นปัญหาสาธารณสุขสำคัญในภาคตะวันออกเฉียงเหนือของประเทศไทย ซึ่งมีปัจจัยเสี่ยงสูง เช่น การเคี้ยวหมาก การสูบบุหรี่ และการดื่มแอลกอฮอล์ ผู้ป่วยส่วนใหญ่ได้รับการวินิจฉัยในระยะลุกลาม ทำให้อัตราการรอดชีวิตต่ำและค่าใช้จ่ายในการรักษาสูง ปัจจุบันการคัดกรองในชุมชนดำเนินการโดย อสม. ซึ่งได้รับการอบรมเพียงประมาณ 1 วัน และบันทึกข้อมูลด้วยแบบฟอร์มกระดาษ ส่งผลให้ความแม่นยำในการคัดกรองแตกต่างกันมาก และมีทั้งการพลาดรอยโรคที่มีความเสี่ยงสูงและการส่งต่อที่ไม่จำเป็น โครงการนี้จะพัฒนาและประเมินแอปพลิเคชัน Kon Pop Detection ซึ่งให้ อสม. ถ่ายภาพช่องปากด้วยสมาร์ทโฟน และใช้ปัญญาประดิษฐ์ประเมินความเสี่ยง พร้อมระบบแดชบอร์ดให้ทันตแพทย์จัดลำดับความเร่งด่วนในการตรวจ การศึกษาจะดำเนินการในเขตสุขภาพที่ 10 ร่วมกับโรงพยาบาล [FILL] แห่ง และ อสม. ประมาณ 300 คน โดยประเมิน (1) ความแม่นยำของระบบเทียบกับการตรวจโดยทันตแพทย์และผลชิ้นเนื้อ (2) ความเป็นไปได้และการยอมรับในการใช้งานจริง และ (3) ต้นทุนและความคุ้มค่าเมื่อเทียบกับการคัดกรองแบบเดิม ผลการศึกษาจะนำไปสู่ข้อเสนอเชิงนโยบายต่อกระทรวงสาธารณสุขและสำนักงานหลักประกันสุขภาพแห่งชาติ เพื่อขยายผลการคัดกรองมะเร็งช่องปากด้วยปัญญาประดิษฐ์ในระดับเขตและระดับประเทศ

## คำสำคัญ (Keywords)
มะเร็งช่องปาก; ปัญญาประดิษฐ์; การคัดกรอง; อาสาสมัครสาธารณสุขประจำหมู่บ้าน; ความคุ้มค่า; เขตสุขภาพที่ 10 / oral cancer; artificial intelligence; screening; village health volunteers; cost-effectiveness

---

## 1. ความสำคัญและที่มาของปัญหา (Problem & health-system significance)
- Burden: oral cancer incidence and mortality in Thailand and the northeast [FILL: GLOBOCAN 2022 Thailand figures; Thai Cancer Registry; late-stage % from Health Region 10 hospitals]
- Risk factors in Health Region 10: betel quid chewing (especially older women), tobacco, alcohol [FILL: local survey data if available]
- **Current service model:** Thailand's oral cancer screening for adults aged 40+. Village health volunteers complete a paper risk questionnaire (smoking, alcohol, betel, ill-fitting dentures) and refer at-risk people to a doctor, dentist or dental nurse. Volunteers receive about one day of training.
- **System problems:**
  1. Variable accuracy of visual screening by non-specialists (Cochrane review, Walsh et al. 2021)
  2. Scarce dentists in the region [FILL: dentist-to-population ratio in Region 10 provinces]
  3. Paper data delays and no prioritisation
  4. Patient costs from unnecessary referrals, and loss to follow-up of true positives
- **Cost to the system:** late-stage treatment costs about five times more than early-stage (US$2,027 vs US$394 per patient per year, Malaysia; Raman et al. 2021) [FILL: Thai costing data if available, e.g. UCS reimbursement for oral cancer surgery and radiotherapy]

## 2. คำถามการวิจัย (Research questions)
1. How accurate is AI-assisted screening by village health volunteers, compared with dentist examination and biopsy, in Health Region 10?
2. Is AI-assisted screening feasible and acceptable within the existing volunteer–sub-district health promoting hospital (รพ.สต.)–community hospital referral system?
3. What is the cost per screen and per high-risk case appropriately referred, and is AI-assisted screening cost-effective for the Universal Coverage Scheme compared with the paper-based approach?

## 3. วัตถุประสงค์ (Objectives)
1. To evaluate the diagnostic accuracy of the Kon Pop Detection AI tool in community screening (sensitivity/specificity for high-risk lesions)
2. To evaluate implementation outcomes (reach, adoption, fidelity, image quality, usability, referral completion, time to dentist review)
3. To estimate costs and cost-effectiveness from the payer (UCS/NHSO) and societal perspectives
4. To develop policy recommendations and an implementation guide for expansion to Health Regions 7 and 9 and nationally

## 4. กรอบแนวคิด (Conceptual framework)
[Diagram] Community screening (volunteer + app) → AI risk score + image quality check → dentist dashboard triage (community/district hospital) → specialist examination → biopsy → treatment
Indicators at each step: coverage; % usable images; % high-risk; positive predictive value; referral completion; time to diagnosis; stage at diagnosis; cost.

## 5. ระเบียบวิธีวิจัย (Methods)
- **Design:** mixed-methods implementation study with an embedded diagnostic accuracy study and economic evaluation. Comparator: [FILL: before/after comparison with historical paper-based screening in the same districts, or comparison districts using standard screening]
- **Setting:** Health Region 10, [FILL: provinces/districts]; hospitals [FILL: e.g. Hua Taphan Hospital (Amnat Charoen) + others]; linked sub-district health promoting hospitals (รพ.สต.)
- **Participants:** adults aged ≥ 40 screened by volunteers; ~300 volunteers; dentists/dental nurses at participating hospitals
- **Sample size:** [FILL: based on expected prevalence of high-risk lesions and target precision for sensitivity (e.g. ± 10%); explain]
- **Reference standard:** examination by a dentist blinded to the AI result; biopsy when clinically indicated; expert-panel review of images for screen-negative samples [FILL: e.g. random __% sample of negatives examined]
- **Implementation outcomes:** RE-AIM framework: volunteer adoption, fidelity, usability (System Usability Scale), time per screen, image-quality pass rate, referral completion, time from screen to dentist review
- **Economic evaluation:** micro-costing of screening, training, devices, software, referrals and biopsies; cost per screen; cost per high-risk case referred; decision model of lifetime costs and QALYs using Thai cost and survival data, following Thai HTA guidelines [FILL: cite HITAP guideline]; budget-impact analysis for the region
- **Qualitative:** focus groups with volunteers, dentists and patients; interviews with Provincial Health Office and Health Region 10 managers
- **Gender analysis:** all outcomes disaggregated by sex and age

## 6. ผลที่คาดว่าจะได้รับและการนำไปใช้ประโยชน์ (Expected results & policy use)
| Output (ผลผลิต) | Outcome (ผลลัพธ์) | Impact (ผลกระทบ) |
|---|---|---|
| Accuracy & implementation report; cost-effectiveness report; policy brief; implementation guide; trained volunteer trainers (20) and volunteers (300) | Health Region 10 decides on expansion; NHSO considers financing; referral efficiency improves | More early-stage diagnoses; lower mortality and treatment costs; a national model for AI-assisted primary-care screening |

**Users of results:** Health Region 10 office; Provincial Health Offices; Department of Health (Bureau of Dental Health) [CONFIRM unit]; NHSO; participating hospitals.

## 7. แผนการดำเนินงาน (Work plan, 18 months [CONFIRM HSRI duration])
| Months | Activity |
|---|---|
| 1–3 | Ethics approvals (Mahidol + sites), data agreements, protocol, staff |
| 2–4 | Train 20 lead trainers → 300 volunteers; baseline data |
| 4–10 | Screening and data collection; referral tracking |
| 8–14 | Accuracy analysis; qualitative study; costing |
| 12–16 | Economic model; policy brief; implementation guide |
| 16–18 | Stakeholder workshop (Regions 7, 9, 10); final report |

## 8. งบประมาณ (Budget, Thai government categories) [FILL amounts]
| หมวด | รายการ | บาท |
|---|---|---|
| ค่าตอบแทน | Volunteer compensation for training/screening days; expert reviewers; focus-group participants | |
| ค่าจ้าง | Project coordinator; research assistants (×[FILL]); data manager | |
| ค่าวัสดุ | Biopsy and histopathology consumables; printing training manuals | |
| ค่าใช้สอย | Training workshops; travel to districts; patient travel support for referral; cloud hosting and data security | |
| ค่าครุภัณฑ์ | Smartphones for volunteers [justify or source elsewhere] | |
| ค่าธรรมเนียมอุดหนุนสถาบัน | Mahidol overhead [CONFIRM rate] | |
| **รวม** | | |

> **Conflict of interest:** KPD is a company that may profit from adoption. State this, and keep the accuracy and cost analyses under Mahidol/hospital investigators, ideally with an independent statistician. HSRI reviewers will look for this.

## 9. การเผยแพร่และผลักดันเชิงนโยบาย (Dissemination & policy translation)
Policy brief (Thai) to Health Region 10 and NHSO; presentation at the Health Region service-plan committee; academic publications; open implementation guide.

## Attachments checklist
☐ NRIIS registration (PI and co-investigators) ☐ Letters from hospital directors [FILL] ☐ Letter from Health Region 10 / Provincial Health Office ☐ Ethics approval or submission evidence ☐ CVs (Thai) ☐ Collaboration agreement with KPD (data, IP, conflict of interest)
