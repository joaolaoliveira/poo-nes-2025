import unittest
from unittest.mock import patch
# import sys, os
# # adiciona a pasta pai (aula_09_testes) ao sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora(10, 5)
        self.calc_zero = Calculadora(10, 0)

    def test_somar(self):
        # calc = Calculadora(10, 5)
        self.assertEqual(self.calc.somar(), 15)

    def test_subtrair(self):
        # calc = Calculadora(10, 5)
        self.assertEqual(self.calc.subtrair(), 5)

    def test_multiplicar(self):
        # calc = Calculadora(10, 5)
        self.assertEqual(self.calc.multiplicar(), 50)

    def test_dividir(self):
        # calc = Calculadora(10, 5)
        self.assertEqual(self.calc.dividir(), 2)

    def test_dividir_por_zero(self):
        # calc = Calculadora(10, 0)
        self.assertIsNone(self.calc_zero.dividir())

    def test_dividir_por_zero_print(self):
        # calc = Calculadora(10, 0)
        with patch('builtins.print') as mock_print:
            resultado = self.calc_zero.dividir()
            mock_print.assert_called_with(self.calc_zero.STR_DIVISAO_POR_ZERO)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()