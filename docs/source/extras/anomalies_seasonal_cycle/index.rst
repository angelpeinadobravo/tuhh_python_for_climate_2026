.. _extra_anomalies:

Extra · Anomalies and the seasonal cycle
================================================================================

Slides: `Anomalies and the seasonal cycle <../../slides/deck.html?md=extra_anomalies_seasonal_cycle.md>`_
· Notebook: ``notebooks/lessons/extra_anomalies_seasonal_cycle.ipynb``

How much has the climate warmed? Remove the seasonal cycle, and look at the **anomalies**. ERA5 2 m temperature,
monthly 1950–2023; reference period 1950–1980, recent period 1981–2023.

What you learn
--------------

- The **seasonal cycle** with ``groupby("time.month")``, and its spread from year to year.
- **Anomalies** against a reference period: each value minus the mean of its month.
- A linear **trend** with ``np.polyfit``, for one series or for every cell of a map at once.
- Why the global mean can use zoom 0 (class 06), and maps need zoom 6.

What it shows
-------------

The globe is warmest in July, and the recent period is warmer in every month. The yearly anomalies of the
global mean grow by **0.21 °C per decade** over 1981–2023. The maps show where: most over land and in the
Arctic.

Exercise: the seasonal cycle, the anomalies and the trend of one place.

The data comes from the `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ of :ref:`class 05 <class_05>`.

Your page
---------

Your page is ready in JupyterLab: ``pages`` → ``anomalies_seasonal_cycle`` → ``my_page.rst``. Run the notebook, describe what
you found, and check it on http://localhost:8000.

.. toctree::
   :maxdepth: 1

   /my_pages/anomalies_seasonal_cycle/my_page
