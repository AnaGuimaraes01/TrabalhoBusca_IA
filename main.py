from puzzle import Puzzle
from heuristicas.foraLugar import heuristica_fora_do_lugar
from heuristicas.manhattan import heuristica_manhattan
from utils.embaralhador import gerar_estado_aleatorio_resolvido
from time import time

from sem_Informacao.b_Largura import busca_em_largura
from sem_Informacao.b_Profundidade import busca_em_profundidade
from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
from com_Informacao.b_Gulosa import busca_gulosa
from com_Informacao.b_AEstrela import busca_a_estrela


def executar_para_tamanhos(algoritmo, heuristica=None):
    tamanhos = [3, 4] if algoritmo in ["largura", "profundidade", "ids"] else [3, 4, 5]

    for tamanho in tamanhos:
        print(f"\n=== Puzzle {tamanho}x{tamanho} ===")
        estado_inicial = gerar_estado_aleatorio_resolvido(tamanho)
        objetivo = tuple(list(range(1, tamanho * tamanho)) + [0])
        puzzle = Puzzle(estado_inicial, tamanho)

        print("\nEstado Inicial vs Estado Objetivo:")
        for i in range(tamanho):
            print(f"{puzzle.estado[i*tamanho:(i+1)*tamanho]}   =>   {list(objetivo)[i*tamanho:(i+1)*tamanho]}")

        inicio = time()
        caminho = []
        passos = 0
        nos = None
        resultado = None

        try:
            if algoritmo == "largura":
                caminho, passos, nos = busca_em_largura(puzzle, objetivo)
            elif algoritmo == "profundidade":
                caminho, passos, nos = busca_em_profundidade(puzzle, objetivo, tempo_maximo=60, limite=400)
            elif algoritmo == "ids":
                caminho, passos, nos, _ = busca_aprofundamento_iterativo(puzzle, objetivo, limite_max=60)
            elif algoritmo == "gulosa":
                resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
                caminho = resultado.caminho() if resultado else []
                passos = resultado.profundidade if resultado else 0
            elif algoritmo == "aestrela":
                resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
                caminho = resultado.caminho() if resultado else []
                passos = resultado.profundidade if resultado else 0
        except TimeoutError:
            print("⏳ Tempo limite atingido.")
            caminho, passos, nos = [], 0, 0

        fim = time()

        print("\nResultado:")
        print("Movimentos:", caminho if caminho else "Nenhum")
        print("Passos:", passos)
        if nos is not None:
            print("Nós expandidos:", nos)
        print(f"Tempo: {fim - inicio:.2f} segundos")

        print("\nCaminho percorrido até o objetivo:")

        if algoritmo in ["largura", "profundidade", "ids"]:
            if caminho:
                estado_atual = Puzzle(estado_inicial, tamanho)
                print("Passo 0 (inicial):")
                for i in range(tamanho):
                    print(estado_atual.estado[i*tamanho:(i+1)*tamanho])
                print()
                for idx, movimento in enumerate(caminho, 1):
                    for filho in estado_atual.gerar_sucessores():
                        if filho.acao == movimento:
                            estado_atual = filho
                            break
                    print(f"Passo {idx}:")
                    for i in range(tamanho):
                        print(estado_atual.estado[i*tamanho:(i+1)*tamanho])
                    print()
        elif resultado:
            estados = resultado.caminho_estados()
            for idx, estado in enumerate(estados):
                print(f"Passo {idx}:")
                for i in range(tamanho):
                    print(estado[i*tamanho:(i+1)*tamanho])
                print()


