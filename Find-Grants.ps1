<#
.SYNOPSIS
  Grant finder for an AI-based early oral cancer detection project in Thailand.

.DESCRIPTION
  1. Searches Grants.gov (live, US federal opportunities that are posted/forecasted)
     with many project-related keywords, scores each opportunity for relevance,
     and checks whether foreign (non-US) organizations are eligible.
  2. Searches NIH RePORTER for already-funded projects similar to yours, to show
     which funding mechanisms / announcements pay for this kind of work.
  3. Includes a curated list of Thai and international funders that fit the project
     (these are not machine-searchable; verify current calls on their websites).
  Produces an HTML report (opens automatically) and CSV files.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\Find-Grants.ps1
  powershell -ExecutionPolicy Bypass -File .\Find-Grants.ps1 -MaxDetails 60 -NoOpen
#>
param(
    [int]$RowsPerQuery = 50,      # Grants.gov results per keyword
    [int]$MaxDetails   = 40,      # top-N opportunities to fetch full details for (eligibility check)
    [string]$OutDir    = (Join-Path $PSScriptRoot "results"),
    [switch]$NoOpen
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# ----------------------------------------------------------------------------
# PROJECT PROFILE - edit this section to match your project
# ----------------------------------------------------------------------------
$Project = @{
    Title     = "AI-assisted early detection of oral cancer in Thailand"
    Country   = "Thailand"
    Hospitals = @(
        "Huathahan Hospital",
        "Partner hospital 2 (edit me)",
        "Partner hospital 3 (edit me)",
        "Partner hospital 4 (edit me)"
    )
}

# Keyword queries sent to Grants.gov
$SearchQueries = @(
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
    "Southeast Asia health research"
)

# Relevance scoring: term (regex) -> points. Applied to title (+ description when fetched).
$ScoreTerms = [ordered]@{
    'oral cancer|oral cavity|mouth cancer|oral squamous|OSCC' = 10
    'head and neck'                                          = 7
    'potentially malignant|premalignant|leukoplakia'         = 7
    'oral health|dental|craniofacial'                        = 4
    'cancer|oncolog|tumou?r|carcinoma'                       = 4
    'early detection|screening|diagnos'                      = 4
    'artificial intelligence|\bAI\b|machine learning|deep learning|computer vision' = 6
    'imaging|image|photograph|smartphone|mobile|point[- ]of[- ]care' = 3
    'digital health|mHealth|telehealth|telemedicine'         = 3
    'global health|international|low- and middle-income|LMIC|low-resource|resource-limited' = 5
    'Fogarty|Asia|Thailand|ASEAN'                            = 5
    'implementation|health equity|disparit'                  = 2
}
# Penalise clearly irrelevant hits
$NegativeTerms = 'drug product|veterinar|agricultur|tobacco retail|dose dumping|fisher'
# Grants focused on a different cancer site are less useful
$OtherCancerTerms = 'pancrea|breast cancer|prostate|colorectal|lung cancer|ovarian|leukemia|PLCO|pediatric cancer'

# ----------------------------------------------------------------------------
# CURATED NON-US / THAI FUNDERS (not searchable by API - check websites for open calls)
# ----------------------------------------------------------------------------
$CuratedFunders = @(
    # --- Thailand ---
    [pscustomobject]@{ Region="Thailand"; Funder="National Research Council of Thailand (NRCT)"; Programme="Annual research grants; medical & public-health research; international co-funding calls"; Fit="High"; Url="https://www.nrct.go.th"; Notes="Primary Thai research funder; Thai PI at a partner hospital should lead." }
    [pscustomobject]@{ Region="Thailand"; Funder="Thailand Science Research and Innovation (TSRI)"; Programme="Fundamental Fund / strategic research via the national STI fund"; Fit="High"; Url="https://www.tsri.or.th"; Notes="Allocates national research budget; hospitals/universities apply via institutional channels." }
    [pscustomobject]@{ Region="Thailand"; Funder="Program Management Unit for Competitiveness (PMU-C) and Program Management Unit for Human Resources & Institutional Development (PMU-B)"; Programme="Medical innovation, AI & digital health, research workforce"; Fit="High"; Url="https://www.pmuc.or.th"; Notes="Good for AI/medical device development and commercialisation. PMU-B: https://www.pmub.or.th" }
    [pscustomobject]@{ Region="Thailand"; Funder="Health Systems Research Institute (HSRI)"; Programme="Health-system and health-technology research"; Fit="High"; Url="https://www.hsri.or.th"; Notes="Strong fit for screening programmes, cost-effectiveness, and scale-up in the Thai health system." }
    [pscustomobject]@{ Region="Thailand"; Funder="National Innovation Agency (NIA)"; Programme="Innovation grants for health-tech / startups"; Fit="Medium"; Url="https://www.nia.or.th"; Notes="Useful if the AI tool is spun into a product or startup." }
    [pscustomobject]@{ Region="Thailand"; Funder="Thai Health Promotion Foundation (ThaiHealth)"; Programme="Health promotion, NCD and risk-factor projects (tobacco, alcohol, betel)"; Fit="Medium"; Url="https://www.thaihealth.or.th"; Notes="Fits community screening and risk-factor outreach components." }
    [pscustomobject]@{ Region="Thailand"; Funder="National Cancer Institute of Thailand / Department of Medical Services"; Programme="Cancer control research and collaboration"; Fit="Medium"; Url="https://www.nci.go.th"; Notes="Potential partner and data source (cancer registry) in addition to funding." }
    [pscustomobject]@{ Region="Thailand"; Funder="NSTDA / NECTEC"; Programme="AI and digital technology research collaboration"; Fit="Medium"; Url="https://www.nstda.or.th"; Notes="Technical AI partner; joint projects and compute resources." }
    # --- Regional / bilateral ---
    [pscustomobject]@{ Region="Asia"; Funder="e-ASIA Joint Research Program (e-ASIA JRP)"; Programme="Multilateral calls incl. health research; Thailand is a member"; Fit="High"; Url="https://www.the-easia.org/jrp/"; Notes="Requires partners from 3+ member countries; Thai side funded via NRCT/TSRI." }
    [pscustomobject]@{ Region="Japan"; Funder="AMED (Japan Agency for Medical Research and Development)"; Programme="SATREPS, Asia-focused medical research programmes"; Fit="Medium"; Url="https://www.amed.go.jp/en/"; Notes="Needs a Japanese lead institution." }
    [pscustomobject]@{ Region="Korea"; Funder="KHIDI (Korea Health Industry Development Institute)"; Programme="International joint R&D in health technology"; Fit="Low-Medium"; Url="https://www.khidi.or.kr/eps"; Notes="Needs a Korean partner." }
    # --- International / philanthropic ---
    [pscustomobject]@{ Region="International"; Funder="UICC (Union for International Cancer Control)"; Programme="Technical fellowships, grants & cancer-control capacity building"; Fit="High"; Url="https://www.uicc.org/what-we-do/capacity-building/grants"; Notes="Open to LMIC cancer professionals; good for training/travel components." }
    [pscustomobject]@{ Region="International"; Funder="IARC (International Agency for Research on Cancer, WHO)"; Programme="Collaborative research, oral cancer screening work in Asia, fellowships"; Fit="High"; Url="https://www.iarc.who.int"; Notes="IARC has led oral cancer screening research in South/Southeast Asia; collaboration can unlock funding." }
    [pscustomobject]@{ Region="International"; Funder="Wellcome Trust"; Programme="Discovery Research; Climate & Health; Data Science / digital health funding"; Fit="Medium"; Url="https://wellcome.org/grant-funding"; Notes="Many schemes open to LMIC institutions; check eligibility for Thai lead applicants." }
    [pscustomobject]@{ Region="International"; Funder="Gates Foundation - Grand Challenges"; Programme="Grand Challenges calls (AI for global health, etc.)"; Fit="Medium"; Url="https://gcgh.grandchallenges.org"; Notes="Calls are topic-specific; watch for AI / LMIC health calls." }
    [pscustomobject]@{ Region="International"; Funder="Google.org"; Programme="AI for health / AI for social good funding & accelerators"; Fit="Medium"; Url="https://www.google.org"; Notes="Periodic open calls; often partner-nominated." }
    [pscustomobject]@{ Region="International"; Funder="Microsoft AI for Good Lab / Azure research credits"; Programme="AI for Health grants and cloud compute"; Fit="Medium"; Url="https://www.microsoft.com/en-us/research/academic-program/"; Notes="Useful for compute/credits to train detection models." }
    [pscustomobject]@{ Region="International"; Funder="NVIDIA Academic Grant Program"; Programme="GPU hardware / compute for AI research"; Fit="Medium"; Url="https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/"; Notes="In-kind GPU support for model development." }
    [pscustomobject]@{ Region="International"; Funder="AWS Health Equity Initiative / AWS Cloud Credit for Research"; Programme="Cloud credits for health-equity and research projects"; Fit="Medium"; Url="https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/"; Notes="In-kind compute." }
    [pscustomobject]@{ Region="International"; Funder="Pfizer Global Medical Grants / industry oncology grants"; Programme="Independent research & quality-improvement grants (oncology)"; Fit="Low-Medium"; Url="https://www.pfizer.com/about/programs-policies/grants"; Notes="Competitive calls on specific oncology topics." }
    # --- US agencies (also searched live via Grants.gov) ---
    [pscustomobject]@{ Region="USA"; Funder="NIH Fogarty International Center"; Programme="Global health research & training (incl. non-communicable disease, mHealth, D43/R21 mechanisms)"; Fit="High"; Url="https://www.fic.nih.gov/Funding"; Notes="Many FOAs allow foreign institutions; often need US partner." }
    [pscustomobject]@{ Region="USA"; Funder="NCI Center for Global Health"; Programme="Global cancer research, technologies for low-resource settings"; Fit="High"; Url="https://www.cancer.gov/about-nci/organization/cgh"; Notes="Funds low-cost cancer detection technologies for LMICs." }
    [pscustomobject]@{ Region="USA"; Funder="NIDCR (National Institute of Dental and Craniofacial Research)"; Programme="Oral cancer and oral health research"; Fit="High"; Url="https://www.nidcr.nih.gov/grants-funding"; Notes="Directly relevant to oral cancer detection." }
)

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
function Get-Score([string]$text) {
    $s = 0; $hits = @()
    foreach ($k in $ScoreTerms.Keys) {
        if ($text -match "(?i)$k") { $s += $ScoreTerms[$k]; $hits += ($k -split '\|')[0] }
    }
    if ($text -match "(?i)$NegativeTerms") { $s -= 15 }
    if ($text -match "(?i)$OtherCancerTerms" -and $text -notmatch "(?i)oral|head and neck") { $s -= 8 }
    return @{ Score = $s; Hits = ($hits -join ", ") }
}

function Invoke-Json($uri, $body) {
    $json = $body | ConvertTo-Json -Depth 10
    for ($i = 1; $i -le 3; $i++) {
        try { return Invoke-RestMethod -Uri $uri -Method Post -Body $json -ContentType "application/json" -TimeoutSec 60 }
        catch { if ($i -eq 3) { Write-Warning "Request failed ($uri): $($_.Exception.Message)"; return $null }; Start-Sleep -Seconds (2 * $i) }
    }
}

function Html([string]$s) { [System.Net.WebUtility]::HtmlEncode($s) }

function Parse-Date([string]$d) {
    if ([string]::IsNullOrWhiteSpace($d)) { return $null }
    $dt = [datetime]::MinValue
    foreach ($fmt in 'MM/dd/yyyy', 'MMM dd, yyyy hh:mm:ss tt EDT', 'MMM dd, yyyy hh:mm:ss tt EST', 'yyyy-MM-dd') {
        if ([datetime]::TryParseExact($d, $fmt, [Globalization.CultureInfo]::InvariantCulture, 'None', [ref]$dt)) { return $dt }
    }
    if ([datetime]::TryParse($d, [ref]$dt)) { return $dt }
    return $null
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$today = Get-Date

# ----------------------------------------------------------------------------
# 1. Grants.gov search
# ----------------------------------------------------------------------------
Write-Host "`n[1/3] Searching Grants.gov ($($SearchQueries.Count) queries)..." -ForegroundColor Cyan
$opps = @{}
foreach ($q in $SearchQueries) {
    $r = Invoke-Json "https://api.grants.gov/v1/api/search2" @{ keyword = $q; oppStatuses = "forecasted|posted"; rows = $RowsPerQuery }
    if (-not $r) { continue }
    $hits = @($r.data.oppHits)
    Write-Host ("  {0,-50} {1,4} hits" -f $q, $hits.Count)
    foreach ($h in $hits) {
        if (-not $opps.ContainsKey($h.id)) {
            $opps[$h.id] = [pscustomobject]@{
                Id = $h.id; Number = $h.number; Title = $h.title; Agency = $h.agency
                Status = $h.oppStatus; OpenDate = $h.openDate; CloseDate = $h.closeDate
                MatchedQueries = [System.Collections.Generic.List[string]]::new()
                Score = 0; Matched = ""; ForeignEligible = "Unknown"; Eligibility = ""
                AwardCeiling = ""; Description = ""
                Url = "https://www.grants.gov/search-results-detail/$($h.id)"
            }
        }
        $opps[$h.id].MatchedQueries.Add($q)
    }
}

# Initial scoring on title; drop expired
$list = foreach ($o in $opps.Values) {
    $cd = Parse-Date $o.CloseDate
    if ($cd -and $cd -lt $today.Date) { continue }
    $sc = Get-Score $o.Title
    $o.Score = $sc.Score + [Math]::Min($o.MatchedQueries.Count, 5)   # bonus for matching several queries
    $o.Matched = $sc.Hits
    $o
}
$list = @($list | Sort-Object Score -Descending)
Write-Host "  $($opps.Count) unique opportunities, $($list.Count) still open/forecasted."

# Fetch details for top results (description, eligibility, award size)
Write-Host "`n[2/3] Fetching details + foreign-eligibility for top $MaxDetails..." -ForegroundColor Cyan
$i = 0
foreach ($o in ($list | Select-Object -First $MaxDetails)) {
    $i++; Write-Progress -Activity "Fetching opportunity details" -Status $o.Number -PercentComplete (100 * $i / $MaxDetails)
    $d = Invoke-Json "https://api.grants.gov/v1/api/fetchOpportunity" @{ opportunityId = [int]$o.Id }
    $syn = $d.data.synopsis
    if (-not $syn) { $syn = $d.data.forecast }
    if (-not $syn) { continue }
    $desc = ($syn.synopsisDesc + " " + $syn.forecastDesc) -replace '<[^>]+>', ' ' -replace '&nbsp;', ' ' -replace '\s+', ' '
    $elig = (($syn.applicantTypes | ForEach-Object { $_.description }) -join "; ") + " " + $syn.applicantEligibilityDesc
    $elig = $elig -replace '<[^>]+>', ' ' -replace '\s+', ' '
    $o.Description = if ($desc.Length -gt 600) { $desc.Substring(0, 600) + "..." } else { $desc }
    $o.Eligibility = $elig.Trim()
    $o.AwardCeiling = $syn.awardCeiling
    if ($elig -match '(?i)non-domestic|foreign (institutions|organizations|components)|non-U\.?S\.? (entities|institutions|organizations)') {
        $o.ForeignEligible = if ($elig -match '(?i)(non-domestic|foreign)[^.]{0,60}(are not|not eligible|ineligible)') { "No" } else { "Yes" }
    } elseif ($elig -match '(?i)unrestricted|Others \(see text') { $o.ForeignEligible = "Possibly - read text" }
    else { $o.ForeignEligible = "Likely no" }
    $sc = Get-Score ($o.Title + " " + $desc)
    $o.Score = $sc.Score + [Math]::Min($o.MatchedQueries.Count, 5)
    if ($o.ForeignEligible -eq "Yes") { $o.Score += 8 }
    $o.Matched = $sc.Hits
}
Write-Progress -Activity "Fetching opportunity details" -Completed
$list = @($list | Sort-Object Score -Descending)

# ----------------------------------------------------------------------------
# 2. NIH RePORTER - similar funded projects
# ----------------------------------------------------------------------------
Write-Host "`n[3/3] Searching NIH RePORTER for similar funded projects..." -ForegroundColor Cyan
$fy = @(($today.Year - 3)..$today.Year)
$similar = @{}
foreach ($t in @("oral cancer artificial intelligence", "oral cancer screening low-resource", "oral cancer deep learning detection", "oral potentially malignant", "head and neck cancer global health")) {
    $r = Invoke-Json "https://api.reporter.nih.gov/v2/projects/search" @{
        criteria = @{ advanced_text_search = @{ operator = "and"; search_field = "projecttitle,terms,abstracttext"; search_text = $t }; fiscal_years = $fy }
        limit = 50
        include_fields = @("ProjectTitle", "OpportunityNumber", "Organization", "FiscalYear", "ProjectNum", "ActivityCode", "AwardAmount", "AgencyIcAdmin", "ContactPiName", "ApplId")
    }
    if (-not $r) { continue }
    Write-Host ("  {0,-50} {1,4} projects" -f $t, $r.meta.total)
    foreach ($p in $r.results) {
        $key = ($p.project_num -replace '^\d', '' -replace '-\d+.*$', '')   # core project number
        if (-not $similar.ContainsKey($key)) {
            $similar[$key] = [pscustomobject]@{
                Project = $key; Title = $p.project_title; Organization = $p.organization.org_name
                Country = $p.organization.org_country; PI = $p.contact_pi_name; Mechanism = $p.activity_code
                Institute = $p.agency_ic_admin.abbreviation; Opportunity = $p.opportunity_number
                FiscalYear = $p.fiscal_year; Award = $p.award_amount
                Url = "https://reporter.nih.gov/project-details/$($p.appl_id)"
            }
        }
    }
}
$similarList = @($similar.Values | Sort-Object FiscalYear -Descending)
$mechSummary = $similarList | Where-Object Opportunity | Group-Object Opportunity | Sort-Object Count -Descending |
    Select-Object @{n = "Opportunity"; e = { $_.Name } }, Count, @{n = "Mechanisms"; e = { ($_.Group.Mechanism | Sort-Object -Unique) -join "/" } } -First 15

# ----------------------------------------------------------------------------
# Output
# ----------------------------------------------------------------------------
$stamp = $today.ToString("yyyy-MM-dd")
$top = @($list | Where-Object { $_.Score -gt 5 })
$top | Select-Object Score, Number, Title, Agency, Status, OpenDate, CloseDate, ForeignEligible, AwardCeiling, Matched, Url, Eligibility |
    Export-Csv (Join-Path $OutDir "grants_gov_$stamp.csv") -NoTypeInformation -Encoding UTF8
$similarList | Export-Csv (Join-Path $OutDir "nih_similar_projects_$stamp.csv") -NoTypeInformation -Encoding UTF8
$CuratedFunders | Export-Csv (Join-Path $OutDir "curated_funders.csv") -NoTypeInformation -Encoding UTF8

$rows = foreach ($o in $top) {
    $cd = Parse-Date $o.CloseDate
    $due = if ($cd) { "$($o.CloseDate)<br><small>$([int]($cd - $today.Date).TotalDays) days left</small>" } else { "Not set" }
    $fe = switch -Wildcard ($o.ForeignEligible) { "Yes" { "yes" } "No*" { "no" } "Likely no" { "no" } default { "maybe" } }
    $n = 0.0
    $amt = if ([double]::TryParse([string]$o.AwardCeiling, [ref]$n) -and $n -gt 0) { '$' + ('{0:N0}' -f $n) } else { "" }
    "<tr><td class='score'>$($o.Score)</td><td><a href='$($o.Url)' target='_blank'>$(Html $o.Title)</a><div class='meta'>$(Html $o.Number) &middot; $(Html $o.Agency) &middot; $($o.Status)</div><div class='desc'>$(Html $o.Description)</div><div class='meta'>Matched: $(Html $o.Matched)</div></td><td>$due</td><td><span class='pill $fe'>$(Html $o.ForeignEligible)</span></td><td>$amt</td></tr>"
}
$curRows = foreach ($c in $CuratedFunders) {
    $cls = if ($c.Fit -eq "High") { "yes" } elseif ($c.Fit -like "Low*") { "no" } else { "maybe" }
    "<tr><td>$(Html $c.Region)</td><td><a href='$($c.Url)' target='_blank'>$(Html $c.Funder)</a><div class='meta'>$(Html $c.Programme)</div></td><td><span class='pill $cls'>$($c.Fit)</span></td><td>$(Html $c.Notes)</td></tr>"
}
$simRows = foreach ($s in ($similarList | Select-Object -First 60)) {
    "<tr><td><a href='$($s.Url)' target='_blank'>$(Html $s.Title)</a><div class='meta'>$(Html $s.PI) &middot; $(Html $s.Organization), $(Html $s.Country)</div></td><td>$($s.Mechanism) / $($s.Institute)</td><td>$(Html $s.Opportunity)</td><td>$($s.FiscalYear)</td></tr>"
}
$mechRows = foreach ($m in $mechSummary) {
    "<tr><td><a href='https://grants.nih.gov/grants/guide/search_results.htm?query=$($m.Opportunity)' target='_blank'>$($m.Opportunity)</a></td><td>$($m.Mechanisms)</td><td>$($m.Count)</td></tr>"
}
$hosp = ($Project.Hospitals | ForEach-Object { "<li>$(Html $_)</li>" }) -join ""

$html = @"
<!doctype html><html><head><meta charset="utf-8"><title>Grant Finder - Oral Cancer AI Thailand</title>
<style>
body{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#f5f6f8;color:#1d2330}
header{background:#123c69;color:#fff;padding:24px 32px}header h1{margin:0 0 4px;font-size:24px}
main{padding:16px 32px 48px;max-width:1300px}section{background:#fff;border-radius:8px;padding:16px 20px;margin:18px 0;box-shadow:0 1px 3px #0001}
h2{margin-top:0;font-size:18px;color:#123c69}table{width:100%;border-collapse:collapse;font-size:13px}
th,td{text-align:left;padding:8px;border-bottom:1px solid #e6e8ec;vertical-align:top}th{background:#f0f2f5;position:sticky;top:0}
.meta{color:#667;font-size:12px;margin-top:3px}.desc{font-size:12px;color:#333;margin-top:4px;max-width:750px}
.score{font-weight:700;font-size:16px;color:#123c69;text-align:center}a{color:#0b5cad;text-decoration:none;font-weight:600}
.pill{padding:2px 8px;border-radius:10px;font-size:12px;white-space:nowrap}.yes{background:#d9f2df;color:#17602a}.no{background:#f6dcdc;color:#8a1f1f}.maybe{background:#fff0c9;color:#7a5a00}
.note{background:#eef4fb;border-left:4px solid #123c69;padding:10px 14px;font-size:13px}ul{margin:4px 0}
</style></head><body>
<header><h1>Grant Finder: $(Html $Project.Title)</h1><div>Generated $($today.ToString("dd MMM yyyy HH:mm"))</div></header>
<main>
<section><h2>Project profile</h2><b>Partner hospitals ($($Project.Hospitals.Count)):</b><ul>$hosp</ul>
<div class="note">Tips: Most US federal grants require a US-registered applicant, so look for <span class="pill yes">Yes</span> foreign eligibility or partner with a US university as the prime applicant. All Thai partners will need SAM.gov/UEI registration for US awards. Always confirm details in the official opportunity documents.</div></section>

<section><h2>1. Thai &amp; international funders (curated - check for open calls)</h2>
<table><tr><th>Region</th><th>Funder / programme</th><th>Fit</th><th>Notes</th></tr>$($curRows -join "`n")</table></section>

<section><h2>2. Open &amp; forecasted Grants.gov opportunities ($($top.Count) relevant of $($list.Count) open)</h2>
<table><tr><th>Score</th><th>Opportunity</th><th>Closes</th><th>Foreign eligible</th><th>Award ceiling</th></tr>$($rows -join "`n")</table></section>

<section><h2>3. Funding announcements that have funded similar NIH projects</h2>
<p class="meta">These announcements and mechanisms have already funded oral cancer, AI, or global-health projects. Look for their reissued versions.</p>
<table><tr><th>Opportunity</th><th>Mechanism</th><th># similar projects</th></tr>$($mechRows -join "`n")</table>
<h2 style="margin-top:20px">Similar funded projects ($($similarList.Count)) - potential collaborators</h2>
<table><tr><th>Project</th><th>Mechanism / IC</th><th>Opportunity</th><th>FY</th></tr>$($simRows -join "`n")</table></section>
</main></body></html>
"@
$htmlPath = Join-Path $OutDir "grant_report_$stamp.html"
[IO.File]::WriteAllText($htmlPath, $html, [Text.Encoding]::UTF8)

Write-Host "`nDone." -ForegroundColor Green
Write-Host "  Report : $htmlPath"
Write-Host "  CSVs   : $OutDir"
Write-Host "`nTop 10 Grants.gov matches:" -ForegroundColor Yellow
$top | Select-Object -First 10 Score, Number, ForeignEligible, CloseDate, @{n = "Title"; e = { if ($_.Title.Length -gt 70) { $_.Title.Substring(0, 70) + "..." } else { $_.Title } } } | Format-Table -AutoSize
if (-not $NoOpen) { Start-Process $htmlPath }
