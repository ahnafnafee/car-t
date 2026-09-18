# Manufacturing evidence from papers and patents

Checked 2026-09-16. Published sources recover several numerical specifications
that are absent from the redacted FDA review. These records support separate,
versioned comparison profiles, not a single composite manufacturing recipe:
commercial US product, earlier academic CTL019, and experimental patent processes
must remain distinguishable. This document extends the
[commercial correspondence map](SOURCE_SPECIFICATION.md).

## Commercial US product: published numerical criteria

Pasquini et al. used Novartis manufacturing records linked to CIBMTR batch
identifiers. Their Methods section, **Patients and study design**, explicitly
defines these release criteria for the commercial products in their analysis,
whose data cutoff was January 23, 2020. The dose denominator is **CAR-positive
viable T cells**, not total cells. [Pasquini et al., Blood Advances 2020,
doi:10.1182/bloodadvances.2020003092](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/)

| Attribute | Published criterion | Scope |
| --- | --- | --- |
| Cell viability | At least 80% | US commercial product in the study |
| B-ALL dose, body weight at most 50 kg | 0.2 million to 5 million CAR-positive viable T cells/kg | Weight-dependent interval |
| B-ALL dose, body weight above 50 kg | 10 million to 250 million CAR-positive viable T cells | Absolute interval |
| NHL dose | 60 million to 600 million CAR-positive viable T cells | Absolute interval |

The same source defines a batch as out of specification when a studied release
parameter misses its interval. It does not publish the complete release panel or
all validated assay procedures, and these historical criteria alone do not
establish every later manufacturing revision.

An independent retrospective analysis explicitly contrasts the commercial US
80% viability boundary with the initial trial's 70% boundary. Receiving an
out-of-specification product under an alternative access pathway is not evidence
that the commercial specification disappeared. [Rossoff et al., Blood 2021,
discussion](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/)

The same paper's results paragraph reports additional reasons for OOS
classification: fewer than 2 billion nucleated cells in the leukapheresis product
(three cases), collection more than nine months earlier (one), and more than
50 residual beads per 3 million cells (one). Two cases failed the IFN-gamma
release assay, without a published numeric cutoff in that paragraph. These
observed boundaries provide commercial evidence beyond viability; they are not
a complete specification sheet. In particular, the residual-bead boundary differs
from the academic panel below.

