# Why the simulator is not a 1:1 reproduction of commercial tisagenlecleucel

This record answers one question directly: for each layer of the product, what
is 1:1 with the commercial version, what is deliberately approximate, and what
cannot be made 1:1 from public evidence at all. It consolidates what
[SOURCE_SPECIFICATION.md](SOURCE_SPECIFICATION.md) scopes, at the level of
individual simulator decisions. Sources were checked 2026-09-16/17/18; file
hashes are in [the reference manifest](../data/references/README.md).

## What was made 1:1 where the evidence allowed

Where a public record states a requirement exactly, the simulator enforces that
requirement exactly, not an approximation of it:

| Layer | 1:1 content | Enforced in |
| --- | --- | --- |
| CAR coding sequence | Exact base-for-base match of the 1,458-nt CDS to US11535869B2 SEQ 1131 at JC053548.1[6,391–7,848]; the historical 1,459-nt entry difference is tested, not hidden | `constructs/vector_reference.py` |
| Protein | Residue-by-residue match to the PDF-reviewed Table F transcription (SEQ 1132); scFv match to PDB 7URV entity 2 | `constructs/verify_sources.py` |
| Vector architecture | The complete 9,174-nt historical transfer vector retained as file bytes; element map and WPRE provenance reconciled to J04514.1 coordinates | `data/references/`, [VECTOR_SOURCES.md](VECTOR_SOURCES.md) |
| Dose intervals | The SBRA/PI intervals verbatim: B-ALL 0.2–5.0×10⁶/kg (≤50 kg), 0.1–2.5×10⁸ (>50 kg); NHL 0.6–6.0×10⁸ | `lot_criteria.dose_interval` |
| Commercial viability floor | ≥80% as published for the US commercial product (Pasquini 2020); academic 70% kept in a separate profile, never merged | `lot_criteria.py` profiles |
| Unredacted release requirements | All four public qualitative requirements of the 2017 SBRA lot-release table — identity by CAR qPCR "Positive", appearance "Colorless to slightly yellow", sterility "Negative", mycoplasma "Negative" — enforced as checks; identity derived from manufactured CAR fraction | `lot_criteria.assess_lot` |
| Total cell count | No specification, per the printed footnote: the table result is used only to compute the dose; the simulator never gates on it | `lot_criteria.py` |
| Academic panel | The Bai 2022 CTL019 boundaries verbatim (≥70%, ≥80% CD3+, ≤100 beads/3×10⁶, ≤3.5 EU/mL, ≤1 µg/mL BSA, ≤50 VSV-G copies/µg DNA, ≥2% TE, 0.02–4 copies/cell) | `lot_criteria.py` profile |
| Published product statistics | All six public per-patient statistics for commercial tisagenlecleucel — ELIANA infused dose (per kg and total), enrollment-to-infusion, Tmax, persistence duration, and the Tyagarajan 2020 manufacturing cycle time — transcribed verbatim with byte-exact quotes tested against the retained files, and exposed as an optional cohort dose distribution | `publication_stats.py`, `run_cohort(product_stats="eliana_2018")`, `tests/test_publication_stats.py` |
| Published per-patient lot attributes | 13 further published attributes (Fong 2023 commercial pediatric B-ALL dose/viability/CAR fraction/leukapheresis input/weight; Pasquini 2020 real-world viability by indication and accept-to-infuse interval; 2025 label JULIET/ELARA dose medians; US20050113564A1 academic transduction; the 23-patient Kato 2025 out-of-specification table drawn patient by patient), each quote-tested byte-exact, with borrowings and inversions reported as assumptions | `lot_distributions.py`, `run_cohort(lot_stats=...)`, `tests/test_lot_distributions.py` |
| Record version anchors | 11 byte-verified anchors naming the exact record version behind each published constant, each with the caveat that travels with it (including that the retained EU record is EMA/485563/2018 and contains neither a `B/2202` number nor an August-2018 date) | `version_anchor.py`, `run_sim.py` report, `tests/test_version_anchor.py` |
| Kinetic denominators | Published statistics are separated into time-denominated, cell-denominated and amplitude-denominated, and the amplitude bridge's three missing factors are named as unretained, so amplitude parameters carry a permanent not-fitted label | `kinetics_units.py`, `tests/test_kinetics_units.py` |

## Deliberate approximations (could be tightened, not yet)

These are simulator choices that a 1:1 claim would have to eliminate. The
required evidence partly exists in the retained files but has not been mapped
into model parameters:

1. **Manufacturing distributions.** With `lot_stats=None` (the default) apheresis
   input, overall recovery and transduction efficiency remain illustrative
   lognormal/round defaults, because the published BLA distributions are `(b)(4)`.
   With `lot_stats="<profile>"` the named attributes are replaced by published
   per-patient values, and the profile states which fields are still defaults.
   The `net_yield` used there is not measured: it is inverted from published dose,
   viability, CAR-positive fraction and leukapheresis input by
   `lot_distributions.implied_net_yield()`, and the inversion is reported per
   patient as `implied_net_yield`. For `commercial_ball_2023` that inversion gives
   a median overall recovery near 0.67, which is why the scenario default of 0.05
   is illustrative rather than conservative.
