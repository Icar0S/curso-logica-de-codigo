

nota = float(input("Digite sua nota: "))

if nota >= 8.5 and nota <=10:
    print("Você tirou um A.")
elif nota >= 7.0 and nota <= 8.49:
    print("Você tirou um B.")
elif nota >= 5.5 and nota <= 6.9:
    print("Você tirou um C.")
elif nota < 5.5 and nota >= 0:
    print("Você está reprovado.")
else:
    print("nota errada, valor da nota de 0 a 10")
