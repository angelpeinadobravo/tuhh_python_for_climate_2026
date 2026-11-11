.. _contribsci:

Your Page in Each Class
================================================================================

Every class with an exercise ends with *Your page*: an example page, *Example Student*, that you change
into yours. You write it in the workshop container, check it on the webpage on your laptop, and send it
to the tutor as a PDF.

Step by step
------------

#. :doc:`Start the container <getstart>` and complete the exercises of the class in your copy of the
   notebooks (``/app/notebooks/lessons``).

#. In the JupyterLab file browser, open ``docs/source/classes/<class>/students/my_page.rst``, e.g.
   ``docs/source/classes/01_setup/students/my_page.rst`` for class 01.

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

Your page stays in ``course/`` on your laptop, so you can keep improving it after every class. New lessons
of the tutor never overwrite it.

For the tutor
-------------

The example page of a class is ``students/template_my_page.rst``. When the webpage is built, every
``template_<name>`` file of a ``students/`` folder is copied to ``<name>`` if that file does not exist yet
(``_create_student_pages`` in ``docs/source/conf.py``). git ignores the copies, so you can improve the
templates at any time without clashing with the students' pages. The class page lists ``students/my_page``
in a ``toctree``.

Improving the lessons
---------------------

Found an error in a notebook, the slides or the webpage? Tell the tutor or :ref:`contact us <contact>`.
