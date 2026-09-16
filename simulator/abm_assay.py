"""Agent-based 2D cytotoxicity model and exploratory comparison with ODE rates.

Motility, synapse timing and fatigue are assumed phenomenological parameters.
The shared engagement function makes this a consistency comparison, not an
independent experimental validation.
"""

import argparse
import math
import os
import random
import sys
from html import escape

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cart_sim as cs
from plotsvg import PlotSVG

# ---------------------------------------------------------------------------
# Parameters (illustrative model assumptions)
# ---------------------------------------------------------------------------
ABM = {
    # arena / geometry
    "arena_um": 1200.0,  # square field side
    "r_tumor": 10.0,  # tumor cell radius (um)
    "r_T": 7.0,  # T cell radius (um)
    "dt_min": 0.25,  # time step (min) = 15 s
    # T-cell motility (activated T cells in tissue: 10-20 um/min)
    "speed_mean": 12.0,  # um/min
    "speed_sd": 3.0,
    "turn_sd": 0.55,  # rad per step (directional persistence ~2-4 min)
    "sense_um": 60.0,  # chemotaxis sensing radius
    "chemotaxis": 0.35,  # steering strength toward local tumor centroid
    # conjugation / synapse
    "p_bond": 0.5,  # per contact-step bond probability factor (* sqrt(eng))
    "tau_kill_min": 22.0,  # mean synapse-to-kill time (min) at full engagement
    "tau_fail_min": 75.0,  # dwell cap: beyond this the bond fails (no kill)
    "t_rest_min": 12.0,  # post-kill refractory (re-arming) (min)
    "t_failrest_min": 5.0,  # refractory after a failed synapse (min)
    # fatigue / serial-killing limits
    "fatigue_tau": 1.0,  # synapse time scales +100% * fatigue
    "fatigue_rest_tau": 0.6,  # rest time scales +100% * fatigue
    "fatigue_recover_min": 45.0,  # one fatigue unit recovered per 45 min idle
    # tumor
    "cd19_sd": 0.35,  # lognormal spread of CD19 density per cell
    "cd19_floor": 0.0,
    # consistency with the ODE model
    "costim": 1.0 + cs.default_params()["f41"],  # 4-1BB costimulation = 1.3
    "Kd_app": cs.default_params()["Kd_app"],  # avidity half-saturation
}


class Tumor:
    __slots__ = ("x", "y", "cd19", "eng", "alive", "bonded", "died_t")

    def __init__(self, x, y, cd19):
        self.x, self.y = x, y
        self.cd19 = cd19
        self.eng = cs.binder_engagement(cd19, ABM["Kd_app"])
        self.alive = True
        self.bonded = False
        self.died_t = None


class Tcell:
    __slots__ = (
        "x",
        "y",
        "th",
        "v",
        "state",
        "partner",
        "t_bond",
        "tau_need",
        "t_rest",
        "fatigue",
        "kills",
        "x0",
        "y0",
        "bond_total",
    )

    def __init__(self, x, y, rng):
        self.x, self.y = x, y
        self.x0, self.y0 = x, y
        self.th = rng.uniform(0, 2 * math.pi)
        self.v = max(2.0, rng.gauss(ABM["speed_mean"], ABM["speed_sd"]))
        self.state = "free"  # free | bonded | resting
        self.partner = -1
        self.t_bond = 0.0
        self.tau_need = 0.0
        self.t_rest = 0.0
        self.fatigue = 0.0
        self.kills = 0
        self.bond_total = 0.0


