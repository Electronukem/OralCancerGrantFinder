# NRCT (วช.) – Draft Proposal: Multi-site Validation of an AI Model for Oral Cancer Risk Detection from Community Smartphone Images

**Applicant (PI):** Dr. Narawitchz Wareekul, Mahidol University [FILL]. **KPD is the technology collaborator.**
**Submission:** NRIIS (Thai), certified by Mahidol's research office before the deadline. NRCT calls for FY2571 funding are expected roughly **Nov 2026–Apr 2027 [CONFIRM the programme/topic, e.g. medical & public health, AI, or ageing society]**.
**How this differs from the HSRI proposal:** NRCT gets the **scientific/technical validation** (dataset, model accuracy, external validation, reader study). HSRI gets the **health-system implementation and cost-effectiveness**. Funders check for overlap, so keep the aims distinct and declare both applications.

---

## ชื่อโครงการ
**TH:** การพัฒนาและตรวจสอบความถูกต้องของแบบจำลองปัญญาประดิษฐ์สำหรับประเมินความเสี่ยงมะเร็งช่องปากจากภาพถ่ายสมาร์ทโฟนในการคัดกรองระดับชุมชน: การศึกษาแบบพหุสถาบัน
**EN:** Development and multi-site validation of an AI model for oral cancer risk assessment from community smartphone images

## บทคัดย่อ (draft; check wording with a native speaker)
การคัดกรองมะเร็งช่องปากในชุมชนอาศัยการตรวจด้วยตาโดยบุคลากรที่ไม่ใช่ผู้เชี่ยวชาญ ซึ่งมีความแม่นยำแตกต่างกันมาก แบบจำลองปัญญาประดิษฐ์ที่มีอยู่ส่วนใหญ่พัฒนาจากภาพถ่ายในโรงพยาบาล จึงอาจใช้ไม่ได้ดีกับภาพที่ถ่ายด้วยสมาร์ทโฟนราคาประหยัดในสภาพแสงที่หลากหลายในชุมชน โครงการนี้จะสร้างชุดข้อมูลภาพช่องปากที่มีผลการวินิจฉัยอ้างอิงจากทันตแพทย์ผู้เชี่ยวชาญและผลชิ้นเนื้อจากโรงพยาบาล [FILL] แห่ง พัฒนาแบบจำลองโดยปรับแต่งโมเดลพื้นฐานทางการแพทย์ (MedGemma) ร่วมกับโมเดลตรวจจับรอยโรค (YOLO) และตรวจสอบความถูกต้องกับข้อมูลจากโรงพยาบาลที่ไม่ได้ใช้ในการฝึก รวมทั้งศึกษาผลของการใช้ปัญญาประดิษฐ์ช่วยต่อความแม่นยำของ อสม. และบุคลากรสาธารณสุข ผลลัพธ์ที่คาดหวังคือแบบจำลองที่ผ่านการตรวจสอบความถูกต้องพร้อมสำหรับการใช้งานจริง (TRL 6) ชุดข้อมูลมาตรฐาน และบทความวิชาการ

---

## หลักการและเหตุผล (Rationale)
Use HSRI §1 (burden, current screening model). Add the **technical gap**: published oral-lesion AI is trained on clinical/specialist images, generalises poorly to community conditions, and is rarely validated externally in Thailand. A Thai, multi-site, biopsy-referenced dataset and an externally validated model do not yet exist [FILL: verify with a literature search; cite the closest Thai studies].

## วัตถุประสงค์ (Objectives)
1. Build a standardised, multi-site oral image dataset with reference-standard labels (dentist panel + histopathology)
2. Develop and internally validate the AI model (risk classification + lesion localisation + image-quality gate)
3. Externally validate the model at a hospital not used in training, with performance reported by device, lighting, sex and age
4. Measure the effect of AI assistance on the accuracy of volunteers and non-specialist health workers (reader study)

## ขอบเขต (Scope)
[FILL: number of hospitals and images; time period; exclusions]

## ระเบียบวิธีวิจัย (Methods)
- **Data:** retrospective archived images + prospective standardised capture (3 views per patient) at [FILL] hospitals; target [FILL] images including ≥ [FILL] histologically confirmed OPMD/cancer
- **Labelling:** two calibrated dentists label independently, a third adjudicates; biopsy results take precedence; inter-rater kappa reported
- **Model:** fine-tune MedGemma; YOLO detector; quality classifier; calibration; train/validation/test split **by patient**, external test **by hospital**
- **Metrics:** AUC, sensitivity, specificity, PPV/NPV with 95% CI; calibration; subgroup analysis; TRIPOD+AI and STARD reporting
- **Reader study:** [FILL: N] volunteers/health workers × [FILL: N] cases, with vs without AI, analysed with a multi-reader multi-case method
- **Ethics & data:** Mahidol EC + site approvals; Thai PDPA; de-identification; data-sharing agreement; Thai institutions own patient data

## TRL / SRL
TRL [FILL: e.g. 4 → 6]; SRL [FILL: e.g. 3 → 5]

## ผลผลิต / ผลลัพธ์ / ผลกระทบ (Outputs / Outcomes / Impact)
- **Outputs:** validated model; dataset with standard protocol; ≥ [FILL] international publications; model card; image-acquisition standard
- **Outcomes:** the model is ready for implementation studies (HSRI) and Thai FDA submission
- **Impact:** earlier diagnosis; Thai capability in medical AI

## งบประมาณ (Budget)
Thai government categories as in the HSRI file. Emphasise labelling/expert time, histopathology, data management, compute (or credits), and publication.

## ความสอดคล้องกับแผนด้าน ววน. (Alignment)
[FILL: cite the current NRCT/TSRI programme or OKR the call names, e.g. medical & health innovation, AI for health]

## Attachments
☐ NRIIS profiles ☐ Hospital letters ☐ Collaboration agreement with KPD (IP, data, conflict of interest) ☐ Ethics status ☐ CVs
