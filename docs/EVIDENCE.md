# Evidence and implementation

The sequence comparisons are reproducible from the source excerpts in
[`data/references`](../data/references). Simulation parameters are a separate layer:
neither a matching protein sequence nor a patent description establishes the
numerical rates used by the models. Run `python -m constructs.verify_sources` to
repeat the sequence checks and `python -m unittest discover -s tests -v` to test
the software invariants.

## Sequence correspondence

| Source | Code or artifact | Comparison and limit |
| --- | --- | --- |
| [US11535869B2, Table F, SEQ ID 1132](https://patents.google.com/patent/US11535869B2/en) | `constructs/build_car.py`: `KYMRIAH_486_AA` | Exact 486-aa match to the PDF-reviewed Table F transcription. The source labels this sequence tisagenlecleucel; this is not independent verification of a commercial lot. |
| Same patent, SEQ ID 1131 | `car_patent_cds.fasta`, `translate()` | Exact 1,458-nt match to the retained source CDS, without an added stop codon. It translates to the same protein. The separate synonymous `car_orf.fasta` has 380 nucleotide substitutions and an added terminal TAA. |
| [PDB 7URV, entity 2](https://www.rcsb.org/structure/7URV) | `VL + LINKER + VH` | Exact 242-aa match to CAR residues 22–263. This structure covers the scFv, not the full receptor. |
| [UniProt P01732 / CD8A](https://www.uniprot.org/uniprotkb/P01732/entry) | `LEADER`, `HINGE`, `TM` | Leader segment matches residues 1–21; hinge plus TM is a contiguous reference segment. The assembler's boundaries are sequence partitions, not experimentally determined cleavage or topology boundaries. |
| [UniProt Q07011 / CD137](https://www.uniprot.org/uniprotkb/Q07011/entry) | `F1BB` | Exact match to residues 214–255, 42 aa. |
| [UniProt P20963 / CD247](https://www.uniprot.org/uniprotkb/P20963/entry) | `CD3Z`, `itam_motifs()` | Matches canonical residues 52–164 after Q65K and deletion of Q101. Three paired YxxL/I motifs remain; two isolated motif fragments were previously miscounted as two ITAMs. |

RCSB and UniProt FASTA records were retrieved on 2026-09-16. The patent table
excerpt was recovered from an existing cached transcription and visually compared
with the freshly downloaded original PDF on that date: PDF pages 70-71, printed
columns 99-102. The retained page images support review of the transcription;
this was a manual comparison, not automated PDF extraction or laboratory
authentication. The verifier reads sequence cells from the retained table excerpt
and removes only line-wrap hyphens; it does not reconstruct its expected answer
from the assembler.
File hashes and retrieval details are recorded in [the source manifest](../data/references/README.md).

The strings previously called CDR3s include flanking residues. They are sequence
contexts rather than formal IMGT or Kabat boundary annotations. The synonymous
encoding routine enforces translation, configured recognition-site exclusions and
homopolymer checks; it does not demonstrate expression optimization. The sequence
CAR builder outputs contain no promoter, WPRE, LTR or packaging signal. A separate
retained GenBank record now supplies the historical patent transfer vector;
it is not synthesized by the CAR builder. Its CAR sequence matches exactly, as
documented in the [vector comparison](VECTOR_SOURCES.md).

Run `python constructs/build_car.py --reference-only` to regenerate only the exact
patent CDS and protein FASTAs. Commercial sequence and process coverage, including
the specifications still needed, is recorded in the
[source specification](SOURCE_SPECIFICATION.md).

## Patent references

| Reference | Relevant subject | Relationship to this code |
| --- | --- | --- |
| [US8399645B2](https://patents.google.com/patent/US8399645B2/en) | Chimeric receptors with a 4-1BB signaling domain; inventors Dario Campana and Chihaya Imai | Architecture context; the sequence comparison uses Q07011. The prior attribution to Grupp was incorrect. |
| [US9328156B2](https://patents.google.com/patent/US9328156B2/en) | Use of CAR-modified T cells to treat cancer | Architecture and treatment context, not a source of the simulation's rate constants. |
| [US9464140B2](https://patents.google.com/patent/US9464140B2/en) | Compositions and methods for treatment of cancer | Related CAR context; no claim-by-claim implementation or freedom-to-operate conclusion is made. |
| [US6136597A](https://patents.google.com/patent/US6136597A/en) | RNA export element | WPRE background only. WPRE is not present in the generated CAR CDS. |

Patent sequence disclosure, claim coverage and present enforceability are separate
questions. The code makes no expiration-based permission or licensing claim.

## Clinical observations and model endpoints

The observations in `simulator/benchmarks.py:TRIALS` retain the original product,
population and denominator. The ranges in `BANDS` are author-selected exploratory
ranges, not published confidence intervals or matched validation targets.

| Source observation | Implemented comparison | Why it is not 1:1 |
| --- | --- | --- |
| [JULIET: best overall response 52%, complete response 40%, N=93](https://doi.org/10.1056/NEJMoa1804980) | DLBCL response/deep-response proxies | The model uses cell-burden thresholds at day 90, not clinical best-response assessment. |
| [ELIANA: remission within 3 months, CR + CRi 81%, N=75](https://doi.org/10.1056/NEJMoa1709866) | B-ALL response proxy | The model has no blood-count recovery endpoint and cannot distinguish CR from CRi. |
| [ZUMA-1: objective response 82%, complete response 54%, N=101](https://doi.org/10.1056/NEJMoa1707447) | Context only | This is axicabtagene ciloleucel, a different product. Its results do not validate a tisagenlecleucel reference model. |
| [ASTCT consensus grading](https://doi.org/10.1016/j.bbmt.2018.12.758) | `toxicity.py` synthetic CRS/ICANS categories | Clinical grading uses fever, hypotension, hypoxia and neurologic assessment. IL-6 thresholds and a CRS-conditioned random draw do not implement those criteria. |

The earlier benchmark list conflated any neurologic event with ICANS grade ≥2,
compared responder-conditioned six-month B-cell aplasia with an all-patient day-90
metric, and mixed products and grading systems. Those claims have been removed.
Relapse, persistence, cytokine thresholds, antigen densities and manufacturing
distributions in the simulator are not source-derived. Published manufacturing
criteria recovered subsequently are recorded separately in the
[process-source comparison](PROCESS_SOURCES.md), with commercial and academic
profiles kept distinct from illustrative yield and composition defaults. The
source-scoped lot comparisons now implement disclosed criteria; no complete
commercial release decision is implemented. VCN is unknown unless supplied.

The [cellular-kinetics review](KINETICS_SOURCES.md) adds primary blood-assay peak
times, fitted transgene parameters and persistence observations. Reports show
these with their units and response groups rather than converting qPCR copies
or flow fractions into unobserved whole-population cell counts. The prior fixed
out-of-specification dose penalty and titer/transduction penalty had no sourced
coefficient and have been removed; this does not imply biological equivalence
of all lots.

`outcomes.py` defines the shared endpoints: response requires a tumor minimum below
10% of baseline by day 90 and a day-90 burden below 20%; deep response additionally
requires day-90 burden below 0.05%. Relapse requires response followed by day-120
burden above both three times the tumor minimum through day 120 (floored at 10,000
cells) and 100 million cells. Persistence uses a day-120 memory-cell threshold of
18 million, while B-cell aplasia uses day-90 B cells below 10 million. These are
model definitions. Cohort rates use all simulated patients as the denominator.
Short trajectories return `None` for unobserved endpoints; cohort runs require at
least 120 days. Intermediate observation days are linearly interpolated.

## Model correspondence and limits

`ode_engine.py` integrates eight compartments with RK4. `micro_engine.py` uses
fitness bins, approximate Poisson event counts and three tumor clones, followed
by a deterministic rescale of the non-memory population toward a midpoint growth
estimate. It is therefore a hybrid population model, not a fully independent
cell-by-cell realization of the ODE. Resting, activated and exhausted labels
share aggregate proliferation and killing rates; functional exhaustion is not
implemented, and fixed fitness bins are not derived from a sampled lot's VCN.

Both engines use the same outcome code and the same meaning of `Ton`: antigen-
positive tumor. In the micro engine `Ton = T_hi + T_dim`; in both engines
`T = Ton + Toff`. Transfers are bounded by the source pool, killing vanishes at
zero target count, and cytokine clearance includes a well-defined zero-clearance
limit. The ODE's fixed killing term remains discontinuous at zero burden and can
require smaller steps near depletion. ODE `sigma` perturbs RK4 derivative calls;
it is a numerical noise device, not a timestep-invariant stochastic differential
equation. The micro engine has its own event noise and does not use `sigma`.

The ABM uses the same engagement function and assumed contact, movement and dwell
rules. Its rate ratio to the ODE is a comparison between two assumed models,
not a measured tissue-availability factor or independent experimental validation.
Generated reports calculate their summaries from the current run and make no
hard-coded claims of universal range agreement or exact engine equivalence.

The repository has no patient-level fitting, holdout dataset, formal parameter
identifiability analysis or experimental validation. These limits cannot be
resolved by forcing the code to match citation percentages.
