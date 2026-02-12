.. _ourdocs:

Our Docs
========

We use Sphinx to build our documentation from reStructuredText (.rst) files (very good for Python code). You can view the documentation locally by building .html files from the .rst files and then opening a .html file in your browser e.g.

.. code-block:: console

  $ cd ./docs && mkdir build && make html
  $ open build/html/index.html

To view the documentation whilst working on a remote machine such as Levante, please follow the :ref:`instructions below <docsonlevante>`.


.. _docsonlevante:

Viewing Files on Levante Using your Local Browser
-------------------------------------------------
Let's say you're working on Levante and have made some changes to the documentation on your branch of this repository. After you built the documentation via

.. code-block:: console

  $ cd ./docs && mkdir build && make html

You probably now want to open a brower and have a look at the updated docs. However, ``open build/html/index.html`` won't work because the ``index.html`` file is on Levante's remote file system not your local one. Here is a good way to solve this problem...

#. Open up a new terminal on your local machine

#. SSH to Levante with local port forwarding enabled:

    .. code-block:: console

      $ ssh -L 8765:localhost:8765 <userid>@levante.dkrz.de

#. Enter the directory than contains the ``index.html`` file and create an http server from it.

    .. code-block:: console

      $ cd docs/build/html/
      $ python -m http.server 8765

#. Open the server on your preferred browser e.g. https://localhost:8765

In the command above the '``8765``'s in ``8765:localhost:8765`` are port numbers. They can be pretty much any number above 1024, but if someone else is already using the port number you choose then it won't work for you. In that case simply try a different number / numbers e.g. ``9090:localhost:9090``.


Things to Note
--------------
- After successfully merging changes to the main branch on the repository on GitLab, you may have to wait a few minutes for the website to update.

- If you build the docs but are getting strange results, try removing the cached .html files and then re-building, e.g.

  .. code-block:: console

    $ make clean && make html


Sphinx
------
`Sphinx Documentation <https://www.sphinx-doc.org/en/master/>`_
###############################################################

`reStructuredText Primer by Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
##############################################################################################################

Contributing to Our Documentation
---------------------------------
If you would like to contribute to the documentation, have questions or would like clarification or more detail on a particular topic, please :ref:`contact us! <contact>`.
