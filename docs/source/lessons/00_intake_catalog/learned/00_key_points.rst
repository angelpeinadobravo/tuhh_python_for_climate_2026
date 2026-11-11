Key points · Instructor
=======================

:Author: Angel Peinado Bravo

- ``intake`` hides where and how data is stored: ``cat["ERA5"](zoom=0).to_dask()`` returns a lazy ``xarray.Dataset``.
- Lazy means nothing is downloaded until ``.load()``, ``.compute()`` or a plot needs the values.
- HEALPix zoom :math:`z` has :math:`12 \cdot 4^z` cells of equal area, so one more zoom level means four times more data.
- Units and long names live in ``.attrs``; check them before computing anything.
