# Faça um programa que use um laço while para somar todos os números de 1 a 99 e exiba o resultado no console.

soma = 0
numero = 1

while numero <= 99:
    soma += numero  # Soma acumulada
    print(f"Somando {numero}, soma parcial: {soma}")  # Exibe o progresso
    numero += 1

print(f"Soma final dos números de 1 a 99: {soma}")
