import random
import string

# Função para gerar uma senha aleatória
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Função para verificar se a senha atende aos requisitos mínimos
def verificar_senha(senha):
    if len(senha) < 8:
        return "Senha fraca: deve ter pelo menos 8 caracteres."
    elif not any(char.isdigit() for char in senha):
        return "Senha fraca: deve conter pelo menos um número."
    elif not any(char.isupper() for char in senha):
        return "Senha fraca: deve conter pelo menos uma letra maiúscula."
    elif not any(char.islower() for char in senha):
        return "Senha fraca: deve conter pelo menos uma letra minúscula."
    elif not any(char in string.punctuation for char in senha):
        return "Senha fraca: deve conter pelo menos um caractere especial."
    else:
        return "Senha forte!"

# Gerando uma senha aleatória
tamanho_senha = int(input("Digite o tamanho desejado para a senha (mínimo 8): "))
senha_gerada = gerar_senha(tamanho_senha)

# Verificando a força da senha
resultado_verificacao = verificar_senha(senha_gerada)

# Exibindo a senha e a verificação
print(f"Senha gerada: {senha_gerada}")
print(resultado_verificacao)
