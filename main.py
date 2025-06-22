from puzzle import Puzzle
from heurísticas.foraLugar import heuristica_fora_do_lugar
from heurísticas.manhattan import heuristica_manhattan
from utils.embaralhador import gerar_estado_aleatorio_resolvido #novo (eduarda)
from utils.tempo import Temporizador
from utils.visualizador import mostrar_caminho

from sem_Informacao.b_Largura import busca_em_largura
from sem_Informacao.b_Profundidade import busca_em_profundidade
from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
from com_Informacao.b_Gulosa import busca_gulosa
from com_Informacao.b_AEstrela import busca_a_estrela


# inicial = Puzzle((2, 3, 0,
#                   1, 5, 6,
#                   4, 7, 8), 3)



#novo estado inicial (eduarda)
# Para 8 peças
estado_inicial = gerar_estado_aleatorio_resolvido(3)
inicial = Puzzle(estado_inicial, 3)

# Para 15 peças:
# estado_inicial = gerar_estado_aleatorio_resolvido(4)
# inicial = Puzzle(estado_inicial, 4)

# Para 24 peças:
# estado_inicial = gerar_estado_aleatorio_resolvido(5)
# inicial = Puzzle(estado_inicial, 5)

objetivo = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

# Busca em Largura
print("\n--- Busca em Largura (BFS) ---")
timer = Temporizador()
timer.iniciar()
acoes, passos, nos = busca_em_largura(inicial, objetivo)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes)
print("Passos:", passos)
print("Nós expandidos:", nos)

# Busca em Profundidade
print("\n--- Busca em Profundidade (DFS) ---")
timer = Temporizador()
timer.iniciar()
acoes_dfs, passos_dfs, nos_dfs = busca_em_profundidade(inicial, objetivo)
timer.parar()
timer.imprimir_tempo()
print("Ações:", acoes_dfs)
print("Passos:", passos_dfs)
print("Nós expandidos:", nos_dfs)

# Busca com Aprofundamento Iterativo
print("\n--- Busca com Aprofundamento Iterativo (IDS) ---")
timer = Temporizador()
timer.iniciar()
caminho_ids, profundidade_ids, nos_ids, solucao_ids = busca_aprofundamento_iterativo(inicial, objetivo)
timer.parar()
timer.imprimir_tempo()
if solucao_ids:
    print("Movimentos:", caminho_ids)
    print("Profundidade:", profundidade_ids)
    print("Nós expandidos:", nos_ids)
    mostrar_caminho(solucao_ids)
else:
    print("Nenhuma solução encontrada.")

# Busca Gulosa com heurística "fora do lugar"
print("\n--- Busca Gulosa ---")
timer = Temporizador()
timer.iniciar()
resultado_gulosa = busca_gulosa(inicial.estado, inicial.tamanho, objetivo, heuristica_fora_do_lugar)
timer.parar()
timer.imprimir_tempo()
if resultado_gulosa:
    print("Movimentos:", resultado_gulosa.caminho())
    print("Profundidade:", resultado_gulosa.profundidade)
    mostrar_caminho(resultado_gulosa)
else:
    print("Nenhuma solução encontrada com busca gulosa.")

# Busca A*
print("\n--- Busca A* ---")
timer = Temporizador()
timer.iniciar()
resultado_astar = busca_a_estrela(inicial.estado, inicial.tamanho, objetivo, heuristica_manhattan)
timer.parar()
timer.imprimir_tempo()
if resultado_astar:
    print("Movimentos:", resultado_astar.caminho())
    print("Profundidade:", resultado_astar.profundidade)
    mostrar_caminho(resultado_astar)
else:
    print("Nenhuma solução encontrada com A*.")
