import numpy as np
import pytest
from numpy.testing import assert_allclose

from template.sample import add, make_array


def test_add():
    assert add(1, 2) == 3
    assert add(1.5, 2.0) == pytest.approx(3.5)


def test_make_array():
    assert_allclose(make_array(3), np.array([3, 3, 3]))
    assert_allclose(make_array(3, 4), np.array([3, 3, 3, 3]))
