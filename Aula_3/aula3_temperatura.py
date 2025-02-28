temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura > 35:
    print("Está muito quente!")
elif temperatura > 25:
    print("Clima agradável.")
elif temperatura > 15:
    print("Clima ameno.")
else:
    print("Está frio!")
