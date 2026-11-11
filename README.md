# Python for Climate Science

Material of the MPI-M workshop *Introduction to Python for climate science* for TUHH:
Jupyter notebooks with exercises, reveal.js slides for each class, and a webpage where students add their lessons learned.

The webpage uses the Shibuya theme (layout of the skeleton project): navigation in the top bar, the full menu on the left and the page outline on the right, in light and dark mode.
A plot `figure.png` is shown in light mode and, if it exists, `figure_dark.png` in dark mode; otherwise `figure.png` is used for both modes.

## Layout

| Folder           | Content                                                                    |
|------------------|----------------------------------------------------------------------------|
| `examples/`      | One notebook per lesson, the figures they write (`Fig/`) and shared helpers (`utils/`) |
| `slides/`        | One reveal.js deck per class, in Markdown, and `deck.html` that shows them  |
| `docs/source/`   | The webpage: `lessons/` (one page per lesson with the students' lessons learned), `slides.rst`, `contribute/` |
| `tests/`         | pytest checks run by the CI                                                |

## Install
The workshop runs in a Docker container that clones this repository and installs `requirements.txt` (see the workshop folder and the [getting started page](https://angelpeinadobravo.github.io/tuhh_python_for_climate_2026/contribute/intro/getstart.html)).

To (locally) reproduce this project without Docker, clone the repository and create an environment with Python 3.11, e.g. using virtualenv:
```
  $ git clone https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026.git
  $ cd tuhh_python_for_climate_2026
  $ python3.11 -m venv tuhh_env
  $ source tuhh_env/bin/activate
  $ python -m pip install -r requirements.txt
```

In Levante, please follow the documentation: [Python Environments](<https://docs.dkrz.de/blog/2021/conda_path.html>) and make the environment visible for jupyterhub:
```
  $ python -m ipykernel install --user --name tuhh_env
```

You will also need to install the pre-commit hooks, e.g.
```
  $ pre-commit install
```
which will be used when you try to commit something or you run `pre-commit run`

## Webpage
The webpage is published by GitHub Actions on every push to main: [angelpeinadobravo.github.io/tuhh_python_for_climate_2026](https://angelpeinadobravo.github.io/tuhh_python_for_climate_2026/).

You can build and view it locally. The slides load their Markdown over HTTP, so serve the files instead of opening them:
```
cd ./docs && make html
python -m http.server 8000 -d build/html
```
and open http://localhost:8000.

## Slides
To present a class without building the webpage, serve the repository root and open the deck:
```
python -m http.server 8000
```
http://localhost:8000/slides/deck.html?md=00_intake_catalog.md

## Contributors
- Angel Peinado Bravo
