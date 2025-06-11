import pytest
from mystatistics import average
from pytest import approx

@pytest.mark.parametrize('ns, expected', [
    ([1, 2, 3, ], 2),
    ([10, 20, 30, 40], 25),
    ([0, 0, 0], 0),
    ([-1, 1], 0),
    ([100], 100),
    ([0.1, 0.1, 0.1], 0.1)
])

def test_average(ns, expected):
    actual = average(ns)
    assert actual == approx(expected, abs=0.01), f'average({ns}) = {actual}, expected ~{expected}'
