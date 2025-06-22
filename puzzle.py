from typing import List, Optional, Tuple

class Puzzle:
    def __init__(self, estado: Tuple[int], tamanho: int, pai: Optional['Puzzle'] = None, acao: Optional[str] = None, profundidade: int = 0):
        self.estado = estado
        self.tamanho = tamanho
        self.pai = pai
        self.acao = acao
        self.profundidade = profundidade

    def __eq__(self, other):
        return self.estado == other.estado

    def __hash__(self):
        return hash(self.estado)

    def posicao_zero(self) -> int:
        return self.estado.index(0)

    def gerar_sucessores(self) -> List['Puzzle']:
        sucessores = []
        i = self.posicao_zero()
        linha, coluna = divmod(i, self.tamanho)

        movimentos = {
            'cima': (linha > 0, -self.tamanho),
            'baixo': (linha < self.tamanho - 1, self.tamanho),
            'esquerda': (coluna > 0, -1),
            'direita': (coluna < self.tamanho - 1, 1)
        }

        for direcao, (condicao, deslocamento) in movimentos.items():
            if condicao:
                novo_estado = list(self.estado)
                j = i + deslocamento
                novo_estado[i], novo_estado[j] = novo_estado[j], novo_estado[i]
                sucessores.append(Puzzle(tuple(novo_estado), self.tamanho, self, direcao, self.profundidade + 1))

        return sucessores

    def caminho(self) -> List[str]:
        """Retorna a sequência de ações do estado inicial ate o no explorado"""
        acoes = []
        atual = self
        while atual.pai is not None:
            acoes.append(atual.acao)
            atual = atual.pai
        return list(reversed(acoes))