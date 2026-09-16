#!/usr/bin/env python3
"""Pure-Python SVG line-plot generator (no external dependencies).

Minimal but clean: axes, ticks, grid, legend, optional log-y, multiple series.
Used by the CAR-T E2E simulator to render trajectory plots without matplotlib.
"""

import math
from html import escape

PALETTE = [
    "#1f77b4",
    "#d62728",
    "#2ca02c",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#17becf",
    "#bcbd22",
    "#7f7f7f",
]


class PlotSVG:
    def __init__(self, width=720, height=420, title="", ylab="", xlab="time (days)"):
        self.W = width
        self.H = height
        self.m = dict(l=62, r=16, t=40, b=48)
        self.title = title
        self.ylab = ylab
        self.xlab = xlab
        self.series = []  # (name, color, [(x, y), ...], log)
        self.ymin = None
        self.ymax = None
        self.xmin = None
        self.xmax = None
        self.logy = False

    def add(self, name, data, color=None, log=False):
        data = [
            (x, y) for (x, y) in data if y is not None and math.isfinite(x) and math.isfinite(y)
        ]
        if not data:
            return
        if self.xmin is None:
            self.xmin = min(x for x, _ in data)
            self.xmax = max(x for x, _ in data)
        else:
            self.xmin = min(self.xmin, min(x for x, _ in data))
            self.xmax = max(self.xmax, max(x for x, _ in data))
        self.logy = self.logy or log
        self.series.append((name, color or PALETTE[len(self.series) % len(PALETTE)], data, log))

    def _ylim(self):
        if self.ymin is not None and self.ymax is not None:
            return self.ymin, self.ymax
        ys = [y for s in self.series for (_, y) in s[2]]
        if not ys:
            return 0.0, 1.0
        lo = min(ys)
        hi = max(ys)
        if lo == hi:
            lo, hi = lo - 1, hi + 1
        return lo, hi

    def render(self):
        W, H, m = self.W, self.H, self.m
        pw = W - m["l"] - m["r"]
        ph = H - m["t"] - m["b"]

        def sx(x):
            if self.xmin is None:
                return m["l"]
            if self.xmax == self.xmin:
                return m["l"] + pw / 2
            return m["l"] + pw * (x - self.xmin) / (self.xmax - self.xmin)

        # y transform (per-series log handled at tick level; use global logy flag)
        glo_log = self.logy
        lo, hi = self._ylim()
        if glo_log:
            lo = lo if lo > 0 else 1e-3
            hi = hi if hi > 0 else 1e3
            if hi <= lo:
                hi = lo * 10
            loglo, loghi = math.log10(lo), math.log10(hi)
        else:
            loglo, loghi = None, None

        def sy(y, log=glo_log):
            if log:
                if y <= 0:
                    y = lo * 0.5
                vv = math.log10(max(y, 1e-12))
                frac = (vv - loglo) / (loghi - loglo)
            else:
                frac = (y - lo) / (hi - lo)
            frac = max(0.0, min(1.0, frac))
            return m["t"] + ph * (1 - frac)

        o = []
        o.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'font-family="Segoe UI, Arial, sans-serif">'
        )
        o.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
        # plot frame
        o.append(
            f'<rect x="{m["l"]}" y="{m["t"]}" width="{pw}" height="{ph}" '
            f'fill="#fbfbfd" stroke="#cccccc" stroke-width="1"/>'
        )

        # x ticks
        nx = 6
        if self.xmin is not None:
            for i in range(nx + 1):
                x = self.xmin + (self.xmax - self.xmin) * i / nx
                px = sx(x)
                o.append(
                    f'<line x1="{px:.1f}" y1="{m["t"] + ph}" x2="{px:.1f}" '
                    f'y2="{m["t"] + ph + 4}" stroke="#999"/>'
                )
                o.append(
                    f'<text x="{px:.1f}" y="{m["t"] + ph + 18}" font-size="11" '
                    f'text-anchor="middle" fill="#333">{_fmt(x)}</text>'
                )

        # y ticks
        ny = 5
        if glo_log:
            span = loghi - loglo
            for i in range(ny + 1):
                lv = loglo + span * i / ny
                val = 10**lv
                py = sy(val)
                o.append(
                    f'<line x1="{m["l"] - 4}" y1="{py:.1f}" x2="{m["l"]}" '
                    f'y2="{py:.1f}" stroke="#999"/>'
                )
                o.append(
                    f'<line x1="{m["l"]}" y1="{py:.1f}" x2="{m["l"] + pw}" '
                    f'y2="{py:.1f}" stroke="#eeeeee"/>'
                )
                o.append(
                    f'<text x="{m["l"] - 6}" y="{py + 4:.1f}" font-size="11" '
                    f'text-anchor="end" fill="#333">{_sci(val)}</text>'
                )
        else:
            for i in range(ny + 1):
                val = lo + (hi - lo) * i / ny
                py = sy(val)
                o.append(
                    f'<line x1="{m["l"] - 4}" y1="{py:.1f}" x2="{m["l"]}" '
                    f'y2="{py:.1f}" stroke="#999"/>'
                )
                o.append(
                    f'<line x1="{m["l"]}" y1="{py:.1f}" x2="{m["l"] + pw}" '
                    f'y2="{py:.1f}" stroke="#eeeeee"/>'
                )
                o.append(
                    f'<text x="{m["l"] - 6}" y="{py + 4:.1f}" font-size="11" '
                    f'text-anchor="end" fill="#333">{_fmt(val)}</text>'
                )

        # series
        for name, color, data, log in self.series:
            pts = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in data)
            o.append(f'<polyline fill="none" stroke="{color}" stroke-width="1.8" points="{pts}"/>')

        # legend
        lx, ly = m["l"] + 8, m["t"] + 8
        for name, color, data, log in self.series:
            o.append(f'<rect x="{lx}" y="{ly - 9}" width="18" height="3" fill="{color}"/>')
            o.append(
                f'<text x="{lx + 22}" y="{ly - 3}" font-size="11" fill="#222">{escape(name)}</text>'
            )
            ly += 16

        # labels
        if self.title:
            o.append(
                f'<text x="{W / 2}" y="20" font-size="15" font-weight="600" '
                f'text-anchor="middle" fill="#111">{escape(self.title)}</text>'
            )
        if self.xlab:
            o.append(
                f'<text x="{m["l"] + pw / 2}" y="{H - 8}" font-size="12" '
                f'text-anchor="middle" fill="#333">{escape(self.xlab)}</text>'
            )
        if self.ylab:
            o.append(
                f'<text x="14" y="{m["t"] + ph / 2}" font-size="12" fill="#333" '
                f'transform="rotate(-90 14 {m["t"] + ph / 2})" text-anchor="middle">{escape(self.ylab)}</text>'
            )
        o.append("</svg>")
        return "\n".join(o)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.render())
        return path


def _fmt(v):
    if abs(v) >= 1e6:
        return f"{v / 1e6:.0f}e6"
    if abs(v) >= 1e4:
        return f"{v:.0f}"
    if v == 0:
        return "0"
    if abs(v) < 1e-3:
        return f"{v:.1e}"
    return f"{v:.3g}"


def _sci(v):
    if v >= 1e6:
        return f"{v:.0e}"
    if v >= 1e4:
        return f"{v:.0e}"
    if v >= 100:
        return f"{v:.0f}"
    if v >= 1:
        return f"{v:.1f}"
    return f"{v:.2f}"
