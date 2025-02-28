# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicitar peso e altura ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calculando o IMC
imc = calcular_imc(peso, altura)
categoria = classificar_imc(imc)

# Exibindo o resultado
print(f"Seu IMC é {imc:.2f} e sua categoria é: {categoria}")
