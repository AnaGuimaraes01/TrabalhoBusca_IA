import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problema import PuzzleProblem  # Importa a classe que define o problema do puzzle

# -----------------------------
# Função de Busca em Profundidade (DFS)
# -----------------------------
def depthFirstSearch(problem):
    # A fronteira começa com o estado inicial e o caminho vazio até ele
    frontier = [(problem.getStartState(), [])]  # Lista funciona como pilha (LIFO)
    explored = set()  # Conjunto de estados já visitados, para evitar repetição

    while frontier:
        # Remove o último item da pilha (comportamento LIFO)
        state, path = frontier.pop()

        # Se já visitou esse estado, ignora e continua
        if state in explored:
            continue

        # Marca o estado como visitado
        explored.add(state)

        # Verifica se o estado atual é o objetivo
        if problem.isGoalState(state):
            return path  # Retorna o caminho (lista de ações) até a solução

        # Para cada sucessor gerado a partir do estado atual
        for successor, action, cost in problem.getSuccessors(state):
            # Cria o novo caminho acumulando a ação feita
            new_path = path + [action]
            # Adiciona o novo estado e seu caminho à pilha
            frontier.append((successor, new_path))

    return []  # Se não encontrar solução, retorna lista vazia


# ---------- TESTE DIRETO -------------
if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    start_tuple = tuple(tuple(row) for row in start)
    goal_tuple = tuple(tuple(row) for row in goal)

    problema = PuzzleProblem(start_tuple, goal_tuple)
    caminho = depthFirstSearch(problema)

    print("\nSolução encontrada com DFS:")
    print("→", " → ".join(caminho))
    print("Número de passos:", len(caminho))
