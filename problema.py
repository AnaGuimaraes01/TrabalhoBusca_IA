
class PuzzleProblem:
    def __init__(self, start_state, goal_state):
        self.start = start_state
        self.goal = goal_state

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        successors = []
        n = len(state)
        grid = [list(row) for row in state]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    x, y = i, j

        movimentos = {
            "cima": (x - 1, y),
            "baixo": (x + 1, y),
            "esquerda": (x, y - 1),
            "direita": (x, y + 1)
        }

        for acao, (nx, ny) in movimentos.items():
            if 0 <= nx < n and 0 <= ny < n:
                novo_grid = [row[:] for row in grid]
                novo_grid[x][y], novo_grid[nx][ny] = novo_grid[nx][ny], novo_grid[x][y]
                novo_estado = tuple(tuple(row) for row in novo_grid)
                successors.append((novo_estado, acao, 1))

        return successors
