# Função para adicionar uma nova conexão
def adicionar_conexao(conexoes, nome, profissao, data_conexao):
    conexoes.append({
        "nome": nome,
        "profissao": profissao,
        "data_conexao": data_conexao
    })

# Função para exibir todas as conexões
def exibir_conexoes(conexoes):
    for conexao in conexoes:
        print(f"Nome: {conexao['nome']}, Profissão: {conexao['profissao']}, Data: {conexao['data_conexao']}")

# Exemplo de uso
conexoes = []
adicionar_conexao(conexoes, "Ana Souza", "Desenvolvedora", "10/09/2024")
adicionar_conexao(conexoes, "Carlos Lima", "Engenheiro de Software", "15/09/2024")
adicionar_conexao(conexoes, "Carlos Lima", "Engenheiro de Software", "15/09/2024")

# Exibindo as conexões
print("Minhas Conexões no LinkedIn:")
exibir_conexoes(conexoes)
