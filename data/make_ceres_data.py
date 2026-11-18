#!/usr/bin/env python3
"""Builds the measured-sunlight files from NASA's CERES EBAF-TOA climatology.

Source: CERES EBAF-TOA Edition 4.2.1, climatological monthly means 07/2005 to 06/2015,
1 x 1 degree grid. DOI 10.5067/TERRA-AQUA-NOAA20/CERES/EBAF-TOA_L3B004.2.1
Download (free): https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA421Selection.jsp
choosing "Climatology", the parameters "Incoming Solar Flux" and "TOA Shortwave Flux, All-Sky",
regional 1 degree grid, NetCDF.

Absorbed sunlight (ASR) in each cell and month = incoming solar - reflected shortwave.

Writes, in this folder:
  ceres_asr_1deg.npz      ASR and incoming solar, 12 months x 180 x 360, in units of 0.05 W/m2
  ceres_asr_2p5deg.bin    ASR on the page's 2.5 degree grid, 12 x 72 x 144, uint16 little-endian,
                          units of 0.05 W/m2, rows from south to north, columns eastward from 0 deg

Usage:
    pip install netCDF4
    python3 data/make_ceres_data.py CERES_EBAF-TOA_Ed4.2.1_Subset_CLIM01-CLIM12.nc
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SCALE = 20  # stored values are W/m2 x 20, i.e. steps of 0.05 W/m2


def band_weights(edges_deg):
    s = np.sin(np.radians(edges_deg))
    return s[1:] - s[:-1]


def regrid_1_to_2p5(a):
    """Area-conserving regrid of (12, 180, 360) at 1 degree to (12, 72, 144) at 2.5 degrees."""
    fine = np.repeat(np.repeat(a, 2, axis=1), 2, axis=2)               # 0.5 degree copies
    w = band_weights(np.arange(-90, 90.25, 0.5))[None, :, None]          # area of each 0.5 degree row
    num = (fine * w).reshape(12, 72, 5, 144, 5).sum(axis=(2, 4))
    den = (np.broadcast_to(w, fine.shape)).reshape(12, 72, 5, 144, 5).sum(axis=(2, 4))
    return num / den


def main():
    import netCDF4
    d = netCDF4.Dataset(sys.argv[1])
    lat, lon = d["lat"][:].data, d["lon"][:].data
    assert lat[0] == -89.5 and lon[0] == 0.5 and d["solar_clim"].shape == (12, 180, 360)
    solar = d["solar_clim"][:].data.astype(np.float64)
    asr = solar - d["toa_sw_all_clim"][:].data.astype(np.float64)
    asr = np.clip(asr, 0, None)
    q = lambda x: np.round(x * SCALE).astype(np.uint16)
    np.savez_compressed(os.path.join(HERE, "ceres_asr_1deg.npz"), asr_x20=q(asr), solar_x20=q(solar),
                        source=np.array(f"CERES EBAF-TOA {d.version}; {d.comment}; DOI {d.DOI}"))
    q(regrid_1_to_2p5(asr)).astype("<u2").tofile(os.path.join(HERE, "ceres_asr_2p5deg.bin"))
    w = band_weights(np.arange(-90, 91, 1.0))
    w = (w / w.sum() / 360)[None, :, None]
    print(f"written; global annual mean: incoming {(solar * w).sum(axis=(1, 2)).mean():.2f} W/m2, "
          f"absorbed {(asr * w).sum(axis=(1, 2)).mean():.2f} W/m2 (months weighted equally)")


if __name__ == "__main__":
    main()
