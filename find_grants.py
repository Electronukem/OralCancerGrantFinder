"""
Grant finder for an AI-based early oral cancer detection project in Thailand.

1. Searches Grants.gov (live, posted/forecasted US federal opportunities) with many
   project-related keywords, scores each for relevance, and checks whether foreign
   (non-US) organizations are eligible.
2. Searches NIH RePORTER for already-funded similar projects, to show which funding
   announcements/mechanisms pay for this kind of work (and potential collaborators).
3. Includes a curated list of Thai and international funders (not machine-searchable;
   verify current calls on their websites).

Outputs an HTML report (opened automatically) and CSV files.

Usage:
    python find_grants.py
    python find_grants.py --max-details 60 --no-open
"""

import argparse
import csv
import html
import re
import time
import webbrowser
from datetime import datetime
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# PROJECT PROFILE - edit this section to match your project
# ---------------------------------------------------------------------------
PROJECT = {
    "title": "Kon Pop Detection: AI-assisted early oral cancer screening in Thailand",
    "country": "Thailand",
    "organization": "Kon Pop Detection (startup; Harvard GAMI incubator; MIT Grand Hack 2025)",
    "team": "Ernest Choi (CEO), Dr. Narawitchz Wareekul (CMO, Mahidol University), Amir Fleurizard (CTO)",
    "pilot": "Health Region 10 (Ubon Ratchathani, Sisaket, Yasothon, Amnat Charoen, Mukdahan); then Regions 7 and 9",
    "hospitals": [
        "Hua Taphan Hospital, Amnat Charoen (confirm: 'Huathahan')",
        "Partner hospital 2 (edit me)",
        "Partner hospital 3 (edit me)",
        "Partner hospital 4 (edit me)",
    ],
}

# Keyword queries sent to Grants.gov
SEARCH_QUERIES = [
    "oral cancer",
    "oral cavity cancer",
    "head and neck cancer",
    "oral potentially malignant disorders",
    "cancer early detection",
    "cancer screening low- and middle-income countries",
    "global cancer research",
    "global health artificial intelligence",
    "artificial intelligence cancer",
    "machine learning medical imaging",
    "digital health low-resource settings",
    "point-of-care cancer detection",
    "Fogarty international",
    "oral health",
    "Southeast Asia health research",
    # Small-business (startup) programmes
    "small business innovation research cancer",
    "SBIR artificial intelligence",
    "STTR cancer",
    "small business digital health",
    "small business imaging technology cancer",
]

# Relevance scoring: regex -> points. Applied to title (+ description when fetched).
SCORE_TERMS = {
    r"oral cancer|oral cavity|mouth cancer|oral squamous|OSCC": 10,
    r"head and neck": 7,
    r"potentially malignant|premalignant|leukoplakia": 7,
    r"oral health|dental|craniofacial": 4,
    r"cancer|oncolog|tumou?r|carcinoma": 4,
    r"early detection|screening|diagnos": 4,
    r"artificial intelligence|\bAI\b|machine learning|deep learning|computer vision": 6,
    r"imaging|image|photograph|smartphone|mobile|point[- ]of[- ]care": 3,
    r"digital health|mHealth|telehealth|telemedicine": 3,
    r"global health|international|low- and middle-income|LMIC|low-resource|resource-limited": 5,
    r"Fogarty|Asia|Thailand|ASEAN": 5,
    r"implementation|health equity|disparit": 2,
    r"small business|SBIR|STTR": 4,
}
# Penalise clearly irrelevant hits
NEGATIVE_TERMS = r"drug product|veterinar|agricultur|tobacco retail|dose dumping|fisher"
# Grants focused on a different cancer site are less useful
OTHER_CANCER_TERMS = r"pancrea|breast cancer|prostate|colorectal|lung cancer|ovarian|leukemia|PLCO|pediatric cancer"

NIH_QUERIES = [
    "oral cancer artificial intelligence",
    "oral cancer screening low-resource",
    "oral cancer deep learning detection",
    "oral potentially malignant",
    "head and neck cancer global health",
]

