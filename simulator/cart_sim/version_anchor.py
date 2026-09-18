"""Version anchors for every record this simulator's constants come from.

A 1:1 reproduction is only meaningful if each published number is tied to a
specific version of a specific record: which label revision, which regulatory
submission, which manufacturing era and which clinical study. This module records
those anchors with a byte-exact quote from the retained copy of the record, so a
report can state exactly which version of the product it reproduces.

The anchors are evidence, not model parameters: nothing here is fitted, and every
quote is asserted byte-exact by ``tests/test_version_anchor.py`` against the file
in ``data/references/``. Where the record itself states a redaction or a
correction, that is recorded too.
"""

#: Retained FDA prescribing information (the label the US release criteria in
#: :mod:`simulator.cart_sim.lot_criteria` are taken from).
PI_2025_06 = {
    "id": "us_pi_kymriah_revised_2025_06",
    "role": "US prescribing information behind the disclosed release criteria "
    "(>=80% viability by flow, identity by CAR qPCR, dose intervals) and behind "
    "the JULIET/ELARA administered-dose medians",
    "source": "Kymriah (tisagenlecleucel) prescribing information, Novartis",
    "url": "https://www.fda.gov/media/107296/download",
    "file": "data/references/fda_pi_kymriah_current.txt",
    "quote": "Revised: 6/2025",
    "version": "2025-06",
    "caveat": "The retained copy is the current revision; earlier revisions are not "
    "retained, so any number quoted from this record is attributable to the June 2025 "
    "revision and not to the 2017 or 2018 label.",
}

#: Original BLA: the process description in docs/PROCESS_SOURCES.md describes the
#: process as submitted and approved in this era.
BLA_125646_0_2017 = {
    "id": "us_bla_125646_0_sbra_2017_08_30",
    "role": "US original licensure (B-ALL); fixes the manufacturing-process era of "
    "the FDA documents retained in this repository",
    "source": "FDA Summary Basis for Regulatory Action, BLA/STN 125646/0",
    "url": "https://www.fda.gov/media/107962/download",
    "file": "data/references/fda_sbra_107962_bla125646_0_ball_2017-08-30.txt",
    "quote": "   BLA/ STN#: 125646/0",
    "version": "2017-08-30",
    "caveat": "Review-era document; the CMC sections it summarises are (b)(4) "
    "redacted, so it anchors the era, not the numerical process limits.",
}

#: DLBCL sBLA: amendment history of the same application, with a dated amendment id.
BLA_125646_76_2018 = {
    "id": "us_bla_125646_76_sbra_2018_04_13",
    "role": "US DLBCL sBLA; names the amendment that added the 30-day efficacy and "
    "safety update to the original application",
    "source": "FDA Summary Basis for Regulatory Action, BLA/STN 125646/76",
    "url": "https://www.fda.gov/media/113215/download",
    "file": "data/references/fda_sbra_113215_bla125646_76_dlbcl_2018-04-13.txt",
    "quote": "Application Supplement (sBLA), STN 125646/76",
    "version": "2018-04-13",
    "caveat": "The same record dates the amendment: 'the applicant proposed on August 23,\n"
    "2017 (Amendment 16130/967) to supplement their initial submission with a 30-day efficacy and\n"
    "safety update (with a data cut-off date of September 6, 2017)', which is the version "
    "identifier for the JULIET data cut-off used in the label.",
}

#: EU centralised procedure: the retained record is the CHMP assessment report.
EMA_CHMP_2018 = {
    "id": "eu_ema_chmp_assessment_2018_06_28",
    "role": "EU assessment report; source of the EU dose ranges, the non-release rule, "
    "the trial-era manufacturing duration and the site-era statement",
    "source": "EMA/485563/2018, CHMP assessment report, Kymriah",
    "url": "https://www.ema.europa.eu/en/medicines/human/EPAR/kymriah",
    "file": "data/references/ema_kymriah_epar_2018.txt",
    "quote": "Procedure No. EMEA/H/C/004090/0000",
    "version": "2018-06-28",
    "caveat": "This is the CHMP assessment report dated 28 June 2018 (procedure "
    "EMEA/H/C/004090/0000), not the Commission decision; the retained copy carries no "
    "'B/2202' product number and no 23 August 2018 date.",
}

