# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza operações matemáticas básicas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

divisao = num1 / num2
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro! Não é possível dividir por zero."

potencia = num1**num2
divisao_inteira = num1 // num2
resto_divisao = num1 % num2

# valor = round(subtracao, 2)
# Exibe os resultados formatados
print("\n Resultados:")
print(f"Soma: {soma}")
print("Subtração: ", subtracao)
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}")
print(f"Potência: {potencia}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Resto da divisão: {resto_divisao}")
