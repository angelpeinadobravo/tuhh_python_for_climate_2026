.. _class_01:

01 · Setting up the Docker container
================================================================================

Slides: `01 · Setting up the Docker container <../../slides/deck.html?md=class01_setup.md>`_
· Notebook: ``notebooks/lessons/class01_first_steps.ipynb``

In this class you create a docker image on your laptop, run your first Python code in JupyterLab, and
add your own page to this webpage.

What you learn
--------------

- What Docker is for and how to start the container.
- How to find your way in JupyterLab: files, notebooks, terminal and text editor.
- The basics of a notebook and of Python: cells, variables, lists, functions, packages and a plot.
- How to write a page of this webpage, add a picture, and save it as PDF.

1. Install Docker
-----------------

Docker runs a *container*: a small computer inside your laptop that has Python and all
the packages already installed, the same for everybody. You install Docker once:

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - System
     - What to install
   * - Windows
     - `Docker Desktop <https://docs.docker.com/desktop/setup/install/windows-install/>`__ (accept the WSL 2 option)
   * - macOS
     - `Docker Desktop <https://docs.docker.com/desktop/setup/install/mac-install/>`__ (Apple silicon or Intel)
   * - Linux
     - `Docker Engine <https://docs.docker.com/engine/install/>`_ with the Compose plugin

Start Docker Desktop and check in a terminal (Windows: *PowerShell*, macOS: *Terminal*) that it works:

.. code-block:: console

   $ docker compose version

2. Deploy the container
-----------------------

#. Unzip the file provided and open a terminal **in that folder** (the one with ``docker-compose.yml``).
#. Or go to the `repositor <https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026>`__ and download
#. the dirctory ``workshop`` in your laptop.
#. Create your settings file ``.env`` from the example (Windows PowerShell: ``Copy-Item .env.example .env``):

   .. code-block:: console

      $ cp .env.example .env

   Open ``.env`` in a text editor and replace ``change-me`` with a password of your choice.
   On Linux, also run ``echo "UID=$(id -u)" >> .env && echo "GID=$(id -g)" >> .env``.
#. Start the docker. The first time takes 10–15 minutes, because Docker downloads all packages:

   .. code-block:: console

      $ docker compose up --build

#. Wait until the terminal shows
   ``JupyterLab: http://localhost:8888   Webpage and slides: http://localhost:8000``.
   Keep the terminal open while you work.

3. Find your way in JupyterLab
------------------------------

Open http://localhost:8888 and log in with your password.

- **File browser** (left): your two folders, ``notebooks`` (the notebooks of the classes) and ``pages``
  (your pages of this webpage). Double-click to open a folder or a file; the arrow up icon **uploads**
  a file from your laptop.
- **Launcher** (the ``+`` tab): start a new notebook, a **terminal** or a text file.
- **Terminal**: type commands and press ``Enter``. You will hardly need it.
- **Editor**: double-click a text file (e.g. ``.rst``) to edit it; save with ``Ctrl + S`` (``Cmd + S`` on macOS).

4. Your first notebook
----------------------

#. In the file browser, open ``notebooks`` → ``lessons`` → ``class01_first_steps.ipynb``.
   Every start of the docker puts the notebooks of new classes there; yours are never overwritten.
#. Read each cell and run it with ``Shift + Enter``, from top to bottom. Change the values and run again:
   you cannot break anything.
#. Section 7 of the notebook draws your region on a globe and saves the picture for your page.

5. Your page on this webpage
----------------------------

Your page is already there: *Example Student · Hamburg*, at the end of this page. You only change it.
Pages are text files in the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format (``.rst``).

#. Make the picture of your region: change ``region_name``, ``lon`` and ``lat`` in section 7 of the
   notebook and run it. It saves the picture as ``my_region.png`` next to your page.

   Prefer a picture of your own? In the file browser, open ``pages`` → ``01_setup``, **upload** it
   (arrow up icon), and write its file name in the ``.. figure::`` line of your page.

#. In the file browser, open ``pages`` → ``01_setup`` → ``my_page.rst``. Replace the example title,
   name, region and text with yours, and save with ``Ctrl + S``.
#. Open http://localhost:8000/classes/01_setup/ (*Classes → 01*). A few seconds after you save, your page
   shows your title in the list below. If it does not, the terminal of ``docker compose up`` shows the
   error with the line number.
#. Open your page, print it (``Ctrl + P`` / ``Cmd + P``), choose **Save as PDF**, and send the PDF to the tutor.

Your page and picture stay on your laptop, in ``my_pages/``. Deleted ``my_page.rst`` by mistake? The next
save of any page brings back the example.

6. Stop and start again
-----------------------

Press ``Ctrl + C`` in the terminal of ``docker compose up``, or run ``docker compose down`` in the
workshop folder. Your work stays in the workshop folder on your laptop: your notebooks in ``my_notebooks/``
and your pages in ``my_pages/``. ``course/`` is the course itself, updated on every start; you do not need
to open it. Next time, start with ``docker compose up``.

Something does not work? See :doc:`../../contribute/intro/getstart` and the *Problems?* table of the
``README.md`` in the workshop folder.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/01_setup/my_page
