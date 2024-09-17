# Lista de compras: Cada produto é representado por uma tupla (nome, preço unitário, quantidade)
compras = [
    ("Arroz", 20.50, 2),
    ("Feijão", 7.80, 3),
    ("Macarrão", 4.50, 4),
    ("Óleo", 9.30, 2),
    ("Leite", 41.20, 12)
]

# Função para calcular o total das compras
def calcular_total(compras):
    total = 0
    for item in compras:
        nome, preco, quantidade = item  # Desempacotar a tupla
        total += preco * quantidade     # Multiplicar preço pela quantidade e somar ao total
    return total

# Função para aplicar o desconto
def aplicar_desconto(total, limite=200, desconto=0.10):
    if total > limite:
        return total * (1 - desconto)  # Aplica 10% de desconto
    return total

# Calcular o total das compras
total_compras = calcular_total(compras)

# Verificar e aplicar desconto
total_final = aplicar_desconto(total_compras)

# Exibir os resultados
print(f"Total sem desconto: R$ {total_compras:.2f}")
print(f"Total com desconto (se aplicável): R$ {total_final:.2f}")