#: Site era, from the same EU assessment report.
SITE_ERA_2016 = {
    "id": "eu_site_fraunhofer_operational_2016_08",
    "role": "Manufacturing-site era: the EU site entered production during the "
    "pivotal programme, so trial-era batches come from two sites",
    "source": "EMA/485563/2018, CHMP assessment report, Kymriah",
    "url": "https://www.ema.europa.eu/en/medicines/human/EPAR/kymriah",
    "file": "data/references/ema_kymriah_epar_2018.txt",
    "quote": "clarified the manufacturing capacity was improved in August 2016, when the EU manufacturing site\n(Fraunhofer) started to actively produce tisagenlecleucel",
    "version": "2016-08",
    "caveat": "Two sites are named in the batch-analysis paragraph ('all batches "
    "manufactures at MP and FH IZI'); batch-level attribution per site is not published.",
}

#: Manufacturing duration: trial era versus the then-current commercial setting.
CYCLE_TIME_2018 = {
    "id": "eu_cycle_time_trial_30_34_days_commercial_24_days",
    "role": "The only published manufacturing-duration figures; the schedule model in "
    "docs/PROCESS_SOURCES.md is otherwise illustrative",
    "source": "EMA/485563/2018, CHMP assessment report, Kymriah",
    "url": "https://www.ema.europa.eu/en/medicines/human/EPAR/kymriah",
    "file": "data/references/ema_kymriah_epar_2018.txt",
    "quote": "staying consistent at a median of 30-34 days which is consistent with\nthe pre-specified 4-5 weeks. In the commercial setting, the time from receipt of leukapheresis to\nproduct shipment is currently 24 days and is targeted to be 22 days going forward",
    "version": "2018-06-28",
    "caveat": "'Currently' means as of the June 2018 assessment; the current commercial "
    "cycle time is not published in the retained corpus.",
}

#: Release rule with published numerical limits (EU).
RELEASE_RULE_2018 = {
    "id": "eu_release_dose_rule_2018",
    "role": "Numerical release/non-release rule that matches the disclosed US dose "
    "intervals in lot_criteria.dose_interval for both weight strata",
    "source": "EMA/485563/2018, CHMP assessment report, Kymriah",
    "url": "https://www.ema.europa.eu/en/medicines/human/EPAR/kymriah",
    "file": "data/references/ema_kymriah_epar_2018.txt",
    "quote": "Products falling below the minimum values in the above allowable cell dose ranges (i.e. 0.2×106 CAR-\npositive viable T-cells per kg or 1.0×108 CAR-positive viable T-cells) were not released for infusion.",
    "version": "2018-06-28",
    "caveat": "The record adds that 'Numerical rounding of\nthe dose was performed by the manufacturing site', "
    "so a released dose may sit slightly outside the stated interval by design.",
}

#: Manufacturing-era shift inside the commercial record.
FONG_ERA_2023 = {
    "id": "us_commercial_era_post_2017_08_30_with_2019_2020_assay_change",
    "role": "Era boundary for the commercial product-attribute distributions in "
    ":mod:`simulator.cart_sim.lot_distributions`",
    "source": "Fong et al., Transpl. Cell Ther. 2023 (commercial tisagenlecleucel outcomes)",
    "url": "https://doi.org/10.1016/j.jtct.2023.06.007",
    "file": "data/references/fong_2023_tct_fulltext_oa.md",
    "quote": "manufacturing data starting after August 30, 2017 (date of first US Food and\nDrug Administration approval)",
    "version": "post-2017-08-30",
    "caveat": "The same record states 'the viability analytical assay was improved between\n"
    "2019 and 2020', so viability drawn from this source spans a pre-change and a "
    "post-change assay era, and batches come from US and non-US sites.",
}

#: Registry era (real-world US/Canada).
PASQUINI_ERA_2020 = {
    "id": "us_registry_era_post_2017_08_30",
    "role": "Era boundary for the real-world viability and time-to-infusion attributes",
    "source": "Pasquini et al., Transplant. Cell Ther. 2020 (CIBMTR real-world tisagenlecleucel)",
    "url": "https://pubmed.ncbi.nlm.nih.gov/32561567/",
    "file": "data/references/pasquini_2020_rwe.txt",
    "quote": "after 30 August 2017 (date of first approval of tisagenlecleucel) in the United States or Canada were eligible",
    "version": "post-2017-08-30",
    "caveat": "Registry eligibility, not a manufacturing record; product attributes are "
    "as-reported by treatment centres.",
}

