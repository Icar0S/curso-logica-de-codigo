idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 60:
    print("Você está em idade ativa para trabalhar.")
elif idade > 60 or idade < 18:
    print("Você está fora da faixa de idade ativa.")
