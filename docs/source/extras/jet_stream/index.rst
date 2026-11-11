.. _extra_jet:

Extra · The jet stream
================================================================================

Slides: `The jet stream <../../slides/deck.html?md=extra_jet_stream.md>`_
· Notebook: ``notebooks/lessons/extra_jet_stream.ipynb``

The **eddy-driven jet** of the mid-latitudes, in the zonal wind at 700 hPa of ERA5 (zoom 6, 1950–2023)
(`Adam et al., 2018 <https://gmd.copernicus.org/articles/11/4339/2018/>`_;
`Breul et al., 2025 <https://www.nature.com/articles/s43017-025-00749-9>`_).

What you learn
--------------

- Select a pressure level (``sel(level=700)``) and a season (``time.dt.month.isin(...)``).
- The **zonal mean** with ``groupby("lat")`` on the rings of the HEALPix grid.
- The latitude of the jet as a mean weighted by the westerly wind to the power 8, and its strength as the
  largest wind.
- Trends of both since 1950.

What it shows
-------------

Two jets, near 45°N and 50°S; the southern one is stronger, and both move towards the pole in their summer.
From 1950–1980 to 1981–2023 the southern jet moved 0.8° towards the pole and grew 0.8 m/s stronger; the
northern jet changed little.

Exercise: the subtropical jet at 250 hPa.

The data comes from the `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ of :ref:`class 05 <class_05>`.

Your page
---------

Your page is ready in JupyterLab: ``pages`` → ``jet_stream`` → ``my_page.rst``. Run the notebook, describe what
you found, and check it on http://localhost:8000.

.. toctree::
   :maxdepth: 1

   /my_pages/jet_stream/my_page
