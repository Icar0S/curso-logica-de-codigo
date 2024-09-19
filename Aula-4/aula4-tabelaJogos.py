import random

# Função que gera a tabela de jogos entre as equipes
def gerar_tabela_de_jogos(equipes):
    tabela = []  # Cria uma lista vazia que irá armazenar as partidas
    # Primeiro loop para selecionar uma equipe
    for i in range(len(equipes)):
        # Segundo loop para selecionar outra equipe sem repetir o confronto
        for j in range(i + 1, len(equipes)):
            # Adiciona o par de equipes (partida) na lista de jogos
            tabela.append((equipes[i], equipes[j]))
    # Embaralha a ordem dos jogos . O shuffle() não cria uma nova lista. altera a lista que foi passada
    random.shuffle(tabela)
    return tabela  # Retorna a lista de jogos gerada

# Função para exibir a tabela de jogos
def exibir_tabela(tabela):
    # Itera sobre a lista de jogos com o índice começando em 1
    for index, partida in enumerate(tabela, 1):
        # Exibe o número do jogo e o confronto entre as duas equipes
        print(f"Jogo {index}: {partida[0]} vs {partida[1]}")

# Exemplo de uso
equipes = ["Turma 3°A", "Turma 3°B", "Turma 2°C", "Turma 2°D", "Turma 1°E", "Turma 1°F"]

# Gerando a tabela de jogos
tabela_jogos = gerar_tabela_de_jogos(equipes)

# Exibindo a tabela de jogos
print("Tabela de Jogos do Interclasse:")
exibir_tabela(tabela_jogos)
