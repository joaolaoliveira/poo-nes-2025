class Livro:
    def __init__(self, titulo : str, autor : str) -> None:
        self.titulo = titulo
        self.autor = autor

    def exibir(self) -> str:
        return f"{self.titulo} por {self.autor}"
    

# Decorador
class Marcador:
    def __init__(self, livro : Livro, pagina : int) -> None:
        self.livro = livro
        self.pagina = pagina

    def exibir(self) -> str:
        return f"{self.livro.exibir()}, marcado na página {self.pagina}."
    

# Uso
meu_livro = Livro("A Guerra dos Tronos: As Crônicas do Gelo e Fogo, volume 1", "George R. R. Martin")
meu_livro_com_marcador = Marcador(meu_livro, 45)

print(meu_livro.exibir())
print(meu_livro_com_marcador.exibir())


# Uma problemática desses decoradores clássicos:
# print(meu_livro_com_marcador.autor)
# Por não ter herança, só há a impressão de que o Livro está 'embrulhado' no Decorador
# Existem formas de contornar isto:

# class Marcador:
#     def __init__(self, livro : Livro, pagina : int) -> None:
#         self.livro = livro
#         self.pagina = pagina

#     def exibir(self) -> str:
#         return f"{self.livro.exibir()}, marcado na página {self.pagina}."
    
#     def __getattr__(self, atributo) :
#         return getattr(self.livro, atributo)