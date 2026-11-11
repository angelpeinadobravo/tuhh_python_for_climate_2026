# 00 · Accessing climate data

Python for Climate Science · TUHH

<small>MPI-M · notebook `examples/00_intake_catalog.ipynb`</small>

---

## Today

1. Open data from an online **catalog**
2. Read an `xarray.Dataset`
3. The **HEALPix** grid and its zoom levels
4. **netCDF** files and lon-lat grids
5. A **quick plot**

---

## Catalogs with intake

```python
import intake

cat = intake.open_catalog("https://data.nextgems-h2020.eu/online.yaml")
print(list(cat))                       # one entry per simulation
ds = cat["ERA5"](zoom=0).to_dask()     # ERA5 on HEALPix zoom 0
```

The dataset is **lazy**: nothing is downloaded until you `.load()`, `.compute()` or plot.

Note: Show `pd.DataFrame(cat["ERA5"].describe()["user_parameters"])` to see the zoom levels.

---

## What is in a Dataset?

- **Dimensions**: `time`, `cell`, `level`
- **Coordinates**: the values along the dimensions
- **Data variables**: `2t`, `tp`, `sp`, ...
- **Attributes**: units and names, `ds["2t"].attrs`

Check the units before you compute anything.

---

## The HEALPix grid

Equal-area cells in a hierarchy: every zoom level splits each cell in four.

| zoom $z$ | nside $= 2^z$ | cells $= 12 \cdot 4^z$ | spacing |
|---:|---:|---:|---:|
| 0 | 1 | 12 | ~6500 km |
| 3 | 8 | 768 | ~815 km |
| 6 | 64 | 49 152 | ~100 km |
| 8 | 256 | 786 432 | ~25 km |

<small>Spacing: square root of the Earth surface (510 million km²) divided by the number of cells.</small>

---

## netCDF files

```python
import xarray as xr

ds_z8 = xr.open_dataset("era5_t2m_2020_monthly_mean_z8.nc", chunks={"time": 1})
ds_ll = xr.open_dataset("era5_t2m_2020_monthly_mean_lonlat.nc", chunks={"time": 1})
```

- HEALPix: one dimension, `cell`, all cells with the same area
- lon-lat: two dimensions, `lon` and `lat`; cells shrink towards the poles

---

## A quick plot

```python
ds_ll.T2M.mean("time").plot()            # lon-lat: xarray plots it directly

import easygems.healpix as egh
egh.healpix_show(ds_z8.T2M.mean("time")) # HEALPix: easygems
```

---

## Exercises

1. **Understanding the dataset**: units and short names of temperature, 100 m wind, precipitation, SST and solar radiation, in ERA5 and ICON `ngc4008`
2. **Three zoom levels**: 1990–1994 mean temperature at zoom 0, 3 and 6, side by side, EqualEarth projection
3. **Two grids**: the same for the 2020 netCDF files

<small>Then add your lessons learned to the webpage.</small>

---

# Questions?
