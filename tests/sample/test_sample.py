import numpy as np
import pytest
from numpy.testing import assert_allclose

from template.sample import add, make_array, divide


def test_add():
    """
    Test that the addition function works.
    """
    assert add(1, 2) == 3


def test_divide():
    """
    Test that the division function works.

    Note that we use `pytest.approx()` here since 3/2 != 1.5
    exactly due to floating point precision differences.

    Also note that we can test that a given error is raised
    by using `pytest.raises(<error>)`.
    """
    assert divide(3, 2) == pytest.approx(1.5)

    with pytest.raises(ValueError):
        divide(10, 0)


def test_make_array():
    """
    Test that the array generation works.

    Note that we use `assert_allclose()` here, which is
    effectively an element-wise call to `pytest.approx()`.
    It wasn't strictly needed in this example but was used
    for demonstration purposes.
    """
    assert make_array(3) == np.array([3, 3, 3])
    assert_allclose(make_array(divide(3, 2), length=4), np.array([1.5, 1.5, 1.5, 1.5]))
