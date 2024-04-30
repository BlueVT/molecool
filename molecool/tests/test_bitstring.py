"""
Testing for function module
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import molecool
import numpy as np
from molecool.bitstring import BitString

@pytest.fixture
def test_init():
    N = 8
    bs = BitString(N)
    assert np.array_equal(bs.config, np.zeros(N, dtype=int))

def test_repr():
    N = 8
    bs = BitString(N)
    assert repr(bs) == f'BitString("{bs.config}")'

def test_eq():
    N = 8
    bs1 = BitString(N)
    bs2 = BitString(N)
    assert bs1 == bs2

def test_len():
    N = 8
    bs = BitString(N)
    assert len(bs) == N

def test_on():
    N = 8
    bs = BitString(N)
    bs.config[2] = 1
    bs.config[4] = 1
    assert bs.on() == 2

def test_off():
    N = 8
    bs = BitString(N)
    bs.config[2] = 1
    bs.config[4] = 1
    assert bs.off() == 6

def test_flip_site():
    N = 8
    bs = BitString(N)
    bs.flip_site(2)
    assert bs.config[2] == 1

def test_set_int_config():
    N = 8
    bs = BitString(N)
    bs.set_int_config(10)
    assert np.array_equal(bs.config, np.array([0, 0, 0, 0, 1, 0, 1, 0]))