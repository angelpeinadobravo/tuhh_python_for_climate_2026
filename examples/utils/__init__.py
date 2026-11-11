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

import pathlib

import healpix as hp
import matplotlib.pyplot as plt
import numpy as np
import requests

EARTH_SURFACE = 510e6  # km2
DWD_DAILY = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"
EOBS_CHUNKS = "https://surfobs.climate.copernicus.eu/dataaccess/access_eobs_chunks.php"


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


def download_dwd_daily(station_id, folder="data"):
    """Download the daily climate data of a DWD station once into `folder`; return the zip file.

    The file name holds the period of the data (e.g. tageswerte_KL_01975_19360101_20251231_hist.zip),
    which grows every year, so it is looked up in the list of files on the DWD server.
    The steps are explained in the notebook class02_get_station_data.
    """
    station = f"{int(station_id):05d}"  # 1975 -> "01975", as in the file names
    folder = pathlib.Path(folder)

    # 1. downloaded before? then there is nothing to do
    found = sorted(folder.glob(f"tageswerte_KL_{station}_*_hist.zip"))
    if found:
        return found[-1]

    # 2. the list of files on the server, and the name of the file of this station in it
    listing = requests.get(DWD_DAILY, timeout=60)
    listing.raise_for_status()
    names = [
        part
        for part in listing.text.split('"')
        if part.startswith(f"tageswerte_KL_{station}_") and part.endswith("_hist.zip")
    ]
    if not names:
        raise ValueError(f"No daily data of station {station} on {DWD_DAILY}")

    # 3. download the file and save it in the folder
    data = requests.get(DWD_DAILY + names[0], timeout=300)
    data.raise_for_status()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / names[0]
    path.write_bytes(data.content)
    return path


def download_eobs(variable, folder="data"):
    """Download the newest 15-year file of an E-OBS variable (0.25 degree) once into `folder`; return it.

    `variable` is the short name used by E-OBS: "tg" mean temperature, "tn" minimum, "tx" maximum,
    "rr" precipitation, "pp" sea level pressure, "hu" humidity, "fg" wind speed, "qq" radiation.
    The file name holds the version of E-OBS (e.g. tg_ens_mean_0.25deg_reg_2011-2025_v33.0e.nc),
    so it is looked up in the links of the E-OBS download page.
    The steps are explained in the notebook class03_get_gridded_data.
    """
    folder = pathlib.Path(folder)
    start = f"{variable}_ens_mean_0.25deg_reg_"

    # 1. downloaded before? then there is nothing to do
    found = sorted(folder.glob(start + "*.nc"))
    if found:
        return found[-1]

    # 2. the links of the download page, and the newest file of this variable among them
    page = requests.get(EOBS_CHUNKS, timeout=60)
    page.raise_for_status()
    links = [
        part
        for part in page.text.split('"')
        if part.split("/")[-1].startswith(start) and part.endswith(".nc")
    ]
    if not links:
        raise ValueError(f"No E-OBS file of variable {variable!r} on {EOBS_CHUNKS}")
    link = sorted(links)[-1]  # the periods sort in time: the last one is the newest

    # 3. download it piece by piece (it is large), first under a temporary name, so that an
    # interrupted download is never taken for a complete file
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / link.split("/")[-1]
    part_path = path.with_name(path.name + ".part")
    with requests.get(link, stream=True, timeout=300) as data:
        data.raise_for_status()
        with open(part_path, "wb") as file:
            for piece in data.iter_content(chunk_size=1024 * 1024):
                file.write(piece)
    part_path.rename(path)
    return path
