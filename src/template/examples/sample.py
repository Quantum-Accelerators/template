from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray


def add(a: float, b: float) -> float:
    """
    A function that adds two numbers.

    Parameters
    ----------
    a
        First number to add.
    b
        Second number to add.

    Returns
    -------
    float
        The sum of a and b.
    """
    return a + b


def divide(a: float, b: float) -> float:
    """
    A function that divides two numbers, i.e. a/b.

    Parameters
    ----------
    a
        The numerator
    b
        The denominator

    Returns
    -------
    float
        The value for a/b
    """
    if b == 0:
        raise ValueError("Uh oh! The value for b should not be 0.")

    return a / b


def make_array(val: float, length: int = 3) -> NDArray:
    """
    A function to transform a number into a numpy array.

    Parameters
    ----------
    val
        Number to turn into an array.
    length
        The length of the array.

    Returns
    -------
    NDArray
        An array composed of `val`.
    """
    return np.array([val] * length)
