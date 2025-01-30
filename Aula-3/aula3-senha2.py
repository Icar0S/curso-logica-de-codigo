import random

# Entrada do nível de segurança do cofre (1 a 3)
nivel = int(input("Digite o nível de segurança do cofre (1, 2 ou 3): "))

# Definindo número de tentativas conforme o nível de segurança
if nivel == 1:
    tentativas = 5
elif nivel == 2:
    tentativas = 3
elif nivel == 3:
    tentativas = 1
else:
    print("Nível inválido! Escolha um nível entre 1 e 3.")
    exit()

# Gerando um número aleatório entre 1 e 5 (chave do cofre)
chave_secreta = random.randint(1, 5)

# Loop para permitir tentativas
print(f"\n🔒 Cofre de Nível {nivel} | Você tem {tentativas} tentativa(s).")
for tentativa in range(tentativas):
    chute = int(
        input(
            f"Tentativa {tentativa + 1}/{tentativas} - Digite um número entre 1 e 5: "
        )
    )

    if chute == chave_secreta:
        print("✅ Acesso permitido! Você abriu o cofre!")
        break
    else:
        print("❌ Chave incorreta!")
        if tentativa < tentativas - 1:
            print("🔁 Tente novamente...")
        else:
            print("🚫 Acesso negado! O cofre permanecerá fechado.")
