.. _class_05:

05 · Getting to know HEALPix
================================================================================

Slides: `05 · Getting to know HEALPix <../../slides/deck.html?md=class05_healpix.md>`_
· Notebooks: ``notebooks/lessons/class05_get_healpix_data.ipynb`` and ``class05_evaluate_models.ipynb``

So far you used observations. In this class you use the output of a **climate model**, the ICON simulations
of the project nextGEMS, on the **HEALPix** grid :cite:`Gorski_2005`. You compare the model with ERA5 to find
its **biases**: where it is too warm or too cold.

What you learn
--------------

- What the HEALPix grid is: cells of equal area, zoom levels, cell numbers instead of latitudes and longitudes.
- How to find and open data with an **intake catalog**.
- How to draw HEALPix maps with ``easygems``, and find the cell of a place with ``healpix``.
- How to evaluate a model: the bias map, the global mean, and the time series at one place.

1. The data
-----------

The `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ lists the simulations of the models ICON
and IFS, and data to compare them with. In this class, at **zoom 6** (49 152 cells of about 100 km):

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - Dataset
     - What
     - In this class
   * - ``cat.ICON.ngc4008``
     - ICON simulation, daily output 2020–2050
     - example: 2 m temperature ``tas``
   * - ``cat.ICON.ngc3028``
     - ICON simulation, daily output 2020–2025
     - exercise
   * - ``cat.ERA5``
     - reanalysis, monthly means 1940–2023
     - reference: 2 m temperature ``2t``

Both are compared for 2021–2023, by monthly means. The IFS simulation of the catalog is not accessible at the
moment (the server answers *403 Forbidden*), so this class uses ICON only.

2. The HEALPix grid
-------------------

HEALPix cuts the sphere into 12 cells of equal area, and every cell again into 4 at each **zoom level** ``z``:
``12 · 4^z`` cells, ``nside = 2^z``. Because all cells have the same area, the global mean is a plain mean over the
cells, without the weights a lon-lat grid needs (class 03). The cells have numbers, not latitudes and longitudes;
``healpix.ang2pix`` gives the cell of a position. Class 06 is about the zoom levels.

3. The notebooks
----------------

Open them in JupyterLab (``notebooks`` → ``lessons``) and run them from top to bottom, in this order:

#. ``class05_get_healpix_data.ipynb``: the catalog, the HEALPix grid, a first map, and the monthly means of
   2021–2023 of ICON and ERA5, saved in ``notebooks/lessons/data/``. Computing the ICON means reads about
   200 MB and can take a few minutes; it is done only once.
#. ``class05_evaluate_models.ipynb``: maps, the bias map, the global mean, and Hamburg with the model, ERA5
   and the DWD station of class 02.

In short:

.. code-block:: python

   cat = intake.open_catalog("https://data.nextgems-h2020.eu/online.yaml")
   icon = cat.ICON.ngc4008(zoom=6, time="P1D").to_dask()            # lazy, as in class 03
   egh.healpix_show(data, ax=ax, cmap="RdBu_r", vmin=-5, vmax=5)    # a HEALPix map on a cartopy axis
   bias = icon_mean - era5_mean                                     # same grid: subtract
   icon.mean("cell")                                                # global mean: equal areas
   hp.ang2pix(64, 10.0, 53.55, nest=True, lonlat=True)              # the cell of Hamburg at zoom 6

4. What the comparison shows
----------------------------

For 2021–2023, ngc4008 is 1.07 K colder than ERA5 in the global mean. The bias is not the same everywhere:
about −1.5 K in the tropics, while the model is too warm over parts of North America and Siberia. The second
simulation, ngc3028, is colder still: −1.40 K in the global mean.

In Hamburg, ERA5 and the DWD station follow each other month by month, but the model can be several degrees
off in a single month, warmer or colder. That is expected: a climate simulation is not given the weather of
2021–2023, it makes its own. A model is evaluated by its **climate**, the mean over many months, not by single
months.

5. Exercise
-----------

Section 5 of part 1 and section 6 of part 2: the same for the simulation **ngc3028**, and which simulation is
closer to ERA5.

6. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``05_healpix`` → ``my_page.rst``. The notebook saves the plots
next to it.

#. Run both notebooks, including the exercise: your plots replace the example pictures.
#. Open ``my_page.rst``, write your name, and describe the biases you found. Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 05*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/05_healpix/my_page
