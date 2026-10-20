# #5 Compute Credits: NVIDIA / AWS / Microsoft (+ Google Cloud) – Application Template

**Why it fits:** these programmes give **GPU time or cloud credits** instead of cash. They are easier to win than research grants and directly lower the cost of training your model. Apply in parallel with everything else.

| Programme | Status (Oct 2026) | What you get | Where |
|---|---|---|---|
| **NVIDIA Academic Grant Program** | ⚠️ **Not accepting applications right now.** Watch the portal for the next call (CFP) | GPU-hours (e.g. up to ~30,000 H100 hours in recent calls) or hardware | academicgrants.nvidia.com |
| **AWS Cloud Credit for Research** | Rolling **[CONFIRM]** | AWS promotional credits | aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/ |
| **Microsoft Research academic programs / AI for Good** | Call-based **[CONFIRM current calls]** | Azure credits, sometimes cash | microsoft.com/en-us/research/academic-program/ |
| **Google Cloud research credits** (extra option) | Rolling **[CONFIRM]** | GCP credits | cloud.google.com/edu/researchers |

---

## A. Eligibility check (shared)
- ☐ Applicant is **faculty or a researcher at an accredited research or degree-granting institution**. NVIDIA requires a **full-time faculty appointment at a PhD-granting institution**; students apply through a faculty sponsor. If the hospital is not a university, apply through an affiliated university/medical school faculty member.
- ☐ Cloud data location: **patient images must be de-identified** and storage must comply with Thai PDPA and your ethics approval (CP §10). Check whether a Singapore or other ASEAN region is acceptable to your ethics committee.

## B. Document checklist
| Item | NVIDIA | AWS | Microsoft | Google |
|---|---|---|---|---|
| Short proposal (NVIDIA: **≤ 4 pages on the official template**; non-compliant proposals are not reviewed) | ☐ | ☐ (online form) | ☐ | ☐ (online form) |
| PI CV / profile | ☐ | ☐ | ☐ | ☐ |
| Compute estimate (GPU-hours, storage TB, services) | ☐ | ☐ (AWS Pricing Calculator) | ☐ | ☐ |
| Which vendor tools you will use (NVIDIA: must use NVIDIA pretrained models / software, e.g. MONAI, NeMo, TAO) | ☐ | ☐ | ☐ | ☐ |
| Timeline matching the credit expiry (NVIDIA GPU-hours expired ~6 months after award in recent calls) | ☐ | ☐ | ☐ | ☐ |
| Plan to share results (papers, code, models) | ☐ | ☐ | ☐ | ☐ |

## C. Fill-in template (≈ 2–4 pages)

**1. Project title & PI:** CP §1, §3

**2. Research goal (½ page):** early oral cancer detection from smartphone/intraoral photos for Thailand; the burden in one paragraph (CP §4)

**3. Technical approach (1 page)**
- Dataset: ____ images, ____ classes, resolution ____, size ____ GB/TB
- Models: e.g. CNN / vision transformer / foundation-model fine-tuning; segmentation + classification
- Training plan: ____ experiments × ____ GPU-hours each; hyper-parameter search; external validation per hospital
- Vendor tools used: NVIDIA → MONAI / Clara / TAO; AWS → SageMaker, S3; Azure → Azure ML; GCP → Vertex AI

**4. Compute request (table)**
| Resource | Amount | Justification |
|---|---|---|
| GPU-hours (type) | ____ | ____ experiments × ____ hrs |
| Storage | ____ TB | images + backups |
| Data transfer / other | ____ | |
| **Estimated value (USD)** | ____ | |

**5. Timeline:** months 1–6 aligned with credit validity

**6. Expected outcomes:** model performance targets, publications, open-source code or model release (state what you can share under your ethics and PDPA rules)

**7. Broader impact:** LMIC health equity, number of people potentially screened

## D. Tips
- Request a **realistic, itemised** amount. Reviewers trust detailed estimates.
- Mention the **funded or pending grants** the credits complement (NRCT, HSRI, NIH).
- NVIDIA: name the specific NVIDIA software you will use. It is a scoring requirement.
- Promise acknowledgement and reporting. Missed reporting hurts future applications.

## E. Verify [CONFIRM]
- ☐ NVIDIA: next CFP date and track (e.g. "AI Training & Model Development")
- ☐ AWS / Microsoft / Google: current programme names, credit limits, data-region rules
