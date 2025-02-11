from functools import reduce

produtos = [
    {"nome": "Caneta", "preco": 1.5, "quantidade": 100},
    {"nome": "Caderno", "preco": 4.0, "quantidade": 50},
    {"nome": "Borracha", "preco": 0.75, "quantidade": 200},
]


# Etapa 1: Calcular o valor total de cada produto usando map
valores_produtos = list(map(lambda p: p["preco"] * p["quantidade"], produtos))
print("Valores individuais dos produtos:", valores_produtos)
# Saída esperada: [150.0, 200.0, 150.0]

# Etapa 2: Somar os valores individuais para obter o total do inventário usando reduce
valor_inventario = reduce(lambda total, valor: total + valor, valores_produtos)
print("Valor total do inventário:", valor_inventario)
# Saída esperada: 500.0
