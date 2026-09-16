# Cellular kinetics and simulation correspondence

Checked 2026-09-16. These primary studies add measurable clinical context to the
[manufacturing evidence](PROCESS_SOURCES.md). Their endpoints concern blood
samples, not the simulator's whole-population cell compartments. The appropriate
software changes are therefore source-specific reporting and removal of
unsupported causal shortcuts, rather than a forced numerical fit.

## B-ALL trial observations

Mueller et al. report ELIANA peripheral-blood qPCR kinetics by response at day 28.
In Table 1, responders are CR/CRi and nonresponders are NR; the number of patients
with each estimable parameter differs. These are trial observations, not a
distribution of current commercial manufacturing lots. [Mueller et al., Clinical
Cancer Research, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7433345/)

| Measurement | Responders | Nonresponders |
| --- | --- | --- |
| Peak time, median days (range), n | 9.91 (0.00764–27.0), 61 | 20.0 (0.0278–62.7), 7 |
| Peak transgene, geometric mean copies/microgram genomic DNA, n | 34,700, 61 | 20,000, 7 |
| AUC through day 28, geometric mean copies/microgram DNA × days, n | 318,000, 61 | 156,000, 6 |
| Last quantifiable observation, median days (range), n | 102 (17.8–380), 62 | 27.8 (20.9–83.9), 8 |

Seven peaks sampled before day 1 might reflect catheter contents. The paper finds
no relationship between the studied dose/manufacturing attributes and qPCR
kinetics within the observed ranges; this is not proof of zero biological effect
outside those ranges. Last observation depends on follow-up and assay sensitivity,
so it cannot be substituted for cell lifespan. [Mueller et al., Table 1 footnote
and Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC7433345/)

## A separately fitted empirical reference

Stein et al. fitted blood transgene kinetics from 90 pediatric/young-adult B-ALL
patients: ELIANA 61 and ENSIGN 29. Table 1 supplies the following typical model
parameters. These are fitted parameters, not observed cohort medians or a
commercial production specification. [Stein et al., 2019, Table 1,
doi:10.1002/psp4.12388](https://pmc.ncbi.nlm.nih.gov/articles/PMC6539725/)

| Parameter | Estimate | Unit |
| --- | --- | --- |
| Expansion fold | 3,900 | Dimensionless |
| Peak time | 9.3 | Days |
| Peak transgene | 24,000 | Copies/microgram genomic DNA |
| Fast decline rate, alpha | 0.16 | Per day |
| Slow component fraction, F_B | 0.0079 | Dimensionless |
| Slow decline rate, beta | 0.0032 | Per day |

The reported doubling time and fast/terminal decline half-lives are 0.78, 4.3,
and 220 days. These offer a separate empirical benchmark, but alpha/beta are not
automatically the simulator's effector/memory death rates: antigen stimulation,
transitions, compartments and observation models differ. [Stein et al., abstract
and model description](https://pmc.ncbi.nlm.nih.gov/articles/PMC6539725/)

## DLBCL is not interchangeable with B-ALL

Awasthi et al. studied 111 JULIET patients. Table 1 reports flow-cytometry blood
measurements classified by response at month 3. Peak CAR-positive percentage
among CD3-positive cells had geometric means of 4.81% for CR/PR (n=34) and 4.18%
for SD/PD/unknown (n=50); median peak times were 6.35 and 7.64 days, respectively.
These are not qPCR peak times or absolute CAR-cell counts. [Awasthi et al., Blood
Advances 2020, Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7013261/)

The study did not identify qPCR-kinetic relationships with the examined product
characteristics or dose. Its illustrative conversion from transgene to circulating
cells assumes leukocyte concentration, DNA mass per cell and transgene copies per
cell; none is supplied by a whole-body cell count alone. Consequently, qPCR
copies/microgram and flow percentages cannot directly calibrate `E_peak` in cells.
[Awasthi et al., bioanalytical methods and Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC7013261/)

## What lower viability does and does not establish

Chong et al. retrospectively studied academic CTL019 products, not a complete
commercial release panel. Among 25 DLBCL products, median viability was 88.6%
(73.7–96%); only four were below 80%. Correlations between viability and peak
expansion were weak and nonsignificant: ALL r=-0.0986 (n=62, P=.45), DLBCL r=0.23
(n=24, P=.28). [Chong et al., Blood 2019,
doi:10.1182/blood.2019002258](https://pmc.ncbi.nlm.nih.gov/articles/PMC6872962/)

This provides no quantitative basis for reducing every out-of-specification lot's
simulated dose or activity by 40%. Removing that penalty removes an unsupported
model rule; it does not show that all OOS products are equivalent, safe or
eligible for infusion. In particular, sterility failures and an academic viability
comparison must not be collapsed into a common efficacy multiplier.

## Updated persistence evidence

Awasthi et al.'s 2025 analysis of ELIANA/ENSIGN/JULIET defines loss of blood
transgene persistence as the first postpeak sample below 50 copies/microgram DNA.
Its B-cell-recovery illustrations use greater than 1% CD19-positive B cells. Among
47 B-ALL patients with ongoing CR, 24 lost detectable persistence, with median
355 days (range 60–961). Thus, loss of the assay signal does not deterministically
imply relapse. [Awasthi et al., Blood Advances 2025, Figure 2 and Figure 3,
doi:10.1182/bloodadvances.2024014995](https://pmc.ncbi.nlm.nih.gov/articles/PMC12405623/)

The simulator's day-90 B-cell-count threshold and day-120 CAR-cell threshold
remain model proxies. Neither becomes the above clinical endpoint without the
corresponding sample denominator, assay model and observation schedule. This is
a model-to-measurement inference, not an additional threshold from the paper.

## Implementation decisions

- Keep administered dose in CAR-positive viable T cells, independently of latent
  fitness. A fitness hypothesis may alter modeled dynamics, but must not silently
  redefine the reported physical dose.
- Apply viability once when converting a recovered total-cell count to a viable
  dose; do not apply it again to an already viable measured count.
- Do not couple an illustrative vector-titer shortfall to a fixed transduction
  penalty or a partial release assessment to a fixed dose penalty. The inspected
  sources do not estimate either coefficient.
- Keep unknown VCN unknown. A permissible interval in an academic release panel
  does not specify a mean, variance or commercial lot distribution.
- Display clinical references alongside model outputs with units, study scope,
  time origin and endpoint population intact. Do not turn these into automatic
  pass/fail bands for `E_peak`, persistence or response.
- Do not fit an unconditioned simulated cohort to response-conditioned summaries:
  that would import outcome labels into calibration. Patient-level observations
  and an explicit measurement model are needed for an identifiable fit.

These choices improve correspondence without claiming clinical validation.
Direct PMC page requests intermittently returned browser checks; the numerical
tables and passages above were available in indexed primary-article text.
No patient-level data or unpublished manufacturing distribution was recovered.
