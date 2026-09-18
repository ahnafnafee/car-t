"""Generate reproducible cohort summaries, ablation comparisons and SVG plots."""

import argparse
import math
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "simulator"))

import cart_sim as cs
from benchmarks import ARMS, BANDS, KINETICS, TRIALS, band_table
from plotsvg import PlotSVG


def fmt_copies(v):
    return f"{v:.2e}"


def patient_dynamics_plot(res, path, title):
    t = res["t"]
    pl = PlotSVG(title=title, ylab="cells (log scale)")
    pl.add("E effector", list(zip(t, res["E"])), log=True)
    pl.add("M memory", list(zip(t, res["M"])), log=True)
    if "T_hi" in res:
        cd19pos = [h + d for h, d in zip(res["T_hi"], res["T_dim"])]
    else:
        cd19pos = res["Ton"]
    pl.add("CD19+ tumor", list(zip(t, cd19pos)), log=True)
    pl.add("CD19- escape", list(zip(t, res["Toff"])), log=True)
    pl.add("B cells", list(zip(t, res["B"])), log=True)
    pl.save(path)


def patient_cytokine_plot(res, path, title):
    t = res["t"]
    pl = PlotSVG(title=title, ylab="pg/mL")
    pl.add("IFN-g", list(zip(t, res["IFN"])))
    pl.add("IL-6", list(zip(t, res["IL6"])))
    pl.add("TNF-a", list(zip(t, res["TNF"])))
    pl.save(path)


def ecdf_plot(values, path, title, xlab):
    xs = sorted(values)
    n = len(xs)
    data = [(xs[i], 100.0 * (i + 1) / n) for i in range(n)]
    pl = PlotSVG(title=title, ylab="% of cohort <= x", xlab=xlab)
    pl.add("cohort", data)
    pl.save(path)


