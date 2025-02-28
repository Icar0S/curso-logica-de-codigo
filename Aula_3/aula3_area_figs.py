import math

# Definir a função para calcular as áreas
def calculate_areas(a, b, c):
    # a) 
    triangulo = (a * c) / 2

    # b) 
    circulo = 3.14159 * c ** 2

    # c) 
    trapezio = ((a + b) * c) / 2

    # d) Área do quadrado (lado B)
    quadrado = b ** 2

    # e) Área do retângulo (lados A e B)
    retangulo = a * b

    # Retornando os resultados formatados com 3 casas decimais
    return {
        "TRIANGULO": f"{triangulo:.3f}",
        "CIRCULO": f"{circulo:.3f}",
        "TRAPEZIO": f"{trapezio:.3f}",
        "QUADRADO": f"{quadrado:.3f}",
        "RETANGULO": f"{retangulo:.3f}"
    }

# Lendo os inputs a partir de uma única linha (como valores separados por espaço)
entrada = input().split()

# Convertendo os valores para float
a, b, c = map(float, entrada)

# Aplicando a função para o conjunto de entrada fornecido pelo usuário
result = calculate_areas(a, b, c)

for shape, area in result.items():
    print(f"{shape}: {area}")
