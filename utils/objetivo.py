# Gera o estado objetivo correto para qualquer tamanho de puzzle (3x3, 4x4, 5x5, etc.)
from typing import Tuple

def gerar_objetivo(tamanho: int) -> Tuple[int]:
    numeros = list(range(1, tamanho * tamanho))
    numeros.append(0)  # 0 representa o espaço vazio
    return tuple(numeros)
