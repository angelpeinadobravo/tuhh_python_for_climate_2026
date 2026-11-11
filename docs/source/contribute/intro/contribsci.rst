.. _contribsci:

Add your Lessons Learned
================================================================================

Every class page ends with a list of the students' pages. Each entry is one file written by one student.
You write yours in the workshop container, check it on the webpage on your laptop, and send it to the
tutor as a PDF.

Step by step
------------

#. :doc:`Start the container <getstart>` and complete the exercises of the lesson in your copy of the
   notebooks (``/app/notebooks/lessons``).

#. In the JupyterLab terminal, copy the instructor's file of the class, e.g. for extra 00:

   .. code-block:: console

      $ cd /app/docs/source/extras/00_intake_catalog/learned
      $ cp 00_key_points.rst <lastname>_<firstname>.rst

#. Open your file in JupyterLab, change the title and author, and write what you learned in a few bullet points.
   A figure of your own goes next to your file (``<lastname>_<firstname>.png``) and into the page with:

   .. code-block:: rst

      .. figure:: <lastname>_<firstname>.png
         :width: 100%

         What the figure shows.

#. Save, and look at the page on http://localhost:8000: it is rebuilt every time you save. Errors in your
   file are shown in the output of ``docker compose up``.

#. Open your page, print it (``Ctrl+P`` or ``Cmd+P``) and choose **Save as PDF**. The printout has only the
   page content, also in dark mode. Send the PDF to the tutor.

Your file stays in ``course/`` on your laptop, so you can keep improving it after every class.

Improving the lessons
---------------------

Found an error in a notebook, the slides or the webpage? Tell the tutor or :ref:`contact us <contact>`.
