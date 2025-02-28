import random


def escolher_fruta():
    frutas = ["maçã", "banana", "laranja", "uva", "manga"]
    return random.choice(frutas)


fruta = escolher_fruta()
print("Fruta escolhida:", fruta)
