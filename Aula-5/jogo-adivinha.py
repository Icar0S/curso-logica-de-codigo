import random


def gerar_numero():
    """Gera um número inteiro aleatório entre 1 e 100."""
    return random.randint(1, 100)


def obter_palpite():
    """Solicita ao usuário um palpite e trata possíveis erros de conversão."""
    while True:
        try:
            palpite = int(input("Digite seu palpite (entre 1 e 100): "))
            return palpite
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
        finally:
            print("Tentativa de leitura finalizada.\n")


def verificar_palpite(numero_secreto, palpite):
    """Compara o palpite do usuário com o número secreto e retorna uma dica."""
    if palpite < numero_secreto:
        print("Tente um número maior!")
    elif palpite > numero_secreto:
        print("Tente um número menor!")
    else:
        print("Parabéns! Você acertou!")


def jogo_adivinhacao():
    """Função principal que organiza o jogo de adivinhação."""
    numero_secreto = gerar_numero()
    print("Bem-vindo ao jogo de adivinhação!")
    tentativas = 0

    while True:
        palpite = obter_palpite()
        tentativas += 1

        if palpite == numero_secreto:
            verificar_palpite(numero_secreto, palpite)
            print(f"Você acertou em {tentativas} tentativas!")
            break
        else:
            verificar_palpite(numero_secreto, palpite)

    print("Obrigado por jogar!")


# Garante que o jogo seja executado apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    jogo_adivinhacao()
