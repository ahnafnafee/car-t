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
process version, not just a numeric threshold. [Eldjerou et al., Leukapheresis and
Tisagenlecleucel Manufacturing Outcomes in Patients Age <3 Years, discussion of
final-product attributes](https://www.astctjournal.org/article/S2666-6367%2823%2901355-6/fulltext)

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
and indication/weight-specific dose subset, and `academic_ctl019_2022` for the
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
