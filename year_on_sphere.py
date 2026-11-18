#!/usr/bin/env python3
"""The whole integral: sunlight on the sphere, point by point, hour by hour, for a year.

Earth's orbit (eccentricity 0.0167, perihelion in early January) and tilt (23.44 deg),
albedo 0.294, emissivity 1, no infrared absorbers: every point radiates sigma T^4
straight to space. Nothing moves heat between points; each point stores heat according
to its heat capacity per square metre:

  none      no storage: each point radiates, instant by instant, what it absorbs
  soil      1e6 J/(m2 K), about half a metre of soil
  ocean     2.09e8 J/(m2 K), a 50 m layer of water
  infinite  each point sits at the temperature of its own annual mean sunlight
  mixed     perfect mixing: one temperature everywhere, all year (the even planet)

Everything runs twice: once with the same 29.4% reflected everywhere, once with the sunlight
each cell really absorbs, as NASA's CERES satellites measure it month by month (EBAF-TOA
Ed4.2.1 climatology, 1 degree grid, see data/make_ceres_data.py). In that second run each cell
absorbs, hour by hour, the model's sunlight scaled so that its monthly total is the measured one.

Prints the mean sunlight on the sphere over the year (compare with the disc formula S/4)
and the mean surface temperature for each case (compare with the ceiling and with 288 K),
and writes results/year_on_sphere.txt.

Usage:
    python3 year_on_sphere.py            # 1 degree grid, 64,800 points (about two minutes)
    python3 year_on_sphere.py 2.5        # the page's grid, 10,368 points
"""
import os
import sys

import numpy as np

SIGMA = 5.670374419e-8
S, ALBEDO = 1361.0, 0.294                  # NASA Earth Fact Sheet
ECC, OBLIQ = 0.0167, np.radians(23.44)
LON_PERI = np.radians(282.9)               # longitude of perihelion, from the March equinox
YEAR_H = 8766                              # hours in a year, 365.25 days
CASES = {"soil": 1.0e6, "ocean": 1000 * 4180 * 50.0}
BASE = os.path.dirname(os.path.abspath(__file__))
MONTH_EDGES = np.array([0, 31, 59.25, 90.25, 120.25, 151.25, 181.25, 212.25, 243.25, 273.25, 304.25, 334.25, 365.25])
MONTH_DAYS = np.diff(MONTH_EDGES)


def month_of(t):
    """Calendar month (0 = January) t hours after perihelion, which falls on 3 January."""
    return int(np.searchsorted(MONTH_EDGES, (2 + t / 24) % 365.25, side="right") - 1)


def orbit(t):
    """(a/r)^2 and the Sun's declination, t hours after perihelion."""
    M = 2 * np.pi * t / YEAR_H
    E = M
    for _ in range(8):
        E = E - (E - ECC * np.sin(E) - M) / (1 - ECC * np.cos(E))
    nu = 2 * np.arctan2(np.sqrt(1 + ECC) * np.sin(E / 2), np.sqrt(1 - ECC) * np.cos(E / 2))
    r = 1 - ECC * np.cos(E)
    return 1 / r**2, np.arcsin(np.sin(OBLIQ) * np.sin(nu + LON_PERI))


