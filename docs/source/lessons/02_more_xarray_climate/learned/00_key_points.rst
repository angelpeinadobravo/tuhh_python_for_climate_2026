Key points · Instructor
=======================

:Author: Angel Peinado Bravo

- Anomalies against a reference period remove the seasonal cycle: ``da.groupby("time.month") - ref.groupby("time.month").mean("time")``.
- ``xarray.apply_ufunc`` applies any NumPy function (here ``numpy.polyfit``) to every cell, lazily with Dask.
- A Hovmöller diagram turns a space-time field into one picture of where and when something happens.
- Correlation is not causation: yearly anomalies of jet and temperature can share a trend without one driving the other.
