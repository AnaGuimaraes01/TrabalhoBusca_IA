# Algoritmo A* (A Estrela) com heurística (ex: Manhattan)
from puzzle import Puzzle
from heapq import heappush, heappop
from typing import Callable, Tuple, Optional
from itertools import count

def busca_a_estrela(estado_inicial: Tuple[int], tamanho: int, objetivo: Tuple[int], heuristica: Callable[[Puzzle, Tuple[int]], int]) -> Optional[Puzzle]:
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
                prioridade = custo + vizinho.profundidade
                heappush(fronteira, (prioridade, next(contador), vizinho))

    return None
