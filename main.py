from problema import Problema
from sem_Informacao.b_Largura import busca_largura
from sem_Informacao.b_Profundidade import busca_profundidade
from com_Informacao.b_AEstrela import busca_a_estrela
from com_Informacao.b_Gulosa import busca_gulosa

def main():
    problema = Problema()

    resultado = busca_largura(problema)
    print("Busca em Largura:", resultado)

    resultado = busca_profundidade(problema)
    print("Busca em Profundidade:", resultado)

    resultado = busca_a_estrela(problema)
    print("Busca A*:", resultado)

    resultado = busca_gulosa(problema)
    print("Busca Gulosa:", resultado)

if __name__ == "__main__":
    main()
