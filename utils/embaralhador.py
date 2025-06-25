import random
from typing import Tuple
from puzzle import Puzzle

def gerar_estado_aleatorio_resolvido (tamanho: int, movimentos: int =15)-> Tuple[int]:
    """
    Gera um estado aleatório resolúvel, aplicando X movimentos a partir do estado objetivo.
    :param tamanho: tamanho do puzzle (ex: 3, 4, 5)
    :param movimentos: número de movimentos aleatórios a aplicar
    :return: estado inicial como tupla
    """
    # Estado objetivo
    objetivo = tuple(range(1, tamanho * tamanho))
    objetivo += (0,)  # Espaço vazio representado pelo 0

    puzzle = Puzzle(objetivo, tamanho)

    for _ in range(movimentos):
        sucessores = puzzle.gerar_sucessores()
        puzzle = random.choice(sucessores)  # Escolhe um movimento aleatório válido

    return puzzle.estado













# # Gera um estado aleatório e resolúvel do puzzle
# import random
# from typing import Tuple

# def gerar_estado_aleatorio_resolvido(tamanho: int) -> Tuple[int]:
#     def inversoes(estado: Tuple[int]) -> int:
#         lista = [n for n in estado if n != 0]
#         return sum(1 for i in range(len(lista)) for j in range(i + 1, len(lista)) if lista[i] > lista[j])

#     def posicao_zero_linha(estado: Tuple[int]) -> int: 
#         return tamanho - (estado.index(0) // tamanho)

#     while True:
#         estado = list(range(tamanho * tamanho))
#         random.shuffle(estado)
#         inv = inversoes(tuple(estado))

#         if tamanho % 2 == 1:
#             if inv % 2 == 0:
#                 return tuple(estado)
#         else:
#             linha_zero = posicao_zero_linha(tuple(estado))
#             if (inv + linha_zero) % 2 == 0:
#                 return tuple(estado)
