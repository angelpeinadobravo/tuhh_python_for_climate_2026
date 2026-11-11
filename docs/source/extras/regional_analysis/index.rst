.. _extra_regional:

Extra · Regional analysis at different zoom levels
================================================================================

Slides: `Regional analysis at different zoom levels <../../slides/deck.html?md=extra_regional_analysis.md>`_
· Notebook: ``notebooks/lessons/extra_regional_analysis.ipynb``

The mean over a region on the HEALPix grid: find the cells inside the region, and average them. Example: the
Tibetan Plateau and its surface pressure (ERA5, 1991–2020), which shows the height of the land.

What you learn
--------------

- Select the cells of a **box** of latitudes and longitudes from the positions of the cells (``lat``, ``lon``).
- Select the cells of a **polygon** with ``shapely`` and ``geopandas``, for regions that are not boxes.
- Read only the cells of a region, and draw them in an otherwise empty map.
- Compare the regional mean at zoom 6 and zoom 8.

What it shows
-------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Region
     - Cells at zoom 6
     - Cells at zoom 8
   * - Box 73–105°E, 26–40°N
     - 437
     - 7 098
   * - Polygon of the plateau
     - 331
     - 5 324

The **shape** matters much more than the zoom: the box is 80 hPa higher in pressure than the polygon (it
contains the lowlands around the plateau), while zoom 6 and zoom 8 of the polygon differ by 1.4 hPa.

Exercise: Costa Rica, a small region, and a region of your choice.

The data comes from the `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ of :ref:`class 05 <class_05>`.

Your page
---------

Your page is ready in JupyterLab: ``pages`` → ``regional_analysis`` → ``my_page.rst``. Run the notebook, describe what
you found, and check it on http://localhost:8000.

.. toctree::
   :maxdepth: 1

   /my_pages/regional_analysis/my_page
