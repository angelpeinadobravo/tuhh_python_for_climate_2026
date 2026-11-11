.. _lesson_00:

00 · Accessing climate data
================================================================================

Notebook: `examples/00_intake_catalog.ipynb <https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026/blob/main/examples/00_intake_catalog.ipynb>`_
· Slides: `00 · Accessing climate data <../../slides/deck.html?md=00_intake_catalog.md>`_

What you learn
--------------

- Open a dataset from an online `intake <https://intake.readthedocs.io>`_ catalog, here ERA5 from the
  km-scale global hackathon (``https://data.nextgems-h2020.eu/online.yaml``).
- Read the structure of an ``xarray.Dataset``: dimensions, coordinates, data variables and their attributes.
- Understand the HEALPix grid :cite:`Gorski_2005`: equal-area cells, :math:`N_\mathrm{cells} = 12\,\mathrm{nside}^2`
  and :math:`\mathrm{nside} = 2^z` for zoom level :math:`z`.
- Open netCDF files with ``xarray.open_dataset`` and compare a HEALPix (zoom 8) with a lon-lat grid.
- Make a quick plot: ``DataArray.plot()`` for lon-lat grids, ``easygems.healpix.healpix_show`` for HEALPix.

Exercises
---------

#. **Understanding the dataset.** Find units and short names of temperature, 100 m wind, precipitation,
   sea surface temperature and downward short-wave radiation in ERA5 and in ICON ``ngc4008``.
#. **Three zoom levels.** Plot the 1990–1994 mean temperature of zoom 0, 3 and 6 side by side with an
   EqualEarth projection, and compute their global means.
#. **Two grids.** Do the same for the 2020 mean of the lon-lat and HEALPix netCDF files.

Lessons learned
---------------

Add your file to ``docs/source/lessons/00_intake_catalog/learned/`` (:ref:`how to <contribsci>`).

.. toctree::
   :glob:
   :maxdepth: 1

   learned/*