Geographic scope must also be preserved. The results accompanying Table 3 of a
Japanese OOS trial identify a 70% viability boundary, rather than the US 80%
boundary. [Kato et al., Cytotherapy 2025,
doi:10.1016/j.jcyt.2025.04.067](https://www.sciencedirect.com/science/article/pii/S1465324925006851)

## Academic CTL019: disclosed release panel

Bai et al. describe samples from Penn/CHOP pilot studies NCT01626495 and
NCT02906371. Their **Materials and Methods: T cell isolation, vector production,
and generation of CTL019 cells**, printed page 12, supplies the panel below.
It is an academic CTL019 profile, not an authenticated commercial Kymriah master
specification. [Bai et al., Science Advances 2022,
doi:10.1126/sciadv.abj2820](https://pmc.ncbi.nlm.nih.gov/articles/PMC9177075/)

| Measured attribute | Reported boundary |
| --- | --- |
| Viability | At least 70% |
| CD3-positive fraction | At least 80% |
| Residual activation beads | At most 100 per 3 million cells |
| Endotoxin | At most 3.5 EU/mL |
| Residual bovine serum albumin | At most 1 microgram/mL |
| VSV-G DNA surrogate measurement | At most 50 copies/microgram DNA |
| CAR-positive fraction by flow cytometry | At least 2% |
| Vector DNA sequence measurement | 0.02 to 4 copies/cell |
| Mycoplasma, bacterial and fungal tests | Negative |

The methods describe day-3 vector washout, 8-12-day WAVE expansion, bead removal
and cryopreservation. VSV-G DNA is a surrogate, not a direct viral-replication assay.

## Patent process correspondence

[WO2012079000A1](https://patents.google.com/patent/WO2012079000A1/en), **Figure 1B
description** and **Clinical protocol/Table 4**, provides early CART19 clinical
manufacturing evidence. Its description links apheresis, mononuclear-cell
elutriation, bead-mediated enrichment/activation, lentiviral transduction and
day-3 vector washout. Table 4 concerns three early CLL pilot patients; the
surrounding text explicitly records release exceptions. That is useful historical
process evidence, not documentation of the subsequently approved commercial
process. Table 4's numerical image was not transcribed for this review.

Later patents can describe **different processes using the same receptor**.
[US20220168389A1](https://patents.google.com/patent/US20220168389A1/en),
**Example 1** and **Materials and Methods: Generation of CAR Constructs**, describes
rapid manufacture involving quiescent T cells and identifies its receptor as the
construct used in Penn CTL019 trials. This does not establish that its rapid
process replaced commercial Kymriah production. Accordingly, the patent's
experimental processing options must not silently become Kymriah defaults.

## Additional commercial process evidence

The [2019 PMDA review](https://www.pmda.go.jp/files/000252613.pdf), **sections
2.1.1-2.1.3, printed page 10**, identifies separate Gag/Pol, Env, Rev and transfer
components, VSV-G pseudotyping, plasmid production from Stbl3 bacterial cell
banks, and 293T producer-cell banks. It also contains redactions in control items
and processing details. These disclosures improve the process-component map but
do not disclose every lot-specific operating limit or full plasmid sequence.

Versioning matters even for an apparently simple measurement. A manufacturer-
authored clinical manufacturing report states that the viability analytical assay
changed during 2019-2020, changing how representative the final cell-count and
viability measurements were at infusion. A value therefore needs an assay and
process version, not just a numeric threshold. [Fong et al., Transplant Cell Ther
2023;29(9):579.e1–e10, discussion (printed p. 579.e5, verified against the retained
open-access full text `fong_2023_tct_fulltext_oa.md`)](https://www.astctjournal.org/article/S2666-6367%2823%2901355-6/fulltext).
An earlier investigator-attributed abstract presented the same data line:
Eldjerou et al., Blood 2019;134(Suppl 1):5066 (abstract; first author of the
precursor, not of the 2023 full article).

## Commercial US product: process parameters and operating ranges

Version label in the Source column. SBRA = FDA B-ALL advisory-committee summary background review, BLA 125646/0, Aug 30 2017 [https://www.fda.gov/media/107962/download](https://www.fda.gov/media/107962/download). CMC Review = "CMC Review, August 29, 2017 - KYMRIAH" and the Melhem DP memo, batch-record extracts, and CMC information requests, all inside the BLA 125646/0 approval-history package [https://www.fda.gov/media/107978/download](https://www.fda.gov/media/107978/download). EPAR = EMA Kymriah assessment report EMA/CHMP/443047/2018 [https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf).

| Parameter | Value/range | Source (version) |
|---|---|---|
| Appearance (color) | "Colorless to slightly yellow" (formulated product) | commercial US [CMC Review, Table 37, printed p. 112](https://www.fda.gov/media/107978/download) |
| Identity | CAR q-PCR "Positive" (post-harvest sample) | commercial US [CMC Review, Table 37, printed p. 112](https://www.fda.gov/media/107978/download) |
| % viable T cells (purity) | redacted `(b) (4)` | commercial US [CMC Review, Table 37, printed p. 112](https://www.fda.gov/media/107978/download) |
| Transduction efficiency (CAR q-PCR) | redacted `(b) (4)` | commercial US [CMC Review, Table 37, printed p. 112](https://www.fda.gov/media/107978/download) |
| Cell viability | redacted `(b) (4)`; "Cell viability is a lot release specification with an acceptance criterion of (b) (4)" | commercial US [SBRA, impurities section](https://www.fda.gov/media/107962/download); [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Residual beads (microscopy) | redacted `(b) (4)`; at end of expansion step "at maximum (b) (4) in 10 mL solution" | commercial US [SBRA](https://www.fda.gov/media/107962/download); [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| % viable CD19+ B cells | redacted `(b) (4)`; B-lineage cells removed in-process, "No residual B-lineage cells have been detected in any batch manufactured at the Novartis Morris Plains Facility" (acceptance criterion and LOQ both `(b) (4)`) | commercial US [SBRA](https://www.fda.gov/media/107962/download); [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Total cell count | "Report cells/mL" — no specification (footnote 4: not a CQA, used in dose calculation) | commercial US [CMC Review, Table 37, printed p. 112, fn 4](https://www.fda.gov/media/107978/download) |
| Number of viable cells (calculated) | redacted `(b) (4)` | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Dose (calculated) | "0.2 to 5.0 × 10⁶ transduced viable T cells/kg body weight (≤50 kg)"; "0.1 to 2.5 ×10⁸ transduced viable T cells (> 50 kg)"; formula "(%CAR expression x Viable cell concentration x Volume per dose)/100" | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download). EU parallel: B-ALL ≤50 kg 0.2–5.0 × 10⁶/kg; >50 kg 0.1–2.5 × 10⁸; DLBCL 0.6–6 × 10⁸, 1–3 bags [EPAR, §4.2 dose, txt lines 1571–1580](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| CAR expression by flow cytometry | redacted `(b) (4)` | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| IFN-γ release (potency) | redacted `(b) (4)`; acceptance "remains unchanged at (b)(4)/transduced cell" from the filing value | commercial US [CMC Review, §3.2.P.5 spec-setting + Table 37, printed pp. 111–112](https://www.fda.gov/media/107978/download) |
| Bacterial endotoxin | redacted `(b) (4)` | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Sterility | "Negative" (formulated product) | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Mycoplasma | "Negative" (qPCR on pre-harvest culture supernatant, before cryopreservation media added) | commercial US [CMC Review, Table 37 p. 112 + fn 1,5](https://www.fda.gov/media/107978/download); [SBRA, Table 1 fn 5](https://www.fda.gov/media/107962/download) |
| VSV-G DNA (qPCR) | redacted `(b) (4)` | commercial US [CMC Review, Table 37, p. 112](https://www.fda.gov/media/107978/download) |
| Red blood cells in starting material | recommended target `(b) (4)`; "The majority of incoming patient leukapheresis material met the recommended target"; appearance test is the RBC control (high RBC → color lot-release failure) | commercial US [SBRA](https://www.fda.gov/media/107962/download) |
| NK cells | no lot-release test | commercial US [SBRA](https://www.fda.gov/media/107962/download) |
| Culture expansion duration | "expanded in culture for up to (b) (4) to reach sufficient numbers" (redacted) | commercial US [SBRA, manufacturing process](https://www.fda.gov/media/107962/download) |
| Pathway selection | "The cellular composition of the leukapheresis material determines which of two manufacturing pathways is used for T cell enrichment" | commercial US [SBRA](https://www.fda.gov/media/107962/download) |
| Bead carry-over reduction | "up to a 5000-fold reduction of residual carry-over by volume replacement" (multiple wash + volume-replacement steps) | commercial US [SBRA](https://www.fda.gov/media/107962/download) |
| Final (infusion) formulation | Plasma-Lyte A 31.25 % v/v; Dextrose & NaCl 31.25 % v/v; HSA 20 % v/v; Dextran 40 10 % v/v; Cryoserv DMSO 7.5 % v/v (final DMSO 7.5 %) | commercial US [Melhem DP memo, Tables 33/36 (BLA package)](https://www.fda.gov/media/107978/download). EU excipient list: glucose, sodium chloride, human albumin solution, dextran 40, DMSO, sodium gluconate, sodium acetate, potassium chloride, magnesium chloride, sodium-N-acetyltryptophanate, sodium caprylate, aluminium, water for injections [EPAR, txt lines 1582–1584](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Cryopreservation / storage | vapor-phase liquid nitrogen, ≤ −120 °C; "stored in the vapor phase of liquid nitrogen (≤ -120 C)"; lowest LN₂ temperature observed −135.2 °C | commercial US [SBRA, Table 1 fn 2](https://www.fda.gov/media/107962/download); [Melhem DP memo (BLA package)](https://www.fda.gov/media/107978/download) |
| Shelf life | 9 months at ≤ −120 °C (VPLN2) in infusion bags; in-use shelf life 30 minutes at 20–25 °C after thawing; CMC Review stability: healthy-donor product 12 months / patient product 9 months (DSR5135 series) | commercial US [CMC Review, stability (BLA package)](https://www.fda.gov/media/107978/download); EU parallel: "shelf-life of 9 months for CTL019 stored in infusion bags at ≤ -120°C in vapour phase liquid nitrogen, and 30 minutes in-use shelf-life after thawing at room temperature 20-25°C" [EPAR, txt lines 1665–1667](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Container closure | EVA infusion bag(s) with PVC tubing and luer spike interconnector; 10–30 mL and 30–50 mL freezing bags (510(k), CE); compatibility demonstrated at low (1 × 10⁸ total cells, 1 × 10⁷/mL) and high (3 × 10⁹ cells, 1 × 10⁸/mL) dose levels | commercial US [CMC Review, container-closure section (BLA package)](https://www.fda.gov/media/107978/download); [EPAR, txt lines 1602–1610](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Critical process parameters (CPP list) | "starting viable WBC, static culture viable WBC seeding number, and Positive selection starting viable WBC" — all numeric values redacted `(b) (4)` | commercial US [CMC Information Request, July 28 2017, re Amendment #32 (BLA package)](https://www.fda.gov/media/107978/download) |
| CPP lower limits | FDA recommended tightening: starting viable WBC lower limit to "exclude the lower 3 terminated/rejected batches" (fig 2-7); static culture seeding lower limit to exclude "the lower terminated batch" (fig 2-31); tighter positive-selection starting viable WBC (fig 2-12); limits `(b) (4)` | commercial US [CMC IR, July 28 2017 (BLA package)](https://www.fda.gov/media/107978/download) |
| Historical process-time ranges | Table 6-4 (unit-operation time ranges for CTL019), values `(b) (4)`; classified as "historical ranges," not CPPs | commercial US [CMC IR, July 28 2017 (BLA package)](https://www.fda.gov/media/107978/download) |
| Leukapheresis hematocrit stop rule | "Record the Hematocrit % from the Leukapheresis: NOTE: if ≥30% stop and call" | commercial US [batch record p. 48 item 53, quoted in CMC Review (BLA package)](https://www.fda.gov/media/107978/download) |
| Collection kit selection | 70 mL CS kit for < 10⁹ TNC; 225 mL CS5 kit for ≥ 10⁹ TNC | commercial US [CMC Review (BLA package)](https://www.fda.gov/media/107978/download) |
| Flow-gating review trigger | %CAR+/CD19+ < 10 % requires supervisor review | commercial US [CMC IR, Mar 29 2017 (BLA package)](https://www.fda.gov/media/107978/download) |
| Throughput (measured) | median 23 days (range 21–37) from receipt of leukapheresed material at the facility to return of product to the clinical site, including shipping; first 37 commercial B-ALL patients, cutoff Jan 30 2018; orders from 13 US treatment sites | commercial US [Tyagarajan et al. 2020, Mol Ther Methods Dev, Results (PMC6970133)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6970133/) |
| Turnaround (stated, 2016, pre-acquisition) | "The T cell engineering process that we have developed takes approximately 14 to 16 days from receipt of the patient's white blood cells at our manufacturing facility to release for delivery to the site for infusion" | commercial US, Kite intent [10-K FY2016](https://www.sec.gov/Archives/edgar/data/1510580/000151058017000003/kite20161231-10k.htm) |
| Manufacturing sites | US: Novartis Morris Plains, 220 East Hanover Avenue, Morris Plains NJ 07950 (FEI 3010353512); EU: plus Fraunhofer Institut für Zelltherapie und Immunologie (FH IZI), Perlickstraße 1, 04103 Leipzig (batch certification: Novartis Pharma GmbH, Nuremberg); vector: Oxford BioMedica (OXB), Oxford, UK. "All three manufacturing facilities (Morris Plains New Jersey, USA, [redacted] have been inspected during the BLA review" | commercial US + EU [CMC Review (BLA package)](https://www.fda.gov/media/107978/download); [EPAR, txt lines 1188, 1392–1393](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Site count (as stated, 2023–2025) | "Novartis has a significant global commercial manufacturing presence, with two manufacturing facilities (US and Switzerland)" | Japanese market paper, global scope [Iwamoto et al. 2025, Methods (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/) — note: EPAR 2018 names US + Leipzig (Germany); both statements reported as made, not merged |
| Vector substance / product shelf life | vector substance 12 months at −60 to −90 °C; vector product 36 months at −60 to −90 °C; WCB 1390.01 being converted to a new MCB | EU (EPAR) [EPAR, txt lines 1227, 1336, 1345](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Process architecture | "The manufacturing process for CTL019 is a continuous process with no holding step; beginning with thawing of the leukapheresis starting material and ending with finished product formulation" | EU (EPAR) [EPAR, txt line 1633](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Bead specification (EU) | "specification for beads: ≤ 50 beads per 3 x 106 cells"; max beads per single pediatric dose computed as 5 × 10⁹ total cells (in 50 mL) × 50; max benzyl alcohol exposure 21 µg | EU (EPAR) [EPAR, txt lines 2127–2147](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf). Consistent with the observed US OOS boundary (>50 residual beads/3 × 10⁶ cells, Rossoff 2021, see existing doc) |
| Pediatric process capability | facilities accept leukapheresis from patients ≥ 6 kg; "tisagenlecleucel has been manufactured for 2 patients < 3 years of age in [commercial setting]" (improvements ensuring < 3-year leukapheresis material usable) | EU (EPAR) [EPAR, txt lines 6170–6175](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf) |
| Shipping | "KYMRIAH is shipped in a vapor phase liquid nitrogen dry shipper (dewar) to the clinical infusion center by a qualified courier" | commercial US [SBRA](https://www.fda.gov/media/107962/download) |
| Dose rationale (academic data in US filing) | UPenn pediatric-ALL data: response at the lowest dose, 0.17 × 10⁶ cells/kg | academic data cited in commercial US filing [CMC Review, dose rationale (BLA package)](https://www.fda.gov/media/107978/download) |
| Vector titer measurement | "the titer of viral vector can be measured by analyzing the percentage of healthy donor cells transduced by predefined MOIs" | commercial US (process description) [Levine et al. 2017, Mol Ther (PMC5363291)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363291/) |
| TE site comparability | OXB vector two-site study: "consistent, dose-dependent transduction efficiency was observed at both sites (unpublished data)"; "equivalent performance across donors and manufacturing sites" | commercial US [Levine et al. 2017 (PMC5363291)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363291/) |
| Dose, Japan | B-ALL >50 kg: 0.1–2.5 × 10⁸ CAR-positive viable T cells irrespective of body weight; DLBCL usual adult dosage 0.6–6.0 × 10⁸ | Japanese market [PMDA review report 2019, §1.1 (txt lines 285–289)](https://www.pmda.go.jp/files/000252613.pdf) |

## Decision rules (OOS, holds, deviations)

- **Hold/stop at collection.** Batch-record stop rule for leukapheresis hematocrit: "Record the Hematocrit % from the Leukapheresis: NOTE: if ≥30% stop and call" [batch record p. 48 item 53, quoted in CMC Review (BLA package)](https://www.fda.gov/media/107978/download). Hematocrit percentages are "measured and reported by the leukapheresis collection sites"; the recommended RBC target is redacted `(b) (4)` [SBRA](https://www.fda.gov/media/107962/download).
- **Supervisor review trigger (flow).** %CAR+/CD19+ < 10 % requires supervisor review [CMC IR, Mar 29 2017 (BLA package)](https://www.fda.gov/media/107978/download).
- **CPP deviation limits (redacted).** CPP lower limits `(b) (4)`; FDA recommended tightening three CPP lower limits specifically to exclude terminated/rejected batches (3 batches for starting viable WBC, 1 for seeding number) [CMC IR, Jul 28 2017 (BLA package)](https://www.fda.gov/media/107978/download).
- **Historical process-time ranges.** Unit-operation times (Table 6-4, values `(b) (4)`) are classified as "historical ranges," not CPPs; FDA asked to "clarify if a deviation will be triggered if a unit operation exceeds a historical range of the process time limit" [CMC IR, Jul 28 2017 (BLA package)](https://www.fda.gov/media/107978/download).
- **OOS appearance released under exception.** One out-of-specification color batch was released under exception; rationale: autologous red blood cells are not a safety risk; appearance tested per SOP AM10041C [CMC Review, per-test detail, printed pp. 113–118 (BLA package)](https://www.fda.gov/media/107978/download).
- **Pre-approval OOS experience.** Of the batches excluded from specification setting, "some batches were not released for clinical use due to out-of-specification testing results"; batches meeting specs but not infused (patient health status changes) were also excluded [CMC Review, spec-setting, printed pp. 111–112 (BLA package)](https://www.fda.gov/media/107978/download).
- **US post-marketing deviations.** Multiple US post-marketing batches deviated from specification (deviating values redacted: "the minimum value, ***% for pediatric ALL and ***% for DLBCL"); "The reasons for frequent deviations from the specification occurring in the US post-marketing settings were investigated in detail, but no definite causes have been identified. Multiple actions will be taken continuously to reduce the risk of deviation from the specification" [PMDA review report 2019, §2.R.2 control strategy (txt lines 872–891)](https://www.pmda.go.jp/files/000252613.pdf). Applicant position: US-approved spec was tighter than the investigational spec, so the Japan spec "will be changed so that it becomes the same as that for the investigational product" [same section].
- **Control-by-verification position (Japan).** PMDA: in process validation, "[redacted] deviated from the specification as a result of variations in process performance"; with an autologous raw material, "at present, there is no choice but to control the processes in a broader way"; pCQAs to be controlled within the quality control strategy. Applicant: "It is difficult to control the specification tightly, and the product is to be controlled by verification so that quality attributes including pCQAs can be assessed [redacted]" — accepted by PMDA [PMDA report 2019, §2.R.2 (txt lines 893–919)](https://www.pmda.go.jp/files/000252613.pdf).
- **OOS product disposition (Japan).** OOS batches were supplied to patients under a phase-3b clinical trial (NCT04094311); year 1–4: 42 patients received OOS tisagenlecleucel (6 B-ALL, 36 DLBCL) in 18 of 44 certified treatment centers; initial results (N = 29): safety and efficacy of OOS product "appears comparable" to in-specification product [Iwamoto et al. 2025, Results/Discussion (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/).
- **Japan 2022 process improvements (OOS reduction).** "The key process improvements include the use of 5 % plasma-derived human AB serum as an alternative serum source (Fig. 2A) and a simplified sample preparation for final product cell viability testing (Fig. 2B)" → MSR 87.9 % → 94.6 %, SSR 93.0 % → 97.5 %, termination 6.0 % → 1.9 %, overall OOS 6.1 % → 3.5 %, viability OOS 2.8 % → 0.2 % [Iwamoto et al. 2025 (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/).
- **Mycoplasma (vector) revalidation — postmarketing commitment.** SBRA: "The review team recommends a Postmarketing Commitment for KYMRIAH for the revalidation of the (b) (4) Mycoplasma Test Validation" for Vector (b) (4) Material performed by (b) (4); Amendment 57 (Aug 28 2017): Novartis commits to revalidate per protocol "Validation of Mycoplasma (b) (4) assay in the presence of KYMRIAH (DOCUMENT No: VP300808.DRAFT00)" (submitted Jul 19 2017); final validation report due June 30 2018 [SBRA, CMC Postmarketing Commitment (printed p. 23)](https://www.fda.gov/media/107962/download). Related PLI items, both resolved: mycoplasma tested on culture supernatant only (not cells + supernatant) — FDA accepted (risk low after long culture); assay validated in medium, not CAR-T matrix — FDA accepted (no matrix effect observed; method shown more sensitive than the standard method) [CMC Review (BLA package)](https://www.fda.gov/media/107978/download).
- **US batch-release testing policy.** FDA determined tisagenlecleucel will NOT be tested for batch release (samples only on request); no formal comparability protocols — Morris Plains manufacturing changes addressed via BLA supplements [CMC Review, 3.2.R.2/3.2.R.3 (BLA package)](https://www.fda.gov/media/107978/download).
- **Specification-setting changes (2017).** Amendment #46: FDA-recommended narrowing of %viable T cells and lowering of the CAR transgene (copies/cell) upper limit (CMC-OTAT IR, Jul 21 2017); IFN-γ acceptance unchanged from filing value `(b) (4)` [CMC Review, spec-setting, printed pp. 111–112 (BLA package)](https://www.fda.gov/media/107978/download).

## Version history (site transfer, assay changes, product revisions)

- **Dec 2012 — facility transfer.** The Morris Plains, NJ facility was acquired from Dendreon in December 2012 [Melhem DP memo (BLA package); Tyagarajan et al. 2020 (PMC6970133)](https://www.fda.gov/media/107978/download). First FDA inspection of the cell-product facility was the 2017 PLI (Melhem memo dates it April 3–7 2017; the BLA package timeline records the PLI as Mar 7 → Apr 4 2017) [BLA package](https://www.fda.gov/media/107978/download).
- **2014 — pre-scale manufacturing (Kite).** S-1/A (Dec 9 2014): "We currently rely on outside vendors to manufacture clinical supplies and process our product candidates, which is currently and will continue to be done on a patient-by-patient basis. We have not yet caused our product candidates to be manufactured or processed on a commercial scale…"; the intended facility approach was based on the NCI approach, with "limited experience in manufacturing…" [S-1/A, Dec 9 2014](https://www.sec.gov/Archives/edgar/data/1510580/000119312514437675/d824808ds1a.htm).
- **2016 — planned US commercial site (Kite, superseded).** 10-K FY2016: planned commercial manufacturing at an El Segundo (adjacent to LAX) facility for KTE-C19; ~14–16 day WBC-receipt-to-release turnaround; "Kite Konnect" logistics platform under development. This pre-acquisition intent was superseded by Morris Plains (acquired Dec 2012) as the commercial site [10-K FY2016](https://www.sec.gov/Archives/edgar/data/1510580/000151058017000003/kite20161231-10k.htm).
- **2017 — BLA 125646/0 (B-ALL) lifecycle.** eCTD received Feb 3 2017; Advisory Committee Feb 22 2017; filing meeting Mar 15 2017; PLI at Morris Plains (Mar–Apr 2017); PLI at the vector substance facility classified VAI. Amendment #32 (Jun 16 2017) defined the CPP list; CMC-OTAT IR Jul 21 2017 (spec narrowing); CMC IR Jul 28 2017 (CPP limits, Table 6-4); Amendment 57 (Aug 28 2017, mycoplasma revalidation); approval Aug 30 2017 (BLA 125646/0) [BLA package; SBRA](https://www.fda.gov/media/107978/download).
- **2017–2018 — DLBCL label and CMC changes.** PAS 125646/80 (Nov 21 2017) significant CMC changes pending at /76; DLBCL approved May 1 2018 (BLA 125646/76) [BLA package approval history](https://www.fda.gov/media/107978/download).
- **2019 — Japan approval and spec alignment.** Japan approvals (March 2019: r/r B-ALL and r/r DLBCL, ≤ 25 y; orphan regenerative medical product designation May 25 2016, No. 3 of 2016); PMDA review report documents the US post-marketing spec deviations and the decision to align the Japan spec with the investigational spec; 2019 safety-specification amendment: "Transmission of an infectious agent" added, "Development of replication competent lentivirus" removed [PMDA report 2019 (txt lines 285–289, 872–919, safety-spec section)](https://www.pmda.go.jp/files/000252613.pdf); [Iwamoto et al. 2025 (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/).
- **2019–2020 — viability assay change.** Final-product viability assay method changed during 2019–2020 (see existing "Additional commercial process evidence" section, Fong et al. 2023; Eldjerou et al. 2019 abstract as precursor).
- **2021–2025 — US product revisions.** Approval letters: Jun 11 2021 (/429); May 27 2022; Apr 12 2024 (/854); Jun 13 2024 (/860); Aug 16 2024 (/902, REMS minor modification); Jun 26 2025 (/984, REMS eliminated) [BLA package approval-history letters](https://www.fda.gov/media/107978/download).
- **2022 — Japan process improvements and second indication.** 5 % plasma-derived human AB serum alternative serum source + simplified viability sample preparation (see Decision rules); r/r follicular lymphoma indication Aug 2022 [Iwamoto et al. 2025 (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/).
- **Site expansion (as stated, not merged).** EPAR 2018: cell product manufactured at Morris Plains (US) + FH IZI Leipzig (Germany), commercial supply "intended from a site in Germany at the Fraunhofer Institute, in Leipzig"; Iwamoto 2025 (data through Dec 31 2023): "two manufacturing facilities (US and Switzerland)" [EPAR, txt lines 1392–1393, 2419](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-european-public-assessment-report-epar_en.pdf); [Iwamoto et al. 2025 (PMC11891598)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11891598/).
- **Controlled documents (versions in the filing).** Commercial batch record FRM-7061151 v1.0 (QA 2016-12-16); WP-7004671 Commercial [Cell] Work Procedure (eCTD 1.11.1 amendment 6, Mar 14 2017; QA Mar 1 2017); SOP versions with effective dates incl. SOP-7018260 v2.0 (2015-04-15) and SOP-7018266 (bioreactor) v6.0 (2016-12-06); media-hold integrity studies USMB.098.TD / USMB.115.TD (static and perfusion) and USMB.372.VD / USMB.362.VD / USMB.363.VD (study numbers only; data not in public record) [Melhem DP memo; batch-record extracts (BLA package)](https://www.fda.gov/media/107978/download).

## Academic CTL019: process parameters

- **Process description (verbatim).** "T cells were enriched by mononuclear cell elutriation and then washed and activated with anti-CD3/CD28–coated paramagnetic beads. A lentiviral vector containing a previously described CD19-specific CAR with 4-1BB/CD3ζ transgene was constructed and produced (33), which was then used to transduce the cells during activation and was washed out 3 days after the culture initiation (42). A rocking platform device (WAVE Bioreactor System) was used to expand cells for 8 to 12 days, and the beads were then magnetically removed. CTL019 cells were harvested and cryopreserved in infusible medium." Starting material: autologous PBMCs by standard leukapheresis [Bai et al. 2022, Sci Adv, Methods, printed pp. 12–13 (doi:10.1126/sciadv.abj2820)](https://doi.org/10.1126/sciadv.abj2820). (Release-criteria panel from the same paper is already tabulated in the existing "Academic CTL019" section.)
- **Early-trial vector supply (academic).** "In early clinical trials performed at the University of Pennsylvania, multiple vector suppliers were used during the generation of the CD19-targeting therapy CTL019"; the OXB vector's transduction efficiency was examined in a two-site study with "consistent, dose-dependent transduction efficiency … at both sites (unpublished data)" and "equivalent performance across donors and manufacturing sites" [Levine et al. 2017, Mol Ther (PMC5363291)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363291/).
- **Academic process description (commercial review, CTL019-specific).** Enrichment by counterflow centrifugal elutriation ("separates cells by size and density and maintains cell viability"); anti-CD3/anti-CD28 coated beads (aAPCs) "easily removed … through magnetic separation"; "In the presence of interleukin-2 and aAPCs, T cells can grow logarithmically in a perfusion bioreactor for several weeks"; WAVE Bioreactor (now Xuri; GE Healthcare Life Sciences) rocking platform "used to expand the CD19-targeted CAR T cell therapy CTL019"; G-Rex (Wilson Wolf) noted as an alternative for low seeding densities; vector titer by % healthy-donor cells transduced at predefined MOIs [Levine et al. 2017 (PMC5363291)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5363291/).
- **Dose-floor data from the academic program.** UPenn pediatric-ALL cohort: responses at the lowest dose, 0.17 × 10⁶ cells/kg (basis for the lower bound of the dose range) [CMC Review, dose rationale (BLA package)](https://www.fda.gov/media/107978/download).
- **Study identifiers.** CTL019 academic/early clinical studies NCT01626495 and NCT02906371 (CHOP/Penn) [Bai et al. 2022 (doi:10.1126/sciadv.abj2820)](https://doi.org/10.1126/sciadv.abj2820).

## Patent-disclosed process examples

Non-limiting-examples caveat: US20220168389A1 states of its Examples that they are "provided for purposes of illustration only, and are not intended to be limiting unless otherwise specified" ([0441]). All values below are patent examples/claim ranges, not Kymriah operating parameters; assignees as listed on Google Patents (Kite Pharma Inc for US12600775B2/US20210161959A1 — application US17/091,039, inventors Bot, Rossi; Novartis AG / University of Pennsylvania for US20220168389A1 — application US17/602,730, filed 2020-04-10, inventor O'Connor).

| Parameter | Value | Example | Patent |
|---|---|---|---|
| Serum during activation/incubation | serum-free or ≤ 0.1–2 % serum, 1–10 h (e.g. 2–6 h) | claim ranges | US20220168389A1 [https://patents.google.com/patent/US20220168389A1/en](https://patents.google.com/patent/US20220168389A1/en) |
| Deoxynucleosides in transduction medium | 40 µM–1.5 mM (e.g. 50 µM) for 14–30 h (e.g. 14–24 h) | claim ranges | US20220168389A1 |
| Cell concentration (rapid manufacture) | ≥ 0.7 × 10⁷ to 1 × 10⁸ cells/mL (e.g. about 1 × 10⁷ cells/mL) | claim ranges | US20220168389A1 |
| Transduction-efficiency increase (deoxynucleosides) | ≥ 1–5 fold | claim ranges | US20220168389A1 |
| Manufacturing duration | complete manufacturing within < 24 h of T-cell collection ("ultrashort"), quiescent CAR-T; potent dose-dependent anti-leukemic activity, persistent engraftment (murine xenograft AML model) | Example 1 ([0442]) | US20220168389A1 |
| Serum starvation step | ~3 h serum starvation; ~2-fold iRFP signal | Example 4, "Rapid Manufacturing of CAR T Cells without T Cell Activation" ([0465]) | US20220168389A1 |
| MCL dosing embodiment | 1.8 × 10⁶, 1.9 × 10⁶, or 2 × 10⁶ CAR-positive viable T cells/kg, maximum 2 × 10⁸ (patients ≥ 100 kg) | dosing embodiments | US12600775B2 [https://patents.google.com/patent/US12600775B2/en](https://patents.google.com/patent/US12600775B2/en) |
| B-ALL dosing embodiment | 0.5 × 10⁶, 1 × 10⁶, or 2 × 10⁶ CAR-positive viable T cells/kg | dosing embodiments | US12600775B2 (application version: US20210161959A1 [https://patents.google.com/patent/US20210161959A1/en](https://patents.google.com/patent/US20210161959A1/en)) |
| Dose form / infusion | single-use, patient-specific infusion bag; IV by gravity or peristaltic pump over 30 minutes | dosage-form embodiment | US20210161959A1 |
| T-cell separation methods (generic) | elutriation, MACS, FACS, bead-based column separation listed as enrichment options | method description | US20210161959A1 |
| Cell-characterization example data | IFN-γ by coculture 6309.5 (424.0–2.0 × 10⁴) pg/mL etc. (MCL cohorts; classical n = 38, blastoid n = 16) | example tables (Table 26) | US20210161959A1 |

Patents in the corpus that were scanned and contain **no usable manufacturing process parameters** (identity from file headers): US20170107286A1 "Chimeric antigen receptors targeting CD-19"; US20050113564A1 "Chimeric receptors with 4-1BB stimulatory signaling domain" (qualitative transduction/NK-cell description only); US9701758B2 "Anti-CD19 scFv (FMC63) polypeptide"; US10125222B2 "Method for the preparation of high molecular weight oligo(alkylene glycol) functionalized polyisocyanopeptides" (not CAR-T-related); US8262992B2 "Modular sensor cassette" (not CAR-T-related); US11535869B2 (fetch-failure stub, 124 B — content unusable). The WO2012079000A1 early-clinical process correspondence (Fig 1B / Table 4) is already covered in the existing "Patent process correspondence" section.

## Redacted and absent content

Redactions are quoted verbatim as they appear in the public documents (FDA: `(b) (4)`; PMDA: `***` / `*************`); no values are guessed.

**Redacted values (verbatim, with location):**

- Table 37 (CMC Review, printed p. 112; commercial US) — test rows whose requirement column is redacted `(b) (4)`: "Percentage of viable T cells", "Determination of transduction efficiency by CAR-q-PCR", "Cell viability", "Determination of residual beads by microscopy", "Percentage of viable CD19+ B cells", "Number of viable cells (calculated)", "Determination of CAR expression by flow cytometry", "Release of IFNγ in response to CD19-expressing target cells — • (b)(4)", "Bacterial Endotoxins", "Determination of VSV-G DNA by quantitative PCR (qPCR)". Disclosed in the same table: Appearance "Colorless to slightly yellow", Identity "Positive", Total cell count "Report cells/mL", Sterility "Negative", Mycoplasma "Negative", and the dose block (see table above). [CMC Review (BLA package)](https://www.fda.gov/media/107978/download)
- Spec-setting passage (CMC Review, printed pp. 111–112): "narrowing the specifications for percentage of viable T cells from (b)(4) and for lowering the upper limit for CAR transgene (b)(4)"; IFN-γ "remains unchanged at (b)(4)/transduced cell". [CMC Review (BLA package)](https://www.fda.gov/media/107978/download)
- SBRA (commercial US): "Cell viability is a lot release specification with an acceptance criterion of (b) (4)"; "An acceptance criterion of (b) (4) B cells in KYMRIAH was established using the validated analytical method with a LOQ = (b) (4)"; "the recommended target for red blood cells (RBC), which is (b) (4)"; "at maximum (b) (4) in 10 mL solution"; "actively removed (b) (4) to meet the acceptance criterion of no mor[e than]…"; "expanded in culture for up to (b) (4) to reach sufficient numbers". [SBRA](https://www.fda.gov/media/107962/download)
- SBRA postmarketing commitment (printed p. 23): "revalidation of the (b) (4) Mycoplasma Test Validation" for "Vector (b) (4) Material performed by (b) (4)"; protocol title "Validation of Mycoplasma (b) (4) assay in the presence of KYMRIAH (DOCUMENT No: VP300808.DRAFT00)". [SBRA](https://www.fda.gov/media/107962/download)
- CMC Information Request (Jul 28 2017): "a. The lower limit of (b)(4) may be more appropriate for the [redacted] starting viable WBC to exclude the lower 3 terminated/rejected batches. See figure 2-7." (three `(b) (4)` CPP limits); "You provided the ranges process time based on historical ranges for CTL019 unit operations (Table 6-4). (b)(4)". [CMC IR (BLA package)](https://www.fda.gov/media/107978/download)
- PMDA report 2019 (Japanese market): "the minimum value, ***% for pediatric ALL and ***% for DLBCL" (§2.R.2, txt line 879); "[redacted] deviated from the specification as a result of variations in process performance" (txt line 901); stability data redacted. [PMDA report 2019](https://www.pmda.go.jp/files/000252613.pdf)
- CMC Review (commercial US): vector substance manufacturer "[redacted CMO] (facility redacted)"; "All three manufacturing facilities (Morris Plains New Jersey, USA, [redacted] have been inspected during the BLA review". [CMC Review (BLA package)](https://www.fda.gov/media/107978/download)

**Structurally absent from the public record:**

- The FDA-posted CMC Review is a **partial posting**: printed pp. 13–100 and pp. 123–142 are not posted (the posted span is pp. 1–12, 101–122, 143–151); the vector structure figures on printed pp. 13–14 are unposted. [BLA package posting](https://www.fda.gov/media/107978/download)
- Complete master production record / commercial work procedure — only fragments are quoted in the public record (FRM-7061151 v1.0, WP-7004671, p. 48 item 53 hematocrit note, color-coded coding scheme).
- The complete CPP set with numeric values (all limits `(b) (4)` in the posted documents).
- Table 6-4 historical process-time ranges (values `(b) (4)`).
- Deviation/OOS investigation records and the CPV protocol content (existence and scope are described; contents are not in the public record).
- Mycoplasma test validation protocol content (document number VP300808.DRAFT00 only).
- Media-hold integrity study data (USMB.098.TD / USMB.115.TD / USMB.372.VD / USMB.362.VD / USMB.363.VD — study numbers only).
- ODAC deck (Jul 12 2017) lot-release-data charts (deck slides 22–24): values not in the public text layer; transcribed 2026-09-16 via vision bridge (retained renders: `.private/verify/fda_bla125646_full_package/figures/odac_slide22.png`, `.private/verify/fda_bla125646_full_package/figures/odac_slide23.png`, `.private/verify/fda_bla125646_full_package/figures/odac_slide24.png` under `data/references/`), i.e., available as transcriptions rather than native text.

## Citation resolution: "Mol Ther 2015;23:718"

The task-referenced citation "Rager Mol Ther 2015;23:718" was resolved against PubMed E-utilities, checked 2026-09-17. A targeted esearch query `("Mol Ther"[Journal] AND 2015[dp] AND (717[Page] OR 718[Page]))` (field translated to Pagination) returned exactly one hit, PMID 25597412; the record was verified by efetch. The paper spanning journal page 718 is: **Fujita Y, Yagishita S, Hagiwara K, Yoshioka Y, Kosaka N, Takeshita F, Fujiwara T, Tsuta K, Nokihara H, Tamura T, Asamura H, Kawaishi M, Kuwano K, Ochiya T. "The clinical relevance of the miR-197/CKS1B/STAT3-mediated PD-L1 network in chemoresistant non-small-cell lung cancer." Mol Ther. 2015 Apr;23(4):717–727. Epub 2015 Jan 19. PMID 25597412, PMCID PMC4395779, DOI 10.1038/mt.2015.10** ([PubMed record 25597412](https://pubmed.ncbi.nlm.nih.gov/25597412/)). Abstract-level facts (from the PubMed record): study of a miR-197/CKS1B/STAT3-mediated network driving PD-L1 expression in chemoresistant non-small-cell lung cancer; miR-197 is downregulated in platinum-resistant NSCLC and its expression is inversely correlated with PD-L1 expression (n = 177; P = 0.026). This is an NSCLC immunology/gene-regulation paper — not a CAR-T or manufacturing source — and no author "Rager" appears. (The research agent's broader enumeration of Mol Ther 2015 vol 23, pp. 700–799, via `find_molther_718.ps1`, places the adjacent record 23(4):707–16, Koganti et al., PMID 25648265, immediately before it.) Conclusion: the "Rager Mol Ther 2015;23:718" attribution does not resolve to a CAR-T manufacturing citation; if this journal volume/page was intended, it resolves to the Fujita et al. paper above.

## Relationship to the simulator

The following were the illustrative assumptions in
[`manufacturing.py`](../simulator/cart_sim/manufacturing.py) when this audit began.
The comparisons are code-review inferences from the sources above; they are not
additional clinical specifications.

| Model assumption | Source-backed correction to its interpretation |
| --- | --- |
| A universal 85% viability release cutoff | Neither the published US commercial boundary nor the academic CTL019 boundary; select a named source profile. |
| CAR-positive fraction accepted from 10% to 95% | Not supported by the academic panel, which gives a 2% lower boundary and no corresponding 95% upper boundary. Commercial limits need separate evidence. |
| Vector-copy default 20 and accepted interval 1-60 | Incompatible with the academic DNA measurement interval if both use copies/cell; the model cannot present this as a sourced release interval. |
| `dose_target` caps total cells before multiplying by `te` | Not the published commercial dosing denominator. A commercial comparison must use the CAR-positive viable count and the appropriate indication/weight interval. |
| `net_yield=0.05` and fixed concentration arithmetic | Locally selected simplifications, not recovered manufacturing performance or process controls. |
| `release_ok` from viability, CAR fraction and vector copy number alone | Incomplete even for the academic panel; unmeasured required attributes must stay unknown, not silently pass. |

For software, a defensible implementation separates generated illustrative values
from externally measured lot attributes, stores source/profile identifiers with
each threshold, and returns an incomplete assessment when an applicable assay
result or specification is unavailable. Matching published numeric boundaries
checks the supplied data against that publication; it does not release a real
product or demonstrate manufacturing equivalence.

## Implemented correspondence

`lot_criteria.py` now implements `us_commercial_2020` for the Pasquini viability
and indication/weight-specific dose subset, plus every unredacted qualitative
requirement of the 2017 SBRA lot-release table (identity CAR qPCR "Positive" —
derived by `manufacture()` from TE > 0; appearance "Colorless to slightly
yellow", sterility "Negative", mycoplasma "Negative" — supplied as
`appearance_ok`/`sterility`/`mycoplasma` booleans, unknown by default;
`run_cohort()` assumes all three pass for its illustrative default lots,
overridable through `lot_params`), and `academic_ctl019_2022` for the
Bai panel. These are distinct source profiles. Rossoff's individual OOS reasons
and the Japanese criteria remain documented evidence rather than being merged
into a synthetic universal release panel. Missing measurements remain unknown;
`meets_disclosed_criteria` means only that supplied values meet that profile.
Every assessment explicitly leaves commercial release unestablished.

`manufacture()` now defines `net_yield` as recovered total T cells per starting
T cell before viability. It applies viability once and caps **viable CAR-positive
cells**, not total cells. Its counts are arithmetic outputs, not measured batches.
`vcn` defaults to `None`; the 20-copy default and 1-60 gate were removed. The
`release_ok` key was replaced by structured `source_assessment`; callers must not
interpret that object as a boolean release decision. `dose_CARplus_cells` remains
an alias of `dose_viable_car_cells`. These corrected semantics change old runs.

`run_cohort()` no longer multiplies dose by latent fitness, imposes a minimum
five-million-cell floor, penalizes partial specification failures, or links the
hypothetical vector-titer calculation to a transduction penalty. Fitness still
affects assumed proliferation and memory formation. All simulated patients remain
in the cohort denominator, including zero-dose scenarios; this does not model a
clinical decision to administer a lot. See the [kinetics rationale](KINETICS_SOURCES.md).

Default dose targets remain explicit scenarios: 200 million viable CAR-positive
cells for DLBCL; 1 million/kg for B-ALL at at most 50 kg, otherwise 100 million.
The default B-ALL weight is 30 kg, configurable through `weight_kg` or the report
CLI's `--all-weight-kg`. Neither these choices nor the TE/yield distributions are
estimates of a commercial population. `lot_params` can override the manufacturing
scenario; `dose_scale` is a subsequent model ablation, separate from lot assessment.

## Verification and unresolved items

The Pasquini full text and both patent descriptions were read directly. Bai's
complete relevant methods page was checked in a downloaded copy of the primary
article PDF; its numbers and inequality signs were visually verified. PMC's
direct Bai/Rossoff views intermittently returned a browser check; the former was
cross-checked against the PDF, and the latter against indexed article text.
The Kato full-text endpoint returned HTTP 403; its Table 3 discussion was available
through the publisher's indexed text. It was not used to reconstruct other assays.

An investigator-attributed educational slide reproduces candidate commercial
CAR-expression and IFN-gamma thresholds, but the corresponding primary abstract's
table was not accessible for independent verification. Those numbers have not
been promoted to authoritative commercial criteria. This is a retrieval gap,
not a claim that the values cannot be found.

Still absent from the inspected records are a complete, version-matched set of
commercial release boundaries and validated methods, the master production
record, all critical process ranges, and evidence that separately disclosed
patent constructs/processes match that commercial version. Published specifications
above narrow these gaps substantially without erasing the remaining distinctions.