class Sphere:
    def __init__(self, deg):
        lat = np.radians(np.arange(-90 + deg / 2, 90, deg))
        lon = np.radians(np.arange(deg / 2, 360, deg))
        self.sin_lat, self.cos_lat = np.sin(lat)[:, None], np.cos(lat)[:, None]
        self.cos_lon, self.sin_lon = np.cos(lon)[None, :], np.sin(lon)[None, :]
        w = np.repeat(np.cos(lat)[:, None], lon.size, axis=1)
        self.w = w / w.sum()
        self.n = w.size
        self.eq = np.abs(np.degrees(lat)) < 0.75 * deg       # the two rows either side of the equator

    def sunlight(self, t):
        """Sunlight on each point (W/m2 on the horizontal) at t hours after perihelion."""
        f, dec = orbit(t)
        a = 2 * np.pi * (t % 24) / 24
        cos_h = np.cos(a) * self.cos_lon - np.sin(a) * self.sin_lon
        cz = self.sin_lat * np.sin(dec) + self.cos_lat * np.cos(dec) * cos_h
        return S * f * np.clip(cz, 0, None)

    def absorbed(self, t):
        """Sunlight absorbed by each point: 70.6% everywhere, or scaled to the CERES monthly totals."""
        I = self.sunlight(t)
        if not hasattr(self, "F"):
            return (1 - ALBEDO) * I
        m = month_of(t)
        return self.F[m] * I + self.U[m]

    def annual_absorbed(self, step=1):
        tot = 0.0
        for k in range(0, YEAR_H, step):
            tot = tot + self.absorbed(k + 0.5)
        return tot / len(range(0, YEAR_H, step))

    def use_ceres(self, deg):
        """Load the measured absorbed sunlight (W/m2, 12 months) and turn it into hourly factors."""
        if deg == 1.0:
            z = np.load(os.path.join(BASE, "data", "ceres_asr_1deg.npz"))
            asr, self.solar_ceres = z["asr_x20"] / 20.0, z["solar_x20"] / 20.0
        elif deg == 2.5:
            asr = np.fromfile(os.path.join(BASE, "data", "ceres_asr_2p5deg.bin"), "<u2").reshape(12, 72, 144) / 20.0
        else:
            sys.exit("the CERES run needs the 1 or the 2.5 degree grid")
        Isum, n = np.zeros(asr.shape), np.zeros(12)
        for k in range(YEAR_H):
            m = month_of(k + 0.5)
            Isum[m] += self.sunlight(k + 0.5)
            n[m] += 1
        Imean = Isum / n[:, None, None]
        lit = Imean > 0.5           # where the model's month is dark but CERES saw a little light, spread it evenly
        self.F = np.where(lit, asr / np.where(lit, Imean, 1), 0.0)
        self.U = np.where(lit, 0.0, asr)
        self.asr_ceres = asr


def run_slab(sp, C, spin_years, spin_dt_h):
    """Explicit steps of C dT/dt = absorbed - sigma T^4, from each point's annual equilibrium.
    Spin-up years with steps of spin_dt_h hours, then one recorded year with hourly steps."""
    T = (sp.annual_absorbed(6) / SIGMA) ** 0.25
    t = -spin_years * YEAR_H
    while t < 0:
        T = np.maximum(T + spin_dt_h * 3600 * (sp.absorbed(t + spin_dt_h / 2) - SIGMA * T**4) / C, 0)
        t += spin_dt_h
    total, tmin, tmax, eq_sum, eq_max = 0.0, 1e9, 0.0, 0.0, 0.0
    for k in range(YEAR_H):
        T = np.maximum(T + 3600 * (sp.absorbed(k + 0.5) - SIGMA * T**4) / C, 0)
        total += (sp.w * T).sum()
        tmin, tmax = min(tmin, T.min()), max(tmax, T.max())
        eq_sum += T[sp.eq].mean()
        eq_max = max(eq_max, T[sp.eq].max())
    return total / YEAR_H, tmin, tmax, eq_max, eq_sum / YEAR_H


