"""
Build the Kon Pop Grant Desk (an interactive fill-in page) from the Markdown
drafts in ./applications.

Every question in a draft becomes an editable field; every [FILL ...] placeholder
becomes its own input box. Re-run after editing any draft:

    python build_workbench.py
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
APPS = HERE / "applications"
TEMPLATE = HERE / "workbench_template.html"
OUT = HERE / "grant-desk.html"

LIMIT = re.compile(r"\{limit:\s*(\d+)\s*(words|chars)\}", re.I)

# Deadlines and details per draft file (prefix = file number). Dates marked
# estimated are inferred from past cycles; the page says so.
META = {
    "01": dict(id="solve", short="MIT Solve 2027", deadline="2026-11-02T12:00:00-05:00", estimated=False,
               applicant="Kon Pop Detection", amount="$10k + prizes up to $150k", portal="solve.mit.edu/challenges/2027-global-health-challenge"),
    "02": dict(id="pandemic", short="Pandemic-preparedness call", deadline=None, window="Which call is this for? Confirm the deadline",
               applicant="Mahidol University (PI from the region)", amount="AI4PEP's last call: up to CAD 362,500", portal="ai4pep.org/funding"),
    "03": dict(id="pic", short="Harvard PIC", deadline="2026-12-07T23:59:00-05:00", estimated=True,
               applicant="Kon Pop Detection (Harvard student on team)", amount="Share of ~$500k prize pool", portal="innovationlabs.harvard.edu/presidents-innovation-challenge"),
    "04": dict(id="nih", short="NIH STTR / SBIR", deadline="2027-01-05T17:00:00-05:00", estimated=True,
               applicant="Kon Pop Detection + US university", amount="Phase I ~$300k", portal="seed.nih.gov · grants.nih.gov (PA-27-102 / PA-27-100)"),
    "05": dict(id="nsf", short="NSF SBIR pitch", deadline="2026-11-04T17:00:00-05:00", estimated=True,
               applicant="Kon Pop Detection", amount="Phase I ~$305k", portal="seedfund.nsf.gov"),
    "06": dict(id="hsri", short="HSRI (สวรส.)", deadline=None, window="Expected Feb–Apr 2027",
               applicant="Mahidol University (Dr. Wareekul)", amount="Varies", portal="hsri.or.th · NRIIS"),
    "07": dict(id="nrct", short="NRCT (วช.)", deadline=None, window="Expected Nov 2026 – Apr 2027",
               applicant="Mahidol University (Dr. Wareekul)", amount="Varies", portal="nrct.go.th · NRIIS"),
    "08": dict(id="pmuc", short="PMU-C (บพข.)", deadline=None, window="Annual call: confirm dates",
               applicant="Mahidol + KPD as co-funding partner", amount="Varies", portal="pmuc.or.th · NRIIS"),
    "09": dict(id="thaihealth", short="ThaiHealth (สสส.)", deadline=None, window="Open grant: confirm",
               applicant="Thai hospital, Mahidol or community organisation", amount="Varies", portal="thaihealth.or.th"),
    "10": dict(id="credits", short="Cloud credits", deadline=None, window="Rolling: apply now",
               applicant="Kon Pop Detection", amount="Cloud and GPU credits", portal="cloud.google.com/startup · aws.amazon.com/activate"),
    "11": dict(id="r21", short="NIH R21 (academic)", deadline="2027-02-16T17:00:00-05:00", estimated=True,
               applicant="A university (UMich / Harvard / MIT / Mahidol)", amount="Up to $275k direct over 2 years", portal="grants.nih.gov · PA-25-253"),
    "12": dict(id="concept", short="Concept note", deadline=None, window="Use for first contact with any funder",
               applicant="Kon Pop Detection", amount="—", portal="—"),
}
ORDER = ["credits", "solve", "nsf", "pic", "nih", "nrct", "r21", "hsri", "pmuc", "thaihealth", "pandemic", "concept"]

FACTS = [
    ("legalName", "Legal company name", "e.g. Kon Pop Detection, Inc."),
    ("incorporation", "Where and when KPD is incorporated", "Country/state and date"),
    ("ownership", "Ownership", "% owned by US citizens / permanent residents (matters for SBIR)"),
    ("hq", "Headquarters city", "Where the senior team works"),
    ("website", "Website / app / social links", ""),
    ("contacts", "Team lead email and phone", "Plus a backup contact"),
    ("hospitals", "Partner hospital names", "e.g. Hua Taphan Hospital (Amnat Charoen), …"),
    ("ethics", "Ethics approval", "Committee name, approval number, date"),
    ("datasetSize", "Dataset size", "Number of images, sources"),
    ("labels", "How images are labelled", "Dentists? Biopsy-confirmed? How many high-risk / cancer cases?"),
    ("metrics", "Model results", "Sensitivity, specificity, AUC, test-set size, compared against what"),
    ("pilot", "Pilot status", "Start date, volunteers trained, people screened, referrals"),
    ("story", "The early-detection case", "Short, factual, no identifying details"),
    ("stage", "Stage of development", "Prototype or Pilot, and why"),
    ("award", "Google award at MIT Grand Hack", "Exact name and amount"),
    ("funding", "Funding received / raised", "Grants, awards, investment, in-kind"),
    ("teamSize", "Team size", "Full-time, part-time, contractors"),
    ("wareekul", "Dr. Wareekul's title and experience", "Faculty, role, screening experience, publications"),
    ("ernest", "Ernest's Harvard programme", "School and programme; previous companies"),
    ("amir", "Amir's AI / health software experience", ""),
    ("stack", "Tech stack", "App framework, backend, cloud provider and region, YOLO version"),
    ("offline", "How it works with poor internet", "e.g. photos queue on the phone and upload later"),
    ("pricing", "Pricing idea", "e.g. per screen / per facility per year"),
    ("thaiStats", "Thailand / Region 10 statistics", "Incidence, mortality, % late-stage, with sources"),
    ("dentists", "Dentists per population in Region 10", "With source"),
]


def table_line(s):
    t = s.strip()
    if not t.startswith("|"):
        return s
    if re.fullmatch(r"[\s|:\-]+", t):
        return None
    return " | ".join(c.strip() for c in t.strip("|").split("|"))


def clean(s):
    s = s.replace("**", "")
    return re.sub(r"`([^`]*)`", r"\1", s)


def tidy(lines):
    out, blank = [], 0
    for l in lines:
        if l.strip():
            out.append(l.rstrip()); blank = 0
        else:
            blank += 1
            if blank == 1 and out:
                out.append("")
    while out and not out[-1].strip():
        out.pop()
    return out


def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("# ")), path.stem)
    heads = [(len(l) - len(l.lstrip("#")), l) for l in lines if re.match(r"^#{2,4} ", l)]
    limited = [lvl for lvl, l in heads if LIMIT.search(l)]
    level = min(limited) if limited else (3 if sum(1 for lvl, _ in heads if lvl == 3) >= 4 else 2)

    intro, groups = [], [{"title": "", "note": [], "fields": []}]
    group, field = groups[0], None

    def sink():
        if field is not None:
            return field["body"]
        return group["note"] if group["title"] else intro

    for raw in lines:
        if raw.startswith("# "):
            continue
        m = re.match(r"^(#{2,4}) (.*)$", raw)
        if m:
            lvl, text = len(m.group(1)), m.group(2)
            if lvl == level:
                lm = LIMIT.search(text)
                field = {"title": clean(LIMIT.sub("", text)).strip(), "limit": int(lm.group(1)) if lm else None,
                         "unit": lm.group(2).lower() if lm else None, "guide": [], "body": []}
                group["fields"].append(field)
            elif lvl < level:
                group = {"title": clean(text).strip(), "note": [], "fields": []}
                groups.append(group)
                field = None
            else:
                sink().append(clean(text).strip())
            continue
        if raw.strip() == "---":
            continue
        if raw.lstrip().startswith(">"):
            txt = clean(raw.lstrip()[1:].strip())
            (field["guide"] if field is not None else sink()).append(txt)
            continue
        t = table_line(raw)
        if t is not None:
            sink().append(clean(t))

    for g in groups:
        g["note"] = tidy(g["note"])
        for f in g["fields"]:
            f["guide"] = [x for x in f["guide"] if x.strip()]
            f["body"] = "\n".join(tidy(f["body"]))
    groups = [g for g in groups if g["fields"] or g["note"]]
    return title, tidy(intro), groups


def main():
    grants = []
    for path in sorted(APPS.glob("*.md")):
        prefix = path.name[:2]
        if prefix not in META:
            continue
        title, intro, groups = parse(path)
        g = dict(META[prefix])
        g.update(title=title, file=path.name, intro=intro, groups=groups)
        grants.append(g)
    grants.sort(key=lambda g: ORDER.index(g["id"]))
    data = {"grants": grants, "facts": [dict(key=k, label=l, hint=h) for k, l, h in FACTS]}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", payload)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    # Standalone copy for GitHub Pages (a full HTML document so Thai text renders correctly)
    site = HERE / "docs" / "index.html"
    site.parent.mkdir(exist_ok=True)
    site.write_text('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
                    '</head>\n<body>\n' + html + '\n</body>\n</html>\n', encoding="utf-8", newline="\n")
    nfields = sum(len(gr["fields"]) for g in grants for gr in g["groups"])
    nblanks = sum(len(re.findall(r"\[FILL[^\]]*\]", f["body"])) for g in grants for gr in g["groups"] for f in gr["fields"])
    print(f"Written {OUT.name}: {len(grants)} grants, {nfields} fields, {nblanks} blanks to fill")


if __name__ == "__main__":
    main()
