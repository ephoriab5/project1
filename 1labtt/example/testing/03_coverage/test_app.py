import pytest
from app import Figure

def test_square_angles():
    fig = Figure("квадрат", 5)
    assert fig.get_angles == 4

