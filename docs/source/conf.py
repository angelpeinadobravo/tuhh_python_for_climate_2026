"""
Copyright (c) 2026 MPI-M
----- Repo -----
File: conf.py
Project: source
Created Date: Thursday 12th February 2026
Author: Angel Peinado (AP)
Additional Contributors:
-----
Last Modified: Wednesday 11th November 2026
Modified By: AP
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
Sphinx configuration of the workshop webpage (Shibuya theme, layout taken from
the skeleton project).
"""

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).parents[2].resolve()
# add "../.." and "../../examples" to system path (autodoc of examples/utils)
sys.path.insert(0, ROOT.as_posix())
sys.path.insert(0, (ROOT / "examples").as_posix())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Python for Climate Science"
license = "BSD 3-Clause"
copyright = "(2026) MPI-M, "
author = "Members of Repo"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

GITHUB_URL = "https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026"

html_theme = "shibuya"
html_title = "TUHH · Python for Climate Science"

# Pastel light/dark palettes and fonts (Fraunces for titles, Hanken Grotesk
# for text) live in _static/custom.css
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# right-hand column: page contents + "Edit this page" (no repo star counter)
html_sidebars = {"**": ["sidebars/localtoc.html", "sidebars/edit-this-page.html"]}
html_context = {
    # "Edit this page" opens the file in the GitHub editor
    "source_edit_template": GITHUB_URL
    + "/edit/main/docs/source/{}",
}

html_theme_options = {
    "accent_color": "indigo",  # overridden by the pastel blue in custom.css
    "color_mode": "auto",  # follow the visitor's system; switch in the top bar
    "nav_links": [
        {"title": "Lessons", "url": "lessons/index"},
        {"title": "Slides", "url": "slides"},
        {"title": "Contribute", "url": "contribute/index"},
    ],
    "github_url": GITHUB_URL,
    "globaltoc_expand_depth": 1,
    "show_ai_links": False,
}

html_last_updated_fmt = "%d %B %Y"

# Add numbering to figures
numfig = True
numfig_secnum_depth = 1

# -- Light and dark versions of plots ------------------------------------------
# For every image "name.png", if "name_dark.png" exists in the same folder, both
# go on the page: "name.png" is shown in light mode and "name_dark.png" in dark
# mode (see the end of _static/custom.css). Write the figure only once in the
# .rst file; its caption, number and references stay as they are. Images
# without a _dark file are shown in both modes.
from docutils import nodes as _nodes


def _add_dark_images(app, doctree):
    env = app.env
    for node in list(doctree.findall(_nodes.image)):
        uri = node.get("uri", "")
        if "://" in uri or uri.startswith("data:") or "only-dark" in node["classes"]:
            continue
        stem, dot, ext = uri.rpartition(".")
        if not dot or stem.endswith("_dark"):
            continue
        dark_uri = f"{stem}_dark.{ext}"
        _, dark_path = env.relfn2path(dark_uri, env.docname)
        if not pathlib.Path(dark_path).is_file():
            continue
        dark = node.deepcopy()  # keeps width, alt text and alignment
        dark["uri"] = dark_uri
        dark.attributes.pop("candidates", None)
        dark["classes"] = [c for c in node["classes"] if c != "only-light"] + [
            "only-dark"
        ]
        node["classes"].append("only-light")
        node.parent.insert(node.parent.index(node) + 1, dark)


# -- reveal.js slides ------------------------------------------------------------
# slides/*.md load figures from ../examples/Fig, so both folders keep their repo
# path in the built site and the decks work the same locally and online.
def _copy_slides(app, exception):
    if exception is None and app.builder.format == "html":
        for folder in ("slides", "examples/Fig"):
            shutil.copytree(
                ROOT / folder, pathlib.Path(app.outdir) / folder, dirs_exist_ok=True
            )


def setup(app):
    # priority below 500: run before Sphinx collects the images to copy
    app.connect("doctree-read", _add_dark_images, priority=400)
    app.connect("build-finished", _copy_slides)
