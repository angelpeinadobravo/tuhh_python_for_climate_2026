"""
Copyright (c) 2025 MPI-M

----- RemapHealpixNative -----
File: test_mock.py
Project: tests
Created Date: Thursday 12th February 2026
Author: Angel Peinado Bravo (APB)
Additional Contributors:
-----
Last Modified: Friday 12th February 2026
Modified By: APB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
"""

import sys
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(path + "/../tasks/general_task/mock_analysis")

import tasks.general_task.mock_analysis.example as example


def test_area_square():
    assert example.area_square(1.0) == 1.0
