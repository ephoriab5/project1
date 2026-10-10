import pytest
from app import Figure

def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"

def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)