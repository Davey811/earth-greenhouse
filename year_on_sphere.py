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

Prints the mean sunlight on the sphere over the year (compare with the disc formula S/4)
and the mean surface temperature for each case (compare with 255.1 K and with 288 K),
and writes results/year_on_sphere.txt.

Usage:
    python3 year_on_sphere.py            # 1 degree grid, 64,800 points (about a minute)
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

    def sunlight(self, t):
        """Sunlight on each point (W/m2 on the horizontal) at t hours after perihelion."""
        f, dec = orbit(t)
        a = 2 * np.pi * (t % 24) / 24
        cos_h = np.cos(a) * self.cos_lon - np.sin(a) * self.sin_lon
        cz = self.sin_lat * np.sin(dec) + self.cos_lat * np.cos(dec) * cos_h
        return S * f * np.clip(cz, 0, None)

    def annual_sunlight(self, step=1):
        tot = 0.0
        for k in range(0, YEAR_H, step):
            tot = tot + self.sunlight(k + 0.5)
        return tot / len(range(0, YEAR_H, step))


def run_slab(sp, C, spin_years, spin_dt_h):
    """Explicit steps of C dT/dt = absorbed - sigma T^4, from each point's annual equilibrium.
    Spin-up years with steps of spin_dt_h hours, then one recorded year with hourly steps."""
    T = ((1 - ALBEDO) * sp.annual_sunlight(6) / SIGMA) ** 0.25
    t = -spin_years * YEAR_H
    while t < 0:
        T = np.maximum(T + spin_dt_h * 3600 * ((1 - ALBEDO) * sp.sunlight(t + spin_dt_h / 2) - SIGMA * T**4) / C, 0)
        t += spin_dt_h
    total, tmin, tmax = 0.0, 1e9, 0.0
    for k in range(YEAR_H):
        T = np.maximum(T + 3600 * ((1 - ALBEDO) * sp.sunlight(k + 0.5) - SIGMA * T**4) / C, 0)
        total += (sp.w * T).sum()
        tmin, tmax = min(tmin, T.min()), max(tmax, T.max())
    return total / YEAR_H, tmin, tmax


def main():
    deg = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    sp = Sphere(deg)
    mean_sun, mean_t0, tmax0 = 0.0, 0.0, 0.0
    for k in range(YEAR_H):
        I = sp.sunlight(k + 0.5)
        T0 = ((1 - ALBEDO) * I / SIGMA) ** 0.25
        mean_sun += (sp.w * I).sum()
        mean_t0 += (sp.w * T0).sum()
        tmax0 = max(tmax0, T0.max())
    mean_sun /= YEAR_H
    mean_t0 /= YEAR_H
    ceiling = ((1 - ALBEDO) * mean_sun / SIGMA) ** 0.25
    soil = run_slab(sp, CASES["soil"], spin_years=1, spin_dt_h=1)
    ocean = run_slab(sp, CASES["ocean"], spin_years=10, spin_dt_h=3)
    T_inf = ((1 - ALBEDO) * sp.annual_sunlight(1) / SIGMA) ** 0.25
    out = [
        f"the whole integral: {sp.n:,} points ({deg:g} degree grid) x {YEAR_H:,} hours, Earth's orbit and tilt, albedo {ALBEDO}",
        f"  mean sunlight on the sphere over the year: {mean_sun:.3f} W/m2",
        f"  disc formula S/4: {S / 4:.3f} W/m2; with the orbit, S/4/sqrt(1 - e^2): {S / 4 / np.sqrt(1 - ECC**2):.3f} W/m2",
        f"  absorbed: {(1 - ALBEDO) * mean_sun:.2f} W/m2; ceiling for the mean temperature: {ceiling:.2f} K",
        "  mean surface temperature, no infrared absorbers, no heat moved between points:",
        f"    no heat storage            {mean_t0:7.2f} K   (up to {tmax0:.1f} K under the Sun, 0 K at night)",
        f"    half a metre of soil       {soil[0]:7.2f} K   (range {soil[1]:.0f} to {soil[2]:.0f} K)",
        f"    50 m of ocean              {ocean[0]:7.2f} K   (range {ocean[1]:.0f} to {ocean[2]:.0f} K)",
        f"    infinite storage           {(sp.w * T_inf).sum():7.2f} K   (poles {T_inf.min():.0f} K, equator {T_inf.max():.0f} K)",
        f"    perfect mixing, even       {ceiling:7.2f} K",
        "  Earth, measured: 288 K",
    ]
    print("\n".join(out))
    if deg == 1.0:
        os.makedirs(os.path.join(BASE, "results"), exist_ok=True)
        with open(os.path.join(BASE, "results", "year_on_sphere.txt"), "w") as f:
            f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
