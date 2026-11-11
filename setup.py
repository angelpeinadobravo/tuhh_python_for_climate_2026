"""
Copyright (c) 2025 MPI-M

----- tuhh_python_for_climate_2026 -----
File: setup.py
Project: tuhh_python_for_climate_2026
Created Date: Friday 05th December 2025
Author: Angel Peinado Bravo (APB)
Additional Contributors:
-----
Last Modified: Friday 05th December 2025
Modified By: APB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

from setuptools import setup, find_packages

setup(
    name="tuhh_python_for_climate_2026",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "sphinx",
    ],
)
