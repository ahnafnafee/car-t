<div align="center"><a name="readme-top"></a>

# CAR-T

### From reference sequence to simulated response.

An evidence-traceable CAR-T (tisagenlecleucel) research simulator in pure Python.

Sequence checks. Lot arithmetic. Population dynamics. Cohort experiments.<br/>
Every claim carries a citation; every retained source file carries a SHA-256.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](#-quick-start)
[![Runtime dependencies](https://img.shields.io/badge/runtime_dependencies-zero-14B8A6?style=flat-square)](#-quick-start)
[![Tests](https://img.shields.io/badge/tests-35%20passing-22C55E?style=flat-square)](#%EF%B8%8F-development)
[![Provenance](https://img.shields.io/badge/provenance-per--claim%20citations-8B5CF6?style=flat-square)](docs/EVIDENCE.md)
[![Status](https://img.shields.io/badge/status-research_model-F59E0B?style=flat-square)](docs/SOURCE_SPECIFICATION.md)

**[Quick start](#-quick-start)** · **[Features](#-features)** · **[Evidence](docs/EVIDENCE.md)** · **[Development](#%EF%B8%8F-development)**

<sup>Research model — sequence matches are exact; commercial product equivalence is not claimed.</sup>

</div>

---

<details>
<summary><kbd>Table of contents</kbd></summary>

#### TOC

- [👋🏻 What this is](#-what-this-is)
- [✨ Features](#-features)
- [🚀 Quick start](#-quick-start)
- [🔬 Explore the models](#-explore-the-models)
- [🧾 Evidence you can inspect](#-evidence-you-can-inspect)
- [📦 Project layout](#-project-layout)
- [⌨️ Development](#%EF%B8%8F-development)

####

<br/>

</details>

## 👋🏻 What this is

CAR-T connects a traceable receptor sequence with models of cell-lot arithmetic,
CAR-T expansion, tumor burden and cytokine dynamics. Use it to inspect assumptions,
compare mechanisms and reproduce numerical experiments.

The project keeps two kinds of statements strictly apart. **Exact matches** — the
protein against a PDF-reviewed patent transcription, the scFv against a PDB entry,
reference segments against UniProt — are computed and re-checked by tests.
**Simulated behavior** — expansion curves, cohort outcomes, assay proxies — is
exploratory modeling with every parameter labeled as assumption or source-backed.
Nothing silently crosses from one category to the other.

> \[!IMPORTANT]
>
> A sequence match does not establish identity of the commercial vector,
> manufacturing process, or released cell product. See the
> [commercial specification map](docs/SOURCE_SPECIFICATION.md) for what public
> records do and do not support.

## ✨ Features

### 🧬 Sequence verification

Exact patent CDS and protein references, a separate synonymous CDS, domain checks
and source comparisons. The verifier re-hashes its own reference files on every run.

### 🧮 Lot criteria, never release

Published US-commercial and academic CTL019 profiles stay separate source profiles.
Missing assays remain unknown, and matching a disclosed subset never authorizes
product release — the assessment object says so explicitly.

### 📈 Patient dynamics

An eight-state ODE model and a hybrid stochastic population model share one set of
endpoint definitions, so engine comparisons are meaningful.

### 👥 Cohort experiments

Seeded patient variation, parameter ablations and explicit endpoint summaries —
every simulated patient stays in the denominator.

### 🎯 Cell interactions

A 2D agent-based assay with movement, contact, synapses and serial killing, plus a
cross-validation exercise against the ODE rates.

### 📄 Readable results

Markdown reports and SVG plots using only the Python standard library.

## 🚀 Quick start

Requires Python 3.10 or newer, no third-party packages. Run from the repository root:

```bash
python -m unittest discover -s tests -v
python -m constructs.verify_sources
python -m constructs.vector_reference
python constructs/build_car.py
python simulator/run_sim.py --n 200 --seed 1001
python simulator/abm_assay.py --crossval
```

The construct builder writes FASTA files and a
[sequence report](constructs/car_report.md) under `constructs/`. Simulation reports
and plots are written to `simulator/out/`; choose another output directory with
`--outdir`. Fixed seeds reproduce results within the same Python runtime and
configuration.

<details>
<summary><kbd>Try a smaller run</kbd></summary>

```bash
python simulator/run_sim.py --n 10
python simulator/abm_assay.py --tumor 40 --hours 1
python simulator/diagnostics/compare_engines.py --seeds 5
```

Small cohorts are useful for checking the workflow; their percentages are noisy.

</details>

## 🔬 Explore the models

The ODE follows effectors, memory cells, antigen-positive and antigen-negative
tumor, normal B cells and three cytokines. The micro engine adds fitness bins and
antigen-dim clones, with a deterministic population correction alongside sampled
events.

```python
from simulator.cart_sim import run_patient

result = run_patient({"sigma": 0.0}, seed=7)
print(result["E_peak_day"])
print(result["T_d90"])
```

Lot comparisons use separate published profiles. Cohort dose is viable CAR-positive
cells, with viability applied once; yield and composition distributions remain
scenario assumptions. The commercial profile enforces every public requirement of
the 2017 FDA lot-release table — viability, dose intervals, and the four unredacted
qualitative rows (identity by CAR qPCR, appearance, sterility, mycoplasma); every
`(b)(4)`-redacted limit stays unknown.

```python
from simulator.cart_sim import assess_lot

assessment = assess_lot({
    "viability": 0.82,
    "dose_viable_car_cells": 2e8,
    "identity_car_pcr_positive": True,
    "appearance_ok": True,
    "sterility_negative": True,
    "mycoplasma_negative": True,
})
print(assessment["status"])  # meets_disclosed_criteria, not a release decision
```

Use `--all-weight-kg` to set the B-ALL report scenario (default 30 kg).
[Kinetics references](docs/KINETICS_SOURCES.md) retain their blood-assay units and
response groups; they are not automatic validation targets for the cell model.

## 🧾 Evidence you can inspect

The protein matches the PDF-reviewed transcription of US11535869B2 Table F,
SEQ ID 1132. Its 242-aa scFv matches PDB 7URV entity 2, and its human-derived
segments are checked against UniProt records. `car_patent_cds.fasta` preserves the
1,458-nt patent CDS unchanged; `car_orf.fasta` is a separate synonymous encoding
with an added stop codon. The retained CD3ζ sequence contains three paired ITAM
motifs.

| Evidence record | Scope |
| --- | --- |
| [Sequence evidence](docs/EVIDENCE.md) | Source-to-code mapping for every comparison |
| [Vector sources](docs/VECTOR_SOURCES.md) | Historical patent transfer vector, element map, WPRE provenance |
| [Manufacturing sources](docs/PROCESS_SOURCES.md) | Process parameters, operating ranges, decision rules, version history |
| [Release sources](docs/RELEASE_SOURCES.md) | Numerical acceptance criteria with verbatim `(b)(4)` redactions |
| [Why not 1:1](docs/ONE_TO_ONE.md) | Layer-by-layer ledger: exact matches, deliberate approximations, and what no code can close |
| [Reference manifest](data/references/README.md) | 110 hashed source files behind every citation |

Clinical trial observations are recorded with their own product, denominator and
endpoint. They are contextual references: model range agreement does not establish
clinical validation, commercial product equivalence or patent clearance.

To regenerate only the exact patent reference files:

```bash
python constructs/build_car.py --reference-only
```

## 📦 Project layout

```text
constructs/             Reference sequence, builder and source verifier
data/references/        Source excerpts and retrieval manifest
docs/                   Evidence and model assumptions
simulator/
  cart_sim/             ODE, micro engine, outcomes and cohort sampling
  diagnostics/          Matched engine comparison
  abm_assay.py          Agent-based assay
  benchmarks.py         Trial observations and assumed model ranges
  run_sim.py            Cohort report driver
  plotsvg.py            SVG renderer
tests/                  Regression and provenance checks
```

## ⌨️ Development

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

> \[!NOTE]
>
> Keep changes reproducible, add regression checks for behavior changes, and
> update the evidence map whenever a claim or source comparison changes.
> Reference files are committed byte-exact against
> [`promoted_manifest.json`](data/references/promoted_manifest.json); re-hash
> before editing anything under `data/references/`.

No software license has been selected for this repository.

<p align="right"><a href="#readme-top">🔝 back to top</a></p>
