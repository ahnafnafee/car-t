# Release specifications for tisagenlecleucel (Kymriah) and its lentiviral vector: numerical acceptance criteria with provenance

Release-specification source record. Companion files:
[`promoted_manifest.json`](../data/references/promoted_manifest.json) and
[data/references/README.md](../data/references/README.md) (per-file SHA-256,
URLs, retrieval dates) and the source files themselves under
`data/references/`. Sources retrieved 2026-09-16/17.

## Scope and method

This record extracts the **numerical acceptance criteria** (release
specifications) for two components:

1. the final tisagenlecleucel (Kymriah) autologous T cell product, and
2. the self-inactivating (SIN) anti-CD19 lentiviral vector component used to
   manufacture it.

Sources are the FDA review package for BLA 125646 (Kymriah), the EMA public
assessment report and SmPC, the PMDA review report, and academic literature
(ELIANA-era CTL019, commercial real-world manufacturing analyses, and patent
examples). Every value is tied to a version:

- **(i) Commercial US product** — the BLA 125646 label product, B-ALL
  (approved Aug 30, 2017), DLBCL (sNDA approved May 1, 2018), and later FL.
  Values here come from the 2017 SBRA lot-release table, the CMC Review of
  Aug 29, 2017 (Amendment #46 specifications), the 2018 sNDA SBRA, the current
  US PI, and peer-reviewed manufacturing analyses (Pasquini 2020, Rossoff
  2021, Fong 2023).
- **(ii) Academic CTL019** — the Penn/CHOP investigational product of the
  NCT01626495 era, as documented by Bai et al. 2022 citing Maude et al. 2014
  (NEJM).
- **(iii) Japanese / other-market** — the PMDA review report (Feb 20, 2019)
  and the Japanese OOS trial (Kato et al. 2025, NCT04094311).
- **(iv) Patent and example processes** — US 2015/0093822 A1,
  WO 2012/079000 A1, US 2022/0168389 A1. These describe experimental or
  historical processes and must not be read as the commercial process.

**Redaction discipline.** FDA documents redact applicant-confidential
commercial information as `(b)(4)` (printed "(b) (4)" in the documents; normalized to
`(b)(4)` here); the PMDA report uses `****`/`**********`.
Redacted values are quoted verbatim with their printed page and table cell and
are **never filled in by guesswork**. Where a peer-reviewed source later
discloses the same number, the disclosure is recorded as an independent
criterion with its own scope (e.g., the 80% commercial viability boundary from
Pasquini 2020 is a published statement about US commercial products with a
January 23, 2020 data freeze; it is not the unredacted SBRA value).

The task label "BLA 761095" refers to the same document as the FDA
SBRA-quality review at `fda.gov/media/107962/download`; the actual BLA number
for Kymriah is **125646** (STN 125646/0 initial B-ALL; /76 DLBCL sNDA).

## Commercial US product: published release criteria

### Lot-release table, 2017 SBRA (BLA 125646/0, approved Aug 30, 2017)

The SBRA-quality review's lot-release table (printed pages 9–10; table
"Requirements for Commercial Use") is the short regulatory form of the release
specification. Values exactly as printed, `(b)(4)` verbatim:

| Test | Requirement for commercial use (as printed) | Sample used for testing |
| --- | --- | --- |
| Appearance | Colorless to slightly yellow | Formulated product (b)(4) |
| Identity by CAR q-PCR | Positive for PCR signal | (b)(4) |
| Percentage of viable T cells | (b)(4) | Final product (b)(4) |
| Determination of transduction efficiency by CAR-q-PCR | (b)(4) | (b)(4) |
| Cell viability | (b)(4) | Final product (b)(4) |
| Determination of residual beads by microscopy | (b)(4) | (b)(4) |
| Percentage of viable CD19+ B cells | (b)(4) | Final product (b)(4) |
| Total cell count (footnote 4) | Report cells/mL | Final product (b)(4) |
| Number of viable cells (calculated) | (b)(4) total viable cells | Final product (after thaw), footnote 2 |
| Dose (calculated) | 0.2 to 5.0 × 10⁶ CAR-positive viable T cells/kg body weight (≤50 kg); 0.1 to 2.5 × 10⁸ CAR-positive viable T cells (>50 kg) | Calculation: (%CAR expression × Viable cell concentration × Volume per dose)/100, divided by body weight in kg for patients ≤50 kg |
| Determination of CAR expression by flow cytometry | (b)(4) | Final product (b)(4) |
| Release of IFNγ in response to CD19-expressing target cells | • (b)(4)<br>• (b)(4) | Final product (b)(4) |
| Bacterial Endotoxins | (b)(4) | Final product (b)(4) |
| Sterility | Negative | Formulated product (b)(4) |
| Mycoplasma | Negative | (b)(4) |
| Determination of VSV-G DNA by quantitative PCR (qPCR) | (b)(4) | (b)(4) |

Footnotes as printed: (1) post-harvest samples are collected prior to addition
of cryopreservation medium to avoid interference from (b)(4) in the final
formulation; (2) the post-thaw sample is an aliquot of the final formulation
collected just prior to bag filling, stored in the vapor phase of liquid
nitrogen (≤ −120°C) and thawed at the time of analysis; (3) residual-bead
testing uses a pre-dose-formulation sample so beads are measured per (b)(4)
without effect from the final cells/mL formulation range; (4) **no
specification is set for total cell count** because it is not a critical
quality attribute — the result is used only to calculate the viable cell
number for dose; (5) the mycoplasma pre-harvest sample is culture
supernatant at the end of culture.

