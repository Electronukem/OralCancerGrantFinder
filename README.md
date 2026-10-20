# Kon Pop Detection – Grant Toolkit

Tools and drafts for funding Kon Pop Detection (KPD), an AI-assisted oral cancer screening tool used by village health volunteers in Health Region 10, Thailand.

## What's here

| Path | What it is |
|---|---|
| `KPD_Funding_Playbook_and_Master_Proposal.md` / `.docx` / `.pdf` | The full funding guide: strategy, calendar, funder directory, master proposal, budget guide, compliance, glossary |
| `applications/` | Draft applications for 12 funders (MIT Solve, Harvard PIC, NIH STTR/SBIR, NSF, HSRI, NRCT, PMU-C, ThaiHealth, cloud credits, NIH R21, concept note, pandemic-preparedness call). `[FILL]` = fact the team must supply; `[CONFIRM]` = check in the official call |
| `templates/` | Generic fill-in templates for 21 funders + a Common Information Pack |
| `grant-desk.html` | Kon Pop Grant Desk: interactive page for filling in every application blank by blank |
| `find_grants.py` | Searches Grants.gov and NIH RePORTER and writes an HTML report + CSVs to `results/` |
| `check_limits.py` | Checks draft answers against word/character limits |
| `build_workbench.py` + `workbench_template.html` | Rebuilds `grant-desk.html` from the drafts |
| `build_master_document.py`, `make_word_templates.py` | Rebuild the Word versions |

## Setup

Requires Python 3.10+.

```
pip install -r requirements.txt
python find_grants.py          # live grant search → results/
python check_limits.py applications/01_MIT_Solve_2027_Global_Health.md
python build_workbench.py      # after editing any draft
```

Drafts are starting points to be rewritten in the team's own words. Several funders (MIT Solve, NIH) restrict applications written with generative AI.
