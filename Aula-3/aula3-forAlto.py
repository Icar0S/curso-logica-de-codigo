# Lista de tuplas com o nome e a altura dos alunos
alunos = [("João", 2.75), ("Maria", 1.68), ("Pedro", 1.82), ("Ana", 1.70), ("Carlos", 1.90)]

# Inicializando variáveis para armazenar o aluno mais alto
aluno_mais_alto = alunos[0]
indice_mais_alto = 0

# Percorrendo a lista de alunos para encontrar o mais alto
for i in range(1, len(alunos)):
    if alunos[i][1] > aluno_mais_alto[1]:  # Comparando a altura
        aluno_mais_alto = alunos[i]
        indice_mais_alto = i

# Removendo o aluno mais alto da lista
#alunos.pop(indice_mais_alto)

# Exibindo o nome do aluno mais alto removido e a lista atualizada
print(f"Aluno mais alto é: {aluno_mais_alto[0]} com {aluno_mais_alto[1]}m de altura.")
print("Lista atualizada de alunos:", alunos)