Unredacted values in this table: appearance "Colorless to slightly yellow";
CAR q-PCR identity "Positive for PCR signal"; total cell count "Report
cells/mL"; the B-ALL-only dose intervals above; sterility and mycoplasma
"Negative". The CMC Review (Aug 29, 2017), Table 37 "Revised Analytical
Methods and Specifications for Release", gives the same 16-test set with
per-test methods and rationale, and records that the original lot release
specifications "have been updated based on the discussion between the FDA and
the applicant and documented in amendment #46 of the BLA": the applicant
"agreed to the FDA recommendation for narrowing the specifications for
percentage of viable T cells from (b)(4) and for lowering the upper limit for
CAR transgene (b)(4) (CMC-OTAT IR 21 July 2017)", while "the acceptance
criteria for release of IFN-γ in response to CD19-expressing target cells to
the value proposed during the BLA filing of (b)(4) IFN-γ/transduced cell
remains unchanged at (b)(4) /transduced cell". Table 37's appearance is
"Colorless to slightly yellow" and its identity test is "Positive" on a
post-harvest sample. The stated basis for the revised specifications is "the
process capability, the results from release and stability testing of
clinical batches during development, corresponding clinical data, and
statistical evaluation", across (b)(4) batches manufactured under study
CCTL019B2202. [FDA, CMC Review Aug 29, 2017, BLA 125646/0,
§3.2.P.5.1/5.6 and Table 37](https://www.fda.gov/media/107978/download);
[FDA, SBRA-quality review BLA 125646/0, printed pp. 9–10
(table "Requirements for Commercial Use")](https://www.fda.gov/media/107962/download)

### Numerical criteria established by peer-reviewed sources (commercial US)

| Attribute | Published criterion | Scope/version | Source |
| --- | --- | --- | --- |
| Cell viability | At least 80% ("the release specification is ≥80% in the United States") | US commercial product, data freeze Jan 23, 2020 | [Pasquini et al., Blood Advances 2020, doi:10.1182/bloodadvances.2020003092, Methods, "Patients and study design"](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/) |
| B-ALL dose, weight ≤ 50 kg | 0.2 × 10⁶ to 5.0 × 10⁶ CAR+ viable T cells/kg | US commercial, B-ALL | [Pasquini et al., Blood Advances 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/); matches SBRA 2017 dose row and current PI |
| B-ALL dose, weight > 50 kg | 0.1 × 10⁸ to 2.5 × 10⁸ CAR+ viable T cells | US commercial, B-ALL | [Pasquini et al., Blood Advances 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/); matches SBRA 2017 and current PI |
| NHL dose | 0.6 × 10⁸ to 6.0 × 10⁸ CAR+ viable T cells | US commercial, NHL (DLBCL; FL added later) | [Pasquini et al., Blood Advances 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/); current US PI; EMA assessment report |
| Out-of-specification definition | "A batch was considered OOS if any of these release parameters did not meet the specifications" (viability, cell dose, CAR expression, IFN-γ release assay for potency, routine microbiologic clearance) | US commercial, OOS batch analysis | [Pasquini et al., Blood Advances 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/) |
| Residual beads | > 50 beads per 3 × 10⁶ cells counted as an OOS reason (n = 1 of 24 OOS batches) | US commercial, PRWCC/alternative-access cohort | [Rossoff et al., Blood 2021, doi:10.1182/blood.2021012392, Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/) |
| Leukapheresis input | Total nucleated cells < 2 × 10⁹ in the leukapheresis product counted as OOS (n = 3) | US commercial | [Rossoff et al., Blood 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/) |
| Leukapheresis age | Collection > 9 months prior to manufacturing counted as OOS (n = 1) | US commercial | [Rossoff et al., Blood 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/) |
| Potency | Failed IFN-γ release assay counted as OOS (n = 2); no numeric cutoff in the paper | US commercial | [Rossoff et al., Blood 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/) |

Rossoff et al. state that "strict specifications were set for
tisagenlecleucel to be eligible for commercial release" and explicitly
contrast the commercial 80% viability boundary with the initial trial's 70%
boundary; receiving an OOS product under alternative access (MAP n = 14,
single-patient IND n = 10, of 24 OOS products) is not evidence that the
commercial specification disappeared. The full OOS sentence: "Reasons for
products being OOS included cell viability < 80% (n = 17), total nucleated
cell count <2 × 10⁹ in leukapheresis product (n = 3), failed interferon-γ
release assay (n = 2), leukapheresis product collected >9 months prior (n =
1), and determination of residual beads >50 beads per 3 × 10⁶ cells (n = 1)."

The 2018 DLBCL sNDA SBRA states, under CBER Lot Release: "Not applicable. No
changes in lot release criteria were requested to this supplement." The sNDA
changed the dose range only (DLBCL 0.6–6.0 × 10⁸, per the current PI and EMA
report), not the lot-release panel. [FDA, SBRA BLA 125646/76 (Apr 13, 2018
document), CBER Lot Release section](https://www.fda.gov/media/113215/download)

## Final product attributes (commercial)

| Attribute | Value (as stated) | Version/scope | Source |
| --- | --- | --- | --- |
| Formulation | "31.25% (v/v) of Plasma-Lyte A, 31.25% (v/v) of 5% Dextrose/0.45% sodium chloride, 10% Dextran 40 (LMD)/5% Dextrose, 20% (v/v) of 25% Human Serum Albumin (HSA), and 7.5% (v/v) Cryoserv® dimethyl sulfoxide (DMSO)" | Current US PI | [US PI, §11 DESCRIPTION](https://www.fda.gov/media/107296/download) |
| Appearance | "colorless to slightly yellow suspension of cells" (thawed); pharmaceutical form "Dispersion for infusion — A colourless to slightly yellow dispersion" | Current US PI; EMA SmPC | [US PI, §11](https://www.fda.gov/media/107296/download); [EMA SmPC, §3/§4](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) |
| pH | **Not stated** in the US PI, EMA SmPC, PMDA report, SBRA, or CMC Review (broad grep for pH/hydrogen ion returns no numeric statement) | Absent, not redacted | Verified absent across all inspected records |
| Osmolality | **Not stated** in any inspected record | Absent, not redacted | Verified absent across all inspected records |
| Potassium | "This medicinal product contains potassium, less than 1 mmol (39 mg) per dose, i.e. essentially 'potassium-free'." | EMA SmPC | [EMA SmPC, "Sodium and potassium content"](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) |
| Sodium | 24.3 to 121.5 mg per dose (1 to 6% of the WHO 2 g/day adult maximum) | EMA SmPC | [EMA SmPC, "Sodium and potassium content"](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) |
| Excipients (EMA) | glucose, sodium chloride, human albumin solution, dextran 40 for injection, dimethyl sulfoxide, sodium gluconate, sodium acetate, potassium chloride, magnesium chloride, sodium-N-acetyltryptophanate, sodium caprylate, aluminium, water for injections | EMA SmPC | [EMA SmPC, excipients](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) |
| Bag volume | 10 mL to 50 mL ("The volume in the infusion bag ranges from 10 mL to 50 mL"; SmPC "10 mL - 50 mL per bag"; PMDA bag sizes redacted `**mL`) | Current US PI; EMA SmPC | [US PI, §2.3/§16](https://www.fda.gov/media/107296/download); [EMA SmPC §4](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) |
| Storage | "Store infusion bag(s) in a temperature-monitored system less than or equal to minus 120°C, e.g., in the vapor phase of liquid nitrogen"; PMDA: 9-month shelf life at ≤ −120°C in a gamma-irradiated sterile EVA bag | Current US PI; PMDA | [US PI, §16](https://www.fda.gov/media/107296/download); [PMDA review report, Stability (printed p. 21)](https://www.pmda.go.jp/files/000252613.pdf) |
| Shipping | "shipped directly to the cell lab associated with the infusion center in a liquid nitrogen Dewar" | Current US PI | [US PI, §16 HOW SUPPLIED](https://www.fda.gov/media/107296/download) |
| Thaw | "Thaw each infusion bag one at a time at 37°C using either a water bath or dry thaw method until there is no visible ice in the infusion bag" | Current US PI | [US PI, §2.3](https://www.fda.gov/media/107296/download) |
| In-use stability after thaw | "Once the infusion bag has been thawed and is at room temperature (20°C to 25°C), it should be infused within 30 minutes." PMDA: "Administration should begin immediately after thawing and be completed within 30 minutes at room temperature." | Current US PI; PMDA | [US PI, §2.3](https://www.fda.gov/media/107296/download); [PMDA review report, Stability](https://www.pmda.go.jp/files/000252613.pdf) |
| Infusion rate | "Administer KYMRIAH as an intravenous infusion at 10 mL to 20 mL per minute"; "Do NOT use a leukocyte-depleting filter" | Current US PI | [US PI, §2.3](https://www.fda.gov/media/107296/download) |
| Sterility gate for shipping | "The product must pass a sterility test before release for shipping as a frozen suspension in a patient-specific infusion bag(s)." | Current US PI | [US PI, §11](https://www.fda.gov/media/107296/download) |
| NDCs | Ped ALL: 0078-0846-19; DLBCL and FL: 0078-0958-19 | Current US PI (FL version) | [US PI, §16](https://www.fda.gov/media/107296/download) |
| Manufacturing failure rate | "up to 9% of manufacturing attempts" (current PI); B2202: "In the clinical study protocol B2202, 7 of the 78 lots manufactured failed due to either termination of manufacturing or out-of-specification results (an approximately 9% failure rate)" | Current US PI §17; SBRA 2017 | [US PI, §17](https://www.fda.gov/media/107296/download); [FDA SBRA-quality review BLA 125646/0](https://www.fda.gov/media/107962/download) |

The cached US PI is the **current** label (includes the FL indication and
NDC 0078-0958-19), not the 2017 label; version is noted wherever it is cited.
The EMA assessment report gives the ELIANA (B2202) dose structure verbatim
(printed p. 64): target dose "2.0 to 5.0×10⁶ tisagenlecleucel cells (i.e.
CAR-positive viable T-cells) per kg body weight (for patients ≤ 50 kg) or of
1.0 to 2.5×10⁸ tisagenlecleucel cells (for patients >50 kg)"; allowed "if all
other safety release criteria were met": "0.2 to 5.0×10⁶ CAR-positive viable
T-cells per kg body weight" (≤50 kg) and "0.1 to 2.5×10⁸ CAR-positive viable
T-cells" (>50 kg); and "Products falling below the minimum values in the
above allowable cell dose ranges (i.e. 0.2×10⁶ CAR-positive viable T-cells
per kg or 1.0×10⁸ CAR-positive viable T-cells) were not released for
infusion." The stated not-released floor of 1.0×10⁸ for patients >50 kg is
internally inconsistent with the same passage's allowed band starting at
0.1×10⁸; both figures are quoted as printed, not reconciled. The adult DLBCL
study CCTL019C2201 (JULIET) targeted 5.0 × 10⁸ viable tisagenlecleucel
transduced cells with an acceptable range of 1.0–5.0 × 10⁸; prior to protocol
amendment 4, doses of 0.5–1.0 × 10⁸ were rounded to 1 × 10⁸ cells and infused;
with amendment 4, doses below 1.0 × 10⁸ cells were no longer released for
infusion ("ZUMA" appears nowhere in the EPAR — the DLBCL study is JULIET). [EMA assessment
report, dosage and trial sections (printed pp. 64, 81–82)](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)

## Academic CTL019 release panel

Bai et al. (Science Advances 2022) document the release panel for the academic
CTL019 product (Penn/CHOP pilot studies NCT01626495 and NCT02906371).
**Materials and Methods: T cell isolation, vector production, and generation
of CTL019 cells**, printed page 12: "The final product release criteria are
listed as follows (6): cell viability ≥ 70%, CD3+ cells ≥ 80%, residual
paramagnetic anti-CD3/CD28–coated paramagnetic beads ≤ 100 per 3 × 10⁶
cells, endotoxin ≤ 3.5 EU/ml, mycoplasma negative, bacterial and fungal
cultures negative, residual bovine serum albumin ≤ 1 μg/ml, vesicular
stomatitis virus-G (VSV-G) DNA as a surrogate marker for replication-competent
lentivirus ≤ 50 copies per microgram of DNA, transduction efficiency by flow
cytometry ≥ 2%, and transduction efficiency by vector DNA sequence = 0.02 to
4 copies per cell." Reference (6) is Maude et al. 2014, NEJM
371:1507–1517. [Bai et al., Science Advances 2022,
doi:10.1126/sciadv.abj2820, Methods p. 12](https://pmc.ncbi.nlm.nih.gov/articles/PMC9177075/)

| Measured attribute | Reported boundary |
| --- | --- |
| Cell viability | ≥ 70% |
| CD3+ cells | ≥ 80% |
| Residual anti-CD3/CD28-coated beads | ≤ 100 per 3 × 10⁶ cells |
| Endotoxin | ≤ 3.5 EU/mL |
| Mycoplasma; bacterial and fungal cultures | Negative |
| Residual BSA | ≤ 1 μg/mL |
| VSV-G DNA (RCL surrogate) | ≤ 50 copies/μg DNA |
| Transduction efficiency by flow cytometry | ≥ 2% |
| Transduction efficiency by vector DNA sequence | 0.02 to 4 copies/cell |

The methods give the surrounding process: autologous PBMC leukapheresis, T
cell enrichment by elutriation, activation with anti-CD3/CD28–coated
paramagnetic beads, SIN-lentiviral transduction during activation with a
**day-3 vector washout**, 8–12-day WAVE (rocking platform) expansion, magnetic
bead removal, and cryopreservation in infusible medium.

Two caveats on provenance. First, the Maude 2014 NEJM **main body contains no
release-criteria list** (targeted searches for the panel terms return no
matches in the PMC full text); the panel is documented secondhand in Bai 2022
citing Maude 2014, most plausibly from the NEJM supplementary appendix, which
was not retrieved. Second, this is an academic profile: the 70% viability
boundary and the ≤ 100 beads/3 × 10⁶ boundary differ from the commercial US
80% boundary and the > 50 beads/3 × 10⁶ OOS trigger, and must not be merged.
[Rossoff et al., Blood 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/)
is the independent source that contrasts the two viability boundaries.

## Vector component release criteria

### Vector system and manufacture

The CTL019 vector is a SIN (self-inactivating), EF1α-promoted, WPRE-containing
lentivirus carrying the murine anti-CD19 (FMC63) scFv CAR; VSV-G
pseudotyped. The FDA briefing document states that the vector's quality
attributes (titer, potency, purity) "to a large extent determine the potency
of the CAR T cell product" and that each vector lot is tested for potency
"using a biologically relevant assay". [FDA ODAC briefing document, BLA
125646, vector quality attributes section](https://www.fda.gov/media/106081/download)

The EMA assessment report (printed pp. 17–18) names the four plasmids:
pRKHVmuEC19 (the transfer plasmid containing the CTL019 vector genome),
pRKHSYNGP (HIV-1 Gag/Pol packaging), pRKHG (envelope packaging, VSV-G), and
pRKHREV (Rev packaging); "The CTL019 vector is manufactured under contract by
Oxford BioMedica, Oxford, UK (OXB)". [EMA assessment report, §vector
(genetic structure), printed pp. 17–18](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)
The PMDA report (sections 2.1.1–2.1.3, printed p. 10) describes the same
4-plasmid system (Gag/Pol, Env/VSV-G, Rev, αCD19CAR) produced from Stbl3
bacterial plasmid cell banks and 293T producer cell banks (ATCC SD-3515),
with ICH Q5A(R1), Q5B, and Q5D testing; plasmid control items are redacted.
Commercial supply came from the Fraunhofer IZI site in Leipzig (cells), with
batch certification by Novartis Pharma GmbH, Nuremberg; the US site was
Morris Plains, NJ. [PMDA review report, §2.1](https://www.pmda.go.jp/files/000252613.pdf);
[EMA assessment report, manufacturing sites (printed p. 22)](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)

### Vector release and specification statements

| Attribute | Value (as stated) | Scope/version | Source |
| --- | --- | --- | --- |
| Vector batch release test | "Biological activity of the vector is controlled for batch release by measuring the transduction efficiency corresponding to a measurement of the infectivity of the vector. The result is expressed in transducing [units]" plus per-batch transgene expression | EMA, clinical vector (Oxford BioMedica) | [EMA assessment report, printed p. 18](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf) |
| Vector substance shelf life | "12 months at -60°C to -90°C" requested; "The proposed shelf-life for the vector substance is acceptable." | EMA | [EMA assessment report, Stability (viral vector), printed p. 20](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf) |
| Vector product shelf life | "A shelf-life of 36 months at -60°C to -90°C is requested for the vector product … the proposed shelf-life for the vector product is acceptable." | EMA | [EMA assessment report, printed p. 21](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf) |
| Vector product characterization (development) | vector concentration, vector particles (copy number), titer, particle-to-infectivity ratio, MOI, total residual DNA, host cell DNA, plasmid DNA, host cell protein, residual BSA, mycoplasma, in vitro virus, bovine virus, RCL, bioburden, bacterial endotoxin | PMDA development stage | [PMDA review report, §2.1, Table 6](https://www.pmda.go.jp/files/000252613.pdf) |
| Vector specification list (preclinical) | copy number, description, identification, purity (Impurity B, Impurity A, host cell DNA, plasmid DNA), bacterial endotoxin, sterility, mycoplasma, viral testing, RCL (infectivity assay), viral titer, particle-to-infectivity ratio | PMDA §2.1.8 | [PMDA review report, §2.1.8](https://www.pmda.go.jp/files/000252613.pdf) |
| Adventitious agent tests as vector specifications | "The tests shown in Table 3 (except bioburden) are also used as specifications for the viral vector [see Section 2.R.1]" (in vitro virus testing in Vero/MRC-5/HEK293; bovine virus CPE/HAD-BT and Vero IFB for BAV/BPV/BRSV/BTV/BVDV/Reo3/Rabies; mycoplasma; RCL) | PMDA, unpurified bulk harvest / end of process | [PMDA review report, §2.1, Table 3 and note](https://www.pmda.go.jp/files/000252613.pdf) |
| Vector stability (Japan) | 8 vector batches stored at -90 to -60°C (long-term), accelerated at -20°C, plus stress studies; "shelf life of *** months is proposed for the viral vector when stored at … in a glass vial sealed with a bromobutyl rubber stopper at ***°C" (values redacted) | PMDA | [PMDA review report, §3.1 Stability of viral vector (printed p. 20)](https://www.pmda.go.jp/files/000252613.pdf) |
| Residual vector in product | Post-manufacture and final-supernatant amounts "below the detection limit (qPCR, ** copies/µg DNA)" (limit redacted) | PMDA | [PMDA review report, §2.2.6.2](https://www.pmda.go.jp/files/000252613.pdf) |
| RCL (product level) | "To date, no RCL has been detected in any clinical batch" using "a sensitive co-culture RCL assay or … PCR-based RCL assay" (SBRA); CMC Review: "Detection of VSV-G DNA is used as marker for RCL, therefore the acceptance criterion is no detection of RCL. The limit is based on the LOQ of the qPCR assay and remains unchanged from the Penn limit. RCL testing using amplification in indicator cells is performed as part of the LV vector release testing." | FDA BLA 125646/0 | [FDA SBRA-quality review BLA 125646/0](https://www.fda.gov/media/107962/download); [FDA CMC Review Aug 29, 2017](https://www.fda.gov/media/107978/download) |
| Vector substance/product acceptance criteria | FDA CMC Review TOC: "Table 7 Acceptance criteria for CTL019 (murine) HIV-1 Vector Substance … 31; Table 8 Acceptance criteria for CTL019 (murine) HIV-1 Vector Product … 31"; the CMC Review also contains "Table 25 Vector Product (b)(4) Acceptance Criteria" (values redacted). The bodies of Tables 7/8 were not fully extracted from the cached text. | FDA BLA 125646/0, printed p. 31 | [FDA CMC Review Aug 29, 2017, TOC and Table 25](https://www.fda.gov/media/107978/download) |

The Tyagarajan et al. 2020 manufacturing paper (the "Reiter manufacturing
paper" in the task list; actually Tyagarajan S, Spencer T, Smith J, Mol Ther
Methods Clin Dev 2020;16:136–144) gives the CQA framework for the product:
appearance; safety (endotoxins, sterility, mycoplasma, VSV-G DNA); purity
(viable T cell percentage, transduction efficiency, viability); impurities
(residual beads, CD19+ B cells); identity (CAR qPCR); quantity (cell count,
viable cells, dose); and potency (CAR expression, IFN-γ release). Median
manufacturing cycle: 23 days (range 21–37). [Tyagarajan et al., Mol Ther
Methods Clin Dev 2020, doi:10.1016/j.omtm.2019.11.018](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6970133/fullTextXML)

## Potency assay

**Identity of the potency test.** The commercial lot-release potency test is
IFN-γ production upon stimulation by CD19-expressing target cells:

- SBRA 2017 lot-release table row: "IFNγ release upon response to
  CD19-expressing target cells", requirement "(b)(4)".
- ODAC introductory remarks (July 12, 2017, CBER): under Potency, "Lot
  release: IFN-γ production upon stimulation by CD19+ cells"; "Additional
  characterization: killing of CD19+ cells."
- ODAC briefing document, §4.1.4.1: "Potency of tisagenlecleucel is measured
  by evaluating IFN-γ production in response to tumor antigen-bearing cells.
  IFN-γ production is considered an indicator of T cell activation and a
  prerequisite for CAR T cell activity. However, in the clinical trials,
  IFN-γ production varied greatly from lot-to-lot (Figure 4), making it
  difficult to correlate IFN-γ production in vitro to tisagenlecleucel
  safety or efficacy."
- CMC Review (Amendment #46): the IFN-γ acceptance criterion "remains
  unchanged at (b)(4) /transduced cell".

The quantity is expressed **per transduced cell** (briefing document
Figure 4 caption: "IFN-γ production per transduced cell. IFN-γ produced
during co-culture with CD19-expressing cells is quantified as a measure of
potency for tisagenlecleucel. (FDA generated)"). [FDA, SBRA-quality review
BLA 125646/0](https://www.fda.gov/media/107962/download); [FDA ODAC
introductory remarks, slides on potency](https://www.fda.gov/media/106489/download);
[FDA ODAC briefing document, §4.1.4.1 and Figures 4–5](https://www.fda.gov/media/106081/download)

**The numeric cutoff is not published.** The SBRA and CMC Review leave the
IFN-γ acceptance value redacted (`(b)(4)`). The ODAC deck's potency slides
show upper/lower limit bands for IFN-γ per CAR+ T cell, %CAR+ T cells, and
VCN per CAR+ T cell (y-axis 0–3.0) **without numeric tick labels**, and state
the release specifications were "based on statistical analysis of historical
data". The educational-slide candidate thresholds (an investigator-attributed
slide reproducing commercial IFN-γ and CAR-expression thresholds) remain
unverified against a primary source; the corresponding primary abstract table
was not accessible. This is a retrieval gap, not a claim that the values
cannot be found. [docs/PROCESS_SOURCES.md, "Verification and unresolved
items"](PROCESS_SOURCES.md)

**Published potency-related ranges (non-cutoff evidence).**

- Bachanova et al. (ASH 2019 abstract #626, JULIET trial, r/r DLBCL):
  "in vitro functional activity upon CD19-specific stimulation, as evidenced
  by IFNγ release, with a wide range among different batches (range,
  23.7–938 fg/CAR+ cell). Durable responses were observed across the entire
  range of IFNγ release; high IFNγ release was not associated with severe
  CRS or NE." [Bachanova et al., Blood 2019;134(Suppl 1):242,
  doi:10.1182/blood-2019-128302](https://ashpublications.org/blood/article/134/Supplement_1/242/426221/Impact-of-Tisagenlecleucel-Chimeric-Antigen)
- Rossoff et al. 2021: two of 24 OUS products "failed interferon-γ release
  assay" (no numeric cutoff in the paper). [Rossoff et al., Blood
  2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/)
- Kato et al. 2025 (Japan): "low IFN-γ release" appears among the OOS types
  in the trial's Table 3. [Kato et al., Cytotherapy 2025,
  doi:10.1016/j.jcyt.2025.04.067](https://www.sciencedirect.com/science/article/pii/S1465324925006851)
- EMA assessment report, potency section (printed p. 26): "Potency is
  measured as [word redacted/omitted in the cached text] to ensure
  appropriate CAR expression and cytokine secretion upon T cell
  activation. The proposed specifications are considered appropriate.
  However, the Applicant should re-evaluate the release tests and their
  acceptance criteria based on post approval data." [EMA assessment report,
  release testing (printed p. 26)](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)

## Redacted and absent values

Redactions are quoted verbatim. "Not stated" means the value is genuinely
absent from every inspected record (verified by grep), distinct from
"redacted".

| Attribute | Verbatim redaction / absence | Location | Best available alternative |
| --- | --- | --- | --- |
| Viable T cell percentage | "(b)(4)"; CMC: narrowed "from (b)(4)" | SBRA 2017, lot-release table, p. 9 | None published |
| Cell viability | "(b)(4)" | SBRA 2017, lot-release table, p. 9 | ≥ 80% for US commercial products (Pasquini 2020, data freeze Jan 2020); 70% academic (Bai 2022); 70% Japanese (Kato 2025) |
| Residual beads | "(b)(4)"; footnote: "No more than (b)(4)" | SBRA 2017, lot-release table p. 9 and process impurities section | > 50 beads per 3 × 10⁶ cells = OOS (Rossoff 2021); ≤ 100 per 3 × 10⁶ academic (Bai 2022) |
| Viable CD19+ B cells | "An acceptance criterion of (b)(4) B cells in KYMRIAH was [set]", LOQ "(b)(4)" | SBRA 2017, process impurities section | None published |
| Vector copy number | "the average vector copy number per cell is limited to less than (b)(4) per cell" | SBRA 2017, vector section | Academic DNA interval 0.02–4 copies/cell (Bai 2022) — different version |
| IFN-γ acceptance | "(b)(4)"; "remains unchanged at (b)(4) /transduced cell" | SBRA 2017, p. 10; CMC Review Table 37 | None published; batch range 23.7–938 fg/CAR+ cell observed in JULIET (Bachanova 2019) |
| CAR expression by flow | "(b)(4) • (b)(4)"; CMC: "lowering the upper limit for CAR transgene (b)(4)" | SBRA 2017, p. 10; CMC Review | None published |
| Viable cell number (dose calculation) | "(b)(4) total viable cells" | SBRA 2017, p. 10 | None published |
| B2202 batch count for spec justification | "(b)(4) batches were manufactured under study CCTL019B2202" | CMC Review | None published (7 of 78 lots failed, ~9%) |
| Potency assay definition wording | "Potency is measured as [redacted/omitted] to ensure appropriate CAR expression and cytokine secretion upon T cell activation." | EMA assessment report, printed p. 26 | Identity established elsewhere (IFN-γ release, SBRA/briefing doc) |
| US post-marketing spec for "**********" (deviation parameter; context: minimum values "***% for pediatric ALL and ***% for DLBCL") | "The approved specification for ********** in the US was tighter than that for the investigational product, and therefore the specification for ********** will be changed so that it becomes the same as that for the investigational product. Further, this specification is also used for products marketed in Japan." | PMDA review report, §2.R.2 (OOS discussion) | Context suggests a %CAR-positive-viable-T-cell / dose-specification parameter; parameter name not recoverable from the public text |
| Vector shelf life (Japan) | "a shelf life of *** months has been proposed for the viral vector when stored in a glass vial sealed with a bromobutyl rubber stopper at **********°C" | PMDA review report, §3.1 Stability of viral vector (printed p. 20) | EMA: 12 months (substance) / 36 months (product) at -60 to -90°C |
| Bag volume (Japan) | "up to ** mL or ** mL" | PMDA review report, product description | 10–50 mL (US PI, SmPC) |
| Residual vector limit | "below the detection limit (qPCR, ** copies/µg DNA)" | PMDA review report, §2.2.6.2 | None published |
| Plasmid control items | Redacted | PMDA review report, §2.1 | None published |
| Vector substance/product acceptance criteria (FDA) | Table 25 "Vector Product (b)(4) Acceptance Criteria" | CMC Review | Tables 7/8 exist (printed p. 31) but values not in the cached text |
| pH | Not stated | US PI, EMA SmPC, PMDA report, SBRA, CMC Review (grep-verified) | None — record as absent |
| Osmolality | Not stated | Same as pH | None — record as absent |
| Educational-slide IFN-γ / CAR thresholds | Primary source not accessible | See [docs/PROCESS_SOURCES.md](PROCESS_SOURCES.md), "Verification and unresolved items" | None promoted to a criterion |

## Version and market notes

**Commercial US versioning.**

1. **2017 (BLA 125646/0, B-ALL, approved Aug 30, 2017):** SBRA Table 1 / CMC
   Table 37 (Amendment #46, after the CMC-OTAT information request of
   July 21, 2017). Appearance criterion identical in both documents:
   "Colorless to slightly yellow" (SBRA Table 1 and CMC Table 37). Dose: B-ALL only (0.2–5.0 × 10⁶/kg ≤50 kg;
   0.1–2.5 × 10⁸ >50 kg).
2. **2018 (sNDA 125646/76, DLBCL, approved May 1, 2018):** "No changes in
   lot release criteria were requested to this supplement." Dose range
   expanded to DLBCL 0.6–6.0 × 10⁸. Regulatory history in the same SBRA:
   sBLA 125646/76 submitted Oct 30, 2017; PAS 125646/80 (changes in
   manufacture) pending Nov 21, 2017.
3. **Current label:** adds the FL indication (NDC 0078-0958-19; the 0846 NDC
   remains for Ped ALL), same dose structure (adult DLBCL/FL 0.6–6.0 × 10⁸),
   "colorless to slightly yellow", ≤ −120°C storage, 30-minute in-use window.

**Japan.** PMDA review report (Feb 20, 2019): 9-month product shelf life at
≤ −120°C in a gamma-irradiated sterile EVA bag; 30-minute room-temperature
administration window; the §2.R.2 statement that the US post-marketing
specification for the redacted parameter "was tighter than that for the
investigational product" and is now changed to match the investigational
product, with "this specification is also used for the product marketed in
Japan". Kato et al. 2025 (single-arm phase 3b, NCT04094311, 29 enrolled
Dec 2019–May 2022 at 13 Japanese sites, 28 infused): the **70% cell-viability
release criterion** is the Japanese boundary (OOS = "low cell viability below
the 70% release criterion", 15/24 DLBCL batches); approved cell range
0.6–6.0 × 10⁸ CAR+ viable T cells (low dose 8/23 DLBCL batches; high dose
4/5 B-ALL batches); median final dose 1.7 × 10⁸ (range 0.2–4.3 × 10⁸),
median viability 68.9%; OOS rate declined from 7.6% (2019) to 3.7% (2023).
The abstract reports 6 CR + 1 PR of 15 assessed; Table 4 of the same paper
shows CR 5/15 (40.0%) and ORR 6/15 (46.7%) — a minor internal discrepancy in
the paper; the abstract wording is quoted. [Kato et al., Cytotherapy 2025,
doi:10.1016/j.jcyt.2025.04.067](https://www.sciencedirect.com/science/article/pii/S1465324925006851)

**Academic CTL019.** 70% viability, ≤ 100 beads/3 × 10⁶, TE ≥ 2% (flow) and
0.02–4 copies/cell (vector DNA) — the Bai 2022 / Maude 2014 panel. Distinct
from all commercial versions; do not blend.

**Patent and example processes.** [US 2015/0093822 A1](https://patents.google.com/patent/US20150093822A1)
("Compositions for Treatment of Cancer", June et al., application
14/567,426) describes the early CART19 clinical process (apheresis,
elutriation, bead activation, lentiviral transduction, day-3 washout) with
documented release exceptions in its clinical examples.
[WO 2012/079000 A1](https://patents.google.com/patent/WO2012079000A1/en)
Table 4 covers three early CLL pilot patients with recorded release
exceptions. [US 2022/0168389 A1](https://patents.google.com/patent/US20220168389A1/en)
Example 1 describes rapid manufacture in quiescent T cells using the Penn
CTL019 receptor. None of these establishes the commercial process.

**Citation identity resolutions (for the task's named targets).**

- "Eldjerou 2023" (the 146-batch / manufacturing-outcomes paper) resolves to
  **Fong D, Tiwari R, Acker C, Clough L, Willert J. Transplant Cell Ther
  2023;29(9):579.e1–e10, doi:10.1016/j.jtct.2023.06.007** (PMID 37311511,
  "Leukapheresis and Tisagenlecleucel Manufacturing Outcomes in Patients Age
  <3 Years…"). Crossref confirms the author list contains no Eldjerou. Note:
  `docs/PROCESS_SOURCES.md` cites this title as "Eldjerou et al." — that
  attribution in the canonical doc appears to be an error; flagged here, not
  edited. The paper's key disclosure for this record: the viability
  analytical assay changed during 2019–2020, so final cell-count and
  viability values need an assay-and-process version, not just a threshold.
- "Junovk 2020 JCO" does not exist as named: 0 PubMed hits for author
  "Junovk" (any field), and neither of the two JCO 2020 tisagenlecleucel
  papers (Frey 2020;38(5):415–422; Whittington 2020;38(4):359–366) has a
  Junovk author. Closest match for "product attributes → clinical
  outcomes" is **Bachanova et al., ASH 2019 abstract #626 (Blood
  134 Suppl 1:242, doi:10.1182/blood-2019-128302)**; no JCO 2020 journal
  version by Bachanova on this topic exists (checked via PubMed).
- "Reiter manufacturing paper" = **Tyagarajan S, Spencer T, Smith J. Mol
  Ther Methods Clin Dev 2020;16:136–144 (PMID 31988978, PMC6970133)**.
- "Maude 2014 NEJM" (the 70% viability primary source per Bai 2022
  reference 6) = Maude SL, Frey N, Shaw PA, et al. N Engl J Med
  2014;371:1507–1517 (PMC4267531); the panel itself is not in the main body.
- BLA number: 125646 (the task's "BLA 761095" label is a misnomer for the
  same `media/107962` SBRA-quality review document).

**Manufacturing-cycle evidence.** Tyagarajan 2020: median 23 days (21–37).
The EMA reviewer article (Ali S, Kjekken R, Niederlander C, et al.,
Oncologist 2020;25(2):e321–e327, the published version of the CHMP review
team's assessment) notes "the median time from enrollment to infusion (54
days) was considerably longer than the prespecified manufacturing time of
4–5 weeks, which again is longer than what would be expected based on the
product's quality specification (approximately 3 weeks)", and that "Some
patients were given tisagenlecleucel even though the recommended dose of
viable CAR T cells was not met, because other effective treatment options
were not available." [Ali et al., Oncologist 2020,
doi:10.1093/oncolo/ozaa003](https://doi.org/10.1093/oncolo/ozaa003)

## Source list (retrieved 2026-09-16)

- FDA SBRA-quality review, BLA 125646/0 (B-ALL, Aug 30, 2017), lot-release
  table printed pp. 9–10 — `../data/references/fda_sbra_107962_bla125646_0_ball_2017-08-30.pdf` —
  <https://www.fda.gov/media/107962/download>
- FDA SBRA, BLA 125646/76 (DLBCL sNDA, Apr 13, 2018 document) —
  `../data/references/fda_sbra_113215_bla125646_76_dlbcl_2018-04-13.pdf` —
  <https://www.fda.gov/media/113215/download>
- FDA ODAC introductory remarks (July 12, 2017, CBER/OTAT) —
  `../data/references/fda_odac_presentation_2017-07-12.pdf` — <https://www.fda.gov/media/106489/download>
- FDA ODAC briefing document, BLA 125646 — `../data/references/fda_odac_briefing_document_125646.pdf`
  — <https://www.fda.gov/media/106081/download>
- FDA BLA 125646 review package (19 MB ZIP; CMC Review Aug 29, 2017 incl.
  Table 37; information requests; clinical/statistical reviews) —
  `../data/references/fda_media_107978_bla125646_approval_history.zip`; key
  members are also promoted individually under `fda_*` names
  — <https://www.fda.gov/media/107978/download>
- FDA approval letters and post-approval documents:
  `../data/references/fda_approval_letter_125646_0_2017-08-30.pdf` (initial BLA approval, Aug 30, 2017),
  `../data/references/fda_approval_letter_125646_76_2018-05-01.pdf` (sNDA approval, May 1, 2018),
  `../data/references/fda_letter_125646_429_2021-06-11.pdf` (June 11, 2021), `../data/references/fda_letter_125646_854_2024-04-12.pdf`
  (April 12, 2024), `../data/references/fda_letter_125646_860_2024-06-13.pdf` and
  `../data/references/fda_letter_125646_902_2024-08-16.pdf` (REMS amendments, 2024) —
  <https://www.fda.gov/media/{106989,112803,150087,178030,179659,181491}/download>
- Current US prescribing information (FL version) —
  `../data/references/fda_pi_kymriah_current.pdf` — <https://www.fda.gov/media/107296/download>
- EMA public assessment report, EMA/CHMP/443047/2018 (June 28, 2018) —
  `../data/references/ema_kymriah_epar_2018.pdf` —
  <https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf>
- EMA SmPC — `../data/references/ema_kymriah_smpc.pdf` —
  <https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf>
- PMDA review report (Kymriah, Novartis Pharma K.K., Feb 20, 2019) —
  `../data/references/pmda_kymriah_review_2019.pdf` —
  <https://www.pmda.go.jp/files/000252613.pdf>
- Pasquini MC, Hu ZH, et al. Blood Adv 2020;4(21):5414–5424 —
  `../data/references/pasquini_2020_rwe.txt` —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/>
- Rossoff J, Baggott C, Prabhu S, et al. Blood 2021;138(21):2138–2142 —
  `../data/references/rossoff_2021_out_of_spec.txt` —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/>
- Bai L, et al. Science Advances 2022 (single-cell landscape of the CAR-T
  infusion product; academic CTL019 release panel) —
  `../data/references/bai2022_ctl019_panel.txt` (local copy; primary PDF verified) —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC9177075/>
- Maude SL, et al. N Engl J Med 2014;371:1507–1517 —
  `../data/references/maude_2014_nejm_ctlo19.txt` —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC4267531/>
- Maude SL, et al. ELIANA (NEJM 2018) — `../data/references/maude_2018_eliana.txt` —
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/>
- Tyagarajan S, Spencer T, Smith J. Mol Ther Methods Clin Dev
  2020;16:136–144 (Europe PMC fullTextXML) —
  `../data/references/tyagarajan_2020_mtmcd.xml` —
  <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6970133/fullTextXML>
- Kato K, et al. Cytotherapy 2025 (Japanese OOS trial, open access) —
  `../data/references/kato_2025_cytotherapy_oos_japan.md` —
  <https://www.sciencedirect.com/science/article/pii/S1465324925006851>
- Bachanova V, et al. ASH 2019 abstract #626, Blood 134 Suppl 1:242 —
  `../data/references/bachanova_2019_ash_abstract_242.html` —
  <https://ashpublications.org/blood/article/134/Supplement_1/242/426221/Impact-of-Tisagenlecleucel-Chimeric-Antigen>
- Fong D, Tiwari R, Acker C, Clough L, Willert J. Transplant Cell Ther
  2023;29(9):579.e1–e10 (abstract/metadata) —
  `../data/references/fong_2023_tct_fulltext_oa.md` — <https://doi.org/10.1016/j.jtct.2023.06.007>
- Ali S, Kjekken R, Niederlander C, et al. Oncologist 2020;25(2):e321–e327 —
  `../data/references/kymriah_reviewer_article_oncologist_2020.txt` —
  <https://doi.org/10.1093/oncolo/ozaa003>
- US 2015/0093822 A1 (June et al., "Compositions for Treatment of Cancer") —
  `../data/references/us20150093822_patent_desc.txt` —
  <https://patents.google.com/patent/US20150093822A1>

## Verification notes (checked 2026-09-17)

Finalizer pass over the local corpus (no web fetches needed). Page
citations use the bottom-of-page footer convention: in the EPAR the footer
"EMA/CHMP/443047/2018 Page N" sits at the bottom of printed page N; in the
PMDA report the two-line footer block (page number + document title) sits at
the bottom of printed page N (confirmed from the end-of-file "ii"/"iii"
blocks, which split the abbreviations list mid-entry). Content after the
"Page N" footer and before the "Page N+1" footer is printed page N+1.

**Verified verbatim this pass (high-value claims).**

- CMC Review Table 37 (Amendment #46, printed p. 111–112): Appearance
  "Colorless to slightly yellow"; Identity "Positive" (post-harvest¹); total
  cell count "Report cells/mL"; Sterility and Mycoplasma "Negative";
  footnotes 1–5 as quoted in MAIN_SESSION_NOTES §2.1. IFN-γ acceptance
  "remains unchanged at (b)(4) /transduced cell"; CAR expression "lowering
  the upper limit for CAR transgene (b)(4)"; RCL limit "based on the LOQ of
  the qPCR assay and remains unchanged from the Penn limit".
- SBRA 2017 (media/107962), Manufacturing Risks: "In the clinical study
  protocol B2202, 7 of the 78 lots manufactured failed due to either
  termination of manufacturing or out-of-specification results (an
  approximately 9% failure rate)." (The draft previously paraphrased this
  inside quotation marks; corrected to verbatim.)
- SBRA 2018 sNDA (media/113215): "No changes in lot release criteria were
  requested to this supplement."
- Pasquini 2020 (PMC7656920): "the release specification is ≥80% in the
  United States"; doses "for ALL, 0.2 × 106 to 5.0 × 106 CAR+ viable T cells
  per kilogram of body weight, if weight ≤50 kg, and 0.1 × 108 to 2.5 × 108
  CAR+ viable T cells if weight >50 kg; for NHL, 0.6 × 108 to 6.0 × 108
  CAR+ viable T cells"; "A batch was considered OOS if any of these release
  parameters did not meet the specifications"; "Data analysis was based upon
  a data freeze on 23 January 2020" (the draft said "data cutoff"; corrected
  to the paper's wording "data freeze"); OOS product viability "ranged from
  61% to 79%".
- Rossoff 2021 (PMC8617436): OOS reasons incl. "cell viability < 80%
  (n = 17), total nucleated cell count <2 × 109 in leukapheresis product
  (n = 3), failed interferon-γ release assay (n = 2), … determination of
  residual beads >50 beads per 3 × 106 cells (n = 1)"; 24 (13%) of 185
  infused patients received OOS products.
- US PI (media/107296, FL version): "up to 9% of manufacturing attempts"
  (§17); formulation and storage statements as quoted; NDC 0078-0958-19
  (DLBCL/FL) and 0078-0846-19 (Ped ALL).
- EMA SmPC: "potassium, less than 1 mmol (39 mg) per dose, i.e. essentially
  'potassium-free'"; "24.3 to 121.5 mg sodium per dose"; "10 mL - 50 mL per
  bag".
- EPAR (EMA/CHMP/443047/2018), re-anchored page by page from the full
  196-footer map: four plasmids pRKHVmuEC19/pRKHSYNGP/pRKHG/pRKHREV +
  "manufactured under contract by Oxford BioMedica, Oxford, UK (OXB)"
  (pp. 17–18); batch-release TU/mL statement (p. 18); vector substance 12-mo
  shelf life "at -60°C to -90°C … acceptable" (p. 20); vector product
  36-mo shelf life (p. 21); manufacturing sites — Morris Plains (MP)
  facility, Fraunhofer FH IZI Leipzig, batch certification by Novartis
  Pharma GmbH Nürnberg (p. 22); potency statement "Potency is measured as
  [word omitted in cached text] to ensure appropriate CAR expression and
  cytokine secretion upon T cell activation" (p. 26); B2202 pALL dose
  passage — target 2.0–5.0 × 10⁶/kg (≤50 kg), 1.0–2.5 × 10⁸ (>50 kg),
  allowed 0.2 × 10⁶/kg and 0.1 × 10⁸, "Products falling below the minimum
  values in the above allowable cell dose ranges … were not released for
  infusion" (p. 64); C2201/JULIET target 5.0 × 10⁸, acceptable
  1.0–5.0 × 10⁸, pre-Amendment-4 rounding of 0.5–1.0 × 10⁸ to 1 × 10⁸
  (p. 81) and post-Amendment-4 "doses below 1.0×108 cells were no longer
  released for infusion" (p. 82); JULIET (C2201) mfg-time passage — median
  enrolment-to-infusion 54 days (range 30–357), screening-to-infusion 119
  days, actual mfg time median 30–34 days, commercial 24 days (target 22),
  C2201 dose range 1.0–5.0 × 10⁸, n=5 below / n=5 above target with similar
  responses (p. 120).
- ODAC deck (media/106489, July 12, 2017; printed slide numbers): slide 19
  lot-release tests (Potency: cytokine production; Dose: viable T cells
  expressing CAR), slide 20 potency = IFN-γ production upon stimulation by
  CD19+ cells, slide 21 specs "based on statistical analysis of historical
  data", slides 22–24 example lot-release data (IFN-γ, transduction
  efficiency, integrated vector) — as cited.
- PMDA report (000252613): §3.1 viral-vector stability — "Based on the
  above, a shelf life of *** months has been proposed for the viral vector
  when stored in a glass vial sealed with a bromobutyl rubber stopper at
  **********°C" (p. 20); §3.2 product — Table 13 incl. "9 months*3" rows,
  "Based on the above, a shelf life of 9 months has been proposed for the
  product when stored in a gamma-irradiated sterile EVA bag at ≤−120°C, and
  the administration should be started immediately after thawing and
  completed within 30 minutes at room temperature" (p. 21).
- Tyagarajan 2020 (PMC6970133): "median throughput time of 23 days (range,
  21–37 days)".
- Ali/Oncologist 2020 (Oncologist 2020;25(2):e321–e327): "the median time
  from enrollment to infusion (54 days) was considerably longer than the
  prespecified manufacturing time of 4–5 weeks, which again is longer than
  what would be expected based on the product's quality specification
  (approximately 3 weeks)"; "the recommended dose of viable CAR T cells was
  not met, because other effective treatment options were not available."
- Bachanova 2019 ASH abstract: IFNγ release range "23.7–938 fg/CAR+ cell".
- Bai 2022 (PMC9177075): academic panel "cell viability ≥ 70%, CD3+ cells
  ≥ 80%, residual paramagnetic anti-CD3/CD28–coated paramagnetic beads
  ≤ 100 per 3 × 106 cells, endotoxin ≤ 3.5 EU/ml, mycoplasma nega[ve]…".
- Kato 2025 (Cytotherapy, S1465324925006851): 29 enrolled / 28 infused
  (Dec 2019–May 2022, 13 sites); 70% viability release criterion (15/24
  DLBCL batches low viability; low dose 8/23; high dose 4/5 B-ALL); median
  dose 1.7 × 10⁸ (0.2–4.3 × 10⁸), median viability 68.9%; OOS rate 7.6%
  (2019) → 3.7% (2023); abstract 6 CR + 1 PR of 15 assessed; Table 4 CR
  5/15 (40.0%), ORR 6/15 (46.7%); CRS in 69.6% (n = 16).

**Corrections made in place (2026-09-17).**

1. L162 SBRA "7 of 78 lots" quote → verbatim (was a paraphrase inside
   quotation marks).
2. EMA citation "(printed pp. 63, 81)" → "(printed pp. 64, 81–82)" (B2202
   dose passage p. 64; JULIET/C2201 dose + Amendment-4 rounding p. 81;
   Amendment-4 no-release statement p. 82).
3. Plasmid/OXB citation "(printed p. 17)" → "(printed pp. 17–18)" (named
   plasmids and OXB statement are on p. 18; section starts p. 17).
4. Vector batch-release TU/mL citation "p. 17" → "p. 18".
5. Manufacturing-sites citation "p. 25" → "p. 22".
6. Vector substance 12-mo shelf-life citation "p. 19" → "p. 20".
7. Vector product 36-mo shelf-life citation "p. 20" → "p. 21".
8. EMA potency statement citations "p. 25" → "p. 26" (three places).
9. PMDA 9-month product shelf-life citation "p. 20" → "p. 21".
10. PMDA vector "*** months" row: section number §3.2 → §3.1 (page p. 20
    was already correct).
11. PMDA vector-shelf-life redaction → verbatim with full storage description
    ("glass vial sealed with a bromobutyl rubber stopper at **********°C")
    and §3.1/p. 20.
12. "data cutoff" → "data freeze" (three places) to match the paper's
    wording "data freeze on 23 January 2020".

**Identity determinations (checked 2026-09-17).**

- CMC copy identity: `../data/references/fda_cmc_review_125646_2017-08-29.pdf` is
  byte-identical (same SHA-256, 1,155,866 B) to the independently downloaded
  working copy of the same posting.
  The public posting is partial: printed pages posted are 1–12, 101–105,
  108–119, 122, 143–151, with four "(b)(4) pages not releasable"
  placeholders (87 pp. for 13–100, 2 pp. for 106–107, 2 pp. for 120–121,
  20 pp. for 123–142). Vector figure pages 13–14 are not posted; Table 37
  spans printed pp. 111–112 and is posted. No coverage expansion vs the
  working copy, so no paragraph was added for it.
- Briefing-doc identity: `../data/references/fda_odac_briefing_document_125646.pdf` header reads
  "FDA Briefing Document / Oncologic Drugs Advisory Committee Meeting / BLA
  125646 Tisagenlecleucel / Novartis Pharmaceuticals Corporation" — the ODAC
  background/briefing document for BLA 125646 (media/106081); the July 12
  2017 meeting date comes from the companion deck (media/106489), not from
  the document's own text.
- SmPC identity: `../data/references/ema_kymriah_smpc.pdf` is the ANNEX I SmPC, "Kymriah
  1.2 × 10⁶ – 6 × 10⁸ cells dispersion for infusion".
- Zip identity: `../data/references/fda_media_107978_bla125646_approval_history.zip`
  (19,350,296 B) matches the independently downloaded approval-history
  package; SHA-256
  261f22a71a682f08b193a81c4a080ba9d3591d3efd359e66d80a10925cf8322b.
- Media-letter identities (STN assignments per letter content): 106989 =
  STN 125646/0 (Aug 30, 2017); 112803 = STN 125646/76 (May 1, 2018); 150087
  = STN 125646/429 (Jun 11, 2021); 178030 = STN 125646/854 (Apr 12, 2024);
  179659 = STN 125646/860 (Jun 13, 2024); 181491 = STN 125646/902 (Aug 16,
  2024, REMS minor change).

**Remaining gaps and weak/unverified claims.**

- Numeric potency cutoff (IFN-γ acceptance value) remains unpublished:
  `(b)(4)` in SBRA/CMC; no primary numeric value in the local corpus.
- (b)(4) redactions quoted verbatim throughout; values not recoverable.
- pH and osmolality absent (not redacted) from US PI, SmPC, PMDA, SBRA, CMC
  — verified by grep; recorded as absent.
- EPAR vector Tables 7/8 "exist at printed p. 31" is supported only by the
  posted TOC entries; p. 31 itself lies in the omitted 13–100 range of the
  CMC posting, so table values are not in the local text.
- Maude 2014 .txt appears to be an incomplete extraction (no "viability"/
  "release criteria" matches); the 70% academic panel is documented
  secondhand via Bai 2022 (citing Maude 2014 ref 6, likely from the
  unretrieved supplementary appendix), as stated in the draft.
- Fong 2023 "viability analytical assay changed during 2019–2020": VERIFIED
  2026-09-17 against the publisher's open-access full text (CC BY-NC-ND,
  https://www.astctjournal.org/article/S2666-6367(23)01355-6/pdf): "It is
  important to note that following health authority approval, the viability
  analytical assay was improved between 2019 and 2020 to simplify sample
  preparation for final product cell count and viability measurement. This
  change in process resulted in cell count and viability measurements that
  were more reflective of final product at infusion in 2020 and 2021; as a
  result, the differences between years should be interpreted with caution"
  (printed p. 579.e5). The paper is Fong D, Tiwari R, Acker C, Clough L,
  Willert J. The same study's 2019 ASH abstract preceded it (Eldjerou LK,
  Acker C, Howick D, et al., Blood 134 Suppl 1:5066,
  doi:10.1182/blood-2019-127346), first author Eldjerou; the 2023
  full-article authorship is Fong et al., and docs/PROCESS_SOURCES.md cites
  it as such.
- WO 2012/079000 Table 4 and US 2022/0168389 Example 1 have no local copies;
  not re-verified this pass (URLs retained as cited).
- ODAC PNG files (`.private/verify/fda_bla125646_full_package/figures/odac_slide22.png`, `.private/verify/fda_bla125646_full_package/figures/odac_slide23.png`,
  `.private/verify/fda_bla125646_full_package/figures/odac_slide24.png`) are vision-bridge renders of the deck,
  not primary sources; cited only via the deck PDF.
