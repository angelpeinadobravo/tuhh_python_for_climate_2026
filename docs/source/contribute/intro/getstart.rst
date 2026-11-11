.. _getstart:

Getting Started
================================================================================

The workshop container
----------------------

The workshop runs in a Docker container with every package of ``requirements.txt``, so you do not need to
set up Python yourself. You need `Docker Desktop <https://docs.docker.com/get-docker/>`_ (Windows, macOS)
or Docker Engine (Linux), and the workshop zip file from the tutor.

#. Unzip the workshop file and open a terminal in its folder.

#. Copy ``.env.example`` to ``.env`` and choose a password:

   .. code-block:: console

      JUPYTER_PASSWORD=<a password of your choice>

   On Linux, also add your user and group id (``id -u`` and ``id -g``) as ``UID=...`` and ``GID=...``,
   so the files the container writes belong to you.

#. Build and start the container (the first build takes 10–15 minutes):

   .. code-block:: console

      $ docker compose up --build

#. Open in your browser:

   - http://localhost:8888 · **JupyterLab**, log in with your ``JUPYTER_PASSWORD``
   - http://localhost:8000 · **this webpage** and the slides, rebuilt every time you save a page

Stop the container with ``Ctrl+C`` or ``docker compose down``, start it again with ``docker compose up``.

Where your work lives
---------------------

Everything you do is saved on your laptop, in the workshop folder, and survives stopping the container:

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - On your laptop
     - In JupyterLab
     - Content
   * - ``my_notebooks/``
     - ``notebooks``
     - Your notebooks: the lessons in ``lessons/``, your homework and data
   * - ``my_pages/``
     - ``pages``
     - Your pages of this webpage, one folder per class
   * - ``course/``
     - (not shown)
     - The course itself: lessons, webpage, slides; you do not need to open it

Every start downloads the new lessons of the tutor into ``course/``, and copies the notebooks and example
pages of new classes into your folders. Your own files are never overwritten. If the update of ``course/``
fails (no internet, or a file in it was changed), the container tells you so; deleting ``course/`` downloads
it again, without touching your notebooks and pages.

Without Docker
--------------

Clone the repository and create an environment with Python 3.11, e.g. with ``venv``:

.. code-block:: console

   $ git clone https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026.git
   $ cd tuhh_python_for_climate_2026
   $ python3.11 -m venv tuhh_env
   $ source tuhh_env/bin/activate
   $ python -m pip install -r requirements.txt

In Levante, please follow the documentation: `Python Environments <https://docs.dkrz.de/blog/2021/conda_path.html>`_,
and make the environment visible for JupyterHub with ``python -m ipykernel install --user --name tuhh_env``.

Now everything should work out of the box and you can :doc:`write your page <contribsci>`. If not, please :ref:`contact us <contact>`.
