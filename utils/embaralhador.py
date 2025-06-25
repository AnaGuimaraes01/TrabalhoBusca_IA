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

