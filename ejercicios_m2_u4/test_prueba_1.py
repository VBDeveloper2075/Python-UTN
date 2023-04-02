from operaciones import sumar
from operaciones import multiplicar
import pytest

@pytest.mark.skip(reason="no way of currently testing this")
#@pytest.mark.marca1
def test_sumar():
    assert sumar(1, 2)==3

"""
@pytest.mark.parametrize(
    "a, b, resultado",
    [
        (1, 2, 2),
        (sumar(1, 2), 2, 6),
        (5, 2, 11),
        (multiplicar(2,2), 2, 8),
        
    ]
)
def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b)==resultado"""

@pytest.fixture
def fixture_1():
    print("Desde mi fixture antes")
    yield 5
    print("Desde mi fixture después")

def test_sumar_f(fixture_1):
    print("Desde test")
    variable = fixture_1
    assert sumar(variable, 2)==7