2. **Kinetics.** Expansion, cytokine and tumor-kill parameters are model
   assumptions with sensitivity ranges. The published kinetics denominators are
   now named explicitly, and the amplitude parameters carry a permanent
   not-fitted label (`kinetics_units.AMPLITUDE_IS_FITTED = False`), see
   [KINETICS_SOURCES.md](KINETICS_SOURCES.md) "Unit denominators".
3. **Potency.** The commercial IFN-γ release assay threshold is `(b)(4)`; the
   simulator has no numeric potency gate, which is correct behavior, and its
   potency proxies are model constructs, not that assay.
4. **Cohort defaults report passing microbial/appearance results.** This is a
   labeled scenario assumption (overridable through `lot_params`), not a
   measured batch property.
5. **Fitness bins and antigen-loss priors** in the micro engine are fixed
   assumptions; sampled manufacturing VCN does not set them.

## Structurally unestablishable from public evidence

No code change can make these 1:1; only the manufacturer's controlled records
contain them:

1. **Commercial-version identity of the vector.** JC053548.1 is the complete
   historical patent transfer vector with the exact CAR CDS. Which controlled
   transfer-plasmid version (pRKHVmuEC19 lineage or a successor) and which
   integrated-sequence annotation correspond to today's released product is not
   public. The EPAR Figure 2 schematic (CTL019 segment "1,460 nt") does not
   resolve CDS boundaries and must not be reconciled by adding bases.
2. **Redacted numerical limits.** The SBRA release table redacts viability, TE,
   CAR-expression, bead, endotoxin, IFN-γ and VSV-G limits as `(b)(4)`; they
   are quoted as redactions in [RELEASE_SOURCES.md](RELEASE_SOURCES.md) and
   remain unknown here.
3. **Master records and validated methods.** The master manufacturing record,
   full CPP operating ranges, in-process decision rules, change history, and
   the validated method behind each criterion (with reference materials) are
   not published in executable form. The EMA assessment confirms such content
   exists in the dossier; it does not reproduce it.
4. **Batch records and comparability data.** Experimental lot data and the
   process-transfer comparability study are internal. Simulated lots are not
   batch records.

## Why this is not a defect

The product is an autologous, patient-specific living cell drug with a
documented change history (site transfers, automation, assay revisions: see
PROCESS_SOURCES.md "Version history"). "The commercial version" is a moving
target, and a 1:1 claim without version anchoring would be wrong for some
version. The simulator's contract is the opposite: every constant either
matches a public record exactly (and is tested), or is labeled an assumption
and varied. A simulated "pass" never authorizes release
(`commercial_release_established: False` in every assessment), and no simulated
value migrates into the evidence set.

## Checklist to get closer to 1:1

Ordered by remaining effort, all verifiable against the retained files:

- [x] Map published per-patient ELIANA/B2202 product attributes into empirical
      cohort distributions instead of defaults. Done as far as the public
      evidence reaches. Two layers now exist: `publication_stats.py` (six
      median/range summaries, calibrated into two-sided log-normals, sampled with
      `product_stats="eliana_2018"`), and `lot_distributions.py` — 13 published
      per-patient product attributes from Fong 2023 (commercial pediatric B-ALL),
      Pasquini 2020 (US real-world), the 2025 FDA label's JULIET/ELARA dose
      medians, US20050113564A1 (academic transduction) and Kato 2025 (a 23-row
      empirical out-of-specification table drawn patient by patient) — exposed as
      four attributable lot profiles through `lot_stats=...`. Every value is a
      byte-exact quote from a retained file, every borrowed, derived or
      unpublished field is reported as an assumption, and the cohort reports
      published-dose attainment against the record. BLA/EPAR numeric tables are
      still `(b)(4)` (see PROCESS_SOURCES.md "Numeric tables"), so per-patient
      commercial VCN remains unavailable.
- [x] Bind kinetics to the PK observations in KINETICS_SOURCES.md with an
      explicit unit-denominator bridge, or label non-fitted permanently. Both
      halves are now recorded in `kinetics_units.py`: the time-denominated and
      cell-denominated published statistics are named as directly comparable,
      the amplitude bridge is written out as an identity, its three required
      factors are each marked "not supplied by any retained record", and
      `AMPLITUDE_IS_FITTED = False` labels the eight amplitude parameters as
      not-fitted. Closing the bridge needs a retained record stating leukocyte
      concentration, DNA mass per cell and VCN — not a better fit.
- [x] Record the version anchor inside simulation reports. `version_anchor.py`
      pins 12 record versions with byte-exact quotes and named version strings
      (June-2025 US label revision; BLA 125646/0 of 2017-08-30 and sBLA
      125646/76 of 2018-04-13 with its 2017-09-06 data cut-off; EU assessment
      report EMA/485563/2018 under procedure EMEA/H/C/004090/0000; the
      Fraunhofer site era from August 2016; trial-era 30-34 day versus
      then-commercial 24-day cycle time; the EU numerical non-release rule; the
      post-2017-08-30 commercial and registry eras with the 2019-2020 viability
      assay change; the Japanese 70% viability criterion and the 2019-02-20 PMDA
      review report that lists the Japanese release panel with asterisk-redacted
      limits; the 2005 academic process), each with the caveat that travels with
      it. `run_sim.py` prints all of them, plus the published-lot profile table
      and the kinetics denominator ledger.
- [ ] Keep the four enforced qualitative checks in step with any future label
      or amendment changes (approval-history letters are retained).

Everything else waits for manufacturer master records, not for code.