def cases(sp):
    mean_sun, mean_abs, mean_t0, tmax0, eq_sum, eq_max = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    for k in range(YEAR_H):
        I, ab = sp.sunlight(k + 0.5), sp.absorbed(k + 0.5)
        T0 = (ab / SIGMA) ** 0.25
        mean_sun += (sp.w * I).sum()
        mean_abs += (sp.w * ab).sum()
        mean_t0 += (sp.w * T0).sum()
        tmax0 = max(tmax0, T0.max())
        eq_sum += T0[sp.eq].mean()
        eq_max = max(eq_max, T0[sp.eq].max())
    mean_sun, mean_abs, mean_t0 = mean_sun / YEAR_H, mean_abs / YEAR_H, mean_t0 / YEAR_H
    T_inf = (sp.annual_absorbed(1) / SIGMA) ** 0.25
    return dict(sun=mean_sun, absorbed=mean_abs, ceiling=(mean_abs / SIGMA) ** 0.25, none=mean_t0, tmax0=tmax0,
                none_eq=(eq_max, eq_sum / YEAR_H),
                soil=run_slab(sp, CASES["soil"], spin_years=1, spin_dt_h=1),
                ocean=run_slab(sp, CASES["ocean"], spin_years=10, spin_dt_h=3),
                inf=(sp.w * T_inf).sum(), inf_min=T_inf.min(), inf_max=T_inf.max(),
                inf_eq=(T_inf[sp.eq].max(), T_inf[sp.eq].mean()))


def report(r):
    return [
        f"  absorbed: {r['absorbed']:.2f} W/m2; ceiling for the mean temperature: {r['ceiling']:.2f} K",
        "  mean surface temperature, no infrared absorbers, no heat moved between points:",
        f"    no heat storage            {r['none']:7.2f} K   (up to {r['tmax0']:.1f} K under the Sun, 0 K at night)",
        f"    half a metre of soil       {r['soil'][0]:7.2f} K   (range {r['soil'][1]:.0f} to {r['soil'][2]:.0f} K)",
        f"    50 m of ocean              {r['ocean'][0]:7.2f} K   (range {r['ocean'][1]:.0f} to {r['ocean'][2]:.0f} K)",
        f"    infinite storage           {r['inf']:7.2f} K   (coldest point {r['inf_min']:.0f} K, warmest {r['inf_max']:.0f} K)",
        f"    perfect mixing, even       {r['ceiling']:7.2f} K",
        "  at the equator (warmest moment / average over the year):",
        f"    no heat storage            {r['none_eq'][0]:7.1f} K / {r['none_eq'][1]:5.1f} K",
        f"    half a metre of soil       {r['soil'][3]:7.1f} K / {r['soil'][4]:5.1f} K",
        f"    50 m of ocean              {r['ocean'][3]:7.1f} K / {r['ocean'][4]:5.1f} K",
        f"    infinite storage           {r['inf_eq'][0]:7.1f} K / {r['inf_eq'][1]:5.1f} K",
    ]


def main():
    deg = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    sp = Sphere(deg)
    u = cases(sp)
    out = [
        f"the whole integral: {sp.n:,} points ({deg:g} degree grid) x {YEAR_H:,} hours, Earth's orbit and tilt",
        f"  mean sunlight on the sphere over the year: {u['sun']:.3f} W/m2",
        f"  disc formula S/4: {S / 4:.3f} W/m2; with the orbit, S/4/sqrt(1 - e^2): {S / 4 / np.sqrt(1 - ECC**2):.3f} W/m2",
        "",
        f"1) the same albedo everywhere, {ALBEDO}",
    ] + report(u)
    sp.use_ceres(deg)
    c = cases(sp)
    days = MONTH_DAYS / MONTH_DAYS.sum()
    ws = sp.w[None]
    out += [
        "",
        "2) the sunlight each cell absorbs, measured by CERES (EBAF-TOA Ed4.2.1, monthly climatology 07/2005-06/2015)",
        f"  measured absorbed sunlight, global mean: {((sp.asr_ceres * ws).sum(axis=(1, 2)) * days).sum():.2f} W/m2"
        + (f"; measured incoming: {((sp.solar_ceres * ws).sum(axis=(1, 2)) * days).sum():.2f} W/m2" if hasattr(sp, "solar_ceres") else ""),
    ] + report(c) + ["", "Earth, measured: 288 K"]
    print("\n".join(out))
    if deg == 1.0:
        os.makedirs(os.path.join(BASE, "results"), exist_ok=True)
        with open(os.path.join(BASE, "results", "year_on_sphere.txt"), "w") as f:
            f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
