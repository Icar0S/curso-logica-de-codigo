# Criando uma lista
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]


# Filtrando valores
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]


# Transformação e Filtro
cubos = [x**3 for x in range(1, 11) if x > 3]
print(cubos)  # Saída: [64, 125, 216, 343, 512, 729, 1000]

print("=======================================================================")
# =======================================================================
# List Comprehension Aninhada – Criando uma matriz 3x3
matriz = [[j for j in range(3)] for _ in range(3)]
print(matriz)  # Saída: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# A seguinte compreensão de lista transporá linhas e colunas:
[[row[i] for row in matrix] for i in range(4)]

"""o listcomp aninhado é avaliado no 
contexto do [for] que o segue, 
então este exemplo é equivalente a:"""
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
