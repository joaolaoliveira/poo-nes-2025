class Contador:
    def __init__(self, baixo, alto):
        self.baixo = baixo
        self.alto = alto

    def __iter__(self):
        self.atual = self.baixo
        return self
    
    def __next__(self):
        if self.atual < self.alto:
            numero = self.atual
            self.atual += 1
            return numero
        raise StopIteration
    

# Uso
contador = Contador(1, 6)

for numero in contador:
    print(numero)