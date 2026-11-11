.. _class_07:

07 · Machine learning for climate data
================================================================================

Slides: `07 · Machine learning for climate data <../../slides/deck.html?md=class07_machine_learning.md>`_
· Notebooks: ``notebooks/lessons/class07_ml_regression.ipynb`` and ``class07_ml_bias_correction.ipynb``

The last class adds one more tool to your climate workflow: **machine learning**. With data you already know,
the DWD stations of class 02 and ERA5 of class 05, you train simple models with ``scikit-learn``, evaluate them
honestly, and use one to correct the bias of a reanalysis.

What you learn
--------------

- The words of supervised learning: features (X), target (y), regression and classification, training and testing.
- How to train and evaluate a model with ``scikit-learn``: ``fit``, ``predict`` and the RMSE.
- Why a time series is split in **time order**, why to compare with simple guesses, and what **overfitting** is.
- How to correct the bias of a reanalysis at a station, and why it must be tested on independent years.

1. A first model
----------------

``class07_ml_regression.ipynb``: predict the daily temperature of Hamburg (station 1975) from the two days
before, with a linear regression; trained on 1936–2009, tested on 2010–2025.

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Prediction of the test days
     - RMSE
   * - linear regression (yesterday, two days ago)
     - 2.14 °C
   * - persistence: tomorrow = today
     - 2.17 °C
   * - climatology: always the mean
     - 6.88 °C
   * - with tomorrow as a feature (a mistake: leakage)
     - 1.46 °C

The model barely beats persistence: an honest result. A **decision tree** shows overfitting: without a
depth limit its error is 1.44 °C on the training days but 2.89 °C on the test days.

**Why in time order?** A forecast only knows the past, and the climate changes: the test years are 1.3 °C warmer
(10.17 against 8.88 °C) than the training years.

2. Bias correction
------------------

``class07_ml_bias_correction.ipynb``: ERA5 (monthly, zoom 8) at the cell of the **Zugspitze** (station 5792,
2 956 m) against the station, 1950–2023. The corrections are trained on 1950–1990 and tested on 1991–2023.

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Test years 1991–2023
     - Mean bias
     - RMSE
   * - ERA5
     - +9.95 °C
     - 10.22 °C
   * - mean shift (−9.40 °C)
     - +0.55 °C
     - 2.39 °C
   * - linear regression (0.722 × ERA5 − 8.10)
     - +0.14 °C
     - 1.61 °C

ERA5 is about 10 °C too warm: its cell is an area whose mean height is far below the summit (class 06). The
regression also corrects the seasonal cycle, which is too large in ERA5. The bias itself grows from about
9.2 °C in the 1950s to 10.2 °C in the 2020s: a correction learned in the past may not hold in a changing climate.

This works because a reanalysis follows the real weather. A free-running simulation like ICON makes its own
weather (class 05), so month-by-month pairs of model and station mean nothing; such models are corrected by
their statistics instead.

3. From grids to samples
------------------------

Gridded data with dimensions ``(time, cell)`` becomes a table of samples and features, e.g. one row per time
and one column per cell, or one model per cell. The algorithm does not care whether the cells come from a
lon-lat grid or from HEALPix; what matters is that features and targets refer to the same times and places.

4. Exercises
------------

At the end of each notebook: more features and a forecast two days ahead; Hamburg, the bias of each month,
and other mountain stations.

5. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``07_machine_learning`` → ``my_page.rst``. The notebooks save
the plots next to it.

#. Run both notebooks, including the exercises.
#. Open ``my_page.rst``, write your name, and describe your results. Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 07*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/07_machine_learning/my_page
