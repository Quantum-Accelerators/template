import numpy as np
from numpy.testing import assert_allclose

from template.sample import add, make_array


def test_add():
	assert add(1, 2) == 3

def test_make_array():
	assert_allclose(make_array(3), np.array([3, 3, 3]))
	assert_allclose(make_array(3, 4), np.array([3, 3, 3, 3]))
