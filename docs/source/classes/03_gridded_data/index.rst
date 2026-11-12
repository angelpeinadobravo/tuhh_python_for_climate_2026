.. _class_03:

03 · Climate data - lon-lat grid, when been square is fine
================================================================================

Slides: `03 · Climate data in NetCDF - lon-lat grid <../../slides/deck.html?md=class03_gridded_data.md>`_
· Notebooks: ``notebooks/lessons/class03_get_gridded_data.ipynb`` and ``class03_use_gridded_data.ipynb``

In class 02 a station gave you the weather at one place. In this class you use **gridded data**, values on
a grid of cells that covers all of Europe, to draw maps and to compute the temperature of Europe.

What you learn
--------------

- What a lon-lat grid is, and what E-OBS is: European station data spread onto a grid :cite:`Cornes_2018`.
- How to download a large file, and what is inside a **netCDF** file: dimensions, coordinates, variables, attributes.
- How to select days, months, years and places with ``xarray``, and draw maps with ``cartopy``.
- Why a mean over a lon-lat grid needs **weights**, and how to compute one.

1. The data
-----------

`E-OBS <https://surfobs.climate.copernicus.eu/dataaccess/access_eobs_chunks.php>`_ has one netCDF file per
variable, grid size and period of 15 years, e.g. ``tg_ens_mean_0.25deg_reg_2011-2025_v33.0e.nc``. In this class:

.. list-table::
   :header-rows: 1
   :widths: 15 45 15 25

   * - Name
     - Variable
     - Unit
     - In this class
   * - ``tg``
     - daily mean temperature
     - °C
     - example
   * - ``rr``
     - daily precipitation
     - mm
     - exercise

Both on the 0.25° grid, 2011–2025: about 165 MB and 140 MB. The grid has 201 latitudes (25°N–75°N) and
464 longitudes (40°W–75°E), land only.

E-OBS is free for non-commercial research and education. Whenever you publish something made with it,
include the acknowledgement asked for on the E-OBS page: *"We acknowledge the E-OBS dataset from the EU-FP6
project UERRA (https://www.uerra.eu) and the Copernicus Climate Change Service, and the data providers in the
ECA&D project (https://www.ecad.eu)"*, and cite :cite:`Cornes_2018`.

2. The notebooks
----------------

Open them in JupyterLab (``notebooks`` → ``lessons``) and run them from top to bottom, in this order:

#. ``class03_get_gridded_data.ipynb``: what a grid and E-OBS are, where the files are, downloading with the
   function ``download_eobs``, and what is inside a netCDF file.
#. ``class03_use_gridded_data.ipynb``: selecting, a map of one month, a map of one year, and the
   temperature of Europe as a time series.

The files are downloaded once into ``notebooks/lessons/data/``. The first time it takes a few minutes.

The xarray you need, in short:

.. code-block:: python

   ds = xr.open_dataset(file, chunks={"time": 31})   # open, reading 31 days at a time
   tg = ds["tg"]                                      # one variable
   tg.sel(time="2025-07")                             # a month; also a day "2025-07-15" or a year "2024"
   tg.sel(latitude=53.55, longitude=10.0, method="nearest")       # the cell of a place
   tg.sel(latitude=slice(35, 72), longitude=slice(-25, 45))       # a region
   tg.sel(time="2025-07").mean("time")                # a map: the mean over the days
   weights = np.cos(np.deg2rad(tg.latitude))
   tg.weighted(weights).mean(("latitude", "longitude"))           # one value per day, weighted by area

3. Why weights?
---------------

Every cell spans 0.25° of longitude, but the lines of longitude come closer towards the pole: a cell is
22.8 km wide at 35°N and only 9.5 km at 70°N. Its area is proportional to the cosine of its latitude. A plain
mean counts the small northern cells as much as the large southern ones: for Europe in 2011–2025 it is almost
1 °C colder than the mean weighted by area.

4. Exercise
-----------

Section 6 of ``class03_use_gridded_data.ipynb``: the same maps and time series for the **precipitation**
(``rr``). Precipitation adds up, so use sums: ``.sum("time", min_count=1)`` for the maps (``min_count=1``
keeps the sea empty instead of 0) and ``.resample(...).sum()`` for the time series.

5. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``03_gridded_data`` → ``my_page.rst``. The notebook saves the
plots next to it.

#. Run both notebooks, including the exercise: your plots replace the example pictures.
#. Open ``my_page.rst``, write your name, and describe your plots, as the page asks. Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 03*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/03_gridded_data/my_page
