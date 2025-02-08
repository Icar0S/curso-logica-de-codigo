# Dobrando os valores da lista
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]


# Converter uma lista de números inteiros para strings
numeros_str = list(map(str, numeros))
print(numeros_str)  # ['1', '2', '3', '4', '5']

# Somando duas listas de números inteiros
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = map(lambda x, y: x + y, lista1, lista2)
print(list(resultado))  # Saída: [5, 7, 9]
