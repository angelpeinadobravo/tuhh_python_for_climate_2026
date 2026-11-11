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
