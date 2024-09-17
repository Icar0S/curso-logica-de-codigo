# Função para calcular a área de um triângulo usando base e altura
def calcular_area_com_altura(base, altura):
    # Fórmula da área do triângulo
    area = (base * altura) / 2
    return area

# Função principal que executa o algoritmo
def main():
    print("Cálculo da área de um triângulo\n")

    # Solicita a base e a altura do triângulo ao usuário
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))

    # Calcula a área
    area = calcular_area_com_altura(base, altura)
    
    # Exibe o resultado
    print(f"\nA área do triângulo é: {area:.2f}\n")

# Executa o programa
main()
