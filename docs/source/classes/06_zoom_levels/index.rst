.. _class_06:

06 · Working with zoom levels
================================================================================

Slides: `06 · Working with zoom levels <../../slides/deck.html?md=class06_zoom_levels.md>`_
· Notebook: ``notebooks/lessons/class06_zoom_levels.ipynb``

The HEALPix data of class 05 is in the catalog at many **zoom levels**. In this class you draw the same map at
different zooms, for the globe and for the Alps, and find out what the zoom changes and what it does not.

What you learn
--------------

- What each zoom level costs: cells, spacing and data.
- Which zoom you need for a map of the globe, and for a region.
- Why the global mean is the same at every zoom: a cell is the mean of its 4 cells of the next zoom.
- Why the value at one place is not, especially in the mountains.

1. The data
-----------

From the `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ of class 05:

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Dataset
     - What
     - Zoom levels used
   * - ``cat.ERA5``
     - 2 m temperature ``2t``, mean of 2021–2023
     - 0 to 8
   * - ``cat.ICON.ngc4008``
     - 2 m temperature ``tas`` of 15 July 2021
     - 6 to 9 (zoom 10 has no values of ``tas``)

.. list-table::
   :header-rows: 1
   :widths: 15 25 25 35

   * - Zoom
     - Cells
     - Spacing
     - One map (4 bytes per cell)
   * - 5
     - 12 288
     - ~200 km
     - 0.05 MB
   * - 6
     - 49 152
     - ~100 km
     - 0.2 MB
   * - 8
     - 786 432
     - ~25 km
     - 3 MB
   * - 9
     - 3 145 728
     - ~13 km
     - 13 MB
   * - 10
     - 12 582 912
     - ~6 km
     - 50 MB

2. The notebook
---------------

Open ``notebooks`` → ``lessons`` → ``class06_zoom_levels.ipynb`` in JupyterLab and run it from top to bottom.
It needs no download of its own: it reads from the catalog, about a minute in total.

In short:

.. code-block:: python

   cat.ERA5(zoom=5).to_dask()                          # the same data at another zoom
   ax.set_extent([4, 16, 43, 49], crs=ccrs.PlateCarree())   # a region: west, east, south, north
   egh.healpix_show(data, ax=ax)                       # works at every zoom
   zoom7.reshape(-1, 4).mean(axis=1)                   # 4 cells of zoom 7 -> 1 cell of zoom 6
   hp.ang2pix(2**zoom, lon, lat, nest=True, lonlat=True)    # the cell of a place at that zoom

3. What the zoom changes
------------------------

- **Maps:** from zoom 5 on, a map of the globe looks smooth. The Alps are a few blocks at zoom 6, and show their
  valleys and ridges at zoom 9.
- **The global mean does not change:** 14.76 °C for ERA5 2021–2023 at every zoom from 0 to 8. The cells of
  a zoom are the means of the 4 cells of the next zoom, which are numbered one after the other (nested order):
  averaging zoom 7 in groups of 4 gives zoom 6.
- **One place does change:** the cell of Hamburg has about 10 °C from zoom 3 on; the cell of the Mont Blanc
  goes from 11 °C at zoom 3 to 4.5 °C at zoom 8, still far warmer than the summit: a cell is an area, not a point.

Take the coarsest zoom that shows what you need: every zoom level multiplies the data by 4.

4. Exercise
-----------

Section 7: maps of your own region at four zoom levels, and one place of it at zoom 0 to 8.

5. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``06_zoom_levels`` → ``my_page.rst``. The notebook saves the
plots next to it.

#. Run the notebook, including the exercise: your plots replace the example pictures.
#. Open ``my_page.rst``, write your name, and describe what the zoom changes. Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 06*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/06_zoom_levels/my_page
