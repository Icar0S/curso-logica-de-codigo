#Encontrar máximo de lista
def encontrar_maximo(lista):
 maximo = lista[0]
 for numero in lista:
    if numero > maximo:
        maximo = numero
 return maximo

# Chamando a função e imprimindo o resultado
lista = [10, 20, 30, 40, 50]
print(f"O maior número da lista {lista} é {encontrar_maximo(lista)}")