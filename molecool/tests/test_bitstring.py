"""
Testing for function module
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import molecool


@pytest.fixture
def test_canvas_with_attribution():
    assert "molecool" in sys.modules
    
# def test_canvas_without_attribution():
#     assert 