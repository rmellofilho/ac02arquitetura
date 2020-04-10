import unittest
from calculo import Calculadora, CalculadoraCientifica
from menu import ExecutarMenuOperacoes, ExecutarOperacao, PassarNumero


class CalculadoraTestes(unittest.TestCase):

        def test_soma(self):
            '''Testar função soma'''
            self.assertEqual(Calculadora(1, 1).somar(), 2)
            self.assertEqual(Calculadora(1, -1).somar(), 0)
        
        def test_subtrair(self):
            '''Testar função de subtração'''
            self.assertEqual(Calculadora(1, 1).subtrair(), 0)
            self.assertEqual(Calculadora(1, -1).subtrair(), 2)
        
        def test_multiplicar(self):
            '''Testar função de multiplicação'''
            self.assertEqual(Calculadora(1, 1).multiplicar(), 1)
            self.assertEqual(Calculadora(3, 0).multiplicar(), 0)
            self.assertEqual(Calculadora(0, 3).multiplicar(), 0)

        def test_dividir(self):
            '''Testar função de divisão'''
            self.assertEqual(Calculadora(2, 1).dividir(), 2)
            self.assertEqual(Calculadora(1, 0).dividir(), "Não pode se dividir por 0!")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(CalculadoraTestes)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


runTests()
