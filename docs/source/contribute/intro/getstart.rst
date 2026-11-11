.. _getstart:

Getting Started
================================================================================

The workshop container
----------------------

The workshop runs in a Docker container that clones this repository and installs every package of
``requirements.txt``, so you do not need to set up Python yourself. You only need
`Docker <https://docs.docker.com/get-docker/>`_ and the workshop folder with the ``Dockerfile`` and
``docker-compose.yml`` that you get from the instructor.

#. To work on your own fork (needed for :doc:`lessons learned <contribsci>`), set in the ``.env`` file of the workshop folder:

   .. code-block:: console

      REPO_URL=https://github.com/<your-user>/tuhh_python_for_climate_2026.git
      JUPYTER_PASSWORD=<a password of your choice>

#. Build and start the container:

   .. code-block:: console

      $ docker compose up --build

#. Open http://localhost:8888 and log in with your ``JUPYTER_PASSWORD``. The repository is in ``/app``;
   the notebooks of the lessons are in ``/app/examples``.

.. warning::
   The repository lives inside the container. Commit and push your work (JupyterLab → Terminal) before you run
   ``docker compose down``, otherwise it is lost. Files in ``/app/notebooks`` are the exception: that folder is
   ``my_notebooks/`` of the workshop folder on your computer.

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

Install the pre-commit hooks:

.. code-block:: console

  $ pre-commit install

``pre-commit`` formats your code and notebooks when you commit. More information can be found in `their documentation <https://pre-commit.com>`_.

Now everything should work out of the box and you can :doc:`add your lessons learned <contribsci>`. If not, please :ref:`raise an issue in the repository <issue>`.
