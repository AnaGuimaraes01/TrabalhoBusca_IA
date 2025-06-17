
# Trabalho de Inteligência Artificial
Resolução do Problema n-Puzzle por meio de Algoritmos de Busca sem Informação
e com informação.

# Problema 
• O n-puzzle é um jogo de tabuleiro composto por uma grade n x n contendo n
peças numeradas de 1 a n-1 e uma posição vazia. As peças podem ser movidas
para a posição vazia adjacente (em cima, embaixo, à esquerda ou à direita). O
objetivo é transformar uma configuração inicial em uma configuração
objetivo.

• Dado um estado inicial do tabuleiro, encontrar a sequência de movimentos
que leva ao estado objetivo.

# Utilizando os seguintes algoritmos:
• Sem informação:
o Busca em Largura (Breadth-First Search - BFS).
o Busca em Profundidade (Deep-First Search - DFS)
o Busca com Aprofundamento Iterativo (Iterative Deepening Search -
IDS).
• Com informação:
o A* (A Estrela).
o Busca Gulosa (Greedy Best-First Search).

# Especificações técnicas:
• O programa deverá receber como entrada uma configuração inicial do
tabuleiro (ex: lista, string ou matriz nxn).
• O programa deverá apresentar como saída:
o A sequência de movimentos realizados.
o O número total de passos.
o O tempo de execução.
o A árvore ou caminho de busca encontrado.

# Parte 1 – Buscas Sem Informação
Tarefas
1. Tipos de puzzle implementados: 8 e 15 números.
2. Formulação do problema, especificando:
o Representação dos estados.
o Estado inicial e estado objetivo.
o Conjunto de operadores (ações possíveis: mover peça para cima, baixo,
esquerda, direita).
o Condição de objetivo.
o Custo de cada ação (assumir custo uniforme = 1).
3. Geração da árvore de busca:
o Exibir o caminho do estado inicial até o estado objetivo.
o Apresentar a árvore gerada, evidenciando o caminho correto (pode ser
via estrutura textual ou visual opcional).
4. Análise Comparativa dos Algoritmos:
o Comparar o número de nós expandidos.
o Comparar o tempo de execução.
o Quantidade de estados expandidos.
o Profundidade da solução.
o Apresentar os dados em forma de gráficos e tabelas no relatório.

# Parte 2 – Buscas Com Informação
Tarefas
1. Tipos de puzzle implementados: 8, 15 e 24 números.
2. Formulação do problema, destacando novamente os elementos essenciais e a
introdução de heurísticas admissíveis:
o Heurísticas:
▪ Número de peças fora do lugar.
▪ Soma das distâncias de Manhattan das peças até suas posições
corretas.
3. Geração da árvore de busca:
o Exibir o caminho do estado inicial até o estado objetivo.
o Apresentar a árvore gerada, evidenciando o caminho correto (pode ser
via estrutura textual ou visual opcional).

# Relatório com análise comparativa:
▪ Comparar o número de nós expandidos.
▪ Comparar o tempo de execução.
▪ Quantidade de estados expandidos.
▪ Profundidade da solução.
▪ Efetividade de cada heurística.

# o Apresentar gráficos comparativos e tabelas.
o Discutir quais heurísticas e algoritmos são mais eficazes para diferentes
dificuldades.
Juntamente com o programa implementado deverá ser entregue um relatório
contendo as informações solicitadas anteriormente, além do vídeo já acordado
anteriormente.