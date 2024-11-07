from calculator import square
import pytest

def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0

def test_positive():
    assert square(2)==4
    assert square(3)==9
    assert square(4)==16

def test_negative():
    assert square(-2)==4
    assert square(-3)==9
    assert square(-4)==16

# use pytest 3rd party library

def test_str():
    with pytest.raises(TypeError):
        square("cat")