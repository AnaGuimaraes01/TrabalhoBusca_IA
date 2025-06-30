from puzzle import Puzzle
from heuristicas.foraLugar import heuristica_fora_do_lugar
from heuristicas.manhattan import heuristica_manhattan
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

        if tamanho == 3:
            estado_inicial = (4, 1, 2,
                              0, 7, 3,
                              8, 5, 6)
        elif tamanho == 4:
            estado_inicial = (1, 2, 3, 4,
                              5, 6, 0, 8,
                              9, 10, 7, 12,
                              13, 14, 11, 15)
        elif tamanho == 5:
            estado_inicial = (1, 2, 3, 4, 5,
                              6, 7, 8, 9, 10,
                              11, 0, 13, 14, 15,
                              16, 12, 18, 19, 20,
                              21, 17, 22, 23, 24)

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
                resultado, nos = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
                caminho = resultado.caminho() if resultado else []
                passos = resultado.profundidade if resultado else 0
            elif algoritmo == "aestrela":
                resultado, nos = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
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