# ---------------------------------------------------------------------------
# CURATED NON-US / THAI FUNDERS (check websites for open calls)
# ---------------------------------------------------------------------------
CURATED_FUNDERS = [
    # --- Thailand ---
    ("Thailand", "National Research Council of Thailand (NRCT)", "Annual research grants; medical & public-health research; international co-funding calls", "High", "https://www.nrct.go.th", "Primary Thai research funder; Thai PI at a partner hospital should lead."),
    ("Thailand", "Thailand Science Research and Innovation (TSRI)", "Fundamental Fund / strategic research via the national STI fund", "High", "https://www.tsri.or.th", "Allocates national research budget; hospitals/universities apply via institutional channels."),
    ("Thailand", "Program Management Units PMU-C (competitiveness) and PMU-B (human resources & institutional development)", "Medical innovation, AI & digital health, research workforce", "High", "https://www.pmuc.or.th", "Good for AI/medical device development and commercialisation. PMU-B: https://www.pmub.or.th"),
    ("Thailand", "Health Systems Research Institute (HSRI)", "Health-system and health-technology research", "High", "https://www.hsri.or.th", "Strong fit for screening programmes, cost-effectiveness, and scale-up in the Thai health system."),
    ("Thailand", "National Innovation Agency (NIA)", "Innovation grants for health-tech / startups", "Medium", "https://www.nia.or.th", "Useful if the AI tool is spun into a product or startup."),
    ("Thailand", "Thai Health Promotion Foundation (ThaiHealth)", "Health promotion, NCD and risk-factor projects (tobacco, alcohol, betel)", "Medium", "https://www.thaihealth.or.th", "Fits community screening and risk-factor outreach components."),
    ("Thailand", "National Cancer Institute of Thailand / Department of Medical Services", "Cancer control research and collaboration", "Medium", "https://www.nci.go.th", "Potential partner and data source (cancer registry) in addition to funding."),
    ("Thailand", "NSTDA / NECTEC", "AI and digital technology research collaboration", "Medium", "https://www.nstda.or.th", "Technical AI partner; joint projects and compute resources."),
    # --- Regional / bilateral ---
    ("Asia", "e-ASIA Joint Research Program (e-ASIA JRP)", "Multilateral calls incl. health research; Thailand is a member", "High", "https://www.the-easia.org/jrp/", "Requires partners from 3+ member countries; Thai side funded via NRCT/TSRI."),
    ("Japan", "AMED (Japan Agency for Medical Research and Development)", "SATREPS, Asia-focused medical research programmes", "Medium", "https://www.amed.go.jp/en/", "Needs a Japanese lead institution."),
    ("Korea", "KHIDI (Korea Health Industry Development Institute)", "International joint R&D in health technology", "Low-Medium", "https://www.khidi.or.kr/eps", "Needs a Korean partner."),
    # --- International / philanthropic ---
    ("International", "UICC (Union for International Cancer Control)", "Technical fellowships, grants & cancer-control capacity building", "High", "https://www.uicc.org/what-we-do/capacity-building/grants", "Open to LMIC cancer professionals; good for training/travel components."),
    ("International", "IARC (International Agency for Research on Cancer, WHO)", "Collaborative research, oral cancer screening work in Asia, fellowships", "High", "https://www.iarc.who.int", "IARC has led oral cancer screening research in South/Southeast Asia; collaboration can unlock funding."),
    ("International", "Wellcome Trust", "Discovery Research; data science / digital health funding", "Medium", "https://wellcome.org/grant-funding", "Many schemes open to LMIC institutions; check eligibility for Thai lead applicants."),
    ("International", "Gates Foundation - Grand Challenges", "Grand Challenges calls (AI for global health, etc.)", "Medium", "https://gcgh.grandchallenges.org", "Calls are topic-specific; watch for AI / LMIC health calls."),
    ("International", "Google.org", "AI for health / AI for social good funding & accelerators", "Medium", "https://www.google.org", "Periodic open calls; often partner-nominated."),
    ("International", "Microsoft Research academic programs / Azure credits", "AI for Health grants and cloud compute", "Medium", "https://www.microsoft.com/en-us/research/academic-program/", "Useful for compute/credits to train detection models."),
    ("International", "NVIDIA Academic Grant Program", "GPU hardware / compute for AI research", "Medium", "https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/", "In-kind GPU support for model development."),
    ("International", "AWS Cloud Credit for Research / Health Equity Initiative", "Cloud credits for health-equity and research projects", "Medium", "https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/", "In-kind compute."),
    ("International", "Pfizer Global Medical Grants / industry oncology grants", "Independent research & quality-improvement grants (oncology)", "Low-Medium", "https://www.pfizer.com/about/programs-policies/grants", "Competitive calls on specific oncology topics."),
    # --- US agencies (also searched live via Grants.gov) ---
    ("USA", "NIH Fogarty International Center", "Global health research & training (NCDs, mHealth, D43/R21 mechanisms)", "High", "https://www.fic.nih.gov/Funding", "Many FOAs allow foreign institutions; often need US partner."),
    ("USA", "NCI Center for Global Health", "Global cancer research, technologies for low-resource settings", "High", "https://www.cancer.gov/about-nci/organization/cgh", "Funds low-cost cancer detection technologies for LMICs."),
    ("USA", "NIDCR (National Institute of Dental and Craniofacial Research)", "Oral cancer and oral health research", "High", "https://www.nidcr.nih.gov/grants-funding", "Directly relevant to oral cancer detection."),
    # --- Startup / small-business programmes (added after reviewing the KPD pitch deck) ---
    ("Startup", "MIT Solve - 2027 Global Health Challenge", "$10k Solver grant + sponsor prizes (AI for Humanity up to $150k); 9-month support", "High", "https://solve.mit.edu/challenges/2027-global-health-challenge", "DEADLINE 2 Nov 2026, 12:00 noon ET. Prototype/Pilot stage or later. Draft: applications/01."),
    ("Startup", "Harvard President's Innovation Challenge (Harvard i-lab)", "Non-dilutive prizes (~$500k pool), Health Care + Life Sciences track", "High", "https://innovationlabs.harvard.edu/presidents-innovation-challenge", "Team needs a current Harvard student. 2026 deadline was 8 Dec 2025; expect ~Dec 2026. Draft: applications/03."),
    ("USA", "NIH/NCI SBIR & STTR (R43/R41)", "Phase I ~$300k; reauthorised Apr 2026 through 2031", "High", "https://seed.nih.gov", "US small business, >50% US-owned; R&D in US. STTR with Harvard/MIT/UMich recommended. Next date ~5 Jan 2027. Draft: applications/04."),
    ("USA", "NSF SBIR/STTR (America's Seed Fund)", "Project Pitch -> Phase I", "Medium", "https://seedfund.nsf.gov", "Technical-risk R&D only; US small business. Draft: applications/05."),
    ("Startup", "Google for Startups Cloud Program / Accelerator", "Cloud credits (higher AI tier), mentoring", "High", "https://cloud.google.com/startup", "KPD builds on Google MedGemma. Draft: applications/10."),
    ("Startup", "AWS Activate / Microsoft for Startups / NVIDIA Inception", "Credits and technical support", "Medium", "https://aws.amazon.com/activate/", "Rolling. Draft: applications/10."),
    # --- Additional Thai funders ---
    ("Thailand", "TCELS (Thailand Center of Excellence for Life Sciences)", "Medical devices at TRL 5-9, toward market", "Medium", "https://www.tcels.or.th", "Later stage, after validation; likely needs a Thai entity."),
    ("Thailand", "depa (Digital Economy Promotion Agency)", "Digital startup funds and pilots", "Medium", "https://www.depa.or.th", "Likely needs a Thai-registered company [confirm]."),
    ("Thailand", "NHSO (สปสช.)", "Financing / adoption of screening in UC benefits", "Medium", "https://www.nhso.go.th", "A buyer and policy partner rather than a grant; target with HSRI cost-effectiveness results."),
    # --- Bilateral / international ---
    ("UK-Thailand", "International Science Partnerships Fund (British Council + NRCT)", "Research collaboration grants (Thai partners up to ~GBP 100k in past rounds)", "Medium", "https://opportunities-insight.britishcouncil.org", "No confirmed 2026 Thailand round; watch the British Council and NRCT."),
    ("Japan-Thailand", "JST ASPIRE / NEXUS (Thailand)", "Japan-Thailand joint research; 2026 Thailand guideline published", "Medium", "https://www.jst.go.jp/aspire/", "Needs a Japanese partner; check whether health/AI topics qualify."),
    ("China-Thailand", "NRCT-NSFC joint call", "Thailand-China joint research", "Low-Medium", "https://en.nrct.go.th", "Needs a Chinese partner."),
    ("Canada", "IDRC / AI4PEP network", "AI for pandemic & epidemic preparedness (Global South)", "Low-Medium", "https://ai4pep.org/funding/", "Last open call 2023; infectious-disease focus; PI must be from the region. Your draft form matches this format (applications/02)."),
    ("International", "ASCO / Conquer Cancer IDEA award", "Travel + mentorship for early-career oncologists in LMICs", "Low", "https://www.conquer.org/idea", "For oncologists within 10 years of training; probably not for dentists [confirm]."),
    ("International", "Cancer Grand Challenges (CRUK + NCI)", "Large team awards on set challenges", "Low", "https://cancergrandchallenges.org", "Only if a challenge matches early detection / LMIC screening."),
    ("International", "Rotary Foundation Global Grants", "Disease prevention & treatment projects via Rotary clubs", "Medium", "https://www.rotary.org/en/our-programs/grants", "Needs a Thai club + an international club as sponsors."),
    ("Asia", "Temasek Foundation", "Regional healthcare capacity building", "Low-Medium", "https://www.temasekfoundation.org.sg", "Usually partner-led; approach via network."),
]
CURATED_FIELDS = ["Region", "Funder", "Programme", "Fit", "Url", "Notes"]

