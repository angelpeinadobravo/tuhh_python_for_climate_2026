"""
Copyright (c) 2026 MPI-M

----- tuhh_python_for_climate_2026 -----
File: test_examples.py
Project: tests
Created Date: Wednesday 11th November 2026
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
Checks run by the CI: the notebooks under examples/ must be valid Jupyter
notebooks and the helpers in examples/utils must work on a HEALPix grid.
"""

import importlib.util
import json
import pathlib
import sys

import numpy as np
import pytest
import xarray as xr

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))

import utils  # noqa: E402

NOTEBOOKS = sorted((ROOT / "examples").glob("*.ipynb"))


@pytest.mark.parametrize("notebook", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_is_valid_json(notebook):
    with open(notebook, encoding="utf-8") as f:
        content = json.load(f)
    assert isinstance(content.get("cells"), list)


def test_get_lon_lat_zoom_1():
    ds = xr.Dataset({"2t": ("cell", np.zeros(48))})  # zoom 1: 12 * 4 cells
    lon, lat = utils.get_lon_lat(ds)
    assert lon.shape == lat.shape == (48,)
    assert np.all((lon >= -180) & (lon < 180))
    assert np.all(np.abs(lat) < 90)
    assert np.isclose(lat.mean(), 0)  # cells are symmetric around the equator


def test_set_helpers_and_error():
    assert sorted(utils.f_intersection([1, 2, 3], [2, 3, 4])) == [2, 3]
    assert utils.f_mean_average_error(np.array([1.0, 3.0]), np.array([0.0, 0.0])) == 2.0


def test_student_pages_start_from_templates(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("conf", ROOT / "docs/source/conf.py")
    conf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(conf)
    template = tmp_path / "docs/source/classes/01_setup/template"
    template.mkdir(parents=True)
    (template / "my_page.rst").write_text("template")
    (template / "my_region.png").write_text("picture")
    pages = tmp_path / "pages"
    (pages / "01_setup").mkdir(parents=True)
    (pages / "01_setup/my_region.png").write_text("the student's own picture")
    monkeypatch.setattr(conf, "ROOT", tmp_path)
    monkeypatch.setattr(conf, "STUDENT_PAGES", pages)

    conf._student_pages(None, None)

    assert (pages / "01_setup/my_page.rst").read_text() == "template"
    assert (pages / "01_setup/my_region.png").read_text() == "the student's own picture"
    copy = tmp_path / "docs/source/my_pages/01_setup"
    assert (copy / "my_region.png").read_text() == "the student's own picture"


def test_download_dwd_daily_finds_file_and_downloads_once(tmp_path, monkeypatch):
    calls = []

    class Response:
        def __init__(self, text="", content=b""):
            self.text, self.content = text, content

        def raise_for_status(self):
            pass

    def fake_get(url, timeout):
        calls.append(url)
        if url == utils.DWD_DAILY:
            return Response(
                text='<a href="tageswerte_KL_01975_19360101_20251231_hist.zip">'
            )
        return Response(content=b"zip")

    monkeypatch.setattr(utils.requests, "get", fake_get)

    path = utils.download_dwd_daily(1975, tmp_path / "data")
    again = utils.download_dwd_daily("01975", tmp_path / "data")

    assert path.name == "tageswerte_KL_01975_19360101_20251231_hist.zip"
    assert path.read_bytes() == b"zip" and again == path
    assert len(calls) == 2  # listing + file, nothing the second time
    with pytest.raises(ValueError):
        utils.download_dwd_daily(433, tmp_path / "data")


def test_download_eobs_takes_newest_file_once(tmp_path, monkeypatch):
    base = "https://example.org/Grid_0.25deg_reg_ensemble/"
    page = "".join(
        f'<a href="{base}{name}">'
        for name in [
            "tg_ens_mean_0.25deg_reg_1995-2010_v33.0e.nc",
            "tg_ens_mean_0.25deg_reg_2011-2025_v33.0e.nc",
            "tg_ens_spread_0.25deg_reg_2011-2025_v33.0e.nc",
            "tg_ens_mean_0.1deg_reg_2011-2025_v33.0e.nc",
        ]
    )
    calls = []

    class Response:
        def __init__(self, text=""):
            self.text = text

        def raise_for_status(self):
            pass

        def iter_content(self, chunk_size):
            yield b"net"
            yield b"cdf"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    def fake_get(url, timeout, stream=False):
        calls.append(url)
        return Response(text=page if url == utils.EOBS_CHUNKS else "")

    monkeypatch.setattr(utils.requests, "get", fake_get)

    path = utils.download_eobs("tg", tmp_path / "data")
    again = utils.download_eobs("tg", tmp_path / "data")

    assert path.name == "tg_ens_mean_0.25deg_reg_2011-2025_v33.0e.nc"
    assert path.read_bytes() == b"netcdf" and again == path
    assert not list((tmp_path / "data").glob("*.part"))
    assert calls == [utils.EOBS_CHUNKS, base + path.name]
    with pytest.raises(ValueError):
        utils.download_eobs("xx", tmp_path / "data")


def test_download_frogs_finds_year_in_catalog(tmp_path, monkeypatch):
    names = {
        "ERA5": [
            "pr_day_1x1_reanalysis_ERA5_20190101-20191231.nc",
            "pr_day_1x1_reanalysis_ERA5_20200101-20201231.nc",
        ],
        "GPCC_FDD_v2022": [
            "full_data_daily_v2022_10_2020.nc",
            "full_data_daily_v2022_10_2021.nc",
        ],
    }
    calls = []

    class Response:
        def __init__(self, text="", status_code=200):
            self.text, self.status_code = text, status_code

        def raise_for_status(self):
            pass

        def iter_content(self, chunk_size):
            yield b"rain"

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    def fake_get(url, timeout, stream=False):
        calls.append(url)
        for product, files in names.items():
            if url.endswith(f"/FROGs/{product}/catalog.xml"):
                return Response(
                    "".join(f'<dataset urlPath="FROGs/{product}/{n}">' for n in files)
                )
        return Response(status_code=404) if url.endswith("catalog.xml") else Response()

    monkeypatch.setattr(utils.requests, "get", fake_get)

    era5 = utils.download_frogs("ERA5", 2020, tmp_path / "data")
    gpcc = utils.download_frogs("GPCC_FDD_v2022", 2021, tmp_path / "data")
    utils.download_frogs("ERA5", 2020, tmp_path / "data")

    assert (
        era5 == tmp_path / "data/ERA5/pr_day_1x1_reanalysis_ERA5_20200101-20201231.nc"
    )
    assert gpcc.name == "full_data_daily_v2022_10_2021.nc"  # not fooled by v2022
    assert era5.read_bytes() == b"rain"
    assert len(calls) == 4  # catalog + file, twice; nothing for the third call
    with pytest.raises(ValueError):
        utils.download_frogs("ERA5", 1950, tmp_path / "data")
    with pytest.raises(ValueError):
        utils.download_frogs("NOPE", 2020, tmp_path / "data")


@pytest.mark.parametrize(
    "template",
    sorted((ROOT / "docs/source/classes").glob("*/template/my_page.rst")),
    ids=lambda p: p.parts[-3],
)
def test_template_pictures_exist(template):
    # Sphinx notices a student's new plot only if a picture of that name existed when the
    # page was first built, so every figure of a template needs a picture in the template
    for line in template.read_text().splitlines():
        if line.startswith(".. figure::"):
            assert (template.parent / line.split("::")[1].strip()).exists(), line