class Assay:
    """One in-silico cytotoxicity assay."""

    def __init__(self, n_tumor, n_t, cd19_mean, seed, hours=6.0, chemotaxis=None, label=""):
        for name, count in (("n_tumor", n_tumor), ("n_t", n_t)):
            if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
                raise ValueError(f"{name} must be a positive integer")
        if not math.isfinite(hours) or hours <= 0:
            raise ValueError("hours must be finite and positive")
        cs.binder_engagement(cd19_mean, ABM["Kd_app"])
        self.rng = random.Random(seed)
        self.n_tumor = n_tumor
        self.n_t = n_t
        self.cd19_mean = cd19_mean
        self.hours = hours
        self.label = label or f"cd19={cd19_mean:.0e} E:T=1:{n_tumor // max(n_t, 1)}"
        self.chemo = ABM["chemotaxis"] if chemotaxis is None else chemotaxis
        A = ABM["arena_um"]

        # Seed each population on a jittered lattice; overlaps are not excluded.
        def lattice(n):
            side = max(2, int(math.ceil(math.sqrt(n))))
            step = A / (side + 1)
            pts = []
            for i in range(side):
                for j in range(side):
                    if len(pts) >= n:
                        break
                    pts.append(
                        (
                            step * (i + 1) + self.rng.uniform(-step * 0.35, step * 0.35),
                            step * (j + 1) + self.rng.uniform(-step * 0.35, step * 0.35),
                        )
                    )
            while len(pts) < n:  # rare overflow
                pts.append((self.rng.uniform(0, A), self.rng.uniform(0, A)))
            return pts

        self.tumors = []
        for x, y in lattice(n_tumor):
            cd19 = (
                0.0
                if cd19_mean <= 0
                else min(3.0e6, cd19_mean * math.exp(self.rng.gauss(0, ABM["cd19_sd"])))
            )
            self.tumors.append(Tumor(x, y, cd19))
        self.tcells = [Tcell(x, y, self.rng) for (x, y) in lattice(n_t)]

        # static tumor spatial grid (bins of ~60 um) for neighbor queries
        self.bin = ABM["sense_um"]
        self.grid = {}
        for i, tm in enumerate(self.tumors):
            self.grid.setdefault(self._bkey(tm.x, tm.y), []).append(i)

        self.t = 0.0
        self.dt = ABM["dt_min"]
        self.nsteps = math.ceil(hours * 60.0 / self.dt)
        self.series_t = [0.0]
        self.series_alive = [n_tumor]
        self.series_conj = [0]
        self.dwell_times = []
        self.snapshots = {}

    # -- helpers ------------------------------------------------------------
    def _bkey(self, x, y):
        return (int(x // self.bin), int(y // self.bin))

    def _nearby_tumors(self, x, y, radius):
        bx, by = self._bkey(x, y)
        r2 = radius * radius
        reach = math.ceil(radius / self.bin)
        for i in range(bx - reach, bx + reach + 1):
            for j in range(by - reach, by + reach + 1):
                for idx in self.grid.get((i, j), ()):
                    tm = self.tumors[idx]
                    if tm.alive:
                        dx, dy = tm.x - x, tm.y - y
                        d2 = dx * dx + dy * dy
                        if d2 <= r2:
                            yield idx, d2

    # -- one time step ------------------------------------------------------
    def step(self):
        rng, A = self.rng, ABM["arena_um"]
        dt = self.dt
        contact_r = ABM["r_T"] + ABM["r_tumor"] + 1.0

        for tc in self.tcells:
            if tc.state == "resting":
                tc.t_rest -= dt
                tc.fatigue = max(0.0, tc.fatigue - dt / ABM["fatigue_recover_min"])
                if tc.t_rest <= 0:
                    tc.state = "free"
                continue

            if tc.state == "bonded":
                tm = self.tumors[tc.partner]
                tc.t_bond += dt
                tc.bond_total += dt
                if tc.t_bond >= tc.tau_need and tc.tau_need <= ABM["tau_fail_min"]:
                    tm.alive = False  # kill
                    tm.bonded = False
                    tm.died_t = self.t + dt
                    tc.kills += 1
                    tc.fatigue += 1.0
                    self.dwell_times.append(tc.t_bond)
                    tc.state = "resting"
                    tc.t_rest = ABM["t_rest_min"] * (1 + ABM["fatigue_rest_tau"] * tc.fatigue)
                elif tc.t_bond >= ABM["tau_fail_min"]:  # failed synapse
                    tm.bonded = False
                    self.dwell_times.append(tc.t_bond)
                    tc.state = "resting"
                    tc.t_rest = ABM["t_failrest_min"]
                continue

            # free: persistent random walk with chemotactic bias
            tc.th += rng.gauss(0, ABM["turn_sd"])
            if self.chemo > 0:
                sx = sy = 0.0
                found = False
                for idx, _ in self._nearby_tumors(tc.x, tc.y, ABM["sense_um"]):
                    tm = self.tumors[idx]
                    if not tm.bonded:
                        sx += tm.x - tc.x
                        sy += tm.y - tc.y
                        found = True
                if found:
                    th_target = math.atan2(sy, sx)
                    dth = (th_target - tc.th + math.pi) % (2 * math.pi) - math.pi
                    tc.th += self.chemo * dth
            d = tc.v * dt
            nx = tc.x + d * math.cos(tc.th)
            ny = tc.y + d * math.sin(tc.th)
            if nx < 0 or nx > A:
                tc.th = math.pi - tc.th
                nx = min(max(nx, 0.0), A)
            if ny < 0 or ny > A:
                tc.th = -tc.th
                ny = min(max(ny, 0.0), A)
            tc.x, tc.y = nx, ny

            # contact -> try to bond (nearest available tumor)
            best, best_d2 = -1, 1e18
            for idx, d2 in self._nearby_tumors(tc.x, tc.y, contact_r):
                if not self.tumors[idx].bonded and d2 < best_d2:
                    best, best_d2 = idx, d2
            if best >= 0:
                eng = self.tumors[best].eng
                p = ABM["p_bond"] * math.sqrt(eng)
                if rng.random() < p:
                    tc.state = "bonded"
                    tc.partner = best
                    tc.t_bond = 0.0
                    self.tumors[best].bonded = True
                    tau_scale = 1 + ABM["fatigue_tau"] * tc.fatigue
                    mean = ABM["tau_kill_min"] / max(eng * ABM["costim"], 1e-6)
                    tc.tau_need = -math.log(max(rng.random(), 1e-12)) * mean * tau_scale

        self.t += dt

    # -- run ----------------------------------------------------------------
    def run(self, snap_at=(0.0, None, None)):
        if self.t > 0:
            raise RuntimeError("an Assay instance can only be run once")
        mid = self.hours * 60.0 / 2.0
        want = [
            snap_at[0] if snap_at[0] is not None else 0.0,
            snap_at[1] if snap_at[1] is not None else mid,
            snap_at[2] if snap_at[2] is not None else self.hours * 60.0,
        ]
        self._snapshot(0)  # t = 0, pre-step
        for i in range(self.nsteps):
            self.dt = min(ABM["dt_min"], self.hours * 60.0 - self.t)
            self.step()
            if (i + 1) % 4 == 0 or i == self.nsteps - 1:  # 1-min cadence
                self.series_t.append(self.t)
                self.series_alive.append(sum(1 for tm in self.tumors if tm.alive))
                self.series_conj.append(sum(1 for tc in self.tcells if tc.state == "bonded"))
            for k in (1, 2):
                if self.t >= want[k] and k not in self.snapshots:
                    self._snapshot(k)
        return self.stats()

    # -- outputs ------------------------------------------------------------
    def stats(self):
        alive = self.series_alive
        t = self.series_t
        kills = [tc.kills for tc in self.tcells]
        n0, nend = alive[0], alive[-1]
        k_obs = fit_exp_rate(t, alive)
        elapsed_min = t[-1]
        msd = sum((tc.x - tc.x0) ** 2 + (tc.y - tc.y0) ** 2 for tc in self.tcells) / self.n_t
        dwell = self.dwell_times
        return {
            "label": self.label,
            "n_tumor0": n0,
            "n_tumor_end": nend,
            "frac_killed": 1.0 - nend / max(n0, 1),
            "k_obs_per_h": (k_obs * 60.0) if k_obs else None,
            "per_effector_per_day": (k_obs * 60.0 * 24.0 * n0 / self.n_t) if k_obs else None,
            "kills_mean": sum(kills) / self.n_t,
            "kills_max": max(kills),
            "kills_total": sum(kills),
            "dwell_mean_min": (sum(dwell) / len(dwell)) if dwell else None,
            "dwell_n": len(dwell),
            "msd_um2": msd,
            "D_um2_min": msd / (4.0 * elapsed_min) if elapsed_min > 0 else None,
            "hours": self.hours,
            "assay": self,
        }

    def _snapshot(self, k):
        A = ABM["arena_um"]
        S = 640.0  # SVG size
        sc = S / A
        o = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(S)}" height="{int(S)}" '
            f'font-family="Segoe UI, Arial, sans-serif">',
            f'<rect width="{int(S)}" height="{int(S)}" fill="#fbfbfd"/>',
            f'<text x="12" y="20" font-size="14" fill="#111">{escape(self.label)} — '
            f"t={(self.t / 60.0):.1f} h, viable={sum(1 for tm in self.tumors if tm.alive)}</text>",
        ]
        for tm in self.tumors:
            if tm.alive:
                g = min(1.0, tm.eng)
                col = f"rgb({int(40 + 80 * (1 - g))},{int(90 + 60 * g)},{int(200)})"
                o.append(
                    f'<circle cx="{tm.x * sc:.1f}" cy="{tm.y * sc:.1f}" r="{ABM["r_tumor"] * sc:.1f}"'
                    f' fill="{col}" fill-opacity="0.75" stroke="#345"/>'
                )
            else:
                o.append(
                    f'<circle cx="{tm.x * sc:.1f}" cy="{tm.y * sc:.1f}" r="{ABM["r_tumor"] * sc:.1f}"'
                    f' fill="#cccccc" fill-opacity="0.45" stroke="#bbb"/>'
                )
        for tc in self.tcells:
            if tc.state == "bonded":
                tm = self.tumors[tc.partner]
                o.append(
                    f'<line x1="{tc.x * sc:.1f}" y1="{tc.y * sc:.1f}" x2="{tm.x * sc:.1f}" '
                    f'y2="{tm.y * sc:.1f}" stroke="#2ca02c" stroke-width="2.2"/>'
                )
                col = "#2ca02c"
            elif tc.state == "resting":
                col = "#ff8c00"
            else:
                col = "#d62728"
            o.append(
                f'<circle cx="{tc.x * sc:.1f}" cy="{tc.y * sc:.1f}" r="{ABM["r_T"] * sc:.1f}"'
                f' fill="{col}" stroke="#555"/>'
            )
        o.append("</svg>")
        self.snapshots[k] = "\n".join(o)