def menu_algoritmos():
    while True:
        print("\n=== Menu - Escolha o algoritmo ===")
        print("1 - Busca em Largura (BFS)")
        print("2 - Busca em Profundidade (DFS)")
        print("3 - Aprofundamento Iterativo (IDS)")
        print("4 - Busca Gulosa")
        print("5 - Busca A* (A Estrela)")
        print("0 - Sair")

        escolha = input("Opção: ")
        if escolha == "0":
            break
        elif escolha == "1":
            executar_para_tamanhos("largura")
        elif escolha == "2":
            executar_para_tamanhos("profundidade")
        elif escolha == "3":
            executar_para_tamanhos("ids")
        elif escolha == "4":
            executar_para_tamanhos("gulosa", heuristica_fora_do_lugar)
        elif escolha == "5":
            executar_para_tamanhos("aestrela", heuristica_manhattan)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_algoritmos()






























# from puzzle import Puzzle
# from heuristicas.foraLugar import heuristica_fora_do_lugar
# from heuristicas.manhattan import heuristica_manhattan
# from utils.embaralhador import gerar_estado_aleatorio_resolvido
# from time import time

# from sem_Informacao.b_Largura import busca_em_largura
# from sem_Informacao.b_Profundidade import busca_em_profundidade
# from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
# from com_Informacao.b_Gulosa import busca_gulosa
# from com_Informacao.b_AEstrela import busca_a_estrela


# def executar_para_tamanhos(algoritmo, heuristica=None):
#     tamanhos = [3, 4] if algoritmo in ["largura", "profundidade", "ids"] else [3, 4, 5]

#     for tamanho in tamanhos:
#         print(f"\n=== Puzzle {tamanho}x{tamanho} ===")
#         estado_inicial = gerar_estado_aleatorio_resolvido(tamanho)
#         objetivo = tuple(list(range(1, tamanho * tamanho)) + [0])
#         puzzle = Puzzle(estado_inicial, tamanho)

#         print("\nEstado Inicial vs Estado Objetivo:")
#         for i in range(tamanho):
#             linha_inicial = puzzle.estado[i*tamanho:(i+1)*tamanho]
#             linha_objetivo = objetivo[i*tamanho:(i+1)*tamanho]
#             print(f"{linha_inicial}   =>   {linha_objetivo}")

#         inicio = time()

#         caminho = []
#         passos = 0
#         nos = None

#         try:
#             if algoritmo == "largura":
#                 caminho, passos, nos = busca_em_largura(puzzle, objetivo, tempo_maximo=30)
#             elif algoritmo == "profundidade":
#                 caminho, passos, nos = busca_em_profundidade(puzzle, objetivo, tempo_maximo=60, limite=400)
#             elif algoritmo == "ids":
#                 caminho, passos, nos, _ = busca_aprofundamento_iterativo(puzzle, objetivo, tempo_maximo=60)
#             elif algoritmo == "gulosa":
#                 resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica, tempo_maximo=60)
#                 caminho = resultado.caminho() if resultado else []
#                 passos = resultado.profundidade if resultado else 0
#             elif algoritmo == "aestrela":
#                 resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica, tempo_maximo=60)
#                 caminho = resultado.caminho() if resultado else []
#                 passos = resultado.profundidade if resultado else 0
#         except TimeoutError:
#             print("⏳ Tempo limite atingido.")
#             caminho, passos, nos = [], 0, 0

#         fim = time()

#         print("\nResultado:")
#         print("Movimentos:", caminho if caminho else "Nenhum")
#         print("Passos:", passos)
#         if nos is not None:
#             print("Nós expandidos:", nos)
#         print(f"Tempo: {fim - inicio:.2f} segundos")

#         # Mostra o caminho completo em estados
#         if caminho:
#             print("\nCaminho percorrido até o objetivo:")
#             estado_atual = list(puzzle.estado)
#             print("Estado inicial:")
#             for i in range(tamanho):
#                 print(estado_atual[i*tamanho:(i+1)*tamanho])
#             for movimento in caminho:
#                 estado_atual = Puzzle.mover(estado_atual, tamanho, movimento)
#                 print(f"\nMovimento: {movimento}")
#                 for i in range(tamanho):
#                     print(estado_atual[i*tamanho:(i+1)*tamanho])
#         print("\n" + "="*40 + "\n")


