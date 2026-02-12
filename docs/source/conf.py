"""
Copyright (c) 2026 MPI-M

----- Repo -----
File: conf.py
Project: source
Created Date: Thursday 12th February 2026
Author: Angel Peinado (AP)
Additional Contributors:
-----
Last Modified: Thursday 12th February 2026
Modified By: AP
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import pathlib
import sys

# add "../.." to system path (depreciated version is: os.path.abspath('../..')
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
# add "../../libs" to system path
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix() + "/libs/")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "XXXXXXXXXXXXXXx"
license = "BSD 3-Clause"
copyright = "(2026) MPI-M, "
author = "Members of Repo"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.duration",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
    "sphinx.ext.viewcode",
]

# configuration of citations using bibtex file(s)
bibtex_bibfiles = ["./references.bib"]
bibtex_reference_style = "label"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# To include the date of the last visit in Sphinx documentation, use the last
# updated feature of Sphinx. This feature automatically adds the last modification
# date of the source file to the rendered HTML output.
html_last_updated_fmt = "%d %B %Y"