#: Japan: a different approved release criterion.
JAPAN_2025 = {
    "id": "jp_release_criterion_70pct_viability",
    "role": "Region-specific release criterion for the out-of-specification profile in "
    ":mod:`simulator.cart_sim.lot_distributions`",
    "source": "Kato et al., Cytotherapy 2025 (out-of-specification tisagenlecleucel in Japan)",
    "url": "https://www.sciencedirect.com/science/article/pii/S1465324925006851",
    "file": "data/references/kato_2025_cytotherapy_oos_japan.md",
    "quote": "Low cell viability (less than the release criteria of 70%) and low dose (less than the approved cell range of 0.6–6.0 × 108 CAR+ viable T cells)",
    "version": "2025 (products 2018-2023 era)",
    "caveat": "Japan's viability criterion is 70%, not the US >=80%; an out-of-specification "
    "classification is region-specific. The Japanese release panel itself is in the "
    "retained PMDA review report (jp_pmda_review_2019_02_20), whose numeric limits are "
    "redacted as asterisks.",
}

#: Japan: the approved release panel itself, from the regulator's own review.
PMDA_2019 = {
    "id": "jp_pmda_review_2019_02_20",
    "role": "Region-specific product release panel structure, and the third regulatory "
    "source for the same dose intervals",
    "source": "PMDA review report, Kymriah Suspension for Intravenous Infusion "
    "(Novartis Pharma K.K.), Medical Device Evaluation Division, 20 February 2019",
    "url": "https://www.pmda.go.jp/files/000231278.pdf",
    "file": "data/references/pmda_kymriah_review_2019.txt",
    "quote": "The proposed specifications for the product include description, "
    "identification (CAR transgene), purity\n(copy number of transgene, percentage of "
    "T-cells, percentage of residual CD19-positive B-cells, cell\nviability rate, and "
    "residual bead count)",
    "version": "2019-02-20",
    "caveat": "The disclosed content is the panel list of items; the numeric limits are "
    "asterisk redactions, e.g. 'detection limit (qPCR, ** copies/**µg DNA)', so the "
    "Japanese viability limit itself stays undisclosed here even though Kato 2025 reports "
    "a 70% criterion in practice. The review's approved dosage (0.2-5.0 x 10^6/kg at "
    "<=50 kg; 0.1-2.5 x 10^8 above 50 kg; 0.6-6.0 x 10^8 for adult DLBCL) matches "
    "lot_criteria.dose_interval() independently of the US label and the EU SmPC.",
}

#: Academic-era process anchor (pre-commercial CTL019).
PATENT_2005 = {
    "id": "us20050113564a1_academic_process",
    "role": "Era boundary for the academic transduction-efficiency distribution",
    "source": "US 2005/0113564 A1, Redirected T cells (Carl June / 6th Street FDA-approved CTL019 process)",
    "url": "https://patents.google.com/patent/US20050113564A1/en",
    "file": "data/references/us20050113564a1_gp_text.txt",
    "quote": "median transduction efficiency was 65% (range, 31% to 86%) for anti-CD19-BB-ζ receptors",
    "version": "2005 publication era",
    "caveat": "Retroviral transduction of activated mononuclear cells, pre-commercial "
    "process; not comparable to a commercial lentiviral final product.",
}

ANCHORS = (
    PI_2025_06,
    BLA_125646_0_2017,
    BLA_125646_76_2018,
    EMA_CHMP_2018,
    SITE_ERA_2016,
    CYCLE_TIME_2018,
    RELEASE_RULE_2018,
    FONG_ERA_2023,
    PASQUINI_ERA_2020,
    JAPAN_2025,
    PMDA_2019,
    PATENT_2005,
)


def anchor_lines():
    """Report lines naming the version of every record the constants come from."""
    lines = [
        "Version anchors (which record version each published constant comes from);",
        "each is asserted byte-exact against the retained file by tests/test_version_anchor.py:",
    ]
    for a in ANCHORS:
        lines.append(f"  - {a['id']}  [version {a['version']}]")
        lines.append(f"      uses: {a['role']}")
        lines.append(f"      caveat: {a['caveat']}")
    return lines
