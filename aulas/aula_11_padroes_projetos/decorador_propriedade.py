class Pessoa:
    def __init__(self, nome : str) -> None:
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome : str) -> None:
        self._nome = novo_nome


# Uso
pessoa = Pessoa("João")
print(pessoa.nome)
pessoa.nome = "Bob"
print(pessoa.nome)