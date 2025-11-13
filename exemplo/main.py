class Animal:
    def __init__(self, nome):
        self.nome = nome


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} diz Au Au")


toby = Cachorro("Toby")
toby.latir()


class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b


calc = Calculadora()
print(calc.somar(10, 5))        # Saída: 15