.. _getstart:

Getting Started
================================================================================

To collaborate in this project:

Clone the GitLab respository

.. code-block:: console

  $ git clone git@gitlab.dkrz.de:m300901/base_gitpage.git

Create an environment with the necessary dependencies, e.g., conda:

.. code-block:: console

   $ conda env create -f environment.yml
   $ conda activate base_gitpage

Install the pre-commit hooks:

.. code-block:: console

  $ pre-commit install

``pre-commit`` will help in commit changes to the project. More information of pre-commit can be found in `their documentation: <https://pre-commit.com>`_.

Now everything should work out of the box and you would be able to move into :doc:`contributing science <contribsci>`, but if not please :ref:`raise an issue in the respository <issue>`.
