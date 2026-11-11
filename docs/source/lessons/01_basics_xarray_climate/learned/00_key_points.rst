Key points · Instructor
=======================

:Author: Angel Peinado Bravo

- On HEALPix a plain ``.mean("cell")`` is already area-weighted; on a lon-lat grid it is not.
- Global means hardly depend on the zoom level, points and small regions do.
- Keep regions as cell indices: the dataset keeps its grid and the selection is cheap to reuse.
- Real regions are not boxes: ``shapely`` polygons with ``geopandas`` select the cells that really belong to a region.
