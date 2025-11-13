from typing import Literal, TypeAlias
from constantes import COLUNAS_DICT, CASAS_DO_TABULEIRO

casas_type : TypeAlias = Literal[*CASAS_DO_TABULEIRO] # type: ignore[misc]

class Peca:
    def __init__(self, posicao : casas_type, 
                 cor : Literal['Branco', 'Preto']) -> None:
        self.cor = cor
        self.nome = self.__class__.__name__ + ' ' + self.cor
        self.coluna = posicao[0]
        self.linha = int(posicao[1])
        self.casas_possiveis = []
        # self.coluna_num = COLUNAS_DICT[self.coluna]

    def __str__(self) -> str:
        return f'{self.nome} está na casa {self.get_posicao()}'
    
    def get_posicao(self) -> str:
        return f'{self.coluna}{self.linha}'
    
    def mover(self, nova_posicao : casas_type) -> None:
        raise NotImplementedError('Método mover() deve ser implementado na subclasse.')
    

class Peao(Peca):

    def __init__(self, posicao : casas_type, 
                 cor : Literal['Branco', 'Preto']) -> None:

        super().__init__(posicao, cor)
        self.__movimento_invalido = f'Movimento inválido: o {self.nome} não pode avançar'

        self.calcular_casas_possiveis()

    def is_posicao_inicial(self) -> bool:
        if self.cor == 'Branco' and self.linha == 2:
            return True
        elif self.cor == 'Preto' and self.linha == 7:
            return True
        return False
    
    def calcular_casas_possiveis(self) -> None:
        
        cor = self.cor

        if cor == 'Branco':
            linha = self.linha

            if self.is_posicao_inicial():
                self.casas_possiveis.append(f'{self.coluna}{linha + 1}')
                self.casas_possiveis.append(f'{self.coluna}{linha + 2}')

            elif linha < 8:
                self.casas_possiveis.append(f'{self.coluna}{linha + 1}')

        else:
            linha = self.linha

            if self.is_posicao_inicial():
                self.casas_possiveis.append(f'{self.coluna}{linha - 1}')
                self.casas_possiveis.append(f'{self.coluna}{linha - 2}')

            elif linha < 8:
                self.casas_possiveis.append(f'{self.coluna}{linha - 1}')          


    def mover(self, nova_posicao : casas_type) -> None:
        pass

    
    # def is_posicao_final(self) -> bool:
    #     if self.cor == 'Branco' and self.linha == 8:
    #         return True
    #     elif self.cor == 'Preto' and self.linha == 1:
    #         return True
    #     return False



    # def mover(self, quantidade_casas : Literal[1, 2]) -> None: # type: ignore[override]

    #     is_possivel_mover = True
    #     match quantidade_casas:
    #         case 1:
    #             is_possivel_mover = not self.is_posicao_final()
    #         case 2:
    #             is_possivel_mover = self.is_posicao_inicial()
    #         case _:
    #             is_possivel_mover = False


    #     if is_possivel_mover:
    #         if self.cor == 'Branco':
    #             self.linha += quantidade_casas
    #         else:
    #             self.linha -= quantidade_casas
    #     else:
    #         print(self.__movimento_invalido)
    