# ---------------------------------------------------------------------------
# analysis helpers
# ---------------------------------------------------------------------------
def fit_exp_rate(ts, alive):
    """Log-linear slope of viable counts over the 90%->30% kill window (per min)."""
    n0 = alive[0]
    lo, hi = 0.30 * n0, 0.90 * n0
    pts = [(t, v) for t, v in zip(ts, alive) if lo <= v <= hi and v > 0]
    if len(pts) < 8:
        return None
    xs = [t for t, _ in pts]
    ys = [math.log(v) for _, v in pts]
    n = len(pts)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx <= 0:
        return None
    return -sxy / sxx  # positive: decay rate (per min)


def killcurve_svg(runs, path, title="ABM kill curves"):
    pl = PlotSVG(title=title, ylab="viable tumor fraction", xlab="time (h)")
    for r in runs:
        a = r["assay"]
        n0 = max(r["n_tumor0"], 1)
        data = [(t / 60.0, v / n0) for t, v in zip(a.series_t, a.series_alive)]
        pl.add(r["label"], data)
    pl.save(path)
    return path


def histogram_svg(values, path, title, xlab):
    if not values:
        return None
    lo, hi = min(values), max(values)
    nb = min(12, max(4, hi - lo + 1))
    w = (hi - lo + 1e-9) / nb
    hist = [0] * nb
    for v in values:
        hist[min(nb - 1, int((v - lo) / w))] += 1
    pl = PlotSVG(title=title, ylab="T cells", xlab=xlab)
    pl.add("dist", [(lo + (i + 0.5) * w, c) for i, c in enumerate(hist)])
    pl.save(path)
    return path