# def menu_algoritmos():
#     while True:
#         print("=== Menu - Escolha o algoritmo ===")
#         print("1 - Busca em Largura (BFS)")
#         print("2 - Busca em Profundidade (DFS)")
#         print("3 - Aprofundamento Iterativo (IDS)")
#         print("4 - Busca Gulosa")
#         print("5 - Busca A* (A Estrela)")
#         print("0 - Sair")

#         escolha = input("Opção: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             executar_para_tamanhos("largura")
#         elif escolha == "2":
#             executar_para_tamanhos("profundidade")
#         elif escolha == "3":
#             executar_para_tamanhos("ids")
#         elif escolha == "4":
#             executar_para_tamanhos("gulosa", heuristica_fora_do_lugar)
#         elif escolha == "5":
#             executar_para_tamanhos("aestrela", heuristica_manhattan)
#         else:
#             print("Opção inválida.")

# if __name__ == "__main__":
#     menu_algoritmos()

# from puzzle import Puzzle
# from heuristicas.foraLugar import heuristica_fora_do_lugar
# from heuristicas.manhattan import heuristica_manhattan
# from utils.embaralhador import gerar_estado_aleatorio_resolvido
# from time import time

# from sem_Informacao.b_Largura import busca_em_largura
# from sem_Informacao.b_Profundidade import busca_em_profundidade
# from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
# from com_Informacao.b_Gulosa import busca_gulosa
# from com_Informacao.b_AEstrela import busca_a_estrela


# def executar_para_tamanhos(algoritmo, heuristica=None):
#     tamanhos = [3, 4] if algoritmo in ["largura", "profundidade", "ids"] else [3, 4, 5]

#     for tamanho in tamanhos:
#         print(f"\n=== Puzzle {tamanho}x{tamanho} ===")
#         estado_inicial = gerar_estado_aleatorio_resolvido(tamanho)
#         objetivo = tuple(list(range(1, tamanho * tamanho)) + [0])
#         puzzle = Puzzle(estado_inicial, tamanho)

#         print("Estado inicial:")
#         for i in range(tamanho):
#             print(puzzle.estado[i*tamanho:(i+1)*tamanho])

#         inicio = time()

#         caminho = []
#         passos = 0
#         nos = None

#         try:
#             if algoritmo == "largura":
#                 caminho, passos, nos = busca_em_largura(puzzle, objetivo, tempo_maximo=30)
#             elif algoritmo == "profundidade":
#                 # AQUI aplicamos tempo e profundidade máxima controlada
#                 caminho, passos, nos = busca_em_profundidade(puzzle, objetivo, tempo_maximo=60, limite=400)
#             elif algoritmo == "ids":
#                 caminho, passos, nos, _ = busca_aprofundamento_iterativo(puzzle, objetivo, tempo_maximo=60)
#             elif algoritmo == "gulosa":
#                 resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica, tempo_maximo=60)
#                 caminho = resultado.caminho() if resultado else []
#                 passos = resultado.profundidade if resultado else 0
#             elif algoritmo == "aestrela":
#                 resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica, tempo_maximo=60)
#                 caminho = resultado.caminho() if resultado else []
#                 passos = resultado.profundidade if resultado else 0
#         except TimeoutError:
#             print("⏳ Tempo limite atingido.")
#             caminho, passos, nos = [], 0, 0

#         fim = time()

#         print("\nResultado:")
#         print("Movimentos:", caminho if caminho else "Nenhum")
#         print("Passos:", passos)
#         if nos is not None:
#             print("Nós expandidos:", nos)
#         print(f"Tempo: {fim - inicio:.2f} segundos\n")


