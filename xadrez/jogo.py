
from tabuleiro import Tabuleiro
from peca import Peao

tabulerio = Tabuleiro()

peao_branco = Peao('e2', 'Branco')
print(peao_branco)

peao_preto = Peao('e7', 'Preto')
print(peao_preto)

peao_branco.mover(2)
print(peao_branco)
peao_preto.mover(2)
print(peao_preto)

peao_branco.mover(1)
print(peao_branco)
peao_preto.mover(1)
print(peao_preto)

peao_branco.mover(1)
print(peao_branco)
peao_preto.mover(1)
print(peao_preto)

peao_branco.mover(2)
print(peao_branco)
peao_preto.mover(2)
print(peao_preto)

peao_branco.mover(1)
print(peao_branco)
peao_preto.mover(1)
print(peao_preto)

peao_branco.mover(1)
print(peao_branco)
peao_preto.mover(1)
print(peao_preto)

peao_branco.mover(1)
print(peao_branco)
peao_preto.mover(1)
print(peao_preto)
