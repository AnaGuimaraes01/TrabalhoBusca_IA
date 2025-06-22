# Gera um estado aleatório e resolúvel do puzzle
import random
from typing import Tuple

def gerar_estado_aleatorio_resolvido(tamanho: int) -> Tuple[int]:
    def inversoes(estado: Tuple[int]) -> int:
        lista = [n for n in estado if n != 0]
        return sum(1 for i in range(len(lista)) for j in range(i + 1, len(lista)) if lista[i] > lista[j])

    def posicao_zero_linha(estado: Tuple[int]) -> int:
        return tamanho - (estado.index(0) // tamanho)

    while True:
        estado = list(range(tamanho * tamanho))
        random.shuffle(estado)
        inv = inversoes(tuple(estado))

        if tamanho % 2 == 1:
            if inv % 2 == 0:
                return tuple(estado)
        else:
            linha_zero = posicao_zero_linha(tuple(estado))
            if (inv + linha_zero) % 2 == 0:
                return tuple(estado)
