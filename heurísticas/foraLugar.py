# Heurística: número de peças fora do lugar
from puzzle import Puzzle
from typing import Tuple

def heuristica_fora_do_lugar(puzzle: Puzzle, objetivo: Tuple[int]) -> int:
    return sum(1 for i, val in enumerate(puzzle.estado) if val != 0 and val != objetivo[i])
