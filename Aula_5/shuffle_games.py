import random


def embaralhar_lista(lista):
    lista_copy = lista[:]  # cria uma cópia da lista
    random.shuffle(lista_copy)
    return lista_copy


numeros = [1, 2, 3, 4, 5]
numeros_embaralhados = embaralhar_lista(numeros)
print("Lista original:", numeros)
print("Lista embaralhada:", numeros_embaralhados)
