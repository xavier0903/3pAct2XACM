import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_suma_enteros(calc):
    assert calc.suma(2, 3) == 5

def test_suma_negativos(calc):
    assert calc.suma(-2, -3) == -5

def test_suma_decimales(calc):
    assert calc.suma(2.5, 1.25) == pytest.approx(3.75)

def test_resta_normal(calc):
    assert calc.resta(5, 2) == 3

def test_resta_negativos(calc):
    assert calc.resta(-1, 3) == -4

def test_divide_normal(calc):
    assert calc.divide(10, 2) == 5

def test_divide_negativo(calc):
    assert calc.divide(-9, 3) == -3

def test_divide_decimales(calc):
    assert calc.divide(7.5, 2.5) == pytest.approx(3.0)

def test_divide_por_cero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
