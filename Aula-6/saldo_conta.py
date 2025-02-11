from functools import reduce


transacoes = [
    {"id": 1, "tipo": "credito", "valor": 1000.0},
    {"id": 2, "tipo": "debito", "valor": 200.0},
    {"id": 3, "tipo": "credito", "valor": 500.0},
    {"id": 4, "tipo": "debito", "valor": 300.0},
]


# Etapa 1: Transformar cada transação em um valor com sinal apropriado usando map
valores = list(
    map(lambda t: t["valor"] if t["tipo"] == "credito" else -t["valor"], transacoes)
)
print("Valores transformados:", valores)
# Saída esperada: [1000.0, -200.0, 500.0, -300.0]


# lambda saldo, valor: saldo + valor
def saldo(a, b):
    return a + b


# Etapa 2: Somar os valores para calcular o saldo final usando reduce
saldo_final = reduce(saldo, valores)
print("Saldo final:", saldo_final)
# Saída esperada: 1000.0
