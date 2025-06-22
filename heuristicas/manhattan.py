# Heurística: Distância de Manhattan
from puzzle import Puzzle
from typing import Tuple

def heuristica_manhattan(puzzle: Puzzle, objetivo: Tuple[int]) -> int:
    distancia = 0
    for i, val in enumerate(puzzle.estado):
        if val != 0:
            pos_atual = divmod(i, puzzle.tamanho)
            pos_objetivo = divmod(objetivo.index(val), puzzle.tamanho)
            distancia += abs(pos_atual[0] - pos_objetivo[0]) + abs(pos_atual[1] - pos_objetivo[1])
    return distancia
