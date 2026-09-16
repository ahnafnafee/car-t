<div align="center">

# CAR-T

### From reference sequence to simulated response.

A dependency-free Python workspace for CD19 CAR sequence checks,<br/>
population dynamics, cohort exploration and agent-based assays.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#quick-start)
[![Runtime dependencies](https://img.shields.io/badge/runtime_dependencies-zero-14B8A6?style=flat-square)](#explore-the-models)
[![Status](https://img.shields.io/badge/status-research_model-8B5CF6?style=flat-square)](docs/EVIDENCE.md)

[Quick start](#quick-start) · [Models](#explore-the-models) · [Evidence](docs/EVIDENCE.md) · [Development](#development)

</div>

---

CAR-T connects a traceable receptor sequence with models of cell-lot arithmetic,
CAR-T expansion, tumor burden and cytokine dynamics. Use it to inspect assumptions,
compare mechanisms and reproduce numerical experiments. Sequence checks establish
specific matches to reference records; the simulations remain exploratory models.

## What you can explore

| Capability | What it produces |
| --- | --- |
| **Sequence verification** | Exact patent CDS and protein references, a separate synonymous CDS, domain checks and source comparisons |
| **Patient dynamics** | An eight-state ODE model and a hybrid stochastic population model |
| **Cohort experiments** | Seeded patient variation, parameter ablations and explicit endpoint summaries |
| **Cell interactions** | A 2D agent-based assay with movement, contact, synapses and serial killing |
| **Readable results** | Markdown reports and SVG plots, using only the Python standard library |

## Quick start

Requires Python 3.10 or newer. Run these commands from the repository root:

```bash
python -m unittest discover -s tests -v
python -m constructs.verify_sources
python -m constructs.vector_reference
python constructs/build_car.py
python simulator/run_sim.py --n 200 --seed 1001
python simulator/abm_assay.py --crossval
```

The construct builder writes FASTA files and a [sequence report](constructs/car_report.md)
under `constructs/`. Simulation reports and plots are written to `simulator/out/`.
Choose another output directory with `--outdir`. Fixed seeds reproduce results
within the same Python runtime and configuration.

<details>
<summary><strong>Try a smaller run</strong></summary>

```bash
python simulator/run_sim.py --n 10
python simulator/abm_assay.py --tumor 40 --hours 1
python simulator/diagnostics/compare_engines.py --seeds 5
```

Small cohorts are useful for checking the workflow; their percentages are noisy.

</details>

## Explore the models

The ODE follows effectors, memory cells, antigen-positive and antigen-negative
tumor, normal B cells and three cytokines. The micro engine adds fitness bins and
antigen-dim clones, with a deterministic population correction alongside sampled
events. Both engines share endpoint definitions.

```python
from simulator.cart_sim import run_patient

result = run_patient({"sigma": 0.0}, seed=7)
print(result["E_peak_day"])
print(result["T_d90"])
```

The ABM represents individual cells in a 2D field. Its `--crossval` option compares
assumed assay rates with ODE rates; it is a model consistency exercise. Cohort
ranges and synthetic toxicity categories remain assumptions, documented alongside
source-backed lot criteria in the [evidence map](docs/EVIDENCE.md).

Lot comparisons now use separate published US-commercial and academic CTL019
profiles. Missing assays remain unknown, and matching a disclosed subset never
authorizes product release. Cohort dose is viable CAR-positive cells, with viability
applied once; yield and composition distributions remain scenario assumptions.

```python
from simulator.cart_sim import assess_lot

assessment = assess_lot({"viability": 0.82, "dose_viable_car_cells": 2e8})
print(assessment["status"])  # meets_disclosed_criteria, not a release decision
```

Use `--all-weight-kg` to set the B-ALL report scenario (default 30 kg).
[Kinetics references](docs/KINETICS_SOURCES.md) retain their blood-assay units and
response groups; they are not automatic validation targets for the cell model.

## Evidence you can inspect

The protein matches the PDF-reviewed transcription of US11535869B2 Table F, SEQ ID 1132.
Its 242-aa scFv matches PDB 7URV entity 2, and its human-derived segments are checked
against UniProt records. `car_patent_cds.fasta` preserves the 1,458-nt patent CDS
unchanged; `car_orf.fasta` is a separate synonymous encoding with an added stop
codon. The retained CD3ζ sequence contains three paired ITAM motifs.

To regenerate only the exact patent reference files:

```bash
python constructs/build_car.py --reference-only
```

[Read the source-to-code mapping →](docs/EVIDENCE.md)

Clinical trial observations are recorded with their own product, denominator and
endpoint. They are contextual references: model range agreement does not establish
clinical validation, commercial product equivalence or patent clearance.
The [commercial specification map](docs/SOURCE_SPECIFICATION.md) distinguishes
disclosed product information from unavailable vector, manufacturing and release
specifications; this repository does not reproduce the full commercial process.
The recovered [historical patent vector](docs/VECTOR_SOURCES.md) contains the exact
CAR CDS. [Paper-derived manufacturing criteria](docs/PROCESS_SOURCES.md) record
published commercial and earlier clinical specifications separately.

## Project layout

```text
constructs/             Reference sequence, builder and source verifier
data/references/        Source excerpts and retrieval manifest
docs/                   Evidence and model assumptions
simulator/
  cart_sim/             ODE, micro engine, outcomes and cohort sampling
  diagnostics/          Matched engine comparison
  abm_assay.py           Agent-based assay
  benchmarks.py          Trial observations and assumed model ranges
  run_sim.py             Cohort report driver
  plotsvg.py             SVG renderer
tests/                   Regression and provenance checks
```

## Development

```bash
python -m unittest discover -s tests -v
python -m simulator.cart_sim
```

Optional editable install for `import cart_sim` outside the repository:

```bash
python -m pip install -e .
```

The source verifier and report commands use repository files and should be run
from a checkout. Formatting and lint checks use Ruff; it is not a runtime dependency.

```bash
uvx ruff check .
uvx ruff format --check .
```

Keep changes reproducible, add regression checks for behavior changes, and update
the evidence map whenever a claim or source comparison changes. No software
license has been selected for this repository.
