from puzzle import Puzzle
from heuristicas.foraLugar import heuristica_fora_do_lugar
from heuristicas.manhattan import heuristica_manhattan
from utils.embaralhador import gerar_estado_aleatorio_resolvido  
from utils.tempo import Temporizador
from utils.visualizador import mostrar_caminho

from sem_Informacao.b_Largura import busca_em_largura
from sem_Informacao.b_Profundidade import busca_em_profundidade
from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
from com_Informacao.b_Gulosa import busca_gulosa
from com_Informacao.b_AEstrela import busca_a_estrela

# -------------
# ESTADOS INICIAIS E OBJETIVOS
# -------------

# Para 8 peças (3x3)
estado_3x3 = gerar_estado_aleatorio_resolvido(3)
puzzle_3x3 = Puzzle(estado_3x3, 3)
objetivo_3x3 = (1, 2, 3,
                4, 5, 6,
                7, 8, 0)

# Para 15 peças (4x4)
estado_4x4 = gerar_estado_aleatorio_resolvido(4)
puzzle_4x4 = Puzzle(estado_4x4, 4)
objetivo_4x4 = (1, 2, 3, 4,
                5, 6, 7, 8,
                9, 10, 11, 12,
                13, 14, 15, 0)

# Para 24 peças (5x5)
estado_5x5 = gerar_estado_aleatorio_resolvido(5)
puzzle_5x5 = Puzzle(estado_5x5, 5)
objetivo_5x5 = (1, 2, 3, 4, 5,
                6, 7, 8, 9, 10,
                11, 12, 13, 14, 15,
                16, 17, 18, 19, 20,
                21, 22, 23, 24, 0)

# -------------
# BUSCAS SEM INFORMAÇÃO - 3x3
# -------------
print("\n--- Busca em Largura (BFS) - 8 peças ---")
timer = Temporizador()
timer.iniciar()
acoes, passos, nos = busca_em_largura(puzzle_3x3, objetivo_3x3)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes)
print("Passos:", passos)
print("Nós expandidos:", nos)

print("\n--- Busca em Profundidade (DFS) - 8 peças ---")
timer.iniciar()
acoes_dfs, passos_dfs, nos_dfs = busca_em_profundidade(puzzle_3x3, objetivo_3x3)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes_dfs)
print("Passos:", passos_dfs)
print("Nós expandidos:", nos_dfs)

print("\n--- Busca com Aprofundamento Iterativo (IDS) - 8 peças ---")
timer.iniciar()
caminho_ids, profundidade_ids, nos_ids, solucao_ids = busca_aprofundamento_iterativo(puzzle_3x3, objetivo_3x3)
timer.parar()
timer.imprimir_tempo()
if solucao_ids:
    print("Movimentos:", caminho_ids)
    print("Profundidade:", profundidade_ids)
    print("Nós expandidos:", nos_ids)
    mostrar_caminho(solucao_ids)
else:
    print("Nenhuma solução encontrada.")

# -------------
# BUSCAS SEM INFORMAÇÃO - 4x4
# -------------
print("\n--- Busca em Largura (BFS) - 15 peças ---")
timer.iniciar()
acoes, passos, nos = busca_em_largura(puzzle_4x4, objetivo_4x4)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes)
print("Passos:", passos)
print("Nós expandidos:", nos)

print("\n--- Busca em Profundidade (DFS) - 15 peças ---")
timer.iniciar()
acoes_dfs, passos_dfs, nos_dfs = busca_em_profundidade(puzzle_4x4, objetivo_4x4)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes_dfs)
print("Passos:", passos_dfs)
print("Nós expandidos:", nos_dfs)

