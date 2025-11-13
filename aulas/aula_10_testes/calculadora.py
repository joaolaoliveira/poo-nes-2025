class Calculadora:
    STR_DIVISAO_POR_ZERO = "Divisão por zero não é permitida."

    def __init__(self, valor_inicial : int|float = 0,
                 valor_final : int|float = 0) -> None:
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def somar(self) -> int|float:
        return self.valor_inicial + self.valor_final
    
    def subtrair(self) -> int|float:
        return self.valor_inicial - self.valor_final
    
    def multiplicar(self) -> int|float:
        return self.valor_inicial * self.valor_final
    
    def dividir(self) -> int | float | None:
        if self.valor_final == 0:
            print(self.STR_DIVISAO_POR_ZERO)
        else:
            return self.valor_inicial / self.valor_final
        
    def power(self) -> int | float:
        '''
            Calcula o valor_inicial elevado ao valor_final

            Returns:
                int | float: resultado da potência
            
            Exemplo: se valor_inicial = 2 e valor_final = 3,
        '''
        return self.valor_inicial ** self.valor_final