# def menu_algoritmos():
#     while True:
#         print("=== Menu - Escolha o algoritmo ===")
#         print("1 - Busca em Largura (BFS)")
#         print("2 - Busca em Profundidade (DFS)")
#         print("3 - Aprofundamento Iterativo (IDS)")
#         print("4 - Busca Gulosa")
#         print("5 - Busca A* (A Estrela)")
#         print("0 - Sair")

#         escolha = input("Opção: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             executar_para_tamanhos("largura")
#         elif escolha == "2":
#             executar_para_tamanhos("profundidade")
#         elif escolha == "3":
#             executar_para_tamanhos("ids")
#         elif escolha == "4":
#             executar_para_tamanhos("gulosa", heuristica_fora_do_lugar)
#         elif escolha == "5":
#             executar_para_tamanhos("aestrela", heuristica_manhattan)
#         else:
#             print("Opção inválida.")

# if __name__ == "__main__":
#     menu_algoritmos()



# from puzzle import Puzzle
# from heuristicas.foraLugar import heuristica_fora_do_lugar
# from heuristicas.manhattan import heuristica_manhattan
# from utils.embaralhador import gerar_estado_aleatorio_resolvido
# from time import time

# from sem_Informacao.b_Largura import busca_em_largura
# from sem_Informacao.b_Profundidade import busca_em_profundidade
# from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
# from com_Informacao.b_Gulosa import busca_gulosa
# from com_Informacao.b_AEstrela import busca_a_estrela

# def executar_para_tamanhos(algoritmo, heuristica=None):
#     if algoritmo in ["largura", "profundidade", "ids"]:
#         tamanhos = [3, 4]  # Apenas 8 e 15 peças
#     else:
#         tamanhos = [3, 4, 5]  # 8, 15 e 24 peças

#     for tamanho in tamanhos:
#         print(f"\n=== Puzzle {tamanho}x{tamanho} ===")
#         estado_inicial = gerar_estado_aleatorio_resolvido(tamanho)
#         objetivo = tuple(list(range(1, tamanho * tamanho)) + [0])
#         puzzle = Puzzle(estado_inicial, tamanho)

#         print("Estado inicial:")
#         for i in range(tamanho):
#             print(puzzle.estado[i*tamanho:(i+1)*tamanho])

#         inicio = time()

#         if algoritmo == "largura":
#             caminho, passos, nos = busca_em_largura(puzzle, objetivo)
#         elif algoritmo == "profundidade":
#             caminho, passos, nos = busca_em_profundidade(puzzle, objetivo)
#         elif algoritmo == "ids":
#             caminho, passos, nos, _ = busca_aprofundamento_iterativo(puzzle, objetivo)
#         elif algoritmo == "gulosa":
#             resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
#             caminho = resultado.caminho() if resultado else []
#             passos = resultado.profundidade if resultado else 0
#             nos = None
#         elif algoritmo == "aestrela":
#             resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
#             caminho = resultado.caminho() if resultado else []
#             passos = resultado.profundidade if resultado else 0
#             nos = None
#         else:
#             print("Algoritmo inválido.")
#             return

#         fim = time()

#         print("\nResultado:")
#         print("Movimentos:", caminho if caminho else "Nenhum")
#         print("Passos:", passos)
#         if nos is not None:
#             print("Nós expandidos:", nos)
#         print(f"Tempo: {fim - inicio:.2f} segundos\n")


# def menu_algoritmos():
#     while True:
#         print("=== Menu - Escolha o algoritmo ===")
#         print("1 - Busca em Largura (BFS)")
#         print("2 - Busca em Profundidade (DFS)")
#         print("3 - Aprofundamento Iterativo (IDS)")
#         print("4 - Busca Gulosa")
#         print("5 - Busca A* (A Estrela)")
#         print("0 - Sair")

