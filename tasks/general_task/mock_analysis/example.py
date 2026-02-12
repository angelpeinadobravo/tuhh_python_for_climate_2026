"""
Copyright (c) 2025 MPI-M,

----- XXXXXXXXXXXXXXXXX -----
File: example.py
Project: mock_analysis
Created Date: Thursday 12th February 2026
Author: Angel Peinado Bravo (APB)
Additional Contributors:
-----
Last Modified: Thursday 12th February 2026
Modified By: APB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
Example Python script for a mock analysis.
"""


def hello_world():
    """
    Prints 'Hello World!'

    This function doesn't take any parameters.
    """

    print("Hello World")


def area_square(side):
    """
    Calculate the are of a square

    Parameters:
        side (float): The side of the square

    Returns:
        float: The area of the square.

    Examples:
      >>> area_square(5.0)
      25.0
    """

    return side * side


hello_world()
print("The are of a square with side length of 1.0 is {:.1f}".format(area_square(1.0)))
