# Escreva um programa que calcule a frequência de cada caractere em uma string. Por exemplo, na string "bananada",
# o programa deve exibir: {'b': 1, 'a': 4, 'n': 2, 'd': 1}

texto = "bananada"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
    print(
        f"Contagem parcial: {frequencia}"
    )  # Mostra como o dicionário está sendo atualizado

print(f"Frequência final dos caracteres: {frequencia}")
