# Entrada do nível de segurança do cofre (1 a 3)
nivel = int(input("Digite o nível de segurança do cofre (1, 2 ou 3): "))

# Entrada da senha
senha = input("Digite a senha de acesso: ")

# Verificando as condições para cada nível
if nivel == 1:
    if senha == "1234":
        print("Acesso permitido! Você abriu o cofre de nível 1.")
    else:
        print("Senha incorreta! Acesso negado.")

elif nivel == 2:
    if senha == "abcd" or senha == "4321":
        print("Acesso permitido! Você abriu o cofre de nível 2.")
    else:
        print("Senha incorreta! Acesso negado.")

elif nivel == 3:
    if senha == "xYz987" and len(senha) >= 6:
        print("Acesso permitido! Você abriu o cofre de nível 3.")
    else:
        print("Senha incorreta ou não atende aos critérios de segurança!")

else:
    print("Nível inválido! Escolha um nível entre 1 e 3.")
