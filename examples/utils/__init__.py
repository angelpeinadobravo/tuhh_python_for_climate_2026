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
import re

import requests

DWD_DAILY = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"
EOBS_CHUNKS = "https://surfobs.climate.copernicus.eu/dataaccess/access_eobs_chunks.php"
FROGS = "https://thredds-x.ipsl.fr/thredds/"


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


def download_file(url, path):
    """Download a large file from `url` piece by piece and save it as `path`; return `path`.

    It is saved under a temporary name (".part") until it is complete, so that an interrupted
    download is never taken for a complete file.
    """
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    part_path = path.with_name(path.name + ".part")
    with requests.get(url, stream=True, timeout=300) as data:
        data.raise_for_status()
        with open(part_path, "wb") as file:
            for piece in data.iter_content(chunk_size=1024 * 1024):
                file.write(piece)
    part_path.rename(path)
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

    # 3. download it (see download_file)
    return download_file(link, folder / link.split("/")[-1])


def download_frogs(product, year, folder="data"):
    """Download one year of daily precipitation of a FROGS product once into `folder`; return the file.

    `product` is the name of a folder of the FROGS server, e.g. "GPCP_CDR_v1.3_yes_enforced",
    "IMERG_V07B_FC" or "ERA5" (all of them: https://thredds-x.ipsl.fr/thredds/catalog/FROGs/catalog.html).
    Every product has one file per year, on the same 1 degree grid; the year is the last number in
    the file name (e.g. GPCP_CDR.1DD.2020.nc or pr_day_1x1_reanalysis_ERA5_20200101-20201231.nc).
    The steps are explained in the notebook class04_get_frogs_data.
    """
    folder = pathlib.Path(folder) / product
    is_year = lambda name: re.findall(r"\d+", name)[-1].startswith(str(year))

    # 1. downloaded before? then there is nothing to do
    found = [path for path in sorted(folder.glob("*.nc")) if is_year(path.name)]
    if found:
        return found[0]

    # 2. the list of files of the product, and the file of this year in it
    catalog = requests.get(f"{FROGS}catalog/FROGs/{product}/catalog.xml", timeout=60)
    if catalog.status_code == 404:
        raise ValueError(
            f"No FROGS product {product!r} on {FROGS}catalog/FROGs/catalog.html"
        )
    catalog.raise_for_status()
    names = [
        part.split("/")[-1]
        for part in catalog.text.split('"')
        if part.startswith(f"FROGs/{product}/") and part.endswith(".nc")
    ]
    names = [name for name in names if is_year(name)]
    if not names:
        raise ValueError(f"No year {year} of FROGS product {product!r}")

    # 3. download it (see download_file)
    url = f"{FROGS}fileServer/FROGs/{product}/{names[0]}"
    return download_file(url, folder / names[0])
