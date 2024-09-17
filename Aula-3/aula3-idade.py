idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (H para homem, M para mulher): ").upper()

if genero == 'H':
    if idade >= 18 and idade <= 65:
        print("Você está em idade ativa para trabalhar.")
    elif idade < 18:
        print("Você ainda não atingiu a idade ativa para trabalhar.")
    else:
        print("Você já atingiu a idade de aposentadoria.")
elif genero == 'M':
    if idade >= 18 and idade <= 60:
        print("Você está em idade ativa para trabalhar.")
    elif idade < 18:
        print("Você ainda não atingiu a idade ativa para trabalhar.")
    else:
        print("Você já atingiu a idade de aposentadoria.")
else:
    print("Gênero inválido. Por favor, insira M para homem ou F para mulher.")