# ---------------------------------------------------------------------------
# ODE cross-validation
# ---------------------------------------------------------------------------
def ode_reference_rates():
    """Per-effector kill rates implied by the ODE (cart_sim) kill term."""
    p = cs.default_params()
    eng = cs.binder_engagement(p["cd19_tumor"], p["Kd_app"])
    costim = 1 + p["f41"]
    hi = eng * costim * (p["kKill0"] * 1.0e10 / (1.0e10 + p["Kd_T"]) + p["kKill_fixed"])
    floor = eng * costim * p["kKill_fixed"]
    return {"eng": eng, "costim": costim, "rate_highT": hi, "rate_floor": floor}


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------
def run_assay(n_tumor, n_t, cd19, seed, hours, label=None, chemotaxis=None):
    a = Assay(n_tumor, n_t, cd19, seed=seed, hours=hours, chemotaxis=chemotaxis, label=label)
    return a.run()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hours", type=float, default=6.0)
    ap.add_argument("--tumor", type=int, default=240)
    ap.add_argument("--et", type=int, default=4, help="E:T ratio, e.g. 4 = 1:4")
    ap.add_argument("--cd19", type=float, default=cs.CD19_TUMOR_DLBCL)
    ap.add_argument("--ko", action="store_true", help="CD19-KO specificity control")
    ap.add_argument("--seed", type=int, default=4242)
    ap.add_argument("--crossval", action="store_true")
    ap.add_argument("--outdir", default=None)
    args = ap.parse_args()
    if args.et <= 0 or args.tumor <= 0 or not math.isfinite(args.hours) or args.hours <= 0:
        ap.error("--et, --tumor and --hours must be positive")
    if not math.isfinite(args.cd19) or args.cd19 < 0:
        ap.error("--cd19 must be finite and nonnegative")
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = args.outdir or os.path.join(here, "out")
    os.makedirs(outdir, exist_ok=True)
    L = []

    def w(s=""):
        L.append(s)

    cd19_main = 0.0 if args.ko else args.cd19
    n_t = max(1, args.tumor // args.et)

    w("# Microscale ABM Assay Report (agent-based)")
    w()
    w(
        f"Generated by `abm_assay.py` (seed={args.seed}, dt={ABM['dt_min']} min, arena "
        f"{ABM['arena_um']:.0f} um). Agent rules: persistent random walk "
        f"({ABM['speed_mean']:.0f} um/min) + chemotaxis; contact bonding probability "
        f"~ sqrt(engagement); synapse-to-kill dwell ~ Exp(mean "
        f"{ABM['tau_kill_min']:.0f} min / (engagement x costimulation)); dwell cap "
        f"{ABM['tau_fail_min']:.0f} min (failed synapse); post-kill refractory "
        f"{ABM['t_rest_min']:.0f} min + cumulative fatigue. Engagement uses the SAME "
        f"avidity function as the ODE (Kd_app = {ABM['Kd_app']:.0e} copies/cell, "
        f"costimulation x{ABM['costim']:.1f})."
    )
    w()

    # ---- main run ---------------------------------------------------------
    r = run_assay(
        args.tumor,
        n_t,
        cd19_main,
        args.seed,
        args.hours,
        label=("CD19-KO control" if args.ko else "CD19-high, E:T 1:%d" % args.et),
    )
    a = r["assay"]
    w("## 1. Main assay")
    w()
    w(
        f"**{r['label']}** ({args.tumor} tumor cells, {n_t} CAR-T, {args.hours:.0f} h): "
        f"viable {r['n_tumor0']} -> {r['n_tumor_end']} "
        f"(**{100 * r['frac_killed']:.0f}% killed**)."
    )
    w()
    w(
        f"- fitted kill rate: "
        f"{('%.3f /h' % r['k_obs_per_h']) if r['k_obs_per_h'] else 'n/a (insufficient kill)'}"
    )
    w(
        f"- per-effector capacity: "
        f"{('%.1f kills/effector/day' % r['per_effector_per_day']) if r['per_effector_per_day'] else 'n/a'}"
    )
    w(
        f"- serial killing: mean {r['kills_mean']:.1f}, max {r['kills_max']} kills/T cell "
        f"({r['kills_total']} total)"
    )
    w(
        f"- conjugate dwell: mean "
        f"{('%.1f min' % r['dwell_mean_min']) if r['dwell_mean_min'] else 'n/a'} "
        f"over {r['dwell_n']} bonds"
    )
    w(f"- motility: MSD {r['msd_um2']:.0f} um^2 -> D = {r['D_um2_min']:.0f} um^2/min")
    w()

    # snapshots
    base = "ko_" if args.ko else ""
    for k, name in ((0, "t0"), (1, "tmid"), (2, "tend")):
        svg = a.snapshots.get(k)
        if svg:
            p = os.path.join(outdir, f"abm_{base}snapshot_{name}.svg")
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg)
    killcurve_svg(
        [r], os.path.join(outdir, f"abm_{base}killcurve.svg"), f"Kill curve — {r['label']}"
    )
    histogram_svg(
        [tc.kills for tc in a.tcells],
        os.path.join(outdir, f"abm_{base}serialkill.svg"),
        "Serial killing distribution",
        "kills per T cell",
    )
    w(
        f"Plots: `abm_{base}snapshot_t0/tmid/tend.svg`, `abm_{base}killcurve.svg`, "
        f"`abm_{base}serialkill.svg` (in `out/`)."
    )
    w()

    # ---- specificity gate -------------------------------------------------
    if args.ko:
        ok = r["frac_killed"] < 0.05
        w("## Specificity control")
        w()
        w(
            f"CD19-KO kill fraction {100 * r['frac_killed']:.1f}% "
            f"{'**< 5% — PASS** (no meaningful off-target killing)' if ok else '**FAIL** — investigate'}"
        )
        w()
    else:
        # run the KO control alongside for the report
        rk = run_assay(args.tumor, n_t, 0.0, args.seed, args.hours, label="CD19-KO control")
        ok = rk["frac_killed"] < 0.05
        w("## 2. Specificity control (auto-run)")
        w()
        w(
            f"Same field with CD19-KO tumor cells: {100 * rk['frac_killed']:.1f}% killed — "
            f"{'**< 5% — PASS**' if ok else '**FAIL**'}. The avidity gate, not an ad-hoc "
            f"rule, produces specificity."
        )
        w()
        killcurve_svg(
            [r, rk],
            os.path.join(outdir, "abm_killcurve_with_ko.svg"),
            "Kill curves — CD19-high vs CD19-KO",
        )

    # ---- cross-validation -------------------------------------------------
    cap_hi = None
    if args.crossval:
        w("## 3. Model comparison with the ODE kill term")
        w()
        conds = [
            ("CD19-high 1:4", args.tumor, max(1, args.tumor // 4), cs.CD19_TUMOR_DLBCL),
            ("CD19-dim 1:4", args.tumor, max(1, args.tumor // 4), 3.0e4),
            ("CD19-KO 1:4", args.tumor, max(1, args.tumor // 4), 0.0),
            ("CD19-high sparse 1:20", 40, 2, cs.CD19_TUMOR_DLBCL),
            ("CD19-high 1:2", args.tumor, max(1, args.tumor // 2), cs.CD19_TUMOR_DLBCL),
        ]
        runs = []
        for name, nt, nc, cd in conds:
            runs.append(run_assay(nt, nc, cd, args.seed + len(runs), args.hours, label=name))
        ode = ode_reference_rates()
        w("| condition | killed % | k (/h) | capacity (kills/effector/day) | dwell mean (min) |")
        w("|---|---|---|---|---|")
        for rr in runs:
            k = f"{rr['k_obs_per_h']:.3f}" if rr["k_obs_per_h"] else "n/a"
            cap = f"{rr['per_effector_per_day']:.1f}" if rr["per_effector_per_day"] else "n/a"
            dw = f"{rr['dwell_mean_min']:.1f}" if rr["dwell_mean_min"] else "n/a"
            w(f"| {rr['label']} | {100 * rr['frac_killed']:.0f} | {k} | {cap} | {dw} |")
        w()
        cap_hi = next(
            (
                rr["per_effector_per_day"]
                for rr in runs
                if rr["label"] == "CD19-high 1:4" and rr["per_effector_per_day"]
            ),
            None,
        )
        w(
            "ODE (`cart_sim` package, ode_engine) implied per-effector rates for the same engagement "
            f"(eng={ode['eng']:.2f}, costim x{ode['costim']:.1f}):"
        )
        w()
        w(
            f"- saturating tumor burden: **{ode['rate_highT']:.1f} kills/effector/day** "
            f"(mass-action term at T=1e10)"
        )
        w(f"- vanishing burden floor: **{ode['rate_floor']:.3f} kills/effector/day** (kKill_fixed)")
        if cap_hi:
            avail = ode["rate_highT"] / cap_hi
            w()
            w(
                f"ABM fitted capacity: **{cap_hi:.1f} kills/effector/day**; "
                f"ODE rate: **{ode['rate_highT']:.1f}**; model-rate ratio: **{avail:.2f}**. "
                "This ratio does not measure trafficking, tissue availability or "
                "clinical killing capacity; both rates depend on model assumptions."
            )
        w()
        killcurve_svg(
            runs,
            os.path.join(outdir, "abm_crossval_killcurves.svg"),
            "Model comparison: kill curves by condition",
        )
        w("Plot: `abm_crossval_killcurves.svg`.")
        w()

    # ---- caveats ------------------------------------------------------------
    w("## Caveats")
    w()
    w(
        "- 2D culture analog: no ECM, no stroma, no 3D penetration — search is easy in 2D, "
        "these outputs do not establish experimental capacities or upper bounds."
    )
    w("- Tumor cells are static; killing does not depend on tumor motility.")
    w(
        "- One T cell per tumor cell per synapse; no T-T cooperation or competition beyond "
        "target occupancy."
    )
    w(
        "- Fatigue is a phenomenological stand-in for granule depletion / receptor "
        "refractoriness, not a mechanistic model."
    )
    w("- No proliferation on this timescale (6 h); population dynamics stay in the ODE.")
    w()

    rep = os.path.join(outdir, "ABM_REPORT.md")
    with open(rep, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"report : {rep}")
    print(
        f"main   : {r['label']}: {100 * r['frac_killed']:.0f}% killed, "
        f"{r['kills_mean']:.1f} kills/T (max {r['kills_max']}), "
        f"dwell {r['dwell_mean_min'] if r['dwell_mean_min'] else float('nan'):.1f} min, "
        f"D = {r['D_um2_min']:.0f} um^2/min"
    )
    if args.crossval:
        print(
            f"ode    : saturating {ode_reference_rates()['rate_highT']:.1f} kills/effector/day"
            f" vs abm capacity {cap_hi:.0f}/day"
            if cap_hi
            else "ode    : see ABM_REPORT.md"
        )


if __name__ == "__main__":
    main()
