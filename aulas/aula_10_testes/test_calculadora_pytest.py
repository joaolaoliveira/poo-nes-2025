from calculadora import Calculadora

CALC = Calculadora(10, 5)

def test_somar():
    assert CALC.somar() == 15

def test_subtrair():
    assert CALC.subtrair() == 5

def test_multiplicar():
    assert CALC.multiplicar() == 50

def test_dividir():
    assert CALC.dividir() == 2

def test_dividir_por_zero():
    assert Calculadora(10,0).dividir() is None

def test_power():
    assert CALC.power() == 100000