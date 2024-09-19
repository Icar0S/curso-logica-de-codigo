#principal.py
from modMaths import somar, subtrair
from modLists import encontrar_maximo, encontrar_minimo, calcular_media, ordenar_lista

def main():
 # Usando funções do modulo_matematica
    soma = somar(5, 5)
    subtracao = subtrair(5, 2)
    print("A soma é:", soma)
    print("A subtracao é:", subtracao)

    # Usando funções do modulo_listas
    lista = [10, 20, 30, 40, 50]
    maximo = encontrar_maximo(lista)
    minimo = encontrar_minimo(lista)
    print("Maximo da lista é:", maximo)
    print("Minimo da lista é:", minimo)

    # Usando função ordenar_lista do modulo_listas
    listaDes = [110, 230, 310, 130, 50]
    ordenada = ordenar_lista(listaDes)
    print("A lista ordenada é:", ordenada)

    
    # Chamando a função e imprimindo o resultado
    numeros = [10, 20, 30, 40, 50, 120, 100]
    media = calcular_media(numeros)
    print(f"A média dos números {numeros} é:", media)

if __name__ == "__main__":
    main()