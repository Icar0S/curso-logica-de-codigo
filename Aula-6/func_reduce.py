from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [x for x in numeros if x % 2 == 0]
quadrados = list(map(lambda x: x**2, pares))
soma = reduce(lambda x, y: x + y, quadrados)

print(f"Pares: {pares}")
print(f"Quadrados: {quadrados}")
print(f"Soma total: {soma}")


numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # 15
