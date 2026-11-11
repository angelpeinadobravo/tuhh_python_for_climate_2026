.. _contribsci:

Your Page in Each Class
================================================================================

Every class with an exercise ends with *Your page*: an example page, *Example Student*, that you change
into yours. You write it in the workshop container, check it on the webpage on your laptop, and send it
to the tutor as a PDF.

Step by step
------------

#. :doc:`Start the container <getstart>` and complete the exercises of the class in its notebook
   (``notebooks/lessons`` in JupyterLab).

#. In the JupyterLab file browser, open ``pages`` → ``<class>`` → ``my_page.rst``, e.g.
   ``pages/01_setup/my_page.rst`` for class 01.

#. Replace the example title, name and text with yours. A figure of your own goes into the same folder
   (the notebooks of the classes save their plots there, or upload one) and into the page with:

   .. code-block:: rst

      .. figure:: my_plot.png
         :width: 100%

         What the figure shows.

#. Save, and look at the page on http://localhost:8000: it is rebuilt every time you save. Errors in your
   file are shown in the output of ``docker compose up``.

#. Open your page, print it (``Ctrl+P`` or ``Cmd+P``) and choose **Save as PDF**. The printout has only the
   page content, also in dark mode. Send the PDF to the tutor.

Your pages stay in ``my_pages/`` on your laptop, so you can keep improving them after every class. New
lessons of the tutor never overwrite them.

For the tutor
-------------

The example page of a class lives in ``docs/source/classes/<class>/template/`` (``my_page.rst`` and its
pictures). When the webpage is built (``_student_pages`` in ``docs/source/conf.py``), every template file is
copied to the student's folder, ``STUDENT_PAGES/<class>/`` (``/app/pages`` in the container, ``my_pages/``
otherwise), if it is not there yet. The student's folder is then copied into the sources as ``my_pages/``,
which the class page lists in a ``toctree`` as ``/my_pages/<class>/my_page``. git ignores both copies, so
you can improve the templates at any time.

Improving the lessons
---------------------

Found an error in a notebook, the slides or the webpage? Tell the tutor or :ref:`contact us <contact>`.
