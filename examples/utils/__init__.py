"""
Copyright (c) 2026 MPI-M

----- tuhh_python_for_climate_2026 -----
File: __init__.py
Project: utils
Created Date: Friday 12th February 2026
Author: Angel Peinado Bravo (APB)
Additional Contributors:
-----
Last Modified: Wednesday 11th November 2026
Modified By: APB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
Helpers shared by the notebooks in examples/ (import with `from utils import ...`).
"""

import healpix as hp
import matplotlib.pyplot as plt
import numpy as np

EARTH_SURFACE = 510e6  # km2


def control_freak(factor=1):
    # Fast function to control plot labels text size
    SMALL_SIZE = int(20 * factor)
    MEDIUM_SIZE = int(22 * factor)
    BIGGER_SIZE = int(26 * factor)

    plt.rc("font", size=SMALL_SIZE)  # controls default text sizes
    plt.rc("axes", titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc("axes", labelsize=SMALL_SIZE)  # fontsize of the x and y labels
    plt.rc("xtick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc("ytick", labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc("legend", fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc("figure", titlesize=BIGGER_SIZE)  # fontsize of the figure title
    return [SMALL_SIZE, MEDIUM_SIZE, BIGGER_SIZE]


def print_basic_info_dataset(ds, var=None):
    """Print time range, HEALPix resolution and size in memory of `var` (default "2t")."""
    var = "2t" if var is None else var
    print(
        f"From {str(ds.time.values[0])[:10]} to {str(ds.time.values[-1])[:10]} | ncells {ds.cell.size: .2e} | "
        + f"nside {hp.npix2nside(ds.cell.size)} | "
        + f"Grid area {EARTH_SURFACE / ds.cell.size :.2f} km2 or spacing of about {np.sqrt(EARTH_SURFACE / ds.cell.size): .2f} km"
        + f" | nbytes {ds[var].nbytes * 1e-6: .2f} MBs"
    )


f_mean_average_error = lambda ds, ds_ref: np.linalg.norm(ds - ds_ref, 1) / ds.size

f_intersection = lambda a, b: np.array(list(set(a).intersection(b)))


def get_lon_lat(ds, dim_cell="cell", nest=True):
    """Longitude in [-180, 180) and latitude of every HEALPix cell of `ds`."""
    nside = hp.npix2nside(ds[dim_cell].size)
    lon, lat = hp.pix2ang(nside, np.arange(ds[dim_cell].size), nest=nest, lonlat=True)
    lon = (lon + 180) % 360 - 180
    return lon, lat