#         escolha = input("Opção: ")
#         if escolha == "0":
#             break
#         elif escolha == "1":
#             executar_para_tamanhos("largura")
#         elif escolha == "2":
#             executar_para_tamanhos("profundidade")
#         elif escolha == "3":
#             executar_para_tamanhos("ids")
#         elif escolha == "4":
#             executar_para_tamanhos("gulosa", heuristica_fora_do_lugar)
#         elif escolha == "5":
#             executar_para_tamanhos("aestrela", heuristica_manhattan)
#         else:
#             print("Opção inválida.")

# if __name__ == "__main__":
#     menu_algoritmos()




# # from puzzle import Puzzle
# # from heuristicas.foraLugar import heuristica_fora_do_lugar
# # from heuristicas.manhattan import heuristica_manhattan
# # from utils.embaralhador import gerar_estado_aleatorio_resolvido
# # from time import time

# # from sem_Informacao.b_Largura import busca_em_largura
# # from sem_Informacao.b_Profundidade import busca_em_profundidade
# # from sem_Informacao.b_ProfundidadeIterativa import busca_aprofundamento_iterativo
# # from com_Informacao.b_Gulosa import busca_gulosa
# # from com_Informacao.b_AEstrela import busca_a_estrela

# # def executar_para_tamanhos(algoritmo, heuristica=None):
# #     for tamanho in [3, 4, 5]:
# #         print(f"\n=== Puzzle {tamanho}x{tamanho} ===")
# #         estado_inicial = gerar_estado_aleatorio_resolvido(tamanho)
# #         objetivo = tuple(list(range(1, tamanho * tamanho)) + [0])
# #         puzzle = Puzzle(estado_inicial, tamanho)

# #         print("Estado inicial:")
# #         for i in range(tamanho):
# #             linha = puzzle.estado[i*tamanho:(i+1)*tamanho]
# #             print(linha)

# #         inicio = time()

# #         if algoritmo == "largura":
# #             caminho, passos, nos = busca_em_largura(puzzle, objetivo)
# #         elif algoritmo == "profundidade":
# #             caminho, passos, nos = busca_em_profundidade(puzzle, objetivo)
# #         elif algoritmo == "ids":
# #             caminho, passos, nos, _ = busca_aprofundamento_iterativo(puzzle, objetivo)
# #         elif algoritmo == "gulosa":
# #             resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
# #             caminho = resultado.caminho() if resultado else []
# #             passos = resultado.profundidade if resultado else 0
# #             nos = None
# #         elif algoritmo == "aestrela":
# #             resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
# #             caminho = resultado.caminho() if resultado else []
# #             passos = resultado.profundidade if resultado else 0
# #             nos = None
# #         else:
# #             print("Algoritmo inválido.")
# #             return

# #         fim = time()

# #         print("\nResultado:")
# #         print("Movimentos:", caminho if caminho else "Nenhum")
# #         print("Passos:", passos)
# #         if nos is not None:
# #             print("Nós expandidos:", nos)
# #         print(f"Tempo: {fim - inicio:.2f} segundos\n")

# # def menu_algoritmos():
# #     while True:
# #         print("=== Menu - Escolha o algoritmo ===")
# #         print("1 - Busca em Largura (BFS)")
# #         print("2 - Busca em Profundidade (DFS)")
# #         print("3 - Aprofundamento Iterativo (IDS)")
# #         print("4 - Busca Gulosa")
# #         print("5 - Busca A* (A Estrela)")
# #         print("0 - Sair")

# #         escolha = input("Opção: ")
# #         if escolha == "0":
# #             break
# #         elif escolha == "1":
# #             executar_para_tamanhos("largura")
# #         elif escolha == "2":
# #             executar_para_tamanhos("profundidade")
# #         elif escolha == "3":
# #             executar_para_tamanhos("ids")
# #         elif escolha == "4":
# #             executar_para_tamanhos("gulosa", heuristica_fora_do_lugar)
# #         elif escolha == "5":
# #             executar_para_tamanhos("aestrela", heuristica_manhattan)
# #         else:
# #             print("Opção inválida.")

# # if __name__ == "__main__":
# #     menu_algoritmos()