GRANTS_SEARCH_URL = "https://api.grants.gov/v1/api/search2"
GRANTS_FETCH_URL = "https://api.grants.gov/v1/api/fetchOpportunity"
NIH_URL = "https://api.reporter.nih.gov/v2/projects/search"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
session = requests.Session()


def post_json(url, body, retries=3):
    for attempt in range(1, retries + 1):
        try:
            r = session.post(url, json=body, timeout=60)
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            if attempt == retries:
                print(f"  WARNING: request failed ({url}): {e}")
                return None
            time.sleep(2 * attempt)


def get_score(text):
    score, hits = 0, []
    for pattern, points in SCORE_TERMS.items():
        if re.search(pattern, text, re.I):
            score += points
            hits.append(pattern.split("|")[0].replace("\\b", ""))
    if re.search(NEGATIVE_TERMS, text, re.I):
        score -= 15
    if re.search(OTHER_CANCER_TERMS, text, re.I) and not re.search(r"oral|head and neck", text, re.I):
        score -= 8
    return score, ", ".join(hits)


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    for fmt in ("%m/%d/%Y", "%b %d, %Y %I:%M:%S %p EDT", "%b %d, %Y %I:%M:%S %p EST", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def classify_foreign(elig):
    if re.search(r"non-domestic|foreign (institutions|organizations|components)|non-U\.?S\.? (entities|institutions|organizations)", elig, re.I):
        if re.search(r"(non-domestic|foreign)[^.]{0,60}(are not|not eligible|ineligible)", elig, re.I):
            return "No"
        return "Yes"
    if re.search(r"unrestricted|Others \(see text", elig, re.I):
        return "Possibly - read text"
    return "Likely no"


def to_money(v):
    try:
        n = float(str(v).replace(",", ""))
        return f"${n:,.0f}" if n > 0 else ""
    except ValueError:
        return ""


# ---------------------------------------------------------------------------
# 1. Grants.gov
# ---------------------------------------------------------------------------
def search_grants_gov(rows_per_query, max_details, today):
    print(f"\n[1/3] Searching Grants.gov ({len(SEARCH_QUERIES)} queries)...")
    opps = {}
    for q in SEARCH_QUERIES:
        r = post_json(GRANTS_SEARCH_URL, {"keyword": q, "oppStatuses": "forecasted|posted", "rows": rows_per_query})
        if not r:
            continue
        hits = r.get("data", {}).get("oppHits", []) or []
        print(f"  {q:<50} {len(hits):>4} hits")
        for h in hits:
            o = opps.setdefault(h["id"], {
                "Id": h["id"], "Number": h.get("number", ""), "Title": h.get("title", ""),
                "Agency": h.get("agency", ""), "Status": h.get("oppStatus", ""),
                "OpenDate": h.get("openDate", ""), "CloseDate": h.get("closeDate", ""),
                "Queries": [], "Score": 0, "Matched": "", "ForeignEligible": "Unknown",
                "Eligibility": "", "AwardCeiling": "", "Description": "",
                "Url": f"https://www.grants.gov/search-results-detail/{h['id']}",
            })
            o["Queries"].append(q)

    results = []
    for o in opps.values():
        cd = parse_date(o["CloseDate"])
        if cd and cd < today:
            continue
        s, hits = get_score(o["Title"])
        o["Score"] = s + min(len(o["Queries"]), 5)  # bonus for matching several queries
        o["Matched"] = hits
        results.append(o)
    results.sort(key=lambda o: o["Score"], reverse=True)
    print(f"  {len(opps)} unique opportunities, {len(results)} still open/forecasted.")

    top_n = results[:max_details]
    print(f"\n[2/3] Fetching details + foreign-eligibility for top {len(top_n)}...")
    for i, o in enumerate(top_n, 1):
        print(f"\r  {i}/{len(top_n)} {o['Number']:<20}", end="", flush=True)
        d = post_json(GRANTS_FETCH_URL, {"opportunityId": int(o["Id"])})
        data = (d or {}).get("data", {}) or {}
        syn = data.get("synopsis") or data.get("forecast")
        if not syn:
            continue
        desc = strip_html((syn.get("synopsisDesc") or "") + " " + (syn.get("forecastDesc") or ""))
        types = "; ".join(t.get("description", "") for t in (syn.get("applicantTypes") or []))
        elig = strip_html(types + " " + (syn.get("applicantEligibilityDesc") or ""))
        o["Description"] = desc[:600] + ("..." if len(desc) > 600 else "")
        o["Eligibility"] = elig
        o["AwardCeiling"] = syn.get("awardCeiling", "")
        o["ForeignEligible"] = classify_foreign(elig)
        s, hits = get_score(o["Title"] + " " + desc)
        o["Score"] = s + min(len(o["Queries"]), 5) + (8 if o["ForeignEligible"] == "Yes" else 0)
        o["Matched"] = hits
    print()
    results.sort(key=lambda o: o["Score"], reverse=True)
    return results


# ---------------------------------------------------------------------------
# 2. NIH RePORTER
# ---------------------------------------------------------------------------
def search_nih(today):
    print("\n[3/3] Searching NIH RePORTER for similar funded projects...")
    years = list(range(today.year - 3, today.year + 1))
    similar = {}
    for t in NIH_QUERIES:
        r = post_json(NIH_URL, {
            "criteria": {
                "advanced_text_search": {"operator": "and", "search_field": "projecttitle,terms,abstracttext", "search_text": t},
                "fiscal_years": years,
            },
            "limit": 50,
            "include_fields": ["ProjectTitle", "OpportunityNumber", "Organization", "FiscalYear", "ProjectNum",
                               "ActivityCode", "AwardAmount", "AgencyIcAdmin", "ContactPiName", "ApplId"],
        })
        if not r:
            continue
        print(f"  {t:<50} {r.get('meta', {}).get('total', 0):>4} projects")
        for p in r.get("results", []):
            core = re.sub(r"-\d+.*$", "", re.sub(r"^\d", "", p.get("project_num") or ""))  # core project number
            if core in similar:
                continue
            org = p.get("organization") or {}
            similar[core] = {
                "Project": core, "Title": p.get("project_title", ""),
                "Organization": org.get("org_name", ""), "Country": org.get("org_country", ""),
                "PI": p.get("contact_pi_name", ""), "Mechanism": p.get("activity_code", ""),
                "Institute": (p.get("agency_ic_admin") or {}).get("abbreviation", ""),
                "Opportunity": p.get("opportunity_number", ""), "FiscalYear": p.get("fiscal_year", ""),
                "Award": p.get("award_amount", ""),
                "Url": f"https://reporter.nih.gov/project-details/{p.get('appl_id')}",
            }
    return sorted(similar.values(), key=lambda s: s["FiscalYear"] or 0, reverse=True)


def summarize_mechanisms(similar, top=15):
    groups = {}
    for s in similar:
        if s["Opportunity"]:
            g = groups.setdefault(s["Opportunity"], {"Opportunity": s["Opportunity"], "Count": 0, "Mechanisms": set()})
            g["Count"] += 1
            g["Mechanisms"].add(s["Mechanism"] or "")
    out = sorted(groups.values(), key=lambda g: g["Count"], reverse=True)[:top]
    for g in out:
        g["Mechanisms"] = "/".join(sorted(g["Mechanisms"]))
    return out


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def pill(cls, text):
    return f"<span class='pill {cls}'>{html.escape(str(text))}</span>"


def build_html(grants, all_open_count, similar, mechs, curated, now):
    e = html.escape
    today = now.date()

    grant_rows = []
    for o in grants:
        cd = parse_date(o["CloseDate"])
        due = f"{e(o['CloseDate'])}<br><small>{(cd - today).days} days left</small>" if cd else "Not set"
        fe = o["ForeignEligible"]
        cls = "yes" if fe == "Yes" else "no" if fe in ("No", "Likely no") else "maybe"
        grant_rows.append(
            f"<tr><td class='score'>{o['Score']}</td><td><a href='{e(o['Url'])}' target='_blank'>{e(o['Title'])}</a>"
            f"<div class='meta'>{e(o['Number'])} &middot; {e(o['Agency'])} &middot; {e(o['Status'])}</div>"
            f"<div class='desc'>{e(o['Description'])}</div><div class='meta'>Matched: {e(o['Matched'])}</div></td>"
            f"<td>{due}</td><td>{pill(cls, fe)}</td><td>{to_money(o['AwardCeiling'])}</td></tr>")

    cur_rows = []
    for c in curated:
        cls = "yes" if c["Fit"] == "High" else "no" if c["Fit"].startswith("Low") else "maybe"
        cur_rows.append(
            f"<tr><td>{e(c['Region'])}</td><td><a href='{e(c['Url'])}' target='_blank'>{e(c['Funder'])}</a>"
            f"<div class='meta'>{e(c['Programme'])}</div></td><td>{pill(cls, c['Fit'])}</td><td>{e(c['Notes'])}</td></tr>")

    sim_rows = [
        f"<tr><td><a href='{e(s['Url'])}' target='_blank'>{e(s['Title'])}</a>"
        f"<div class='meta'>{e(s['PI'] or '')} &middot; {e(s['Organization'] or '')}, {e(s['Country'] or '')}</div></td>"
        f"<td>{e(s['Mechanism'] or '')} / {e(s['Institute'] or '')}</td><td>{e(s['Opportunity'] or '')}</td><td>{s['FiscalYear']}</td></tr>"
        for s in similar[:60]]

    mech_rows = [
        f"<tr><td><a href='https://grants.nih.gov/grants/guide/search_results.htm?query={e(m['Opportunity'])}' target='_blank'>"
        f"{e(m['Opportunity'])}</a></td><td>{e(m['Mechanisms'])}</td><td>{m['Count']}</td></tr>"
        for m in mechs]

    hospitals = "".join(f"<li>{e(h)}</li>" for h in PROJECT["hospitals"])
    nl = "\n"
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Grant Finder - Oral Cancer AI Thailand</title>
<style>
body{{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f5f6f8;color:#1d2330}}
header{{background:#123c69;color:#fff;padding:24px 32px}}header h1{{margin:0 0 4px;font-size:24px}}
main{{padding:16px 32px 48px;max-width:1300px}}section{{background:#fff;border-radius:8px;padding:16px 20px;margin:18px 0;box-shadow:0 1px 3px #0001}}
h2{{margin-top:0;font-size:18px;color:#123c69}}table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{text-align:left;padding:8px;border-bottom:1px solid #e6e8ec;vertical-align:top}}th{{background:#f0f2f5;position:sticky;top:0}}
.meta{{color:#667;font-size:12px;margin-top:3px}}.desc{{font-size:12px;color:#333;margin-top:4px;max-width:750px}}
.score{{font-weight:700;font-size:16px;color:#123c69;text-align:center}}a{{color:#0b5cad;text-decoration:none;font-weight:600}}
.pill{{padding:2px 8px;border-radius:10px;font-size:12px;white-space:nowrap}}.yes{{background:#d9f2df;color:#17602a}}.no{{background:#f6dcdc;color:#8a1f1f}}.maybe{{background:#fff0c9;color:#7a5a00}}
.note{{background:#eef4fb;border-left:4px solid #123c69;padding:10px 14px;font-size:13px}}ul{{margin:4px 0}}
</style></head><body>
<header><h1>Grant Finder: {e(PROJECT['title'])}</h1><div>Generated {now:%d %b %Y %H:%M}</div></header>
<main>
<section><h2>Project profile</h2>
<p><b>Organization:</b> {e(PROJECT.get('organization', ''))}<br><b>Team:</b> {e(PROJECT.get('team', ''))}<br><b>Pilot:</b> {e(PROJECT.get('pilot', ''))}</p>
<b>Partner hospitals ({len(PROJECT['hospitals'])}):</b><ul>{hospitals}</ul>
<div class="note">Tips: Most US federal grants require a US-registered applicant, so look for {pill('yes', 'Yes')} foreign eligibility
or partner with a US university as the prime applicant. Thai partners will need SAM.gov/UEI registration for US awards.
Always confirm details in the official opportunity documents.</div></section>

<section><h2>1. Thai &amp; international funders (curated - check for open calls)</h2>
<table><tr><th>Region</th><th>Funder / programme</th><th>Fit</th><th>Notes</th></tr>{nl.join(cur_rows)}</table></section>

<section><h2>2. Open &amp; forecasted Grants.gov opportunities ({len(grants)} relevant of {all_open_count} open)</h2>
<table><tr><th>Score</th><th>Opportunity</th><th>Closes</th><th>Foreign eligible</th><th>Award ceiling</th></tr>{nl.join(grant_rows)}</table></section>

<section><h2>3. Funding announcements that have funded similar NIH projects</h2>
<p class="meta">These announcements/mechanisms have already funded oral cancer, AI, or global-health projects. Look for their reissued versions.</p>
<table><tr><th>Opportunity</th><th>Mechanism</th><th># similar projects</th></tr>{nl.join(mech_rows)}</table>
<h2 style="margin-top:20px">Similar funded projects ({len(similar)}) - potential collaborators</h2>
<table><tr><th>Project</th><th>Mechanism / IC</th><th>Opportunity</th><th>FY</th></tr>{nl.join(sim_rows)}</table></section>
</main></body></html>"""


def main():
    ap = argparse.ArgumentParser(description="Find grants for an AI oral cancer detection project in Thailand.")
    ap.add_argument("--rows-per-query", type=int, default=50, help="Grants.gov results per keyword (default 50)")
    ap.add_argument("--max-details", type=int, default=40, help="top-N opportunities to fetch eligibility details for (default 40)")
    ap.add_argument("--min-score", type=int, default=6, help="minimum relevance score to include in report (default 6)")
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "results"))
    ap.add_argument("--no-open", action="store_true", help="don't open the report in a browser")
    args = ap.parse_args()

    now = datetime.now()
    today = now.date()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    grants = search_grants_gov(args.rows_per_query, args.max_details, today)
    similar = search_nih(today)
    mechs = summarize_mechanisms(similar)
    curated = [dict(zip(CURATED_FIELDS, c)) for c in CURATED_FUNDERS]
    relevant = [g for g in grants if g["Score"] >= args.min_score]

    stamp = today.isoformat()
    write_csv(out / f"grants_gov_{stamp}.csv", relevant,
              ["Score", "Number", "Title", "Agency", "Status", "OpenDate", "CloseDate", "ForeignEligible",
               "AwardCeiling", "Matched", "Url", "Eligibility"])
    write_csv(out / f"nih_similar_projects_{stamp}.csv", similar,
              ["Project", "Title", "Organization", "Country", "PI", "Mechanism", "Institute", "Opportunity",
               "FiscalYear", "Award", "Url"])
    write_csv(out / "curated_funders.csv", curated, CURATED_FIELDS)

    report = out / f"grant_report_{stamp}.html"
    report.write_text(build_html(relevant, len(grants), similar, mechs, curated, now), encoding="utf-8")

    print("\nDone.")
    print(f"  Report : {report}")
    print(f"  CSVs   : {out}")
    print("\nTop 10 Grants.gov matches:")
    print(f"  {'Score':>5}  {'Number':<16} {'Foreign':<20} {'Closes':<11} Title")
    for g in relevant[:10]:
        print(f"  {g['Score']:>5}  {g['Number']:<16} {g['ForeignEligible']:<20} {g['CloseDate'] or '-':<11} {g['Title'][:70]}")

    if not args.no_open:
        webbrowser.open(report.resolve().as_uri())


if __name__ == "__main__":
    main()
