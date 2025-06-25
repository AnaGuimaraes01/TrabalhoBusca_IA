
# Algoritmo A* (A Estrela) com heurística (ex: Manhattan)
# from puzzle import Puzzle
# from heapq import heappush, heappop
# from typing import Callable, Tuple, Optional
# from itertools import count

# def busca_a_estrela(estado_inicial: Tuple[int], tamanho: int, objetivo: Tuple[int], heuristica: Callable[[Puzzle, Tuple[int]], int]) -> Optional[Puzzle]:
#     raiz = Puzzle(estado_inicial, tamanho)
#     fronteira = []
#     visitados = set()
#     contador = count()

#     heappush(fronteira, (0, next(contador), raiz))

#     while fronteira:
#         _, _, atual = heappop(fronteira)

#         if atual.estado == objetivo:
#             return atual

#         visitados.add(atual.estado)

#         for vizinho in atual.gerar_sucessores():
#             if vizinho.estado not in visitados:
#                 custo = heuristica(vizinho, objetivo)
#                 prioridade = custo + vizinho.profundidade
#                 heappush(fronteira, (prioridade, next(contador), vizinho))

#     return None  

from heapq import heappop, heappush
from itertools import count
from typing import Callable, Optional, Tuple

from puzzle import Puzzle


def busca_a_estrela(estado_inicial: Tuple[int], tamanho: int, objetivo: Tuple[int], heuristica: Callable[[Puzzle, Tuple[int]], int]) -> Tuple[Optional[Puzzle], int]:
    raiz = Puzzle(estado_inicial, tamanho)
    fronteira = []
    visitados = set()
    contador = count()
    nos_expandidos = 0

    heappush(fronteira, (0, next(contador), raiz))

    while fronteira:
        _, _, atual = heappop(fronteira)
        nos_expandidos += 1  # Conta o nó expandido

        if atual.estado == objetivo:
            return atual, nos_expandidos

        visitados.add(atual.estado)

        for vizinho in atual.gerar_sucessores():
            if vizinho.estado not in visitados:
                custo = heuristica(vizinho, objetivo)
                prioridade = custo + vizinho.profundidade
                heappush(fronteira, (prioridade, next(contador), vizinho))

    return None, nos_expandidos
