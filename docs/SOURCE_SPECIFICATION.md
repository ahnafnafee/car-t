# Commercial product correspondence

The target is tisagenlecleucel (Kymriah), a patient-specific cell product. An exact
match to a disclosed CAR coding sequence is a bounded sequence result; it does
not establish identity of the complete vector, manufacturing process, or released
cell product. The distinction matters because the FDA description includes the
patient's modified T cells, possible additional cell populations, formulation,
manufacturing operations, and product testing. [FDA prescribing information,
revised June 2025, section 11](https://www.fda.gov/media/107296/download?attachment=)

Sources were checked on 2026-09-16. Historical approval documents describe the
versions they assessed; they cannot by themselves establish the specifications of
every subsequent manufacturing version.

The follow-up paper and patent search recovered a complete 9,174-nt historical
transfer-vector record containing the exact CAR CDS, published commercial US
viability and dose criteria, and a separately identified academic CTL019 release
panel. The earlier gap is therefore narrower than a blanket absence of sequence
or release information. See the [vector records](VECTOR_SOURCES.md) and
[manufacturing sources](PROCESS_SOURCES.md) for accession versions, comparisons
and source-specific limits.

## Evidence coverage

| Layer | What can be supported | What remains unestablished |
| --- | --- | --- |
| CAR protein and coding sequence | A residue-by-residue or nucleotide-by-nucleotide comparison with an identified patent sequence listing; see [the sequence evidence](EVIDENCE.md). | Independent authentication of the sequence against the manufacturer's controlled commercial vector record and relevant version. |
| Receptor architecture | CD19-binding scFv, CD8 hinge/transmembrane region, 4-1BB and CD3-zeta signaling domains. | Architecture alone cannot authenticate the complete DNA construct. [FDA label, section 11](https://www.fda.gov/media/107296/download?attachment=) |
| Vector sequence | GenBank JC053548.1 supplies the complete 9,174-nt historical patent transfer vector, including the exact CAR CDS; regulators separately describe the integrated-vector architecture. | Identity to a specified commercial transfer-plasmid version and the corresponding integrated sequence remains unverified. [Sequence comparison](VECTOR_SOURCES.md), [EMA reviewers, Figure 2](https://academic.oup.com/oncolo/article/25/2/e321/6443357) |
| Vector and cell manufacturing | Regulatory summaries identify unit operations and acknowledge validated process controls. | Those summaries do not establish a complete set of operating ranges, decision rules and production records. [FDA approval review, printed pp. 8–9](https://www.fda.gov/media/107962/download) |
| Lot release | Papers disclose commercial US viability/dose boundaries and a more detailed, separately scoped academic CTL019 panel. | The FDA table redacts most limits; the retrieved papers still do not establish a complete version-matched commercial panel and its validated methods. [Paper-derived criteria](PROCESS_SOURCES.md), [FDA approval review, printed pp. 9–10](https://www.fda.gov/media/107962/download) |
| Comparability | The manufacturer describes analytical equivalence assessment during process transfer, including growth, potency, viability and residual removal. | A sequence test or simulated batch cannot replace the experimental comparability data. [Tyagarajan et al., 2020, Figure 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC6970133/) |

## Complete vector sequence

The EMA assessment identifies a transfer plasmid and three packaging plasmids and
states that detailed genetic-element documentation was supplied in the regulatory
dossier. Its Figure 2 labels the CTL019 segment as 1,460 nt. That figure does not
resolve the boundaries of the 1,458-nt patent coding sequence used here, so the
lengths must not be reconciled by adding guessed bases. Neither this schematic nor
the patent CDS constitutes an authenticated full commercial transfer-plasmid or
integrated-vector sequence. [EMA public assessment report, printed
p. 18](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)

The recovered GenBank patent record now provides an actual historical transfer
vector rather than a reconstructed generic backbone. Its exact CAR match and
the extra trailing base in the separately listed CAR entry are tested in
`constructs.vector_reference`. This resolves historical source-record recovery,
while commercial-version identity still requires an evidenced link to the
applicable controlled construct and its integrated sequence.

## Process and product identity

The FDA review describes qualified materials, in-process monitoring, lot release,
traceability and process validation. It redacts parts of vector manufacture and
the expansion duration as well as release limits. These are direct evidence of
missing specification content, rather than missing software functions. [FDA
approval review, printed pp. 8–10](https://www.fda.gov/media/107962/download)

The EMA assessment likewise discusses critical process parameters, proven
acceptable ranges, normal operating ranges, process verification and site
comparability, without publishing a complete executable specification. Its
statement that regulators received sufficient detail does not mean that the same
detail appears in the assessment report. [EMA assessment, printed pp.
23–26](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)

The manufacturer's account describes changes to automation, analytical methods,
vector production and starting-material handling during technology transfer.
Consequently, a claim of process identity must identify the manufacturing version
and site being compared. This version requirement is an inference from the
documented changes. [Tyagarajan et al., 2020, “Transfer of Tisagenlecleucel
Manufacturing”](https://pmc.ncbi.nlm.nih.gov/articles/PMC6970133/)

## Completion criteria

Commercial equivalence remains unverified until the following evidence is
available for one defined product/process version. The recovered historical
vector and published subsets are progress toward these criteria, not absent data:

1. Authenticated complete vector sequences and controlled annotations.
2. The applicable master manufacturing records, material specifications, process
   limits, in-process decision rules and change history.
3. Validated analytical methods, their numerical acceptance criteria and the
   associated reference materials or controls.
4. Experimental batch records, assay results and a justified comparability study
   against the reference product.

These are evidence requirements inferred from the gaps above, not claims that
the repository possesses such records. Missing specifications must stay
explicitly unknown. Illustrative yield, vector-copy, potency or release values
must not become commercial specifications merely because a simulation returns
them, and a simulated release result cannot authenticate an actual cell lot.

The FDA PDFs and the EMA reviewers' journal article were accessible directly.
Direct retrieval of the EMA assessment PDF returned a rate-limit response, and
PMC's article view returned a browser check; the cited assessment passages and
manufacturer article sections were available through indexed source excerpts.
Those access limits are retained here rather than implying an exhaustive review
of every supplement or confidential submission.
