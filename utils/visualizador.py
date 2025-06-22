# Mostra o caminho da solução visualmente (em texto)
from puzzle import Puzzle

def mostrar_estado(puzzle: Puzzle):
    tamanho = puzzle.tamanho
    for i in range(0, len(puzzle.estado), tamanho):
        linha = puzzle.estado[i:i + tamanho]
        print(" ".join(str(n) if n != 0 else "_" for n in linha))
    print()

def mostrar_caminho(puzzle: Puzzle):
    caminho = []
    atual = puzzle
    while atual:
        caminho.append(atual)
        atual = atual.pai
    for estado in reversed(caminho):
        mostrar_estado(estado)
