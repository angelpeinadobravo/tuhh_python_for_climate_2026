.. _extra_hovmuller:

Extra · A Hovmöller diagram of the West African monsoon
================================================================================

Slides: `A Hovmöller diagram of the West African monsoon <../../slides/deck.html?md=extra_hovmuller_diagram.md>`_
· Notebook: ``notebooks/lessons/extra_hovmuller_diagram.ipynb``

A **Hovmöller diagram** shows a value against position and time: here the precipitation between 10°W and
10°E against latitude and month, from ERA5 at zoom 7. It follows the rain band of the West African monsoon
(`Da-Allada et al., 2020 <https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2020EF001595>`_).

What you learn
--------------

- Two means one after the other: over the years of each month, and over each ring of equal latitude
  (``groupby("lat")``: HEALPix cells lie on rings).
- Load a small region into memory with ``.compute()`` before grouping it.
- Draw a diagram of month and latitude, and the difference of two periods.

What it shows
-------------

The rain band is at the coast of the Gulf of Guinea (5°N) in May and June, reaches 10°N and further north in
August, and goes back south in autumn. The difference map shows how this changed between 1950–1980 and
1981–2023.

Exercise: the Indian monsoon.

The data comes from the `nextGEMS catalog <https://data.nextgems-h2020.eu/online.yaml>`_ of :ref:`class 05 <class_05>`.

Your page
---------

Your page is ready in JupyterLab: ``pages`` → ``hovmuller_diagram`` → ``my_page.rst``. Run the notebook, describe what
you found, and check it on http://localhost:8000.

.. toctree::
   :maxdepth: 1

   /my_pages/hovmuller_diagram/my_page
