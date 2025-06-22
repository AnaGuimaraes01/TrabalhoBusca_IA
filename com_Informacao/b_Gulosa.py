# Busca Gulosa com heurística (ex: fora do lugar)
from puzzle import Puzzle
from heapq import heappush, heappop
from typing import Callable, Tuple, Optional
from itertools import count

def busca_gulosa(estado_inicial: Tuple[int], tamanho: int, objetivo: Tuple[int], heuristica: Callable[[Puzzle, Tuple[int]], int]) -> Optional[Puzzle]:
    raiz = Puzzle(estado_inicial, tamanho)
    fronteira = []
    visitados = set()
    contador = count()

    heappush(fronteira, (0, next(contador), raiz))

    while fronteira:
        _, _, atual = heappop(fronteira)

        if atual.estado == objetivo:
            return atual

        visitados.add(atual.estado)

        for vizinho in atual.gerar_sucessores():
            if vizinho.estado not in visitados:
                custo = heuristica(vizinho, objetivo)
                heappush(fronteira, (custo, next(contador), vizinho))

    return None
