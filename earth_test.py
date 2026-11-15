#!/usr/bin/env python3
"""The Earth Test: is Earth's 15 C set by pressure and the lapse rate, or by the greenhouse effect?

Two runs with the same sunlight, the same 1 bar and the same lapse rate:
  1. pressure only        the air doesn't absorb infrared, the surface radiates straight to space
  2. infrared absorbers   Earth radiates to space from the level where the measured profile
                          reaches the emission temperature

Prints the energy ledgers, the compression bill, the middle-of-the-mass rule, the Moon test,
the "dividing by 4" spread and rings, the CO2 doubling numbers, the spectral bands and the Mars test,
and writes results/numbers.txt and results/earth_test.png.

Usage:
    python3 earth_test.py
"""
import csv
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SIGMA = 5.670374419e-8
S, ALBEDO, R_EARTH = 1361.0, 0.294, 6371.0        # NASA Earth Fact Sheet
SUN_AT_SURFACE = 161.0                             # W/m2, Trenberth et al. 2009; Wild et al. 2013
SURFACE_LW, BACK_LW = 396.0, 333.0                 # W/m2, Trenberth et al. 2009
LAPSE = 6.5                                        # K/km, U.S. Standard Atmosphere troposphere
BASE = os.path.dirname(os.path.abspath(__file__))


def load():
    with open(os.path.join(BASE, "data", "earth_us1976.csv")) as f:
        rows = list(csv.DictReader(f))
    return tuple(np.array([float(r[k]) for r in rows]) for k in ("altitude_km", "temperature_K", "pressure_bar"))


