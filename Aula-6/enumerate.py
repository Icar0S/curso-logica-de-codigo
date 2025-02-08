# Lista
frutas = ["maçã", "banana", "laranja"]

for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

# Definindo um índice inicial diferente
for indice, fruta in enumerate(frutas, start=1):
    print(f"Índice: {indice} - Fruta: {fruta}")


# Convertendo o objeto enumerate em uma lista
# Converte o objeto retornado por enumerate em uma lista de tuplas
lista_enumerada = list(enumerate(frutas))
print(lista_enumerada)