def ablation_plot(arms, path):
    xs = list(range(len(arms)))
    orr = [100 * a["ORR"] for (_, a) in arms]
    cr = [100 * a["CR_rate"] for (_, a) in arms]
    per = [100 * a["persistent_rate"] for (_, a) in arms]
    rel = [100 * a["relapse_rate"] for (_, a) in arms]
    pl = PlotSVG(title="Ablation arms (0=base, see report table)", ylab="%")
    pl.add("ORR", list(zip(xs, orr)))
    pl.add("CR", list(zip(xs, cr)))
    pl.add("persistence", list(zip(xs, per)))
    pl.add("relapse", list(zip(xs, rel)))
    pl.save(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--n", type=int, default=200, help="patients per cohort/arm")
    ap.add_argument("--seed", type=int, default=1001)
    ap.add_argument(
        "--all-weight-kg",
        type=float,
        default=30.0,
        help="B-ALL scenario weight, not a sampled clinical distribution",
    )
    ap.add_argument(
        "--lot-stats",
        default="none",
        help="sample lots from a published attribute profile instead of scenario defaults "
        f"({', '.join(cs.lot_distributions.profile_names())}, or none)",
    )
    ap.add_argument("--outdir", type=Path, default=Path(__file__).parent / "out")
    args = ap.parse_args()
    if args.n <= 0:
        ap.error("--n must be positive")
    if not math.isfinite(args.all_weight_kg) or args.all_weight_kg <= 0:
        ap.error("--all-weight-kg must be positive and finite")
    if args.lot_stats != "none" and args.lot_stats not in cs.lot_distributions.LOT_PROFILES:
        ap.error(f"--lot-stats must be 'none' or one of {cs.lot_distributions.profile_names()}")
    args.outdir.mkdir(parents=True, exist_ok=True)
    evidence_link = Path(os.path.relpath(ROOT / "docs" / "EVIDENCE.md", args.outdir)).as_posix()
    release_link = Path(os.path.relpath(ROOT / "docs" / "RELEASE_SOURCES.md", args.outdir)).as_posix()
    lot_stats = None if args.lot_stats == "none" else args.lot_stats

    def lot_stats_for(indication):
        """A profile tied to one indication cannot be applied to the other cohort."""
        if lot_stats is None:
            return None
        wanted = cs.lot_distributions.LOT_PROFILES[lot_stats]["indication"]
        return lot_stats if wanted in (None, indication) else None

    cohorts = {
        ind: cs.run_cohort(
            n=args.n,
            seed=args.seed,
            indication=ind,
            weight_kg=args.all_weight_kg,
            lot_stats=lot_stats_for(ind),
        )
        for ind in ("DLBCL", "B-ALL")
    }
    lines = [
        "# CAR-T simulation report",
        "",
        f"Run: {args.n} patients per cohort, seed {args.seed}, micro engine.",
        "Plots are in this report's directory.",
        "",
        "These are phenomenological model outputs. Range membership is a",
        "calibration check, not clinical validation. Endpoint definitions and",
        f"source limitations are in [the evidence map](<{evidence_link}>).",
        "",
        "## Construct and process assumptions",
        "",
        f"Reference protein: {cs.CONSTRUCT['total_aa']} aa; generated CDS: "
        f"{cs.CONSTRUCT['orf_stop_bp']} bp including stop; "
        f"GC: {cs.CONSTRUCT['gc_pct']}%.",
        "Sequence identity does not determine the simulation's rate constants.",
        "",
        "The vector and manufacturing functions use hypothetical lot arithmetic.",
        "Viable CAR+ dose arithmetic and source-scoped criteria are explicit;",
        "yield, composition and titer scenarios remain assumptions. VCN is unknown.",
        "Passing disclosed criteria does not establish commercial lot release.",
        "US criteria source: [Pasquini et al., 2020](https://doi.org/10.1182/bloodadvances.2020003092).",
        f"B-ALL scenario weight: {args.all_weight_kg:g} kg; dose targets are scenario choices.",
        "",
    ]
    vec, man = cs.vector_production(), cs.manufacture()
    lines += [
        f"Vector titer: {vec['titer_conc_TU_mL']:.2e} TU/mL; "
        f"model target met: {vec['meets_target']}.",
        f"Nominal viable CAR+ dose: {man['dose_CARplus_cells']:.2e}; "
        f"source comparison: {man['source_assessment']['status']}.",
        "Hypothetical vector titer does not automatically alter cohort transduction or dose.",
        "",
        "## Source version anchors",
        "",
        "Evidence fixed for this run (version ledger: docs/ONE_TO_ONE.md):",
        "- Lot-release panel: 2017 US Summarizing Bases (BLA 125646/0, printed pp. 9-10);",
        f"  later label amendments supersede it. Scope: [the release sources](<{release_link}>).",
        f"- {len(cs.publication_stats.STATS)} published product/timeline/kinetics statistics are",
        "  transcribed verbatim in simulator/cart_sim/publication_stats.py from retained",
        "  files under data/references/; quotes are checked in tests/test_publication_stats.py.",
        "- Model time origin is infusion: manufacturing and enrollment timelines have no",
        "  simulated counterpart and anchor context only.",
        "",
        "| Published statistic | Published median [range] | Simulated counterpart |",
        "| --- | --- | --- |",
    ]
    ps = cs.publication_stats.STATS

    def anchor_row(key, counterpart):
        s = ps[key]
        return (
            f"| {s['unit']} ([source]({s['url']})) "
            f"| {s['median']:.3g} [{s['low']:.3g}, {s['high']:.3g}] | {counterpart} |"
        )

    ball = cohorts["B-ALL"]
    scenario_per_kg = (
        ball["patients"][0]["manufacturing"]["dose_viable_car_cells"] / args.all_weight_kg
    )
    lines += [
        anchor_row(
            "eliana2018_dose_per_kg",
            f"scenario target {scenario_per_kg:.2e}/kg at {args.all_weight_kg:g} kg; run "
            "run_cohort(product_stats='eliana_2018') to sample this distribution instead",
        ),
        anchor_row("eliana2018_total_dose", "follows the scenario target; not independently set"),
        anchor_row("eliana2018_screen_to_infuse_days", "none modeled: model time origin is infusion"),
        anchor_row("tyagarajan2020_cycle_days", "none modeled: manufacturing has no simulated time axis"),
        anchor_row(
            "eliana2018_tmax_responders_days",
            f"B-ALL effector peak day median {ball['E_peak_day_median']:.2f} "
            "(unconditioned, not response-matched)",
        ),
        anchor_row("eliana2018_persistence_days", "reported as a persistence fraction, not a day count"),
        "",
        *cs.version_anchor.anchor_lines(),
        "",
        "## Published lot profiles",
        "",
        "Scenario defaults for apheresis inputs, overall recovery and transduction are",
        "illustrative. Each profile below replaces named attributes with published",
        "per-patient values, so a run can be attributed to a named population instead",
        "of an invented distribution. Unpublished fields stay scenario defaults and are",
        "listed as assumptions per drawn lot.",
        "",
        "| Profile | Indication | Published attributes | Published medians |",
        "| --- | --- | --- | --- |",
    ]
    ld = cs.lot_distributions
    for name in ld.profile_names():
        spec = ld.LOT_PROFILES[name]
        keys = sorted({v for k, v in spec["fields"].items() if k != "empirical_pair"})
        medians = "; ".join(
            f"{k}: {v:.3g}" if isinstance(v, (int, float)) else f"{k}: {v}"
            for k, v in ld.published_medians(name).items()
        )
        lines.append(
            f"| {name} | {spec['indication'] or 'either'} | {', '.join(keys) or '(empirical table)'} "
            f"| {medians} |"
        )
    lines += [
        "",
        "Every profile's `population_caveat` is reproduced per patient in the cohort",
        "JSON as `lot_provenance`, together with `assumptions` naming each borrowed,",
        "derived or unpublished field.",
        "",
    ]
    if lot_stats is not None:
        for ind in ("DLBCL", "B-ALL"):
            cohort = cohorts[ind]
            if cohort.get("lot_stats") is None:
                lines.append(
                    f"{ind}: profile `{lot_stats}` is attributable to "
                    f"{ld.LOT_PROFILES[lot_stats]['indication']} only, so this cohort kept "
                    "scenario defaults."
                )
                continue
            lines += [
                f"{ind} cohort drawn from `{cohort['lot_stats']}` "
                f"(n={args.n}, weight {args.all_weight_kg:g} kg):",
            ]
            attainment = cohort["published_dose_attainment_median"]
            implied = cohort["implied_net_yield_median"]
            if attainment is None:
                lines.append(
                    "- published-dose attainment: not computed (this profile does not publish "
                    "the leukapheresis input, so overall recovery stays a scenario default)"
                )
            else:
                lines.append(f"- published-dose attainment median: {attainment:.3f}")
            if implied is None:
                lines.append("- implied overall recovery: not derivable from this profile")
            else:
                lines += [
                    f"- implied overall recovery median: {implied:.4f}",
                    "  (inverted from published dose, viability, CAR-positive fraction and",
                    "  leukapheresis input; a consistency inversion, not a measured recovery)",
                ]
    lines += [
        "",
        "## Trial observations",
        "",
        "These observations retain each trial's product, denominator and endpoint.",
        "They are contextual anchors, not matched tests of the model.",
        "",
        "| Trial | Indication | Product | N | Endpoint | Observation |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for trial, ind, product, n, endpoint, value, url in TRIALS:
        lines.append(f"| [{trial}]({url}) | {ind} | {product} | {n} | {endpoint} | {value} |")
    lines += [
        "",
        "## Cellular kinetics references",
        "",
        "Time origin is infusion. These response-conditioned blood measurements",
        "are not validation bands for the unconditioned whole-population model.",
        "qPCR copies/microgram DNA and flow fractions are not absolute cell counts.",
        "",
        "| Study | Response group | N with estimated peak | Assay | Median peak day |",
        "| --- | --- | ---: | --- | ---: |",
    ]
    lines.extend(
        f"| [{study}]({url}) | {group} | {n} | {assay} | {day:g} |"
        for study, group, n, assay, day, url in KINETICS
    )
    lines += ["", "```"] + cs.kinetics_units.bridge_status() + ["```"]
    for ind, cohort in cohorts.items():
        lines += [
            "",
            f"## {ind} model ranges",
            "",
            f"Lot comparisons: {cohort['lot_assessment_counts']}. These are partial source checks.",
            f"Unconditioned model effector peak day, median: {cohort['E_peak_day_median']:.2f}.",
            "",
            "| Metric | Simulated | Assumed range | Check |",
            "| --- | ---: | --- | --- |",
        ]
        rows = band_table(cohort, ind)
        lines.extend(
            f"| {label} | {value:.1f} | {lo}–{hi} | {'IN RANGE' if ok else 'OUTSIDE'} |"
            for label, value, lo, hi, _, ok in rows
        )
        lines += [
            "",
            f"{sum(row[-1] for row in rows)}/{len(BANDS[ind])} "
            "model ranges contain this run's estimate.",
        ]
    patients = cohorts["DLBCL"]["patients"]
    examples = [("patient_responder", next((r for r in patients if r["CR"]), patients[0]))]
    relapser = next((r for r in patients if r["relapses"]), None)
    if relapser is not None:
        examples.append(("patient_relapser", relapser))
    lines += ["", "## Example trajectories", ""]
    for name, patient in examples:
        lines.append(
            f"- {name}: response={patient['responds']}, "
            f"deep response={patient['CR']}, relapse={patient['relapses']}; "
            f"initial antigen-negative fraction={patient['f_agloss']:.3f}."
        )
        patient_dynamics_plot(patient, args.outdir / f"{name}_dynamics.svg", name)
        patient_cytokine_plot(patient, args.outdir / f"{name}_cytokines.svg", name)
    ecdf_plot(
        [math.log10(max(r["IL6_peak"], 1e-3)) for r in patients],
        args.outdir / "cohort_il6_ecdf.svg",
        "DLBCL: simulated peak IL-6",
        "log10(peak IL-6, pg/mL)",
    )
    arms = []
    for name, base, mode in ARMS:
        cohort = (
            cohorts["DLBCL"]
            if not base and mode is None
            else cs.run_cohort(
                base=base,
                n=args.n,
                seed=args.seed,
                indication="DLBCL",
                agloss_mode=mode or "natural",
            )
        )
        arms.append((name, cohort))
    lines += [
        "",
        "## Parameter ablations",
        "",
        "Arm names describe model parameter changes; they do not reconstruct",
        "different products from molecular sequences.",
        "",
        "| Arm | Response % | Deep response % | Relapse % | Persistence % |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    lines.extend(
        f"| {name} | {100 * c['ORR']:.1f} | {100 * c['CR_rate']:.1f} | "
        f"{100 * c['relapse_rate']:.1f} | {100 * c['persistent_rate']:.1f} |"
        for name, c in arms
    )
    ablation_plot(arms, args.outdir / "ablation_summary.svg")
    lines += [
        "",
        "## Interpretation limits",
        "",
        "No holdout cohort or patient-level fitting is included. The ODE and",
        "micro engines share assumptions; agreement is not independent validation.",
        "The micro engine uses a deterministic population rescale and approximate",
        "Poisson sampling. Its exhaustion labels do not reduce aggregate function.",
        "CRS and ICANS outputs are synthetic categories, not ASTCT grades.",
        "Relapse fractions use all simulated patients as the denominator.",
        "Monte Carlo variation and numerical discretization both affect results.",
        "",
    ]
    report = args.outdir / "SIM_REPORT.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report}")
    for ind, cohort in cohorts.items():
        print(f"{ind}: response={cohort['ORR']:.3f}, deep response={cohort['CR_rate']:.3f}")


if __name__ == "__main__":
    main()