def main():
    z, T, p = load()
    absorbed = S * (1 - ALBEDO) / 4
    Te = (absorbed / SIGMA) ** 0.25
    T_em = lambda h: Te * (R_EARTH / (R_EARTH + h)) ** 0.5
    ze = 5.0
    for _ in range(60):
        ze = (T[0] - T_em(ze)) / LAPSE              # emission level on the measured troposphere
    Ts = T_em(ze) + LAPSE * ze
    emit = SIGMA * T[0] ** 4
    ceiling = (S / 4 / SIGMA) ** 0.25

    # half of the mass above: the 1976 troposphere, p/p0 = (T/T0)^(g M / (R L))
    expo = 9.80665 * 0.0289644 / (8.3144598 * LAPSE / 1e3)
    zhalf = (T[0] - T[0] * 0.5 ** (1 / expo)) / LAPSE

    # gravitational energy of the column, integral of p dz
    E = sum((z[i + 1] - z[i]) * 1e3 / np.log(p[i] / p[i + 1]) * (p[i] - p[i + 1]) * 1e5 for i in range(len(z) - 1))
    E += p[-1] * 1e5 * 7e3                          # above 50 km
    bill = emit - SUN_AT_SURFACE
    p0 = p[0] * 1e5

    q_moon = S * (1 - 0.11) / 4

    # dividing by 4: a share s of the sunlight spread evenly, the rest radiated where it falls, no heat stored
    x = (np.arange(200000) + 0.5) / 200000          # share of the surface from the point under the Sun
    spread = []
    for s_ in (0, 0.3, 0.5, 0.9, 1):
        F = (1 - s_) * S * (1 - ALBEDO) * np.clip(1 - 2 * x, 0, None) + s_ * absorbed
        Tx = (F / SIGMA) ** 0.25
        spread.append(f"  {s_:4.0%} spread: average {Tx.mean():6.1f} K, warmest {Tx[0]:5.1f} K, coldest {Tx[-1]:5.1f} K, "
                      f"sent to space {np.mean(SIGMA * Tx ** 4):.1f} W/m2")

    # the sphere from N rings around the Sun-Earth line: light caught = light on the shadow, surface 4 pi R^2 cos(pi/2N)
    rings = []
    for n in (2, 4, 6, 10, 40, 60):
        th = np.arange(n + 1) * np.pi / n
        surf = np.sum((np.sin(th[:-1]) + np.sin(th[1:])) * 2 * np.sin(np.pi / (2 * n)))      # in units of pi R^2
        light = np.sum(np.sin(np.minimum(th[1:], np.pi / 2)) ** 2 - np.sin(np.minimum(th[:-1], np.pi / 2)) ** 2)
        rings.append(f"  {n:2d} rings: light caught {light:.4f} x pi R^2, surface {surf:.3f} x pi R^2 "
                     f"(4 cos(pi/2N) = {4 * np.cos(np.pi / (2 * n)):.3f}), sunlight per m2 {S * (1 - ALBEDO) / surf:.1f} W/m2")

    # CO2: forcing 5.35 ln(C/280) (Myhre et al. 1998); no feedbacks, the column warms by F / (4 sigma Te^3)
    planck = 4 * SIGMA * Te ** 3
    co2 = []
    for c in (420, 560, 1120, 2240):
        F = 5.35 * np.log(c / 280)
        co2.append(f"  {c:5d} ppm: forcing {F:5.2f} W/m2, emission level +{F / planck / LAPSE * 1e3:3.0f} m, "
                   f"surface +{F / planck:.2f} K before feedbacks, {3 * np.log2(c / 280):.1f} K with them (3 K per doubling)")

    # the First Law in time: CO2 doubled at once, no feedbacks, one heat store:
    # the top 100 m of ocean over 71% of the planet
    F2 = 5.35 * np.log(2)
    C = 1025 * 3990 * 100 * 0.71
    YEAR = 3.15576e7
    tau = C / planck / YEAR
    first_law = [f"  heat capacity {C:.3g} J/(m2 K), time constant {tau:.2f} years"]
    for t in (0, 1, 3, 10):
        e = np.exp(-t / tau)
        first_law.append(f"  {t:2d} years: imbalance {F2 * e:.2f} W/m2, surface +{F2 / planck * (1 - e):.2f} K, "
                         f"stored {C * F2 / planck * (1 - e) / 1e6:.0f} MJ/m2")
    area = 4 * np.pi * (R_EARTH * 1e3) ** 2
    first_law.append(f"  measured 0.76 W/m2 (2006-2020) over {area:.4g} m2: {0.76 * area * YEAR / 1e21:.1f} ZJ a year")

    # share of the surface's emission in the window and in the CO2 band, at 288.15 K
    HP, CL, KB = 6.62607015e-34, 2.99792458e8, 1.380649e-23
    lam = np.linspace(0.5, 300, 600000)
    M = 2 * np.pi * HP * CL ** 2 / (lam * 1e-6) ** 5 / (np.exp(HP * CL / (lam * 1e-6 * KB * T[0])) - 1) * 1e-6
    band = lambda a, b: np.trapezoid(M[(lam >= a) & (lam <= b)], lam[(lam >= a) & (lam <= b)]) / (SIGMA * T[0] ** 4)

    # what a satellite sees, schematic: window from the surface, CO2 band from the tropopause (216.65 K),
    # the rest from water vapour at the temperature that makes the total equal to the absorbed sunlight
    def seen_from_space(t_water):
        t_lam = np.where((lam >= 8) & (lam < 13), T[0], np.where((lam >= 13) & (lam <= 17), 216.65, t_water))
        m = 2 * np.pi * HP * CL ** 2 / (lam * 1e-6) ** 5 / (np.exp(HP * CL / (lam * 1e-6 * KB * t_lam)) - 1) * 1e-6
        return np.trapezoid(m, lam)
    lo, hi = 150.0, 350.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if seen_from_space(mid) > absorbed else (mid, hi)
    t_water = (lo + hi) / 2

    # Mars and Venus, NASA NSSDC Fact Sheets: irradiance, Bond albedo, surface pressure (Pa), g, CO2 by volume, molar mass
    planets = {"Mars": (586.2, 0.250, 636.0, 3.73, 0.951, 43.49), "Venus": (2601.3, 0.77, 92e5, 8.87, 0.965, 43.45)}
    co2_earth = p[0] * 1e5 / 9.80665 * 420e-6 * 44.01 / 28.97
    mars = []
    for name, (Sp, Ap, pp, gp, xco2, mm) in planets.items():
        qp = Sp * (1 - Ap) / 4
        col = pp / gp * xco2 * 44.01 / mm
        mars.append(f"  {name:5s}: absorbs {qp:5.1f} W/m2, black body {(qp / SIGMA) ** 0.25:5.1f} K, "
                    f"CO2 above each m2 {col:,.0f} kg ({col / co2_earth:,.0f} x Earth's)")

    out = [
        f"absorbed sunlight (planet average)  {absorbed:6.1f} W/m2, Te = {Te:.2f} K",
        f"emission level                      {ze:6.3f} km, T_em = {T_em(ze):.2f} K (curvature)",
        f"surface, T_em + lapse x z_e         {T_em(ze):.2f} + {LAPSE} x {ze:.3f} = {Ts:.2f} K (measured {T[0]} K)",
        f"ceiling, transparent air, nothing reflected: {ceiling:.1f} K",
        "",
        "pressure only: surface at Te, emits = leaves = absorbed, greenhouse effect 0",
        "infrared absorbers:",
        f"  surface emits sigma T^4 = {emit:.1f} W/m2 (measured {SURFACE_LW:.0f}), leaves {absorbed:.1f}",
        f"  greenhouse effect = {emit - absorbed:.1f} W/m2 (measured {SURFACE_LW - absorbed:.0f})",
        f"  sunlight absorbed by the surface {SUN_AT_SURFACE:.0f}, must come back from the air >= {emit - SUN_AT_SURFACE:.0f} (measured back radiation {BACK_LW:.0f})",
        "",
        "middle-of-the-mass rule:",
        f"  half the mass above {zhalf:.3f} km: {Te:.2f} + {LAPSE} x {zhalf:.3f} = {Te + LAPSE * zhalf:.2f} K, off by {T[0] - (Te + LAPSE * zhalf):+.2f} K",
        "",
        "if compression paid the bill:",
        f"  bill {bill:.0f} W/m2 -> sinking speed {bill / p0 * 1e3:.2f} mm/s = {bill / p0 * 3.156e7 / 1e3:.0f} km/yr",
        f"  gravitational energy {E / 1e6:.0f} MJ/m2, centre of mass {E / p0 / 1e3:.1f} km, lasts {E / bill / 86400:.0f} days",
        "",
        "Moon test:",
        f"  Moon absorbs {q_moon:.1f} W/m2 ({q_moon / absorbed - 1:+.0%} vs Earth), black body {(q_moon / SIGMA) ** 0.25:.1f} K (NASA Moon Fact Sheet: 270.4 K)",
        "",
        f"CO2 above each m2 at 420 ppm: {p0 / 9.80665 * 420e-6 * 44.01 / 28.97:.1f} kg, air {p0 / 9.80665 / 1e3:.1f} t",
        "",
        "dividing by 4: same sunlight, spread more or less evenly, no infrared absorbers:",
        *spread,
        "the sphere built from rings:",
        *rings,
        "",
        "is CO2 saturated?",
        *co2,
        "",
        "the First Law in time (doubling, no feedbacks):",
        *first_law,
        "",
        f"surface emission at {T[0]} K: window 8-13 um {band(8, 13):.1%}, CO2 band 13-17 um {band(13, 17):.1%}",
        f"seen from space (schematic): window at {T[0]} K, CO2 band at 216.65 K, water vapour at {t_water:.1f} K "
        f"-> {seen_from_space(t_water):.1f} W/m2",
        "",
        "Mars test:",
        *mars,
    ]
    print("\n".join(out))
    os.makedirs(os.path.join(BASE, "results"), exist_ok=True)
    with open(os.path.join(BASE, "results", "numbers.txt"), "w") as f:
        f.write("\n".join(out) + "\n")

    BG, FG, DIM = "#0f1419", "#e7e9ea", "#8b98a5"
    plt.rcParams.update({"text.color": FG, "axes.labelcolor": FG, "xtick.color": DIM, "ytick.color": DIM,
                         "axes.edgecolor": DIM, "figure.facecolor": BG, "axes.facecolor": BG, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(8, 6), dpi=160)
    m = z <= 20
    ax.plot(T[m], z[m], color=FG, alpha=0.5, lw=2.4, label="U.S. Standard Atmosphere 1976")
    ax.axvline(Te, color=DIM, ls="--", lw=1)
    ax.text(Te + 1, 19.2, f"Te = {Te:.1f} K", color=DIM, fontsize=9)
    ax.plot([T_em(ze), Ts], [ze, 0], color="#4fd1c5", lw=2.6)
    ax.plot(T_em(ze), ze, "o", color="#4fd1c5", ms=7)
    ax.plot(Ts, 0, "o", color="#4fd1c5", ms=11, clip_on=False, label=f"infrared absorbers: surface {Ts:.0f} K")
    ax.plot(Te, 0, "o", color="#a0aec0", ms=11, clip_on=False, label=f"pressure only: surface {Te:.0f} K")
    ax.set_xlim(200, 330)
    ax.set_ylim(0, 20)
    ax.set_xlabel("temperature (K)")
    ax.set_ylabel("altitude (km)")
    ax.set_title("The Earth Test: same pressure, same lapse rate", loc="left", fontsize=12)
    ax.grid(alpha=0.15)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    fig.text(0.01, 0.01, "Data: U.S. Standard Atmosphere 1976; NASA Earth Fact Sheet; Trenberth et al. 2009   ·   Made with Python by @splugged",
             fontsize=7.5, color=DIM)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    path = os.path.join(BASE, "results", "earth_test.png")
    fig.savefig(path, facecolor=BG)
    print("saved", path)


if __name__ == "__main__":
    main()
