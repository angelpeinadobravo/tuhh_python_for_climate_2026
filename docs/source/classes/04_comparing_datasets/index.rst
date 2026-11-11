.. _class_04:

04 · Comparing datasets
================================================================================

Slides: `04 · Comparing datasets <../../slides/deck.html?md=class04_comparing_datasets.md>`_
· Notebooks: ``notebooks/lessons/class04_get_frogs_data.ipynb`` and ``class04_compare_datasets.ipynb``

How much does it rain on Earth? Different groups estimate it in different ways, and their estimates differ.
In this class you compare two estimates of the precipitation of 2020, with maps, their difference and
time series. The difference tells how uncertain our knowledge of precipitation is.

What you learn
--------------

- The three ways to estimate precipitation: rain gauges, satellites and reanalyses.
- What FROGS is: more than 50 precipitation products on the same 1° grid :cite:`Roca_2019`.
- How to compare two maps: the same colour scale, and a map of their difference with colours centred on 0.
- Why global means can hide large regional differences.

1. The data
-----------

`FROGS <https://frogs.ipsl.fr/download-data/>`_ has one folder per product on the IPSL data server
(`catalog <https://thredds-x.ipsl.fr/thredds/catalog/FROGs/catalog.html>`_), and one file per year in it.
All products have daily precipitation in mm/day on the same grid of 1° × 1° (180 latitudes × 360 longitudes),
one file is about 95 MB. In this class, 2020 of:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Product (folder)
     - What
   * - ``GPCP_CDR_v1.3_yes_enforced``
     - GPCP: satellites combined with rain gauges
   * - ``IMERG_V07B_FC``
     - IMERG: satellites, calibrated with rain gauges
   * - your choice, e.g. ``ERA5``
     - exercise: a third product, e.g. the reanalysis ERA5

The references of each product are in the list of the FROGS page. Cite FROGS as :cite:`Roca_2019`.

2. The notebooks
----------------

Open them in JupyterLab (``notebooks`` → ``lessons``) and run them from top to bottom, in this order:

#. ``class04_get_frogs_data.ipynb``: the three ways to estimate precipitation, where FROGS is, downloading
   one year of a product with ``download_frogs``, and checking that two products share the same grid.
#. ``class04_compare_datasets.ipynb``: maps with the same colours, the difference map, global and
   latitude-band means, and the time series of Europe with two curves.

The files are downloaded once into ``notebooks/lessons/data/<product>/``.

In short:

.. code-block:: python

   gpcp = xr.open_dataset(download_frogs("GPCP_CDR_v1.3_yes_enforced", 2020))["rain"]
   imerg = xr.open_dataset(download_frogs("IMERG_V07B_FC", 2020))["rain"]
   difference = imerg.mean("time") - gpcp.mean("time")      # same grid: subtract directly
   difference.plot(cmap="BrBG", vmin=-3, vmax=3)             # 0 in the middle of the colours
   xr.concat([gpcp_year, imerg_year, third_year], dim="product").std("product")   # spread

3. What the comparison shows
----------------------------

For 2020, the global means of GPCP and IMERG are close: 2.66 and 2.73 mm per day. The map of the
difference shows why that is not the whole story: IMERG has more rain than GPCP in parts of the tropics, and
less near the poles, so the differences cancel in the global mean. Over Europe the two curves are close in
most months but not in all: in August 2020, 1.1 mm per day from GPCP against 1.8 from IMERG.

4. Exercise
-----------

Section 6 of ``class04_compare_datasets.ipynb``: add a third product, map its difference to GPCP and the
**spread** of the three products (their standard deviation), and draw Europe with three curves.

5. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``04_comparing_datasets`` → ``my_page.rst``. The notebook saves the
plots next to it.

#. Run both notebooks, including the exercise: your plots replace the example pictures.
#. Open ``my_page.rst``, write your name, and describe what you found, as the page asks. Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 04*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/04_comparing_datasets/my_page
