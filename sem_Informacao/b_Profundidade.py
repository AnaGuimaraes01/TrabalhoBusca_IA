# Busca em Profundidade (DFS) com limite de profundidade
from puzzle import Puzzle
from typing import List, Tuple

def busca_em_profundidade(inicial: Puzzle, objetivo: Tuple[int], limite: int = 50) -> Tuple[List[str], int, int]:
    fronteira = [inicial]
    visitados = set()
    nos_expandidos = 0

    while fronteira:
        atual = fronteira.pop()
        visitados.add(atual)
        nos_expandidos += 1

        if atual.estado == objetivo:
            return atual.caminho(), atual.profundidade, nos_expandidos

        if atual.profundidade < limite:
            for vizinho in reversed(atual.gerar_sucessores()):
                if vizinho not in visitados:
                    fronteira.append(vizinho)

    return [], 0, nos_expandidos