print("\n--- Busca com Aprofundamento Iterativo (IDS) - 15 peças ---")
timer.iniciar()
caminho_ids, profundidade_ids, nos_ids, solucao_ids = busca_aprofundamento_iterativo(puzzle_4x4, objetivo_4x4)
timer.parar()
timer.imprimir_tempo()
if solucao_ids:
    print("Movimentos:", caminho_ids)
    print("Profundidade:", profundidade_ids)
    print("Nós expandidos:", nos_ids)
    mostrar_caminho(solucao_ids)
else:
    print("Nenhuma solução encontrada.")

# -------------
# BUSCAS COM INFORMAÇÃO - 3x3
# -------------
print("\n--- Busca Gulosa - 8 peças ---")
timer.iniciar()
resultado_gulosa = busca_gulosa(puzzle_3x3.estado, puzzle_3x3.tamanho, objetivo_3x3, heuristica_fora_do_lugar)
timer.parar()
timer.imprimir_tempo()
if resultado_gulosa:
    print("Movimentos:", resultado_gulosa.caminho())
    print("Profundidade:", resultado_gulosa.profundidade)
    mostrar_caminho(resultado_gulosa)
else:
    print("Nenhuma solução encontrada com busca gulosa.")

print("\n--- Busca A* - 8 peças ---")
timer.iniciar()
resultado_astar = busca_a_estrela(puzzle_3x3.estado, puzzle_3x3.tamanho, objetivo_3x3, heuristica_manhattan)
timer.parar()
timer.imprimir_tempo()
if resultado_astar:
    print("Movimentos:", resultado_astar.caminho())
    print("Profundidade:", resultado_astar.profundidade)
    mostrar_caminho(resultado_astar)
else:
    print("Nenhuma solução encontrada com A*.")

# -------------
# BUSCAS COM INFORMAÇÃO - 4x4
# -------------
print("\n--- Busca Gulosa - 15 peças ---")
timer.iniciar()
resultado_gulosa = busca_gulosa(puzzle_4x4.estado, puzzle_4x4.tamanho, objetivo_4x4, heuristica_fora_do_lugar)
timer.parar()
timer.imprimir_tempo()
if resultado_gulosa:
    print("Movimentos:", resultado_gulosa.caminho())
    print("Profundidade:", resultado_gulosa.profundidade)
    mostrar_caminho(resultado_gulosa)
else:
    print("Nenhuma solução encontrada com busca gulosa.")

print("\n--- Busca A* - 15 peças ---")
timer.iniciar()
resultado_astar = busca_a_estrela(puzzle_4x4.estado, puzzle_4x4.tamanho, objetivo_4x4, heuristica_manhattan)
timer.parar()
timer.imprimir_tempo()
if resultado_astar:
    print("Movimentos:", resultado_astar.caminho())
    print("Profundidade:", resultado_astar.profundidade)
    mostrar_caminho(resultado_astar)
else:
    print("Nenhuma solução encontrada com A*.")

# -------------
# BUSCAS COM INFORMAÇÃO - 5x5
# -------------
print("\n--- Busca Gulosa - 24 peças ---")
timer.iniciar()
resultado_gulosa = busca_gulosa(puzzle_5x5.estado, puzzle_5x5.tamanho, objetivo_5x5, heuristica_fora_do_lugar)
timer.parar()
timer.imprimir_tempo()
if resultado_gulosa:
    print("Movimentos:", resultado_gulosa.caminho())
    print("Profundidade:", resultado_gulosa.profundidade)
    mostrar_caminho(resultado_gulosa)
else:
    print("Nenhuma solução encontrada com busca gulosa.")

print("\n--- Busca A* - 24 peças ---")
timer.iniciar()
resultado_astar = busca_a_estrela(puzzle_5x5.estado, puzzle_5x5.tamanho, objetivo_5x5, heuristica_manhattan)
timer.parar()
timer.imprimir_tempo()
if resultado_astar:
    print("Movimentos:", resultado_astar.caminho())
    print("Profundidade:", resultado_astar.profundidade)
    mostrar_caminho(resultado_astar)
else:
    print("Nenhuma solução encontrada com A*.")
