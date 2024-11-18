from __future__ import annotations

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal

from template.examples.sample import add, divide, make_array


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

    with pytest.raises(ValueError, match="Uh oh! The value for b should not be 0"):
        divide(10, 0)


def test_make_array():
    """
    Test that the array generation works.

    Note that we use `assert_array_equal` to assert that two
    numpy arrays are the same. We also use `assert_allclose()`,
    which is effectively an element-wise call to `pytest.approx()`.
    """
    assert_array_equal(make_array(3), np.array([3, 3, 3]))
    assert_allclose(make_array(divide(3, 2), length=4), np.array([1.5, 1.5, 1.5, 1.5]))
