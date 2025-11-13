from setuptools import find_packages

import funcoes
from funcoes import calculadora
from funcoes.estatistica import media


print(funcoes.calculadora.soma(3, 5))
print(calculadora.subtrai(10, 4))

print(calculadora.multiplica(3, 7))

print(media(4, 8))


print(find_packages())