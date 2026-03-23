# base_gitpage

This repository serve as a template for the workshop introduction to python for climate science in the MPI-M for TUHH.

## Install
To (locally) reproduce this project simply clone the repository.
```
git clone https://github.com/angelpeinadobravo/tuhh_python_for_climate_2026.git
```

You will need to create an environment with the necessary packages as listed in the environment.yml
e.g. using a conda environment:
```
  $ conda env create --name tuhh_env --file requirements.txt
  $ conda activate tuhh_env
```

e.g. using virtualenv
```
  $ virtualenv tuhh_env
  $ source venv/bin/activate
  $ python -m pip install -r requirements.txt
  $ pre-commit install
```

In Levante, please follow the documentation: [Python Environments](<https://docs.dkrz.de/blog/2021/conda_path.html>). We recommend creating a directory to collect your environments and make the environment visible for jupyterhub:
```
  $ module load python3
  $ conda env create --name tuhh_env --file requirements.yml
  $ source activate tuhh_env
  $ python -m ipykernel install --user --name tuhh_env
```

You will also need to install the pre-commit hooks, e.g.
```
  $ pre-commit install
```
which will be used when you try to commit something or you run `pre-commit run`

## Webpage
You can build and view the documentation locally. First build the .html files using
Sphinx, then view them in your default browser. E.g.

```
cd ./docs && mkdir build && make html
open build/html/index.html
```

## Contributors
- Angel Peinado Bravo
