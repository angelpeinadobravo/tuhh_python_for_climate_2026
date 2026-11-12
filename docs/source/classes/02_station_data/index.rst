.. _class_02:

02 · Station data and time series
================================================================================

Slides: `02 · Station data and time series <../../slides/deck.html?md=class02_station_data.md>`_
· Notebooks: ``notebooks/lessons/class02_get_station_data.ipynb`` and ``class02_use_station_data.ipynb``

In this class you download the measurements of a weather station of the German Weather Service (DWD),
read them with pandas, and plot how temperature and precipitation change over the years.

What you learn
--------------

- Where to find station data: the `DWD open data server <https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/>`_,
  and how to download it with Python.
- What a function is and why it helps: ``download_dwd_daily``.
- How to read a table of measurements with ``pandas``: separators, missing values and dates.
- How to select periods and compute monthly and yearly means and sums with ``resample``.
- How to plot a time series and save it for your page.

1. The data
-----------

Every DWD station has a number and a file of **daily values**, from the first day it measured until the end
of last year. In this class:

.. list-table::
   :header-rows: 1
   :widths: 15 40 45

   * - Number
     - Station
     - Data
   * - 1975
     - Hamburg-Fuhlsbüttel
     - since 1936 · example: temperature
   * - 433
     - Berlin-Tempelhof
     - since 1948 · exercise: precipitation

All stations are in the `list of stations
<https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/KL_Tageswerte_Beschreibung_Stationen.txt>`_.
The file of a station is a zip file with the measurements (``produkt_klima_tag_...txt``) and descriptions
of the station (*Metadaten*). *When you get a new dataset, always look into the data structure!*.

The measurements look like this, one line per day:

.. code-block:: text

   STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
          1975;19360101;-999;-999;-999;    5;   0.1;   1;-999;   0;   7.7;   8.5;  998.00;    7.3;   82.00;    8.8;    5.7;-999;eor

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - Column
     - Meaning
     - Unit
   * - ``MESS_DATUM``
     - date, as ``yyyymmdd``
     -
   * - ``TMK``
     - daily mean temperature (2 m)
     - °C
   * - ``TXK``, ``TNK``
     - daily maximum and minimum temperature (2 m)
     - °C
   * - ``RSK``
     - daily precipitation
     - mm
   * - ``SDK``
     - sunshine duration
     - hours

``-999`` means that there is no measurement for that day.

2. The notebooks
----------------

Open them in JupyterLab (``notebooks`` → ``lessons``) and run them from top to bottom, in this order:

#. ``class02_get_station_data.ipynb``: where the data is on the server, how to find a station and its file,
   and how to download it with Python. Then the same steps as a **function**, ``download_dwd_daily``: why
   functions help, and how to read one.
#. ``class02_use_station_data.ipynb``: read the data with pandas and plot the time series.

The data is downloaded once into ``notebooks/lessons/data/``, so you need internet the first time.

The function, in short: ``download_dwd_daily(1975)`` gives back the zip file of station 1975 in ``data/``,
and downloads it only if it is not there yet.

The pandas you need, in short:

.. code-block:: python

   table = pd.read_csv(file, sep=";", skipinitialspace=True, na_values=[-999])   # read
   table["date"] = pd.to_datetime(table["MESS_DATUM"].astype(str), format="%Y%m%d")
   table = table.set_index("date")                                             # dates as row labels
   table["TMK"]                       # one column
   table.loc["2025", "TMK"]           # one year of it
   table["TMK"].isna().sum()          # number of missing values
   table["TMK"].resample("MS").mean() # monthly means; "YS" for yearly, .sum() for sums

3. Exercise
-----------

Section 6 of ``class02_use_station_data.ipynb``: do the same for the **precipitation** (``RSK``) of **Berlin-Tempelhof**. Precipitation
adds up, so use monthly and yearly **sums** instead of means. Save your plot as
``/app/pages/02_station_data/berlin_precipitation.png``.

4. Your page
------------

Your page is ready in JupyterLab: ``pages`` → ``02_station_data`` → ``my_page.rst``. The notebook saves both
plots next to it.

#. Run the notebook, including the exercise: your plots replace the example pictures.
#. Open ``my_page.rst``, write your name, and describe each plot in two or three sentences, as the page asks.
   Save with ``Ctrl + S``.
#. Check it on http://localhost:8000 → *Classes → 02*, print it and **Save as PDF**, and send it to the tutor.

Your page
---------

.. toctree::
   :maxdepth: 1

   /my_pages/02_station_data/my_page
