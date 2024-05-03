"""
Testing for function module
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import molecool
import numpy as np
import pytest
from molecool.ising_hamiltonian import IsingHamiltonian

@pytest.fixture
def test_IsingHamiltonian_constructor():
    J = [[(0, 0.5), (1, -0.5)], [(1, 0.2)]]
    mu = np.array([0.1, -0.2])
    ising = IsingHamiltonian(J, mu)
    
    assert len(ising.J) == 2
    assert len(ising.J[0]) == 2
    assert len(ising.J[1]) == 1
    assert np.array_equal(ising.mu, np.array([0.1, -0.2]))
    assert ising.N == 2

def test_IsingHamiltonian_compute_average_values():
    J = [[(0, 0.5), (1, -0.5)], [(1, 0.2)]]
    mu = np.array([0.1, -0.2])
    ising = IsingHamiltonian(J, mu)
    
    T = 1.0
    E, M, HC, MS = ising.compute_average_values(T)
    
    assert E == 0.44535333508629155
    assert M == 0.1441701750237102
    assert HC == 0.20031737075901146
    assert MS == 2.8722234046424293

def test_get_lowest_energy_config():
    J = [[(0, 0.5), (1, 0.5)], [(1, 0.2)]]
    mu = np.array([1, 1])
    ising = IsingHamiltonian(J, mu)

    energy, config = ising.get_lowest_energy_config()

    assert energy == -0.8
    assert config.config[0] == 0
    assert config.config[1] == 0