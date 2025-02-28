# Crie um programa que declare um dicionário com as seguintes chaves e valores: {"nome": "MARIA", "idade": 22, "cidade": "CAPITAL DO CEARÁ"}
# e exiba o valor associado à chave "idade"


pessoa = {"nome": "MARIA", "idade": 22, "cidade": "CAPITAL DO CEARÁ"}

if "idade" in pessoa:  # Verifica se a chave existe
    print(f"A idade da pessoa é: {pessoa['idade']}")
else:
    print("Chave 'idade' não encontrada no dicionário.")
