# Busca em Largura (BFS) com controle de tempo
from collections import deque
from puzzle import Puzzle
from typing import List, Tuple
from time import time

def busca_em_largura(inicial: Puzzle, objetivo: Tuple[int], tempo_maximo: int = 30) -> Tuple[List[str], int, int]:
    inicio = time()
    fronteira = deque([inicial])
    visitados = set()
    nos_expandidos = 0

    while fronteira:
        if time() - inicio > tempo_maximo:
            raise TimeoutError("Tempo limite atingido.")

        atual = fronteira.popleft()
        visitados.add(atual)
        nos_expandidos += 1

        if atual.estado == objetivo:
            return atual.caminho(), atual.profundidade, nos_expandidos

        for vizinho in atual.gerar_sucessores():
            if vizinho not in visitados and vizinho not in fronteira:
                fronteira.append(vizinho)

    return [], 0, nos_expandidos

# # Busca em Largura (BFS) usando fila FIFO
# from collections import deque
# from puzzle import Puzzle
# from typing import List, Tuple

# def busca_em_largura(inicial: Puzzle, objetivo: Tuple[int]) -> Tuple[List[str], int, int]:
#     fronteira = deque([inicial])
#     visitados = set()
#     nos_expandidos = 0

#     while fronteira:
#         atual = fronteira.popleft()
#         visitados.add(atual)
#         nos_expandidos += 1

#         if atual.estado == objetivo:
#             return atual.caminho(), atual.profundidade, nos_expandidos

#         for vizinho in atual.gerar_sucessores():
#             if vizinho not in visitados and vizinho not in fronteira:
#                 fronteira.append(vizinho)

#     return [], 0, nos_expandidos
