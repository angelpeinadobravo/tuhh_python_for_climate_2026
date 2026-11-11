.. _ourdocs:

Our Docs
========

We use Sphinx with the `Shibuya <https://shibuya.lepture.com>`_ theme to build this webpage from
reStructuredText (.rst) files in ``docs/source``. Build the .html files and serve them, e.g.

.. code-block:: console

  $ cd docs && make html
  $ python -m http.server 8000 -d build/html

and open http://localhost:8000. This works the same in the workshop container (port 8000 is forwarded)
and on your computer. Serve the files instead of opening ``index.html`` directly: the slides load their
Markdown over HTTP.

Plots in light and dark mode
----------------------------

The webpage has a light and a dark mode. For every figure ``name.png``, a ``name_dark.png`` next to it
is shown in dark mode; without it, ``name.png`` is shown in both modes. Write the figure only once in
the .rst file.

.. _ourslides:

Our Slides
----------

Each class has one `reveal.js <https://revealjs.com>`_ deck in ``slides/``, written in Markdown:

- ``---`` on its own line starts a new slide, ``--`` a slide below it (vertical),
- ``Note:`` starts the speaker notes of a slide (press ``S`` while presenting),
- ``$...$`` is LaTeX math, and ``![](../examples/Fig/name.png)`` a figure of the notebooks.

``slides/deck.html`` shows the deck named in the address, e.g. ``slides/deck.html?md=00_intake_catalog.md``.
To present without building the webpage, serve the repository root:

.. code-block:: console

  $ python -m http.server 8000

and open http://localhost:8000/slides/deck.html?md=00_intake_catalog.md. A new deck needs a row in
``docs/source/slides.rst``. Sphinx copies ``slides/`` and ``examples/Fig/`` into the webpage, so the
same links work online.

Viewing Files on Levante Using your Local Browser
-------------------------------------------------
On Levante, the files are on a remote file system. Forward a port when you connect:

.. code-block:: console

  $ ssh -L 8765:localhost:8765 <userid>@levante.dkrz.de

then build the docs, run ``python -m http.server 8765 -d build/html`` and open http://localhost:8765.
If the port is in use, pick another number above 1024.

Things to Note
--------------
- After a pull request is merged into main, GitHub Actions rebuilds the webpage; it can take a few minutes to update.

- If you build the docs but are getting strange results, try removing the cached .html files and then re-building, e.g.

  .. code-block:: console

    $ make clean && make html

Sphinx
------
- `Sphinx Documentation <https://www.sphinx-doc.org/en/master/>`_
- `reStructuredText Primer by Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
