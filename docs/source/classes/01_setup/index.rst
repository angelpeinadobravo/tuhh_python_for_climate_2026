.. _class_01:

01 · Setting up the workshop
================================================================================

Slides: `01 · Setting up the workshop <../../slides/deck.html?md=class01_setup.md>`_
· Notebook: ``examples/class01_first_steps.ipynb``

In this class you install the workshop on your laptop, run your first Python code in JupyterLab, and
add your own page to this webpage, with your name and a picture of a region of the world you are interested in.

What you learn
--------------

- What Docker is for and how to start the workshop container.
- How to find your way in JupyterLab: files, notebooks, terminal and text editor.
- The basics of a notebook and of Python: cells, variables, lists, functions, packages and a plot.
- How to write a page of this webpage, add a picture, and save it as PDF.

1. Install Docker
-----------------

Docker runs the workshop in a *container*: a small computer inside your laptop that has Python and all
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

2. Start the workshop
---------------------

#. Unzip the workshop file from the tutor and open a terminal **in that folder** (the one with
   ``docker-compose.yml``).
#. Create your settings file ``.env`` from the example (Windows PowerShell: ``Copy-Item .env.example .env``):

   .. code-block:: console

      $ cp .env.example .env

   Open ``.env`` in a text editor and replace ``change-me`` with a password of your choice.
   On Linux, also run ``echo "UID=$(id -u)" >> .env && echo "GID=$(id -g)" >> .env``.
#. Start the workshop. The first time takes 10–15 minutes, because Docker downloads all packages:

   .. code-block:: console

      $ docker compose up --build

#. Wait until the terminal shows
   ``JupyterLab: http://localhost:8888   Webpage and slides: http://localhost:8000``.
   Keep the terminal open while you work.

3. Find your way in JupyterLab
------------------------------

Open http://localhost:8888 and log in with your password.

- **File browser** (left): the folder ``/app`` is the course; ``notebooks`` is your own folder.
  Double-click to open a folder or a file; the arrow up icon **uploads** a file from your laptop.
- **Launcher** (the ``+`` tab): start a new notebook, a **terminal** or a text file.
- **Terminal**: type commands and press ``Enter``. You need it for a few commands in this workshop.
- **Editor**: double-click a text file (e.g. ``.rst``) to edit it; save with ``Ctrl + S`` (``Cmd + S`` on macOS).

4. Your first notebook
----------------------

#. Open a terminal (*Launcher → Terminal*) and copy the notebooks of the course into your own folder,
   so your work never mixes with the course files:

   .. code-block:: console

      $ cp -r /app/examples /app/notebooks/lessons

#. In the file browser, open ``notebooks`` → ``lessons`` → ``class01_first_steps.ipynb``.
#. Read each cell and run it with ``Shift + Enter``, from top to bottom. Change the values and run again:
   you cannot break anything.
#. Section 7 of the notebook draws your region on a globe and saves the picture for your page.

5. Your page on this webpage
----------------------------

Everybody adds a page to the list at the end of this page. Pages are text files in the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format (``.rst``).

#. Copy the example page in the terminal (use your names, all lower case, no spaces or accents):

   .. code-block:: console

      $ cd /app/docs/source/classes/01_setup/students
      $ cp 00_example.rst <lastname>_<firstname>.rst

#. Your picture must be in the same folder, as ``<lastname>_<firstname>.png``. Either

   - run section 7 of the notebook (it saves the picture there), or
   - open the folder ``docs/source/classes/01_setup/students`` in the file browser, **upload** a picture of
     your own and rename it (right-click → *Rename*). A ``.jpg`` works too.

#. Open your ``.rst`` file in the file browser and change the title, your name, your region, the text,
   and the file name in the ``.. figure::`` line. Save with ``Ctrl + S``.
#. Open http://localhost:8000/classes/01_setup/ (*Classes → 01*). A few seconds after you save, your page
   appears in the list below. If it does not, the terminal of ``docker compose up`` shows the error
   with the line number.
#. Open your page, print it (``Ctrl + P`` / ``Cmd + P``), choose **Save as PDF**, and send the PDF to the tutor.

6. Stop and start again
-----------------------

Press ``Ctrl + C`` in the terminal of ``docker compose up``, or run ``docker compose down`` in the
workshop folder. Your work stays in the workshop folder on your laptop: the course and your page in
``course/``, your notebooks in ``my_notebooks/``. Next time, start with ``docker compose up``.

Something does not work? See :doc:`../../contribute/intro/getstart` and the *Problems?* table of the
``README.md`` in the workshop folder.

Students
--------

.. toctree::
   :glob:
   :maxdepth: 1

   students/*
