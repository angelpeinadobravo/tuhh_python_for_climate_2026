.. _contribsci:

Add your Lessons Learned
================================================================================

Every lesson page ends with a *Lessons learned* list. Each entry is one file written by one student, so
nobody edits the same file and pull requests do not conflict.

Step by step
------------

#. `Fork the repository <https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026/fork>`_ on GitHub and
   :doc:`start the container <getstart>` with your fork as ``REPO_URL``.

#. In the JupyterLab terminal, set your name and create a branch (``main`` is protected by ``pre-commit``):

   .. code-block:: console

      $ cd /app
      $ git config user.name "<Your Name>"
      $ git config user.email "<your@email>"
      $ git switch -c learned-00-<lastname>

#. Complete the exercises of the notebook in ``examples/``.

#. Copy the instructor's file of the lesson and write your own, e.g. for lesson 00:

   .. code-block:: console

      $ cd docs/source/lessons/00_intake_catalog/learned
      $ cp 00_key_points.rst <lastname>_<firstname>.rst

   Change the title and author and write what you learned in a few bullet points. A figure of your own goes
   next to your file (``<lastname>_<firstname>.png``) and into the page with:

   .. code-block:: rst

      .. figure:: <lastname>_<firstname>.png
         :width: 100%

         What the figure shows.

#. :ref:`Build the webpage <ourdocs>` and check your page.

#. Commit, push and open a pull request to ``main``:

   .. code-block:: console

      $ git add docs/source/lessons
      $ git commit -m "Add lessons learned of lesson 00"
      $ git push -u origin learned-00-<lastname>

   ``git push`` asks for your GitHub user name and, as password, a
   `personal access token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_.
   GitHub then shows a link to open the pull request. Once it is merged, your page is online.

Improving the lessons
---------------------

Found an error in a notebook, the slides or the webpage? :ref:`Open an issue <issue>` or a pull request with the fix.
