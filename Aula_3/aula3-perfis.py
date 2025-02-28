# Entrada do usuário: nome e nível de permissão
usuario = input("Digite seu nome de usuário: ")
nivel = (
    input("Digite seu nível de acesso (analista, gerente, administrador): ")
    .strip()
    .lower()
)

# Verificando nível de acesso ao dashboard de Big Data
if nivel == "analista":
    print(f"Bem-vindo, {usuario}! Você pode Visualizar relatórios de dados.")

elif nivel == "gerente":
    print(f"Bem-vindo, {usuario}! Você pode Visualizar e Editar relatórios de dados.")

elif nivel == "administrador":
    print(
        f"Bem-vindo, {usuario}! Você tem acesso total ao sistema, incluindo configurações avançadas."
    )

else:
    print("Erro: Nível de acesso inválido. Contate o administrador do sistema.")
