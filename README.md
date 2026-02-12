# base_gitpage

This repository serve as a template for puzzle project in the MPI-M.

Please replace the link to gitpage and some variables as: m300901 and base_gitpage.

## Install
To (locally) reproduce this project simply clone the repository.
```
git clone https://gitlab.dkrz.de/m300901/base_gitpage.git
```

You will need to create an environment with the necessary packages as listed in the environment.yml
e.g. using a conda environment:
```
  $ conda env create -f environment.yml
  $ conda activate base_gitpage
```

In Levante, please follow the documentation: [Python Environments](<https://docs.dkrz.de/blog/2021/conda_path.html>). We recommend creating a directory to collect your environments and make the environment visible for jupyterhub:
```
  $ module load python3
  $ conda env create --prefix <path_for_the_environment>/base_gitpage -f environment.yml
  $ source activate <path_for_the_environment>/base_gitpage
  $ python -m ipykernel install --user --name base_gitpage
```

You will also need to install the pre-commit hooks, e.g.
```
  $ pre-commit install
```
which will be used when you try to commit something or you run `pre-commit run`

## Documentation
You can find the documentation for this project hosted online in the [repo-webpage](<https://google.com/>)

If you cannot access this website, please raise an issue in the repository.

Alternatively, You can build and view the documentation locally. First build the .html files using
Sphinx, then view them in your default browser. E.g.

```
cd ./docs && mkdir build && make html
open build/html/index.html
```

## Contributors
- Angel Peinado Bravo
